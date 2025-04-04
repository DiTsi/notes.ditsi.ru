# ceph

## Commands

```bash
# Main
ceph status
ceph health detail

# OSD
ceph osd tree # see tree of objects
ceph osd df # size of data on OSDs
ceph osd reweight osd.5 0.2 # send data to osd.5 with factor 0.2
ceph osd crush reweight osd.0 0.8 # set store factor 0.8 for osd.0 (moving data)
ceph osd pool ls detail # check replication factor
# OSD Crush
ceph osd crush add-bucket RACK-0 rack
ceph osd crush move RACK-0 datacenter=Australia
ceph osd crush set osd.8 0 host=host-1 # move OSD to host object and set weight 0.0

# Volume
ceph-volume lvm list
ceph-volume lvm prepare --bluestore --data /dev/nvme0n1p2 --crush-device-class nvme # create OSD with specific class
ceph-volume lvm activate 0 faaca5da-ec09-44ab-8ed6-4b4c5a7ddbbd # run OSD 0 with id 0 and fsid faaca5da-ec09-44ab-8ed6-4b4c5a7ddbbd

# PG
ceph pg stat
```

## Scenarios

### Change a Device Class in the CRUSH Map

1. Extract the current CRUSH map

    First, get the current CRUSH map in binary format:
    ```bash
    ceph osd getcrushmap -o crushmap.bin
    ```

2. Convert the CRUSH map to text format:

    Use crushtool to convert the binary CRUSH map to a text format:
    ```bash
    crushtool -d crushmap.bin -o crushmap.txt
    ```

3. Edit the CRUSH map:

    Open the crushmap.txt file in a text editor:
    ```bash
    nano crushmap.txt
    ```

    Find the lines related to osd.6 and osd.7 and change the class from ssd to nvme. For example:
    ```bash
    device 6 osd.6 class nvme
    device 7 osd.7 class nvme
    ```
4. Convert the CRUSH map back to binary format:

    After editing crushmap.txt, convert it back to binary format:
    ```bash
    crushtool -c crushmap.txt -o crushmap_new.bin
    ```

5. Upload the new CRUSH map to Ceph:

    Load the modified CRUSH map into your Ceph cluster:
    ```bash
    ceph osd setcrushmap -i crushmap_new.bin
    ```
6. Verify the changes:

    Make sure the changes were successfully applied by running:

    ```bash
    ceph osd tree
    ```
    You should now see that devices osd.6 and osd.7 have the class nvme.

### Restore keyring

```bash
ceph auth get osd.6 -o /var/lib/ceph/osd/ceph-6/keyring
# or
ceph auth add osd.6 osd 'allow *' mon 'allow profile osd' -o /var/lib/ceph/osd/ceph-6/keyring
```
