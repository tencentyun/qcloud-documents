云服务器系统内核需要支持virtio驱动（包括块设备驱动 `virtio_blk` 和网卡驱动 `virtio_net`）才能在腾讯云上正常运行，对于未编译进内核的`virtio_blk` 驱动，还需要包含在`initramfs(或者initrd)`文件中，云服务器才能正常工作，本文将说明导入镜像前如何检查以及修复镜像中对 virtio 驱动的支持。

## 内核支持virtio驱动检查
以`Centos7`为例详细说明如何确定当前内核是否支持`virtio`驱动

（1）确认当前内核是否支持`virtio`驱动
```
grep -i virtio /boot/config-$(uname -r)
```
如下图所示：当前内核包含了`virtio_blk`和`virtio_net`驱动，并且是以模块形式编译的（`CONFIG_VIRTIO_BLK=m`，表示编译成为内核模块，等于y表示编译进内核），如果这一步没有找到`virtio_net`或`virtio_blk`的驱动信息，那么该镜像 *不支持* 导入腾讯云。
![](//mc.qcloudimg.com/static/img/4f4c1b835ccc8a344c20fdf34183b48f/image.png)

如果内核支持`virtio`驱动（`virtio_blk`和`virtio_net`都支持），且`virtio_blk`驱动编译进入了内核（即`CONFIG_VIRTIO_BLK=y`），则该内核支持导入，不需要后续确认，如果`virtio_blk`驱动是编译成内核模块的（即`CONFIG_VIRTIO_BLK=m`），则还需要继续后续确认步骤，确认`virtio_blk`驱动正确包含进了`initramfs（或initrd）`文件中。

（2）确认`initramfs`中是否包含`virtio_blk`驱动
```
lsinitrd /boot/initramfs-$(uname -r).img | grep virtio
```
如下图所示，`initramfs`中包含了`virtio_blk`驱动，以及其所依赖的`virtio.ko`、`virtio_pci.ko`、`virtio_ring.ko`，这样`initramfs`包含驱动正常，该镜像可以导入。
![](//mc.qcloudimg.com/static/img/4bac7c12a585eea3cdbd4b27c6a8caa6/image.png)

（3）如果`initramfs`中未找到相关的`virtio`信息，则需要重新制作`initramf`s文件

1) CentOS 7 操作方法
```
cp /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak
mkinitrd -f --with=virtio_blk --with=virtio_pci /boot/initramfs-$(uname -r).img $(uname -r)
```
![](//mc.qcloudimg.com/static/img/559c71e11c197ea620a035b0ddd443cf/image.png)

2) Redhat5/Centos5 操作方法
a. 通过如下方式确定initrd文件中是否包含驱动信息
```
mkdir -p /tmp/initrd && cd /tmp/initrd
zcat /boot/initrd-$(uname -r).img | cpio -idmv
find . -name "virtio*"
```

b. 如果需要重新制作`initrd`文件，执行以下命令
```
cp /boot/initrd-$(uname -r).img /boot/initrd-$(uname -r).img.bak
mkinitrd -f --with=virtio_blk --with=virtio_pci /boot/initrd-$(uname -r).img $(uname -r)
```

3) Debian/Ubuntu 操作方法
a. 检查virtio驱动情况
```
lsinitramfs /boot/initrd.img-$(uname -r) | grep virtio
```
b. 如果initramfs中未包含，则执行以下步骤修复
```
echo -e "virtio_pci\nvirtio_blk" >> /etc/initramfs-tools/modules
update-initramfs  -u
```
