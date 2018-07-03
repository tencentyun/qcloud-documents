
## 1. Creating and Configuring a CVM Instance
To access the file system, you need to mount the file system to Linux- or Windows-based Tencent Cloud CVM instances. In this step, you will create and configure a Windows-based Tencent Cloud CVM instance. If you want to use a Linux-based CVM, please see [Creating a Network File System (Linux) with CFS](/doc/product/582/11523). If a CVM instance has been created, go to Step 2 [Create a File System and Mount Point](#1).

Go to the Tencent Cloud official website, select **Cloud Products** -> **Compute and Network** -> **CVM**, then click **Buy Now** to enter the [CVM purchase page](https://buy.cloud.tencent.com/buy/cvm).

### (1) Select a region and model
![](https://main.qcloudimg.com/raw/3f41daecd7fb1e73cdf69345cda87f3b.png)
- Select a billing mode: Prepaid or postpaid (users who cannot purchase postpaid CVMs need to complete [Identity Verification](https://console.cloud.tencent.com/developer/auth) first). For more information, please see [Billing Mode](/doc/product/213/2180).
- Select a region and an availability zone: When you need more than one CVM, it is recommended that you choose different availability zones to implement disaster recovery.
- Select a model and configuration: For more information, please see [Instance Types](/doc/product/213/7153).

### (2) Select an image
![](https://main.qcloudimg.com/raw/ffe82a64aa448ff02a3e1d3d225c4e7a.png)
- Select an image provider.
Tencent Cloud supports public images, custom images, shared images and service marketplace images. You can view [Image Types](/doc/product/213/4941) to select an image. The public image type, which contain legitimate Windows operating system, is recommended for users who have just started using Tencent Cloud. You need to build subsequent operating environment on your own.
- Select an operating system: Windows Server.
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
- Set login information: You can set a password or use an automatically generated password. The password you set can be modified after creation of CVM. The automatically generated password is sent to you via the internal message.
- Select a security group (**Make sure that the login port 3389 is enabled.** For more information, please see [Security Group](/doc/product/213/5221)).

Click **Buy Now** button to complete the payment before you can log in to the [console](https://console.cloud.tencent.com/cvm) to check your CVM.
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

3. Obtain the mount point information. After the file system and the mount point are created, click the instance ID to enter the file system details page, and then click **Mount Point Information** to obtain the mount command for Windows.

The mount point information of NFS file system is as follows:
![](https://main.qcloudimg.com/raw/e52d235c97f0a6f16a9cbd86eabe5aa6.png)

The mount point information of CIFS/SMB file system is as follows: 
![](https://main.qcloudimg.com/raw/3a13257ec58a8de79929d8af39b4ed5a.png)



## 3. Connecting Instances
This section describes how to log in to a Windows CVM. Login method depends on the scenarios. This step shows how to log in to the CVM in the console. For more information on other login methods, please see [Log in to Windows Instance](/doc/product/213/5435).

**Prerequisites**
You need to use the admin account ID and the corresponding password to log in to the CVM.
- Admin account ID: It is Administrator for all Windows instances.
- Password: The password is the one you specified when purchasing the CVM instance.
   
**Log in to CVM via the console**
(1) In the Action column of CVM list, click **Log In** button to connect to Windows CVM via VNC.
![](https://main.qcloudimg.com/raw/ff0adff1a8e94577ebe45bcb0650b5f8.png)
(2) By sending the **Ctrl-Alt-Delete** command at the top left corner, enter the system login screen.
![](//mc.qcloudimg.com/static/img/e4dbc02ca9ae2a7cb9ada5316effd31a/image.png)
(3) Enter the account (Administrator) and password to log in.

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
### Mount CIFS/SMB file system
#### Mount file system via graphical interface
a. Open **Map Network Drive**
Log in to the Windows, on which you want to mount the file system. Right click **Computer** in the **Start** menu, and then click **Map Network Drive**. 
![](https://main.qcloudimg.com/raw/24cd4dcf15bedb4eba176bc4b53ae2cf.png)

b. Enter the access path
In the pop-up configuration window, set the drive letter and folder (namely, the mounting directory displayed in the CIFS/SMB file system) for the **drive**.
![](https://main.qcloudimg.com/raw/3a13257ec58a8de79929d8af39b4ed5a.png)
![](https://main.qcloudimg.com/raw/156fbc26e0ba7d7f25b6422bf6eb652a.png)


c. Verify the correctness of read and write
After confirmation, the page is directed to the mounted file system. You can right click to create a file to verify the correctness of read and write.
![](https://main.qcloudimg.com/raw/9c328df637f8df81200fb84c87de3e64.png)

#### Mount file system via command line
Use FSID to mount the file system. The mount command is as follows.
```
net use <shared directory name>: \\10.10.11.12\FSID 
```
Example:
```
net use X: \\10.10.11.12\fjie120
```

> **Note:**
> FSID can be found under **Console** -> **File System Details** -> **Mount Point Information**.
![](https://main.qcloudimg.com/raw/3a13257ec58a8de79929d8af39b4ed5a.png)


### Mount a NFS file system
#### (1) Enable the NFS service
Before mounting the NFS file system, make sure that the system has enabled the NFS service. Here we use Windows Server 2012 R2 to enable the NFS service.
a. Open **Control Panel** -> **Programs** -> **Turn Windows Features On or Off** -> **Server Roles**, and select **Server for NFS**.
![](https://mc.qcloudimg.com/static/img/eaeed922e9d1f673e47137d80a88fa70/image.png)
b. Open **Control Panel** -> **Programs** -> **Turn Windows Features On or Off** -> **Features**, and select **Client for NFS** to enable the Windows NFS client service.
![](https://mc.qcloudimg.com/static/img/4f9d7ac7b877ceffc5bc2b1d7c050a24/image.png)

#### (2) Verify whether the NFS service is enabled
Open the command line tool under Windows, and execute the following command in the panel. If the relevant NFS information is returned, the NFS client is running normally.
```
mount -h
```
![](https://mc.qcloudimg.com/static/img/4e4f9db217874ccec91ac1f888c8e451/image.png)

#### (3) Add anonymous users and user groups
a. Open the registry
Enter the regedit command in the command line window and press Enter to open the registry window.
![](https://mc.qcloudimg.com/static/img/c9fca9a1b123a5b2dbc69b0ce66d539f/image.png)

b. Add configuration items AnonymousUid and AnonymousGid.
Select the following path in the registry. 
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default
```
Right click on the right blank space and the click **Create**. Select **DWORD(32-bit) Value** or **QWORD(64-bit) Value** (depending on the bit count of your OS) in the menu. Then, a new record will appear in the list. Modify the name field to AnonymousUid, and use the default value 0 for the data value. Add another record in the same way, with the name of AnonymousGid and the data value of 0 by default.
![](https://mc.qcloudimg.com/static/img/381cdc3b68fb35be5dcceb2a4c962e33/image.png)
![](https://mc.qcloudimg.com/static/img/80bb0cfbffbed939522459a830df3eac/image.png)

c. Restart the system to make the configuration take effect.
Close the registry and restart the Windows system to complete the registry modification.

##### (4) Mount the file system
###### Mount via graphical interface
a. Open **Map Network Drive**
Log in to the Windows, on which you want to mount the file system. Right click **Computer** in the **Start** menu, and then click **Map Network Drive**. 
![](https://main.qcloudimg.com/raw/24cd4dcf15bedb4eba176bc4b53ae2cf.png)

b. Enter the access path
In the pop-up configuration window, set the drive letter and folder (namely, the mounting directory displayed in the NFS file system) for the **drive**.
![](https://main.qcloudimg.com/raw/18cdceb91b0ec88f3286ea56fbed71c5.png)
![](https://main.qcloudimg.com/raw/1ab67b4e381b996389ea7bb900740ec4.png)


c. Verify the correctness of read and write
After confirmation, the page is directed to the mounted file system. You can right click to create a file to verify the correctness of read and write.
![](https://main.qcloudimg.com/raw/9c328df637f8df81200fb84c87de3e64.png)

###### Mount via CMD command line
Enter the following command in the Windows command line tool to mount the file system. The default subdirectory is "nfs".
```
mount  <mount point IP>:/<subdirectory> <shared directory name>:
```
Example:
```
mount 10.10.0.12:/nfs X:
```

If the folder cannot be renamed after the file system is mounted using the above command, use the FSID to mount it. The mount command is as follows.
```
mount <mount point IP>:/FSID <shared directory name>:
```
Example:
```
mount 10.10.0.12:/z3r6k95r X:
```

> **Note:**
> FSID can be found under **Console** -> **File System Details** -> **Mount Point Information**.

![](https://main.qcloudimg.com/raw/e52d235c97f0a6f16a9cbd86eabe5aa6.png)


### (5) Unmount the file system
#### Unmount a shared directory via graphical interface
To disconnect a mounted file system, right click on the disk and click **Disconnect** from the menu.
![](https://main.qcloudimg.com/raw/dd216d8014823bead7302b90df78b7cc.png)

#### Unmount the NFS shared directory via the CMD command 

When you need to uninstall a shared directory in some cases, use the following command. The "directory name" refers to the full path of the root directory or file system.
```
umount <directory name>:
```
Example:
```
umount X：
```



## 5. Terminating Resources
You can terminate a CVM instance or a file system in the Tencent Cloud console. It is recommended that you terminate any resource that is no longer used, to avoid further fee deduction.
1. Terminate a Tencent Cloud instance. Go to the Tencent Cloud CVM [console](https://console.cloud.tencent.com/cvm/index), and select the instance to be terminated. Click **More** -> **CVM Status**, and then select **Terminate** to terminate the  CVM instance.
![](https://main.qcloudimg.com/raw/aebd52db8eb742cbc5b6a3cffe61b82f.png)
2. Terminate a file system. Go to the Tencent Cloud CFS [console](https://console.cloud.tencent.com/cfs), select the file system to be terminated. Click **Delete** and **OK** to delete the file system.
![](https://main.qcloudimg.com/raw/996e1c0ab24a7417d2357831f06cf705.png)



