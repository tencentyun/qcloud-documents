云硬盘是云上可扩展的存储设备，用户可以在创建云硬盘后随时扩展其大小，以增加存储空间，同时不失去云硬盘上原有的数据。要达到扩容并使用扩容空间的目的，用户在 [扩容实体云硬盘](/doc/product/362/5747) 大小之后，还需要扩展其上的文件系统以识别新近可用的空间。您可以根据下面的步骤进行：
1. [扩容实体云硬盘大小](/doc/product/362/5747)
2. 扩容分区
 - 确定文件系统分区表形式
 - 扩容分区
3. 扩容文件系统

## 检查文件系统大小
在执行扩容实体云硬盘大小操作后，用户可以通过检查文件系统大小来查看实例是否识别了更大的云硬盘空间。在 Linux 上，可以使用 `df -h` 命令检查文件系统大小。

如果没有看到云硬盘大小变成扩容后的值，则需要扩容此文件系统，以便实例可以使用新的空间。

## 确认分区表形式
执行以下命令，确认云硬盘在扩容前使用的分区表形式。
```
fdisk -l
```
- 若结果如下两图所示（根据操作系统不同略有不同），则说明云服务器扩容前为 GPT 分区方式，后续操作请参见《GPT 分区云硬盘扩容后修改分区指南》。
![](//mccdn.qcloud.com/static/img/972969e3db92b65311211734690fe763/image.png)
![](//mccdn.qcloud.com/static/img/2c1f4a40279d211a7b81bada7ed38280/image.png)
- 若结果如下图所示（根据操作系统不同略有不同），则说明云服务器扩容前为 MBR 分区方式，后续操作请参见《MBR 分区云硬盘扩容后修改分区指南》。
![](//mccdn.qcloud.com/static/img/4d789ec2865a2895305f47f0513d4e2b/image.png)

## GPT 分区云硬盘扩容后修改分区指引
### 新空间格式化成一个独立 GPT 分区
#### 查看数据盘信息
执行以下命令， 确认云硬盘的容量变化。
```
parted 磁盘路径 print
```
若在过程中收到如下提示，请输入 `Fix`。
![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
如下图所示，扩容后的云硬盘大小为107GB，已有分区的大小为10.7GB。
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)

#### 卸载已挂载数据盘
1. 执行以下命令，确认该云硬盘是否还有分区已挂载。
```
mount | grep '磁盘路径' 
```
如下图所示，云硬盘上有一个分区（vdb1）挂载在 /data 上，需要将其解挂。
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
2. 执行以下命令，解挂数据盘。
```
umount 挂载点
```
本例中即执行 `umount /data` 进行卸载。
>? 须将云硬盘上所有分区的文件系统都解挂，例如 vdb1、vdb2等。
3. 卸载完成后，重复执行步骤1，确认此硬盘上所有分区的文件系统都已解挂。
例如执行以下命令，确认 `/dev/vdb` 硬盘路径下所有分区的文件系统都已解挂。
```
mount | grep '/dev/vdb'
```
![](//mccdn.qcloud.com/static/img/a2f6db45a94485785ea15e6ea950bcb8/image.png)

#### 数据盘分区 
1. 确认云硬盘所有分区均已卸载后，执行以下命令，新建一个分区。
```
parted 磁盘路径
```
例如磁盘路径为 `parted /dev/vdb`。
2. 执行 `print` 命令，查看分区信息。
3. 记住已有分区的 End 值，以此值作为下一个分区的起始偏移值。
![](//mccdn.qcloud.com/static/img/788ce125bba952f204ed6ee36dfb644d/image.png)
4. 执行以下命令，新建一个主分区。此分区将从已有分区的末尾开始，覆盖硬盘所有的新增空间。
```
mkpart primary start end
```
本例使用`mkpart primary 10.7GB 100% `
5. 执行 `print` 命令，即可发现新分区已经新建成功。
![](//mccdn.qcloud.com/static/img/fc54fd4c05102ee91c648526d77d1b42/image.png)
6. 键入 `quit` 即可退出 parted 工具。

#### 格式化新建分区
执行以下命令，格式化上述新建的分区。用户可以自行决定文件系统的格式，例如 ext2、ext3等。
```
mkfs.[fstype] [分区路径] 
```
例如，执行以下命令，对新分区进行格式化，文件系统为 EXT3。 
```
mkfs.ext3 /dev/vdb2
```

### 新空间增加到已有分区中（GPT 分区格式）
#### 查看数据盘信息
执行以下命令，确认云硬盘的容量变化。
```
parted 磁盘路径 print
```
若在过程中收到如下提示，请输入`Fix`。
![](//mccdn.qcloud.com/static/img/cf51cda9a12085f76949ab0d5dd0fbfc/image.png)
如下图所示，扩容后的云硬盘大小为107GB，已有分区的大小为10.7GB。
![](//mccdn.qcloud.com/static/img/01a0a7a8fdfe6f05f2739f0326a74ef9/image.png)

#### 卸载已挂载数据盘
1. 执行以下命令，确认该云硬盘是否还有分区已挂载。
```
mount | grep '磁盘路径' 
```
如下图所示，云硬盘上有一个分区（vdb1）挂载在 /data 上，需要将其解挂。
![](//mccdn.qcloud.com/static/img/edc5bbd6834e1dd929ce0eb00acd53ca/image.png)
2. 执行以下命令，解挂数据盘。
```
umount 挂载点
```
本例中即执行`umount /data`进行卸载。
>? 要将云硬盘上所有分区的文件系统都解挂，例如 vdb1、vdb2等。
3. 重复执行 `mount | grep '/dev/vdb' `命令，确认此硬盘上所有分区的文件系统都已解挂。
![](//mccdn.qcloud.com/static/img/a2f6db45a94485785ea15e6ea950bcb8/image.png)

#### 数据盘分区 
1. 确认云硬盘所有分区均已卸载后，执行以下命令，将原分区删除并以同样的起始偏移新建一个分区。
```
parted [磁盘路径]
```
2. 执行以下命令，将显示和操纵单位变成 sector（默认为GB）。
```
unit s
```
3. 输入 `print`，查看分区信息，并记住已有分区的 Start 值。
>! 删除分区并新建后，Start 值必须与这个相同，否则数据将会丢失。

 ![](//mccdn.qcloud.com/static/img/67ba54c1d9d63c307d4b8a157b70c722/image.png)
4. 执行以下命令，删除原有分区。
```
rm [分区Number]
```
例如，由上图可知云硬盘上有一个分区，Number 为“1”，执行 `rm 1` 命令，返回结果如下图。
![](//mccdn.qcloud.com/static/img/3384eeada87ce75695e0e55125109eff/image.png)
5. 执行以下命令，新建一个主分区。其中，100%表示此分区到磁盘的最末尾。
```
mkpart primary [原分区起始扇区] 100%
```
例如，主分区从第2048个扇区开始（必须与删除之前的分区一致），则执行以下命令。
```
mkpart primary 2048s 100%
```
如果出现如下图所示的状态，请输入 `Ignore`。
![](//mccdn.qcloud.com/static/img/c45966e20dc856817c65fd6b81155e4a/image.png)
6. 执行 `print` 命令，即可发现新分区已经新建成功。
![](//mccdn.qcloud.com/static/img/cb1af5adaf6c89d066077c43fd428a38/image.png)
7. 输入`quit`，即可退出 parted 工具。

#### 检查扩容后分区的文件系统
执行以下命令，检查扩容后的分区。
```
e2fsck -f 分区路径
```
例如，已新建分区1，执行 `e2fsck -f /dev/vdb1` 命令，返回结果如下所示：
![](//mccdn.qcloud.com/static/img/307f7a0c98eea05ca1d4560fe4e96f57/image.png)

#### 扩容 EXT 文件系统
执行以下命令，对新分区上 EXT 文件系统进行扩容操作。
```
resize2fs 分区路径，如/dev/vdb1
```
![](//mccdn.qcloud.com/static/img/57d66da9b5020324703498dbef0b12f9/image.png)

#### 扩容 XFS 文件系统
执行以下命令，对新分区上 XFS 文件系统进行扩容操作。
```
xfs_growfs 分区路径，如/dev/vdb1
```

#### 挂载新分区
执行以下命令，挂载分区。
```
mount 分区路径 挂载点
```
例如，执行 `mount /dev/vdb1 /data` 命令，手动挂载新分区，并执行 `df -h` 命令查看新分区，出现以下信息说明挂载成功，即可以查看到数据盘。
![](//mccdn.qcloud.com/static/img/a2bd04c79e8383745689e19033a0daaa/image.png)

## MBR 分区云硬盘扩容后修改分区指引
MBR 分区的云硬盘进行扩容后，您可以选择：
- 将新增的容量空间建立成独立的新分区，同时原有分区保持不变。
- 扩容原有分区至新增的容量空间（包括未分区直接格式化的场景），并且保持原有分区的数据不丢失。

在您的 Linux 云服务器的云硬盘升级成功之后，以上两种场景都可以通过 Linux 下的分区扩容工具（fdisk/e2fsck/resize2fs）执行一系列命令，完成分区扩容，并且保证原数据不会丢失。
>! 
> - 为了内核可以识别出新的分区表，不管是添加新分区，还是扩容到已有分区，都需要先将此磁盘的所有已挂载分区 umount，再执行扩容操作。
> - 由于 MBR 的限制，选择任何一种方式时，请保持任意分区的大小不超过2TB（若您扩容后的空间已经大于2TB则不可选择第二种方式。

### 新空间格式化成一个独立分区
#### 查看数据盘信息
1. 执行以下命令，查看已挂载的数据盘分区信息。
```
df -h
```
![](//mccdn.qcloud.com/static/img/0a450dfaa9cfc7b2c7fdc04861f0e754/image.png)
2. 执行以下命令，查看数据盘扩容后未分区的信息。
```
fdisk -l
```
![](//mccdn.qcloud.com/static/img/594671a1215dee3036b7940892438f62/image.png)

#### 卸载所有已挂载的分区
执行以下命令，卸载所有已挂载的分区。
```
umount 挂载点
```
例如，执行 `umount /data` 命令，卸载所有已挂载分区。

#### 数据盘分区
确认云硬盘所有分区均已卸载后，执行以下命令，新建一个新分区。
```
fdisk [硬盘路径]
```
例如，执行 `fdisk /dev/xvdc` 命令，并按照界面的提示，依次输入”p”（查看现有分区信息）、“n”（新建分区）、“p”（新建主分区）、“2”（新建第2个主分区），两次回车（使用默认配置），输入 “w”（保存分区表），开始分区。如下图所示：
![](//mccdn.qcloud.com/static/img/8c35d6f4dfb367e74edc27ce6822c317/image.png)
>? 以创建1个分区为例，您也可以根据实际需求创建多个分区。

#### 查看新分区
执行以下命令，查看新分区。
```
fdisk -l
```
如下图所示，新的分区 xvdc2 已经创建完成。
![](//mccdn.qcloud.com/static/img/e04e924d62317bc2c605c8abaac394f5/image.png)


#### 格式化新分区并创建文件系统
在进行分区格式化时，用户可以自行决定文件系统的格式，例如 ext2、ext3等。
以 “ext3” 为例，执行以下命令， 对新分区进行格式化。 
```
mkfs.ext3 /dev/xvdc2
```
![](//mccdn.qcloud.com/static/img/074e23eaa580495f96fb532b688d2d68/image.png)

#### 挂载新分区
执行以下命令，创建新的挂载点。
```
mkdir 新挂载点
```
并执行以下命令挂载新分区到新挂载点上：
```
mount 新分区路径 新挂载点
```
例如，执行 `mkdir /data1` 命令，创建 data1 目录，并在执行 `mount /dev/xvdc2 /data1` 命令手动挂载新分区后，执行 `df -h` 命令查看新分区信息。出现以下信息说明挂载成功，即可以查看到数据盘。
![](//mccdn.qcloud.com/static/img/7b749a4bb6e7c8267c9354e1590c35d4/image.png)

#### 添加新分区信息
如果您希望云服务器在重启或开机时，能自动挂载数据盘，必须将分区信息添加到 /etc/fstab 中。如果没有添加，则云服务器重启或开机后都不能自动挂载数据盘。
1. 执行以下命令，添加信息。
```
echo '/dev/xvdc2 /data1 ext3 defaults 0 0' >> /etc/fstab
```
2. 执行以下命令，查看信息。若出现以下信息，则表示添加分区信息成功。
```
cat /etc/fstab
```
![](//mccdn.qcloud.com/static/img/f0b5c14bf08fd3629ddf6d9b1ae01ffc/image.png)

### 将新空间增加到已有分区空间中
若原有的硬盘分区为一个 MBR 分区(可以看到 vdb1、vdc1 等字样)，同时在此分区上制作了文件系统。或原有的硬盘没有分区，直接在此硬盘上制作了文件系统。这两种情况都可以选择使用自动扩容工具进行扩容。

自动扩容工具适用于 Linux 操作系统，用于将扩容时新扩的云硬盘存储空间添加到已存在的文件系统中，扩容能够成功必须满足下面4个条件：
- 文件系统是 EXT2/EXT3/EXT4/XFS
- 当前文件系统不能有错误
- 扩容后的磁盘大小不超过2TB
- 当前工具仅支持 Python 2 版本，不支持 Python 3 版本

下面介绍自动扩容工具的使用方法。

#### 卸载正在使用的硬盘分区
执行以下命令，卸载分区。
```
umount 挂载点
```
![](//mccdn.qcloud.com/static/img/c0acc05057941681627a5fd34979d194/image.jpg)

#### 下载一键扩容工具
执行以下命令，下载工具。
```
wget -O /tmp/devresize.py https://raw.githubusercontent.com/tencentyun/tencentcloud-cbs-tools/master/devresize/devresize.py
```

#### 执行扩容工具
执行以下命令，扩容工具。
```
python /tmp/devresize.py 硬盘路径
```
>! 硬盘路径指的是需要扩容的云硬盘，不是分区名。

例如，您的文件系统在 vdb1 上，则应执行以下命令。 如下图所示：
```
python /tmp/devresize.py  /dev/vdb
```
![](//mccdn.qcloud.com/static/img/c7617b90578192d64d19f02325f00ffb/image.jpg)
- 若输出 “The filesystem on /dev/vdb1 is now XXXXX blocks long.“ 则表示扩容成功。
- 若输出的是 “[ERROR] - e2fsck failed!!“，请使用 `fsck` 命令对文件系统所在分区进行修复，自动修复的命令格式如下：
```
fsck -a 分区路径
```
>! 这里与前一个命令不同，需要填写的是文件系统所在分区。

 例如，您的文件系统在 vdb1 上，则应执行以下命令。
```
fsck -a /dev/vdb1
```
修复成功后，再执行 `python /tmp/devresize.py 硬盘路径`命令来使用扩容工具进行扩容。


#### 重新挂载扩容后的分区
1. 执行以下命令，挂载扩容后的分区。
```
mount 分区路径 挂载点
```
例如，执行以下命令，手动挂载扩容后的分区。
```
mount /dev/vdb1 /data
```
如果原先没有分区，则执行以下命令。
```
mount /dev/vdb /data`
```
2. 执行以下命令，查看扩容后的分区容量。若返回类似如下图所示的信息，说明挂载成功，即可以查看到数据盘：
```
df -h
```
![](//mccdn.qcloud.com/static/img/2367f3e70cd0c3c1bef665cc47c1c3bc/image.jpg)
5. 执行以下命令，则可以查看扩容后原分区的数据没有丢失，新增加的存储空间已经扩容到文件系统中。
```
ll /data
```
