# DFS

## Commands

```Powershell
# show list of sheduled files
Get-DfsrState -ComputerName "COMP1" # type on NOT COMP1 machine!

# show replication state
Get-DfsReplicationGroup -Groupname "ditsi.ru\groupname"

DfsDiag.exe /TestDFSConfig /DFSRoot:\\site.com\share

# force sync
Sync-DfsReplicationGroup -GroupName "site.com\share" -SourceComputerName "fs1" -DestinationComputerName "fs2" -DurationInMinutes 5 -Verbose
```