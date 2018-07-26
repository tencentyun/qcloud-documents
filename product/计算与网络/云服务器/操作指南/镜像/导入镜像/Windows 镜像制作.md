## 一. 准备工作
制作系统盘镜像导出时需要做以下检查，数据盘镜像导出可以忽略。
- 检查 OS 分区，目前服务迁移不支持 GPT 分区。
检查分区的方法：
依次打开【控制面板】>【磁盘管理】，在磁盘右键选择【属性】，如下图可以看到磁盘分区形式。
![image](https://main.qcloudimg.com/raw/4052bede45120da38445995a6d66b1a6.jpg)
磁盘分区形式如果为 GPT，则说明该磁盘是 GPT 分区。

- 检查启动方式，目前服务迁移不支持 EFI 启动。
如果 path 中有 efi，则说明目前操作系统是以 EFI 方式启动。
以管理员身份打开命令提示符（CMD），然后执行：
```
bcdedit /enum {current}
```

运行结果示例：
```
C:\WINDOWS\system32>bcdedit /enum {current}

Windows 启动加载器
-------------------
标识符                  {current}
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

- 检查网络配置，目前服务迁移不支持 IPv6，不支持多网卡。依赖于 IPv6 和多网卡的服务都无法正常工作。

- 卸载会产生冲突的驱动和软件（包括 VMware tools，Xen tools， Virtualbox GuestAdditions 以及一些自带底层驱动的软件）。

- 安装 cloud-base：请参考 [cloud-base 安装文档](https://cloud.tencent.com/document/product/213/12587)。

- 检查或安装 virtio 驱动
在【控制面板】>【程序和功能】中搜索到 virtio，如下图示，则说明已安装 virtio：
![image](https://main.qcloudimg.com/raw/de738e8549cb0f090f53038104ae3428.jpg
)
否则需要手动安装 virtio 驱动：
 - 以下系统版本，驱动下载：[腾讯云定制版virtio](http://windowsvirtio-10016717.file.myqcloud.com/InstallQCloud.exe?_ga=1.44298212.1367540472.1504757536)
Microsoft Windows Server 2008 R2（标准版、数据中心版、企业版)，Microsoft Windows Server 2012 R2（标准版）
 - 其它系统版本，请下载 [社区版本 virtio](https://www.linux-kvm.org/page/WindowsGuestDrivers/Download_Drivers)。

- 检查其它硬件相关的配置，上云之后的硬件变化包括但可能不限于：
 - 显卡更换为 cirrus vga；
 - 磁盘更换为 virtio disk；
 - 网卡更换为 virtio nic，默认为本地连接。

## 二. 使用平台工具导出
使用 VMWare vCenter Convert 或 Citrix XenConvert 等虚拟化平台的导出镜像工具，详情请见各平台的导出工具文档。目前腾讯云服务迁移支持的镜像格式有：qcow2，vhd，raw，vmdk。

## 三. 使用 disk2vhd 导出镜像
如果待导出系统是在物理机，或者不想使用平台工具导出，那么可以选择 disk2vhd 工具。
[下载 disk2vhd](https://download.sysinternals.com/files/Disk2vhd.zip)

安装后界面如下图：
![image](https://main.qcloudimg.com/raw/68d9c4e5e7db49c4cefdd3785ce9b68d.jpg)

使用时勾选需要复制的卷，以及导出的文件名，单击【Create】即可导出 vhd 。

> **注意：**
- disk2vhd 需要 Windows 预装 vss 功能后才能运行。
- 请勿勾选"Use Vhdx"，目前系统不支持 vhdx 格式的镜像。
- 建议勾选"Use volume Shadow Copy"，使用卷影复制功能，将能更好地保证数据完整性。

## 四. 镜像检查
如上所述，当不停服制作镜像或者其它原因，可能导致制作出的镜像文件系统有误，因此建议在制作镜像后检查是否无误。

当镜像格式和当前平台支持的格式一致时，可以直接打开镜像检查文件系统。 例如 Windows 平台可以直接附加 vhd 格式镜像，Linux 可以使用 qemu-nbd 打开 qcow2 格式镜像，Xen 平台可以直接启用 vhd 文件。 以 Linux 平台为例：
```
modprobe nbd
qemu-nbd -c /dev/nbd0 xxxx.qcow2
mount /dev/nbd0p1 /mnt
```
如果 qcow2 镜像的第一个分区导出时文件系统被破坏，mount 时将会报错。

此外还可以在上传镜像前，先启动虚拟机测试镜像文件是否可以使用。
