## 操作场景
本文介绍如何在云服务器内部扩容文件系统，此方式适用于未在云硬盘上创建分区，直接创建文件系统的场景。

## 操作步骤
1. 执行以下命令，确认云硬盘的文件系统类型。
```
df -ihT
```
 - 返回结果如下图所示，则文件系统类型为 EXT。
![](https://main.qcloudimg.com/raw/198ad9bcb209db6ed1934e02f3234f8b.png)
 - 返回结果如下图所示，则文件系统类型为 XFS。
![](https://main.qcloudimg.com/raw/50ecea03c960daa2d04b734226ad69a0.png)
2. 根据云硬盘文件系统的类型，执行不同的命令进行扩容。
>?EXT 文件系统具备以下容量限制：
> - EXT3 文件系统最大支持16TB，单个文件2TB。
> - EXT4 文件系统最大支持1EB，单个文件16TB。
>
 - 执行以下命令扩容 EXT 文件系统（以 `/dev/vdb` 为例）。
```
resize2fs /dev/vdb
```
执行结果如下图所示，则扩容成功。
![](https://main.qcloudimg.com/raw/9f68b0ab1e6446943da4e426df92919b.png)
 - 执行以下命令扩容 XFS 文件系统（以 `/dev/vdc` 为例）。
```
xfs_growfs /dev/vdc
```
执行结果如下图所示，则扩容成功。
![](https://main.qcloudimg.com/raw/56fac50edbb153585adb67b2eb246cf4.png)
3. 执行以下命令，查看文件系统的硬盘空间情况。
```
df -h
```
