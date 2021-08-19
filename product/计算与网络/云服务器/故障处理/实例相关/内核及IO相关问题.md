使用实例自助检测时，可从检测报告中获取实例的异常情况。本文主要介绍实例自助检测报告中，内核及 IO 相关问题现象、引发原因及处理步骤。

## 内核问题定位及处理

### 故障现象
内核相关故障，可能导致机器无法登录或异常重启

### 可能原因
#### 内核 hung_task
hung task 机制通过内核线程 khungtaskd 实现，khungtaskd 监控 TASK_UNINTERRUPTIBLE 状态的进程。如果在 `kernel.hung_task_timeout_secs`（默认120秒）周期内一直处于 D 状态，则会打印 hung task 进程的堆栈信息。

如果配置 `kernel.hung_task_panic=1`，则会触发内核 panic 重启机器。



#### 内核软死锁 soft lockup
soft lockup 指 CPU 被内核代码占据以至于无法执行其他进程。检测 soft lockup 的原理是给每个 CPU 分配一个定时执行的内核线程 [watchdog/x]，如果该线程在一定周期内（默认为`2*kernel.watchdog_thresh`，3.10内核 `kernel.watchdog_thresh` 默认为10秒）没有得到执行，则表明发生了 soft lockup。

如果配置了 `kernel.softlockup_panic=1`，则会触发内核 panic 重启机器。


#### 内核 panic
内核异常 crash 导致机器异常重启，常见的内核 panic 场景如下：
- 内核出现了 hung_task 且配置了 `kernel.hung_task_panic=1`。
- 内核出现了软死锁 soft lockup 且配置了 `kernel.softlockup_panic=1`。
- 触发了内核 bug。

### 处理步骤
内核相关问题排查及处理步骤较复杂，建议通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_213
) 进一步定位及处理。


## 硬盘问题定位及处理

### 硬盘 inode 满
**故障现象**：创建新文件时提示 “No space left on device” 错误信息，且使用 `df -i` 命令查看 inode 空间使用率100%。
**可能原因**： 文件系统 inode 耗尽。
**处理步骤**：删除无需使用的文件或扩容硬盘。

### 硬盘空间使用率满
**故障现象**：创建新文件时提示 “No space left on device” 错误信息，且使用 `df -h` 命令查看到硬盘空间使用率100%。
**可能原因**： 硬盘空间耗尽。
**处理步骤**：删除无需使用的文件或扩容硬盘。

### 硬盘只读
**故障现象**： 文件系统只能读文件，不能创建新文件。
**可能原因**： 文件系统有损坏。
**处理步骤**：
1. 创建快照以备份硬盘数据，详情请参见 [创建快照](https://cloud.tencent.com/document/product/362/5755)。
2. 根据硬盘类型，执行对应处理步骤：
<dx-tabs>
::: 系统盘
建议直接重启实例，详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。
::: 
::: 数据盘
1. 执行以下命令，查看只读盘对应的文件系统类型。
```
lsblk -f
``` 
2. 执行以下命令，卸载数据盘。
```
umount <对应盘挂载路径>
```
3. 对应文件系统类型，执行以下命令进行修复：
 - **ext3/ext4** 文件系统，执行以下命令：
```
fsck -y /dev/对应盘
```
 - **xfs** 文件系统，执行以下命令：
```
xfs_repair /dev/对应盘
```
:::
</dx-tabs>

### 硬盘 %util 高
**故障现象**：实例卡顿，使用 SSH 或 VNC 登录慢或无响应。
**可能原因**：IO 高导致硬盘 %util 达到100%。
**处理步骤**：查看 IO 高是否合理，且需评估是否减少 IO 读写或者置换更高性能的硬盘。




