## 1. Overview of Database Dedicated Cluster
Database Dedicated Cluster (Dedicated Cluster for short) allows you to purchase and create databases by **exclusively using physical cluster (complete device)** resources to meet your needs for exclusive use of resources, physical security, industrial regulation, etc. After purchasing the dedicated cluster, you can flexibly create various cloud databases with custom specifications.
- Supported databases: MySQL, TDSQL.
- Supported environments: Deployment of Database Dedicated Cluster is supported in public cloud, finance cloud and finance cloud cage in Beijing, Shanghai, Shenzhen, and Guangzhou.
- Supported models: HIOY5 model (48-core CPU, memory 512 GB, SSD disk 7,200 GB, 10-Gb dual ENI). **Note: The database instance specification used in practice only accounts for 70-90% of actual configuration of the model.**

## 2. Architecture of Database Dedicated Cluster
The schemes of dedicated cluster and multi-tenant public cloud are shown in the following figures:
![](https://mc.qcloudimg.com/static/img/7e89269ea6998d9da3947050212528ea/image.png)
In addition to all of the capabilities of cloud database, dedicated cluster has the following advantages in terms of deployment architecture:
- Database server: The physical host where the database resides in is the main part of your use of database and is exclusively occupied by you.
-	Tencent Cloud integrated operation management system: Deployed in the higher level of management network in Tencent Cloud, it serves as the basis on which you can provide flexible O&M capabilities, and is shared by you and other users.
- 	Backup and log storage: The backup center is based on HDFS technical architecture. You can apply for the exclusive use of it (for financial customers only).
-	Tencent Cloud gateway/Security gateway: Deployed at the frontend of database, the virtual network device features intelligent cloud load balancer and security management to provide your database with VIP (unique virtual IP), VPC, master/slave switchover, security protection and other capabilities. It is shared by you and other users.

>**Note:**
>Dedicated cluster solutions in finance cloud cage is different from that in public cloud in terms of isolation. For more information, consult the architect.

## 3. Procedure for Using Database Dedicated Cluster
1. [Purchase a dedicated cluster](https://buy.cloud.tencent.com/excluster) at a cluster device dimension. During the purchase, make sure to:
	- Select the region and availability zone where your server resides in for a better user experience.
	- Select database kernel. For more information, please see [Compatibility Between TDSQL and MySQL](https://cloud.tencent.com/document/product/237/6988).
	- Select model and master/slave architecture. "One Master, Multi-Slave" architecture is currently supported. The availability varies with different number of slaves. Theoretically, the availability of "One Master, One Slave" and "One Master, Two Slaves" is 99.95% and 99.99% or more, respectively.
	- Select the number of groups to purchase. Multiple groups of devices can form a cluster, and more redundancy resource pools can be provided for the cluster to ensure the availability.
2. View and manage details of dedicated clusters on the [List of Clusters](https://cdt.cloud.tencent.com/excluster/page/lists) page. Click "Action" -> "Allocate Instances" to allocate database instances on the dedicated cluster.
![](https://mc.qcloudimg.com/static/img/1a0829726ad5e7662e394c11c1604519/image.png)
3. Go to the "MySQL/TDSQL Instance List" page to check the database instances you just allocated. [Initialize Instances](https://cloud.tencent.com/document/product/236/3128) before you can use them.
As shown in the figure below, all the instances marked "Master instance (dedicated)" are allocated on dedicated cluster:
![](https://mc.qcloudimg.com/static/img/33ff4d302883b8d5f450f7ec9ddda2e2/image.png)

## 4. FAQs

Dedicated cluster means that an independent physical resource pool is dedicated to your use. Here are some suggestions on the use of dedicated cluster:
1. **Why do you need to reserve some redundancy for each instance and the dedicated cluster?**
The availability of database has a direct effect on that of the entire business system. You're recommended to reserve redundancy for each instance and unallocated resources or devices for the dedicated cluster to provide for unexpected changes.
2. **In most cases, you can specify the devices to which instances are allocated, but why can't you do so in some cases?**
Tencent Cloud provides you with the capability to allocate instances to a specified group of devices. If you can predict with certainty the load on each instance, then allocate the load on instances evenly to different device groups (unless there are restrictions on the system). However, in application scenarios such as distributed database, you cannot predict the load on each node. So the system specifies devices for some instances by default.
3. **How to apply for the exclusive use of cold backup data and log?**
The exclusive use of cold backup data and log is not supported for the public cloud now. For the finance cloud cage solution, contact your architect.
4. **Why can't you use 100% of the resources if device configuration ≠ maximum instance configuration?**
Operating system, disk raid and necessary space occupied by system logs take up device resources. Tencent Cloud has set a maximum instance specification (this value is subject to adjustment) for a single instance based on years of experience.
5. **Whether a VPC is supported for dedicated cluster?**
No, but you can allocate the instances that are allocated on the dedicated cluster to different VPCs.

