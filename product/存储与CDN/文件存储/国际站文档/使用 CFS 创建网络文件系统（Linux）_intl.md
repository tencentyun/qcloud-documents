

## 1. Creating and Configuring a CVM Instance
To access the file system, you need to mount the file system to Linux- or Windows-based Tencent Cloud CVM instances. In this step, you will create and configure a Linux-based Tencent Cloud CVM instance. If you want to use a Windows-based CVM, please see [Creating a Network File System (Windows) with CFS](/doc/product/582/11524). If a CVM instance has been created, go to Step 2 [Create a File System and Mount Point](#1).

Go to the Tencent Cloud official website, select **Cloud Products** -> **Compute and Network** -> **CVM**, then click **Buy Now** to enter the [CVM purchase page](https://buy.cloud.tencent.com/buy/cvm).
### (1) Select a region and model
![](https://main.qcloudimg.com/raw/3f41daecd7fb1e73cdf69345cda87f3b.png)
- Select a billing mode: Prepaid or postpaid (users who cannot purchase postpaid CVMs need to complete [Identity Verification](https://console.cloud.tencent.com/developer/auth) first). For more information, please see [Billing Mode](/doc/product/213/2180).
- Select a region and an availability zone: When you need more than one CVM, it is recommended that you choose different availability zones to implement disaster recovery.
- Select a model and configuration: For more information, please see [Instance Types](/doc/product/213/7153).


### (2) Select an image
![](https://main.qcloudimg.com/raw/ffe82a64aa448ff02a3e1d3d225c4e7a.png)
- Select an image provider. Tencent Cloud supports public images, custom images, shared images and service marketplace images. You can view [Image Types](/doc/product/213/4941) to select an image. The public image type is recommended for users who have just started using Tencent Cloud.
- Select an operating system. Tencent Cloud provides various operating systems such as CentOS, CoreOS, Debian, FreeBSD, OpenSUSE, SUSE and Ubuntu. You need to build subsequent operating environment on your own.
- Select a system version. 

### (3) Select storage and network
![](https://main.qcloudimg.com/raw/1d0f67e38dfecae3d1b46254c377b441.png)
- Select the type of disk and the size of data disk.
Tencent Cloud provides two types of disks, cloud disk and local disk (system disk size is optional. The default is 50 GB).
  - Cloud disk: Deliver high data reliability with the distributed three-copy mechanism.
  - Local disk: A storage device on the physical machine where the CVM resides in, which allows low latency but may cause single point of failure risk. For the comparison, please see [Product Category](/doc/product/362/2353).
- Select a network type.
Tencent Cloud provides two network types: basic network and VPC.
 - Basic network: Suitable for new users. CVMs of the same user are interconnected via the private network.
 - VPC: Suitable for advanced users. Different VPCs are logically isolated from each other.
- Select the public network bandwidth.
Tencent Cloud provides two options: Bill-by-bandwidth or bill-by-traffic.
 - Bill-by-bandwidth: Select a fixed bandwidth. Packet loss occurs if this bandwidth is exceeded. This is suitable for scenarios with minor network fluctuation.
 - Bill-by-traffic: The service is charged based on the actual traffic usage. You can set a limit for peak bandwidth to avoid extra fees caused by unplanned traffic. Packet loss occurs when the instantaneous bandwidth exceeds this limit. This is suitable for scenarios with large network fluctuations.
- Select the quantity.
- Select the usage period and renewal method (only for prepaid CVMs).

### (4) Configure information
![](https://main.qcloudimg.com/raw/4ff1d71ec345f84e1029f8b77cbaaf89.png)
- Set CVM name: You can name it after creation or name it now.
- Set login information:
 - Set Password: Enter a CVM password.
 - Associate Key Now: Associate SSH key. If you do not have a key or have an invalid key, click **Create Now** to create one. For more information, please see [Create Key](/doc/product/213/516#1). For more information on SSH key, please see [SSH Key](/doc/product/213/503).
 - Automatically Generate Password: The automatically generated password is sent to you via the internal message.
- Select a security group (**Make sure that the login port 22 is enabled.** For more information, please see [Security Group](/doc/product/213/5221)).

Click **Buy Now** button to complete the payment, and then you may enter the [Console](https://console.cloud.tencent.com/cvm/) to check your CVM.
After the CVM is created, you will receive an internal message containing such information as instance name, public IP address, private IP address, login name, and initial login password. You can use the information to log in to and manage instances.
 

<span id="1"></span>
## 2. Creating File System and Mount Point

1. Log in to the Tencent Cloud [Console](https://console.cloud.tencent.com/). Click **Cloud Products** -> **Storage** -> **CFS** to go to the CFS console.
![](https://main.qcloudimg.com/raw/b7ac1f186ac0491ac369d62952447d26.png)

2. In the Tencent Cloud CFS console, click **Create** and the Create File System popup window appears. Enter relevant information and confirm, and then click **OK** to create the file system.
![](https://main.qcloudimg.com/raw/b2c089eb76dec621eda63ef3e138efe0.png)
 - Name: Name the file system to be created.
 - Region and availability zone: Choose a region closest to your customers to minimize access latency and improve download speed.
 - File protocol: NFS (suitable for Linux and Unix clients), CIFS/SMB (suitable for Windows clients).
 - Network type: Tencent Cloud provides two network types: basic network and VPC. Basic network is suitable for new users. CVMs of the same user are interconnected via the private network. VPC is suitable for advanced users. Different VPCs are logically isolated from each other.
  	
 > **Note:**
 > Create and mount a file system based on the network where your CVM instance resides.
 > - To allow a file system to be shared by CVMs under a VPC, you need to select VPC when creating a file system. When the file system belongs to VPC, only CVM instances in the same VPC can be mounted if no specific network settings are made.
 > - To allow a file system to be shared by CVMs under a basic network, you need to select basic network when creating a file system. When the file system belongs to basic network, only CVM instances in the same basic network can be mounted if no specific network settings are made.
 > - For more information on how to share a file system among multiple networks, please see [Cross-availability zone and Cross-network Access to File System](/doc/product/582/9764).

3. Obtain the mount point information. After the file system and the mount point are created, click the instance ID to enter the file system details page, and then click **Mount Point Information** to obtain the mount command for Linux.

The mount point information of NFS file system is as follows:
![](https://main.qcloudimg.com/raw/e52d235c97f0a6f16a9cbd86eabe5aa6.png)

The mount point information of CIFS/SMB file system is as follows: 
![](https://main.qcloudimg.com/raw/3a13257ec58a8de79929d8af39b4ed5a.png)



## 3. Connecting Instances
This section describes how to log in to a Linux CVM. Login method depends on the scenarios. This step shows how to log in to the CVM in the console. For more information on other login methods, please see [Log in to Linux Instance](/doc/product/213/5436).

**Prerequisites**
You need to use the admin account ID and the corresponding password to log in to the CVM.
 - Admin account ID: It is "root" for Linux instances ("ubuntu" for Ubuntu system users).
 - Password: The password is the one you specified when purchasing the CVM instance.

**Log in to CVM via the console**
- In the Action column of CVM list, click **Log In** button to connect to Linux CVM via VNC.
![](https://main.qcloudimg.com/raw/ff0adff1a8e94577ebe45bcb0650b5f8.png)
- Enter the account ID "root" ("ubuntu" for Ubuntu system users) and its password to log in.

>**Note:**
>This terminal is exclusive, that is, only one user can log in using the console at a time.


**Verify network communications**
Before mounting, you need to confirm the network connectivity between the client and the file system. You can use the telnet command to verify it. The specific protocols and open ports for clients are as follows:

File System Protocol | Open Port for Client | Check Network Connectivity
------- | ------- | ---------
NFS 3.0 | 111, 892, 2049 | telnet 111 or 892 or 2049
NFS 4.0 | 2049 | telnet 2049
CIFS/SMB | 445 | telnet 445 

Note: CFS does not support ping.

## 4. Mounting a File System
### Mount a NFS file system

#### (1) Launch the NFS client
Before mounting, make sure that `nfs-utils` or `nfs-common` has already been installed in the system. The installation method is as follows:
- CentOS:
```
sudo yum install nfs-utils
```
- Ubuntu or Debian:
```
sudo apt-get install nfs-common
```

#### (2) Create a target mount directory
Create a target mount directory with the following command.
```
mkdir <target mount directory>
```
Example:
```
mkdir /local/
mkdir /local/test
```

#### (3) Mount a file system
**Mount NFS v4.0**
Mount NFS v4.0 with the following command.
```
sudo mount -t nfs -o vers=4 <mount point IP>:/ <target mount directory>
```
- Mount point IP: It is automatically generated when the file system is created.
- By default, NFS v4.0 is mounted under the root directory ("/") of the file system. After a subdirectory is created in the file system, this subdirectory can be mounted.
- Target mount directory: You must first create the target mount directory before mounting it on the current CVM.

> **Note:**
> There is a space between `<mount point IP>:/` and `<target mount directory>`.


Example:
- Mount to the root directory of CFS:
```
sudo mount -t nfs -o vers=4 10.0.0.1:/ /local/test
```
- Mount to the subdirectory/subfolder of CFS:
```
sudo mount -t nfs -o vers=4 10.10.19.12:/subfolder /local/test
```

 ![](https://main.qcloudimg.com/raw/e52d235c97f0a6f16a9cbd86eabe5aa6.png)

**Mount NFS v3.0**
Mount NFS v3.0 with the following command.
```
sudo mount -t nfs -o vers=3,nolock,proto=tcp <mount point IP>:/ <target mount directory>
```
- Mount point IP: It is automatically generated when the file system is created.
- NFS v3.0 can only be mounted to a subdirectory. The default file system subdirectory is FSID or "nfs".
- Target mount directory: You must first create the target mount directory before mounting it on the current CVM.
Example

> **Note:**
> There is a space between `<mount point IP>:/` and `<target mount directory>`.


Example:
- Mount to the subdirectory/subfolder of CFS:
```
mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/z3r6k95r /local/test
```
- Mount to the subdirectory/subfolder of CFS:
```
mount -t nfs -o vers=3,nolock,proto=tcp 10.10.19.12:/nfs /local/test
```
![](https://main.qcloudimg.com/raw/e52d235c97f0a6f16a9cbd86eabe5aa6.png)

#### (4) View the mount point information
After the mounting, the mounted file system can be viewed with the following command:
```
mount -l
```
The capacity information of this file system can be viewed with the following command:
```
df -h
```
### Mount CIFS/SMB file system
#### (1) Launch a CIFS client
Before mounting, make sure that `cifs-utils` has already been installed in the system. The installation method is as follows:
CentOS:
```
sudo yum install cifs-utils.x86_64 -y
```


#### (2) Create a target mount directory
Create a target mount directory with the following command.
```
mkdir <target mount directory>
```
Example:
```
mkdir /local/
mkdir /local/test
```

#### (3) Mount a file system
Mount CIFS with the following command.
```
mount -t cifs -o guest //<mount point IP>/<FSID> /<target mount directory>
```
- Mount point IP: It is automatically generated when the file system is created.
- By default, FSID of the file system is used for the mounting. 
- Target mount directory: You must first create the target mount directory before mounting it on the current CVM.

> **Note:**
> There is a space between `<FSID>/` and `<target mount directory>`.

Example:

```
mount -t cifs -o guest //10.66.168.75/vj3i1135  /local/test
```

 ![](https://main.qcloudimg.com/raw/3a13257ec58a8de79929d8af39b4ed5a.png)

#### (4) View the mount point information
After the mounting, the mounted file system can be viewed with the following command:
```
mount -l
```
The capacity information of this file system can be viewed with the following command:
```
df -h
```

### (5) Unmount a shared directory
When you need to unmount a shared directory in some cases, use the following command. The "directory name" refers to the full path of the root directory or file system.
```
umount <directory name>
```

Example: 
```
umount /local/test
```


## 5. Terminating Resources
You can terminate a CVM instance or a file system in the Tencent Cloud console. It is recommended that you terminate any resource that is no longer used, to avoid further fee deduction.
1. Terminate a Tencent Cloud instance. Go to the Tencent Cloud CVM [console](https://console.cloud.tencent.com/cvm/index), and select the instance to be terminated. Click **More** -> **CVM Status**, and then select **Terminate** to terminate the  CVM instance.
![](https://main.qcloudimg.com/raw/aebd52db8eb742cbc5b6a3cffe61b82f.png)
2. Terminate a file system. Go to the Tencent Cloud CFS [console](https://console.cloud.tencent.com/cfs), select the file system to be terminated. Click **Delete** and **OK** to delete the file system.
![](https://main.qcloudimg.com/raw/996e1c0ab24a7417d2357831f06cf705.png)



