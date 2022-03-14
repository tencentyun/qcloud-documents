## 简介

### 组件介绍

Node-Problem-Detector-Plus 是 Kubernetes 集群节点的健康监测组件。在容器服务 TKE 环境中以 DaemonSet 方式运行，帮助用户实时检测节点上的各种异常情况，并将检测结果报告给上游的 Kube-apiserver。

### 部署在集群内的 Kubernetes 对象



| kubernetes 对象名称   | 类型               | 资源量 |  Namespaces |
| --------------------- | ------------------ | ------------ | --------------- |
| node-problem-detector | DaemonSet          | 0.5C80M     | kube-system     |
| node-problem-detector | ServiceAccount     | -            | kube-system     |
| node-problem-detector | ClusterRole        | -            | -               |
| node-problem-detector | ClusterRoleBinding | -            | -               |

## 使用场景

使用 Node-Problem-Detector-Plus 组件可以监控节点的工作状态，包括内核死锁、OOM、系统线程数压力、系统文件描述符压力等指标，通过 Node Condition 和 Event 的形式上报给 Apiserver。
您可以通过检测相应的指标，提前预知节点的资源压力，可以在节点开始驱逐 Pod 之前手动释放或扩容节点资源压力，防止 Kubenetes 进行资源回收或节点不可用可能带来的损失。

## 限制条件
在集群中使用 NPD，需要在集群内安装该扩展组件，NPD 容器将被限制使用0.5核 CPU，80M内存的系统资源。


## 使用方法


1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 Node-Problem-Detector-Plus。
5. 单击**完成**即可创建组件。安装成功后，您的集群中会有对应的 node-problem-detector 资源，在 Node 的 Condition 中也会增加相应的条目。







## 附录
### Node Conditions

安装 NPD 插件后，会在节点中增加以下特定的 Conditions：

|Condition Type            | 默认值 | 描述                                                                     |
| ------------------------- | ------ | ------------------------------------------------------------------------ |
| ReadonlyFilesystem        | False  | 文件系统是否只读                                                         |
| FDPressure                | False  | 查看主机的文件描述符数量是否达到最大值的80%                             |
| FrequentKubeletRestart    | False  | Kubelet 是否在20Min内重启超过5次                                     |
| CorruptDockerOverlay2     | False  | DockerImage 是否存在问题                                                 |
| KubeletProblem            | False  | Kubelet service 是否 Running                                             |
| KernelDeadlock            | False  | 内核是否存在死锁                                                         |
| FrequentDockerRestart     | False  | Docker 是否在20Min内重启超过5次                                          |
| FrequentContainerdRestart | False  | Containerd 是否在20Min内重启超过5次                                      |
| DockerdProblem            | False  | Docker service 是否 Running（若节点运行时为 Containerd，则一直为 False） |
| ContainerdProblem         | False  | Containerd service 是否 Running（若节点运行时为 Docker，则一直为 False） |
| ThreadPressure            | False  | 系统目前线程数是否达到最大值的90%                                       |
| NetworkUnavailable        | False  | NTP service 是否 Running                                                |
| SerfFailed                | False  | 分布式检测节点网络健康状态                                               |
