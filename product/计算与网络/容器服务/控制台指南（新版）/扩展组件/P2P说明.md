## 简介

### 组件介绍
P2P Addon 是容器镜像服务 TCR 推出的基于 P2P 技术的容器镜像加速分发插件，可应用于大规模容器服务 TKE 集群快速拉取 GB 级容器镜像，支持上千节点的并发拉取。

该组件由 `p2p-agent`、`p2p-proxy` 和 `p2p-tracker` 组成：
- p2p-agent：部署在集群中每个节点上，代理每个节点的镜像拉取请求，并转发至 P2P 网络的各个 peer（node 节点）间。
- p2p-proxy：部署在集群部分节点上，作为原始种子连接被加速的镜像仓库。proxy 节点既需要做种，也需要从目标镜像仓库中拉取原始数据。
- p2p-tracker：部署在集群部分节点上，开源 bittorrent 协议的 tracker 服务。

### 部署在集群内的 Kubernetes 对象

| Kubernetes 对象名称 | 类型       | 请求资源                     | 所属 Namespace |
| :----------------- | ---------- | ---------------------------- | -------------- |
| p2p-agent          | DaemonSet  | 每个节点0.2核 CPU，0.2G内存 | kube-system    |
| p2p-proxy          | Deployment | 每个节点0.5核 CPU，0.5G内存   | kube-system    |
| p2p-tracker        | Deployment | 每个节点0.5核 CPU，0.5G内存   | kube-system    |
| p2p-proxy          | Service    | -                            | kube-system    |
| p2p-tracker        | Service    | -                            | kube-system    |
| agent              | Configmap  | -                            | kube-system    |
| proxy              | Configmap  | -                            | kube-system    |
| tracker            | Configmap  | -                            | kube-system    |

## 使用场景

应用于大规模 TKE 集群快速拉取 GB 级容器镜像，支持上千节点的并发拉取，推荐如下使用场景：
- 集群内具备节点500 - 1000台，使用本地盘存储拉取的容器镜像。此场景下，集群内节点最高可支持100MB/s的并发拉取速度。
- 集群内具备节点500 - 1000台，使用 CBS 云盘存储拉取的容器镜像，且集群所在地域为广州、北京、上海等国内主要地域。此场景下，集群内节点最高可支持20MB/s的并发拉取速度。

## 限制条件
- 在大规模集群内启用 P2P Addon 拉取容器镜像时，将对节点数据盘造成较高读写压力，可能影响集群内已有业务。若集群内节点使用 CBS 云盘存储拉取的容器镜像，请按照集群所在地域选择合适的下载限速或联系您的售后/架构师，避免因镜像拉取时云盘读写负载过高造成集群内现网业务中断现象，甚至影响该地域内其他用户的正常使用。
- 开启 P2P 插件需要预留一定的资源，P2P 组件在镜像加速拉取的过程中会占用节点的 CPU 和内存资源，加速结束后不再占用资源。其中：
 - Proxy 的 limit 限制为：4核 CPU 和4G 内存。
 - Agent 的 limit 限制为：4核 CPU 和2G 内存。
 - Tracker 的 limit 限制为：2核 CPU 和4G 内存。
- 需要根据集群的节点规模，估算启动的 Proxy 个数。Proxy 运行节点的最低配置为4C8G，内网带宽1.5GB/s，单个 Proxy 服务可支撑200个集群节点。
- 需要主动为 Proxy 和 Tracker 组件选择部署节点，使用方式为手动为节点打 K8S 标签，详情请参见 [使用方法](#Instructions)。Proxy 和 Agent 所在的节点需要能够访问的仓库源站。
- Agent 组件将会占用节点的5004端口，以及 P2P 专用通信端口6881（Agent）和6882（Proxy）。Agent、Proxy 组件会分别创建本地工作目录 `/p2p_agent_data` 和 `/p2p_proxy_data` 用于缓存容器镜像，请提前确认节点已预留足够的存储空间。





## 使用方法[](id:Instructions)
1. 选取合适的节点部署运行 Proxy 组件。
可通过 `kubectl label nodes XXXX proxy=p2p-proxy` 命令标记节点，插件安装时将自动在这些节点中部署该组件。安装后如果需要调整 Proxy 组件的个数，可在指定节点上添加或者删除该 label 后，修改集群中 kube-system 命名空间下 p2p-proxy 工作负载的副本个数。
2. 选取合适的节点部署运行 Tracker 组件。
可通过 `kubectl label nodes XXXX tracker=p2p-tracker` 命令标记节点，插件安装时将自动在这些节点中部署该组件。安装后如果需要调整 Tracker 的个数，可在指定节点上添加或者删除该 label 后，修改集群中 kube-system 命名空间下 p2p-tracker 工作负载的副本个数。
3. 节点安全组需要添加的配置为：入站规则放通 TCP 和 UDP 的30000 - 32768 端口、以及 VPC 内 IP 全放通。出站规则放通全部（TKE 集群 work 节点默认安全组已满足要求）。
4. 选择指定集群 [开启 P2P Addon 插件](#start)。填写需要加速的镜像仓库域名，节点拉取限速、Proxy 个数，Tracker 个数。安装后如果需要重新调整下载的最高速度，可修改 p2p-agent configmap 中的 downloadRate 和 uploadRate。
5. 在业务命名空间内创建拉取镜像所需的 dockercfg，其中仓库域名为 localhost:5004，用户名及密码即为目标镜像仓库的原有访问凭证。
6. 修改业务 YAML，将需要加速的镜像仓库域名地址修改为 localhost:5004，如 localhost:5004/p2p-test/test:1.0，并使用新建的 dockercfg 作为 ImagePullSecret。
7. 使用业务 YAML 部署更新工作负载，并实时观察镜像拉取速度及节点磁盘读写负载，及时调整节点的下载限速以达到最好加速效果。






## 操作步骤[](id:start)
1. 登录[ 容器服务控制台 ](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入“组件列表”页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 P2P。
5. 选择“参数配置”，在弹出的“P2P组件参数设置”窗口中，填写需要加速的镜像仓库域名、节点拉取限速、Proxy 个数及 Tracker 个数。如下图所示：
![](https://main.qcloudimg.com/raw/2651ee1a5d38d789a7675ce0c8bc614a.png)
