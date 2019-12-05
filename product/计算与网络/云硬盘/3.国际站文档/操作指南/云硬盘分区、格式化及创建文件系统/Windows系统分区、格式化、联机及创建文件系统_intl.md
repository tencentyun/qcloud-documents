An instance can recognize the connected cloud disk and regard it as an HDD cloud disk. You can use any file system to format and partition the cloud block storage device, and create file systems. Any data written to the file systems is then written to the cloud disk and is transparent to the applications that use the device. The data disks are offline by default, and cannot be used before being partitioned and formatted. This document shows how to partition and format disks in the Windows system.

The path to "Disk Management" may vary with the Windows version (Windows 2012, Windows 2008, Windows 2003, etc.), but the steps to partition and format the disks are basically the same.
 
This document will guide you through the mounting, partitioning and formatting of data disks in Windows 2012 and Windows 2008.

## Prerequisites
- Make sure you have [connected cloud disk to the CVM instance](/doc/product/362/5745), and [logged in to Windows instance](/doc/product/213/5435).
- <font color="red">After formatting, all the data in the data disk will be cleared. Before formatting, make sure there is no data in the data disk or important data has been backed up. To avoid service exceptions, ensure that the CVM has stopped external services before formatting.</font>
- If you purchased multiple cloud disks, it is recommended to set a custom name for the elastic cloud disk that stores important data and set auto renewal for it to prevent the impact on your business due to the failure to renew the expired elastic cloud disk in a timely manner. 
- You can locate a cloud disk quickly based on the custom name or the private IP of associated CVM in [CBS Console](https://console.cloud.tencent.com/cvm/cbs).

## Making a Disk Online, and Partitioning and Formatting the Disk in Windows 2012
### Making a disk online
In Windows 2012, you can go to **Start** -> **Server Management** -> **Tools** -> **Computer Management** -> **Disk Management** to manage disks.

Click **Start**:

![](//mccdn.qcloud.com/img56b1ae00cc2f5.jpg)

Click **Server Management**:

![](//mccdn.qcloud.com/img56b1ae17e6f48.jpg)

Click **Tools** -> **Computer Management**:

![](//mccdn.qcloud.com/img56b1aed3a67b3.jpg)

Click **Disk Management**:

![](//mccdn.qcloud.com/img56b1af025f7e1.jpg)

As shown in the figure below, right click on Disk 1, and then select **Online**:

![](//mccdn.qcloud.com/img56b1b00b8935c.jpg)

If the disk already contains data (non-empty disk), you can ignore the following steps. Reformatting or partitioning a non-empty disk will <font color="red">clear all existing data on it</font>.

### (Optional) Formatting a disk
Right click and select **Initialize Disk**:

![](//mccdn.qcloud.com/img56b1b057ada88.jpg)

Select **GPT** or **MBR** depending on the partitioning format, and then click **OK**:

![](//mccdn.qcloud.com/img56b1b0a1cd741.jpg)

> **Note:**
> Only GPT partitioning format is supported when disk is larger than 2 TB. If you are not sure whether the disk capacity will exceed this value after subsequent expansion, GPT partitioning format is recommended; if you're sure that the disk capacity will not exceed this value, you're recommended to select MBR partitioning for a better compatibility.

### (Optional) Partitioning a disk
Right-click in the unallocated space and select **New Simple Volume**:

![](//mccdn.qcloud.com/img56b1b0bead71b.jpg)

In the **New Simple Volume Wizard** pop-up window, click **Next**:

![](//mccdn.qcloud.com/img56b1b0fae959f.jpg)

Enter the desired disk size for the partition, and then click **Next**:

![](//mccdn.qcloud.com/img56b1b1de673fb.jpg)

Enter the drive letter, and then click **Next**:

![](//mccdn.qcloud.com/img56b1b2f078870.jpg)

Choose to format the partition, select file system, and then click **Next**:

![](//mccdn.qcloud.com/img56b1b32b1846e.jpg)

Click **Finish** to create the new simple volume:

![](//mccdn.qcloud.com/img56b1b37e6e5f2.jpg)

Check the new partition:

![](//mccdn.qcloud.com/img56b1b39fb404d.jpg)

![](//mccdn.qcloud.com/img56b1b3a3e4dd4.jpg)


## Partitioning and Formatting a Disk in Windows 2008
### Making a disk online
In Windows 2008, the path to "Disk Management" is **Server Management** -> **Storage** -> **Disk Management**, which is different from that in Windows 2012.

Click **Server Management**:
![](//mccdn.qcloud.com/img56b1b5c4cd2ad.jpg)

Click **Storage** -> **Disk Management**:

![](//mccdn.qcloud.com/img56b1b6b60f2fd.jpg)

"Disk 1" is not online in its initial state. Right click **Disk 1** and click **Online** in the pop-up menu:

![](//mccdn.qcloud.com/img56b1b71f7e7d4.jpg)

### (Optional) Formatting a disk
Right click **Disk 1** and click **Initialize Disk** in the pop-up menu:

![](//mccdn.qcloud.com/img56b1b75941a79.jpg)

Select GPT as initialization format and click **OK**:
![](//mccdn.qcloud.com/img56b1b89cb0675.jpg)
Note: Be sure to select GPT as the partitioning format if the disk is larger than 2 TB.

### (Optional) Partitioning a disk
Right-click in the unallocated space following Disk 1 and select **New Simple Volume** from the popup menu:
![](//mccdn.qcloud.com/img56b1b91f2445b.jpg)

As instructed in the wizard, enter the size of the disk partition, then click **Next**:
![](//mccdn.qcloud.com/img56b1b93ab1e4a.jpg)

Choose to format the partition, select file system, and then click **Next**:
![](//mccdn.qcloud.com/img56b1b95a7f09a.jpg)

Click **Finish** to create the new simple volume:
![](//mccdn.qcloud.com/img56b1b9829f98e.jpg)

The figure below shows that it is being formatted:
![](//mccdn.qcloud.com/img56b1b99be5831.jpg)

At this point, you can see the partitioned disk on the PC:
![](//mccdn.qcloud.com/img56b1b9b953e21.jpg)

> Note: Do not convert a basic disk to a dynamic disk. We will not be responsible for any data loss caused by this operation.

## Online Setting
In the Windows operating system, you often need to set online in disk management. To make it easier for you to use elastic cloud disk, we recommend making the following modifications to the operating system:

Open the cmd command line and execute the following command:
```
diskpart
san policy=onlineall
```
![](//mccdn.qcloud.com/static/img/cfb2f1d6d9b99c6786db612f343df525/image.png)

After this operation, when an elastic cloud disk with valid file system is remounted to Windows CVM, you can use this disk directly without additional operations.

## Mounting a data disk automatically when launching new instance using custom images and data disk snapshots
When a new CVM instance is launched, if you specify ***custom image*** and ***data disk snapshot***, Tencent Cloud's cloud disk can be automatically mounted after the launch of CVM instance (read and write data directly without the need to perform operations such as addition, partitioning and formatting). You need to perform some operations on the original instance before making custom images and data disk snapshots, which will be described in detail below.

On the Windows system, if you want the cloud disk produced from the specified data disk snapshot to be automatically mounted to the new CVM instance, the specified custom image and data disk snapshot must meet the following requirements:

- The SAN policy in the custom image is `onlineAll`. Public images for Windows provided by Tencent Cloud have been configured as such, but it is recommended to check the configuration before creating any custom image by following the step below:
![](//mccdn.qcloud.com/static/img/74e490afd81bd7ad9fc9590565b48a80/image.jpg)

- The data disk must have been formatted as `ntfs` or `fat32` before you make a snapshot.

Only when both of the conditions are met can the data disk of the launched Windows CVM instance be automatically recognized and mounted.
