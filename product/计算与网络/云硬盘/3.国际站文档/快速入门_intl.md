This document describes how to create an empty elastic cloud disk `cbs-test` in Beijing, connect to a CVM instance, create a file system and write a file named `qcloud.txt` in the system so as to help users have a basic understanding on Tencent Cloud's cloud disks. For more information on the definition of elastic cloud disk, please see [Cloud Disk Classification](https://cloud.tencent.com/document/product/362/2353). For more information on how to create a cloud disk with data, please see [Create Cloud Disk from Snapshot](/doc/product/362/5757).

## Prerequisites
To use cloud disks according to this document, make sure that you have an available running CVM instance in the region and availability zone (Beijing Zone 1 in this example) where your cloud disks are created. For information on how to purchase and launch a CVM instance, please see [Purchase and Launch CVM](/doc/product/213/4855).

## Purchasing Cloud Disks
In this example, an ordinary elastic cloud disk is purchased via the console. For more information on how to create a cloud disk, please see [Create Cloud Disk](/doc/product/362/5744).

(1) Log in to [Cloud Block Storage Console](https://console.cloud.tencent.com/cvm/cbs) and click **+ New** to purchase.

(2). In the pop-up box, select **North China (Beijing)** -> **Beijing Zone 1** -> **Prepaid** -> **Cloud Block Storage** -> **20 GB**, set the purchase period to one month, and click **OK**.

(3) On the payment page, click **Confirm Payment** to complete the purchase. On the [Cloud Disk List Page](https://console.cloud.tencent.com/cvm/cbs), you can view the purchased cloud disks. The elastic cloud disk you just purchased is unnamed by default and displayed as <font color="red">To Be Mounted</font>. Click the Edit icon and name it "cbs-test".

## Connecting to a CVM Instance
(1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/).

(2) Go to **CVM** -> **CBS** tab.

(3) On the Cloud Disk List page, click **More** -> **Mount to CVM** button beside the new cloud disk.

(4) In the pop-up box, select the CVM to be mounted to (see Prerequisites), and click **OK**.

## Formatting, Creating a File System and Writing a File
### Connection to a Linux instance

(1) Execute the command `fdisk -l` to view the name of the disk device connected to the instance. Find the created 20 GB cloud disk, assuming its device name is `/dev/vdb`.

(2) Format the device (EXT4 file system is used in this example): Execute the command `mkfs.ext4 /dev/vdb`.

(3) Mount it to point `/data` and execute the following command:
```
mount /dev/vdb /data
```

(4) Enter the device, write a file named `qcloud.txt`, and execute the following command:
```
cd /data
vi qcloud.txt
```
Write something in the editing state, for example: "This is my first test". Press ESC to exit the editing state, and enter `wq` to save the change. Execute the command `ls`, and then you can see that the file has been written to the disk.

For more information on partitioning, formatting, and file system creation on Linux, please see [Partitioning, Formatting, Mounting and File System Creation on Linux](/document/product/362/6735
).

### Connection to a Windows instance
(1). Go to (**Start** ->) **CVM Management** -> **Storage/Computer Management** -> **Disk Management**.

(2) Right-click on the created empty elastic cloud disk and select **Online**.

(3) Right-click on the disk and select **New Simple Volume** in the pop-up shortcut menu. Follow the instructions in the Wizard, and enter the size of the entire disk. Click **Next** to select the file system (When the disk is larger than 2 TB, make sure to select GPT partition). Format the partition, click **Next**, and click **OK**.

(4) The elastic cloud disk is being formatted. After the formatting is completed, it can be used.

(5) Create a file named `qcloud.txt` in the disk. Enter something, and click "Save". Now you have successfully written the file.

For more information on partitioning, formatting, online and file system creation on Windows, please see [Partitioning, Formatting, Online and File System Creation on Windows](https://intl.cloud.tencent.com/document/product/362/6734).

