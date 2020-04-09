本文档介绍可能导致 Pod 一直处于 ContainerCreating 或 Waiting 状态的几种情形，以及如何通过排查步骤定位异常原因。请对应实际异常情况按照以下步骤依次排查直至能够定位引发异常原因，定位问题后恢复正确配置即可。

## 可能原因及排查步骤
### Pod 配置错误
1. 检查是否打包了正确的镜像。
2. 检查是否配置了正确的容器参数。

### 挂载 Volume 失败
Volume 挂载失败的诱因存在多种可能，以下列出其中两种已知情况：

#### 1. Pod 漂移导致未正常解挂磁盘
**Pod 漂移**
在云托管的 K8S 服务环境下，默认挂载的 Volume 通常为一块存储类型的云硬盘。如果某个节点出现故障，kubelet 无法正常运行或与 apiserver 通信，则到达时间阈值后就会触发节点驱逐，自动在其它节点上启动相同的 Pod。

**影响**
被驱逐的节点无法正常运行及确定自身状态，故该节点的 Volume 也未正确执行解挂操作。而 cloud-controller-manager 需等待 Volume 正确解挂后，再调用云厂商接口真正解挂 Volume。Pod 漂移将导致 cloud-controller-manager 在达到一个时间阈值后，强制解挂 Volume 并挂载到 Pod 最新调度的节点上。**最终导致 ContainerCreating 的时间相对较长**，**但通常是可以启动成功的**。

#### 2. 命中 K8S 挂载 configmap/secret 时 subpath 的 bug

实践发现，当修改了 Pod 已挂载的 configmap 或 secret 的内容，并且 Pod 中容器又进行了原地重启操作时（例如，存活检查失败被 kill 后重启拉起），就会触发 K8S 挂载 configmap/secret 时 subpath 的 bug。

如果出现了以上情况，容器将会持续启动不成功。报错示例如下：
``` bash
$ kubectl -n prod get pod -o yaml manage-5bd487cf9d-bqmvm
...
lastState: terminated
containerID: containerd://e6746201faa1dfe7f3251b8c30d59ebf613d99715f3b800740e587e681d2a903
exitCode: 128
finishedAt: 2019-09-15T00:47:22Z
message: 'failed to create containerd task: OCI runtime create failed: container_linux.go:345:
starting container process caused "process_linux.go:424: container init
caused \"rootfs_linux.go:58: mounting \\\"/var/lib/kubelet/pods/211d53f4-d08c-11e9-b0a7-b6655eaf02a6/volume-subpaths/manage-config-volume/manage/0\\\"
to rootfs \\\"/run/containerd/io.containerd.runtime.v1.linux/k8s.io/e6746201faa1dfe7f3251b8c30d59ebf613d99715f3b800740e587e681d2a903/rootfs\\\"
at \\\"/run/containerd/io.containerd.runtime.v1.linux/k8s.io/e6746201faa1dfe7f3251b8c30d59ebf613d99715f3b800740e587e681d2a903/rootfs/app/resources/application.properties\\\"
caused \\\"no such file or directory\\\"\"": unknown'
```

### 磁盘空间不足
启动 Pod 时会调 CRI 接口创建容器，容器运行时组件创建容器时通常会在数据目录下为新建的容器创建一些目录和文件。如果数据目录所在的磁盘空间不足，将会导致容器创建失败。通常会显示以下报错信息：
```bash
Events:
  Type     Reason                  Age                  From                   Message
  ----     ------                  ----                 ----                   -------
  Warning  FailedCreatePodSandBox  2m (x4307 over 16h)  kubelet, 10.179.80.31  (combined from similar events): Failed create pod sandbox: rpc error: code = Unknown desc = failed to create a sandbox for pod "apigateway-6dc48bf8b6-l8xrw": Error response from daemon: mkdir /var/lib/docker/aufs/mnt/1f09d6c1c9f24e8daaea5bf33a4230de7dbc758e3b22785e8ee21e3e3d921214-init: no space left on device
```

