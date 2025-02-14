package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
	"os/user"
	"path"
	"path/filepath"
	"strconv"
	"strings"
	"syscall"
	"time"
)

// DiskUsage ...
type DiskUsage struct {
	stat *syscall.Statfs_t
}

func main() {

	var sourcedir string
	var destdir string
	var movedirs bool
	var listTransfer []string

	flag.StringVar(&sourcedir, "sourcedir", "/home", "Source catalog that contains users' home folders")
	flag.StringVar(&destdir, "destdir", "/data/archive_folders", "Destination catalog")
	flag.BoolVar(&movedirs, "movedirs", false, "Move all users' home directories to archive")
	flag.Parse()

	sourcedir = "1/" //!
	destdir = "/tmp" //!

	listTransfer = FindFiredUsers(sourcedir)

	// check list is empty
	if len(listTransfer) == 0 {
		fmt.Println("There are no user folders to move")
		os.Exit(0)
	}

	fmt.Println("User folders to move:")
	var totalSize int64 = 0
	for _, src := range listTransfer {
		var dirSize int64
		var stat os.FileInfo

		dirSize, _ = DirSize(src)
		stat, _ = os.Stat(src)

		fmt.Printf("  %-11s  [%s]   %s\n", ByteCountSI(dirSize), stat.ModTime().Format(time.ANSIC), src)

		totalSize += dirSize
	}

	fmt.Printf("Total size: %s\n", ByteCountSI(totalSize))

	// fmt.Printf(ByteCountSI()

	if movedirs == true {
		if totalSize < NewDiskUsage(destdir).Available() {
			fmt.Printf("\nMoving folders to %s:\n", destdir)
			os.Mkdir(destdir, 0770)

			var totalMoved int64 = 0
			for _, src := range listTransfer {
				var size int64
				size, _ = DirSize(src)

				if err := MoveDir(src, destdir); err == nil {
					fmt.Printf("  %s  [DONE]\n", src)
					totalMoved += size
				} else {
					fmt.Printf("  %s  [%s]\n", src, err)
				}
			}
			fmt.Printf("Moved %s of data\n", ByteCountSI(totalMoved))
		} else {
			fmt.Printf("\nNot enough free space on %s: %s\n", destdir, ByteCountSI(NewDiskUsage(destdir).Available()))
		}
	} else {
		fmt.Printf("\nUse --movedirs=true to archive directories\n")
	}
}

// FindFiredUsers - функция для поиска пользователей, у которых удален профиль на сервере.
// Возвращает массив из путей к home каталогу. Если это симлинк, возвращает настоящий путь
func FindFiredUsers(homedir string) []string {
	var FiredUsers []string

	fileInfos, err := ioutil.ReadDir(homedir)
	if err != nil {
		fmt.Println("Error in accessing directory:", err)
	}

	for _, file := range fileInfos {
		var UID int
		var pathToCheck string

		pathToCheck, _ = filepath.Abs(filepath.Join(homedir, file.Name()))
		infoSymLink, _ := os.Lstat(pathToCheck)

		if infoSymLink.Mode()&os.ModeSymlink == os.ModeSymlink {
			realpath, _ := os.Readlink(pathToCheck)
			pathToCheck = realpath
		}

		info, _ := os.Stat(pathToCheck)

		if stat, ok := info.Sys().(*syscall.Stat_t); ok {
			UID = int(stat.Uid)
		}

		_, error := user.LookupId(strconv.Itoa(UID))
		if error != nil {
			FiredUsers = append(FiredUsers, pathToCheck)
		}
	}
	return FiredUsers
}

// DirSize - для подсчета размера каталога пользователя [bytes]
func DirSize(path string) (int64, error) {
	var size int64
	err := filepath.Walk(path, func(_ string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			size += info.Size()
		}
		return err
	})
	return size, err
}

// NewDiskUsage ...
func NewDiskUsage(volumePath string) *DiskUsage {
	var stat syscall.Statfs_t
	syscall.Statfs(volumePath, &stat)
	return &DiskUsage{&stat}
}

// Available функция для подсчета доступного места в килобайтах на разделе, куда планируется переносить каталог
func (d *DiskUsage) Available() int64 {
	return int64(d.stat.Bavail * uint64(d.stat.Bsize))
}

// ByteCountSI returns prettify size text
func ByteCountSI(b int64) string {
	const unit = 1000
	if b < unit {
		return fmt.Sprintf("%d B", b)
	}
	div, exp := int64(unit), 0
	for n := b / unit; n >= unit; n /= unit {
		div *= unit
		exp++
	}
	return fmt.Sprintf("%.1f %cB",
		float64(b)/float64(div), "kMGTPE"[exp])
}

//MoveDir функция переноса каталога. Создает в расположении одноименный каталог пользователя и рекурсивно переносит содержимое папки пользователя. Исходная папка удаляется.
func MoveDir(src string, dst string) error {
	var err error
	var fds []os.FileInfo
	var srcinfo os.FileInfo

	var pathsplit = strings.Split(src, "/")
	var foldername = pathsplit[len(pathsplit)-1]

	err = os.Mkdir(path.Join(dst, foldername), 0770)
	if err != nil {
		return err
	}

	if srcinfo, err = os.Stat(src); err != nil {
		return err
	}

	if err = os.MkdirAll(dst, srcinfo.Mode()); err != nil {
		return err
	}

	if fds, err = ioutil.ReadDir(src); err != nil {
		return err
	}
	for _, fd := range fds {
		srcfp := path.Join(src, fd.Name())
		dstfp := path.Join(dst, foldername, fd.Name())
		if err = os.Rename(srcfp, dstfp); err != nil {
			fmt.Println(err)
		}
	}

	if err == nil {
		err := os.Remove(src)
		if err != nil {
			fmt.Println(err)
		}
	}

	return err
}
