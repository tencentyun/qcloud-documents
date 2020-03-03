LVM（Logical Volume Manager，逻辑卷管理）通过在硬盘和分区之上建立一个逻辑层，可以将磁盘或分区划分为相同大小的PE（Physical Extents）单元，不同的磁盘或分区可以划归到同一个卷组（VG，Volume Group），在VG上可以创建逻辑卷（LV，Logical Volume），在LV上可以创建文件系统。可以简单的把卷组与磁盘，逻辑卷与分区的概念对应起来。但是相对于直接使用磁盘分区的方式，LVM的重点在于弹性调整文件系统的容量：

- 文件系统不再受限于物理磁盘的大小，可以分布在多个磁盘上：比如您可以购买3个4TB的弹性云盘并使用LVM创建一个将近12TB的超大文件系统
- 可以动态调整逻辑卷大小，不需要重新对磁盘重新分区：当LVM卷组的空间无法满足您的需求时，您可以单独购买弹性云盘并将其挂载在相应的云主机上，然后参考下边的指引将其添加到LVM卷组中进行扩容操作
....

下面介绍如何使用三块腾讯云弹性云硬盘通过LVM创建可以动态调整大小的文件系统。

![](//mccdn.qcloud.com/static/img/a22b0e07c2430684faedc44a9bf3f2c2/image.png)

## 创建物理卷（PV）
执行以下命令创建一个物理卷：

```
pvcreate 磁盘路径1 ... 磁盘路径N
```

![](//mccdn.qcloud.com/static/img/6bda1d27a97c2bc4a2f6ecc12d5ce407/image.png)

执行 `pvscan` 、 `lvmdiskscan` 、 `pvs` 、 `pvdisplay 物理卷路径`等命令查看现在系统中的物理卷：

![](//mccdn.qcloud.com/static/img/89b9329aee52edbd46098da4d8eba8c8/image.png)

## 创建卷组（VG）
执行以下命令创建卷组：

```
vgcreate [-s 指定PE大小] 卷组名 物理卷路径
```
![](//mccdn.qcloud.com/static/img/b6bef868d56920544969fb3de29278a9/image.png)

创建完成后可以使用`vgextend 卷组名 新物理卷路径`来向卷组中添加新的物理卷：
![](//mccdn.qcloud.com/static/img/5a6e292aa42c06da83faeafb64ff4634/image.png)

使用`vgs`、`vgdisplay`等命令查看当前系统中的卷组：
![](//mccdn.qcloud.com/static/img/a5939970bb877134961aa57cac492082/image.png)

## 创建逻辑卷（LV）
创建出大卷组后，接下来可以开始建立分割区（LV）了，执行以下命令创建逻辑卷：

```
lvcreate [-L 逻辑卷大小][ -n 逻辑卷名称] VG名称
```
![](//mccdn.qcloud.com/static/img/6a333909caf1197979f433b5144725ea/image.png)
这里创建了一个8G的名为“lv_0”的逻辑卷。

此时使用`pvs`命令可以发现只有vdc的PE被使用了：
![](//mccdn.qcloud.com/static/img/0de6857e273bf94736e601d691aff855/image.png)

## 创建文件系统
执行以下命令在创建好的逻辑卷上创建文件系统：

```
mkfs
```

![](//mccdn.qcloud.com/static/img/910be0713d9e6a216d5a114ab6cae5d4/image.png)

使用`mount`命令挂载该文件系统：
![](//mccdn.qcloud.com/static/img/72f94b557077a76cbbf6dffe95bbc994/image.png)

## 动态扩展逻辑卷及文件系统大小
当VG容量有剩余时，LV容量可动态扩展。执行以下命令扩展逻辑卷大小：

```
lvextend [-L +/- 增减容量] 逻辑卷路径
```

![](//mccdn.qcloud.com/static/img/a56f7ab937831f3bef2ba68962a543fc/image.png)
这里对名为“lv_0”的逻辑卷扩展了4G大小的空间。

此时使用`pvs`命令可以发现vdc已被完全使用，vdd被使用了2G空间：
![](//mccdn.qcloud.com/static/img/59a3c0ce8fa6c004144eb2c8ea8d12cc/image.png)

此时只是扩展的逻辑卷的大小，在其之上的文件系统也要随之进行扩展才能使用，这里使用`resize2fs`来扩展文件系统大小：

![](//mccdn.qcloud.com/static/img/3b39782a7826c8c262f1500d083682ce/image.png)
此时使用`df`命令可以看到lv_0的大小已被修改为12G了。
