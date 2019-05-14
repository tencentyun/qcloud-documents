## 1. Preparations
Check the followings before exporting a system disk image. Ignore them if you're exporting a data disk image.

- OS partition - Service Migration does not support GPT-style partition.
```
sudo parted -l /dev/sda | grep 'Partition Table'
```
"msdos" represents MBR-style partition, and "gpt" represents GPT-style partition.

- Check the startup mode. Service Migration does not support starting the system with EFI.
```
sudo ls /sys/firmware/efi
```
If the EFI file exists, then the current system starts in the EFI mode, and it is necessary to confirm that there is a traditional startup item in grub.

- Check the network configuration. Service Migration does not support IPv6 nor multi-ENI. Services that rely on both IPv6 and multi-ENI cannot work normally.

- Check system-critical files, including but not limited to the following system files:
> Follow the standards of relevant distributions to ensure that the locations and permissions of the system-critical files are correct and the files can be read and written normally.

 - /etc/grub/grub.cfg: In the kernel parameter, uuid is recommended for mounting root. Other methods (such as root=/dev/sda) may cause the failure in starting the system.
 - /etc/fstab: Do not mount other disks. After migration, the system may fail to start due to disk missing.
 - /etc/shadow: It has normal permissions and can be read and written.

- Unmount the drivers and software that produce conflicts (including VMware tools, Xen tools, Virtualbox GuestAdditions and other software that comes with underlying drivers).

- Check the virtio driver: Please see [Check virtio Driver in Linux System](https://cloud.tencent.com/document/product/213/9929).

- Install cloud-init: Please see [Install cloud-init](https://cloud.tencent.com/document/product/213/12587).

- Check other hardware-related configurations, such as driver settings in the Linux desktop environment. Changes to the hardware on the cloud include but not limited to:
 - Replacing the graphics card with cirrus vga.
 - Replacing the disk with virtio disk. Device name is vda, vdb, and so on.
 - Replacing the ENI with virtio nic. By default, only eth0 is available.

## Determining Partitions and Sizes
Use the mount command to confirm the current partition format and determine the partitions to be copied and their sizes.
Example:
```
mount
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
sys on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
dev on /dev type devtmpfs (rw,nosuid,relatime,size=4080220k,nr_inodes=1020055,mode=755)
run on /run type tmpfs (rw,nosuid,nodev,relatime,mode=755)
/dev/sda1 on / type ext4 (rw,relatime,data=ordered)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,mode=755)
cgroup on /sys/fs/cgroup/unified type cgroup2 (rw,nosuid,nodev,noexec,relatime,nsdelegate)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,xattr,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,cpu,cpuacct)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,cpuset)
cgroup on /sys/fs/cgroup/rdma type cgroup (rw,nosuid,nodev,noexec,relatime,rdma)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,blkio)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,hugetlb)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,memory)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,pids)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,freezer)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,net_cls,net_prio)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,perf_event)
systemd-1 on /home/libin/work_doc type autofs (rw,relatime,fd=33,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=12692)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=39,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=12709)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
mqueue on /dev/mqueue type mqueue (rw,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime,pagesize=2M)
tmpfs on /tmp type tmpfs (rw,nosuid,nodev)
configfs on /sys/kernel/config type configfs (rw,relatime)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=817176k,mode=700,uid=1000,gid=100)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=100)
```
According to the example, the root partition is `/dev/sda1`, and no boot or home partition is created independently. You can copy the entire sda or copy it to the end of sda1.

The exported image should contain at least the root partition and mbr. If `/boot` and `/home` partitions are created, you also need to include these two independent partitions.
> **Note:**
> "mbr" should be included when you copy sda, otherwise the system cannot start. Even if the boot partition is included in sda1, the system may fail to start without mbr, so sda must be copied.


## Exporting Images with Tools
For more information on how to use image export tools of VMWare vCenter Convert, Citrix XenConvert and other virtualization platforms, please see the relevant document of each platform. The image formats supported by Tencent Cloud Service Migration include qcow2, vhd, raw, and vmdk.

## Exporting Images with Commands
### Use qemu-img command
Example:
```
sudo qemu-img convert -f raw -O qcow2 /dev/sda /mnt/sdb/test.qcow2
```
This command is used to export the entire `/dev/sda` disk to `/mnt/sdb/test.qcow2`. Another disk or other network storage should be mounted to `/mnt/sdb`.
To change to other parameters, you need to modify the `-O` parameter. The following parameters are available:

<a id="-o"></a>
Value | Description
---|---
qcow2 | qcow2 format
vpc | vhd format
vmdk | vmdk format
raw | None

### Use dd command
Example:
```
sudo dd if=/dev/sda of=/mnt/sdb/test.imag bs=1K count=$count
```
The image exported using dd is in raw format and needs to be converted again. The count parameter determines the number of bytes to be copied, which can be queried with the fdisk command:
```
fdisk -lu /dev/sda

Disk /dev/sda: 1495.0 GB, 1494996746240 bytes
255 heads, 63 sectors/track, 181756 cylinders, total 2919915520 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disk identifier: 0x0008f290

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    41945087    20971520   83  Linux
/dev/sda2        41945088    46123007     2088960   82  Linux swap / Solaris
/dev/sda3        46123008    88066047    20971520   83  Linux
/dev/sda4        88066048  2919910139  1415922046   8e  Linux LVM
```
From the above, the sda1 ends at 41945087 * 512 bytes, so the copy size is 20,481 MB.
The count parameter can be ignored in case of full disk copy.

> **Note:**
> Manual export with commands poses a large risk. For example, the file system's metadata may be corrupted when io is busy. It is recommended to check that the image is intact and correct after it is exported.

## 5. Converting Image Format
The image formats supported by Tencent Cloud Service Migration include qcow2, vpc, vmdk, and raw. It is recommended to use a compressed image format to reduce the time for transmission and migration.
> The image exported using dd is in raw format, which should be converted to qcow2 or vhd.

Convert the image format using the qemu-img command:
```
sudo qemu-img convert -f raw -O qcow2 test.img test.qcow2
```
- `-f` is the source image file format.
- `-O` is the destination image file format.
For parameters, please see [Exporting Images with Commands](#-o)

## 6. Checking Image
As mentioned above, an error may be occurred with the image file system if it is created when the server is not shut down or due to other reasons. Therefore, you are recommended to check whether the created image is error-free.

When the image format is consistent with the format supported by the current platform, you can directly open the image to check the file system.
For example, vhd images can be directly added to Windows platform, qcow2 images can be opened using qemu-nbd on Linux platform, and vhd images can be enabled directly on Xen platform.
Take the Linux platform as an example:
```
modprobe nbd
qemu-nbd -c /dev/nbd0 xxxx.qcow2
mount /dev/nbd0p1 /mnt
```
If the file system is corrupted when the first partition of the qcow2 image is exported, an error will occur when using the mount command.

In addition, you can start the CVM to check whether the image file works before uploading the image.

