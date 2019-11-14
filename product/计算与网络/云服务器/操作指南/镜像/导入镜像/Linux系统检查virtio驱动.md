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
 - 如果返回结果中`CONFIG_VIRTIO_BLK` 参数和`CONFIG_VIRTIO_NET` 参数取值为 `m`，请执行步骤2。
 - 如果在返回结果中`CONFIG_VIRTIO_BLK` 参数和`CONFIG_VIRTIO_NET` 参数取值为 `y`，表示该操作系统包含了 Virtio 驱动，您可以直接导入自定义的镜像到腾讯云。操作详情请参见 [导入镜像概述](https://cloud.tencent.com/document/product/213/4945)。
 - 如果在返回结果中没有`CONFIG_VIRTIO_BLK` 参数和`CONFIG_VIRTIO_NET` 参数的信息，表示该操作系统**不支持**导入腾讯云。

<span id="CheckVirtioForInitramfs"></span>
### 步骤2：检查临时文件系统是否包含 Virtio 驱动
如果 [步骤1](#CheckVirtioForKernel) 的执行结果参数取值为 `m`，则需要进一步检查，确认临时文件系统 `initramfs` 或者 `initrd` 是否包含 `virtio` 驱动。请根据操作系统的不同，执行相应命令：
- CentOS 6/CentOS 7/RedHat 6/RedHat 7 操作系统：
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
如果 <code>initramfs</code> 或者 <code>initrd</code> 没有包含 <code>virtio</code> 驱动，请执行步骤3。

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




