An instance can recognize the connected cloud disk and regard it as an HDD cloud disk. You can use any file system to format and partition the cloud block storage device, and create file systems. Any data written to the file systems is then written to the cloud disk and is transparent to the applications that use the device. This document uses an example to demonstrate how to use a block storage device in a CVM and describes some important considerations. For more information about how to use cloud disks on Windows instances,
please see [Making cloud disk online, partitioning and formating cloud disk, and creating file systems on Windows](https://intl.cloud.tencent.com/document/product/362/6734).

In this example, the user purchased a 20-GB system disk and a 30-GB data disk (non-elastic cloud disk) when the CVM is launched, and then purchased a 10-GB elastic cloud disk in the CBS Console.

## Prerequisites
- Make sure you have [connected cloud disk to the CVM instance](/doc/product/362/5745), and [logged in to Linux instance](/doc/product/213/5436).
- <font color="red">After formatting, all the data in the data disk will be cleared. Before formatting, make sure there is no data in the data disk or important data has been backed up. To avoid service exceptions, ensure that the CVM has stopped external services before formatting. </font>
- If you purchased multiple cloud disks, it is recommended to set a custom name for the elastic cloud disk that stores important data and set auto renewal for it to prevent the impact on your business due to the failure to renew the expired elastic cloud disk in a timely manner.  
- You can locate a cloud disk quickly based on the custom name or the private IP of associated CVM in [CBS Console](https://console.cloud.tencent.com/cvm/cbs).

In this example, the elastic cloud disk ID is `ins-kjo6azag` and the name is `elastic cloud disk usage demo`. 


## Viewing the Mounted Disk
1) Execute the command `fdisk -l` to view disk information.

At this point, you can find that the non-elastic cloud disk `vdb` created with the CVM and the elastic cloud disk `vdc` you just mounted have not yet been formatted.
![](//mccdn.qcloud.com/static/img/0096d7b0af255789bc68356ae8861ca7/image.png)

2) Run the command `ls -l /dev/disk/by-id/`. You can see the mapping between the elastic cloud disk and the device name. Note: No information is displayed for non-elastic cloud disk.
![](//mccdn.qcloud.com/static/img/c004f380599b1ac12475f325f24b9d77/image.png)

If the disk has never been initialized, you need to create a file system before you can use it. The cloud disk created from a snapshot may already contain a file system. <font color="red">If you create a new file system on an existing file system, all exiting data will be overwritten.</font>

Use the command `file -s device` to list special information, such as file system type.

```

sudo file -s /dev/xvdf
/dev/xvdf: data

```
If the output of the preceding command shows only the data of the device, this means there is no file system on the device and you need to create a file system. You can proceed with all the steps below. If you run this command on a device that contains a file system, the output will be different. If an output like `Linux rev 1.0 ext4 filesystem data` is returned, this means a file system has been created on this disk. You can skip the partitioning and formatting steps.

- If the disk has been initialized, you can determine from the field `System` whether a new file system needs to be created. If the field System shows such file system types as EXT3 and EXT4, you do not need to create a new file system. You can skip the partitioning and formatting steps.

## (Optional) Partitioning a Disk
1) Partition the cloud disk. You can also skip the partitioning process and directly proceed to formatting. This example shows how to divide the elastic cloud disk into two partitions. Execute the following command:
```
fdisk /dev/vdb
```
By following the instructions on the interface, enter "n" (create a partition), "p" (create an extended partition), and "1" (use the first primary partition) in turn, press Enter twice (use default settings), and enter "w" (save partition table), and then press Enter to start partitioning.

This example creates one partition. Developers can create multiple partitions as needed.
![](//mccdn.qcloud.com/img56a604c2b886f.png)

Using the command "fdisk -l", you can find that the new partition `vdb1` has been created.
![](//mccdn.qcloud.com/img56a605027a966.png)


![](//mccdn.qcloud.com/static/img/049a61e867c38eacbe636b11764461bf/image.png)

2) After partitioning, execute the command `ls -l /dev/disk/by-id` and you can see the following:
![](//mccdn.qcloud.com/static/img/1b88d2d8deb8d7a421e65ce6e27b82d6/image.png)

## (Conditional) Formatting a Disk
> This step assumes that you are working on an initialized disk. If the disk already contains data (such as a cloud disk created from a snapshot), do not use mkfs (skip to the next step). Otherwise, you will format the disk and delete the existing data.

Execute the command `mkfs.ext4 device_name` to format and create ext4 file system. Replace device_name with a device name (e.g. /dev/vdb). Depending on the requirements of the application or operating system, you can select other file system types, such as ext3 or XFS.

![](//mccdn.qcloud.com/static/img/1339a1feb56d7eab4715146d52045f74/image.png)

## Mounting a Disk
```
mkdir /data/part1 -p  # Create a sample mount point
mkdir /data/part5 -p # Create a sample mount point
mount /dev/vdc1 /data/part1 #Mount vdc1 to /data/part1
mount /dev/vdc5 /data/part5 # Mount vdc5 to /data/part5
touch /data/part1/disk-bm42ztpm-part1.txt #Create an empty file for subsequent demonstration
touch /data/part5/disk-bm42ztpm-part5.txt # Create an empty file for subsequent demonstration
yum install tree -y # Install a tool to show the directory structure
tree /data  #View /data directory structure
```

At this point, you can see the following tree:
![](//mccdn.qcloud.com/static/img/2f4b8f43bb0d19ee8e62761dcc51a5c1/image.png)

Execute the command `lsblk -f` to query file system UUID and mount point information.
![](//mccdn.qcloud.com/static/img/5d14f104ce38e76af50758031aecab20/image.png)

## (Optional) Configuring Auto Mount

If you restart the CVM at this time, you can find that the mount point you just created has disappeared. If you want the data disk to be automatically mounted to the CVM when the CVM is restarted or re-launched, you need to add the partition information to `/etc/fstab`. If it is not added, the data disk cannot be automatically mounted to the CVM when the CVM is restarted or re-launched. You can use three different methods in the `/etc/fstab` configuration file to allow the file system to locate mount points:


| Auto-Mount Method | Advantage | Disadvantage |
|---|---|--|
| Use device name || If you unmount the elastic cloud disk from the CVM and mount it again (for example, when migrating data), the name may change, which may cause your auto-mount setting to be invalid |
| Use file system UUID || This is related to file system. After the file system is reformatted, the UUID will change, which may cause your auto-mount setting to be invalid |
| Use elastic cloud disk soft link | This is the unique name corresponding to the used cloud disk, unrelated to the device name and file system. | Only an elastic cloud disk has this soft link, and the formatting of partition cannot be perceived. |

As you can see from the figure below, the UUID has changed after the file system is reformatted:
![](//mccdn.qcloud.com/static/img/12b7d1675e6cf0271a53f5a69213856c/image.png)

Similarly, as shown in the figure below, the device name has changed after the elastic cloud disk is unmounted and then remounted in the console:
![](//mccdn.qcloud.com/static/img/e31475d93916a83f5fba8cb31c456936/image.png)

In summary, we recommend that you always use the third method to automatically mount an elastic cloud disk. Create a backup of the file `/etc/fstab` so that you can use the backup in case that the file is accidentally damaged or deleted.

```

 cp /etc/fstab /etc/fstab.backup

```

Open the file `/etc/fstab`.

```
vi /etc/fstab

Use elastic cloud disk soft link (recommended)
Input:device_name  mount_point  file_system_type  fs_mntops  fs_freq  fs_passno  

Example:
/dev/disk/by-id/virtio-disk-bm42ztpm-part1 /data/part1 ext3 defaults,nofail 0 1
/dev/disk/by-id/virtio-disk-bm42ztpm-part5 /data/part5 ext3 defaults,nofail 0 1
```
The last three fields refer to the file system installation options, the file system dump frequency, and the file system check sequence on launch. Use the value in the example (defaults,nofail 0 2). You can view more information about the entry `/etc/fstab` by entering "man fstab" in the command line.

Run the command `mount -a`. If the command is run successfully, the file is normal. The file system you just created is automatically installed the next time you launch the instance.


## (Optional) Mounting a data disk automatically when launching new instance using custom image and data disk snapshot
When a new CVM instance is launched, if you specify ***custom image*** and ***data disk snapshot***, Tencent Cloud's cloud disk can be automatically mounted after the launch of CVM instance (read and write data directly without the need to perform operations such as addition, partitioning and formatting). You need to perform some operations on the original instance before making custom images and data disk snapshots, which will be described in detail below.

On the Linux system, if you want to specify that the cloud disk produced from the data disk snapshot can be automatically mounted to the new CVM instance. The specified custom image and data disk snapshot must meet the following requirements:
- The data disk ***must*** be formatted before the snapshot is generated. That is, the data disk has been successfully mounted to the original CVM.
- Before making a custom image on the system disk, you need to add the following command to the file `/etc/rc.local` to write the data disk mount point to the file:

```
mkdir -p <mount-point>
mount <device-id> <mount-point>
```

Enter the mount point of file system in `<mount-point>`, such as `/mydata`, and the actual file partition location in `<device-id>`, such as `/dev/vdb (device without partition and with file system)` and `/dev/vdb1 (device with both partition and file system)`.

Only when both of the conditions are met can the data disk of the launched Linux CVM instance be automatically recognized and mounted.

