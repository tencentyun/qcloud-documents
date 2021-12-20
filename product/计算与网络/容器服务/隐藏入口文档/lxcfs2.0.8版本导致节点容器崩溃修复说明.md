## 问题说明
由于 Ubuntu 16.04 作为操作系统创建 TKE 集群系统默认安装 2.0.0 版本的 LXCFS，如果在节点上执行了系统升级命令 `sudo apt upgrade` 或主动将 LXCFS 包升级到最新的 2.0.8 版本后并未重启节点，kubelet 可能会在后续不确定的时间点发生故障，进而导致运行在该节点的容器崩溃以致无法正常提供服务。

## 影响版本
所有使用 **Ubuntu 16.04** 作为操作系统的集群节点。

## 原因及触发场景

### 原因分析
Ubuntu 16.04 系统默认安装 LXCFS 的 2.0.0 版本。
由于 2.0.0 版本的 LXCFS 会在 `/run/lxcfs/controllers/` 下挂载 cgroups 子系统，导致 kubelet 会探测到此挂载点，并用来控制容器资源。而在未安装 LXCFS 2.0.0 版本的情况下，kubelet 使用 `/sys/fs/cgroup/` 下的挂载点。




### 触发场景说明
在创建集群和节点后，若在节点上执行了系统升级命令 `sudo apt upgrade` 或者主动升级了 LXCFS 版本，那么 LXCFS 将升级到最新的 2.0.8 版本。

2.0.8 版本的 LXCFS 架构较之前版本发生变化，即不再挂载和使用 `/run/lxcfs/controllers/` 下的 cgroups 子系统。但在升级时，为了满足 LXCFS 服务进程 ID 不变的需求及其安装包的设置，系统不会重启 LXCFS 服务（重启服务时会解挂挂载点），而会向运行中的 LXCFS 服务进程发送 USR1 信号，并在 LXCFS 使用计数为0时，reload 相关 `.so` 模块。LXCFS 在 reload 时会解挂挂载点，导致 kubelet 在设置容器的 cgroups 资源时无法找到对应的目录和文件，最终导致容器崩溃。

LXCFS 计数为0和 reload 的时间无法预估，如果在某个时间触发以上场景，会导致该节点上的容器崩溃无法提供服务。为了确保消除这个隐患，请按照以下修复措施进行修复。 



## 判断节点情况
### 新建集群或节点
目前针对增量的修复已经全网上线，新建集群的节点或者已有集群新建的节点已经自动修复，不受该问题影响。

### 存量集群节点
>!除以下两种情况的存量节点外，其余情况的存量节点请按照 [具体修复步骤](#repair) 尽快修复。
>

#### 情况1：未升级 LXCFS ，并确定不进行升级操作
如果您的存量节点未升级 LXCFS，并确定之后也不会进行升级操作，则该存量节点无需修复。您可通过以下步骤确定节点是否属于此种情况：

在节点执行以下命令，查看 LXCFS 安装版本。
```
apt policy lxcfs
```
 - 如显示已安装的版本为 `2.0.0-0ubuntu2`，则 LXCFS 未升级。
 如该节点的 LXCFS 未升级，但您不能确定之后是否需要升级，请按照  [具体修复步骤](#repair) 进行修复。
 - 如显示已安装的版本为 `2.0.8-0ubuntu1~16.04.2`，则 LXCFS 已升级，请执行 [情况2](#CaseTwo) 判断节点是否需要修复。


#### 情况2：已升级 LXCFS 并重启节点[](id:CaseTwo)
如果您的存量节点已升级 LXCFS，并已进行重启操作。请按照以下步骤判断该节点是否需要修复：
1. 执行以下命令，查看 LXCFS 升级时间。
```
zgrep -B 4 "lxcfs" /var/log/apt/history.log*
```
返回结果中的 `Start-Date` 则为 LXCFS 升级时间。
2. 执行以下命令，查看系统启动时间。
```
uptime -s
```
3. 比较 LXCFS 升级时间与系统启动时间。
 - 如系统启动时间**晚于** LXCFS 升级时间，则节点无需修复。
 - 如系统启动时间**早于** LXCFS 升级时间，请按照 [具体修复步骤](#repair) 尽快修复。



## 修复措施
### 可能影响说明
- 在执行脚本修复的过程中，被修复的节点可能会短时间进入 NotReady 状态，但很快会恢复。在此期间该节点上运行的应用容器及其提供的服务不受影响。
- 如果您在修复过程中遇到问题，可以拨打 95716 或 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 反馈给我们，我们将尽快为您核实处理。

### 具体修复步骤[](id:repair)
1. 在需修复的节点上下载修复脚本，下载地址为：`https://lxcfs-1251707795.cos.ap-chengdu.myqcloud.com/upgrade-lxcfs.zip`。
2. 执行以下命令，解压并设置运行权限。
```
unzip -o upgrade-lxcfs.zip && chmod +x upgrade-lxcfs.sh
```
3. 执行以下命令，运行修复脚本。
```
./upgrade-lxcfs.sh
```

### 脚本内容说明
- 停止 kubelet 服务。
- 如果 LXCFS 未升级，则升级到 2.0.8 版本。
- 解挂 `/run/lxcfs/controllers/` 下的 cgroups 子系统。
- 启动 kubelet 服务。
- 给节点添加 annotation `cloud.tencent.com/node-lxcfs-upgraded=true`，以便统计升级情况。
