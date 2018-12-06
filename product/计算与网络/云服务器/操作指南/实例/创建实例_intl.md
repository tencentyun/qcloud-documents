## Prerequisites
Before creating a CVM instance, you need to complete the following steps:

- [Sign up for Tencent Cloud](https://cloud.tencent.com/document/product/378/9603), and complete [Identity Verification](https://cloud.tencent.com/document/product/378/3629).
- To create a CVM instance whose network type is virtual private cloud (VPC), you need to [Create a VPC](https://cloud.tencent.com/document/product/215/8113) in the target region, and [Create a Subnet](https://cloud.tencent.com/document/product/215/8114) in the destination region under the VPC.
- If you do not use the default project created automatically by the system, you need to [Create a Project](https://cloud.tencent.com/document/product/378/8192).
- If you do not use the default security group automatically created by the system, you need to [Create a Security Group](https://cloud.tencent.com/document/product/213/12450) in the target region, and add security group rules that meet your business needs.
- If you need to bind an SSH key pair when creating a Linux instance, you need to [Create an SSH key](https://cloud.tencent.com/document/product/213/516) under the target project.
- To create a CVM instance with custom image, you need to [Create Custom Image](https://cloud.tencent.com/document/product/213/4942) or [Import Image](https://cloud.tencent.com/document/product/213/4945).



## Procedure
(1) Log in to [Tencent Cloud Official Website](https://cloud.tencent.com), select **Product** -> **Computing** -> **CVM**, and then click the **Buy Now** button to enter the CVM purchase page.

- **Quick configuration.** Suitable for conventional scenarios, allowing users to quickly select a CVM instance that meets common needs.

- **Custom Configuration.** Suitable for specific scenarios, allowing users to easily select a CVM instance that meets their own specific needs.

(2) Select a billing method.

- Prepaid or postpaid (users who cannot purchase postpaid CVM should complete [Identity Verification](https://cloud.tencent.com/document/product/378/3629) first). For more information on the billing methods, please see [Billing Methods](https://cloud.tencent.com/document/product/213/2180).

(3) Select a region and availability zone.

- When purchasing cloud services, it is recommended to choose the region that is closest to your customers to minimize the access latency and improve access speed.
- When you need more than one CVMs, it is recommended that you select different availability zones to ensure disaster tolerance.
- For more information on available regions and available zones, please see [Regions and Availability Zones](https://cloud.tencent.com/document/product/213/6091).

(4) Select the series, model, and configuration.

- Tencent Cloud offers three series of instances: Series 1, Series 2 and Series 3. To achieve the best performance, we recommend that you use the latest generation of instances when creating instances. For more information on instance series, please see [Instance Specifications](https://cloud.tencent.com/document/product/213/7153).
- Tencent Cloud offers standard, high IO, MEM optimized, computing, GPU computing, FPGA, big data, and network enhanced instances. For more information on models, please see [Instance Specifications](https://cloud.tencent.com/document/product/213/7153).
- Tencent Cloud provides rich instance configurations, and different models correspond to different instance configurations. For more information on the instance configuration, please see [Instance Specifications](https://cloud.tencent.com/document/product/213/11518).

(5) Select an image.

- Based on different sources, images provided by Tencent Cloud are divided into public images, custom images, shared images, and service marketplace images. For more information on image types, please see [Image Types](https://cloud.tencent.com/document/product/213/4941).

(6) Select a system disk and a data disk.

- System disk: Required. Used for installing the OS. You can select the type and capacity of the cloud disk used as the system disk. The available types of cloud disks vary in different regions. The default capacity of the system disk is 50 GB.
- Data disk: Optional. You can add a data disk after creating an instance, or add a data disk when purchasing an instance, and then select the cloud disk type and capacity for the data disk. You can create an empty data disk, or use a data disk snapshot to create a data disk.
- For more information on cloud block storage, please see [Cloud Block Storage Types](https://cloud.tencent.com/document/product/362/2353).

(7) Select the network type (basic network or VPC).

- Basic network: The basic network is no longer supported in regions launched after August 3, 2017 for all users, and it is also no longer supported for some new accounts registered after June 13, 2017.
- VPC: You must select the VPC and subnet. If you have not created a VPC and subnet, select the default VPC and subnet.
- For more information on basic network and VPC, please see [Product Overview](https://cloud.tencent.com/document/product/215/535).


(8) Select public network IP and billing method of bandwidth (billing by fixed bandwidth or traffic).

- If you need to assign a public IP address to the instance, you need to select **Buy Now**, select **Bill-by-bandwidth** or **Bill-by-traffic**, and set a value greater than 0 Mbps. IP addresses assigned in this way can be unbound with the instance only after being converted into an elastic public network IP, but cannot be unbound directly.
- For more information on the elastic public IP, please see [Elastic Public IP](https://cloud.tencent.com/document/product/213/5733).
- Bill-by-bandwidth: Select a fixed bandwidth. Packet loss occurs if this bandwidth is exceeded. This is suitable for scenarios with minor network fluctuation.
- Bill-by-traffic: The service is charged based on actual traffic usage. You can set a limit for peak bandwidth. Packet loss occurs when the instantaneous bandwidth exceeds this limit. This is suitable for scenarios with large network fluctuations.
- For more information on the bandwidth billing methods, please see [Billing Methods](https://cloud.tencent.com/document/product/213/10578).


(9) Determine the number of servers and the length of purchase (only for CVMs with an annual and monthly plan).

(10) Set auto renewal.

- If you set auto renewal and your account balance is sufficient, the device is automatically renewed upon its expiration on a monthly basis. For more information on auto renewal, please see [Renewal Management](https://cloud.tencent.com/document/product/555/7454).

(11) Set the project.

(12) Set CVM name and login method.

- CVM name: You can choose the CVM naming method as **Name It Now** when purchasing it, and enter a semantic name limited to 60 characters. You can also choose **Name It after Creation**, and the created CVM's name is "Not Named". This name is only displayed on the console, not as the hostname of CVM.
- Login method: For CVMs with Linux images, you can choose **Set Password**, **Associate with Key Immediately**, and **Automatically Generated Password** as the login method. For CVMs with Windows images, you can choose **Set Password** and **Automatically Generated Password** as the login method.

(13) Select the security group.

- If you do not create a security group, select **New Security Group**. If you have an existing security group, select **Existing Security Group**. You can also preview the security group rules. For more information on security group rules, please see [Security Group](https://cloud.tencent.com/document/product/213/5221).

(14) Choose to install security reinforcement and cloud monitoring components.

- Security reinforcement: Activate anti-DDoS service, WAF and CVM Security (YunJing) at no cost. For more information, please see [CVM Security](https://cloud.tencent.com/document/product/296/2221).
- Cloud monitoring: Activate cloud product monitoring at no cost, install components to obtain CVM monitoring metrics and display them in the form of monitor icons, and support customization of alarm threshold. For more information, please see [Cloud Monitoring Overview](https://cloud.tencent.com/document/product/248/13466).

>After the CVM is created, you will get an internal message containing such information as instance name, Public IP address, Private IP address, login name, and initial login password (when you choose the method of "Automatically Generated Password"). You can use the information to log in to and manage instances.




