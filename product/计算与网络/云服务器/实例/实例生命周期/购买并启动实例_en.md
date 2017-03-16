Users can start a new instance as follows:

## Purchase and start the instance via image

1) Log in to the Tencent Cloud official website, select "Cloud Services" - "Compute and Network" - "Cloud Virtual Machine", then click "Buy Now" button, enter the [CVM purchase page](https://buy.qcloud.com/buy/cvm).

2) Select the billing mode: annual or monthly plan or charge by quantity (If you are not able to purchase CVMs on a charge-by-quantity basis, please go through a [Qualification](https://console.qcloud.com/developer/infomation) process first). With these two modes, the fee is charged on a monthly basis and by the seconds for which the server is used, respectively. For more information, see [here](http://www.qcloud.com/doc/product/213/%E8%AE%A1%E8%B4%B9%E6%A8%A1%E5%BC%8F%E8%AF%B4%E6%98%8E).
![](//mccdn.qcloud.com/static/img/2116de97fc48aa340e08d3ebb982bbde/image.png)

3) Select a region and availability zone. When you need more than one CVMs, it's recommended that you choose different availability zones so as to ensure disaster tolerance.

4) Select the model and configuration. Tencent Cloud provides three CVM models.
- Standard: With CPUs ranging from low to high core count, this is suitable for medium- and small-sized Web applications and databases.
- High IO: Both system and data disks are high-performance SSDs. This is suitable for I/O intensive applications with low latency.
- Memory: A CPU:memory ratio of 1:8, applicable to applications that need considerable memory operations, search, and compute.
For the comparison, see [here](/document/product/213/7153).

![](//mccdn.qcloud.com/static/img/0a506ce5c9c271ee09ea237ce1d34944/image.png)

5) Select the image

Those who have just started using Tencent Cloud products can select public images, which contain the vast majority of Linux systems and the legitimate Windows systems. You need to build subsequent operating environment on your own. Select an operating system and the version as needed.
![](//mccdn.qcloud.com/static/img/aaf71863f01a1b6c28c7e3eadeb3734a/image.png)

- Linux image system provided by Tencent Cloud is an open source system that supports a variety of popular programming languages and databases like MySQL (need to be installed by user). 
- Windows image system provided by Tencent Cloud contains legitimate activation key at no extra charge (except for certain overseas regions).  

6) Select the type of hard disk and the size of data disk.
Tencent Cloud provides Cloud Block Storage and local hard disk.
- Cloud Block Storage: delivers high data reliability with the distributed three-copy mechanism.
- Local hard disk: a storage located on the physical machine where the CVM resides; it allows low latency but may cause single-point loss risk. For the comparison, see [here](/doc/product/213/4952).

Whichever type of disk you choose, a complimentary 20GB system disk will be provided for each Linux CVM purchase by default, and you can adjust the capacity to 50GB through the billing mode; a complimentary 50GB system disk will be supplied with each Windows CVM purchase by default, and it cannot be adjusted at the moment. You can select the data disk size as needed when making the purchase.

7) Choose the type of network (basic network or VPC) and network billing mode (charge by fixed bandwidth or by traffic).
- Basic network: suitable for new users; CVM private networks of the same user are interconnected.
- Virtual Private Cloud: suitable for higher-level users; there is logic isolation between different VPCs.
> NOTE: Windows CVM cannot be used as the [Public Network Gateway](/doc/product/215/4972). Users who need public network gateway can select the Linux image to create CVM.

- Charge by fixed bandwidth: a fixed bandwidth is selected; exceeding this bandwidth will lead to packet loss. Suitable for scenarios with a low level of network fluctuation.
- Charge by traffic: the fee will be charged by the actually consumed traffic. You may set a peak bandwidth limit to avoid any cost arising from unexpected traffic. Packet loss will happen when the instantaneous bandwidth exceeds that peak value. Suitable![](//mccdn.qcloud.com/static/img/bca65a7bc1681058e3810810f18a23d4/image.png)

8) Determine the number of servers and the length of purchase (only for CVMs with an annual and monthly plan).

9) Set host name and login method
You may choose the host naming method of "Name It Now" at the time of purchase, and fill in a meaningful name limited to 60 characters, such as `my-first-cvm`, or choose to "Name It after Creation". In the latter case, naming is not needed, and the name of the started CVM will be `Unnamed`.

Tencent Cloud supports multiple CVM login methods, from which users are free to choose:

