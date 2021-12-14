本文档将为您展示可能导致 Pod 一直处于 Terminating 状态的几种情形，以及如何通过排查步骤定位异常原因。请按照以下步骤依次进行排查，定位问题后恢复正确配置即可。

## 可能原因
- 磁盘空间不足
- 存在 “i” 文件属性
- Docker 17 版本 bug
- 存在 Finalizers
- 低版本 kubelet list-watch 的 bug
- Dockerd 与 containerd 状态不同步
- Daemonset Controller Bug

## 排查方法
### 检查磁盘空间是否不足
当 Docker 的数据目录所在磁盘被写满时，Docker 将无法正常运行，甚至无法进行删除和创建操作。kubelet 调用 Docker 删除容器时将无响应，执行 `kubectl describe pod <pod-name>` 命令，查看 event 通常返回信息如下：
```bash
Normal  Killing  39s (x735 over 15h)  kubelet, 10.179.80.31  Killing container with id docker://apigateway:Need to kill Pod
```

解决方法及更多信息请参考 [磁盘爆满](https://cloud.tencent.com/document/product/457/43126)。

### 检查是否存在 “i” 文件属性
#### 现象描述
“i” 文件属性描述可通过 `man chattr` 进行查看，描述示例如下：
``` txt
       A file with the 'i' attribute cannot be modified: it cannot be deleted or renamed, no link can be created to this file and no data can be written to the file.  Only the superuser or a process possessing the CAP_LINUX_IMMUTABLE capability can set or clear this attribute.
```
>!如果容器镜像本身或者容器启动后写入的文件存在 “i” 文件属性，此文件将无法被修改或删除。 
>
在进行 Pod 删除操作时，会清理容器目录，若该目录中存在不可删除的文件，会导致容器目录无法删除，Pod 状态也将一直保持 Terminating。此种情况下，kubelet 将会出现以下报错：
``` log
Sep 27 14:37:21 VM_0_7_centos kubelet[14109]: E0927 14:37:21.922965   14109 remote_runtime.go:250] RemoveContainer "19d837c77a3c294052a99ff9347c520bc8acb7b8b9a9dc9fab281fc09df38257" from runtime service failed: rpc error: code = Unknown desc = failed to remove container "19d837c77a3c294052a99ff9347c520bc8acb7b8b9a9dc9fab281fc09df38257": Error response from daemon: container 19d837c77a3c294052a99ff9347c520bc8acb7b8b9a9dc9fab281fc09df38257: driver "overlay2" failed to remove root filesystem: remove /data/docker/overlay2/b1aea29c590aa9abda79f7cf3976422073fb3652757f0391db88534027546868/diff/usr/bin/bash: operation not permitted
Sep 27 14:37:21 VM_0_7_centos kubelet[14109]: E0927 14:37:21.923027   14109 kuberuntime_gc.go:126] Failed to remove container "19d837c77a3c294052a99ff9347c520bc8acb7b8b9a9dc9fab281fc09df38257": rpc error: code = Unknown desc = failed to remove container "19d837c77a3c294052a99ff9347c520bc8acb7b8b9a9dc9fab281fc09df38257": Error response from daemon: container 19d837c77a3c294052a99ff9347c520bc8acb7b8b9a9dc9fab281fc09df38257: driver "overlay2" failed to remove root filesystem: remove /data/docker/overlay2/b1aea29c590aa9abda79f7cf3976422073fb3652757f0391db88534027546868/diff/usr/bin/bash: operation not permitted
```

#### 解决方法
- 彻底解决方法：不在容器镜像中或启动后的容器设置 “i” 文件属性，彻底杜绝此问题发生。
- 临时恢复方法：
 1. 针对 kubelet 日志报错提示的文件路径，执行 `chattr -i <file>` 命令。示例如下：
``` bash
    chattr -i /data/docker/overlay2/b1aea29c590aa9abda79f7cf3976422073fb3652757f0391db88534027546868/diff/usr/bin/bash
```
 2. 等待 kubelet 自动重试，Pod 即可自动删除。

### 检查是否存在 Docker 17 版本 bug
#### 现象描述
Docker hang 住，没有任何响应。执行 `kubectl describe pod <pod-name>` 命令查看 event 显示如下：
```bash
Warning FailedSync 3m (x408 over 1h) kubelet, 10.179.80.31 error determining status: rpc error: code = DeadlineExceeded desc = context deadline exceeded
```

造成该问题原因可能为17版本 dockerd 的 bug，虽然可以通过 `kubectl -n cn-staging delete pod apigateway-6dc48bf8b6-clcwk --force --grace-period=0` 强制删除 Pod，但执行 `docker ps` 命令后，仍然看得到该容器。

#### 解决方法
升级 Docker 版本至18，该版本使用了新的 containerd，针对很多已有 bug 进行了修复。
若 Pod 仍出现 Terminating 状态，请 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 联系工程师进行排查。**不建议直接强行删除**，可能会导致业务出现问题。

### 检查是否存在 Finalizers
#### 现象描述
K8S 资源的 metadata 中如果存在 `finalizers`，通常说明该资源是由某个程序创建的，`finalizers` 中也会添加一个专属于该程序的标识。例如，Rancher 创建的一些资源就会写入 `finalizers` 标识。

若想要删除该程序所创建的资源时，则需要由创建该资源的程序进行删除前的清理，且只有清理完成并将标识从该资源的 `finalizers` 中移除，才可以彻底删除资源。

#### 解决方法
使用 `kubectl edit` 命令手动编辑资源定义，删除 `finalizers`，删除资源便不会再受阻。


### 检查是否存在低版本 kubelet list-watch 的 bug
历史排查异常过程中发现，使用  v1.8.13 版本的 K8S 时，kubelet 会出现 list-watch 异常的情况。该问题会导致在删除 Pod 后，kubelet 未获取相关事件，并未真正删除，使 Pod 一直处 Terminating 状态。

请参考文档[ 升级集群 ](https://cloud.tencent.com/document/product/457/32192)步骤进行集群 Kubernetes 版本升级。

### Dockerd 与 containerd 状态不同步

#### 现象描述
docker 在 aufs 存储驱动下如果磁盘爆满，则可能发生内核 panic ，报错信息如下：
``` txt
aufs au_opts_verify:1597:dockerd[5347]: dirperm1 breaks the protection by the permission bits on the lower branch
```
若磁盘曾爆满过，dockerd 日志通常会有以下类似记录，且后续可能发生状态不同步问题。
``` log
Sep 18 10:19:49 VM-1-33-ubuntu dockerd[4822]: time="2019-09-18T10:19:49.903943652+08:00" level=error msg="Failed to log msg \"\" for logger json-file: write /opt/docker/containers/54922ec8b1863bcc504f6dac41e40139047f7a84ff09175d2800100aaccbad1f/54922ec8b1863bcc504f6dac41e40139047f7a84ff09175d2800100aaccbad1f-json.log: no space left on device"
```

#### 问题分析
判断 dockerd 与 containerd 的某个容器状态是否同步，可采用以下几种方法：
* 首先通过 `describe pod` 获取容器 ID，再通过 `docker ps` 查看容器状态是否为 dockerd 中所保存的状态。
* 通过 `docker-container-ctr` 查看容器在 containerd 中的状态。示例如下：
``` bash
  $ docker-container-ctr --namespace moby --address /var/run/docker/containerd/docker-containerd.sock task ls |grep a9a1785b81343c3ad2093ad973f4f8e52dbf54823b8bb089886c8356d4036fe0
  a9a1785b81343c3ad2093ad973f4f8e52dbf54823b8bb089886c8356d4036fe0    30639    STOPPED
```

若 containerd 中容器状态是 stopped 或者已经无记录，而 docker 中容器状态却是 running，则说明 dockerd 与 containerd 之间容器状态同步存在问题。




#### 解决方法
* 临时解决方法：执行 `docker container prune` 命令或重启 dockerd。
* 彻底解决方法：运行时推荐直接使用 containerd，绕过 dockerd 避免 Docker 本身的 Bug。

### Daemonset Controller Bug

K8S 中存在的 Bug 会导致 Daemonset Pod 持续 Terminating，Kubernetes 1.10 和 1.11 版本受此影响。由于 Daemonset Controller 复用 scheduler 的 predicates 逻辑，将 nodeAffinity 的 nodeSelector 数组进行排序（传递的指针参数），导致 spec 与 apiserver 中的值不一致。为了版本控制，Daemonset Controller 又使用了 spec 为 rollingUpdate 类型的 Daemonset 计算 hash。
上述传递过程造成的前后参数不一致问题，导致了 Pod 陷入持续启动和停止的循环。

#### 解决方法
- 临时解决方法：确保 rollingUpdate 类型 Daemonset 使用 nodeSelector 而不使用 nodeAffinity。
- 彻底解决方法：参考文档[ 升级集群 ](https://cloud.tencent.com/document/product/457/32192)步骤将集群 Kubernetes 版本升级至 1.12。




