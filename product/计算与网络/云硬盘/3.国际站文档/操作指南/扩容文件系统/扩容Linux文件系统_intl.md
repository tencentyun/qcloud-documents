Cloud disk is an expandable storage device on cloud. When a cloud disk is created, you can expand its capacity at any time to increase its storage space without losing any data on it. To expand the capacity for use, you need to [expand physical cloud disk](/doc/product/362/5747) and file system on it to identify new available space. You can follow the steps below:

1) [Expand Physical Cloud Disk](/doc/product/362/5747)

2) Expand partition

- Determine the format of file system partition table
- Expand partition

3) Expand file system


## Checking the Size of File System
After expanding the physical cloud disk, you can check whether the instance identifies a larger cloud disk space by checking the size of the file system. On Linux, you can check the size of file system using command `df -h`.

If the size of the cloud disk does not increase to the expanded value, expand the file system so that the instance can use the expanded space.

## Confirming the Format of Partition Table
Use the following command to confirm the format of partition table used by the cloud disk before capacity expansion:

```
fdisk -l
```

If the result is displayed as shown in either of the following two figures (depending on the OS), the GPT partition mode is used before the CVM expansion. For the subsequent operations, please see Guidelines on Modifying Partition after Expanding the GPT Partition Cloud Disk.
![](//mccdn.qcloud.com/static/img/972969e3db92b65311211734690fe763/image.png)
![](//mccdn.qcloud.com/static/img/2c1f4a40279d211a7b81bada7ed38280/image.png)

If the result is displayed as shown in the following figure (depending on the OS), the MBR partition mode is used before the CVM expansion. For the subsequent operations, please see Guidelines on Modifying Partition after Expanding the MBR Partition Cloud Disk.
![](//mccdn.qcloud.com/static/img/4d789ec2865a2895305f47f0513d4e2b/image.png)

## Guidelines on Modifying Partition after Expanding the GPT Partition Cloud Disk
### Formatting New Space as an Independent GPT Partition
#### Viewing Data Disk Information
Run the command `parted disk path print` to check the capacity change of the cloud disk. Enter `Fix` when receiving the following prompt:

![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)
As shown in the figure above, the size of expanded cloud disk is 107 GB and the size of existing partition is 10.7 GB.

#### Unmounting the mounted data disk
Run the following command to check whether the cloud disk has partitions mounted:

```
mount | grep 'Disk path' 
```
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
As shown in the figure above, there is a partition (vdb1) on the cloud disk mounted on /data, which needs to be unmounted.

Unmount it using the following command:

```
umount  Mount point
```

In this example, run `umount /data` to unmount the partition.

> Note: Unmount the file system in all partitions of the cloud disk, such as vdb1, vdb2...

Use command `mount | grep '/dev/vdb' again to confirm that all partitions on this disk have been unmounted.

![](//mccdn.qcloud.com/static/img/a2f6db45a94485785ea15e6ea950bcb8/image.png)

#### Data Disk Partition 
After confirming that all the partitions of the cloud disk have been unmounted, run the following command to create a partition:

```
parted Disk path
```
Here enter `parted /dev/vdb`.

Then enter `print` to view the partition information. Remember the End value of the existing partition, which is the starting offset of the next partition:
![](//mccdn.qcloud.com/static/img/788ce125bba952f204ed6ee36dfb644d/image.png)

Then run the following command to create a primary partition. This partition starts at the end of the existing partition, and cover all the expanded space on the disk. :

```
mkpart primary start end
```

In this example, use `mkpart primary 10.7GB 100%`

Run `print` again, and you can find that the new partition has been created successfully. Type `quit` to exit the parted tool:
![](//mccdn.qcloud.com/static/img/fc54fd4c05102ee91c648526d77d1b42/image.png)

#### Formatting New Partition
Run the following command to format the new partition above. You can decide the format of the file system, such as ext2 and ext3.

```
mkfs.[fstype] [Partition path] 
```
Here the new partition is formatted using the command `mkfs.ext3 /dev/vdb2`, and the file system is EXT3. 


### Adding New Space to Existing Partition (GPT Partition Format)
#### Viewing Data Disk Information
Run the command `parted disk path print` to check the capacity change of the cloud disk. Enter `Fix` when receiving the following prompt:

![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)
As shown in the figure above, the size of expanded cloud disk is 107 GB and the size of existing partition is 10.7 GB.

#### Unmounting the mounted data disk
Run the following command to check whether the cloud disk has partitions mounted:

```
mount | grep 'Disk path' 
```
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
As shown in the figure above, there is a partition (vdb1) on the cloud disk mounted on /data, which needs to be unmounted.

Unmount it using the following command:

```
umount  Mount point
```

In this example, run `umount /data` to unmount the partition.

> Note: Unmount the file system in all partitions of the cloud disk, such as vdb1, vdb2...

Use command `mount | grep '/dev/vdb' again to confirm that all partitions on this disk have been unmounted.

![](//mccdn.qcloud.com/static/img/a2f6db45a94485785ea15e6ea950bcb8/image.png)

#### Data Disk Partition 
After confirming that all the partitions of the cloud disk have been unmounted, run the following command to delete the original partition, and create a partition with the same starting offset:

```
parted [Disk path]
```

Next, enter `unit s` to change the display and control units to sector (GB by default). Enter `print` to view the partition information, and remember the Start value of the existing partition. For the partition created after deleting the original one, the Start value must be the same as this value, otherwise the data will be lost.
![](//mccdn.qcloud.com/static/img/67ba54c1d9d63c307d4b8a157b70c722/image.png)

Run the following command to delete the original partition:

```
rm [Partition Number]
```

As shown in the figure above, there is a partition on the cloud disk with Number of "1". Run `rm 1` to get the result as shown below:
![](//mccdn.qcloud.com/static/img/3384eeada87ce75695e0e55125109eff/image.png)

Enter `mkpart primary [starting sector of original partition] 100%` to create a primary partition. In this example, `mkpart primary 2048s 100%` is used. This primary partition starts from the 2048th sector (the starting sector must be the same before and after deletion), and 100% means this partition reaches the end of the disk.

If it is shown as in the figure, enter Ignore:
![](//mccdn.qcloud.com/static/img/c45966e20dc856817c65fd6b81155e4a/image.png)

Run `print` again, and you can find that the new partition has been created successfully. Type `quit` to exit the parted tool:
![](//mccdn.qcloud.com/static/img/cb1af5adaf6c89d066077c43fd428a38/image.png)

#### Checking File System of Partition after Capacity Expansion
Check the expanded partition using the following command:

```
e2fsck -f Partition path
```
In the preceding steps, partition 1 has been created for this example. Run `e2fsck -f /dev/vdb1`. The results are:
![](//mccdn.qcloud.com/static/img/307f7a0c98eea05ca1d4560fe4e96f57/image.png)

#### Expanding File System
Run the following command to expand the file system on the partition:

```
resize2fs Partition path
```
![](//mccdn.qcloud.com/static/img/57d66da9b5020324703498dbef0b12f9/image.png)

#### Mounting New Partition
Run the following command to mount the partition:

```
mount Partition path Mount point
```

Here, mount the new partition manually with the command `mount /dev/vdb1 /data`, and check it with the command `df -h`. If the following message appears, the partition is mounted successfully, that is you can view the data disk.
![](//mccdn.qcloud.com/static/img/a2bd04c79e8383745689e19033a0daaa/image.png)

## Guidelines on Modifying the Partition after the MBR Partition Cloud Disk is Expanded
After expanding the MBR partition cloud disk, you can choose to:
- Format new space as a new separate partition with the original partition unchanged
- Expand the original partition to the new capacity (including the scenario of direct formatting without partitioning), and retain the data in the original partition.

In the two scenarios above, after the cloud disk of your Linux CVM is successfully upgraded, you can use the partition expansion tool (fdisk/e2fsck/resize2fs) in Linux to run a series of commands to complete the partition expansion with the original data retained. Note: regardless of adding a partition or expanding an existing partition, you need to unmount all mounted partitions of the cloud disk before expanding the capacity in order for the kernel to recognize the new partition table.

Note: due to MBR restrictions, no matter which method you choose, keep the size of any partition not more than 2 TB (if the expanded space is greater than 2 TB, you cannot choose the second method).

### Formatting New Space as an Independent Partition
#### Viewing Data Disk Information
Run the command `df -h` to view the partition information of the mounted data disk, and the command `fdisk -l` to view the information of the expanded data disk before partitioning:
![](//mccdn.qcloud.com/static/img/0a450dfaa9cfc7b2c7fdc04861f0e754/image.png)
![](//mccdn.qcloud.com/static/img/594671a1215dee3036b7940892438f62/image.png)

#### Unmounting All Mounted Partitions
Run the following command to unmount all mounted partitions:

```
umount  Mount point
```

Use `umount /data` to unmount all mounted partitions here.

#### Data Disk Partition
After confirming that all the partitions of the cloud disk have been unmounted, run the following command to create a partition:

```
fdisk [Disk path]
```
In this example, use the command `fdisk /dev/xvdc`, and follow the prompts to enter "p" (view existing partition information), "n" (create partition), "p" (create primary partition), and "2" (create the second primary partition) in sequence, press enter twice (use default settings), enter "w" (save partition table) to start partitioning:
![](//mccdn.qcloud.com/static/img/8c35d6f4dfb367e74edc27ce6822c317/image.png)
In this example, we only create one partition. You can create multiple partitions according to your needs.

#### Viewing New Partition
Run the following command to view the information of the new partition.

```
fdisk -l
```

![](//mccdn.qcloud.com/static/img/e04e924d62317bc2c605c8abaac394f5/image.png)
As shown in the figure above, the new partition xvdc2 has been created.

#### Formatting New Partition and Creating File System
When formatting partitions, you can decide the file system format, such as ext2 and ext3. Here we take "ext3" as an example, and use the command `mkfs.ext3 /dev/xvdc2` to format the new partition. 

![](//mccdn.qcloud.com/static/img/074e23eaa580495f96fb532b688d2d68/image.png)

#### Mounting New Partition
Create a new mount point using the following command

```
mkdir New mount point
```
And run the following command to mount the new partition to the new mount point:

```
mount New partition path New mount point
```

Here we use the command `mkdir /data1` to create the data1 directory, and use the command `mount /dev/xvdc2 /data1` to manually mount the new partition, and then use the command `df -h` to check. If the following message appears, the partition is mounted successfully, that is you can view the data disk:
![](//mccdn.qcloud.com/static/img/7b749a4bb6e7c8267c9354e1590c35d4/image.png)

#### Adding Information of New Partition
If you want the data disk to be automatically mounted to CVM when CVM is restarted or booted up, you need to add the partition information to /etc/fstab. If you do not, the data disk will not be automatically mounted to the CVM when the CVM is restarted or booted up.

Run the following command to add information:
`echo '/dev/xvdc2 /data1 ext3 defaults 0 0' >> /etc/fstab`

Run the `cat /etc/fstab` command to check. If the following message appears, the partition information is successfully added:
![](//mccdn.qcloud.com/static/img/f0b5c14bf08fd3629ddf6d9b1ae01ffc/image.png)

### Adding New Space to Existing Partition Space
The original disk partition is an MBR partition (you can see vdb1, vdc1, etc.), and the file system is also created on this partition. Or the original disk is not partitioned, and the file system is directly created on this disk. In both cases, you can choose to use the automatic expansion tool for capacity expansion.

The automatic expansion tool is applicable to the Linux operating system, which is used to add the new cloud disk storage space to the existing file system. To expand capacity successfully, the following three conditions must be satisfied:
- The file system is ext2/ext3/ext4.
- No error occurs on the current file system.
- Expanded disk size does not exceed 2 TB.

Next we describe how to use the automatic expansion tool.

#### Unmounting Disk Partition in Use
Run the following command to unmount the partition:

```
umount  Mount point
```

![](//mccdn.qcloud.com/static/img/c0acc05057941681627a5fd34979d194/image.jpg)

#### Downloading the Quick Expansion Tool
Run the following command to download the tool:

```
wget -O /tmp/devresize.py https://raw.githubusercontent.com/tencentyun/tencentcloud-cbs-tools/master/devresize/devresize.py
```

#### Running the Expansion Tool
Run the following command to expand capacity:
```
python /tmp/devresize.py Disk path
```
Note that the disk path here refers to the cloud disk to be expanded, but not the partition name. If your file system is on vdb1, run `python /tmp/devresize.py  /dev/vdb`.

![](//mccdn.qcloud.com/static/img/c7617b90578192d64d19f02325f00ffb/image.jpg)

If the output is "The filesystem on /dev/vdb1 is now XXXXX blocks long.", it means the expansion is successful.

If the output is "[ERROR] - e2fsck failed!!", use fsck to repair the partition where the file system is located. You can run the following command to automatically repair it:
```
fsck -a Partition path
```
Note that this is different from the previous command. Enter the partition where the file system is located. If your file system is on vdb1, run `fsck -a /dev/vdb1`.

After the partition is repaired successfully, use `python /tmp/devresize.py disk path` to expand capacity with the expansion tool.

#### Remounting Expanded Partition
Run the following command to mount the expanded partition:
```
mount Partition path Mount point
```

Run the following command to view the capacity of the expanded partition:
```
df -h
```

Here we use the command `mount /dev/vdb1 /data` to manually mount the expanded partition (if there is no partition before, run `mount /dev/vdb /data`), and use the command `df -h` to check. If the following message appears, the mounting is successful, that is you can view the data disk:

![](//mccdn.qcloud.com/static/img/2367f3e70cd0c3c1bef665cc47c1c3bc/image.jpg)
Then run the command `ll /data`, and you can find that the data in the original partition is not lost after the expansion and the new storage space has been expanded to the file system.
