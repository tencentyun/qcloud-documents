


## 前提条件

- 已登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)。
- 集群内已 [部署 NginxIngress 组件](https://cloud.tencent.com/document/product/457/50503#Nginx-ingress)。
- 已安装并创建业务需要的 Nginx-ingress 实例。



## 使用方法

### Nginx-ingress 控制台操作指引

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群管理页面。
3. 单击已安装 Nginx-ingress 组件的集群 ID，进入集群管理页面。
4. 选择**服务与路由** > **Ingress**，进入 Ingress 信息页面。
5. 单击**新建**，进入“新建Ingress”页面。
6. 根据实际需求，设置 Ingress 参数。如下图所示：
![](https://main.qcloudimg.com/raw/5d7e5c0b032db515d8d11479f11b4739.png)
 - Ingress类型：选择**IngressController**。
 - 转发规则：需自行设置。
 - Annotation：设置注解，可配置的注解可参见 [为 Nginx 类型 Ingress 对象配置注解](#annotation)。
7. 单击**创建Ingress**即可。






### Kubectl 操作 Nginx-ingress 指引


在 Kubernetes 中引入 IngressClass 资源和 ingressClassName 字段之前，Ingress 类由 Ingress 中的 `kubernetes.io/ingress.class` 注解指定。
示例如下：

```
metadata:
  name: 
  annotations:
    kubernetes.io/ingress.class: "nginx-pulic". ## 对应 TKE 集群 Nginx-ingress 组件中的 Nginx-ingress 实例名称
```


## 相关操作[](id:annotation)

为 Nginx 类型 Ingress 对象可配置注解，详情可参见 [官方文档](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)。

### Nginx-ingress 对象使用模型

当多个 Ingress 对象作用于一个 Nginx 实体时：
- 按 CreationTimestamp 字段对 Ingress 规则排序，即先按旧规则。
- 如果在多个 Ingress 中为同一主机定义了相同路径，则最早的规则将获胜。
- 如果多个 Ingress 包含同一主机的 TLS 部分，则最早的规则将获胜。
- 如果多个 Ingress 定义了一个影响 Server 块配置的注释，则最早的规则将获胜。
- 按每个 hostname 创建 NGINX Server。
- 如果多个 Ingress 为同一 host 定义了不同的路径，则 ingress-controller 合并这些定义。
- 多个 Ingress 可以定义不同的注释。这些定义在 Ingress 之间不共享。
- Ingress 的注释将应用于 Ingress 中的所有路径。

### 触发更新 nginx.conf 机制

以下内容描述了需要重新加载 nginx.conf 的情况：
- 创建新的 ingress 对象。
- 为 Ingress 添加新的 TLS。
- Ingress 注解的更改不仅影响上游配置，而且影响更大。例如 load-balance 注释不需要重新加载。
- 为 Ingress 添加/删除路径。
- 删除 Ingress、Ingress 的 Service、Secret。
- Ingress 关联的对象状态不可知，例如 Service 或 Secret。
- 更新 Secret。
