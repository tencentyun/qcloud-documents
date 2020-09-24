## 概述

本文将介绍如何使用 Nginx Ingress 实现金丝雀发布，从使用场景分析，到用法详解，再到上手实践。

## 前提条件

集群中需要部署 Nginx Ingress 作为 Ingress Controller，并且对外暴露了统一的流量入口，参考 [在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293)。

## Nginx Ingress 可以用在哪些发布场景 ?

使用 Nginx Ingress 来实现金丝雀发布，可以用在哪些场景呢？这个主要看使用什么策略进行流量切分，目前 Nginx Ingress 支持基于 Header、Cookie 和服务权重这 3 种流量切分的策略，基于它们可以实现以下两种发布场景。

### 场景一: 将新版本灰度给部分用户

假设线上运行了一套对外提供 7 层服务的 Service A 服务，后来开发了个新版本 Service A' 想要上线，但又不想直接替换掉原来的 Service A，希望先灰度一小部分用户，等运行一段时间足够稳定了再逐渐全量上线新版本，最后平滑下线旧版本。这个时候就可以利用 Nginx Ingress 基于 Header 或 Cookie 进行流量切分的策略来发布，业务使用 Header 或 Cookie 来标识不同类型的用户，我们通过配置 Ingress 来实现让带有指定 Header 或 Cookie 的请求被转发到新版本，其它的仍然转发到旧版本，从而实现将新版本灰度给部分用户:

<img style="width:450px" src="https://main.qcloudimg.com/raw/d13fbc13f02b00d2bb9817c4d2839268.jpg" data-nonescope="true">

### 场景二: 切一定比例的流量给新版本

假设线上运行了一套对外提供 7 层服务的 Service B 服务，后来修复了一些问题，需要灰度上线一个新版本 Service B'，但又不想直接替换掉原来的 Service B，而是让先切 10% 的流量到新版本，等观察一段时间稳定后再逐渐加大新版本的流量比例直至完全替换旧版本，最后再滑下线旧版本，从而实现切一定比例的流量给新版本:

<img style="width:450px" src="https://main.qcloudimg.com/raw/2ab50d5a6d3572e5cbfe6b14180d3105.jpg" data-nonescope="true">

## 注解说明

我们通过给 Ingress 资源指定 Nginx Ingress 所支持的一些 annotation 可以实现金丝雀发布，需要给服务创建两个 Ingress，一个正常的 Ingress，另一个是带 `nginx.ingress.kubernetes.io/canary: "true"` 这个固定的 annotation 的 Ingress，我们姑且称它为 Canary Ingress，一般代表新版本的服务，结合另外针对流量切分策略的 annotation 一起配置即可实现多种场景的金丝雀发布，以下对这些 annotation 详细介绍下:

* `nginx.ingress.kubernetes.io/canary-by-header`: 表示如果请求头中包含这里指定的 header 名称，并且值为 `always` 的话，就将该请求转发给该 Ingress 定义的对应后端服务；如果值为 `never` 就不转发，可以用于回滚到旧版；如果是其它值则忽略该 annotation。
* `nginx.ingress.kubernetes.io/canary-by-header-value`: 这个可以作为 ``canary-by-header`的补充，允许指定请求头的值可以自定义成其它值，不再只能是 `always` 或 `never`；当请求头的值命中这里的自定义值时，请求将会转发给该 Ingress 定义的对应后端服务，如果是其它值则将会忽略该 annotation。
* `nginx.ingress.kubernetes.io/canary-by-header-pattern`: 这个与上面的 `canary-by-header-value` 类似，唯一的区别是它是用正则表达式对来匹配请求头的值，而不是只固定某一个值；需要注意的是，如果它与 ``canary-by-header-value` 同时存在，这个 annotation 将会被忽略。

* `nginx.ingress.kubernetes.io/canary-by-cookie`: 这个与 `canary-by-header` 类似，只是这个用于 cookie，同样也是只支持 `always` 和 `never` 的值。
* `nginx.ingress.kubernetes.io/canary-weight`: 表示 Canary Ingress 所分配流量的比例的百分比，取值范围 [0-100]，比如设置为 10，意思是分配 10% 的流量给 Canary Ingress 对应的后端服务。

上面的规则会按优先顺序进行评估，优先顺序如下： `canary-by-header -> canary-by-cookie -> canary-weight`

注意: 当 Ingress 被标记为 Canary Ingress 时，除了`nginx.ingress.kubernetes.io/load-balance`和 `nginx.ingress.kubernetes.io/upstream-hash-by` 之外，所有其他非 Canary 注释都将被忽略。

## 上手实践

下面我们给出一些例子，让你快速上手 Nginx Ingress 的金丝雀发布，环境为 TKE 集群。

### 使用 YAML 创建资源

本文的示例将使用 yaml 的方式部署工作负载和创建 Service，有两种操作方式。

方式一：在 TKE 或 EKS 控制台右上角点击 `YAML 创建资源`，然后将本文示例的 yaml 粘贴进去:

<img style="width:450px" src="https://main.qcloudimg.com/raw/740c0597b6bc773b3664ca20f290c3e4.png" data-nonescope="true">

方式二：将示例的 yaml 保存成文件，然后使用 kubectl 指定 yaml 文件来创建，如: `kubectl apply -f xx.yaml` 。

### 部署两个版本的服务

这里以简单的 nginx 为例，先部署一个 v1 版本:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-v1
spec:
  replicas: 1
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

