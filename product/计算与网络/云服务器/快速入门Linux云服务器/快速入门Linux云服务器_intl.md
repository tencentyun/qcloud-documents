
This document describes how to easily use the features of CVM instances on Linux system and is designed to help beginners to get started with the creation and configuration of Tencent Cloud CVM quickly.

<div id="page1"></div>
## Step 1: Prepare and Select Model
### Signing up for a Tencent Cloud Account
For new users to Tencent Cloud, please [Register](https://intl.cloud.tencent.com/register) at Tencent Cloud official website. For more information, please see [Signing Up for Tencent Cloud](/doc/product/378/9603).

### Specifying the Region and Availability Zone
Rules for region selection:
 - Be close to your users
The region of a CVM should be selected depending on your users' geographical location. The closer the CVM is to your customers who access it, the shorter the access latency and the higher the access speed will be. For example, if most of your users are in North America, then Toronto is a good choice.
 - In the same region
CVMs in the same region communicate with each other via private network, If you need to use multiple CVMs via private network need to choose the same region.
CVMs in the same region can communicate with each other via private network free of charge.
CVMs in different regions cannot communicate with each other via private network but only via public network with a charge.

### Choosing Configurations
Check details of different configurations in [More Models](https://intl.cloud.tencent.com/document/product/213/7153). You can also [Upgrade Configuration](https://intl.cloud.tencent.com/document/product/213/5730) purchased CVMs whenever necessary.

### Choosing Billing Method
Tencent cloud supports Postpaid billing method. For more information, please see [Billing Methods](/doc/product/213/2180).
If Prepaid method is selected, you need to complete [Identity Verification](https://console.cloud.tencent.com/developer/infomation).

<div id="page2"></div>
## Step 2: Create Linux CVM
This step describes how to create a Linux CVM. Let's take quick configuration as an example.



 1.Log in to Tencent Cloud official website, go to **Products** -> **Compute** -> **Cloud Virtual Machine**, then click the **Experience** button to go to [CVM Purchase Page](https://console.cloud.tencent.com/cvm/index), and click **+ NEW** to start purchase.
![](//mc.qcloudimg.com/static/img/51e3ba45030b206b51f7a03b05d4a757/image.png)

 2.Select a model.
 
 3.Select a region. Choosing a region close to your users can minimize access latency and improve download speed.![](//mc.qcloudimg.com/static/img/8a2ea5f4d088d2beac5686a8364994d7/image.png)
 
 4.Select an image. Select a Linux operating system that meets your requirement.
 ![](//mc.qcloudimg.com/static/img/351555b94d60fae965b315404f0f37af/image.png)
 5.Select public network bandwidth. If you do not need to connect to the public network, set the bandwidth value to 0.
 6.Select CVM quantity and the usage period.
![](//mc.qcloudimg.com/static/img/727646454414ef49b6891c7b5a96cc3a/image.png)
 7.Set account name and login method.
 ![](//mc.qcloudimg.com/static/img/671d4120d3f7578087d85a84d0e824f9/image.png)
For more information on how to view internal message, please see later steps.
 
<div id="Inter-Page">  </div>
## Step 3: Log in to Linux CVM
This section describes how to log in to the Linux CVM. You can use different login methods in different situations. We describe the steps to login on Console here. 

### Preconditions
You need to use the admin account ID and the corresponding password to log in to the CVM.

 * Admin account ID: It is always *root* for Linux instances (*ubuntu* for Ubuntu system users)
 * Password: For quick configuration, the initial password is randomly assigned by the system. For detailed operations, see next section (View Internal Message and CVM Information).
   For more information, please see [Login Password](/doc/product/213/6093).
   
### Viewing Internal Message and CVM Information
After a CVM is purchased and launched, the instance name, public IP address, private IP address, login name and initial login password of the CVM are sent to your account via [Internal Message](https://console.cloud.tencent.com/message).

![](//mc.qcloudimg.com/static/img/4af14d1f95582f48e42912441def19b0/image.png)
 1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/index). You can see the public IP address, private IP address and other information after login.

 2. Click **Internal Message** at the upper right corner.

 3. New CVM and information including login name and password can be found in Internal Message page.


### Log in to CVM Through the Console
 1. In the Action column of CVM list, click **Log In** button to connect to Linux CVM via VNC.
	![](//mc.qcloudimg.com/static/img/2458a30dd79da5762ea6cf474755319e/image.png)

 2. Select **Ctrl-Alt-Delete** from the top left corner, go to the system login interface:
	![](//mc.qcloudimg.com/static/img/ac56e378386a3e6fbc3eaa50ba80358c/image.png)
	
 3. Enter the account ID (Admin) and the initial password from the internal message (or the password modified by you) to log in.

>**Note:**
>This terminal is exclusive, that is, only one user can log in through the console at a time.

<div id="page4"></div>
## Step 4: Partition and Format Data Disk

### Preconditions
 - After purchasing the data disks, you need to format them. Skip this step if you don't need data disks.
 - Make sure you have logged in to the CVM as described in Step 3.
 - Data disks larger than 2 TB should be mounted via GPT method. For more information, please see [Partition and Format Data Disk Using GPT Partition Table](/doc/product/213/2043).
 
### Partitioning Data Disk

 1. Log in to Linux CVM by following the method described in Step 3.

	> **Note:**
	> It only supports partitioning of data disk, not system disk. Forced partitioning of system disk may lead to system crash or other serious problems, for which Tencent Cloud shall not be held liable.

 2. Enter the command `fdisk -l` to check the data disk information.
	In this example, a 54 GB data disk `(/vdb)` needs to be mounted.
	>**Note:**
	> Both `fdisk -l` and `df -h` commands are used to check the data disk information. However, using the command `df -h` does not display the information of the data disk if it has not been partitioned and formatted.

	![](//mc.qcloudimg.com/static/img/f26b5a092e1521556410afdc75a95474/image.png)

 3. Partition the data disk. Perform the operations below by following the instructions on the interface:

 	(1) Enter `fdisk /dev/vdb` (partition the data disk), and press Enter.
 	(2) Enter `n` (create a new partition), and press Enter.
 	(3) Enter `p` (create an extended partition), and press Enter.
 	(4) Enter `1` (use the first primary partition), and press Enter.
 	(5) Press Enter (use default settings).
 	(6) Press Enter again (use default settings).
 	(7) Enter `wq` (save partition table), and press Enter to start partitioning.

	In this example, we only create one partition. You can create multiple partitions according to your actual needs.
	![](//mc.qcloudimg.com/static/img/8a9c8ff4db5a7e4622bf2968d0309129/image.png)

 4. Use `fdisk -l` command to check that the new partition `vdb1` has been created.
	![](//mc.qcloudimg.com/static/img/304ccd9491f2a25b8d3b33b5213faa0e/image.png)

### Formatting Data Disk

 1. Format a new partition
 The newly created partition needs to be formatted. You can decide the file system format on your own, such as ext2 and ext3. The example here uses ext3.
Use the following command to format the new partition: 
	```
	mkfs.ext3 /dev/vdb1
	```
	![](//mc.qcloudimg.com/static/img/fce59c4aba93c688c429fe4760452264/image.png)

 2. Mount the partition
	Use the following command to create mydata directory and mount the partition under this directory:
	```
	mkdir /mydata
	mount /dev/vdb1 /mydata
	```
	Use the command to view the status of mounting:
	```
	df -h
	```
	If the following message appears, the disk is succesfully mounted. You can view the data disk.
	![](//mc.qcloudimg.com/static/img/d6bc35b30b823c567812affd032bfedf/image.png)

 3. Configure auto mount upon startup
If you want the data disk to be automatically mounted to CVM when CVM is restarted or started up, you need to add the partition information to `/etc/fstab`.
Use the following command to add partition information:
	```
	echo '/dev/vdb1 /mydata ext3 defaults 0 0' >> /etc/fstab
	```
	Use the following command to make a check:
	```
	cat /etc/fstab
	```
	If the following message appears, the partition information has been successfully added.
	![](//mc.qcloudimg.com/static/img/39025e909cd849d5a34378a7d0078d13/image.png)
	
**Now, you have completed the creation and basic configuration of a Linux CVM.**

