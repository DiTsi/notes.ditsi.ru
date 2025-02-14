# Scripts

## Example

```
:foreach gre in=$greList do={
  :local oldStatus
  :local newStatus
  :set newStatus [/interface gre get $gre running]
  :set oldStatus ($greListStatus->$gre)
  :if ($oldStatus != $newStatus) do={
    /tool e-mail send to=it_alerts@test.com subject="Mikrotik Moscow" body="gre: $gre\nStatus: $newStatus"
    :set ($greListStatus->$gre) $newStatus 
  }
}
```