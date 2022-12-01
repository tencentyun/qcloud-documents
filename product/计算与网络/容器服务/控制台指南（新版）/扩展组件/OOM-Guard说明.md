## 简介 
>? 该组件在用户态降低了由于 cgroup 内存回收失败而产生的各种内核故障的发生几率，仅适用于解决操作系统版本为 CenteOS 7.2/7.6的原生内核缺陷，其他镜像版本无需安装。


### 组件介绍
内存溢出（Out of Memory，OOM）是指应用系统中存在无法回收的内存或使用的内存过多，最终使得程序运行要用到的内存大于能提供的最大内存。当 cgroup 内存不足时，Linux 内核会触发 cgroup OOM 来选择一些进程杀掉，以便能回收一些内存从而尽量继续保持系统继续运行。但 Linux 内核（尤其是3.10等低版本内核）对 cgroup OOM 的处理存在很多问题，频繁的 cgroup OOM 经常会带来节点故障（例如卡死、重启或进程异常但无法杀死）的情况。

OOM-Guard 是容器服务 TKE 提供用于在用户态处理容器 cgroup OOM 的组件。当 cgroup OOM 情况出现时，在系统内核杀死相关容器进程之前，OOM-Guard 组件会直接在用户空间杀掉超过内存限制的容器，从而减少了在内核态回收内存失败而触发各种节点故障的概率。

在触发阈值进行 OOM 之前，OOM-Guard 会先通过写入 `memory.force_empty` 触发相关 cgroup 的内存回收，如果 `memory.stat` 显示还有较多 cache，则不会触发后续处理策略。在 cgroup OOM 杀掉容器后，会向 Kubernetes 上报 `OomGuardKillContainer` 事件，可以通过 `kubectl get event` 命令进行查看。

### 原理介绍
核心思想是在发生内核 cgroup OOM kill 之前，在用户空间杀掉超限的容器， 减少走到内核 cgroup 内存回收失败后的代码分支从而触发各种内核故障的机会。

oom-guard 会给 memory cgroup 设置 threshold notify，接受内核的通知。详情见 [threshold notify](https://lwn.net/Articles/529927/)。

#### 示例
假如一个 pod 设置的 memory limit 是1000M，oom-guard 会根据配置参数计算出 margin。
```
margin = 1000M * margin_ratio = 20M // 缺省 margin_ratio 是 0.02
```
另外 margin 最小不小于 min_margin（缺省1M），最大不大于 max_margin（缺省为50M）。如果超出范围，则取 min_margin 或 max_margin。

然后计算 threshold：
```
threshold = limit - margin // 即 1000M - 20M = 980M
```
把980M作为阈值设置给内核。当这个 pod 的内存使用量达到980M时，oom-guard 会收到内核的通知。

在触发阈值之前，oom-gurad 会先通过 memory.force_empty 触发相关 cgroup 的内存回收。另外，如果触发阈值时，相关 cgroup 的 memory.stat 显示还有较多 cache，则不会触发后续处理策略，这样当 cgroup 内存达到 limit 时，内核还是会触发 cgroup OOM。

#### 达到阈值后的处理策略
通过`--policy`参数来控制处理策略。目前有以下三个策略，缺省策略是 container。

| 策略 | 描述|
|---------|---------|
|process | 采用跟内核 cgroup OOM killer 相同的策略，在该 cgroup 内部，选择一个 oom_score 得分最高的进程杀掉。通过 oom-guard 发送 SIGKILL 来杀掉进程。  | 
| container | 在该 cgroup 下选择一个 docker 容器，杀掉整个容器。| 
| noop |  只记录日志，并不采取任何措施。| 

### 部署在集群内的 Kubernetes 对象

| Kubernetes 对象名称 | 类型               | 默认占用资源            | 所属 Namespaces |
| ------------------- | ------------------ | ----------------------- | --------------- |
| oomguard            | ServiceAccount     | -                | kube-system     |
| system:oomguard     | ClusterRoleBinding |-                   | -            |
| oom-guard           | DaemonSet          | 0.02核 CPU，120MB内存 | kube-system     |

## 使用场景 
应用于节点内存压力比较大，业务容器经常发生 OOM 导致节点故障的 Kubernetes 集群。

## 限制条件
- 没有修改 containerd 服务 socket 路径，保持 TKE 的默认路径：
   - docker 运行时：`/run/docker/containerd/docker-containerd.sock`
   - containerd 运行时：`/run/containerd/containerd.sock`
- 没有修改 cgroup 内存子系统挂载点，保持默认挂载点：`/sys/fs/cgroup/memory`

## 使用方法

1. 登录[ 容器服务控制台  ](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 OOM-Guard。
5. 单击**完成**即可安装组件。
