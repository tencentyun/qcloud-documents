## 操作场景
本文以 Windows Server 2012 操作系统为例，指引您如何制作 Windows 镜像。若使用其他版本 Windows Server 操作系统，也可参考本文进行镜像制作。

## 操作步骤

### 准备工作

制作系统盘镜像导出时，需要进行以下检查：
>? 如果您是通过数据盘镜像导出，则可以跳过此操作。
>

#### 检查 OS 分区和启动方式

1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: 0;">，打开 Windows PowerShell 窗口。
2. 在 Windows PowerShell 窗口中，输入 **diskmgmt.msc**，按 **Enter**，打开 “磁盘管理”。
3. 右键单击需要检查的磁盘 >【属性】，选择【卷】页签，查看磁盘分区形式。
2. 判断磁盘分区形式是否为 GPT 分区。
 - 是，因服务迁移暂不支持 GPT 分区，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 反馈。
 - 否，请执行下一步。
3. 使用管理员身份打开 CMD，并执行以下命令，检验操作系统是否以 EFI 方式启动。
```
bcdedit /enum {current}
```
以以下返回结果为例：
```
Windows 启动加载器
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
 - 若 `path` 参数中含有 efi，则表示当前操作系统以 EFI 方式启动，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 反馈。
 - 若 `path` 参数中没有 efi，请执行下一步。

#### 卸载软件

卸载会产生冲突的驱动和软件（包括 VMware tools，Xen tools， Virtualbox GuestAdditions 以及一些自带底层驱动的软件）。

#### 安装 cloud-base

安装详情请参考 [cloud-base 安装文档](https://cloud.tencent.com/document/product/213/30000)。

#### 检查或安装 Virtio 驱动

1. 打开【控制面板】>【程序和功能】，并在搜索栏中搜索 Virtio。
 - 若返回结果如下图示，则表示已安装了 Virtio 驱动。
![](https://main.qcloudimg.com/raw/d8b0c17385de25bd41cdfcd291008f5c.png)
 - 若没有安装 Virtio 驱动，则需要手动安装。
    - Microsoft Windows Server 2008 R2（标准版、数据中心版、企业版）、Microsoft Windows Server 2012 R2（标准版）、Microsoft Windows Server 2016（数据中心版）、Microsoft Windows Server 2019（数据中心版）请下载腾讯云定制版 Virtio。下载地址如下，请对应实际网络环境下载：
      -  公网下载地址：`http://mirrors.tencent.com/install/windows/virtio_64_1.0.9.exe`
      -  内网下载地址：`http://mirrors.tencentyun.com/install/windows/virtio_64_1.0.9.exe`
    - 其它系统版本，请下载 [社区版本 virtio](https://www.linux-kvm.org/page/WindowsGuestDrivers/Download_Drivers)。

#### 检查其它硬件相关的配置

上云之后的硬件变化包括但可能不限于：
 - 显卡更换为 Cirrus VGA。
 - 磁盘更换为 Virtio Disk。
 - 网卡更换为 Virtio Nic，默认为本地连接。

### 导出镜像
根据实际需求，选择不同的工具导出镜像：
<dx-tabs>
::: 使用平台工具导出镜像[](id:Useplatform)
使用 VMWare vCenter Convert 或 Citrix XenConvert 等虚拟化平台的导出镜像工具。详情请参见各平台的导出工具文档。
>? 目前腾讯云服务迁移支持的镜像格式有：qcow2，vhd，raw，vmdk。
>
:::
::: 使用\sdisk2vhd\s导出镜像[](id:Usedisk2vhd)
当您的需要导出物理机上的系统或者不想使用平台工具导出时，可以使用 disk2vhd 工具进行导出。
1. 安装并打开 disk2vhd 工具。
[点此下载 disk2vhd 工具 >>](https://download.sysinternals.com/files/Disk2vhd.zip)
3. 选择需要导出的镜像存放路径，勾选需要复制的卷，单击【Create】。如下图所示：
>! 
> - disk2vhd 需要 Windows 预装 VSS（卷影拷贝服务）功能后才能运行。关于 VSS 功能的更多信息请参见 [Volume Shadow Copy Service](https://docs.microsoft.com/zh-cn/windows/win32/vss/volume-shadow-copy-service-portal?redirectedfrom=MSDN)。
> - 请勿勾选 “Use Vhdx”，目前系统不支持 vhdx 格式的镜像。
> - 建议勾选 “Use volume Shadow Copy”，使用卷影复制功能，将能更好地保证数据完整性。
> 
![image](https://main.qcloudimg.com/raw/68d9c4e5e7db49c4cefdd3785ce9b68d.jpg)
:::
</dx-tabs>


### 转换镜像格式（可选）
参考 [转换镜像镜像](https://cloud.tencent.com/document/product/213/62569#windows)，使用 `qemu-img` 将镜像文件转换为支持的格式。

### 检查镜像

>? 当您未停止服务直接制作镜像或者其它原因，可能导致制作出的镜像文件系统有误，因此建议您在制作镜像后检查是否无误。
>
当镜像格式和当前平台支持的格式一致时，您可以直接打开镜像检查文件系统。 例如，Windows 平台可以直接附加 vhd 格式镜像，Linux 平台可以使用 qemu-nbd 打开 qcow2 格式镜像，Xen 平台可以直接启用 vhd 文件。

本文以 Windows 平台为例，通过“磁盘管理”中的“附加 VHD”，查看 vhd 格式镜像。步骤如下：
1. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/3d815ac1c196b47b2eea7c3a516c3d88.png" style="margin:-4px 0px">，并在弹出菜单中选择【计算机管理】。
2. 选择【存储】>【磁盘管理】，进入磁盘管理界面。
3. 在窗口上方选择【操作】>【附加 VHD】。如下图所示：
![](https://main.qcloudimg.com/raw/447f09239201bfccd8adf62bd804c13e.png)
出现如下图所示结果，表示已成功制作镜像。
![](https://main.qcloudimg.com/raw/8a487604cfccb0bf34caad4cc75b3b15.png)
