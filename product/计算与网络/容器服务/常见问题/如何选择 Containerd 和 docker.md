
## 如何选择 Containerd 和 Docker

### 如何选择运行时组件？

容器运行时（Container Runtime）是 Kubernetes（K8S） 最重要的组件之一，负责管理镜像和容器的生命周期。Kubelet 通过 `Container Runtime Interface (CRI)` 与容器运行时交互，以管理镜像和容器。

TKE 支持用户选择 Containerd 和 Docker 作为运行时组件：
- Containerd 调用链更短，组件更少，更稳定，占用节点资源更少。建议选择 Containerd。
- 当您遇到以下情况时，请选择 docker 作为运行时组件：
 - 如需使用 docker in docker。
 - 如需在 TKE 节点使用 docker build/push/save/load 等命令。
 - 如需调用 docker API。
 - 如需 docker compose 或 docker swarm。


### 如何修改运行时组件？
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster/startUp) ，选择左侧导航栏中的集群。
2. 在“集群管理”列表页面，选择目标集群 ID，进入该集群基本信息页面。
3. 在“集群基本信息”中修改运行时组件。如下图所示：
>? 修改运行时组件及版本，只对集群内无节点池归属的增量节点生效，不会影响存量节点。
>
![](https://qcloudimg.tencent-cloud.cn/raw/bafb92c1dff0c5a51555745f85b9e13f.png)


### Containerd 和 Docker 组件常用命令是什么？
Containerd 不支持 docker API 和 docker CLI，但是可以通过 cri-tool 命令实现类似的功能。

#### 镜像相关
| 镜像相关功能     | Docker                  | Containerd              |
| :--------------- | :---------------------- | :---------------------- |
| 显示本地镜像列表 | docker images           | crictl images           |
| 下载镜像         | docker pull             | crictl pull             |
| 上传镜像         | docker push             | 无                      |
| 删除本地镜像     | docker rmi              | crictl rmi              |
| 查看镜像详情     | docker inspect IMAGE-ID | crictl inspect IMAGE-ID |


#### 容器相关

| 容器相关功能 | Docker         | Containerd     |
| :----------- | :------------- | :------------- |
| 显示容器列表 | docker ps      | crictl ps      |
| 创建容器     | docker create  | crictl create  |
| 启动容器     | docker start   | crictl start   |
| 停止容器     | docker stop    | crictl stop    |
| 删除容器     | docker rm      | crictl rm      |
| 查看容器详情 | docker inspect | crictl inspect |
| attach       | docker attach  | crictl attach  |
| exec         | docker exec    | crictl exec    |
| logs         | docker logs    | crictl logs    |
| stats        | docker stats   | crictl stats   |

#### POD 相关
| POD 相关功能  | Docker | Containerd      |
| :------------ | :----- | :-------------- |
| 显示 POD 列表 | 无     | crictl pods     |
| 查看 POD 详情 | 无     | crictl inspectp |
| 运行 POD      | 无     | crictl runp     |
| 停止 POD      | 无     | crictl stopp    |

### 调用链区别有哪些？
- Docker 作为 K8S 容器运行时，调用关系如下：
`kubelet --> docker shim （在 kubelet 进程中） --> dockerd --> containerd`
- Containerd 作为 K8S 容器运行时，调用关系如下：
`kubelet --> cri plugin（在 containerd 进程中） --> containerd`

其中 dockerd 虽增加了 swarm cluster、docker build 、docker API 等功能，但也会引入一些 bug，而与 Containerd 相比，多了一层调用。
包括 exec，preStop，ipv6，日志 stdout 的格式等。


## Stream 服务的区别
`kubectl exec/logs` 等命令需要 kubelet 在 apiserver 跟容器运行时之间建立流转发通道。

### Stream 服务的原理是什么？

可以通过了解`kubectl exec`命令的原理来了解 CRI 的 Stream Service 是如何工作的：
1. dockershim 或 containerd 在启动后会监听某个端口，用以运行 Stream 服务。
2. 当执行 `kubectl exec` 等命令时，请求经过 kube-apiserver 找到 Pod 对应的节点，转发到 kubelet。
3. 此时 kubelet 会请求 CRI-Service（dockershim 或 containerd-cri）的 GetExec 接口，CRI-Server 会为本次请求生成一个随机的 Token，记录后和 CRI Stream server 监听端口组合成 URL，返回给 kubelet。
4. kubelet 将 kube-apiserver 发过来的 HTTP 请求升级 websocket，并作为 apiserver 和 CRI Stream 之间的 proxy 转发数据。

### 如何在 Containerd 中使用并配置 Stream 服务？

Docker API 本身提供 stream 服务，Dockershim 位于 kubelet 内部有默认的配置 "127.0.0.1:0" 。

Containerd 的 stream 服务需要单独配置：

```
[plugins.cri]
  stream_server_address = "127.0.0.1"
  stream_server_port = "0"
  enable_tls_streaming = false
```

### K8S 1.11 前后版本配置区别是什么？
Containerd 的 stream 服务在 K8S 不同版本运行时场景下配置不同。
- 在 K8S 1.11 之前：
Kubelet 不会做 stream proxy，只会做重定向。即 Kubelet 会将 containerd 暴露的 stream server 地址发送给 apiserver，并让 apiserver 直接访问 containerd 的 stream 服务。此时，您需要给 stream 服务转发器认证，用于安全防护。
- 在 K8S 1.11 之后：
 K8S 1.11 引入了 [kubelet stream proxy](https://github.com/kubernetes/kubernetes/pull/64006)， 使 containerd stream 服务只需要监听本地地址即可。

## 容器 Exec 的区别

Docker 和 Containerd 在 Exec 的实现上略有区别，区别主要在 Execsync 的实现上，也即执行单条命令的情况。

因此 `kubectl exec`命令在不指定参数`-it`时 和 pod lifecycle 中的 ExecProbe 在 Runtime 类型不同的节点上表现可能稍有不同。

### kubectl exec 的区别

- docker exec 时会以 **当前exec首进程结束** 为 exec 结束的标志。
- CRI exec 会以 **当前exec中所有进程结束** 为本次 exec 结束。

如 `kubectl exec <pod-id> -- bash -c "nohup sleep 10 &"` 命令，在 Runtime 是 docker 的节点上会在两秒左右结束；而在 containerd 的节点上需要等到 sleep 进程退出后才能结束。

### pod exec probe 的区别

kubelet 在实现 exec probe 时使用了 CRI Runtime 的 ExecSync 接口，因此 exec probe 和 `kubectl exec # no -t -i` 的表现一致，也即：

- 在 Docker 节点上，exec probe 如果残留子进程仍会正常退出。
- 在 Containerd 节点上，exec probe 会等到 probe 中所有的进程退出再结束。

区别导致的影响主要出现在 pod lifecycle 的 postStartHook 和 preStopHook 中，如果在 hook 中使用 exec probe 并且出现残留子进程的情况，在 containerd 的节点上可能会遇到 Pod 长期卡在 containerCreating 状态。原因是 kubelet 在 syncPod 时会逐个容器拉起，并执行 probe，如果某个 probe 因上述原因阻塞住，会导致后续容器无法启动。

在 ExecProbe 中拉起子进程并退出父进程属于 K8S 中未定义的行为，具体表现可能会和运行时版本、种类相关，因此建议尽量不要在 probe 执行过于复杂的操作。

## 容器网络的区别

在正常情况下，Pod 中的容器会共享同一个 Network Namespace，因此 Pod 需要在创建 Sandbox 容器时将网络准备好。为了更好的说明区别，我们简单介绍下 Pod 网络初始化的流程：

1. kubelet 调用 CRI Runtime（dockershim 或 containerd）创建 Pod 的 Sandbox 容器。
2. CRI Runtime 调用底层 docker 或 containerd 创建 pause 容器（此时 pause 进程还没启动，但已经初始化 Network Namespace）。
3. CRI Runtime 调用 CNI 执行在 Network Namespace 中创建 veth 并加入 cbr0 网桥等网络初始化操作。
4. CRI Runtime 启动 pause 容器，pause 进程被拉起。
5. kubelet 继续调用 CRI Runtime 执行创建容器等后续操作。

Docker 和 containerd 在**创建 pause 容器并初始化 Network Namespace**和 **调用 CNI 初始化 veth** 这两步有区别。

### 创建 pause 容器

Containerd 是为了 kubernetes 设计的 CRI Runtime，没有独立的网络模块；但 Docker 在设计时带有自己的网络功能的，因此 docker 在创建 Pause 容器时，会进行 Docker 特有的网络设置。该设置导致和 Containerd 最大的区别是在不使用 IPv6 的情况下，Docker 会将容器 Network Namespace 中内核参数`net.ipv6.conf.all.disable_ipv6` 设置为1，也即关闭容器内的 ipv6 选项。

**同样的 Pod 在 Docker 的节点上只开启了 IPv4，而在 Containerd 的节点上会同时开启 IPv4 和 IPv6。**

同时开启 IPv4 和 IPv6 的情况中，DNS 解析可能会同时发出v4、v6两个版本的包。在某些情况，业务如果需要频繁进行 DNS 解析，可能会触发 DNS 解析库的 Bug（取决于 Pod 业务的实现时的依赖）。在 Containerd 节点上，可以通过给 Pod 添加 init container 来针对 Pod 关闭 IPv6 设置。代码如下： 

``` yaml
apiVersion: v1
kind: Pod
...
spec:
  initContainers:
  - image: busybox
    name: sysctl
    command: ["sysctl", "-w", "net.ipv6.conf.all.disable_ipv6=1"]
    securityContext:
      privileged: true
...
```

### 调用 CNI 

两者在调用 CNI 上没有实质区别。

| 对比项         | Docker                                                       | Containerd                                                   |
| :------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 谁负责调用 CNI | Kubelet 内部的 docker-shim                                   | Containerd 内置的 cri-plugin                                 |
| 如何配置 CNI   | Kubelet 参数 <code>--cni-bin-dir</code> 和 <code>--cni-conf-dir</code> | Containerd 配置文件（toml）：<br> <code>[plugins.cri.cni]</code><br>    <code>bin\_dir = "/opt/cni/bin"</code><br>    <code>conf\_dir = "/etc/cni/net.d"</code> |

## 容器日志的区别

<table>
	<tr>
	<th style="width:10%;">对比项</th>
	<th>Docker</th>
	<th>Containerd</th>
	</tr>
	<tr>
		<td>存储路径</td>
		<td>
	如果 Docker 作为 K8S 容器运行时，容器日志的落盘将由 docker 来完成，保存在类似<code>/var/lib/docker/containers/$CONTAINERID</code> 目录下。Kubelet 会在 <code>/var/log/pods</code> 和 <code>/var/log/containers</code> 下面建立软链接，指向 <code>/var/lib/docker/containers/$CONTAINERID</code> 该目录下的容器日志文件。
		</td>
		<td>
		如果 Containerd 作为 K8S 容器运行时， 容器日志的落盘由 Kubelet 来完成，保存至 <code>/var/log/pods/$CONTAINER_NAME</code> 目录下，同时在 <code>/var/log/containers</code> 目录下创建软链接，指向日志文件。             
		</td>
	</tr>
  <tr>
    <td>存储大小</td>
    <td>Pod中的每个容器，docker默认会保留 100MB*10 = 1G 日志</td>
    <td>Pod中的每个容器，containerd默认会保留 10MB*5 = 50MB 日志</td>
  </tr>
	<tr>
		<td>配置参数 </td>
		<td>
		在 docker 配置文件中指定：
		<br>    <code>"log-driver": "json-file",</code> 
		<br>    <code>"log-opts": {"max-size": "100m","max-file": "5"}</code>
		</td>
		<td>
		<ul>
		<li>
		方法一：在 kubelet 参数中指定： <br> <code>--container-log-max-files=5<br> --container-log-max-size="100Mi"</code> <br>
		</li>
		<li>方法二：在 KubeletConfiguration 中指定：<br>    <code>"containerLogMaxSize": "100Mi",</code><br>    <code>"containerLogMaxFiles": 5, </code>
		</li>
		</ul>
		</td>
	</tr>
	<tr>
	<td>把容器日志保存到数据盘</td>
	<td>把数据盘挂载到 “data-root”（缺省是 <code>/var/lib/docker</code>）即可。</td>
	<td>创建一个软链接 <code>/var/log/pods</code> 指向数据盘挂载点下的某个目录。  <br>在 TKE 中选择“将容器和镜像存储在数据盘”，会自动创建软链接 <code>/var/log/pods</code>。
	</td>
	</tr>
</table>
