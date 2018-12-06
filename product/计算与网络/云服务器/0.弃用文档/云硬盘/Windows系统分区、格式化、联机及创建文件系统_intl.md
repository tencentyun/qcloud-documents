Instances can recognize a connected cloud disk and regard it as an ordinary hard disk. Users can use any file systems to format and partition the Cloud Block Storage device, and create a file system for it. After this, any data written into the file system will be written into the cloud disk, and the data will be transparent to the applications that use this device. The data disks are offline by default, which cannot be used before being partitioned and formatted. This tutorial will guide you on how to partition and format disks in Windows system.

The path to "Disk Management" may vary with the Windows version (Windows 2012, Windows 2008, Windows 2003, etc.), but the steps to partition and format the disks are basically the same.
 
This document provides the guide on how to mount, partition and format data disks in Windows 2012 and Windows 2008.

## Preconditions
- Please make sure that you have performed [Connect Cloud Block Storage to CVM Instance](/doc/product/362/5745), and [Log in to Windows Instance](/doc/product/213/5435) operations.
- <font color="red">After formatting, all data in the data disk will be erased. Before formatting, please make sure that there is no data in the data disk, or that important data has been backed up. In order to avoid service errors, please make sure that CVM has already stopped external service before formatting.</font>
- If you have purchased multiple cloud disks, it is suggested that you set a custom name for the elastic cloud disk with important data in it and configure automatic renewal, to prevent any impact on your business caused by expired elastic cloud disk when the disk is not renewed in time. 
- Users can locate a cloud disk quickly by using the custom name or the private IP of an associated CVM in the [Cloud Block Storage Console](https://console.cloud.tencent.com/cvm/cbs).

## Making Disk Online, Disk Partitioning and Formatting in Windows 2012
### Making Disk Online
In Windows 2012, the path to Disk Management is "Start" - "Server Management" - "Tools" - "Computer Management" - "Disk Management".

Click "Start" button.

Click "Server Management".

Click "Tools" - "Computer Management".

Click "Disk Management".

Right click on Disk 1, then select "Online".

If the disk already has data in it (i.e. non-empty disk), users can ignore the following operations. If you reformat or repartition a non-empty disk, <font color="red">all the original data will be erased</font>

### (Optional) Disk Formatting
Right click, then select "Initialize Disk".

Select "GPT" or "MBR" depending on the partitioning method, and click the "OK" button.

> Note: Make sure to select GPT as partitioning method if the disk is larger than 2TB.

### (Optional) Disk Partitioning
Right click on unallocated space, and select "New Simple Volume".

In the "New Simple Volume Wizard" pop-up window, click "Next".

Enter the desired disk size for the partition, then click "Next".

Enter the drive letter, then click "Next".

Select "File System", then "Format Partition", and click "Next".
.
Upon completing the New Simple Volume operation, click "Finish".
View the new partition.


## Disk Partitioning and Formatting in Windows 2008
### Making Disk Online
In Windows 2008, the path to "Disk Management" is different from the path in Windows 2012. Enter it via "Server Management" - "Storage" - "Disk Management".

Click "Server Management".

Click "Storage" - "Disk Management".

"Disk 1" is not online in its initial state. Right click "Disk 1" and click "Online" in the pop-up menu.

### (Optional) Disk Formatting
Again, right click "Disk 1" and click "Initialize Disk" in the pop-up menu.

Select GPT as initialization method and click "OK".

Note: Make sure to select GPT as the partitioning method if the disk is larger than 2TB.

### (Optional) Disk Partitioning
Right click on unallocated space behind "Disk 1", and select "New Simple Volume" in the pop-up shortcut menu.

Follow the instructions in the Wizard, enter the size of the disk partition, then click "Next".

Select "File System", then "Format Partition", and click "Next".

Upon completing the New Simple Volume operation, click "Finish".

"Formatting..." is displayed.

At this point, the newly partitioned data disk can be seen on the computer screen.

> Note: Do not convert a basic hard disk to a dynamic hard disk. We are not liable for any data loss arising out of this action.

## Online Settings
In Windows operating system, online settings are often needed to be configured in Disk Management. To help you make better use of elastic cloud disk, we recommend that you modify the operating system.

Open the cmd command line and execute the following command
```
diskpart
san policy=onlineall
```


After this operation, if an elastic cloud disk with valid file system is remounted to Windows CVM, the user will be able to use this disk directly without additional operations.

## Mounting Data Disk Automatically When Activating New Instance Using Custom Image and Data Disk Snapshot
When a new CVM instance is activated, if a user specified ***custom image*** and ***data disk snapshot***, Tencent Cloud CBS is able to mount data disk automatically when a CVM instance is activated (which means you can read and write the data disk directly without performing operations such as adding, partitioning and formatting). The user needs to perform several operations on the original instance before creating custom image and data disk snapshot. Details will be described below.

For Windows system, if a user hopes that the cloud disk generated from a specified data disk snapshot can be automatically mounted to a new CVM instance, the specified custom image and data disk snapshot must meet the following requirements:

- The SAN policy in the custom image is `onlineAll`. Public Windows images currently provided by Tencent Cloud have been properly configured by default, but it is recommended that users check the configuration before creating any custom images.

- The data disk must have already been formatted into `ntfs` or `fat32` before it can be used to create snapshot.

Both of the above two requirements need to be satisfied to ensure that newly activated Windows CVM instance data disks can be automatically recognized and made online.
