#!/usr/bin/env python3

import os
import argparse
# from colorama import Fore, Back, Style
from datetime import datetime


class Directory:
  def __init__(self, path):
    self.path = os.path.join(path, '')
    self.exists = True if os.path.isdir(self.path) else False
    self.isempty = True
    if self.exists:
      if os.listdir(self.path):
        self.isempty = False
    self.length = self.path.count("/")
    self.remove = False
    self.removed = False

  def __str__(self):
    return self.path

  def exists(self):
    return self.exists


class File:
  def __init__(self, path):
    self.path = path
    self.ctime = os.path.getctime(path)
    self.mtime = os.path.getmtime(path)
    self.remove = False
    self.removed = False
    self.age = (datetime.now() - datetime.fromtimestamp(self.mtime)).days # days
  
  def __str__(self):
    return self.path


def directory_not_exists(directories_list):
  if all(i.exists == True for i in directories_list):
    return False
  return True


def dir_len(path):
  return path.count("/")


if __name__ == "__main__":
  parser = argparse.ArgumentParser(add_help=True)
  parser.add_argument('-i', '--ignore', action='store_true', dest='ignore', help='ignore non-existent directories')
  parser.add_argument('-t', '--test', action='store_true', dest='test', help='do nothing, just print logs')
  parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='print full log')
  parser.add_argument('-d', '--days', action='store', dest='days', help='file lifetime (older files will be deleted)', type=int, required=True)
  parser.add_argument('directory', nargs='+', help='directory', type=str)
  args = parser.parse_args()

  dirs_list = args.directory
  directories_list = list()
  directories_list[:] = [Directory(path=dirs_list[i]) for i in range(len(dirs_list))]
  if args.verbose:
    print('Directories to explore:')
    # print(Style.BRIGHT + 'Directories to explore:' + Style.RESET_ALL)
    for d in directories_list:
      print('  {}'.format(d) if d.exists else '  {} (not exists)'.format(d))
      # print('  {}'.format(d) if d.exists else '  {} (format(d)' + Fore.RED + 'not exists' + Style.RESET_ALL + ')')
  if not args.ignore and directory_not_exists(directories_list):
    if args.verbose:
      print('\nError: Process will not start. Use -i flag to ignore non-existsing directories')
      # print('\n' + Fore.RED + Style.BRIGHT + 'Error: Process will not start. Use -i flag to ignore non-existsing directories' + Style.RESET_ALL)
    else:
      print('\nError: Process will not start. Use -v flag to see non-existing directories or -i flag to ignore it')
      # print('\n' + Fore.RED + Style.BRIGHT + 'Error: Process will not start. Use -v flag to see non-existing directories or -i flag to ignore it' + Style.RESET_ALL)

    exit(1)

  folder_list = []
  file_list = []

  # create list of folders and list of files
  for directory in directories_list:
    for dir_, _, files_ in os.walk(str(directory)):
      dir_ = os.path.join(dir_, '')
      folder_list.append(dir_)
      file_list.extend([dir_ + i for i in files_])
  
  folders_objects = []
  files_objects = []

  # create list of Files
  for f in folder_list:
    folders_objects.append(Directory(f))

  for f in file_list:
    files_objects.append(File(f))

  for file in files_objects:
    if file.age > args.days:
      file.remove = True      

  # show files to remove
  if args.verbose and not all(i.remove == False for i in files_objects):
    print('\nFiles to remove:')
    # print(Style.BRIGHT + '\nFiles to remove:' + Style.RESET_ALL)
    for f in files_objects:
      if f.remove == True:
        print('  {} (age: {} days)'.format(f, f.age))
  else:
    print('\nThere are no files older than {} days'.format(args.days))
    exit(0)

  # removing files
  if not args.test:
    if args.verbose:
      print('\nRemoving files...' , end='')
      # print(Style.BRIGHT + '\nRemoving files...' + Style.RESET_ALL, end='')
    for f in files_objects:
      if f.remove == True:
        os.remove(f.path)
        f.removed = True
    if args.verbose:
      print(' [DONE]')
      # print(Style.BRIGHT + ' [DONE]' + Style.RESET_ALL)

  if args.test:
    print('\nTesting mode. Do not specify -t flag to perform removing')
    # print('\n' + Fore.RED + Style.BRIGHT + 'Testing mode. Do not specify -t flag to perform removing' + Style.RESET_ALL)

  exit(0)
