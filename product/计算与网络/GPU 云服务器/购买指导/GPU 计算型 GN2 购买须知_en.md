## Purchasing GPU Computing GN2 Instance
The following need to be considered before purchase:
1. Make sure you have got an understanding of [Tencent Cloud GCC instances](/doc/product/560/8015l) and their [configurations and prices](/doc/product/560/8025). Be sure to purchase them based on your actual demand. Refund is not available once you have successfully made the purchase.
2. Currently, **Guangzhou Zone 3**, **Shanghai Zone 1**, **Shanghai Zone 2**, **Beijing Zone 2** and **Shenzhen Finance Zone 1** are available for GPU rendering GA2 instances. More regions will be supported soon.
>**Note:**
> "Shenzhen Finance Zone" is only available to customers from financial sectors.


## Procedure for Purchasing GPU Computing GN2 Instances
You can quickly purchase a GPU computing GN2 instance by following the steps below.
### 1. Log in to Purchase Page
[Click here to go to the purchase page>>](https://buy.cloud.tencent.com/cvm?regionId=8&zoneId=800002&generation=v2&deviceType=gpu&tabIndex=1)
### 2. Select Region and Model
In this step, you need to select:
1. Billing method: Prepaid or postpaid.
2. Region and availability zone: Currently, only the following zones are supported for GCC instances: **Guangzhou Zone 3**, **Shanghai Zone 1**, **Shanghai Zone 2**, **Beijing Zone 2** and **Shenzhen Finance Zone 1**.
3. Model and configuration: Select "Series 2" -> "GPU computing GN2" for model. You can choose from the two configurations we provided according to your needs.

After the configuration, click **Next Step: Select an Image**.
 ![](//mc.qcloudimg.com/static/img/550bf1efa9c9471d2967192f2d0e7478/image.png)
### 3. Select an Image
Four images types are supported for GCC instances: public images, custom images, shared images and service marketplace images. [Learn more about image >>](/doc/product/213/4940).
Those who have just started using Tencent Cloud can select "public images" and choose the version as you need. Three public images are provided for GCC instance: Centos, Ubuntu, Windows Server. Choose one of these public images according to your needs.

![](//mc.qcloudimg.com/static/img/63210bc3654107b68336d1e92789b000/image.png)

**Note:**
**GCC instances can only operate normally with a compatible GPU driver.**

- If you install a public image, an created GPU instance can function normally only when the GPU driver is installed. For more information on driver installation, please see [How to Install NVIDIA Driver](https://cloud.tencent.com/document/product/560/8048).
- The service marketplace images with GPU driver are provided.
 - Select "Service Marketplace Images" -> "Select from Service Marketplace"
![](//mc.qcloudimg.com/static/img/ee7d1e5401bbfa03c43a6990fd619949/image.png)
 - Search for "M40 GPU"
![](//mc.qcloudimg.com/static/img/18b79dc307d14d95477078b9ec5e728c/image.png)
 - We provide two types of service marketplace images: public images CentOS 7.2 (64-bit) and Ubuntu 16.04 LTS (64-bit) with preinstalled TESLA NVIDIA M40 GPU Driver and CUDA Toolkit 7.5. You can directly use these images without the need to install the GPU driver. Select a desired image type, and click "Free to Use".

 After the configuration, click "Next Step: Select Storage and Network".

### 4. Select Storage and Network
In this step, you need to select:
- Storage: The sizes of system disk and data disk of your GCC instance depends on the configuration you made in step 3.
	1. System disk: Always 50 GB local SSD.
	2. Data disk: Local SSD is provided as data disk for GCC instances. You can [Create Cloud Disk](/doc/product/362/5744#.E5.88.9B.E5.BB.BA.E5.BC.B9.E6.80.A7.E4.BA.91.E7.9B.98) and mount the disk after you have successfully purchased your GCC instance.
- Network: Choose network type (basic network or VPC) and public network bandwidth (charge by fixed bandwidth or by traffic usage).
	1. Network type:
		(1) Basic network: Suitable for new users. CVMs of the same user are interconnected via private network.
		(2) VPC: Suitable for advanced users. Different VPCs are logically isolated from each other.
	2. Public network bandwidth:
		(1) Charge by fixed bandwidth: Select a fixed bandwidth. Packet loss occurs if this bandwidth is exceeded. This is suitable for scenarios with minor network fluctuation.
		(2) Charge by traffic usage: The service is charged based on actual traffic usage. You can set a limit for peak bandwidth. Packet loss occurs when the instantaneous bandwidth exceeds this limit (suitable for scenarios with large network fluctuations).
- Configure instance quantity and purchased usage period (currently, the maximum usage period supported for GCC instances in a single purchase is 5 months).

After the configuration, click "Next Step: Configure Information"
![](//mc.qcloudimg.com/static/img/fad7f5a70733d8d2b8eea5ca4d675f2f/image.png)
### 5. Configure Information
In this step, you need to:
- Configure instance name (optional) and password.
- Select security group

After the configuration, click "Buy Now".
### 6. Check the Instance
After the payment is made, go to the [Console](https://console.cloud.tencent.com/cvm) to check the purchased instance in your mailbox.
When a GCC instance is purchased, you will receive an internal message containing information such as instance name, public IP address, private IP address, login name, and initial login password. Use these information to log in to and manage your instance. You're recommended to change your login password as soon as possible for security.
![](//mc.qcloudimg.com/static/img/2003b614e24ea973f9c03a9c084380ce/image.png)



