## LVM 简介
逻辑卷管理（Logical Volume Manager，LVM）通过在硬盘和分区之上建立一个逻辑层，将磁盘或分区划分为相同大小的 PE（Physical Extents）单元，不同的磁盘或分区可以划归到同一个卷组（VG，Volume Group），在 VG 上可以创建逻辑卷（LV，Logical Volume），在 LV 上可以创建文件系统。
相较于直接使用磁盘分区的方式，LVM 的优势在于弹性调整文件系统的容量：
- 文件系统不再受限于物理磁盘的大小，可以分布在多个磁盘中。
例如，您可以购买3块4TB的弹性云硬盘并使用 LVM 创建一个将近12TB的超大文件系统。
- 可以动态调整逻辑卷大小，不需要对磁盘重新分区。
当 LVM 卷组的空间无法满足您的需求时，您可以单独购买弹性云硬盘并挂载到相应的云服务器上，然后将其添加到 LVM 卷组中进行扩容操作。

## 构建 LVM
>?本文以使用3块弹性云硬盘通过 LVM 创建可动态调整大小的文件系统为例。如下图所示：
![](https://main.qcloudimg.com/raw/81086e80477ff7e374e7c3f0fe9d2788.png)

### 步骤 1  创建物理卷 PV
1. 以 root 用户 [登录 Linux 云服务器](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，创建一个 物理卷（Physical Volume， PV）。
```plaintext
pvcreate <磁盘路径1> ... <磁盘路径N>
``` 本文以 `/dev/vdc`、`/dev/vdd` 和 `/dev/vde` 为例，则执行：
```plaintext
pvcreate /dev/vdc /dev/vdd /dev/vde
``` 创建成功则如下图所示：
![](https://main.qcloudimg.com/raw/5b92a6c7878e22906599af48bfa09d95.png)
3. 执行以下命令，查看现在系统中的物理卷。
```plaintext
lvmdiskscan | grep LVM
``` ![](https://main.qcloudimg.com/raw/1de75af4a49c2deea689a2576eb075d9.png)

### 步骤 2 创建卷组 VG
1. 执行以下命令，创建 VG。
```plaintext
vgcreate [-s <指定PE大小>] <卷组名> <物理卷路径>
``` 本文以创建一个名为 “lvm_demo0” 的卷组为例，则执行：
```plaintext
vgcreate lvm_demo0 /dev/vdc /dev/vdd
``` 创建成功则如下图所示：
![](https://main.qcloudimg.com/raw/3b8dba3329f62e85d2075fad10898632.png)
 当提示 “Volume group “<卷组名>” successfully created” 时，表示卷组创建成功。
 - 卷组创建完成后，可执行以下命令，向卷组中添加新的物理卷。
```plaintext
vgextend 卷组名 新物理卷路径
``` 添加成功则如下图所示：
![](https://main.qcloudimg.com/raw/105e5a77472f173ffd4a58624f20a863.png)
 - 卷组创建完成后，可执行`vgs`、`vgdisplay`等命令查看当前系统中的卷组信息。如下图所示：
![](https://main.qcloudimg.com/raw/309c991d32cf4b801ddbe8d898f1bfbb.png)

### 步骤 3 创建逻辑卷 LV
1. 执行以下命令，创建 LV。
```plaintext
lvcreate [-L <逻辑卷大小>][ -n <逻辑卷名称>] <VG名称>
``` 本文以创建一个8GB的名为 “lv_0” 的逻辑卷为例，则执行：
```plaintext
lvcreate -L 8G -n lv_0 lvm_demo0
``` 创建成功则如下图所示：
![](https://main.qcloudimg.com/raw/ed6d2f827ae7c4a4630bf17e24d90df2.png)
>?执行 `pvs` 命令，可查看到此时只有 `/dev/vdc` 被使用了8GB。如下图所示：
>![](https://main.qcloudimg.com/raw/2718d08f7c74b7b469a23473a1398dfe.png)

### 步骤 4 创建并挂载文件系统
1. 执行以下命令，在创建好的逻辑卷上创建文件系统。
```plaintext
mkfs.ext3 /dev/lvm_demo0/lv_0
```
2. 执行以下命令，创建挂载节点目录 `/vg0`。
```plaintext
mkdir /vg0
```
2. 执行以下命令，挂载文件系统。
```plaintext
mount /dev/lvm_demo0/lv_0 /vg0
``` 挂载成功则如下图所示：
![](https://main.qcloudimg.com/raw/34af8440192a1fa74f85ea44b6354194.png)

### 步骤 5 动态扩展逻辑卷及文件系统大小
>!仅当 VG 容量有剩余时，LV 容量可动态扩展。扩展 LV 容量后，需一并扩展创建在该 LV 上的文件系统的大小。
>
1. 执行以下命令，扩展逻辑卷大小。
```plaintext
lvextend [-L +/- <增减容量>] <逻辑卷路径>
``` 本文以向逻辑卷 “lv_0” 扩展4GB容量为例，则执行：
```plaintext
lvextend -L +4G /dev/lvm_demo0/lv_0
``` 扩展成功则如下图所示：
![](https://main.qcloudimg.com/raw/eccd7d6aec587eb90ec655a384367595.png)
>?执行 `pvs` 命令，可查看到此时 `/dev/vdc` 已被完全使用，`/dev/vdd` 被使用了2GB。如下图所示：
>![](https://main.qcloudimg.com/raw/189155ca377ef9550c4587ca78ab5b27.png)
2. 执行以下命令，扩展文件系统。
```plaintext
resize2fs /dev/lvm_demo0/lv_0
``` 扩展成功则如下图所示：
![](https://main.qcloudimg.com/raw/2e37f35678014ab1ca398fe5470a754b.png)
扩展成功后，可执行以下命令，查看逻辑卷的容量是否变为12GB。
```plaintext
df -h
```




