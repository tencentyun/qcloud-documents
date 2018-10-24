## 1. Purchase Instances 
Log in to the [Tencent Cloud official website](https://cloud.tencent.com/), click the menu shown in the following figure to go to the [MongoDB Overview](https://cloud.tencent.com/product/mongodb) page.
![](https://main.qcloudimg.com/raw/0ca36011c0ea72c457079c869a3149d7.png)
Click **Buy Now** to go to the [product purchase page](https://buy.cloud.tencent.com/mongodb).
![](https://main.qcloudimg.com/raw/db8d147eeb15b9716516cf40271d4b04.png)
The product purchase page mainly covers the following settings, which are described in detail below.
### 1.1 Billing method and region
#### (1) Billing method 
The postpaid method is supported, which is applicable to scenarios where the business volume fluctuates dramatically at a certain time. If large fluctuations exist in business development and cannot be predicted accurately, or resources may be used in special or emergency case, it is recommended to choose the postpaid mode. In the postpaid mode, when you create a cloud MongoDB storage, the system freezes the hardware cost of an hour in your cloud account and makes a settlement every hour on the hour, with a time granularity down to second. In this mode, you are charged for the actual usage of the Cloud MongoDB Service, without the need to make any advance payments.
#### (2) Regions
Tencent Cloud's hosting data centers are distributed globally, covering Southeast Asia, Asia Pacific, US West, US East, North America, Europe and other overseas regions. More regions will be available to deploy more nodes.<br>
Notes: <br>

- Cloud products in the same region communicate with each other over the private network, but the private networks for the resources under different accounts are completely isolated from each other.
- Cloud products in different regions cannot communicate with each other over the private network.
- Tencent Cloud resources in different regions cannot access each other over the private network.
- Select a region closest to your customers when purchasing cloud services to minimize the access latency.

#### (3) Availability zone
Availability zones are Tencent Cloud's physical IDCs with power facilities and networks independent of each other within the same region. They are designed to ensure that failures within an availability zone can be isolated (except for large-scale disaster or major power failure) without spreading to other zones, so as to ensure your business stability. Availability zones in the same region communicate with each other over the private network, and network latency is shorter for products within the same availability zone.
### 1.2 Basic configuration 
The basic configuration mainly involves server types, database versions, storage engines, instance types, number of multipart nodes, computing resource specifications, storage capacity, etc. See below for details:
#### (1) Configuration types
Two types of models are available: High IO and High IO (10 GB).
#### (2) Versions
The database version 3.2 is supported.
#### (3) Engines 
TencentDB for MongoDB supports two database engines: WiredTiger and Rocks.
#### (4) Instance types and number of nodes
Instances types include replica set instances and sharding instances. If replica set instances are used, the "1 Master, 2 Slaves" architecture is configured by default. When a sharding cluster is used, you can select the number of shards and the number of nodes in each shard as needed. The "1 Master, 2 Slaves" architecture is used in each shard by default. To improve data availability, you can increase the number of nodes in each shard. To expand the storage capacity of the cluster, you can increase the number of shards.
#### (5) Specifications
Computation specifications supported for each node are shown in the following table:

| CPU | MEM |
| ------- |-------|
| 1 core | 2 GB |
| 2 cores | 4 GB |
| 4 cores | 8 GB |
| 6 cores | 16 GB |
| 12 cores | 32 GB |
| 24 cores | 64 GB |
| 24 cores | 128 GB |
| 32 cores | 240 GB |

#### (6) Capacity
You can choose storage specifications according to computation specifications. The storage space of Oplog is 10% of the selected storage capacity by default, which can be adjusted on the Tencent Cloud console.
### 1.3 Networks and projects
#### (1) Network types
VPCs and basic networks are supported. If you select a basic network, only devices in the basic network can access the created database instances. If you select a VPC, only devices in the current subnet can access the created database instances.
#### (2) Projects 
You can select appropriate projects based on your business needs.
### 1.4 Quantity and usage period
#### (1) Quantity
You can purchase a maximum of 10 prepaid instances, and a maximum of 30 postpaid instances in all regions.
#### (2) Usage period 
In the prepaid billing mode, you can select a usage period of 3 years at most. You can also enjoy 12% off for a usage period of more than 6 months, 60% off for a usage period of 2 years and 70% off for a usage period of 3 years.
## 2. Initialize Instance
After an instance is purchased and delivered successfully, you can find it in the [Instance List](https://console.cloud.tencent.com/mongodb) on the console, as shown below.
![](https://main.qcloudimg.com/raw/349b681a43275ccc0c3d79f54dea421f.png)
Click **Initialize First** to set a password for mongouser and rwuser. The popup box is shown as follows:
![](https://main.qcloudimg.com/raw/042e6a5a5d4da7eb73e3df906644e84d.png)

