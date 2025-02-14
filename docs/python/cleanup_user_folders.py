#!/usr/bin/env python3

import os
import argparse
from datetime import datetime
import shutil
import time
import psutil


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class Directory:
  def __init__(self, path):
    self.path = os.path.join(path, '')
    self.exists = True if os.path.isdir(self.path) else False
    self.isempty = True
    if self.exists:
      if os.listdir(self.path):
        self.isempty = False
    self.remove = False
    if self.exists:
      self.remove = True
    self.size = 0
    if self.exists:
      self.last_modify = os.path.getmtime(path)
      total_size = 0
      for dirpath, _, filenames in os.walk(self.path):
          for f in filenames:
              fp = os.path.join(dirpath, f)
              if not os.path.islink(fp):
                  total_size += os.path.getsize(fp)
      self.size = total_size
      
  def __str__(self):
    return self.path


# home_path = "/home/ditsi/temp/2020.10.22"
home_path = "/home"


if __name__ == "__main__":
  parser = argparse.ArgumentParser(add_help=True)
  parser.add_argument('-t', '--test', action='store_true', dest='test', help='do nothing, just print report')
  parser.add_argument('-d', '--dest', action='store', dest='dest', help='dest directory for user folders', required=True)
  parser.add_argument('user_list', help='user_list.txt file', type=str)
  args = parser.parse_args()

  users_file = args.user_list
  users_list = list()
  with open(users_file, "r") as f:
      users_list = f.read().splitlines()

  directories_list = list()
  directories_list[:] = [Directory(path=home_path + '/' + users_list[i]) for i in range(len(users_list))]

  if all(i.remove == False for i in directories_list):
    print('There are no user folders to move')
    exit(0)

  # Log
  total_bytes = 0
  print('User folders to move:')
  for i in directories_list:
    if i.remove:
      print('  {:8s}   [{}]   {}'.format(sizeof_fmt(i.size), time.strftime('%Y.%m.%d__%H:%M:%S', time.localtime(i.last_modify)), i))
      total_bytes += i.size
  print('\n  Total size: {}'.format(sizeof_fmt(total_bytes)))
  
  # Removing
  if args.test:
    print('\nTesting mode. Do not specify -t flag to perform removing')
    exit(0)
  else:
    # try to create destination directory
    if not os.path.isdir(args.dest):
      os.makedirs(args.dest)

    # check destination free space
    destdisk = psutil.disk_usage(args.dest)
    if total_bytes > destdisk.free:
      print('\nFree space on {}: {}'.format(args.dest, sizeof_fmt(destdisk.free)))
      print('But you need {}'.format(sizeof_fmt(total_bytes)))
      print('Nothing was done. Exiting')
      exit(0)

    total_bytes = 0
    print('\nMoving folders to {}:'.format(args.dest))
    for i in directories_list:
      if i.remove:
        print('  {}'.format(i), end='')
        try:
          shutil.move(i.path, args.dest)
        except Exception:
          print('  [FAILED]')
          continue
        print('  [DONE]')
        total_bytes += i.size
    print('\n  Moved {} of data'.format(sizeof_fmt(total_bytes)))
  exit(0)
