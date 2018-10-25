To help users get started with Tencent Cloud's Cloud Block Storage quickly, we provide an example in this document on how to create an empty elastic cloud disk `cbs-test` in Beijing zone (For more information about elastic cloud disk, refer to [Categories of Cloud Block Storage](/doc/product/362/2353); for instructions on how to create a cloud disk containing data, refer to [Creating Cloud Disk from Snapshot](/doc/product/362/5757)), connect it to a CVM instance, create a file system and write a file named `qcloud.txt` to the system.

## Preconditions
To use cloud block storage as described in this document, please make sure that you have a running CVM instance available in the region and availability zone where the cloud disk is to be created (in this example, in the Beijing Zone 1). For instructions on how to create and activate a CVM instance, please refer to [Purchasing and Activating CVM](/doc/product/213/4855).

## Purchasing Cloud Disk
In this example, you purchase an elastic cloud disk through console. For more information on how to create a cloud disk, refer to [Creating a Cloud Disk](/doc/product/362/5744).

1) Log in to [Cloud Block Storage Console](https://console.cloud.tencent.com/cvm/cbs), click ![](//mccdn.qcloud.com/static/img/acaf7d7ec8c66cd55ab9dd1be3319dfb/image.png) to purchase a cloud disk.

2) In the pop-up box, select "North China (Beijing)" - "Beijing Zone 1", "Annual or Monthly Plan", "Cloud Block Storage", "20GB", and select "1 month" as the purchase period, then click "OK".

3) Click "Payment Completed" in the payment page and complete the purchase. You can check the purchased cloud disk in the [CBS List Page](https://console.cloud.tencent.com/cvm/cbs). The elastic cloud disk you just purchased is unnamed by default, and has a status of <font color="red">Pending mounted</font>. Click the "Edit" icon and name it "cbs-test".

## Connecting to CVM instance
1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Go to "Cloud Virtual Machine" - "Cloud Block Storage" tab.

3) In the CBS list page, click "More" - "Mount to CVM" button next to the new cloud disk.

4) In the pop-up box, select the CVM to which the cloud disk needs to be mounted (refer to "Preconditions") and click "OK".

## Formatting, Creating File System and Writing a File
### If connecting to an instance on Linux

1) Execute the command `fdisk -l` to check the name of the disk device connected to the instance. Find the 20 GB cloud disk you just created. Let's suppose that its device name is `/dev/vdb`.

2) Format the device (this example uses an EXT4 file system): Execute the command `mkfs.ext4 /dev/vdb`.

3) Mount to the `/ data` mount point and execute the following command:
```
mount /dev/vdb /data
```

4) Enter the device, and write a file named `qcloud.txt` and execute the following command:
```
cd /data
vi qcloud.txt
```
Write some content in the edit mode, such as: "This is my first test". After pressing ESC to exit the edit mode, enter `wq` to save the changed content. When executing the` ls` command, you'll find that the file has been written to the disk.

.For more information on partitioning, formatting  and file system creation on Linux system, please refer to [Partitioning, Formatting, Mounting and File System Creation on Linux System](https://cloud.tencent.com/document/product/362/6735).



### If connecting to an instance on Windows
1) Go to "Disk Management" page by following the path of ("Start"-) "CVM Management" - "Storage/Computer Management" - "Disk Management".

2) Right-click the empty elastic cloud disk you just created, and select "Online".

3) Right-click the disk, and select "New Simple Volume" in the pop-up shortcut menu. As instructed by the wizard, enter the disk size and click "Next"; select the file system (make sure to select GPT as the partition format if the disk is larger than 2TB); format the partition, click "Next", then click "Finish":

4) You'll be prompted that the formatting is in progress. When formatting is completed, you can use the elastic cloud disk.

5) Enter the disk created, create a file called `qcloud.txt`, enter the required content, click "Save". Now, the writing of file has been completed.

For more information on partitioning, formatting, going online and file system creation on Windows system, please refer to [Partitioning, Formating, Going Online and File System Creation on Windows System](https://cloud.tencent.com/document/product/362/6734
).
