The CVM instance described below also refers to dedicated CVM.

In addition to [Create Custom Images](/doc/product/213/4942) feature, Tencent Cloud also supports importing images, that is, import local images or server system disk images on other platforms to CVM custom images. The imported images could be used in creation or re-installization of CVMs.

## Supported Linux Images
The local Linux images to be imported must meet following requirements:


| Image Property   | Requirement                                       |
| ------ | ---------------------------------------- |
| Operating system   | Images based on CentOS, Ubuntu, Debian, CoreOS, OpenSUSE or SUSE release versions. <br>Both 32-bit and 64-bit images are supported |
| Image file format   | raw. vhd, qcow2 or vmdk                       |
| File system type | ext3 or ext4 file system with MBR partition (GPT partition is not supported)        |
| System disk size  | Smaller than 50 GB. You can only import the images of system disks rather than that of data disks               |
| Network     | Multiple network APIs are not supported. Only eth0 is supported.<br>IPv6 address is not supported<br>. When users create CVMs with imported images, Tencent Cloud will create a network configuration file and store it in `/etc/qcloud-network-config.ini`, which includes IP, subnet mask, gateway and DNS, etc. Users can log in to CVMs created with the images to configure the network.  |
| Driver     | The virtio driver for virtualization platform KVM must be installed                    |
| Kernel   | It's recommended to use a native Linux kernel, otherwise the virtual machines may fail to import.<br><font color="red">All imported Red Hat Enterprise Linux (RHEL) images must have BYOL licenses. Users should purchase licenses and services from Red Hat before importing. </font> |


## Supported Windows Images
The local Windows images to be imported must meet following requirements:


| Image Property   | Requirement                                       |
| ------ | ---------------------------------------- |
| Operating system   | Microsoft Windows Server 2008 R2 (Standard, Datacenter or Enterprise)<br>Microsoft Windows Server 2012 R2 (Standard);<br><font color="red">Only 64-bit version is supported</font> |
| Image file format   | raw. vhd, qcow2 or vmdk                       |
| File system type | NTFS file system with MBR partition (GPT partition is not supported)             |
| System disk size  | Smaller than 50 GB. You can only import the images of system disks rather than that of data disks                 |
| Network     | Multiple network APIs are not supported. Only eth0 is supported.<br>IPv6 address is not supported<br>. When users create CVMs with imported images, Tencent Cloud will create a network configuration file and store it in `C:\qcloud-network-config.ini`, which includes IP, subnet mask, gateway and DNS, etc. Users can log in to CVMs created with the images to configure the network.  |
| Driver     | The virtio driver for virtualization platform KVM must be installed. By default, Windows is not installed with virtio driver. You can use the [software package provided by Tencent Cloud](http://windowsvirtio-10016717.file.myqcloud.com/InstallQCloud.exe) to install the driver before exporting machines on external platform to local images.  |
| Misc     | We do <font color="red">NOT</font> provide [Windows activation](https://cloud.tencent.com/doc/product/213/%E6%AD%A3%E7%89%88%E6%BF%80%E6%B4%BB) service for imported Windows images |

## Importing Images in the Console
> Check whether your Tencent Cloud account has applied for the import permission. If not, please submit related information via ticket system for an application.

1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) Click "Image" in the navigation pane.

3) Click "Custom Image", and select the custom images of the CVM instances you want to share.

4) Click "Import Image" button, and follow the instructions to activate Tencent Cloud's Cloud Object Storage (COS) and upload valid images to COS. Click "Next".

5) Fill the appropriate form based on the actual situation. Make sure that you input a valid COS URL. Click "Start Importing".

6) Notification about the result of the import would be sent to the mobile phone or e-mail box bound to your Tencent Cloud account through SMS and e-mail.
