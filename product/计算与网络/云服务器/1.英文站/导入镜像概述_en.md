In addition to the [Create Custom Image](/doc/product/213/4942) feature, Tencent Cloud also supports import feature. You can import an image file of a server system disk on the local machine or another platform into the CVM custom images. After the image is imported, you can use it to create a CVM or reinstall the system for the existing CVM.
## Preparations for Import


### Preparing Image File
You need to prepare an image file that meets the importing restrictions in advance.
 - **Restrictions for Linux images:**

| Image Attribute | Condition |
|---------|---------|
| Operating system | <li>The image that is based on CentOS, Ubuntu, Debian, CoreOS, OpenSUSE, and SUSE distributions.<br><li>Both 32-bit and 64-bit systems are supported. |
| Image format | <li>The image formats such as RAW, VHD, QCOW2 and VMDK are supported.<br><li>Use<code> qemu-img info imageName &#124; grep 'file format'</code> to view the image format. |
| Image size | <li>If the actual size of an image does not exceed 50 GB, use <code>qemu-img info imageName &#124; grep 'disk size' </code>to check the actual size of the image.<br><li>If the vsize of an image does not exceed 500 GB, use <code>qemu-img info imageName &#124; grep 'virtual size' </code>to check the vsize of the image.<br><li>Note: Review the image size when you import an image, which is subject to the information of the image that is converted to the QCOW2 format. |
| System disk | <li>Only system disks can be imported into Tencent Cloud. |
| Network | <li>Tencent Cloud provides the `eth0` network interface for the instance by default.<br><li>Tencent cloud does not support IPV6.<br><li>Users can query the network configuration of an instance through the metadata service in the instance. For more information, please see [Instance Metadata](/document/product/213/4934). |
| Driver | <li>The virtio driver of the visualization platform KVM must be installed in the image. For more information, please see [Linux Imports Image to Check Virtio Driver](/document/product/213/9929).<br><li>It is recommended to install cloudinit for the image. For more information, please see [Linux Imports Image to Install cloudinit](/document/product/213/12587).<br><li>If cloudinit cannot be installed in the image for some reason, you can configure the instance manually according to the steps of [Forced Import](/document/product/213/12849). |
| Limit on Kernel | <li>For an image, the native kernel is preferred. Any modifications may cause failure in importing the image into the virtual machine. |

 - **Restrictions for Windows images:**

| Image Attribute | Condition |
|---------|---------|
| Operating system | <li>Microsoft Windows Server 2008 R2 (Standard Edition, Datacenter Edition, Enterprise Edition), Microsoft Windows Server 2012 R2 (Standard Edition).<br><li>Only 64-bit system is supported. |
| Image format | <li>The image formats such as RAW, VHD, QCOW2 and VMDK are supported.<br><li>Use<code> qemu-img info imageName &#124; grep 'file format'</code> to view the image format. |
| File system type | <li>Only NTFS file system that uses MBR partitioning is supported.<br><li>GPT partitioning is not supported.<br><li>Logical Volume Management (LVM) is not supported. |
| Image size | <li>If the actual size of an image does not exceed 50 GB, use <code>qemu-img info imageName &#124; grep 'disk size' </code>to check the actual size of the image.<br><li>If the vsize of an image does not exceed 500 GB, use <code>qemu-img info imageName &#124; grep 'virtual size' </code>to check the vsize of the image.<br><li>Note: Review the image size when you import an image, which is subject to the information of the image that is converted to the QCOW2 format. |
| System disk | Only system disks can be imported into Tencent Cloud. |
| Network | <li>Tencent Cloud provides the `eth0` network interface for the instance by default.<br><li>Tencent cloud does not support IPV6.<br><li>Users can query the network configuration of an instance through the metadata service in the instance. For more information, please see [Instance Metadata](/document/product/213/4934). |
| Driver | <li>The virtio driver of the visualization platform KVM must be installed in the image. If the Windows system is not installed with a virtio driver by default, you can install the [Windows Virtio Driver](http://windowsvirtio-10016717.file.myqcloud.com/InstallQCloud.exe), and then export the local image. |
| Other | <li>The imported Windows image **does not provide** the [Windows Activation](/doc/product/213/%E6%AD%A3%E7%89%88%E6%BF%80%E6%B4%BB) service. |

## Importing Steps
 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
 2. Click **Image** in the left navigation bar.
 3. Click **Custom Images**, and then click the **Import Image** button.
 4. As instructed in the steps, you first need to [Activate COS](https://console.cloud.tencent.com/cos4/index), then [Create Bucket](/doc/product/436/6232), upload the image file to the bucket and [Obtain the Image File URL](/doc/product/436/6260), and then click **Next**.
 5. Fill in the form according to the actual situation, make sure that the URL of the COS file you entered is correct, and then click **Start Importing**.
 6. You will be notified whether the import is successful or failed via internal message.

## Error Codes
 
| Error Code | Reason | Recommended Processing Method |
|-----|-----|-----|
| InvalidUrl | COS link is invalid | Check if the COS link is the same as the link of the imported image. |
| InvalidFormatSize | The format or size does not meet the conditions. | The image needs to meet the restrictions on the `image format` and `image size` in [Import Preparation](#导入准备). |
| VirtioNotInstall | The virtio driver is not installed | Install the virtio driver in the image by referring to the `Driver` section in [Import Preparation](#导入准备). |
| PartitionNotPresent | The partition information is not found | The image is corrupted, which is possibly caused by the incorrect image creation method. |
| CloudInitNotInstalled | cloud-init is not installed | Install cloud-init in the Linux image by referring to the `Driver` section in [Import Preparation](#导入准备). |
| RootPartitionNotFound | The root partition is not detected | The image is corrupted, which is possibly caused by the incorrect image creation method. |
| InternalError | Other errors | Please contact the customer service to solve the problem. |


