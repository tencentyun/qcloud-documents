新购买的Linux云服务器，数据盘未做分区和格式化，无法使用。
>注：

> <font color="red">格式化后，数据盘中的数据将被全部清空。请在格式化之前，确保数据盘中没有数据或对重要数据已进行备份。为避免服务发生异常，格式化前请确保云服务器已停止对外服务。</font>

## 1. 查看磁盘列表
使用以下命令，查看磁盘设备列表：
```
fdisk –l
```

对于FreeBSD系统，请使用以下命令：

```
diskinfo -v /dev/vtbd1
```
![](//mccdn.qcloud.com/img56a6086d43aa3.png)
![](//mccdn.qcloud.com/img56a616a9911da.png)

## 2. 创建GPT分区
使用parted工具，创建GPT分区。
![](//mccdn.qcloud.com/img56a608a4b9d93.png)

对于FreeBSD系统，请按以下步骤进行：
执行命令`gpart create -s gpt vtbd1`
![](//mccdn.qcloud.com/img56a6171206c80.png)

执行命令`gpart add -t freebsd-ufs -a 1M vtbd1`
![](//mccdn.qcloud.com/img56a6172bb39c0.png)

## 3. 查看新分区信息
分区创建完成后，可以使用以下命令查看到新分区信息：
```
fdisk –l
```
![](//mccdn.qcloud.com/img56a608e6c6545.png)

## 4. 格式化分区
使用mkfs工具格式化分区。
![](//mccdn.qcloud.com/img56a609267ccb7.png)


对于FreeBSD系统，使用newfs工具格式化分区。输入以下命令：

```
newfs -j /dev/vtbd1p1
```

## 5. 挂载新分区
格式化完成后，使用以下命令挂载新分区
```
mount 文件系统 分区路径 挂载点
```
此时使用以下命令可以查看到磁盘剩余容量
```
df –h
```
![](//mccdn.qcloud.com/img56a60985596aa.png)
![](//mccdn.qcloud.com/img56a617f21cae1.png)

## 6. 设置自动挂载
修改fstab文件，设置系统重启时自动挂载新分区，如图，加入最后一行内容。
![](//mccdn.qcloud.com/img56a609b19718b.png)

对于FreeBSD系统，修改/etc/fstab文件，设置系统重启时自动挂载新分区。如图，加入最后一行内容。
![](//mccdn.qcloud.com/img56a6188004bac.png)