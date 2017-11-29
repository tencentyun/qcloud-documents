
This document describes how to easily use the features of CVM instances on Windows system and is designed to help beginners to get started with the creation and configuration of Tencent Cloud CVM quickly.

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
You can compare the configurations in [More Models](https://intl.cloud.tencent.com/document/product/213/7153) based on your actual needs. You can also [Upgrade Configuration](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-配置升级) or [Degrade Configuration](/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-配置降级) at any time after purchasing a CVM based on your actual needs.
>**Note:**
> Windows CVM cannot be used as [Public Network Gateway](/doc/product/215/%E7%BD%91%E5%85%B3#1.-公网网关). If you want to use public network gateway, please refer to [Quick Start for Linux CVM](/doc/product/213/2936).

### Choosing Billing Method
Tencent cloud supports Postpaid billing method. For more information, please see [Billing Methods](/doc/product/213/2180).
If Prepaid method is selected, you need to complete [Identity Verification](https://console.cloud.tencent.com/developer/infomation).

<div id="page2"></div>
## Step 2: Create a Windows CVM
This step describes how to create a Windows CVM. Let's take quick configuration as an example. If it does not meet your requirements, you can choose a detailed configuration by referring to [Customized Configuration of Windows CVM](/doc/product/213/10516) document.

![](//mc.qcloudimg.com/static/img/fa3a62404421c2fab5c8e08b6fe40588/image.png)

 1. Log in to Tencent Cloud official website, go to **Products** -> **Compute** -> **Cloud Virtual Machine**, then click the **Experience** button to go to [CVM Purchase Page](https://console.cloud.tencent.com/cvm/index), and click **+ NEW** to start purchase.

 2. Select an image. Select a Windows operating system that meets your requirement.
 
 3. Select a model.
 
 4. Select a region. Choosing a region close to your users can minimize access latency and improve download speed.
 
 5. Select public network bandwidth. If you do not need to connect to the public network, set the bandwidth value to 0.
 
 6. Select CVM quantity and the usage period.

 7. Set account name and login method.
 
For more information on how to view internal message, please see later steps.
 
<div id="Inter-Page">  </div>
## Step 3: Log in to Windows CVM
This section describes how to log in to the Windows CVM. You can use different login methods in different situations. We describe the steps to login on Console here. For more information on other login methods, please see [Log in to Windows Instance](/doc/product/213/5435).

### Preconditions
You need to use the admin account ID and the corresponding password to log in to the CVM.

 * Admin account ID: It is always Administrator for Windows instances
 * Password: For quick configuration, the initial password is randomly assigned by the system. For detailed operations, see next section (View Internal Message and CVM Information).
   For more information, please see [Login Password](/doc/product/213/6093).
   
### Viewing Internal Message and CVM Information
After a CVM is purchased and launched, the instance name, public IP address, private IP address, login name and initial login password of the CVM are sent to your account via [Internal Message](https://console.cloud.tencent.com/message).

![](//mc.qcloudimg.com/static/img/da559439d58296f6da3ff28c2c1ab952/image.png)
 1. Log in to [CVM Console](https://console.cloud.tencent.com/cvm/index) to check public IP address, private IP address and other information of the CVM.

 2. Click **Internal Message** at the upper right corner.

 3. New CVM and information including login name and password can be found in Internal Message page.

.
### Logging in to CVM via Console
 1. In the Action column of CVM list, click **Log In** button to connect to Windows CVM via VNC.
	![](//mc.qcloudimg.com/static/img/2458a30dd79da5762ea6cf474755319e/image.png)

 2. Select **Ctrl-Alt-Delete** from the top left corner, go to the system login interface:
	![](//mc.qcloudimg.com/static/img/e4dbc02ca9ae2a7cb9ada5316effd31a/image.png)
	
 3. Enter the account ID (Admin) and the initial password from the internal message (or the password modified by you) to log in.

>**Note:**
>This terminal is exclusive, that is, only one user can log in through the console at a time.

<div id="page4"></div>
## Step 4: Format and Partition Data Disk

The following example describes how to format a data disk on Windows 2012 R2.

### Preconditions
 - After purchasing the data disks, you need to format them. Skip this step if you don't need data disks.
 - Make sure you have logged in to the CVM as described in Step 3.

### Formatting Data Disk

 1. Log in to Windows CVM by following the method described in Step 3.

 2. Click **Start** -> **Server manager** -> **tool** - **Computer management** -> **storage** -> **Disk management**.

 3. Right click on Disk 1 and select **Online**:
	![](//mc.qcloudimg.com/static/img/1217193557509925a622dcdb81aa2e35/image.png)

 4. Right click and select **Initialize disk**:
	![](//mc.qcloudimg.com/static/img/94ab92867d77ea69bc803a0b20f2b941/image.png)

 5. Select **GPT** or **MBR** depending on the partitioning method, and click the **OK** button:
 > **Note:**
 > Make sure to select GPT as partitioning method if the disk is larger than 2 TB.
	![](//mc.qcloudimg.com/static/img/1f7b0f72767193cfa662e188c86cf31b/image.png)

## Disk Partitioning (Optional)

 1. Right click on unallocated space, and select **New Simple Volume**:
	![](//mc.qcloudimg.com/static/img/a6ca720af2082d7a470ece17a8e13f5d/image.png)

 2. In the **New Simple Volume Wizard** pop-up window, click **Next**:
	![](//mc.qcloudimg.com/static/img/10fdcd70b510a57919c6a40cf43452a7/image.png)

 3. Enter the desired disk size for the partition, and click **Next**:
	![](//mc.qcloudimg.com/static/img/05c8d1425a0208597b1d2c75a9c811b6/image.png)

 4. Enter the drive letter, and click **Next**:
	![](//mc.qcloudimg.com/static/img/737ed569049ad617715efb06fe44e7b2/image.png)

 5. Select **File System** -> **Format Partition**, and click **Next**:
	![](//mc.qcloudimg.com/static/img/896cb3f2705fb9fcd04c236b8fb9ec59/image.png)

 6. Upon completing the New Simple Volume operation, and click **Complete**:
	![](//mc.qcloudimg.com/static/img/1e257b9c76d80f30b34f612496b8007b/image.png)

 7. Open **Computer** in **Win** to view the new partition:
	![](//mc.qcloudimg.com/static/img/1cbb4ad1c3c01852a00a1415526a3e12/image.png)

**Now, you have completed the creation and basic configuration of a Windows CVM.**