解决步骤及更多信息请参见 [磁盘爆满](https://cloud.tencent.com/document/product/457/43126)。


### 节点内存碎片化
如果节点出现内存碎片化严重、缺少大页内存问题，即使总体剩余内存较多，仍会出现申请内存失败的情况。解决步骤及更多信息请参见 [内存碎片化](https://cloud.tencent.com/document/product/457/43128)。

### Limit 设置过小或单位错误
当 limit 设置过小以至于不足以成功运行 Sandbox 时，也会导致 Pod 一直处于 ContainerCreating 或 Waiting 状态，此问题通常是 memory limit 单位设置错误引起的。如果误将 memory limit 单位设置为小写字母 `m`，则该单位将会被 K8S 识别成 Byte，**正确单位设置应为 `Mi` 或 `M`**。

例如，memory limit 设置为1024m，则表示其大小将会被限制在1.024Byte以下。较小的内存环境下，pause 容器一启动就会被 cgroup-oom kill 掉，导致 Pod 状态一直处于 ContainerCreating。

执行 `kubectl describe pod <pod-name>` 命令，查看 event 报错信息如下：
``` txt
Pod sandbox changed, it will be killed and re-created。
```
此问题 kubelet 报错如下：
``` txt
to start sandbox container for pod ... Error response from daemon: OCI runtime create failed: container_linux.go:348: starting container process caused "process_linux.go:301: running exec setns process for init caused \"signal: killed\"": unknown
```

### 拉取镜像失败
引起镜像拉取失败原因较多，本文列举如下情况：
- 配置了错误的镜像。
* Kubelet 无法访问镜像仓库。例如，默认 pause 镜像在 gcr.io 上，而国内环境访问需要特殊处理。
* 拉取私有镜像的 imagePullSecret 没有配置或配置有误。
* 镜像太大，拉取超时。可在拉取时适当调整 kubelet 的 `--image-pull-progress-deadline` 和 `--runtime-request-timeout` 选项。

### CNI 网络错误

如果发生 CNI 网络错误，通常需要检查网络插件的配置和运行状态。没有正确配置或无法正常运行通常表现为：
* 无法配置 Pod 网络。
* 无法分配 Pod IP。

### controller-manager 异常
查看 Master 上 kube-controller-manager 状态，异常时尝试重启。

### 安装 docker 时未完全删除旧版本
节点已有 docker 或旧版本 docker 未完全卸载的情况下，又安装了 docker。例如，在 CentOS 上，执行以下命令重复安装了 docker：
```
yum install -y docker
```
由于重复安装的 docker 版本不一致，组件间不完全兼容，导致 dockerd 持续无法成功创建容器，使 Pod 状态一直 ContainerCreating。执行 `kubectl describe pod <pod-name>` 命令，查看 event 报错信息如下：
```
  Type     Reason                  Age                     From                  Message
  ----     ------                  ----                    ----                  -------
  Warning  FailedCreatePodSandBox  18m (x3583 over 83m)    kubelet, 192.168.4.5  (combined from similar events): Failed create pod sandbox: rpc error: code = Unknown desc = failed to start sandbox container for pod "nginx-7db9fccd9b-2j6dh": Error response from daemon: ttrpc: client shutting down: read unix @->@/containerd-shim/moby/de2bfeefc999af42783115acca62745e6798981dff75f4148fae8c086668f667/shim.sock: read: connection reset by peer: unknown
  Normal   SandboxChanged          3m12s (x4420 over 83m)  kubelet, 192.168.4.5  Pod sandbox changed, it will be killed and re-created.
```

### 存在同名容器

当节点上已存在同名容器时，则创建 sandbox 时会失败。执行 `kubectl describe pod <pod-name>` 命令，查看 event 报错信息如下：
```
  Warning  FailedCreatePodSandBox  2m                kubelet, 10.205.8.91  Failed create pod sandbox: rpc error: code = Unknown desc = failed to create a sandbox for pod "lomp-ext-d8c8b8c46-4v8tl": operation timeout: context deadline exceeded
  Warning  FailedCreatePodSandBox  3s (x12 over 2m)  kubelet, 10.205.8.91  Failed create pod sandbox: rpc error: code = Unknown desc = failed to create a sandbox for pod "lomp-ext-d8c8b8c46-4v8tl": Error response from daemon: Conflict. The container name "/k8s_POD_lomp-ext-d8c8b8c46-4v8tl_default_65046a06-f795-11e9-9bb6-b67fb7a70bad_0" is already in use by container "30aa3f5847e0ce89e9d411e76783ba14accba7eb7743e605a10a9a862a72c1e2". You have to remove (or rename) that container to be able to reuse that name.
```