---

apiVersion: v1
kind: Service
metadata:
  name: nginx-v1
spec:
  type: ClusterIP
  ports:
  - port: 80
    protocol: TCP
    name: http
  selector:
    app: nginx
    version: v1
```

再部署一个 v2 版本:

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-v2
spec:
  replicas: 1
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

---

apiVersion: v1
kind: Service
metadata:
  name: nginx-v2
spec:
  type: ClusterIP
  ports:
  - port: 80
    protocol: TCP
    name: http
  selector:
    app: nginx
    version: v2
```

可以在控制台看到部署的情况:

<img style="width:450px" src="https://main.qcloudimg.com/raw/e6ab2764ed98bef07920d6a8246f3ab8.png" data-nonescope="true">

再创建一个 Ingress，对外暴露服务，指向 v1 版本的服务:

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: canary.example.com
    http:
      paths:
      - backend:
          serviceName: nginx-v1
          servicePort: 80
        path: /
```

访问验证一下:

``` bash
$ curl -H "Host: canary.example.com" http://EXTERNAL-IP # EXTERNAL-IP 替换为 Nginx Ingress 自身对外暴露的 IP
nginx-v1
```

### 基于 Header 的流量切分

创建 Canary Ingress，指定 v2 版本的后端服务，且加上一些 annotation，实现仅将带有名为 Region 且值为 cd 或 sz 的请求头的请求转发给当前 Canary Ingress，模拟灰度新版本给成都和深圳地域的用户:

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "Region"
    nginx.ingress.kubernetes.io/canary-by-header-pattern: "cd|sz"
  name: nginx-canary
spec:
  rules:
  - host: canary.example.com
    http:
      paths:
      - backend:
          serviceName: nginx-v2
          servicePort: 80
        path: /
```

测试访问:

``` bash
$ curl -H "Host: canary.example.com" -H "Region: cd" http://EXTERNAL-IP # EXTERNAL-IP 替换为 Nginx Ingress 自身对外暴露的 IP
nginx-v2
$ curl -H "Host: canary.example.com" -H "Region: bj" http://EXTERNAL-IP
nginx-v1
$ curl -H "Host: canary.example.com" -H "Region: cd" http://EXTERNAL-IP
nginx-v2
$ curl -H "Host: canary.example.com" http://EXTERNAL-IP
nginx-v1
```

可以看到，只有 header `Region` 为 cd 或 sz 的请求才由 v2 版本服务响应。

### 基于 Cookie 的流量切分

与前面 Header 类似，不过使用 Cookie 就无法自定义 value 了，这里以模拟灰度成都地域用户为例，仅将带有名为 `user_from_cd` 的 cookie 的请求转发给当前 Canary Ingress 。先删除前面基于 Header 的流量切分的 Canary Ingress，然后创建下面新的 Canary Ingress:

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-cookie: "user_from_cd"
  name: nginx-canary
spec:
  rules:
  - host: canary.example.com
    http:
      paths:
      - backend:
          serviceName: nginx-v2
          servicePort: 80
        path: /
```

测试访问:

``` bash
$ curl -s -H "Host: canary.example.com" --cookie "user_from_cd=always" http://EXTERNAL-IP # EXTERNAL-IP 替换为 Nginx Ingress 自身对外暴露的 IP
nginx-v2
$ curl -s -H "Host: canary.example.com" --cookie "user_from_bj=always" http://EXTERNAL-IP
nginx-v1
$ curl -s -H "Host: canary.example.com" http://EXTERNAL-IP
nginx-v1
```

可以看到，只有 cookie `user_from_cd` 为 `always` 的请求才由 v2 版本的服务响应。

### 基于服务权重的流量切分

基于服务权重的 Canary Ingress 就简单了，直接定义需要导入的流量比例，这里以导入 10% 流量到 v2 版本为例 (如果有，先删除之前的 Canary Ingress):

``` bash
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "10"
  name: nginx-canary
spec:
  rules:
  - host: canary.example.com
    http:
      paths:
      - backend:
          serviceName: nginx-v2
          servicePort: 80
        path: /
```

测试访问:

``` bash
$ for i in {1..10}; do curl -H "Host: canary.example.com" http://EXTERNAL-IP; done;
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v1
nginx-v2
nginx-v1
nginx-v1
nginx-v1
```

可以看到，大概只有十分之一的几率由 v2 版本的服务响应，符合 10% 服务权重的设置。

## 存在的缺陷

虽然我们使用 Nginx Ingress 实现了几种不同姿势的金丝雀发布，但还存在一些缺陷:

1. 相同服务的 Canary Ingress 只能定义一个，所以后端服务最多支持两个版本。
2. Ingress 里必须配置域名，否则不会有效果。
3. 即便流量完全切到了 Canary Ingress 上，旧版服务也还是必须存在，不然会报错。

## 总结

本文全方位总结了 Nginx Ingress 的金丝雀发布用法，虽然 Nginx Ingress 在金丝雀发布这方面的能力有限，并且还存在一些缺陷，但基本也能覆盖一些常见的场景，如果集群中使用了 Nginx Ingress，并且发布的需求也不复杂，可以考虑使用这种方案。

## 参考资料

* Nginx Ingress 金丝雀注解官方文档: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#canary
* 在 TKE 上部署 Nginx Ingress: https://cloud.tencent.com/document/product/457/47293