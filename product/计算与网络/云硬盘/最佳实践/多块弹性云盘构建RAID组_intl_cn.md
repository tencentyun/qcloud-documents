RAID（独立磁盘冗余阵列，Redundant Array of Independent Disks）可以将多个磁盘组合起来，构成一个磁盘阵列组，以提高数据的读写性能和可靠性。同时操作系统只会将磁盘阵列组当作一个硬盘来使用。目前RAID有多种等级，以下将介绍RAID0、RAID1、RAID01和RAID10。根据选择版本不同，磁盘阵列组相较于一块容量相当的大硬盘有增强数据集成度、增强容错功能、增加处理量或容量等优势。

以下是不同RAID版本的对比信息：
<table>
<tbody>
<tr><th>RAID等级</th><th>RAID0</th><th>RAID1</th><th>RAID01</th><th>RAID10</th>
<tr><td>特点</td><td>数据分段存放在不同的磁盘中。虚拟盘大小为阵列中盘容量之和</td><td>数据被镜像存储在多个磁盘中。虚拟盘大小为阵列中容量最小的盘的容量</td><td>对数据先做RAID0，后做RAID1</td><td>对数据先做RAID1，后做RAID0</td>
<tr><td>优点</td><td>读写都可以并行进行，因此理论的读写速率可以达到单个磁盘的N倍（N为组成RAID0的磁盘个数），但实际上受限于文件大小、文件系统大小等多种因素</td><td>单个磁盘的损坏不会导致数据的不可修复，读取速度快</td><td colspan="2">兼顾RAID0和RAID1的优势</td>
<tr><td>缺点</td><td>没有数据冗余，单个磁盘损坏时，在最严重的情况下将有可能导致所有数据的丢失</td><td>磁盘利用率最低，写入速度受限于单个磁盘的写入速度</td><td colspan="2">成本相对较高，需要使用至少4块盘</td>
<tr><td>建议使用场景</td><td>对I/O性能要求很高，并且已通过其他方式对数据进行了备份处理或者不需要进行数据备份的情况</td><td>对读性能要求较高，并且需要对写入的数据进行备份处理</td><td colspan="2">推荐使用RAID10，因为如果发生单一磁盘的损坏，RAID01会导致同组的磁盘都不可用</td>
</tbody>
</table>

下面介绍如何使用4块腾讯云弹性云盘来构建RAID0阵列。Linux内核提供了md模块在底层管理RAID设备，我们可以使用mdadm工具来调用md模块。

![](//mccdn.qcloud.com/static/img/9f42e96976ee6f3655090a4208f461c5/image.png)
>注：请及时对将要到期的弹性云盘进行续费操作，以避免由于弹性云盘到期导致被系统强制隔离对RAID阵列产生影响。

## 安装mdadm（以CentOS为例）
![](//mccdn.qcloud.com/static/img/59896b0ee3f20cd0f20f2f3633e56a1f/image.png)

## 使用mdadm创建RAID0
![](//mccdn.qcloud.com/static/img/8d180220850c396dcf91266b43f2220d/image.png)

>注：创建RAID1、RAID01、RAID10时最好使用相同大小的分区创建RAID，以避免对磁盘空间的浪费。

## 使用mkfs创建文件系统
![](//mccdn.qcloud.com/static/img/e92608f31d914556a585e3190a009a64/image.png)

## 挂载文件系统
![](//mccdn.qcloud.com/static/img/a4c36941609c64a3753648622392de65/image.png)

## 修改mdadm配置文件
确定文件系统UUID：
![](//mccdn.qcloud.com/static/img/e42b1f74126420929cd3b3668cca3f21/image.png)

执行以下命令修改mdadm配置文件：

```
vi /etc/mdadm.conf
```

对于弹性云硬盘，建议写入以下配置：

```
DEVICE /dev/disk/by-id/virtio-弹性云盘1ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘2ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘3ID-part1 
DEVICE /dev/disk/by-id/virtio-弹性云盘4ID-part1 
ARRAY 逻辑设备路径 metadata= UUID=
```
本例为：ARRAY /dev/md0 metadata=1.2 UUID=3c2adec2:14cf1fa7:999c29c5:7d739349

