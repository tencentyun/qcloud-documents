In addition to the [Create Custom Image](/doc/product/213/4942) feature, Tencent Cloud also supports image import feature. You can import an image file of a server system disk on the local machine or another platform into the CVM custom images. After the image is imported, you can use it to create a CVM or reinstall the system for an existing CVM.
## Preparations for Import
### Applying for Permission
Before using this feature, make sure that you have activated the image import permission. If you need to activate the permission, contact the Business Manager and submit relevant information to the ticket system.

### Prepare the image file
You need to prepare an image file that meets the import limits in advance.
 - **Limits on Linux images:**

| Image Attribute | Condition |
|---------|---------|
| Operating system | <li>The image that is based on CentOS, Ubuntu, Debian, CoreOS, OpenSUSE, and SUSE distributions.<br><li>Both 32-bit and 64-bit systems are supported. |
| Image format | <li>The image formats such as RAW, VHD, QCOW2 and VMDK are supported.<br><li>Use <code>qemu-img info imageName &#124; grep 'file format'</code> to check the image format. |
| Image size | <li>Use <code>qemu-img info imageName &#124; grep 'disk size'</code> to check the actual size of the image if it does not exceed 50 GB. <br><li>Use <code>qemu-img info imageName &#124; grep 'virtual size'</code> to check the vsize of the image if it does not exceed 500 GB.<br><li>Note: Check the image size when you import an image, which is subject to the information of the image that is converted to the QCOW2 format. |
| Network | <li>Tencent Cloud provides the `eth0` network interface for the instance by default.<br><li>Tencent Cloud does not support IPV6.<br><li>You can query the network configuration of an instance through the metadata service in the instance. For more information, please see [Instance Metadata](/document/product/213/4934). |
| Driver | <li>The virtio driver of the visualization platform KVM must be installed in the image. For more information, please see [Import Image to Linux to Check virtio Driver](/document/product/213/9929).<br><li>It is recommended to install cloudinit for the image. For more information, please see [Import Image to Linux to Install cloudinit](/document/product/213/12587).<br><li>If cloudinit cannot be installed in the image for some reason, you can configure the instance manually by referring to [Forced Import](/document/product/213/12849). |
| Limit on Kernel | <li>Native kernel is preferable for an image. Any modifications may cause failure in importing the image into the CVM. |

 - **Limits on Windows images:**

| Image Attribute | Condition |
|---------|---------|
| Operating system | <li>Microsoft Windows Server 2008 R2 (Standard Edition, Datacenter Edition, Enterprise Edition), Microsoft Windows Server 2012 R2 (Standard Edition).<br><li>Both 32-bit and 64-bit systems are supported. |
| Image format | <li>The image formats such as RAW, VHD, QCOW2 and VMDK are supported. <br><li>Use <code>qemu-img info imageName &#124; grep 'file format'</code> to check the image format. |
| File system type | <li>Only NTFS file system using the MBR-style partition is supported.<br><li>GPT-style partition is not supported.<br><li>Logical Volume Management (LVM) is not supported. |
| Image size | <li>Use <code>qemu-img info imageName &#124; grep 'disk size'</code> to check the actual size of the image if it does not exceed 50 GB.<br><li>Use <code>qemu-img info imageName &#124; grep 'virtual size'</code> to check the vsize of the image if it does not exceed 500 GB.<br><li>Note: Check the image size when you import an image, which is subject to the information of the image that is converted to the QCOW2 format. |
| Network | <li>Tencent Cloud provides the `Local Area Connection` network interface for the instance by default.<br><li>Tencent Cloud does not support IPV6.<br><li>You can query the network configuration of an instance through the metadata service in the instance. For more information, please see [Instance Metadata](/document/product/213/4934). |
| Driver | <li>The virtio driver of the visualization platform KVM must be installed in the image. If it is not installed in the Windows system by default, you can install the [Windows virtio driver](http://windowsvirtio-10016717.file.myqcloud.com/InstallQCloud.exe), and then export the local image. |
| Other | <li>The imported Windows image **does not provide** the [Windows Activation](/doc/product/213/%E6%AD%A3%E7%89%88%E6%BF%80%E6%B4%BB) service. |

## Importing Steps
 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/). 
 2. Click **Image** in the left navigation bar.
 3. Click **Custom Image**, and then click the **Import Image** button.
 4. As instructed in the steps, you need to [**Enable Cloud Object Storage**](https://console.cloud.tencent.com/cos4/index), [**Create bucket**](/doc/product/436/6232), then **Upload the image file to the bucket and [get Image file URL](/doc/product/436/6260)**, and then click **Next**.
 5. Fill in the form according to the actual situation. Be sure to enter the correct COS file URL, and then click **Import**.
 6. You will be notified whether the import is successful or failed via internal message.

## Error Codes
 
| Error Code | Reason | Recommended Processing Method |
|-----|-----|-----|
|InvalidUrl|COS link is invalid | Check if the COS file URL is the same as the imported image URL. |
|InvalidFormatSize|The format or size is unqualified. | The image must meet the limits on `Image format` and `Image size` in [Preparations for Import](#导入准备). |
|VirtioNotInstall|The virtio driver is not installed | Install the virtio driver in the image by referring to the `Driver` section in [Preparations for Import](#导入准备). |
|PartitionNotPresent|The partition information is not found | The image is corrupted probably because it is created incorrectly. |
|CloudInitNotInstalled|cloud-init is not installed | Install cloud-init in the Linux image by referring to the `Driver' section in [Preparations for Import](#导入准备). |
|RootPartitionNotFound|The root partition is not found | The image is corrupted probably because it is created incorrectly. |
|InternalError|Other errors | Contact customer service |


