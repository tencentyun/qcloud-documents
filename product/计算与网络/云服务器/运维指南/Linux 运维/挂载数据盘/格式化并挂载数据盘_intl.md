>**Note:**
>- After formatting, all the data in the data disk will be cleared. Before formatting, make sure there is no data in the data disk or important data has been backed up. To avoid service exceptions, ensure that the CVM has stopped external services before formatting.

## Manual Formatting and Mounting Data Disk
Format and mount a data disk by following the steps below.

>**Note:**
>- When executing the following commands, remember to modify the data disk drive letter. The drive letter is `vdb` in this example.

### Step 1: Format the data disk

>**Note:**
> When formatting partitions, developers can decide the file system format on their own, such as `ext3` and `ext4`. `ext4` is used in this example.

Format the data disk by performing the mkfs command:
```
mkfs.ext4 /dev/vdb
```

### Step 2: Mount the data disk
1. Create a mount point - data directory:
```
mkdir /data
```

2. Mount new partitions:
```
mount /dev/vdb /data
```

3. Verify whether the data disk is mounted successfully:
```
df -h
```
The following message indicates that it is mounted successfully (i.e. the data disk is mounted on the Linux CVM):
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/vdb        50G  53M   47G   1% /data
```

### Step 3: Enable auto mount upon launch
Add the data disk mount information to `/etc/fstab` to enable auto mount upon launch.

To allow your CVM to be automatically mounted with data disk when it is restarted or launched, add the mount information to `/etc/fstab`. Otherwise, the data disk cannot be automatically mounted to the CVM when the CVM is restarted or launched.

1. Execute the following command to add partition information:
```
echo '/dev/vdb /data ext4 defaults 0 0' >> /etc/fstab
```
2. Execute the following command to view the partition information:
```
cat /etc/fstab
```
The following message indicates that the data disk mount information is added successfully.
```
/dev/vdb /data ext4 defaults 0 0
```

## Auto Formatting and Mounting Data Disk
You can format and mount a data disk on Tencent Cloud Linux CVM by running the following Shell script:
```
#!/bin/bash
type=ext4
mount_dir=/data
mkfs.$type /dev/vdb 
mkdir -p $mount_dir
echo "/dev/vdb $mount_dir $type defaults 0 0" >> /etc/fstab
mount -a
```

