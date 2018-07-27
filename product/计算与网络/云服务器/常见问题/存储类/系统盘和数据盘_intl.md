### What is the default capacity of a CVM system disk?

A new CVM system disk has a capacity of 50 GB by default.

### Can I change a CVM system disk from a local disk to a cloud disk?

CVM instances only support selecting disk type for system disk at the time of purchase. After the purchase, the switch between local and cloud disks for system disk is not allowed. It is recommended to select cloud disk as the system disk the next time you purchase a CVM instance.

### Which regions and availability zones support increasing system disk capacity to more than 50 GB?

For Beijing, Shanghai, and Guangzhou regions, if the system disk is a cloud disk, its capacity can be changed to more than 50 GB. This is not supported in the domestic finance zones and other regions. 

### When the system is reinstalled, can the capacity of CVM system disk be expanded?

Generally, this involves two scenarios:

- **System disk is a cloud disk:**
  In this case, when you reinstall the system, expanding capacity (increasing the system disk size) is supported, but reducing capacity (reducing the system disk size) is not supported.

- **System disk is a local disk:**

  This can be further divided into two scenarios, depending on the size of the current system disk:

  - For the instance whose system disk's default capacity is 50 GB at the time of purchase, expanding capacity is not supported.
  - This applies to the instances that were purchased at early stage: if the system disk capacity is less than or equal to 20 GB, it is adjusted to 20 GB by default; if the capacity is greater than 20 GB, it is adjusted to 50 GB by default.

### How do I expand the capacity of a cloud disk?

If your CVM uses a cloud disk, you can expand the disk capacity. For more information on how to expand the capacity, please see [Expanding Capacity of Cloud Disks](https://cloud.tencent.com/document/product/362/5747).

### Can the capacity of an expanded system disk be reduced by reinstalling the system?

The capacity of a system disk cannot be reduced.

### How can I expand the system disk capacity with the current data on the CVM stored?

You can create an image first, and then use the image to reinstall the system to expand the system disk capacity.

### What is the system disk capacity if I use an image less than 50 GB to create or reinstall the CVM?

The system disk has a minimum capacity of 50 GB regardless of the image capacity.

### How much free capacity is provided for a separately purchased cloud disk? What is the difference between a separately purchased cloud disk and a cloud disk purchased with CVM?

No free capacity is given for a cloud disk purchased separately, and there is no difference between such a cloud disk and a could disk purchased with a CVM. A cloud disk purchased with a CVM cannot be unmounted from the CVM and is renewed along with the CVM. A separately purchased cloud disk can be mounted to different CVMs and is renewed separately. This makes it more flexible than a cloud disk purchased with a CVM.

### How can I check the data disk?

Log in to the [Console](https://console.cloud.tencent.com/cvm), and go to **Cloud Virtual Machine** -> **Cloud Block Storage**. In the **Attribute** column, select **Data Disk** to check all data disks in the region.

### How do I read and write the original NTFS data disk after the operating system is changed from Windows to Linux?

A Windows file system usually uses NTFS or FAT32 format, while a Linux file system uses EXT format. When the operating system is changed from Windows to Linux after re-installation, the data disk remains in the original format. Thus, the access to the data disk file system may fail in the reinstalled system. On the reinstalled Linux CVM, you can read data from the data disk under Windows by performing the following operations:

1. Install ntfsprogs software on the Linux system using the following command to enable Linux to support NTFS file system:
   ```
   yum install ntfsprogs
   ```

2. Mount the data disk under Windows to Linux CVM. Skip this step if the data disk has already been mounted:
Log in to [Console](https://console.cloud.tencent.com/cvm), go to **Cloud Virtual Machine** -> **Cloud Block Storage**, and then click **More** -> **Mount to CVM** button for the Windows data disk to be mounted. Select the reinstalled Linux CVM in the pop-up box, and then click **OK**.

3. Check the data disk migrated from Windows by running the following command:
   ```
   parted -l
   ```

4. Mount the data disk by running the following command:
   ```
   mount -t ntfs-3g Data disk path Mount point
   ```
   ![Mount a data disk](https://main.qcloudimg.com/raw/7f093da789d6d6e08b9e24365ea31208.png)

5. When the file system is identified, the mounted data disk can be directly read and written by the Linux system.

### How do I read the data disk in EXT format after the operating is changed from Linux to Windows after re-installation?

A Windows file system usually uses NTFS or FAT32 format, while a Linux file system uses EXT format. When the operating system is changed from Linux to Windows after re-installation, the data disk remains in the original format. Thus, the access to the data disk file system may fail in the reinstalled system. On the reinstalled Windows CVM, you can read data from the data disk under Linux system by performing the following operations:

1. Suppose the Linux CVM data disk has two partitions before re-installation: /dev/vdb1 and /dev/vdb2. ![Figure](https://main.qcloudimg.com/raw/f66b9494e966a0e85b4091be5af315e2.png)

2. Download and install DiskInternals Linux Reader on the reinstalled Windows CVM.
3. Mount the data disk under Linux to the Windows CVM. Skip this step if the data disk has already been mounted: Log in to [Console](https://console.cloud.tencent.com/cvm), go to **Cloud Virtual Machine** -> **Cloud Block Storage**, and then click **More** -> **Mount to CVM** button for the Linux data disk to be mounted. Select the reinstalled Windows CVM in the pop-up box, and then click **OK**.
4. Run DiskInternals to check the information of the data disk you just mounted. /root/mnt and /root/mnt1 correspond to partitions vdb1 and vdb2, respectively:![](https://main.qcloudimg.com/raw/b35757625119c8226a022042cf0fac3f.png)
5. Click to enter /root/mnt, right-click the file you want to copy, and then select **Save** to save the file.![](https://main.qcloudimg.com/raw/05b1cecf7206fec9052973f4ae7955a6.png)

6. Note that the Linux data disk is read-only at this time. To perform read and write operations on the data disk as you do on a Windows data disk, back up the files you need and then re-format the disk into a standard type supported by Windows operating system. For more information, please see [Data Disk Partitioning and Formatting on Windows System](https://cloud.tencent.com/document/product/213/2158).

