By default, the data disks purchased on the CVM purchase page are not automatically mounted under an offline state. Data disks that are not partitioned and formatted cannot be used. This tutorial will guide you to mount, partition and format data disks in a Windows system.

The path to the "Disk Management" interface may vary with the Windows version (Windows 2012, Windows 2008, Windows 2003, etc.), but the steps to partition and format the disks are basically the same.

This article provides the guide on how to mount, partition and format data disks on Windows 2012 and Windows 2008.

>Note:

> <font color="red">Once formatted, all the data in the disk will be cleared. Make sure that there is no data left in the disk or the important data has been backed up before formatting. To avoid any service exception, make sure that the CVM has stopped providing services before formatting. </font>

## 1. Disk Partitioning and Formatting on Windows 2012

On Windows 2012, the path to Disk Management is "Start" - "Server Management" - "Tools" - "Computer Management" - "Disk Management".

Click the "Start" button:

![](//mccdn.qcloud.com/img56b1ae00cc2f5.jpg)

Click "Server Management":

![](//mccdn.qcloud.com/img56b1ae17e6f48.jpg)

Click "Tools" - "Computer Management":

![](//mccdn.qcloud.com/img56b1aed3a67b3.jpg)

Click on "Disk Management":

![](//mccdn.qcloud.com/img56b1af025f7e1.jpg)

As shown below, "Disk 1" is an unpartitioned disk. Here, the process is illustrated by creating one partition for "Disk 1". Right click on Disk 1, then select "Online":

![](//mccdn.qcloud.com/img56b1b00b8935c.jpg)

Right click again, then select "Initialize Disk":

![](//mccdn.qcloud.com/img56b1b057ada88.jpg)

Select "GPT" or "MBR" depending on the partitioning method, and click on the "OK" button:

![](//mccdn.qcloud.com/img56b1b0a1cd741.jpg)

> Note: Make sure to select GPT as the partitioning method if the disk is larger than 2TB.

Right click on the unallocated space, and select "New Simple Volume":

![](//mccdn.qcloud.com/img56b1b0bead71b.jpg)

In the "New Simple Volume Wizard" pop-up window, click "Next":

![](//mccdn.qcloud.com/img56b1b0fae959f.jpg)

Enter the desired disk size for the partition, then click "Next":

![](//mccdn.qcloud.com/img56b1b1de673fb.jpg)

Enter the drive letter, then click "Next":

![](//mccdn.qcloud.com/img56b1b2f078870.jpg)

Select "File System", then "Format Partition", and click "Next":

![](//mccdn.qcloud.com/img56b1b32b1846e.jpg)

Upon completing the New Simple Volume Wizard, click "Finish":

![](//mccdn.qcloud.com/img56b1b37e6e5f2.jpg)

View the new partition:

![](//mccdn.qcloud.com/img56b1b39fb404d.jpg)

![](//mccdn.qcloud.com/img56b1b3a3e4dd4.jpg)


## 2. Disk Partitioning and Formatting on Windows 2008
On Windows 2008, the path to "Disk Management", different from that on Windows 2012, is "Server Management" - "Storage" - "Disk Management".

Click "Server Management":
![](//mccdn.qcloud.com/img56b1b5c4cd2ad.jpg)

Click "Storage" - "Disk Management":

![](//mccdn.qcloud.com/img56b1b6b60f2fd.jpg)

As shown above, "Disk 1" is an unallocated disk. Here, the process is illustrated by creating one partition for "Disk 1".

"Disk 1" is not online in the initial state. Right click "Disk 1", and then click "Online" in the pop-up menu:

![](//mccdn.qcloud.com/img56b1b71f7e7d4.jpg)

Again, right click "Disk 1", and then click "Initialize Disk" in the pop-up menu:

![](//mccdn.qcloud.com/img56b1b75941a79.jpg)

Select the GPT initialization method, and click the "OK" button:
![](//mccdn.qcloud.com/img56b1b89cb0675.jpg)
Note: Make sure to select GPT as the partitioning method if the disk is larger than 2TB.

Right click on the unallocated region behind "Disk 1", and select "New Simple Volume" in the shortcut menu that pops up:
![](//mccdn.qcloud.com/img56b1b91f2445b.jpg)

As prompted by the Wizard, enter the size of the disk partition, then click "Next":
![](//mccdn.qcloud.com/img56b1b93ab1e4a.jpg)

Select "File System", then "Format Partition", and click "Next":
![](//mccdn.qcloud.com/img56b1b95a7f09a.jpg)

Upon completing the New Simple Volume Wizard, click "Finish":
![](//mccdn.qcloud.com/img56b1b9829f98e.jpg)

"Formatting..." is displayed:
![](//mccdn.qcloud.com/img56b1b99be5831.jpg)

At this point, the newly partitioned data disk can be seen on the computer screen:
![](//mccdn.qcloud.com/img56b1b9b953e21.jpg)

> Note: Do not convert a basic hard disk to a dynamic hard disk. We are not liable for any data loss arising out of this action.

## 3. Online Settings
Under a Windows operating system, online settings are often needed in Disk Management. To help you make better use of Elastic Cloud Block Storage, we recommend that you modify the operating system as follows:
Open the cmd line and run the following command
```
diskpart
san policy = onlineall
```

![](//mccdn.qcloud.com/static/img/cfb2f1d6d9b99c6786db612f343df525/image.png)
Once remounted to the Windows CVM, the Elastic Cloud Block Storage can be used directly without any user action as long as it contains a valid file system.