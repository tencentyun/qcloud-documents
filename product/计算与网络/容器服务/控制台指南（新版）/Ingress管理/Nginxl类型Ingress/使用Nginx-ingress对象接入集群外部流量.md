## 使用Nginx-ingress对象接入集群外部流量 

### 前置条件
1. 集群内必须部署nginx-ingress组件
2. 已安装并创建业务需要的nginx-ingress实例



### 使用方法
#### 控制台使用
在已安装nginx-ingress组件的集群中，进入ingress管理页面
1. 创建ingress
2. 选择nginx-ingress类型
3. 选择ingressClass - 对应组件中的ingress实例
4. 设置转发规则
5. 设置注解 - 可配置的注解见下文。

#### Yaml使用
##### kubernetes集群在1.18及以上版本
kubernetes集群在1.18及以上版本采用了IngressClass资源来实现多种ingress 类型的资源选择。  
您在集群中安装ingress-controller实例时已自动根据您的参数配置创建了IngressClass资源，示例如下：
注：您无需再在集群中安装下述资源

注：yaml待更新
```yaml
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb  ## 对应TKE集群 Nginx-ingress组件中的Nginx-ingress实例名称
spec:
  controller: example.com/ingress-controller
  parameters:
    apiGroup: k8s.example.com
    kind: IngressParameters
    name: external-lb
```

您可以通过以下示例创建您的nginx类型的ingress对象

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


##### kubernetes集群在1.18以下版本
在 Kubernetes 1.18 版本引入 IngressClass 资源和 ingressClassName 字段之前， Ingress 类是通过 Ingress 中的一个 kubernetes.io/ingress.class 注解来指定的。
示例如下：
```
metadata:
  name: foo
  annotations:
    kubernetes.io/ingress.class: "nginx-pulic". ## 对应TKE集群 Nginx-ingress组件中的Nginx-ingress实例名称
```


### Nginx类型的ingress对象可配置的注解

待补充几个常用注解

更多注解可查看[官方文档])(https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)


### Nginx-ingress对象使用模型
多个ingress对象作用于一个Nginx实体时：
1. 按CreationTimestamp字段对Ingress规则排序，即先按旧规则。
2. 如果在多个Ingress中为同一主机定义了相同路径，则最早的规则将获胜。
3. 如果多个Ingress包含同一主机的TLS部分，则最早的规则将获胜。
4. 如果多个Ingress定义了一个影响Server块配置的注释，则最早的规则将获胜。
5. 按每个hostname创建NGINX Server
6. 如果多个ingress为同一host定义了不同的路径，则ingress-controller合并这些定义。
7. 多个Ingress可以定义不同的注释。这些定义在Ingress之间不共享。
8. ingress的注释将应用于Ingress中的所有路径。

### 触发更新nginx.conf的机制
下面的列表描述了需要重新加载nginx.conf的情况：
1. 创建新的ingress对象。
2. 为ingress添加新的TLS。
3. Ingress注解的更改不仅影响上游配置，而且影响更大。例如load-balance注释不需要重新加载。
4. 为Ingress添加/删除路径。
5. 删除ingress，ingress的service，secret。
6. ingress关联的对象状态不可知，例如Service或Secret。
7. 更新secret。