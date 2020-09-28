## 概述

如何在腾讯云 Kubernetes 集群实现蓝绿发布和灰度发布？通常要向集群额外部署其它开源工具来实现，比如 Nginx Ingress，Traefik 等，或者让业务上 Service Mesh（服务网格），利用服务网格的能力来实现。这些方案多多少少都是需要一点点门槛的，如果蓝绿发布或灰度发布的需求不复杂，同时不希望让集群引入更多的组件或复杂的用法，可以考虑使用本文的简单方案，利用 Kubernetes 原生的特性以及腾讯云 TKE/EKS 集群自带的 LB 插件实现简单的蓝绿发布和灰度发布。

>! 本文适用产品范围: TKE 集群、EKS 集群 (弹性集群)

## 原理介绍

我们通常使用 Deployment, StatefulSet 等 Kubernetes 自带的工作负载来部署业务，每个工作负载都管理一组 Pod，以 Deployment 为例:

<img style="width:450px" src="https://main.qcloudimg.com/raw/bcbda91a3bd75840afd4a23fbc136310.png" data-nonescope="true">

通常还会为每个工作负载创建对应的 Service，Service 通过 selector 来匹配后端 Pod，其它服务或者外部通过访问 Service 即可访问到后端 Pod 提供的服务。要对外暴露可以直接将 Service 类型设置为 LoadBalancer，LB 插件会自动为其创建 CLB (腾讯云负载均衡器) 作为流量入口。 

如何实现蓝绿发布？以 Deployment 为例，集群中部署两个不同版本的 Deployment，它们的 Pod 拥有共同的 label，但有一个 label 的值不同，用于区分不同的版本，Service 使用 selector 选中了其中一个版本的 Deployment 的 Pod，通过修改 Service 的 selector 中决定 服务版本的 label 的值来改变 Service 后端对应的 Deployment，实现让服务从一个版本直接切换到另一个版本，即蓝绿发布:

<img style="width:450px" src="https://main.qcloudimg.com/raw/f38aec8893abdcb311e05a132ec37440.png" data-nonescope="true">

如何实现灰度发布？虽然我们通常会为每个工作负载都创建一个 Service，但 Kubernetes 并没有限制 Service 一定要与工作负载一一对应，因为 Service 是通过 selector 来匹配后端 Pod 的，只要不同工作负载的 Pod 都能被相同 selector 选中，就可以实现一个 Service 对应多个版本的工作负载的效果，调整不同版本工作负载的副本数就相当于调整不同版本服务的权重，实现灰度发布:

<img style="width:450px" src="https://main.qcloudimg.com/raw/e271e9d585524b899807c6059afac03d.png" data-nonescope="true">

## 使用 YAML 创建资源

本文的示例将使用 yaml 的方式部署工作负载和创建 Service，有两种操作方式。

方式一：在 TKE 或 EKS 控制台右上角点击 `YAML 创建资源`，然后将本文示例的 yaml 粘贴进去:

<img style="width:450px" src="https://main.qcloudimg.com/raw/740c0597b6bc773b3664ca20f290c3e4.png" data-nonescope="true">

方式二：将示例的 yaml 保存成文件，然后使用 kubectl 指定 yaml 文件来创建，如: `kubectl apply -f xx.yaml` 。

## 部署多版本工作负载

要实现蓝绿发布或灰度发布，首先我们需要在集群中部署多个版本的工作负载，这里以简单的 nginx 为例，部署第一个版本:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
      version: v1
  template:
    metadata:
      labels:
        app: nginx
        version: v1
    spec:
      containers:
      - name: nginx
        image: "openresty/openresty:centos"
        ports:
        - name: http
          protocol: TCP
          containerPort: 80
        volumeMounts:
        - mountPath: /usr/local/openresty/nginx/conf/nginx.conf
          name: config
          subPath: nginx.conf
      volumes:
      - name: config
        configMap:
          name: nginx-v1

---

apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: nginx
    version: v1
  name: nginx-v1
data:
  nginx.conf: |-
    worker_processes  1;

    events {
        accept_mutex on;
        multi_accept on;
        use epoll;
        worker_connections  1024;
    }

    http {
        ignore_invalid_headers off;
        server {
            listen 80;
            location / {
                access_by_lua '
                    local header_str = ngx.say("nginx-v1")
                ';
            }
        }
    }
