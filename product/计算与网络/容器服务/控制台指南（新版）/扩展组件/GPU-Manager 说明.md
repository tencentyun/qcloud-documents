
## 简介

### 组件介绍

GPU Manager 提供一个 All-in-One 的 GPU 管理器，基于 Kubernetes DevicePlugin 插件系统实现，该管理器提供了分配并共享 GPU、GPU 指标查询、容器运行前的 GPU 相关设备准备等功能，支持用户在 Kubernetes 集群中使用 GPU 设备。

### 组件功能
- **拓扑分配**：提供基于 GPU 拓扑分配功能，当用户分配超过1张 GPU 卡的应用，可以选择拓扑连接最快的方式分配 GPU 设备。
- **GPU 共享**：允许用户提交小于1张卡资源的任务，并提供 QoS 保证。
- **应用 GPU 指标的查询**：用户可以访问主机端口（默认为 5678）的 `/metric` 路径，可以为 Prometheus 提供 GPU 指标的收集功能，访问 `/usage` 路径可以进行可读性的容器状况查询。

### 部署在集群内的 Kubernetes 对象


| Kubernetes 对象名称        | 类型         | 建议预留资源 | 所属 Namespaces |
| --------------------- | ---------- | ------ | ------------ |
| gpu-manager-daemonset | DaemonSet  | 每节点1核 CPU, 1Gi内存     | kube-system  |
| gpu-quota-admission   | Deployment | 每节点1核 CPU, 1Gi内存      | kube-system  |

## 使用场景

在 Kubernetes 集群中运行 GPU 应用时，可以解决 AI 训练等场景中申请独立卡造成资源浪费的情况，让计算资源得到充分利用。

## 限制条件
- 该组件基于 Kubernetes DevicePlugin 实现，可直接在 Kubernetes 1.10 以上版本的集群使用。
-  每张 GPU 卡一共有100个单位的资源，仅支持0 - 1的小数卡，以及1的倍数的整数卡设置。显存资源是以256MiB为最小的一个单位的分配显存。
- 使用 GPU-Manager 要求集群内包含 GPU 机型节点。



## 使用方法

### 组件安装
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，在左侧导航栏中选择**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 GpuManager。
5. 单击**完成**即可创建组件。



### 创建细粒度的 GPU 工作负载
当 GpuManager 组件成功安装后，您可通过以下两种方式创建细粒度的 GPU 工作负载。

#### 方式一：通过 TKE 控制台创建
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择需要创建 GPU 应用的集群，进入工作负载管理页，并单击**新建**。
3. 在“新建Workload”页面根据实际需求进行配置，可在“GPU资源”配置细粒度的 GPU 工作负载。如下图所示：
![](https://main.qcloudimg.com/raw/044d6ab9a8c17611f761024c26b6dfde.png)

#### 方式二：通过 yaml 创建
>?在提交时通过 yaml 为容器设置 GPU 的使用资源，核资源需要在 resource 上填写 `tencent.com/vcuda-core`，显存资源需要在 resource 上填写 `tencent.com/vcuda-memory`。

下面给出 yaml 示例：
- 使用1张卡的 P4 设备：
```
apiVersion: v1
kind: Pod
...
spec:
containers:
 - name: gpu
resources:
tencent.com/vcuda-core: 100
```
- 使用0.3张卡，5GiB 显存的应用：
```
apiVersion: v1
kind: Pod
...
spec:
containers:
 - name: gpu
resources:
tencent.com/vcuda-core: 30
tencent.com/vcuda-memory: 20
```

