当用户需要进行文件备份或迁移时，传统`rsync`类工具无法指定迁移任务启动/终止时间，极有可能导致迁移任务在用户业务高负载时挤占用户计算、网络、存储等资源。为减轻用户管理数据迁移任务的负担，文件存储（Cloud File Storage，CFS）提供了可控制数据迁移任务起止时间的迁移工具 `Filetruck`。

- Filetruck 的主要功能如下：
  - 数据迁移任务
  - 支持增量迁移，自动完成 MD5 一致性校验 （迁移时建议使用 sync 方式挂载，进一步保障一致性）
  - 根据任务 ID 查询任务执行情况
  - 列出所有历史任务
- Filetruck 支持的源和目的地址如下：
<table>
	<tr><th>支持项</th><th>源</th><th>目的</th></tr>
	<tr>
	<td>迁移地址</td>
	<td><ul  style="margin: 0;">
	<li>CFS 文件系统 </li>
	<li> 本地文件系统（CBS 云硬盘格式化后安装的文件系统） </li>
	<li> COSFS 本地路径 </li>
	<li>打通网络后挂载到该主机上的所有本地路径</li>
	</ul>
</td>
<td><ul  style="margin: 0;">
	<li>CFS 文件系统 </li>
	<li> 本地文件系统（CBS 云硬盘格式化后安装的文件系统）</li>
	<li> COSFS 本地路径 </li>
	<li> 打通网络后挂载到该主机上的所有本地路径</li>
	</ul>
</td></tr>
</table>
- Filetruck 功能说明：
Filetruck 为一次性迁移工具，如在迁移过程中修改源文件，可能会导致迁移结果与源文件不一致。（取决于被修改的内容在保存的时刻该段数据是否已经完成迁移；若被修改部分在修改时刻已经完成了迁移，则修改内容不会出现在迁移结果中；若被修改部分在修改时刻还未执行迁移，则修改内容会继续被同步到目标地址。因此建议执行迁移/备份任务过程中暂停对源文件的修改或者更新。）


下面介绍如何使用迁移工具进行数据迁移或者数据备份。

## 准备工作

在迁移工作开始前，用户需要先下载并安装 Filetruck 迁移工具。
1. 执行如下命令，下载 cfs-filetruck 工具。
```
wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/tools/cfs-filetruck.tar.gz
```
2. 执行如下命令，解压工具。
```
tar -xzvf cfs-filetruck.tar.gz
```
3. 执行如下命令，校验 MD5 值。
```
cd ./cfs-filetruck/ && md5sum *
cat ./md5sum.txt
```
4. 执行如下命令，安装 cfs-filetruck。
```
sudo mv ./filetruck_client /usr/local/bin
sudo mv ./server_filetruck /usr/local/bin
```


## 操作步骤
### 创建数据迁移任务

####  通过简单配置启动新任务

迁移工具根据`ini`格式配置文件启动迁移任务。新任务配置文件**需要用户手动创建**且**需要用户使用系统管理员权限运行**。最简单的新任务配置文件内容如下：

```
# 源文件夹绝对路径
SourceDirPath=/path/to/sourceDir
# 目的文件夹绝对路径
TargetDirPath=/path/to/targetDir
```

用户可以复制上述内容到配置文件`newTask.ini`中，再按需调整源文件夹和目的文件夹路径，然后以 root 用户身份执行命令`filetruck_client -c newTask.ini`即可启动一个新任务。

如果新任务启动成功，迁移工具将返回如下包含 TaskId 的返回信息：

```
# filetruck_client -c newTask.ini
TaskId=1
```

如果配置文件中信息有误，会导致新任务启动失败，迁移工具将返回相关告警信息提示用户修改配置文件：

```
# filetruck_client -c newTask.ini
Error: Directory does not exist: /path/to/sourceDir
```

####  通过高级配置启动新任务

大部分情况下，用户只需指定文件迁移任务的源文件夹地址（SourceDirPath）和目的文件夹地址（TargetDirPath）即可创建一个新的迁移任务。如果用户需要指定迁移任务起止时间（StartDate、EndDate）、数据传输带宽限制（BandwidthLimitInKbps）以及目的文件匹配规则（IncludeRule、ExcludeRule），可以通过给迁移工具提供高级任务配置文件满足需求。

一个高级任务配置文件内容如下：

```
# 源文件夹地址（必填，需要文件夹绝对路径）
SourceDirPath=/path/to/sourceDir
# 目的文件夹地址（必填，需要文件夹绝对路径）
TargetDirPath=/path/to/targetDir
# 任务启动时间（选填，格式必须为：YYYY MMM DD hh:mm:ss）
StartDate=2020 Aug 02 11:22:33
# 任务终止时间（选填，格式必须为：YYYY MMM DD hh:mm:ss）
EndDate=2020 Aug 02 12:22:33
# 数据传输带宽限制（选填，单位为KiB/s，范围是[0, 2147483647]，0代表不限速）
BandwidthLimitInKbps=1024
# 待迁移文件匹配规则（选填）
IncludeRule=*.jpg
# 非迁移文件匹配规则（选填）
ExcludeRule=*.png
```

#### 参数说明

