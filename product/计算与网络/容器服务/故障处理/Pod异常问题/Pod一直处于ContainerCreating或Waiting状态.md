本文档介绍可能导致 Pod 处于 CrashLoopBackOff 状态的几种情形，以及如何通过排查步骤定位异常原因。请按照以下步骤依次进行排查，定位问题后恢复正确配置即可。

## 现象描述

Pod 处于 `CrashLoopBackOff` 状态，说明该 Pod 在正常启动过后异常退出过，此时只要 Pod 的 [restartPolicy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) 不是 Never 就可能会被重启拉起，此状态下 Pod 的 `RestartCounts` 通常大于0。

## 可能原因
- 容器进程主动退出
- 系统 OOM
- cgroup OOM
- 节点内存碎片化
- 健康检查失败

## 排查步骤
>?可参考 [通过 Exit Code 定位 Pod 异常退出原因](https://cloud.tencent.com/document/product/457/43125)，查看容器进程的退出状态码缩小问题范围及获取更多异常信息。

### 检查容器进程是否主动退出

容器进程主动退出时，退出状态码通常在0 - 128之间，导致异常的原因可能是业务程序 Bug，也可能是其它原因，请参考 [容器进程主动退出](https://cloud.tencent.com/document/product/457/43148) 进一步分析异常原因。

### 系统 OOM

如果发生系统 OOM，Pod 中容器退出状态码为137，表示其被 `SIGKILL` 信号停止，同时内核将会出现以下报错信息。
```
Out of memory: Kill process ...
```
该异常大概率是由于节点上部署了其它非 K8S 管理的进程消耗了较多的内存，或者 kubelet 的 `--kube-reserved` 和 `--system-reserved` 所分配的内存太小以至于没有足够的空间运行其它非容器进程。

节点上所有 Pod 的实际内存占用总量不会超过  `/sys/fs/cgroup/memory/kubepods` 中 cgroup 的限制，该限制值等于 `capacity - "kube-reserved" - "system-reserved"`。通常情况下，如果预留空间设置合理，且节点上其它非容器进程（非 kubelet、dockerd、kube-proxy 及 sshd 等）内存占用没有超过 kubelet 配置的预留空间，是不会发生系统 OOM 的。为确保不再发生此类问题，您可以根据实际需求对预留空间进行合理的调整。

### cgroup OOM
如果是 cgroup OOM 停止的进程，可查看 Pod 事件下 `Reason` 为 `OOMKilled`，说明容器实际占用的内存已超过 limit，同时内核日志会报 `Memory cgroup out of memory`，此时可以根据需求调整 limit。

### 节点内存碎片化
如果出现节点内存碎片化严重、缺少大页内存问题，将会导致即便剩余总内存较多，但仍会申请内存失败，请参考 [内存碎片化](https://cloud.tencent.com/document/product/457/43128) 进行处理。

### 健康检查失败
请参考 [Pod 健康检查失败](https://cloud.tencent.com/document/product/457/43129) 进行问题进一步定位。
