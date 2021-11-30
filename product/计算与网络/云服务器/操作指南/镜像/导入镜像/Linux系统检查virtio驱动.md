## 操作场景
云服务器系统内核需要支持 Virtio 驱动（包括块设备驱动 `virtio_blk` 和网卡驱动 `virtio_net`）才能在腾讯云上正常运行。为避免导入自定义镜像后，创建的云服务器实例无法启动，您需要在导入镜像前，检查是否需要在源服务器中检查以及修复镜像中对 Virtio 驱动的支持。本文档以 CentOS 操作系统为例，指导您如何在导入镜像前进行检查以及修复镜像中对 Virtio 驱动的支持。

## 操作步骤

<span id="CheckVirtioForKernel"></span>
### 步骤1：检查内核是否支持 Virtio 驱动
执行以下命令，确认当前内核是否支持 Virtio 驱动。
```
grep -i virtio /boot/config-$(uname -r)
```
返回类似如下结果：
![](https://main.qcloudimg.com/raw/8c32c3dd554700a0c17ff0c7e5675090.png)
 - 如果返回结果中`CONFIG_VIRTIO_BLK` 参数和`CONFIG_VIRTIO_NET` 参数取值为 `m`，请执行 [步骤2](#CheckVirtioForInitramfs)。
 - 如果在返回结果中`CONFIG_VIRTIO_BLK` 参数和`CONFIG_VIRTIO_NET` 参数取值为 `y`，表示该操作系统包含了 Virtio 驱动，您可以直接导入自定义的镜像到腾讯云。操作详情请参见 [导入镜像概述](https://cloud.tencent.com/document/product/213/4945)。
 - 如果在返回结果中没有`CONFIG_VIRTIO_BLK` 参数和`CONFIG_VIRTIO_NET` 参数的信息，表示该操作系统**不支持**导入腾讯云，请 [下载和编译内核](#DownloadCompileKernel)。

<span id="CheckVirtioForInitramfs"></span>
### 步骤2：检查临时文件系统是否包含 Virtio 驱动
如果 [步骤1](#CheckVirtioForKernel) 的执行结果参数取值为 `m`，则需要进一步检查，确认临时文件系统 `initramfs` 或者 `initrd` 是否包含 `virtio` 驱动。请根据操作系统的不同，执行相应命令：
- CentOS 6/CentOS 7/CentOS 8/RedHat 6/RedHat 7 操作系统：
```
lsinitrd /boot/initramfs-$(uname -r).img | grep virtio
```
- RedHat 5/CentOS 5 操作系统：
```
mkdir -p /tmp/initrd && cd /tmp/initrd
zcat /boot/initrd-$(uname -r).img | cpio -idmv
find . -name "virtio*"
```
- Debian/Ubuntu 操作系统：
```
lsinitramfs /boot/initrd.img-$(uname -r) | grep virtio
```

返回类似如下结果：
<img src="https://main.qcloudimg.com/raw/a5e22f75f48ce26a6b03f65588a52877.png" />
可得知，<code>initramfs</code> 已经包含了 <code>virtio_blk</code> 驱动，以及其所依赖的 <code>virtio.ko</code>、<code>virtio_pci.ko</code> 和 <code>virtio_ring.ko</code>，您可以直接导入自定义的镜像到腾讯云。操作详情请参见 <a href="https://cloud.tencent.com/document/product/213/4945">导入镜像概述</a>。
如果 <code>initramfs</code> 或者 <code>initrd</code> 没有包含 <code>virtio</code> 驱动，请执行 [步骤3](#ReconfigureInitramfs)。

<span id="ReconfigureInitramfs"></span>
### 步骤3：重新配置临时文件系统
如果 [步骤2](#CheckVirtioForInitramfs) 的执行结果显示临时文件系统 `initramfs` 或者 `initrd` 没有包含 `virtio` 驱动，则需要重新配置临时文件系统 `initramfs` 或者 `initrd`，使其包含 `virtio` 驱动。请根据操作系统的不同，选择相应操作：
 - CentOS 6/CentOS 7/RedHat 6/RedHat 7 操作系统：
```
cp /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak
mkinitrd -f --with=virtio_blk --with=virtio_pci /boot/initramfs-$(uname -r).img $(uname -r)
```
 - RedHat 5/CentOS 5 操作系统：
```
cp /boot/initrd-$(uname -r).img /boot/initrd-$(uname -r).img.bak
mkinitrd -f --with=virtio_blk --with=virtio_pci /boot/initrd-$(uname -r).img $(uname -r)
```
 - Debian/Ubuntu 操作系统：
```
echo -e "virtio_pci\nvirtio_blk" >> /etc/initramfs-tools/modules
update-initramfs  -u
```

## 附录
<span id="DownloadCompileKernel"></span>
### 下载和编译内核

#### 下载内核安装包
1. 执行以下命令，安装编译内核的必要组件。
```
yum install -y ncurses-devel gcc make wget
```
2. 执行以下命令，查询当前系统使用的内核版本。
```
uname -r
```
返回类似如下结果，当前系统使用的内核版本为`2.6.32-642.6.2.el6.x86_64`。
![](https://main.qcloudimg.com/raw/739b19fc7af96d6de7872df0a498b7b6.png)
3. 前往 [Linux 内核下载页面](https://www.kernel.org/pub/linux/kernel/?spm=a2c4g.11186623.2.26.7e4179b4zo5WVJ)，下载对应的内核版本源码。
例如，`2.6.32-642.6.2.el6.x86_64`版本的内核下载 `linux-2.6.32.tar.gz` 的安装包，其下载路径为：`https://mirrors.edge.kernel.org/pub/linux/kernel/v2.6/linux-2.6.32.tar.gz`。
4. 执行以下命令，切换目录。
```
cd /usr/src/
```
5. 执行以下命令，下载安装包。
```
wget https://mirrors.edge.kernel.org/pub/linux/kernel/v2.6/linux-2.6.32.tar.gz
```
6. 执行以下命令，解压安装包。
```
tar -xzf linux-2.6.32.tar.gz
```
7. 执行以下命令，建立链接。
```
ln -s linux-2.6.32 linux
```
8. 执行以下命令，切换目录。
```
cd /usr/src/linux
```

#### 编译内核

1. 依次执行以下命令，编译内核。
```
make mrproper
cp /boot/config-$(uname -r) ./.config
make menuconfig
```
进入 “Linux Kernel vX.X.XX Configuration” 界面。如下图所示：
![](https://main.qcloudimg.com/raw/72c3bea10627aaef022f1a72b72ac79a.png)
>? 如果没有进入 “Linux Kernel vX.X.XX Configuration” 界面，请执行 [步骤18](#OptionalStep)。
> “Linux Kernel vX.X.XX Configuration” 界面：
> - 按 “Tab” 或 “↑” “↓” 方向键移动光标。
> - 按 “Enter” 选择或执行光标所选项目。
> - 按空格键选中光标所选项目，“\*” 表示编译到内核，“M” 表示编译为模块。 
> 
2. 按 “↓” 键将光标调到 “Virtualization”，并按空格键选中 “Virtualization”。
3. 在 “Virtualization” 处按 “Enter”，进入 Virtualization 详情界面。
4. 在 Virtualization 详情界面，确认是否勾选了 Kernel-based Virtual Machine （KVM）support 选项。如下图所示：
![](https://main.qcloudimg.com/raw/d5614d31ebaed0f0b270dc1046b9ff2e.png)
若未勾选，请按空格键选中 “Kernel-based Virtual Machine （KVM）support” 选项。
5. 按 “Esc” 返回 “Linux Kernel vX.X.XX Configuration” 主界面。
6. 按 “↓” 键将光标调到 “Processor type and features”，并按 “Enter”，进入 Processor type and features 详情界面。
7. 按 “↓” 键将光标调到 “Paravirtualized guest support”，并按 “Enter”，进入 Paravirtualized guest support 详情界面。
8. 在 Paravirtualized guest support 详情界面，确认是否勾选了 “KVM paravirtualized clock” 和 “KVM Guest support”。如下图所示：
![](https://main.qcloudimg.com/raw/2e49f9b46ecb9f9d272db36dffbade07.png)
若未勾选，请按空格键选中 “KVM paravirtualized clock” 和 “KVM Guest support” 选项。
9. 按 “Esc” 返回 “Linux Kernel vX.X.XX Configuration” 主界面。
10. 按 “↓” 键将光标调到 “Device Drivers”，并按 “Enter”，进入 Device Drivers 详情界面。
11. 按 “↓” 键将光标调到 “Block devices”，并按 “Enter”，进入 Block devices 详情界面。
12. 在 Block devices 详情界面，确认是否勾选了 “Virtio block driver (EXPERIMENTAL)”。如下图所示：
![](https://main.qcloudimg.com/raw/79f3e29a6d77224a164c6c716e41fa84.png)
若未勾选，请按空格键选中 “Virtio block driver (EXPERIMENTAL)” 选项。
13. 按 “Esc” 返回 Device Drivers 详情界面。
14. 按 “↓” 键将光标调到 “Network device support”，并按 “Enter”，进入 Network device support 详情界面。
15. 在 Network device support 详情界面，确认是否勾选了 “Virtio network driver (EXPERIMENTAL)”。如下图所示：
![](https://main.qcloudimg.com/raw/811388c89393882ea83bceb7a00bc1b7.png)
若未勾选，请按空格键选中 “Virtio network driver (EXPERIMENTAL)” 选项。
16. 按 “Esc” 退出内核配置界面，并根据弹窗提示，选择 “YES”，保存 `.config` 文件。
17. 参考 [步骤1：检查内核是否支持 Virtio 驱动](#CheckVirtioForKernel)，验证 Virtio 驱动是否已经正确配置。
18. <span id="OptionalStep"></span>（可选）执行以下命令，手动编辑 `.config` 文件。
>? 如果您符合如下任一条件，建议执行此操作：
> - 若检查后发现，内核仍无 Virtio 驱动的相关配置信息。
> - 编译内核时，无法进入内核配置界面或者未成功保存 `.config` 文件。
> 
```
make oldconfig
make prepare
make scripts
make
make install
```
19. 依次执行以下命令，查看 Virtio 驱动的安装情况。
```
find /lib/modules/"$(uname -r)"/ -name "virtio.*" | grep -E "virtio.*"
grep -E "virtio.*" < /lib/modules/"$(uname -r)"/modules.builtin
```
如果任一命令的返回结果输出 `virtio_blk`、`virtio_pci.virtio_console` 等文件列表，即表明您已经正确安装了 Virtio 驱动。



