## LVM 简介
LVM 通过在硬盘和分区之上建立一个逻辑层，将磁盘或分区划分为相同大小的 PE（Physical Extents）单元，不同的磁盘或分区可以划归到同一个卷组（VG，Volume Group），在 VG 上可以创建逻辑卷（LV，Logical Volume），在 LV 上可以创建文件系统。
相较于直接使用磁盘分区的方式，LVM 的优势在于弹性调整文件系统的容量：
- 文件系统不再受限于物理磁盘的大小，可以分布在多个磁盘中。
例如，您可以购买3块4TB的弹性云硬盘并使用 LVM 创建一个将近12TB的超大文件系统。
- 可以动态调整逻辑卷大小，不需要重新对磁盘重新分区。
当 LVM 卷组的空间无法满足您的需求时，您可以单独购买弹性云硬盘并挂载到相应的云服务器上，然后将其添加到 LVM 卷组中进行扩容操作。

## 构建 LVM
>?本文以使用3块弹性云硬盘通过 LVM 创建可动态调整大小的文件系统为例。
![](//mccdn.qcloud.com/static/img/a22b0e07c2430684faedc44a9bf3f2c2/image.png)

### 步骤一  创建物理卷 PV
1. 以 root 用户 [登录 Linux 云服务器](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，创建一个 PV（物理卷，Physical Volume）。
```
pvcreate <磁盘路径1> ... <磁盘路径N>
```
本文以`/dev/vdc`、`/dev/vdd`和`/dev/vde`为例，则执行：
```
pvcreate /dev/vdc /dev/vdd /dev/vde
```
![](//mccdn.qcloud.com/static/img/6bda1d27a97c2bc4a2f6ecc12d5ce407/image.png)

3. 执行以下命令，查看现在系统中的物理卷。
```
lvmdiskscan | grep LVM
```
![](//mccdn.qcloud.com/static/img/89b9329aee52edbd46098da4d8eba8c8/image.png)

### 步骤二 创建卷组 VG
1. 执行以下命令，创建 VG。
```
vgcreate [-s <指定PE大小>] <卷组名> <物理卷路径>
```
本文以创建一个名为“lvm_demo0”的卷组为例，则执行：
```
vgcreate lvm_demo0 /dev/vdc /dev/vdd
```
![](//mccdn.qcloud.com/static/img/b6bef868d56920544969fb3de29278a9/image.png)
 当提示“Volume group “<卷组名>” successfully created”时，表示卷组创建成功。
 - 卷组创建完成后，可执行以下命令，向卷组中添加新的物理卷。
```
vgextend 卷组名 新物理卷路径
```
![](//mccdn.qcloud.com/static/img/5a6e292aa42c06da83faeafb64ff4634/image.png)
 - 卷组创建完成后，可执行`vgs`、`vgdisplay`等命令查看当前系统中的卷组信息。
![](//mccdn.qcloud.com/static/img/a5939970bb877134961aa57cac492082/image.png)

### 步骤三 创建逻辑卷 LV
1. 执行以下命令，创建 LV。
```
lvcreate [-L <逻辑卷大小>][ -n <逻辑卷名称>] <VG名称>
```
本文以创建一个8GB的名为“lv_0”的逻辑卷为例，则执行：
```
lvcreate -L 8G -n lv_0 lvm_demo0
```
![](//mccdn.qcloud.com/static/img/6a333909caf1197979f433b5144725ea/image.png)
>?执行`pvs`命令，可查看到此时只有`/dev/vdc`被使用了8GB。
>![](//mccdn.qcloud.com/static/img/0de6857e273bf94736e601d691aff855/image.png)

### 步骤四 创建并挂载文件系统
1. 执行以下命令，在创建好的逻辑卷上创建文件系统。
```
mkfs.ext3 /dev/lvm_demo0/lv_0
```
2. 执行以下命令，挂载文件系统。
```
mount /dev/lvm_demo0/lv_0 vg0/
```
![](//mccdn.qcloud.com/static/img/72f94b557077a76cbbf6dffe95bbc994/image.png)

### 步骤五 动态扩展逻辑卷及文件系统大小
>!仅当 VG 容量有剩余时，LV 容量可动态扩展。扩展 LV 容量后，需一并扩展创建在该 LV 上的文件系统的大小。

1. 执行以下命令，扩展逻辑卷大小。
```
lvextend [-L +/- <增减容量>] <逻辑卷路径>
```
本文以向逻辑卷“lv_0”扩展4GB容量为例，则执行：
```
lvextend -L + 4G /dev/lvm_demo0/lv_0
```
![](//mccdn.qcloud.com/static/img/a56f7ab937831f3bef2ba68962a543fc/image.png)
>?执行`pvs`命令，可查看到此时`/dev/vdc`已被完全使用，`/dev/vdd`被使用了2GB。
>![](//mccdn.qcloud.com/static/img/59a3c0ce8fa6c004144eb2c8ea8d12cc/image.png)

2. 执行以下命令，扩展文件系统。
```
resise2fs /dev/lvm_demo0/lv_0
```
![](//mccdn.qcloud.com/static/img/3b39782a7826c8c262f1500d083682ce/image.png)
扩展成功后，可执行以下命令，查看逻辑卷的容量是否变为12GB。
```
df -h
```
