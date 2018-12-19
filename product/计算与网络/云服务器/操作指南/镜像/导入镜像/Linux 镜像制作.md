## 一. 准备工作
制作系统盘镜像导出时需要做以下检查，数据盘镜像导出可以忽略。

- 检查 OS 分区，目前服务迁移不支持 GPT 分区。
```
sudo parted -l /dev/sda | grep 'Partition Table'
```
msdos 表示 MBR 分区；gpt 表示 GPT 分区。

- 检查启动方式，目前服务迁移不支持 EFI 启动。
```
sudo ls /sys/firmware/efi
```
若文件存在，则目前系统是以 EFI 方式启动，需要确认 grub 中有传统方式的启动项。

- 检查网络配置，目前服务迁移不支持 IPv6，不支持多网卡。依赖于 IPv6 和多网卡的服务都无法正常工作。

- 检查系统关键文件，包括且不限于以下系统文件：
> 请遵循相关发行版的标准，确保系统关键文件位置和权限正确无误，可以正常读写。

 - /etc/grub/grub.cfg： kernel 参数里推荐使用 uuid 挂载 root，其它方式（如 root=/dev/sda）可能导致系统无法启动；
 - /etc/fstab：请勿挂载其它硬盘，迁移后可能会由于磁盘缺失导致系统无法启动；
 - /etc/shadow：权限正常，可以读写。

- 卸载会产生冲突的驱动和软件（包括 VMware tools，Xen tools，Virtualbox GuestAdditions 以及一些自带底层驱动的软件）。

- 检查 virtio 驱动：请参考 [Linux 系统检查 virtio 驱动](https://cloud.tencent.com/document/product/213/9929)。

- 安装 cloud-init：请参考 [cloud-init 安装文档](https://cloud.tencent.com/document/product/213/12587)。

- 检查其它硬件相关的配置，如 Linux 桌面环境中的驱动设置。上云之后的硬件变化包括但可能不限于：
 - 显卡更换为 cirrus vga；
 - 磁盘更换为 virtio disk，设备名为 vda、vdb；
 - 网卡更换为 virtio nic，默认只提供 eth0。

## 二. 查找分区和大小
使用 mount 命令确认目前的分区格式，判断要复制的分区及大小。
示例：
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
从示例中可以看出根分区是在`/dev/sda1`，boot 和 home 没有独立分区。可以复制整个 sda，或者复制到 sda1 结束位置。

导出的镜像中至少应该要包含根分区以及 mbr。如果`/boot`和`/home`独立分区的话，也需要包含这两个独立分区。
> **注意：**
> 复制时要包含 mbr，否则无法会启动，如上述示例，虽然 sda1 里也包含 boot 分区，但由于缺少 mbr 是无法启动的，必须要复制sda。


## 三. 使用工具导出
使用 VMWare vCenter Convert 或 Citrix XenConvert 等虚拟化平台的导出镜像工具，详情请见各平台的导出工具文档。目前腾讯云服务迁移支持的镜像格式有：qcow2，vhd，raw，vmdk。

## 四. 使用命令导出镜像
### 使用 qemu-img 命令
示例：
```
sudo qemu-img convert -f raw -O qcow2 /dev/sda /mnt/sdb/test.qcow2
```
这个命令是将`/dev/sda`整个盘导出到`/mnt/sdb/test.qcow2`。`/mnt/sdb`这里应该挂载另外一块磁盘，或者是其它网络存储。
如果要转换成其它参数，需要修改`-O`参数，可选的参数有：
<a id="-o"></a>

值 | 含义
---|---
qcow2 | qcow2 格式
vpc | vhd 格式
vmdk | vmdk 格式
raw | 无格式

### 使用 dd 命令
示例：
```
sudo dd if=/dev/sda of=/mnt/sdb/test.imag bs=1K count=$count
```
dd 导出的镜像为 raw 格式，需要再做一次转换。count 参数决定了要复制的数量，这个数量可以用 fdisk 命令查出：
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
可以看出 sda1 结束位置在 41945087 * 512 字节处，所以复制 20481M 即可。
如果是全盘复制的话，count 参数可以忽略。

> **注意：**
> 使用命令手工导出的风险比较大，例如在 io 繁忙时可能造成文件系统的 metadata 错乱等。建议在导出镜像后，检查镜像完整无误。

## 五. 镜像格式转换
目前腾讯云的服务迁移支持的镜像格式有：qcow2，vpc，vmdk，raw。建议使用压缩的镜像格式，可以节省传输和迁移的时间。
> dd 导出的镜像为 raw 格式，建议转换为 qcow2 或 vhd。

使用 qemu-img 命令转换镜像格式：
```
sudo qemu-img convert -f raw -O qcow2 test.img test.qcow2
```
- `-f`为源端镜像文件格式；
- `-O` 为目的端镜像文件格式。
参数见 [第四节](#-o)。

## 六. 镜像检查
如上所述，当不停服制作镜像或者其它原因，可能导致制作出的镜像文件系统有误，因此建议在制作镜像后检查是否无误。

当镜像格式和当前平台支持的格式一致时，可以直接打开镜像检查文件系统。
例如 Windows 平台可以直接附加 vhd 格式镜像，Linux 可以使用 qemu-nbd 打开 qcow2 格式镜像，Xen 平台可以直接启用 vhd 文件。
以 Linux 平台为例：
```
modprobe nbd
qemu-nbd -c /dev/nbd0 xxxx.qcow2
mount /dev/nbd0p1 /mnt
```
如果 qcow2 镜像的第一个分区导出时文件系统被破坏，mount 时将会报错。

此外还可以在上传镜像前，先启动虚拟机测试镜像文件是否可以使用。
