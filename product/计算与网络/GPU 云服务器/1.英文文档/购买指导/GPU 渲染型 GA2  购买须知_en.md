## Notes About Purchasing GPU Rendering GA2 Instances
The following need to be considered before purchase:
1. Make sure you have got an understanding of [Tencent Cloud GCC instances](/doc/product/560/8015l) and their [configurations and prices](/doc/product/560/8025). Be sure to purchase them based on your actual demand. Refund is not available once you have successfully made the purchase.
2. Currently, only **Beijing Zone 2** is available for GPU rendering GA2 instances. More regions will be supported soon.

## Procedure for Purchasing GPU Rendering GA2 Instances

You can quickly purchase a GPU rendering GA2 instance by following the steps below.
>GPU rendering GA2 instance is under internal trial. You can click [here](https://cloud.tencent.com/act/apply/ga2) to apply for it.

### 1. Log in to Purchase Page
[Click here to go to the purchase page>>](https://buy.cloud.tencent.com/cvm?regionId=8&zoneId=800002&generation=v2&deviceType=ga&tabIndex=1)

### 2. Select Region and Model
In this step, you need to select:
1. Billing method: Prepaid or postpaid.
2. Region and availability zone: Currently, Only **Beijing Zone 2** is supported for GCC instances. 
3. Model and configuration: Select "Series 2" -> "GPU rendering GA2" for model.

After the configuration, click "Next Step: Select an Image".
![](//mc.qcloudimg.com/static/img/4b8bc6bd5b1b838acf064c157f66c361/image.png)
### 3. Select an Image
Four image types are supported for GPU rendering GA2 instances: public images, custom images, shared images and service marketplace images. [Learn more about image >>](/doc/product/213/4940).

GA2 is used with AMD S7150 GPU, which can function normally only if a compatible driver is installed in the server. Provided by AMD, the driver is specifically optimized for the virtualized environment. Users who are using CVMs can install the driver in two ways.

- Select the service marketplace image **AMD GPU Windows Basic Environment V1.0**.
After the configuration, click "Next Step: Select Storage and Network".
![](//mc.qcloudimg.com/static/img/9c653b7a37c8dcb8f0a95d7e548f8739/image.png)
- You can also select an image based on your needs. If you want to create an instance with a public image, only Windows 2008 R2 Enterprise Edition SP1 (64-bit) is supported currently.
![](//mc.qcloudimg.com/static/img/5c8133796dda48a522c5fa76a5adcd57/image.png)
Note: To create an instance with a public image, you need to install the GPU driver from [here](http://mirrors.tencentyun.com/install/windows/s7150_guest_driver.7z). Please NOTE that this is a link within Tencent Cloud private network and needs to be accessed from server. Then, execute Setup.exe to install it. After the installation, go to **Device Manager** to check whether the driver is installed successfully, as shown below.
![](//mc.qcloudimg.com/static/img/831923fe6942f4cb03640cffdb5883fd/image.png)
### 4. Select Storage and Network
In this step, you need to select:
- Storage: The sizes of system disk and data disk of your GCC instance depends on the configuration you made in step 3.
	1. System disk: SSD cloud storage
	2. Data disk: SSD cloud storage. Alternatively, you can [Create Cloud Disk](/doc/product/362/5744#.E5.88.9B.E5.BB.BA.E5.BC.B9.E6.80.A7.E4.BA.91.E7.9B.98) and mount the disk after you have successfully purchased your GCC instance.
- Network: Choose network type (basic network or VPC) and public network bandwidth (charge by fixed bandwidth or by traffic usage).
	1. Network type:
		(1) Basic network: Suitable for new users. CVMs of the same user are interconnected via private network.
		(2) VPC: Suitable for advanced users. Different VPCs are logically isolated from each other.
	2. Public network bandwidth:
		(1) Charge by fixed bandwidth: Select a fixed bandwidth. Packet loss occurs if this bandwidth is exceeded. This is suitable for scenarios with minor network fluctuation.
		(2) Charge by traffic usage: The service is charged based on actual traffic usage. You can set a limit for peak bandwidth. Packet loss occurs when the instantaneous bandwidth exceeds this limit (suitable for scenarios with large network fluctuations).
- Configure instance quantity and purchased usage period

After the configuration, click "Next Step: Configure Information"

### 5. Configure Information
In this step, you need to:
- Configure instance name (optional) and password.
- Select security group

After the configuration, click "Buy Now".
### 6. Check the Instance
After the payment is made, go to the [Console](https://console.qcloud.com/cvm) to check the purchased instance in your mailbox.
When a GA2 instance is purchased, you will receive an internal message containing information such as instance name, public IP address, private IP address, login name, and initial login password. Use these information to log in to and manage your instance. You're recommended to change your login password as soon as possible for security.



