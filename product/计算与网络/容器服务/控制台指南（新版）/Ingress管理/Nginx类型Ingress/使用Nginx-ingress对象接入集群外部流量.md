


## 前置条件

- 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster?rid=1)。
- 集群内已 [部署 Nginx-ingress 组件](https://cloud.tencent.com/document/product/457/50503#Nginx-ingress)。
- 已安装并创建业务需要的 Nginx-ingress 实例。



## 使用方法

### Nginx-ingress 控制台操作指引

在已安装 Nginx-ingress 组件的集群中，进入 ingress 管理页面。

1. 创建 ingress
2. 选择 nginx-ingress 类型
3. 选择 ingressClass - 对应组件中的 ingress 实例
4. 设置转发规则
5. 设置注解 - 可配置的注解见下文。






### Kubectl 操作 Nginx-ingress 指引


#### kubernetes 集群在1.18 及以上版本

kubernetes 集群在1.18及以上版本采用了 IngressClass 资源来实现多种 Ingress 类型的资源选择。  
您在集群中安装 ingress-controller 实例时已自动根据您的参数配置创建了 IngressClass 资源，示例如下：
>! 您无需再在集群中安装下述资源。



您可以通过以下示例创建您的 Nginx 类型的 Ingress  对象

```yaml
piVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: example-ingress
spec:
  ingressClassName: external-lb ## 对应TKE集群 Nginx-ingress组件中的Nginx-ingress实例名称
  rules:
  - host: *.example.com
    http:
      paths:
      - path: /example
        pathType: Prefix
        backend:
          serviceName: example-service
          servicePort: 80

```


#### kubernetes 集群在1.18以下版本

在 Kubernetes 1.18 版本引入 IngressClass 资源和 ingressClassName 字段之前，Ingress 类由 Ingress 中的 `kubernetes.io/ingress.class` 注解指定。
示例如下：

```
metadata:
  name: 
  annotations:
    kubernetes.io/ingress.class: "nginx-pulic". ## 对应 TKE 集群 Nginx-ingress 组件中的 Nginx-ingress实例名称
```


## Nginx 类型的 ingress 对象可配置的注解

待补充几个常用注解

更多注解可查看[官方文档])(https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)


### Nginx-ingress 对象使用模型

多个 Ingress 对象作用于一个 Nginx 实体时：
1. 按 CreationTimestamp 字段对 Ingress 规则排序，即先按旧规则。
2. 如果在多个 Ingress 中为同一主机定义了相同路径，则最早的规则将获胜。
3. 如果多个 Ingress 包含同一主机的 TLS 部分，则最早的规则将获胜。
4. 如果多个 Ingress 定义了一个影响 Server 块配置的注释，则最早的规则将获胜。
5. 按每个 hostname 创建 NGINX Server。
6. 如果多个 Ingress 为同一 host 定义了不同的路径，则 ingress-controller 合并这些定义。
7. 多个 Ingress 可以定义不同的注释。这些定义在 Ingress 之间不共享。
8. Ingress 的注释将应用于 Ingress 中的所有路径。

### 触发更新 nginx.conf 机制

以下内容描述了需要重新加载 nginx.conf 的情况：
1. 创建新的 ingress 对象。
2. 为 Ingress 添加新的 TLS。
3. Ingress 注解的更改不仅影响上游配置，而且影响更大。例如 load-balance 注释不需要重新加载。
4. 为 Ingress 添加/删除路径。
5. 删除 Ingress、Ingress 的 Service、Secret。
6. Ingress 关联的对象状态不可知，例如 Service 或 Secret。
7. 更新 Secret。
