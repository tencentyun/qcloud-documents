A non-elastic cloud disk (a cloud disk whose lifecycle follows the CVM instance) is automatically connected to the created CVM instance when it is created, and cannot be changed. Meanwhile, you can manually mount the elastic cloud disk to any instance in the same availability zone. You can determine how many more cloud disks can be mounted on each instance during mounting. For more information on cloud disk quantity limits, please see [Usage Constraints](/doc/product/362/5145). For more information on elastic and non-elastic cloud disks, please see [Classification of Cloud Disks](https://cloud.tencent.com/document/product/362/2353).

## Connecting Elastic Cloud Disk to Instance via Console
The ordinary HDD cloud disk can be mounted as a <font color="red">data disk</font>, but cannot be mounted as a system disk.

1) Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Enter **CVM** -> **Cloud Disk** tab.

3) On the cloud disk list page, click **More** -> **Mount to CVM** button next to the cloud disk in the status of <font color="red">To be Mounted and Support Mounting/Unmounting</font> to mount a single cloud disk.
Or on the cloud disk list page, select the cloud disks in the status of <font color="red">To be Mounted and Support Mounting/Unmounting</font>, and click the **Mount** button on the top to mount cloud disks in batch.

4) In the pop-up box, select the CVM on which to mount the cloud disk, and click **OK**. After the mounting is completed, you can log in to the CVM to view the cloud disk mounting status.

The mounted cloud disk cannot be used immediately. It requires a series of operations such as partitioning and formatting. For more information on how to perform the operations, please see [Partitioning, Formatting, and File System Creation on Windows System](https://intl.cloud.tencent.com/document/product/362/6734
) and [Partitioning, Formatting, Mounting and File System Creation on Linux System](/document/product/362/6735).

## Connecting Elastic Cloud Disk to Instance via API
For more information, please see [AttachCbsStorages API](https://cloud.tencent.com/doc/api/364/2520).

## Solution to Problem of Some Created CVM Instances Unable to Identify Elastic Cloud Disk

All images available support the connection/unmounting of elastic cloud disks.<font color="red"> Note: Perform "unmount" (Linux) or "offline" (Windows) operation before taking out (unmounting) the cloud disk, otherwise it may not be identified when remounting.</font>

However, if you have purchased the following types of CVMs and plan to add elastic cloud disk to the CVM:

<table>
<tbody>
<tr><th> CVM OS </th><th> Version </th>
<tr><td rowspan="4"> CentOS </td><td> 5.11 64-bit </td>
<tr><td> 5.11 32-bit </td>
<tr><td> 5.8 64-bit </td>
<tr><td> 5.8 32-bit </td>
<tr><td > Debian </td><td> 6.0.3 32-bit </td>
<tr><td rowspan="2"> Ubuntu </td><td> 10.04 64-bit </td>
<tr><td> 10.04 32-bit </td>
<tr><td rowspan="2"> OpenSuse </td><td> 12.3 64-bit </td>
<tr><td> 12.3 32-bit </td>
</tbody>
</table>

It is recommended that you add the driver to get the hot-plugging feature by running the following command in the instance before you purchase the elastic cloud disk:

```
modprobe acpiphp
```
  
In addition, after you shut down or reboot the CVM, you need to load the `acpiphp` driver module again. It is recommended that you set the `acpiphp` module to "load automatically when CVM starts up". The setting methods for various series are as follows:

**CentOS 5 series**

Run the following command to create a file:

```
vi /etc/sysconfig/modules/acpiphp.modules
```

And add the following content in the file:

```
 #!/bin/bash
 modprobe acpiphp >& /dev/null
```

Run the following command to add executable permissions. After the settings are completed, the script can be loaded when the CVM starts up:

```
chmod a+x /etc/sysconfig/modules/acpiphp.modules
```

**Debian 6 series and Ubuntu 10.04 series**

Run the following command to modify the file:

```
vi /etc/modules
```
Write the following:

```
acpiphp
```
 	  
**OpenSUSE 12.3 series**

Run the following command to modify the file:

```
vi /etc/sysconfig/kernel
```
Write the following:

```
MODULES_LOADED_ON_BOOT="acpiphp"
``` 
	   
