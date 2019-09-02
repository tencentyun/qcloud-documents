## Purchasing GPU Computing GN8 Instance
The following need to be considered before purchase:
1. Make sure you have got an understanding of [Tencent Cloud GCC instances](/doc/product/560/8015l) and their [configurations and prices](/doc/product/560/8025). Be sure to purchase them based on your actual demand. Refund is not available once you have successfully made the purchase.
2. Currently, **Guangzhou Zone 3**, **Beijing Zone 2** and **Chengdu Zone 1** are available for GPU computer GN8 instances. More regions will be supported soon.



## Procedure for Purchasing GPU Computing GN8 Instances
You can quickly purchase a GPU computing GN8 instance by following the steps below.
### 1. Log in to Purchase Page
[Click here to go to the purchase page>>](https://buy.cloud.tencent.com/cvm?regionId=8&zoneId=800002&generation=v2&deviceType=gpu&tabIndex=1)
### 2. Select Region and Model
In this step, you need to select:
1. Billing method: Prepaid or postpaid.
2. Region and availability zone: Currently, only the following zones are supported for GPU GN8 instances: **Guangzhou Zone 3**, **Beijing Zone 2** and **Chengdu Zone 1**.
3. Model and configuration: "GPU computing GN8" for model. You can choose from the three configurations we provided according to your needs.

After the configuration, click **Next Step: Select an Image**.
 ![](//mc.qcloudimg.com/static/img/db914ea989c976c7cb053b11cc96f4fe/GN8_select.png)
### 3. Select an Image
Four images types are supported for GCC instances: public images, custom images, shared images and service marketplace images. [Learn more about image >>](/doc/product/213/4940).
Those who have just started using Tencent Cloud can select "public images" and choose the version as you need. Three public images are provided for GCC instance: CentOS, Ubuntu, Windows Server. Choose one of these public images according to your needs.

![](//mc.qcloudimg.com/static/img/7701f037e9f301130f13974691168849/GN8_image.png)

**Note:**
**GCC instances can only operate normally with a compatible GPU driver.**

- If you install a public image, an created GPU instance can function normally only when the GPU driver is installed. For more information on driver installation, please see [How to Install NVIDIA Driver](https://cloud.tencent.com/document/product/560/8048).


 After the configuration, click "Next Step: Select Storage and Network".

### 4. Select Storage and Network
In this step, you need to select:
- Storage: The sizes of system disk and data disk of your GCC instance is freely to chose .
	1. System disk:  Cloud Block Storage/SSD Cloud Storage/Local SSD Disk.
	2. Data disk: Cloud Block Storage/Premium Cloud Storage(white list)/SSD Cloud Storage/Local SSD Disk.
- Network: Choose network type (basic network or VPC) and public network bandwidth (charge by fixed bandwidth or by traffic usage).
	1. Network type:
		(1) Basic network: Suitable for new users. CVMs of the same user are interconnected via private network.
		(2) VPC: Suitable for advanced users. Different VPCs are logically isolated from each other.
	2. Public network bandwidth:
		(1) Charge by fixed bandwidth: Select a fixed bandwidth. Packet loss occurs if this bandwidth is exceeded. This is suitable for scenarios with minor network fluctuation.
		(2) Charge by traffic usage: The service is charged based on actual traffic usage. You can set a limit for peak bandwidth. Packet loss occurs when the instantaneous bandwidth exceeds this limit (suitable for scenarios with large network fluctuations).
- Configure instance quantity and purchased usage period.

After the configuration, click "Next Step: Configure Information"
![](//mc.qcloudimg.com/static/img/b1b51645f6c224dd8128c46828640d72/storage_net.png)
### 5. Configure Information
In this step, you need to:
- Configure instance name (optional) and password.
- Select security group

After the configuration, click "Buy Now".
### 6. Check the Instance
After the payment is made, go to the [Console](https://console.cloud.tencent.com/cvm) to check the purchased instance in your mailbox.
When a GCC instance is purchased, you will receive an internal message containing information such as instance name, public IP address, private IP address, login name, and initial login password. Use these information to log in to and manage your instance. You're recommended to change your login password as soon as possible for security.
![](//mc.qcloudimg.com/static/img/2003b614e24ea973f9c03a9c084380ce/image.png)



