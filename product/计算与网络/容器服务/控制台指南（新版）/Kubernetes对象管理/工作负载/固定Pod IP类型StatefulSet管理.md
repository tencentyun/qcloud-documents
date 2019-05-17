### 简介

如果您存在业务需要在 TKE 中部署，并存在固定 Pod IP 的述求， 您可以使用固定 IP 类型的 StatefulSet。 腾讯云容器服务提供扩展的 StatefulSet 固定 IP 能力，该类型的 StatefulSet 创建的 Pod 将通过弹性网卡分配真实的 VPC 内的 IP 地址。腾讯云容器服务 VPC-CNI 的插件负责 IP 分配，当 Pod 重启或迁移，可实现 IP 地址不变。

### 应用场景

您可以通过创建固定 IP 类型 StatefulSet 来满足类似以下场景：
- 通过来源 IP 授权。
- 基于 IP 做流程审核。
- 基于 Pod IP 做日志查询等。

### 使用限制

- 集群内必须开启了 VPC-CNI 模式网络， 详情请参考 [集群开启 VPC-CNI 模式网络](https://cloud.tencent.com/document/product/457/34993)。
- 支持 StatefulSet 生命周期内固定 IP。

### 使用方法

前提条件需要集群内开启了 VPC-CNI 模式网络， 详情请参考 [集群开启VPC-CNI模式网络](https://cloud.tencent.com/document/product/457/34993)。

### 创建固定 IP 类型 StatefulSet

#### 控制台使用
1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。
2. 在左侧导航栏中，单击【集群】。
3. 选择需要查看的集群ID/名称，进入该集群的管理页面。
4. 选择 【工作负载】>【StatefulSet】，进入【StatefulSet】的集群管理页面。
5. 单击【新建】，查看【实例数量】。如下图所示：
![](https://main.qcloudimg.com/raw/2dbd219d6bd76b8fe90971390daacc3c.png)
6. 单击【显示高级设置】，根据您实际需求，设置【StatefulSet】参数。 关键参数信息如下：
   ![创建StatefulSet](https://main.qcloudimg.com/raw/2a5bf4e7b3e5c85c62fef2b7b09e02f3.png)
 - 网络模式：勾选【使用 VPC-CNI 模式】。
 - IP 地址范围：当前仅支持随机。
 - 固定 Pod IP：开启。

#### Yaml 示例

```yaml

apiVersion: apps/v1beta1

kind: StatefulSet

metadata:

annotations:

tke.cloud.tencent.com/enable-static-ip: "true"

name: busybox

spec:

serviceName: "busybox"

replicas: 3

template:

metadata:

annotations:

tke.cloud.tencent.com/networks: "tke-route-eni"

labels:

app: busybox

spec:

terminationGracePeriodSeconds: 0

containers:

- name: busybox

image: busybox

command: ["sleep", "10000000000"]

resources:

requests:

tke.cloud.tencent.com/eni-ip: "1"

limits:

tke.cloud.tencent.com/eni-ip: "1"
```

- metadata.annotations：创建固定 IP 的 StatefulSet，您需要设置`tke.cloud.tencent.com/enable-static-ip`annotations
- spec.template.annotations：创建 VPC-CNI 模式的 Pod，您需要设置`tke.cloud.tencent.com/networks`annotations为`tke-route-eni`
- spec.template.spec.containers.0.resources：创建 VPC-CNI 模式的 Pod，您需要添加 requests 和 limits 限制`tke.cloud.tencent.com/eni-ip`
