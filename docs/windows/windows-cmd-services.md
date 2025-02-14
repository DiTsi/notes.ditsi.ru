# windows cmd services

```shell
devmgmt.msc - Devices management

services.msc - Services

net use - Show mounted network devices

# recurse change file owner (run with admin privileges)
takeown /f "c:\folder\subfolder" /r

taskmgr.exe - Task Manager

# Show uptime
net statistics server

# Run service
net start metricbeat

# Create symbolic link
mklink /D link_path target_path

# Long path copy
robocopy.exe src dst /E /B
Robocopy.exe "f:\folder1\folder2" "e:\folder1\folder2" /B /E /copy:DATSO /dcopy:DAT
# remove (delete) folder files
Robocopy /mir 'empty_folder' 'your_folder'

# Show remote RDP users
Query User

# curl
Invoke-WebRequest -Uri https://google.com/ | Select-Object -ExpandProperty Content
```