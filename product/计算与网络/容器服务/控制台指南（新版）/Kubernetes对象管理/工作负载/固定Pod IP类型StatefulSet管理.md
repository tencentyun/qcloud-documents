## 创建固定IP类型StatefulSet

### 固定IP类型StatefulSet说明

如果您存在业务在TKE中部署，并存在固定Pod IP的述求， 您可以使用固定IP类型的StatefulSet。 腾讯云容器服务提供扩展的StatefulSet固定IP能力， 该类型的StatefulSet创建的Pod将通过弹性网卡分配真实的VPC内的IP地址， 腾讯云容器服务VPC-CNI的插件负责IP分配，当Pod重启或迁移，可实现IP地址不变。

### 固定IP类型StatefulSet应用场景

您可以通过创建固定IP类型StatefulSet来满足类似以下场景：

1. 通过来源IP授权

2. 基于IP做流程审核

3. 基于Pod IP做日志查询等

### 固定IP类型StatefulSet使用限制

1. 集群内必须开启了VPC-CNI模式网络， 详情见[集群开启VPC-CNI模式网络]()

2. 支持StatefulSet生命周期内固定ip

### 固定IP类型StatefulSet使用方法

前置条件需要集群内开启了VPC-CNI模式网络， 详情见[集群开启VPC-CNI模式网络]()

#### 控制台使用

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)。

2. 在左侧导航栏中，单击【集群】，进入集群管理页面。点击【基本信息】。

3. 单击需要创建 StatefulSet 的集群 ID，进入待创建 StatefulSet 的集群管理页面。

4. 根据实际需求，设置 StatefulSet 参数。关键参数信息如下：
   
   ![创建StatefulSet](https://main.qcloudimg.com/raw/2a5bf4e7b3e5c85c62fef2b7b09e02f3.png)
-  高级设置-网络模式-使用VPC-CNI模式
- ip地址范围：当前仅支持随机
- 固定pod ip:  开启 

#### Yaml创建

YAML示例：

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

- metadata.annotations：创建固定IP的StatefulSet您需要设置`tke.cloud.tencent.com/enable-static-ip`annotations

- spec.template.annotations：创建VPC-CNI模式的Pod您需要设置`tke.cloud.tencent.com/networks`annotations为tke-route-eni

- spec.template.spec.containers.0.resources：创建VPC-CNI模式的Pod您需要设置添加requests和limits限制`tke.cloud.tencent.com/eni-ip`
