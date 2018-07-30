## 1. Preparations
The following checks are required to export a system disk image, and can be ignored when you export a data disk image.
- Check the OS partition. Service Migration does not support GPT-style partition.
How to check the partition:
Open the **Control Panel** -> **Disk Management**, right-click the disk to select **Property**, and you can find the Partition style in the figure below.
![image](https://main.qcloudimg.com/raw/4052bede45120da38445995a6d66b1a6.jpg)
If it reads GPT, the GPT-style partition is used.

- Check the startup mode. Service Migration does not support starting the system with EFI.
If EFI exists in the path, then the current operating system starts in the EFI mode.
Open the command prompt (CMD) as admin and execute the following command:
```
bcdedit /enum {current}
```

Example of execution result:
```
C:\WINDOWS\system32>bcdedit /enum {current}

Windows  bootstrapper
-------------------
identifier                  {current}
device                  partition=C:
path                    \WINDOWS\system32\winload.exe
description             Windows 10
locale                  zh-CN
inherit                 {bootloadersettings}
recoverysequence        {f9dbeba1-1935-11e8-88dd-ff37cca2625c}
displaymessageoverride  Recovery
recoveryenabled         Yes
flightsigning           Yes
allowedinmemorysettings 0x15000075
osdevice                partition=C:
systemroot              \WINDOWS
resumeobject            {1bcd0c6f-1935-11e8-8d3e-3464a915af28}
nx                      OptIn
bootmenupolicy          Standard
```

- Check the network configuration. Service Migration does not support IPv6 nor multi-ENI. Services that rely on both IPv6 and multi-ENI cannot work normally.

- Unmount the drivers and software that produce conflicts (including VMware tools, Xen tools, Virtualbox GuestAdditions and other software that comes with underlying drivers).

- Install cloud-base: Please see [Install cloud-base](https://cloud.tencent.com/document/product/213/12587).

- Check or install the virtio driver
The virtio driver has been installed if it is found in the **Control Panel** -> **Programs and Features**:
![image](https://main.qcloudimg.com/raw/de738e8549cb0f090f53038104ae3428.jpg
)
Otherwise, you need to manually install the virtio driver:
 - For the following system versions, download [Tencent Cloud's customized virtio](http://windowsvirtio-10016717.file.myqcloud.com/InstallQCloud.exe?_ga=1.44298212.1367540472.1504757536)
Microsoft Windows Server 2008 R2 (Standard Edition, Datacenter Edition, Enterprise Edition), Microsoft Windows Server 2012 R2 (Standard Edition)
 - For other system versions, download the [virtio community version](https://www.linux-kvm.org/page/WindowsGuestDrivers/Download_Drivers).

- Check the configurations of other hardware. Changes to the hardware on the cloud include but not limited to:
 - Replacing the graphics card with cirrus vga.
 - Replacing the disk with virtio disk.
 - Replacing the ENI with virtio nic. Local Area Connection is used by default.

## 2. Export the Image Using a Platform Tool
For more information on how to use image export tools of VMWare vCenter Convert, Citrix XenConvert and other virtualization platforms, please see the relevant document of each platform. The image formats supported by Tencent Cloud Service Migration include qcow2, vhd, raw, and vmdk.

## 3. Export the Image Using Disk2vhd
The Disk2vhd tool can be used to export the system if it is deployed on a physical machine or if you do not want to export it using a platform tool.
[Download Disk2vhd](https://download.sysinternals.com/files/Disk2vhd.zip)

The interface after installation is shown as below:
![image](https://main.qcloudimg.com/raw/68d9c4e5e7db49c4cefdd3785ce9b68d.jpg)

When using the tool, select the volume to be copied and the name of the file to be exported, and click **Create** to export vhd.

> **Note:**
- The vss feature must be preset in Windows before Disk2vhd can run.
- Do not select "Use Vhdx". The system does not support vhdx images.
- "Use volume Shadow Copy" should be selected to ensure the data integrity.

## 4. Check the Image
As mentioned above, an error may be occurred with the image file system if it is created when the server is not shut down or due to other reasons. Therefore, you are recommended to check whether the created image is error-free.

When the image format is consistent with the format supported by the current platform, you can directly open the image to check the file system. For example, vhd images can be directly added to Windows platform, qcow2 images can be opened using qemu-nbd on Linux platform, and vhd images can be enabled directly on Xen platform. Take the Linux platform as an example:
```
modprobe nbd
qemu-nbd -c /dev/nbd0 xxxx.qcow2
mount /dev/nbd0p1 /mnt
```
If the file system is corrupted when the first partition of the qcow2 image is exported, an error will occur when using the mount command.

In addition, you can start the CVM to check whether the image file works before uploading the image.

