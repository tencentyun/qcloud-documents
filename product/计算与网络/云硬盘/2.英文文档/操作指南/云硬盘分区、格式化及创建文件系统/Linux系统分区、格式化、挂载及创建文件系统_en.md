Instances can recognize a connected cloud disk and regard it as an ordinary hard disk. Users can use any file systems to format and partition the Cloud Block Storage device, and create a file system for it. After this, any data written into the file system will be written into the cloud disk, and the data will be transparent to the applications that use this device. This document will use an example to show you how to use block storage device in a CVM, and describe several points you need to be aware of in details. You can also go to the [Windows System Partitioning, Formatting, Linking and File System Creation](https://cloud.tencent.com/document/product/362/6734
) page for a guide on how to use Cloud Block Storage on Windows instances.

In this example, the user has purchased a system disk with a capacity of 20GB and a data disk with a capacity of 30GB (i.e. non-elastic cloud disk) when activating the CVM, then the user also purchased an elastic cloud disk with a capacity of 10GB in the Cloud Block Storage Console.

## Preconditions
- Please make sure that you have gone through [Connect Cloud Block Storage to a CVM Instance](/doc/product/362/5745), and [Log in to Linux Instance](/doc/product/213/5436).
- After formatting, all data in the data disk will be erased. Before formatting, please make sure that there is no data in the data disk, or that important data has been backed up. In order to avoid service errors, please make sure that CVM has already stopped external service before formatting.
- If you have purchased multiple cloud disks, it is suggested that you set a custom name for the elastic cloud disk with important data in it and configure automatic renewal, to prevent any impact on your business caused by expired elastic cloud disk when the disk is not renewed in time. 
- Users can locate a cloud disk quickly by using the custom name or the private IP of an associated CVM in the [Cloud Block Storage Console](https://console.cloud.tencent.com/cvm/cbs).

In this example, the ID and the name of elastic cloud disk are `ins-kjo6azag` and `Elastic Cloud Disk Demo` respectively. 


## Viewing Mounted Disk
1) Execute the command `fdisk -l` to view disk information.

You can see that the non-elastic cloud disk `vdb` created with the CVM and the elastic cloud disk `vdc` which is mounted just now are not formatted.
![](//mccdn.qcloud.com/static/img/0096d7b0af255789bc68356ae8861ca7/image.png)

2) Execute the command `ls -l /dev/disk/by-id/`, you can see the relation between the elastic cloud disk and the device name. Note: At this time, the information of non-elastic cloud disk will not be shown here.
![](//mccdn.qcloud.com/static/img/c004f380599b1ac12475f325f24b9d77/image.png)

If the disk has never been initialized, you need to create a file system before you can use it. A cloud disk created from a snapshot may already contain a file system. All original data will be overwritten if you create a new file system when a file system already exists.

Special information, such as file system type, can be listed out by using the command `file -s device`.

```

sudo file -s /dev/xvdf
/dev/xvdf: data

```
If the output of the above command only displays the device's data, it means that there is no file system on the device, and you need to create one. You can continue to perform all the following steps. The output will be different if you run this command on a device that contains a file system. If an output such as `Linux rev 1.0 ext4 filesystem data` is returned, it means that there is a file system on this disk, and you can skip the partitioning and formatting steps.

- If the disk has been initialized, you can determine whether you need to create a new file system according to the `System` field. If a file system type such as EXT3, EXT4 is displayed in the System field, there is no need to create a new file system, and you can skip the partitioning and formatting steps.

## (Optional) Disk Partitioning
1) Partition the cloud disk. You can also skip the partitioning process and simply proceed to formatting. In this example, we show you how to divide the elastic cloud disk into two partitions before using it. Execute the following command:
```
fdisk /dev/vdb
```
Follow the instructions on the UI and enter "n" (create a new partition), "p" (create an extended partition), and "1" (use the first primary partition) in sequence, press Enter twice (use default settings), then enter "wq" (save partition table) and press Enter to start partitioning.