- `SourceDirPath` 和 `TargetDirPath` 为必填项，且需要提供文件夹的绝对路径。
- `StartDate`、`EndDate`、`BandwidthLimitInKbps`、`IncludeRule`、`ExcludeRule`为选填项，可以不在配置文件中列出。
- `StartDate` 和 `EndData` 的格式必须为`yyyy mmm dd HH:MM:SS`。例如2020年8月8号20点20分8秒，不能写成`2020 Aug 8 20:20:8`，而要遵循格式，写成`2020 Aug 08 20:20:08`。
- `BandwidthLimitInKbps`的合法值范围是[0, 2147483647]，0代表不限速。说明：工具运行过程中，迁移/备份速度与所在主机的 CPU/内存配置/网络带宽配置，源及目的地址的网络位置，以及所需要迁移/备份的文件大小直接相关；通常主机配置越高、网络出口带宽越大同时文件越大迁移/备份速度会越快。例如，主机配置为8核16G 网络带宽1.5Gbps， 从本地文件系统迁移4KB  小文件到 CFS 性能型文件系统，速度大约为40KB/s；从本地文件系统迁移1TB 大文件到 CFS 性能型文件系统，速度大约为140MB/s。
- `IncludeRule/ExcludeRule` 的匹配规则如下：
  - 迁移工具目前只支持用户提供 `IncludeRule` 和 `ExcludeRule` 各一条。
  - 迁移工具默认迁移源文件夹下全部文件（包含硬链接）。
  - `IncludeRule` 仅在 `ExcludeRule` 存在时生效。
  - 当 `IncludeRule` 与 `ExcludeRule` 同时存在时，把源文件夹看做全集，迁移工具将迁移 `ExcludeRule` 划定的补集以及 `IncludeRule` 和 `ExcludeRule` 的交集。
  - 常用的同步通配符有：`*`、`？`等。`*`将匹配除`/`外的任意多个字符，`?`将匹配除`/`外的单个字符。
  - 常用的匹配模式有：`*.jpg`、`abc*`、`abc*def`
  - 常见的匹配模式有：
    - 迁移全部文件：`IncludeRule=`和`ExcludeRule=`
    - 不迁移 png 文件：`ExcludeRule=*.png`
    - 只迁移 jpg 文件，不迁移 png 文件：`IncludeRule=*.jpg`配合`ExcludeRule=*.png`
    - 只迁移 jpg 文件，不迁移剩余文件：`IncludeRule=*.jpg`配合`ExcludeRule=sourceDir/*`


###  查询任务执行情况

####  查询全部任务执行情况

用户可以通过执行命令`filetruck_client -l`查看迁移工具全部历史任务（含运行中和已完成的任务）：

```
# filetruck_client -l
TaskId  State           FileCount       SentBytes       Speed           Progress
1       Partial Done    59              0               0B/s            3%
2       All Done        1               1073872935      511K/s          100%
3       All Done        2               1073872935      511K/s          100%
4       Partial Done    1               0               0B/s            3%
5       All Done        2               1073872935      511K/s          100%
6       All Done        2               1073872935      511K/s          100%
7       All Done        1285            138796240       502K/s          100%
8       All Done        1               0               0B/s            100%
9       All Done        0               0               0B/s            100%
10      Running         712             82799297        449K/s          24%
```


#### 参数说明
- 迁移工具创建的迁移任务共有5种状态，分别是：
  - `Waiting`：等待
  - `Running`：运行中
  - `All Done`：全部完成
  - `Partial Done`：部分完成（因超时或用户主动取消而被终止）
  - `Failed`：失败
  - `另， FileCount/SentBytes/Speed/Progress`的值未计算出来时，将显示`-`。
- 迁移任务完成后，文件 inode 值将变化。
- 迁移工具将默认迁移源文件夹下存在的硬链接。




####  查询指定任务执行情况

用户也可以通过命令`filetruck_client -t TASK_ID`根据有效任务 ID 查询某任务详细信息：

```
# filetruck_client -t 3
TaskId:                 3
TaskState:              All Done
SourceDirPath:          /mnt/cfs0/
TargetDirPath:          /mnt/cfs1/
BeginDate:              2020 Dec 02 15:13:20
EndDate:                2020 Dec 02 15:30:25
SentFilesCount:         2
SentDataSizeInByte:     1073872935
SentSpeed:              511K/s
TaskProgress:           100%
```

当用户给定的`TASK_ID`无效时，迁移工具将返回如下报错信息：

```
# filetruck_client -t 999
Error: Task with ID=999 is not founded.
```

### 取消执行中的任务

用户可以通过命令`filetruck_client -k TASK_ID`根据 TASK_ID 取消某个执行中的任务。

```
# filetruck_client -k 10
Success
```


<dx-alert infotype="notice" title="">
取消执行中的迁移任务可能导致未完成传输的文件在目的文件夹被销毁，从而避免在目的文件夹留下不完整的文件。
</dx-alert>


### 获取帮助信息

用户可以通过命令`filetruck_client -h`获取迁移工具帮助信息。

```
CFS-Filetruck version: 0.1.3b
Copyright (C) 2020 Tencent Inc. All rights reserved.
Link: https://cloud.tencent.com/product/cfs
 
CFS-Filetruck makes file migration easier.
 
Usage:
  Create a new task:
    filetruck_client -c /path/to/new/task/config/file.ini
 
  Get task state by task id:
    filetruck_client -t TASK_ID
 
  Cancel/Kill task by task id:
    filetruck_client -k TASK_ID
 
  List all tasks:
    filetruck_client -l
 
  Print help:
    filetruck_client -h
```
