# bareos

## Проблемы

### Read before installation
The dbaddress must be specified in the `catalog/MyCatalog.conf` file. Bareos itself does not do this, and then, like an idiot, reports that the password to the database is incorrect

## Server Installation

Process described [here](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareos.html)

Main steps:

- Run script to add repos and install
- Configure postgresql database with [scripts](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareos.html#postgresql)
- Start the [daemons](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareos.html#postgresql)

Web UI:

- [Install bareos-webui](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareosWebui.html#install-the-bareos-webui-package)
- [Configure Apache](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareosWebui.html#configure-your-apache-webserver)
- go to [http://localhost/bareos-webui](http://localhost/bareos-webui)
- [create config file](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareosWebui.html#create-a-restricted-consoles) with template and change it
- restart Director: `service bareos-dir restart`

### add S3 backend

To add new S3 bucket as backend you must add two files:

- /etc/bareos/bareos-sd.d/device/S3\_device.conf
- /etc/bareos/bareos-dir.d/storageS3\_storage.conf

### add client

**run bconsole**

```bash
configure add client name=gitlab address=<ip> password="<password>"
```

copy content of file

```bash
cat /etc/bareos/bareos-dir-export/client/<client>/bareos-fd.d/director/bareos-dir.conf
```

create file on client side and paste content from clipboard

```bash
vim /etc/bareos/bareos-fd.d/director/bareos-dir.conf
```

### add job

bconsole command

```bash
configure add job name=<name> client=<client> jobdefs=DefaultJob
```

## Backup Configuration

### Server side

**run `bconsole` and execute**

```bash
configure add client name=qwerty address=192.168.0.2 password=SOME_PASSWORD
```

export configuration and copy to clipboard

```bash
configure export client=qwerty
```

### Client side

replace configuration in `/etc/bareos/bareos-fd.d/director/bareos-dir.conf` with your clipboard

```bash
systemctl restart bareos-filedaemon
```

## Jobs

**[good tutorial](https://www.svennd.be/create-a-backup-job-on-bareos/)**

## Cleanup

#### Cleanup of unnecessary job and files

```bash
bconsole
  delete yes jobid=189
  
rm /data/bareos/Job-1000
```

#### Cleanup job

[link](https://www.bacula.lat/truncate-bacula-volumes-to-free-disk-space/?lang=en)

```JSON
Job {
  ...
  Type=Admin
  RunScript {
    Console = "prune expired volume yes"
    Console = "truncate pool=Diaria storage=File1"
    # or Console = "purge volume action=truncate allpools storage=File1"
    RunsWhen = Before
    RunsOnFailure = yes
    RunsOnClient = no
  }
}
```

#### purge unused volumes

```bash
echo purge volume=Full-0{107..121..1} | bconsole
```

#### remove unused volumes

```bash
rm Full-0{107..121..1}
```

## Concurrent jobs

[link](https://www.svennd.be/concurrent-jobs-in-bareos-with-disk-storage/)

#### Add same devices with new names

```bash
# /etc/bareos/bareos-sd.d/device/FileStorage.conf

Device {
  Name = FileStorage1
  Media Type = File
  Archive Device = /storage/block
  LabelMedia = yes;
  Random Access = yes;
  AutomaticMount = yes;
  RemovableMedia = no;
  AlwaysOpen = no;
  Description = "File device. A connecting Director must have the same Name and MediaType."
}

Device {
  Name = FileStorage2
  Media Type = File
  Archive Device = /storage/block
  ...
}

Device {
  Name = FileStorage3
  Media Type = File
  Archive Device = /storage/block
  ...
}
```

#### Add devices to director

```bash
# /etc/bareos/bareos-dir.d/storage/File.conf

Storage {
  Name = File
  Address = bareos
  Password = "password"
  Device = FileStorage3
  Device = FileStorage1
  Device = FileStorage2
  Media Type = File
  Maximum Concurrent Jobs = 10
}
```

#### Restart bareos

<p class="callout info">reload in bconsole is not enough</p>

```bash
systemctl restart bareos-sd bareos-dir bareos-fd
```