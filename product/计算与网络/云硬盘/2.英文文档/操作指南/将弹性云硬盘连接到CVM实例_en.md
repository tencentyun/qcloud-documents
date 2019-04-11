After being created, a non-elastic cloud disk (a cloud disk whose lifecyle is same as that of CVM instance) is automatically connected to the created CVM instance and cannot be changed. You can also manually mount an elastic cloud disk to any instance within the same availability zone and check how many additional cloud disks can be mounted for each instance. For more information on the maximum number of cloud disks allowed to be mounted, refer to [Usage Restrictions](/doc/product/362/5145). For more information on elastic cloud disk and non-elastic cloud disk, refer to [Categories of Cloud Block Storage](https://cloud.tencent.com/document/product/362/2353).

## Connecting an elastic cloud disk to CVM instance in console
Currently, only elastic HDD cloud storages used as data disks can be mounted, and system disks are not allowed to be mounted.

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Go to "Cloud Virtual Machine" - "Cloud Block Storage" tab.

3) In the CBS list page, click "More" - "Mount to CVM" button next to the cloud disk with a status of **Pending mounted, Mounting/Unmounting Supported** for a single disk mounting.
You can also check the cloud disks with a status of **Pending mounted, Mounting/Unmounting Supported**, and click the "Mount" button on the top for a batch mounting.

4) In the pop-up box, select the CVM to which the cloud disk to be mounted, and click "OK". After the mounting, log in to the CVM to check the mounting status of the cloud disks.

After being mounted, a cloud disk must go through a series operations such as partitioning and formatting to be put into use. For instructions on how to perform such operations, please refer to [Partitioning, Formatting and File System Creation on Windows System](https://cloud.tencent.com/document/product/362/6734
) and [Partitioning, Formatting, Mouting and File System Creation on Linux System](https://cloud.tencent.com/document/product/362/6735).

## Connecting an elastic cloud disk to CVM instance with API
Please refer to [API AttachCbsStorages](https://cloud.tencent.com/doc/api/364/2520).

## How to solve the problem that some of the created CVM instances cannot recognize elastic cloud disks

All of the supplied images support mounting/unmounting of elastic cloud disks.Please make sure to perform unmount (for Linux) or offline (for Windows) actions before removing (uninstalling) the disk, otherwise it is likely that the disk cannot be recognized when mounted again.

If you have purchased the following CVMs and plan to add elastic cloud disks to the CVMs:

<table>
<tbody>
<tr><th>CVM Operating System Type</th><th>Version</th>
<tr><td rowspan="4">CentOS</td><td>5.11 64-bit</td>
<tr><td>5.11 32-bit</td>
<tr><td>5.8 64-bit</td>
<tr><td>5.8 32-bit</td>
<tr><td >Debian</td><td>6.0.3 32-bit</td>
<tr><td rowspan="2">Ubuntu</td><td>10.04 64-bit</td>
<tr><td>10.04 32-bit</td>
<tr><td rowspan="2">OpenSuse</td><td>12.3 64-bit</td>
<tr><td>12.3 32-bit</td>
</tbody>
</table>

You're recommended to execute the following command in the instance to add a driver to support hot-swapping before purchasing an elastic cloud disk:

```
modprobe acpiphp
```
　　
In addition, after shutting down or restarting the CVM, you still need to re-load `acpiphp` driver module. So you're recommended to set the `acpiphp` module to be automatically loaded upon the startup of CVM. The procedures for setting this for various operating systems are as follows:

**CentOS 5 Series**

Execute the following command to create the file:

```
vi /etc/sysconfig/modules/acpiphp.modules
```

And write the following content to the file:

```
 #!/bin/bash
 modprobe acpiphp >& /dev/null
```

Execute the following command to add executable permissions. After the setting, the script can be loaded upon the startup of CVM:

```
chmod a+x /etc/sysconfig/modules/acpiphp.modules
```

**Debian 6 Series, Ubuntu 10.04 Series**

Execute the following command to modify the file:

```
vi /etc/modules
```
And write the following content to the file:

```
acpiphp
```
 	  
**OpenSUSE 12.3 Series**

Execute the following command to modify the file:

```
vi /etc/sysconfig/kernel
```
And write the following content to the file:

```
MODULES_LOADED_ON_BOOT="acpiphp"
```　
	   