In this example, we only create one partition. Developers can create multiple partitions according to their own needs.
![](//mccdn.qcloud.com/img56a604c2b886f.png)

By using the command "fdisk -l", you can see that the new partition `vdb1` has been created.
![](//mccdn.qcloud.com/img56a605027a966.png)


![](//mccdn.qcloud.com/static/img/049a61e867c38eacbe636b11764461bf/image.png)

2) After partitioning, you can execute the command `ls -l /dev/disk/by-id` to view the following content:
![](//mccdn.qcloud.com/static/img/1b88d2d8deb8d7a421e65ce6e27b82d6/image.png)

## (Conditional) Disk Formatting
> In this step, we assume that you are processing an initialized disk. If this disk contains data (e.g. a cloud disk created from snapshot), do not use mkfs (you should skip to the next step). Otherwise, you will format the disk and erase the existing data.

Execute the command `mkfs.ext4 device_name` to format and create ext4 file system. Replace device_name with a device name (e.g. /dev/vdb). Based on the requirement of applications or the restrictions of operating system, you can choose other file systems such as ext3 or XFS.

![](//mccdn.qcloud.com/static/img/1339a1feb56d7eab4715146d52045f74/image.png)

## Disk Mounting
```
mkdir /data/part1 -p  # create a sample mount point
mkdir /data/part5 -p # create a sample mount point
mount /dev/vdc1 /data/part1 # mount vdc1 to /data/part1
mount /dev/vdc5 /data/part5 # mount vdc5 to /data/part5
touch /data/part1/disk-bm42ztpm-part1.txt # create an empty file for subsequent presentation
touch /data/part5/disk-bm42ztpm-part5.txt # create an empty file for subsequent presentation
yum install tree -y # install a tool used to show the directory structure
tree /data  # view the structure of /data directory
```

Here, you can see the following structure tree:
![](//mccdn.qcloud.com/static/img/2f4b8f43bb0d19ee8e62761dcc51a5c1/image.png)

Execute the command `lsblk -f` to query file system UUID and mount point information.
![](//mccdn.qcloud.com/static/img/5d14f104ce38e76af50758031aecab20/image.png)

## (Optional) Configuring Auto Mount

If you restart the CVM now, you will find that the mount point you have created just now has disappeared. If you want the data disk to be automatically mounted to CVM when CVM is restarted or booted up, you need to add the partition information into `/etc/fstab`. If you didn't, the data disk will not be automatically mounted to the CVM when the CVM is restarted or rebooted. You can use three different methods in the `/etc/fstab` configuration file to allow the file system to locate mount points:


| Auto-mount Method| Advantage | Disadvantage |
|---|---|--|
| Use device name || If you remount the elastic cloud disk on the CVM after you unmount it (e.g. during data migration), the name may change, which may cause your auto-mount configuration to lose its effect |
| Use file system UUID || This is related to the file system. UUID will change when the file system is reformatted, which may cause your auto-mount configuration to lose its effect |
| Use elastic cloud disk soft link | This is not related to the device name or the file system, and is a unique name corresponding to the cloud disk actually used | Only elastic cloud disks have this soft link, it cannot detect formatting operations on the partition |

From the following figure, you can see that the UUID has changed after the file system is reformatted:
![](//mccdn.qcloud.com/static/img/12b7d1675e6cf0271a53f5a69213856c/image.png)

Similarly, as is seen from the following figure, the device name is changed after the elastic cloud disk is unmounted and then remounted in the console:
![](//mccdn.qcloud.com/static/img/e31475d93916a83f5fba8cb31c456936/image.png)

As a summary, we suggest that you should always use the third method to achieve auto-mount of elastic cloud disks. Create a backup of the `/etc/fstab` file and use it in case of accidental corruption or deletion of the file.

```

 cp /etc/fstab /etc/fstab.backup

```

Open the `/etc/fstab` file.

```
vi /etc/fstab

Use elastic cloud disk soft link (recommended)
Input:device_name  mount_point  file_system_type  fs_mntops  fs_freq  fs_passno  

Example:
/dev/disk/by-id/virtio-disk-bm42ztpm-part1 /data/part1 ext3 defaults,nofail 0 1
/dev/disk/by-id/virtio-disk-bm42ztpm-part5 /data/part5 ext3 defaults,nofail 0 1
```
The last three fields are the installation option of the file system, the dump frequency of the file system and the checking sequence of the file system upon boot-up, respectively. You can use the value (defaults,nofail 0 2) in the example. You can view more information about the `/etc/fstab` entry by entering "man fstab" in the command line.

Execute the command `mount -a`. A successful execution means that the file is normal, and the file system you have created just now will be automatically installed during the next boot-up.


## (Optional) Mounting Data Disk Automatically When Activating New Instance by Using Custom Image and Data Disk Snapshot
When a new CVM instance is activated, if a user specified ***custom image*** and ***data disk snapshot***, Tencent Cloud CBS is able to mount data disk automatically when a CVM instance is activated (which means you can read and write the data disk directly without performing operations such as adding, partitioning and formatting). The user needs to perform several operations on the original instance before creating custom image and data disk snapshot. Details will be described below.

For Linux system, if a user hopes that the cloud disk generated from a specified data disk snapshot can be automatically mounted to a new CVM instance, the specified custom image and data disk snapshot must meet the following requirements:
- The data disk ***must*** have already been formatted before it is used to create snapshot, which also means it has already been successfully mounted on the original CVM.
- You need to add the following commands to the `/etc/rc.local` file and write the data disk mount points into the file, before you can create custom image for the system disk:

```
mkdir -p <mount-point>
mount <device-id> <mount-point>
```

For `<mount-point>`, enter the mount point of the file system, such as `/mydata`. For `<device-id>`, enter the user's actual file partition location, such as `/dev/vdb (the name of a device with file system but without partitions)` and `/dev/vdb1 (the name of a device with both file system and partitions)`.

Both of the above two requirements are needed to be satisfied to ensure that newly activated Linux CVM instance data disks can be automatically recognized and mounted.