- For CVMs with Linux images, three login methods are available.
 - Setting a password: users can set a password to log in to the CVM by following the instructions in the page.
 - Associating with the keys immediately: logging in with SSH keys is safer than logging in with passwords. Users need to choose available SSH keys, or create new SSH keys. For more information about SSH keys, please refer to [SSH Key] (/doc/product/213/6092).
 - Automatically generated password: Tencent Cloud can generate a password automatically and send the initial password to you through internal message after the CVM is started.
- For CVMs with Windows images, two login methods are available.
 - Setting a password: users can set a password to log in to the CVM by following the instructions in the page.
 - Automatically generated password: Tencent Cloud can generate a password automatically and send the initial password to you through internal message after the CVM is started.

For more information about logging in to server, please refer to [Logging in to Windows Instance] (/doc/product/213/5435) and [Logging in to Linux Instance] (/doc/product/213/5436)

10) Choose a Security Group (<font color="red">Make sure the login ports 22 (Linux) or 3389 (Windows) are open</font>. See [Security Group] (/doc/product/213/5221) for more information), click "Buy Now" button and complete the payment, and then you may enter [Console](https://console.qcloud.com/cvm) to check and accept your CVM.

After the CVM is created, the user will get an internal message containing such information as instance name, Public IP address, Private IP address, login name, and initial login password (if you choose the method of automatically generated password). You may use the information to log in to and manage instances.

## Start an instance which is the same as the current CVM

Tencent Cloud allows users to start an instance which is the same as the current CVM (operating system, application and configuration, etc.) by making a CVM custom image. The instance will get a new Private IP address and a new optional Public IP address.

1) Open the Tencent Cloud console, choose "Cloud Virtual Machine" tab.

2) After clicking the CVM instance for which an image will be made in the CVM list, choose "Operation" - "More" - "Make Image" buttons.

3) After an image is successfully made, the operation log at the upper right corner will display the completion status. Redirect to the image list through the completed image ID. 

4) Click the "Create Cloud Virtual Machine" button after the image to redirect to the CVM purchase page. The operating system will select this image by default.

5) Make a purchase following the steps described in the "Purchase and Start an Instance via Image" above, and then you can create an instance that is the same as the current CVM.

## Automatically mount data disks when using custom image and data disk snapshot to start a new instance

For instances started based on the method above, the data disks can only be used by CVM instances after being mounted or made online. See the [Linux System Partitioning, Formatting, Mounting and File System Creation] (/document/product/362/6735) and [Windows System Partitioning, Formatting and File System Creation] (/doc/product/362/6134) for details. When starting new CVM instances, if a user specifies a ***custom image*** and***data disk snapshot***, the Cloud Block Storage of Tencent Cloud can support automatic mounting after a CVM instance is started (which means reading and writing for data disks can be achieved directly without the need to perform a series of operations including adding, partitioning and formatting). Users need to perform several operations on the original instances according to the following instructions before making custom images and data disk snapshots:

### How to set automatic mounting of data disks in Linux system
In a Linux system, if a user hopes that the Cloud Block Storage generated by a specified data disk snapshot can automatically mount new CVM instances, the specified custom image and data disk snapshot must meet the following requirements:
- The data disk ***should*** be formatted before a snapshot is made for it, namely it was successfully mounted to the original CVM.
- Before an image is made for the system disk, the following commands need to be added to the `/etc/rc.local` file so that data disk mount points are written in the file:

```
mkdir -p <mount-point>
mount <device-id> <mount-point>
```

Note: Input the mount point of the file system in `<mount-point>`, such as `/mydata`, and input the actual location of file on the partition in `<device-id>`, such as `/dev/vdb (The device name without partitions and with a file system)` and `/dev/vdb1 (The device name with both a file system and partitions)`.

Only if the two requirements above are both satisfied can the new Linux CVM instance data disk be automatically recognized and mounted.

### How to set automatic mounting of data disks in Windows system
In a Windows system, if a user hopes that the Cloud Block Storage generated by a specified data disk snapshot can automatically mount new CVM instances, the specified custom image and data disk snapshot must meet the following requirements:

- The SAN policy in the custom image is `onlineAll`. The Windows public images currently provided by Tencent Cloud have been configured accordingly by default, but users are recommended to check the configuration before making custom images as follows:
![](//mccdn.qcloud.com/static/img/74e490afd81bd7ad9fc9590565b48a80/image.jpg)

- Data disks should be formatted into `ntfs` or `fat32` before snapshots are made.

Only if the two requirements above are both satisfied can the new Windows CVM instance data disk be automatically recognized and made online.