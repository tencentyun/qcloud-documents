## 运行时组件说明
容器运行时（Container Runtime）是 Kubernetes 最重要的组件之一，负责真正管理镜像和容器的生命周期。Kubelet 通过 `Container Runtime Interface (CRI)` 与容器运行时交互，以管理镜像和容器。

TKE 支持用户选择 contaierd 和 docker 作为运行时组件：
containerd 调用链更短，组件更少,  更稳定，占用节点资源更少。 建议选择 containerd， 除以下情况需要选择 docker 作为运行时组件。
- 如需使用 docker in docker，请选择 docker。
- 如需在 TKE 节点使用 docker build/push/save/load 等命令， 请选择 docker。
- 如需调用 docker API， 请选择 docker。
- 如需 docker compose 或 docker swarm，请选择 docker。

更多详细对比见下文：

## Containerd 和 Docker 组件常用命令
containerd 不支持 docker API 和 docker CLI，但是可以通过 cri-tool 实现类似的功能。

| 镜像相关功能   | docker         | containerd      |
|:-------- |:-------------- |:--------------- |
| 显示本地镜像列表 | docker images  | crictl ps       |
| 下载镜像     | docker pull    | crictl pull     |
| 上传镜像     | docke push     | 无               |
| 删除本地镜像   | docker rmi     | crictl rmi      |
| 查看镜像详情   | docker inspect | crictl inspecti |

---

| 容器相关功能 | docker         | containerd     |
|:------ |:-------------- |:-------------- |
| 显示容器列表 | docker ps      | crictl ps      |
| 创建容器   | docker create  | crtctl create  |
| 启动容器   | docker start   | crtctl start   |
| 停止容器   | docker stop    | crictl stop    |
| 删除容器   | docker rm      | crictl rm      |
| 查看容器详情 | docker inspect | crictl inspect |
| attach | docker attach  | crictl attach  |
| exec   | docker exec    | crictl exec    |
| logs   | docker logs    | crictl logs    |
| stats  | docker stats   | crictl stats   |

---

| POD 相关功能 | docker | containerd      |
|:------- |:------ |:--------------- |
| 显示 POD 列表 | 无      | crictl pods     |
| 查看 POD 详情 | 无      | crictl inspectp |
| 运行 POD   | 无      | crictl runp     |
| 停止 POD   | 无      | crictl stopp    |

## 调用链说明
`kubelet --> docker shim （在 kubelet 进程中） --> dockerd --> containerd`

`kubelet --> cri plugin（在 containerd 进程中） --> containerd`

其中 dockerd 增加了 swarm cluster、 docker build 、 docker api 等能力，同时也会引入而外的 bug，多了一层调用。

## 其他差异
### 容器日志及相关参数

| 对比项         | docker         | containerd       |
|:----------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 存储路径        | docker 作为 k8s 容器运行时的情况下，容器日志的落盘由 docker 来完成， 保存在类似 `/var/lib/docker/containers/$CONTAINERID` 目录下。kubelet 会在 `/var/log/pods` 和 `/var/log/containers` 下面建立软链接，指向 `/var/lib/docker/containers/$CONTAINERID` 目录下的容器日志文件。 | containerd 作为 k8s 容器运行时的情况下， 容器日志的落盘由 kubelet 来完成，保存到 `/var/log/pods/$CONTAINER_NAME` 目录下，同时在 `/var/log/containers` 目录下创建软链接，指向日志文件。                                                                      |
| 配置参数        | 在 docker 配置文件中指定：<br>    "log-driver": "json-file", <br>    "log-opts": {"max-size": "100m","max-file": "5"}                                                                                            | 方法一：在 kubelet 参数中指定： <br> --container-log-max-files=5 --container-log-max-size="100Mi" <br>方法二：在 KubeletConfiguration 中指定：<br>    "containerLogMaxSize": "100Mi",<br>    "containerLogMaxFiles": 5, |
| 把容器日志保存到数据盘 | 把数据盘挂载到“data-root”（缺省是 /var/lib/docker）即可                                                                                                                                                              | 创建一个软链接 /var/log/pods 指向数据盘挂载点下的某个目录 <br>在 TKE 中选择“将容器和镜像存储在数据盘”，会自动创建软链接 /var/log/pods                                                                                                              |

### stream server
kubectl exec/logs 等命令需要在 apiserver 跟容器运行时之间建立流转发通道。
docker API 本身提供 stream 服务，kubelet 内部的 docker-shim 会通过 docker API 做流转发。
containerd 的 stream 服务需要单独配置：
```
[plugins.cri]
  stream_server_address = "127.0.0.1"
  stream_server_port = "0"
  enable_tls_streaming = false
```
在 k8s 1.11 之前，kubelet 并不会做 stream proxy，只会做 redirect。也就是把 containerd 暴露的 stream server 地址告诉 apiserver，让 apiserver 直接来访问 containerd 的 stream server。这种情况下，需要给 stream server 使能 tle 认证来做安全防护。
从 k8s1.11 引入了 [kubelet stream proxy](https://github.com/kubernetes/kubernetes/pull/64006)， 从而使得 containerd stream server 只需要监听本地地址即可。

#### CNI网络

| 对比项      | docker            | containerd                                                                                                       |
|:-------- |:---------------------------------------- |:---------------------------------------------------------------------------------------------------------------- |
| 谁负责调用 CNI | kubelet 内部的 docker-shim                    | containerd 内置的 cri-plugin（containerd 1.1以后）                                                                        |
| 如何配置 CNI  | kubele t参数 --cni-bin-dir 和 --cni-conf-dir | containerd 配置文件（toml）：<br> [plugins.cri.cni]<br>    bin\_dir = "/opt/cni/bin"<br>    conf\_dir = "/etc/cni/net.d" |
