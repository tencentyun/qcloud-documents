Cloud disk is an expandable storage device on cloud. When a cloud disk is created, you can expand its capacity at any time to increase its storage space without losing any data on it. To expand the cloud disk and use the expanded capacity, in addition to [expanding physical cloud disk](/doc/product/362/5747), you need to expand the file system on it to identify the new available space. You can follow the steps below:

1) [Expanding physical cloud disk](/doc/product/362/5747)

2) Expanding the partition

- Determine the partition table format of file system
- Expanding the partition

3) Expanding the file system


## Checking the file system size
After the expansion of physical cloud disk, you can check the file system size to see whether the instance identifies a larger cloud disk space. On Linux system, you can use the command `df -h` to check the file system size.

If you find that the cloud disk size does not become the expanded value, you need to expand the file system so that the instance can use the new space.

## Confirming the partition table format
Use the following command to check the partition table format used by the cloud disk before its expansion:

```
fdisk -l
```

If you get the results as shown in the following two figures (the results vary slightly with operating systems), you can conclude that the CVM has a GPT partition format before the expansion. For the information on subsequent operations, refer to "Guide on Partition Modification After Expansion of Cloud Disk with a GPT Partition Format".
![](//mccdn.qcloud.com/static/img/972969e3db92b65311211734690fe763/image.png)
![](//mccdn.qcloud.com/static/img/2c1f4a40279d211a7b81bada7ed38280/image.png)

If you get the results as shown in the following figure (the results vary slightly with operating systems), you can conclude that the CVM has an MBR partition format before the expansion. For the information on subsequent operations, refer to "Guide on Partition Modification After Expansion of Cloud Disk with an MBR Partition Format".
![](//mccdn.qcloud.com/static/img/4d789ec2865a2895305f47f0513d4e2b/image.png)

## Guide on Partition Modification After Expansion of Cloud Disk with a GPT Partition Format
### Formatting the new disk space as a separate GPT partition
#### Viewing data disk information
Execute the command `parted disk path print` to verify the capacity change of the cloud disk. If during the process you get the following prompt, enter `Fix`:

![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)
The expanded cloud disk has a size of 107GB, with the size of existing partition being 10.7GB.

#### Unmounting the mounted data disk
Execute the following command to verify whether the cloud disk still has a mounted partition:

```
mount | grep 'Disk path' 
```
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
The cloud disk has a partition (vdb1) mounted on /data, which needs to be unmounted.

Use the following command to unmount the partition:

```
umount Mount point
```

In this example, execute `umount /data` to unmount the partition.

> Note: To unmount the file systems of all the partitions of the cloud disk (such as vdb1, vdb2...),

please use the command `mount | grep '/dev/vdb' ` to verify that the file systems of all the partitions on the cloud disk have been unmounted.

![](//mccdn.qcloud.com/static/img/a2f6db45a94485785ea15e6ea950bcb8/image.png)

#### Data disk partitioning 
After confirming that all partitions of the cloud disk have been unmounted, execute the following command to create a new partition:

```
parted Disk path
```
Enter `parted /dev/vdb`.

Next, enter `print` to view the partition information, record the End value of the existing partition, and use it as the starting offset value for the next partition:
![](//mccdn.qcloud.com/static/img/788ce125bba952f204ed6ee36dfb644d/image.png)

Then execute the following command to create a new primary partition. This partition starts with the end of the existing partition, covering all the new space of the disk. :

```
mkpart primary start end
```

In this example, use `mkpart primary 10.7GB 100%`

Execute `print` again and you'll find that the new partition has been created successfully. Enter `quit` to exit the parted tool:
![](//mccdn.qcloud.com/static/img/fc54fd4c05102ee91c648526d77d1b42/image.png)

#### Formatting the new partition
Execute the following command to format the new partition mentioned above. You can decide the file system format yourself, such as ext2, ext3.

```
mkfs.[fstype] [Partition path] 
```
Use the command `mkfs.ext3 /dev/vdb2` to format the new partition. The file system is ext3. 


### Adding the new space to the existing partition (GPT partition format)
#### Viewing data disk information
Execute the command `parted disk path print` to verify the capacity change of the cloud disk. If during the process you get the following prompt, enter `Fix`:

![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)
The expanded cloud disk has a size of 107GB, with the size of existing partition being 10.7GB.

#### Unmounting the mounted data disk
Execute the following command to verify whether the cloud disk still has a mounted partition:

```
mount | grep 'Disk path' 
```
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
The cloud disk has a partition (vdb1) mounted on /data, which needs to be unmounted.

Use the following command to unmount the partition:

```
umount Mount point
```

In this example, execute `umount /data` to unmount the partition.

> Note: To unmount the file systems of all the partitions of the cloud disk (such as vdb1, vdb2...),

please use the command `mount | grep '/dev/vdb' ` to verify that the file systems of all the partitions on the cloud disk have been unmounted.

![](//mccdn.qcloud.com/static/img/a2f6db45a94485785ea15e6ea950bcb8/image.png)

#### Data disk partitioning  
After confirming that all partitions of the cloud disk have been unmounted, execute the following command to delete the old partition and create a new partition with the same starting offset value:

```
parted [Disk path]
```

Then enter `unit s` to change the unit for display and operation to sector (default to GB). Then enter `print` to view the partition information, and record the Start value of the existing partition. After the deletion of the old partition and creation of new partition, the Start value of the new partition must be same as that of the old one, otherwise the data will be lost.
![](//mccdn.qcloud.com/static/img/67ba54c1d9d63c307d4b8a157b70c722/image.png)

Execute the following command to delete the old partition:

```
rm [Partition Number]
```

As shown in the above figure, there is a partition with the Number of "1" on the cloud disk. After the execution of `rm 1', you'll get the result as shown below:
![](//mccdn.qcloud.com/static/img/3384eeada87ce75695e0e55125109eff/image.png)

Enter `mkpart primary [staring sector of old partition] 100%` to create a new primary partition. In this example, use `mkpart primary 2048s 100%`. This primary partition starts with the 2048th sector (this must be consistent with the partition before deletion), and 100% indicates that this partition extends to the end of the disk.

In case of the status as shown in the figure, please enter Ignore:
![](//mccdn.qcloud.com/static/img/c45966e20dc856817c65fd6b81155e4a/image.png)

Execute `print` again and you'll find the new partition has been created successfully. Enter `quit` to exit the parted tool:
![](//mccdn.qcloud.com/static/img/cb1af5adaf6c89d066077c43fd428a38/image.png)

#### Check the file system of the partition after expansion
Use the following command to check the partition after expansion:

```
e2fsck -f Partition path
```
In the previous steps, Partition 1 has been created. Execute the command `e2fsck -f /dev/vdb1`. The result is as follows:
![](//mccdn.qcloud.com/static/img/307f7a0c98eea05ca1d4560fe4e96f57/image.png)

#### Expand the file system
Execute the following command to expand the file system on the partition:

```
resize2fs Partition path
```
![](//mccdn.qcloud.com/static/img/57d66da9b5020324703498dbef0b12f9/image.png)

#### Mounting new partition
Execute the following command to mount the partition:

```
mount Partition path Mount point
```

Use the command `mount/dev/vdb1/data` to manually mount the new partition, and use `df-h` to make a check. The appearance of the following message indicates that the mounting has been completed successfully and you can view the data disk.
! [](// mccdn.qcloud.com/static/img/a2bd04c79e8383745689e19033a0daaa/image.png)

## Guide on Partition Modification After Expansion of Cloud Disk with a MBR Partition Format.
After the expansion of cloud disk with a MBR partition format, you can choose to:
- Build the new capacity space into a separate new partition without changing the existing partition
- Expand the existing partition to a new capacity value (including the scenario where formatting is performed without partitioning), and leave the data of existing partition unchanged.

In both of the above two scenarios, after the upgrade of the cloud disk on Linux CVM, you can execute a series of commands with the partition expanding tool under Linux (fdisk/e2fsck/resize2fs) to complete the expansion of partition while ensuring the existing data will not be lost. Please note that whether you want to add a new partition or to expand the existing partition, it is necessary to unmount the mounted partition before expansion, so that the kernel can identify the new partition table.

Due to the limitations of MBR, please ensure the size of any partition does not exceed 2TB in either of the two cases (If the expanded space is greater than 2TB, the second option is not allowed).

### Formatting the new disk space to a separate partition
#### Viewing data disk information
Execute the command `df-h` to view the partition information of the mounted data disk, and the command `fdisk -l` to view the information of the expanded data disk before partitioning:
![](//mccdn.qcloud.com/static/img/0a450dfaa9cfc7b2c7fdc04861f0e754/image.png)
![](//mccdn.qcloud.com/static/img/594671a1215dee3036b7940892438f62/image.png)

#### Unmounting all the mounted partitions
Execute the following command to unmount all the mounted partitions:

```
umount Mount point
```

Execute the command `unmount /data` to unmount all the mounted partitions.

#### Data disk partitioning
After confirming that all partitions of the cloud disk have been unmounted, execute the following command to create a new partition:

```
fdisk [Disk path]
```
In this example, use the command `fdisk /dev/xvdc`. As prompted in the interface, enter "p" (check the existing partition information), "n" (create a new partition), "p" (create a primary partition), and "2" (create the second primary partition) in turn, press Enter twice (use default settings), and then enter "w" (save partition table) to start partitioning:
![](//mccdn.qcloud.com/static/img/8c35d6f4dfb367e74edc27ce6822c317/image.png)
Here you'll create one partition. You can create multiple partitions as required.

#### Checking new partition
Use the following command to check the new partition.

```
fdisk -l
```

![](//mccdn.qcloud.com/static/img/e04e924d62317bc2c605c8abaac394f5/image.png)
The new partition xvdc2 has been created.

#### Formatting the new partition and creating the file system
When formatting a partition, you can decide the file system format yourself, such as ext2, ext3 and so on. Here "ext3" is taken as an example. Use the command `mkfs.ext3 /dev/xvdc2` to format the new partition. 

![](//mccdn.qcloud.com/static/img/074e23eaa580495f96fb532b688d2d68/image.png)

#### Mounting new partition
Use the following command to create a new mount point:

```
mkdir New mount point
```
Execute the following command to mount the new partition on the new mount point:

```
mount New partition path New mount point
```

Use the command `mkdir /data1` to create data1 directory. Then use the command `mount /dev/xvdc2 /data1` to manually mount the new partition, and use the` df-h` to make a check. The appearance of the following message indicates that the mounting has been successfully completed and you can view the data disk:.
![](//mccdn.qcloud.com/static/img/7b749a4bb6e7c8267c9354e1590c35d4/image.png)

#### Adding new partition information
If you want the data disk to be automatically mounted to CVM when CVM is restarted or booted, you need to add the partition information to /etc/fstab. If you do not do so, the data disk will not be automatically mounted to the CVM when the CVM is restarted or booted.

Execute the following command to add information:
`echo '/dev/xvdc2 /data1 ext3 defaults 0 0' >> /etc/fstab`

Execute the command `cat /etc/fstab` to make a check, and the appearance of the following message indicates the partition information has been successfully added:
![](//mccdn.qcloud.com/static/img/f0b5c14bf08fd3629ddf6d9b1ae01ffc/image.png)

### Adding new space to the existing partition
If the old disk partition is an MBR partition (with identifier like vdb1, vdc1 and so on), and a file system has been created on this partition; Or if the old disk has not been partitioned and a file system has been directly created on this disk: In both of the above cases, you can choose to use the automatic expansion tool for expansion.

The automatic expansion tool is suitable for Linux system, used to add the new space of cloud disk to the existing file system. The following three conditions must be met to ensure the success of expansion:
- The file system is ext2/ext3/ext4
- No error occurs with the current file system
- The disk size after expansion does not exceed 2TB

The following describes how to use the automatic expansion tool.

#### Uninstalling the disk partition which is in use
Execute the following command to unmount the partition:

```
umount Mount point
```

![](//mccdn.qcloud.com/static/img/c0acc05057941681627a5fd34979d194/image.jpg)

#### Downloading the one-click expansion tool
Execute the following command to download the tool:

```
wget -O /tmp/devresize.py https://raw.githubusercontent.com/tencentyun/tencentcloud-cbs-tools/master/devresize/devresize.py
```

#### Executing the expansion tool
Execute the following command:
```
python /tmp/devresize.py Disk path
```
Please note that the disk path points to the cloud disk to be expanded, rather than the partition name. If your file system is on vdb1, execute `python /tmp/devresize.py  /dev/vdb`

![](//mccdn.qcloud.com/static/img/c7617b90578192d64d19f02325f00ffb/image.jpg)

The output of "The file system on /dev/vdb1 is now XXXXX blocks long." indicates the expansion has been successfully completed.

If the output shows "[ERROR] - e2fsck failed!!", you may need to repair the partition of your file system by the following command:

```
fsck Partition path
```

Notice that this command is different from the above. The partition path refers to your partition which contains the your file system. If your file system is on vdb1, execute `fsck /dev/vdb1`.

Once the repair finishes, you can continue to execute the expansion tool with command `python /tmp/devresize.py Disk path`.

#### Remounting the expanded partition
Execute the following command to mount the expanded partition:
```
mount Partition path Mount point
```

Execute the commands to check the partition capacity after expansion:
```
df -h
```

Use the command `mount /dev/ vdb1 /data` to manually mount the expanded partition (if no partition exists previously, execute `mount /dev/vdb /data`), and use the command ` df-h` to make a check. The appearance of the following message indicates that the mounting has been completed successfully and you can view the data disk:

![](//mccdn.qcloud.com/static/img/2367f3e70cd0c3c1bef665cc47c1c3bc/image.jpg)
Then execute the command `ll /data` and you can find that after the expansion the data on the old partition is not lost, and the new space has been added to the file system.
