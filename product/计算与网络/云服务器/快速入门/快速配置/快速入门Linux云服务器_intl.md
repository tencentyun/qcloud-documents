
This document describes how to use the features of Linux CVM to help beginners quickly get started with the creation and configuration of Tencent Cloud CVM.
<div id="page1"></div>
## Step 1: Prepare and Select Model
### Signing up for a Tencent Cloud Account
New users need to [register](
https://intl.cloud.tencent.com/register) with Tencent Cloud official website. For more information, please see [How to Sign up for Tencent Cloud](/doc/product/378/9603).

### Specifying the Region and Availability Zone in Which the CVM Resides
How to select region:
 - Near user's region.
The region of a CVM should be selected depending on your user's geographical location. The closer the CVM is to your users who access it, the shorter the access latency and the higher the access speed will be. For example, if most of your users are located near Yangtze River Delta, then Shanghai would be a good choice.
 - Communicate via private network in the same region.
CVMs in the same region are interconnected with each other via private network, but those in different regions cannot communicate with each other via private network. Users who communicate with each other using multiple CVMs via private network need to choose the same region.
CVMs in the same region can communicate with each other via private network free of charge.
CVMs in different regions cannot communicate with each other via private network but only via public network with a charge.

### Selecting CPM Configuration Solution
The following configurations are recommended: ["Model Recommendation"](https://cloud.tencent.com/act/recommended)
- Entry: Suitable for start-up personal websites. For example, small websites such as personal blogs.
- Basic: Suitable for websites or applications with a certain number of visits. For example, large enterprise official websites, small e-commerce websites.
- Universal: Suitable for scenarios where cloud computing is frequently used. For example, portals, SaaS software, small Apps.
- Application: Suitable for applications demanding high concurrency and scenarios with high requirement for CVM network and computing. For example, large portals, e-commerce websites, game Apps.

If recommended configuration does not meet your needs, you can compare the configurations in [More Models](https://buy.cloud.tencent.com/cvm?tab=custom&regionId=4&step=1 ) based on your actual needs. You can also [Upgrade Configuration](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-配置升级) or [Downgrade Configuration](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-配置降级) at any time after purchasing a CVM based on your business needs.

### Choosing Billing Method
Tencent Cloud provides two billing methods: Prepaid and Postpaid. For more information, please see [Billing Methods](/doc/product/213/2180).
If Postpaid method is selected, you need to complete [Identity Verification](https://console.cloud.tencent.com/developer/infomation).

<div id="page2"></div>
## Step 2: Create Linux CVM
This step introduces how to create a Linux CVM. If it does not meet your requirements, you can configure your CVM by referring to [Custom Configuration of Linux CVM](/doc/product/213/10517) document.



<div id="page3"></div>
## Step 3: Log in to Linux CVM
This section describes how to log in to a Linux CVM. Login method varies depending on different scenarios. This step shows how to log in to the CVM through the console. For more information on other login methods, please see [Log in to Linux Instance](/doc/product/213/5436).

### Prerequisites
You need to use the admin account ID and the corresponding password to log in to the CVM.

 * Admin account ID: It is always root for Linux instances (ubuntu for Ubuntu system users)
 * Password: For quick configuration, the initial password is randomly assigned by the system. For detailed operations, see next section (View Internal Message and CVM Information).
 	For more information, please see [Login Password](/doc/product/213/6093).
   
### Viewing Internal Message and CVM Information
After a CVM is purchased and created, the instance name, public IP address, private IP address, login name, initial login password and other information of the CVM are sent to your account via [Internal Message](https://console.cloud.tencent.com/message).
![](https://main.qcloudimg.com/raw/f6085b53103a5db0e944d0fd971c73fc.png)
 1) Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/index). You can see the public IP address, private IP address and other information after login.
 
 2. Click **Internal Message** at the upper right corner.
 
 3. New CVM and information including login name and password can be found in the Internal Message page.


### Logging in to CVM Through the Console
 1. Click **Log in** button in the operation column on the CVM list page to log in to the Linux CVM through WebShell.
	![](https://main.qcloudimg.com/raw/fa2582e16ef7e865d225abcd3487005d.png)
	
 2. Enter the account ID "root" ("ubuntu" for Ubuntu system users) and the initial password from the internal message (or the modified password) to log in.

>**Note:**
>This terminal is exclusive, that is, only one user can log in through the console at a time.

<div id="page4"></div>
## Step 4: Partition and Format Data Disk

### Prerequisites
 - Users who have purchased the data disk need to format it before use. Users who do not purchase data disk can skip this step.
 - Make sure you have completed Step 3 to log in to the CVM.
 - Mount data disks larger than 2 TB using GPT method. For more information, please see [Partition and Format Data Disk Using GPT Partition Table](/doc/product/213/2043).
 
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

	In this example, we only create one partition. Developers can create multiple partitions according to their own needs.
	![](//mc.qcloudimg.com/static/img/8a9c8ff4db5a7e4622bf2968d0309129/image.png)

 4. Use `fdisk -l` command to check that the new partition vdb1 has been created.
	![](//mc.qcloudimg.com/static/img/304ccd9491f2a25b8d3b33b5213faa0e/image.png)

### Formatting Data Disk

 1. Format a new partition
 The newly created partition needs to be formatted. You can use a file system format based on your own needs, such as ext2 or ext3. In this example, ext3 is used.
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
	Use the following command to view the status of mounting:
	```
	df -h
	```
	The information of vdb1 shown in the red box indicates that the mounting is successful and the data disk is displayed.
	![](//mc.qcloudimg.com/static/img/d6bc35b30b823c567812affd032bfedf/image.png)

 3. Configure auto mount upon startup
To allow your CVM to be automatically mounted with data disk when it is restarted or started up, add the partition information to `/etc/fstab`.
Use the following command to add partition information:
	```
	echo '/dev/vdb1 /mydata ext3 defaults 0 0' >> /etc/fstab
	```
	Use the following command to make a check:
	```
	cat /etc/fstab
	```
	The information of vdb1 shown in the red box indicates that the partition information has been successfully added.
	![](//mc.qcloudimg.com/static/img/39025e909cd849d5a34378a7d0078d13/image.png)
	
**Now, you have completed the creation and basic configuration of a Linux CVM.**

