## 操作场景

您可以通过 API 网关直接接入TKE 集群的 Pod，不需要经过 CLB。本文档指导您通过控制台创建 TKE 通道，并在 API 的后端中，配置后端类型为 TKE 通道，让 API 网关的请求，直接转到 TKE 通道的对应的 Pod 上。

**功能优势**
- API 网关直接连接 TKE 集群的 Pod，减少中间节点（例如 CLB）。
- 一个 TKE 通道可以同时对接多个 TKE 集群。

>?目前仅在**专享**类型的 API 网关上支持 TKE 通道。

## 前提条件
1. 已有专享型的服务。
2. 已有容器服务 TKE 的集群，并且已获取集群 Admin 角色。

## 操作步骤
### 步骤1：创建 TKE 通道

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index)。
2. 在左侧导航栏选择**后端通道**，单击**新建**。
3. 在新建后端通道页面填写以下信息： 
   - 后端通道名称：输入后端通道名称
   - 通道类型：选择**容器通道**
   - 私有网络：选择私有网络 VPC
   - 协议：选择所需协议
   - Host Header：可选项，Host Header 是 API 网关访问后端服务时候，HTTP/HTTPS 请求中，携带的请求 HEADER 中 Host 的值。
   - 服务列表：服务列表中配置多个服务，服务数量上限为20个, 多个 Pod 之间采用加权轮询算法分配流量。单个服务配置的步骤如下：
     1. 填写服务的每个 Pod 的权重占比。
     2. 选择容器服务类型，支持容器服务TKE、弹性容器服务EKS；
     3. 选择集群，如果集群还未授权，API 网关会请求授权。如已在容器集群中完成授权，可点击重试。直至提示”已授权API网关“；
     4. 选择集群的命名空间。
     5. 选择服务和服务的端口。
     6. 高级可选项：额外节点 Label。
   - 健康检查：可勾选主动健康检查、被动健康检查、设置异常恢复时间。
   - 标签：可选项，标签用于从不同维度对资源分类管理。

一个完整的 TKE 通道配置如下：

<img src="https://qcloudimg.tencent-cloud.cn/raw/9f3e5683e3777384076f5c8f9e29178e.png" width=900/>


### 步骤2：API 后端对接 TKE 通道
1. 在 API 网关控制台的 [服务](https://console.cloud.tencent.com/apigateway/service)页面，选择专享实例的服务、单击第1列服务名的“ServiceID”，进入管理 API 页面。
2. 单击**新建**，API类型选择通用 API。
3. 输入前端配置，然后单击**下一步**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/20cc8d5bee0ccd021125ae9e1a6d0017.png" width=900/>
4. 选择后端类型为 **VPC内资源**，选择VPC信息，选择对接方式。
5. 选择后端通道类型为 **容器通道**，选择通道、设置后端路径。
6. 单击**下一步**。  
	<img src="https://qcloudimg.tencent-cloud.cn/raw/86a1083d2f03c574b946c775519040fa.png" width=900/>
5. 设置响应结果，并单击**完成**。

## 网络架构
TKE 通道被 API 绑定后，整个网络的架构如下：
	<img src="https://qcloudimg.tencent-cloud.cn/raw/ca04e628647d61f5b46e68e48a28dc7c.png" width=900/>
API 网关直接访问 容器集群 中的 Pod，不需要经过 CLB。因为在 容器集群 中，httpbin 的服务配置文件 YAML 如下，其中 selector 中，表示选择带有标签的Pod（其中标签键 app，标签值 httpbin）作为 容器通道 的节点。因此，version 为 v1/v2/v3 的 Pod 也都是 容器通道 的节点。
```yaml
apiVersion: v1
kind: Service
metadata:
  name: httpbin
  labels:
    app: httpbin
    service: httpbin
spec:
  ports:
  - name: http
    port: 8000
    targetPort: 80
  selector:
    app: httpbin
```

 

## 注意事项

- 一个 容器通道最多只能对接20个 TKE 服务。
- 用户需要授权获取 容器集群 的 Admin 角色。
- 容器通道和 API 网关的专享实例服务在**同一个 VPC** 下才能使用，目前 API 网关暂时不支持直接跨 VPC。
