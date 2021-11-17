## 操作场景
当您的云硬盘在已有 MBR 分区并已创建文件系统的情况下，已扩容至大于2TB，此时 MBR 分区下的文件系统已无法扩容至大于2TB，请参考本文将 MBR 分区形式转换为 GPT 分区形式。

## 注意事项
- 转换分区表格式需替换原有分区，适当操作不会删除原有分区的数据，但需要先卸载原有分区，会一定程度影响线上业务运行。
- 请谨慎操作，误操作可能会导致数据丢失或异常。请给对应云硬盘创建快照，完成数据备份。详情请参见 [创建快照](https://cloud.tencent.com/document/product/362/5755)。如出现误操作导致数据丢失，则可回滚快照进行数据恢复。


## 操作步骤
1. 登录云服务器，详情请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 执行以下命令，查看分区类型是否为 MBR。
```
fdisk -l
```
若结果如下图所示（根据操作系统不同略有不同），则说明为 MBR 分区形式。
![](https://qcloudimg.tencent-cloud.cn/raw/504b1b28343c7dffc09dd4f1057e35b1.png)
3. 执行以下命令，卸载分区。
```
umount <挂载点>
```
本文挂载点以 /data 为例，则执行：
```
umount /data
```
4. 执行以下命令，查看分区的卸载结果。
```
lsblk
```
若原分区 MOUNTPOINT 已显示为空，则表明卸载任务成功。本文以 `/dev/vdb1` 分区为例，返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6813b4e3ec44ec7a5735f8b424e5ee9b.png)
5. 执行以下命令，进入 parted 分区工具。
```
parted <磁盘路径>
```
本文以磁盘路径以 `/dev/vdb` 为例，则执行：
```
parted /dev/vdb
```
5. 输入 `p` 并按 **Enter**，查看当前分区信息。回显信息类似如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/f58f03bf910e52647645e9730c9f0307.png)
6. 输入 `rm 分区号` 并按 **Enter**，删除待替换的末尾分区。
本文示例中仅有1个分区，可输入 `rm 1` 并按 **Enter**，删除分区1。
7. 输入 `p` 并按 **Enter**，查看当前分区信息，观察末尾分区是否已删除。
8. 输入 `mklabel GPT` 并按 **Enter**，使用 GPT 分区形式重新划分分区。
9. 在确认提示后输入 `Yes`，按 **Enter**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b8d89b8f1fc358e2e3c357aa04b1f02c.png)
10. 输入 `mkpart primary 2048s 100%`，按 **Enter**，创建分区。
其中，`2048s` 表示硬盘初始容量，`100%` 表示磁盘截止容量，此处仅供参考，您可以根据业务需要自行规划磁盘分区数量及容量。
<dx-alert infotype="notice" title="">
以下情况可能导致数据丢失：
- 选择的初始容量与原分区不一致。
- 选择的截止容量小于扩容前的原分区容量的值。
</dx-alert> 
11. 输入 `p` 并按 **Enter**，查看新分区是否替换成功。回显信息类似如下图所示，则表示已成功替换：
![](https://qcloudimg.tencent-cloud.cn/raw/a48c842ae52e696d7ad03cca217638f3.png)
12. 输入 `q` 并按 **Enter**，退出 parted 分区工具。
12. 执行以下命令，挂载分区。
```
mount <分区路径> <挂载点>
```
本文以分区路径以 `/dev/vdb1`，挂载点 `/data` 为例，则执行：
```
mount /dev/vdb1 /data
```
13. 执行对应命令，扩容文件系统。
<dx-tabs>
::: 扩容 ext 文件系统
执行以下命令，扩容 ext 文件系统。
```
 resize2fs /dev/对应分区
```
本文以分区路径以 `/dev/vdb1`，则执行：
```
 resize2fs /dev/vdb1
```
:::
::: 扩容 xfs 文件系统
执行以下命令，扩容 xfs 文件系统。
```
 resize2fs /dev/对应分区
```
本文以分区路径以 `/dev/vdb1`，则执行：
```
xfs_growfs /dev/vdb1

```
:::
</dx-tabs>
14. 参考 [设置开机自动挂载](https://cloud.tencent.com/document/product/362/6735#step16) 操作，设置分区自动挂载。

至此，已完成 MBR 分区转 GPT 分区配置，您可执行 `df -h` 命令查看分区信息。
