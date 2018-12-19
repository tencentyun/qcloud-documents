A CVM must have a kernel supporting virtio drivers (including the block device driver `virtio_blk` and NIC driver `virtio_net`) in order to run on Tencent Cloud. CVMs whose kernels do not have the `virtio_blk` driver must include this driver in the file `initramfs (or initrd)` for normal operation. This document describes how to check and repair the support for virtio drivers before importing images.

## Checking Whether Virtio Drivers are Supported in the Kernel
The following takes `Centos7` as an example to illustrates how to check whether `virtio` driver are supported in the current kernel.

(1) Check whether `virtio` drivers are support in the kernel
```
grep -i virtio /boot/config-$(uname -r)
```
As shown in the figure below, `virtio_blk` and `virtio_net` drivers are compiled as modules in the kernel. (`CONFIG_VIRTIO_BLK=m` means to compile`virtio_blk` as a module in the kernel and `CONFIG_VIRTIO_BLK=y` means to compile `virtio_blk` into the kernel) If no information on the `virtio_net` or `virtio_blk` drivers is found in this step, the image *cannot* be imported to Tencent Cloud.
![](//mc.qcloudimg.com/static/img/4f4c1b835ccc8a344c20fdf34183b48f/image.png)

If the kernel supports both `virtio_blk` and `virtio_net` drivers, and the `virtio_blk` driver is compiled into the kernel (`CONFIG_VIRTIO_BLK=y`), the kernel supports importing without confirmation. If the `virtio_blk` driver is compiled as a module in the kernel (`CONFIG_VIRTIO_BLK=m`), confirmation is required to ensure that the `virtio_blk` driver is properly included in the `initramfs (or initrd)` file.

(2) Check for the `virtio_blk` driver in `initramfs`
```
lsinitrd /boot/initramfs-$(uname -r).img | grep virtio
```
As shown in the figure below, `initramfs` contains the `virtio_blk` driver and the dependent `virtio.ko`, `virtio_pci.ko`, and `virtio_ring.ko`, which means all the neccesary components are included in `initramfs`. In this case, the image can be imported.
![](//mc.qcloudimg.com/static/img/4bac7c12a585eea3cdbd4b27c6a8caa6/image.png)

(3) If no `virtio` information is found in `initramfs`, you must recreate the `initramfs` file.

1) Operations in CentOS 7
```
cp /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak
mkinitrd -f --with=virtio_blk --with=virtio_pci /boot/initramfs-$(uname -r).img $(uname -r)
```
![](//mc.qcloudimg.com/static/img/559c71e11c197ea620a035b0ddd443cf/image.png)

2) Operations in Redhat5/Centos5
a. Check for the driver information in the initrd file, as shown below:
```
mkdir -p /tmp/initrd && cd /tmp/initrd
zcat /boot/initrd-$(uname -r).img | cpio -idmv
find . -name "virtio*"
```

b. If necessary, execute the following command to recreate the `initrd` file.
```
cp /boot/initrd-$(uname -r).img /boot/initrd-$(uname -r).img.bak
mkinitrd -f --with=virtio_blk --with=virtio_pci /boot/initrd-$(uname -r).img $(uname -r)
```

3) Operations in Debian/Ubuntu
a. Check for the virtio driver
```
lsinitramfs /boot/initrd.img-$(uname -r) | grep virtio
```
b. If initramfs does not contain the driver, follow the procedure below to repair it.
```
echo -e "virtio_pci\nvirtio_blk" >> /etc/initramfs-tools/modules
update-initramfs  -u
```

