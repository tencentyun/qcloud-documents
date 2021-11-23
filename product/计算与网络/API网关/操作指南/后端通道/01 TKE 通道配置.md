## 操作场景

您可以通过 API 网关直接接入TKE 集群的 Pod，不需要经过 CLB。本文档指导您如何操作 TKE 通道的创建和使用。

**产品优势**

1. API 网关直接连接 TKE 集群的 Pod，减少中间节点，比如 CLB。
2. 一个 TKE 通道可以同时对接多个 TKE 集群。

>  ? 目前仅在**专享**类型的 API 网关上支持 TKE 通道。

## 前提条件

已有容器服务 TKE 的集群，并且已获取集群 admin 角色。

## 操作步骤

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index)。
2. 在左侧导航栏选择**后端通道**，单击**新建**。
3. 点击**后端通道**，**后端通道**在API网关首页左边的侧边栏处。  
   - 后端通道名称：输入后端通道名称
   - 通道类型：选择**TKE通道**
   - 私有网络：选择私有网络VPC
   - 服务列表：服务列表中配置多个服务，服务数量上限为20个, 多个Pod之间采用加权轮训算法分配流量。单个服务配置的步骤如下：
     1. 填写服务的每个 Pod 的权重占比。
     2. 选择集群，如果集群还没授权，API 网关会请求授权。
     3. 选择集群内命名空间。
     4. 选择服务和服务的端口。
     5. 高级可选项：额外节点 Label。
   - 后端类型：选择 HTTP 或者 HTTPS。
   - Host Header：可选项，Host Header 是 API 网关访问后端服务时候，HTTP/HTTPS 请求中，携带的请求 HEADER 中 Host 的值。
   - 标签：可选项，标签用于从不同维度对资源分类管理。

一个完整的TKE通道配置如下：

![](https://qcloudimg.tencent-cloud.cn/raw/1091058afb38b1e33f3c6ec269b7dd4f.png)                         

 TKE 通道被 API 绑定后，整个网络的架构如下：

![](https://qcloudimg.tencent-cloud.cn/raw/ca04e628647d61f5b46e68e48a28dc7c.png)

API 网关直接访问 TKE 集群中的 Pod，不需要经过 CLB。因为在 TKE 集群中，httpbin 的服务配置文件 YAML 如下，其中 selector 中，表示选择带有标签键 app，标签值为 httpbin 的 Pod 作为 TKE 通道的节点。因此，version 为 v1/v2/v3 的 Pod 也都是 TKE 通道的节点。



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

 

## **注意事项**

1. 一个 TKE 通道最多只能对接20个 TKE 服务。
2. 用户需要拥有 TKE 集群的 admin 角色。
