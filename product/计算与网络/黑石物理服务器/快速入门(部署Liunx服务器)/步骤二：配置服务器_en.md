
This section describes how to configure the CPM, including selecting operating system, configuring RAID and defining operating system partition, as well as adding the capability for access from public network, etc.

## Selecting Operating System
After selecting the CPM configuration, click "Next Step: Select Operating System"
Select an operating system on the screen. We use CentOS 6.5
![](http://mc.qcloudimg.com/static/img/e00158153200502aa737fc9b70cceb52/image.png)

*CVM can eliminate compatibility issues using virtualization technology, so you do not have to consider hardware compatibility issues when installing an operating system on CVM.
However, since CPMs are provided as bare-metal physical machines, the operating systems available on the page need to be verified by CPM manufacturers and tested by Tencent Cloud, to ensure their availability in the data center.
If your desired operating system is not listed here, please contact Tencent Cloud customer service department and tell us your requirements.*

## Configuring RAID
After selecting the operating system, click "Next Step: Select Storage and Network"
In this step, you can select a RAID level you wish to use. From the page, you can see that two RAID levels are supported for PC100: RAID0 and RAID1. "NO RAID" mode is used to set RAID card to HBA operating mode, that is, no RAID storage group will be created.
Web application server is only used to store application log and no redundant storage is required, thus you can simply use RAID 0
![](http://mc.qcloudimg.com/static/img/d5e9db2ef6fc4d5a490e7f26b72eeb3d/image.png)
*For more information about RAID, please see [Configure RAID Level](/doc/product/386/7142 "Configure RAID Level") section*

## Configuring Operating System Partition
You can configure the size of the operating system partition before installing the operating system.
In this scenario, there is no particular demand, you may partition the disk following the instructions on the page.
![](http://mc.qcloudimg.com/static/img/d3778be090dac54af50964a103fbcb50/image.png)</br>
*You can specify partition size if necessary. For more information, please see [Customize Disk Partition](/doc/product/386/7141 "Customize Disk Partition") section*

## Network Isolation
VPC allows you to pre-configure an independent network space in the cloud. You can customize the cloud resources deployed in the virtual network. You can achieve complete network logic isolation by customizing IP address range, IP address, routing policy, etc.
Please select the VPC and subnet where your CPM resides in.

## Public Network Access Methods
CPM provides two methods for access from public network: elastic public IP and BM load balancer.</br>

<li>Elastic public IP (EIP)</li> 
It is a static IP address designed for dynamic cloud computing. Unlike traditional static IP, EIP can be bound to any CPM - CPM A or CPM B. In case of a failure of a CPM or availability zone, you can remap the IP to a healthy CPM so that you can deal with the CPM problem while offering service.
*For more information, please see [Elastic Public IP](/doc/product/386/7144)*

<li>BM load balancer</li> 
BM load balancer can automatically spread access traffic of applications among multiple CPMs. It improves the fault tolerance of applications, and continuously provides the load balance capacity needed for responding to the incoming traffic of applications. BM load balancer can detect any unhealthy CPM in the cluster and automatically shift the route to a healthy CPM until the unhealthy one recovers. You can enable the BM load balancer in a single availability zone or multiple availability zones to achieve a more consistent application performance.

Next, we will build a simple scenario regarding public network access, where public network access is provided by binding an EIP.

## Binding Elastic Public IP
On the purchase page, select "Assign EIP for Free" to acquire a CPM with an EIP already bound with it.
![](http://mc.qcloudimg.com/static/img/37b974f6f3bd6ff5367d660845ef3fbc/image.png)
*For more information about the features of EIP, please see [Elastic Public IP](/doc/product/386/7144) section*	