```

再部署第二个版本:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-v2
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
      version: v2
  template:
    metadata:
      labels:
        app: nginx
        version: v2
    spec:
      containers:
      - name: nginx
        image: "openresty/openresty:centos"
        ports:
        - name: http
          protocol: TCP
          containerPort: 80
        volumeMounts:
        - mountPath: /usr/local/openresty/nginx/conf/nginx.conf
          name: config
          subPath: nginx.conf
      volumes:
      - name: config
        configMap:
          name: nginx-v2
---

apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: nginx
    version: v2
  name: nginx-v2
data:
  nginx.conf: |-
    worker_processes  1;

    events {
        accept_mutex on;
        multi_accept on;
        use epoll;
        worker_connections  1024;
    }

    http {
        ignore_invalid_headers off;
        server {
            listen 80;
            location / {
                access_by_lua '
                    local header_str = ngx.say("nginx-v2")
                ';
            }
        }
    }
```

可以在控制台看到部署的情况:

<img style="width:450px" src="https://main.qcloudimg.com/raw/4d3411bb5f9301d4ff8bee25066c64be.png" data-nonescope="true">

## 实现蓝绿发布

为我们部署的 Deployment 创建 LoadBalancer 类型的 Service 对外暴露服务，指定使用 v1 版本的服务:

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: LoadBalancer
  ports:
  - port: 80
    protocol: TCP
    name: http
  selector:
    app: nginx
    version: v1
```

测试访问:

``` bash
$ for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
```

全是 v1 版本的响应，现在我们切到 v2 版本，修改 Service 的 selector，让它选中 v2 版本的服务，如果在控制台改，先找到对应 Service，点击 `编辑YAML`:

<img style="width:450px" src="https://main.qcloudimg.com/raw/589a6704d1e13d77da8795f8b97ab94c.png" data-nonescope="true">

修改 selector 部分:

``` yaml
  selector:
    app: nginx
    version: v2
```

或者也可以直接用 kubectl 修改:

``` bash
kubectl patch service nginx -p '{"spec":{"selector":{"version":"v2"}}}'
```

再次测试访问:

``` bash
$ for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
nginx-v2
nginx-v2
nginx-v2
nginx-v2
nginx-v2
nginx-v2
nginx-v2
nginx-v2
nginx-v2
nginx-v2
```

全是 v2 版本的响应，成功实现了蓝绿发布。

## 实现灰度发布

相比蓝绿发布，我们为不给 Service 指定使用 v1 版本的服务，从 selector 中删除 `version` 标签，让 Service 同时选中两个版本的 Deployment 的 Pod:

``` yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: LoadBalancer
  ports:
  - port: 80
    protocol: TCP
    name: http
  selector:
    app: nginx
```

测试访问:

``` yaml
$ for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
nginx-v1
nginx-v1
nginx-v2
nginx-v2
nginx-v2
nginx-v1
nginx-v1
nginx-v1
nginx-v2
nginx-v2
```

可以看到，一半是 v1 版本的响应，另一半是 v2 版本的响应。现在我们来调节 v1 和 v2 版本的 Deployment 的副本，将 v1 版本调至 1 个副本，v2 版本调至 4 个副本。

可以通过控制台操作:

<img style="width:450px" src="https://main.qcloudimg.com/raw/5b2484c9d2b0f22cece721f31fe873f7.png" data-nonescope="true">

也可以通过 kubectl 操作:

``` bash
kubectl scale deployment/nginx-v1 --replicas=1
kubectl scale deployment/nginx-v2 --replicas=4
```

然后再次进行访问测试:

``` bash
$ for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
nginx-v2
nginx-v1
nginx-v2
nginx-v2
nginx-v2
nginx-v2
nginx-v1
nginx-v2
nginx-v2
nginx-v2
```

可以看到，10 次访问中只有 2 次返回了 v1 版本，v1 与 v2 的响应比例与其副本数比例一致，为 1:4，通过控制不同版本服务的副本数就实现了灰度发布。

## 总结

本文我们介绍了如何在有限的条件下在 Kubernetes 集群中实现简单的蓝绿发布与灰度发布，对于一些简单的发布需求场景可以考虑使用这种方案。