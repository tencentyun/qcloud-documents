本文将介绍使用 Nginx Ingress 实现金丝雀发布的使用场景、用法详解及实践。
>?使用 Nginx Ingress 实现金丝雀发布的集群，需部署 Nginx Ingress 作为 Ingress Controller，并且对外暴露统一的流量入口。详情请参见 [在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293)。

## 使用场景
使用 Nginx Ingress 实现金丝雀发布适用场景主要取决于业务流量切分的策略，目前 Nginx Ingress 支持基于 Header、Cookie 和服务权重3种流量切分的策略，基于这3种策略可实现以下两种发布场景：


### 场景1: 灰度新版本到部分用户
假设线上已运行了一套对外提供7层服务的 Service A，此时需上线开发的新版本 Service A'，但不期望直接替换原有的 Service A，仅灰度部分用户，待运行一段时间足够稳定后再逐渐全量上线新版本，平滑下线旧版本。
针对此场景可使用 Nginx Ingress 基于 Header 或 Cookie 进行流量切分的策略来发布，业务使用 Header 或 Cookie 来标识不同类型的用户，并通过配置 Ingress 来实现让带有指定 Header 或 Cookie 的请求被转发到新版本，其它请求仍然转发到旧版本，从而将新版本灰度给部分用户。示意图如下：
<img style="width:80%" src="https://main.qcloudimg.com/raw/d13fbc13f02b00d2bb9817c4d2839268.jpg" data-nonescope="true">

### 场景2: 切分一定比例的流量到新版本
假设线上已运行了一套对外提供7层服务的 Service B，此时修复了 Service B 的部分问题，需灰度上线新版本 Service B'。但不期望直接替换原有的 Service B，需先切换10%的流量至新版本，待运行一段时间足够稳定后再逐渐加大新版本流量比例直至完全替换旧版本，最终平滑下线旧版本。示意图如下：
<img style="width:80%" src="https://main.qcloudimg.com/raw/2ab50d5a6d3572e5cbfe6b14180d3105.jpg" data-nonescope="true">

## 注解说明
通过给 Ingress 资源指定 Nginx Ingress 所支持的 annotation 可实现金丝雀发布。需给服务创建2个 Ingress，其中1个常规 Ingress，另1个为带 `nginx.ingress.kubernetes.io/canary: "true"` 固定的 annotation 的 Ingress，称为 Canary Ingress。Canary Ingress 一般代表新版本的服务，结合另外针对流量切分策略的 annotation 一起配置即可实现多种场景的金丝雀发布。以下为相关 annotation 的详细介绍：

- **`nginx.ingress.kubernetes.io/canary-by-header`**
表示如果请求头中包含指定的 header 名称，并且值为 `always`，就将该请求转发给该 Ingress 定义的对应后端服务。如果值为 `never` 则不转发，可以用于回滚到旧版。如果为其他值则忽略该 annotation。

- **`nginx.ingress.kubernetes.io/canary-by-header-value`**
该 annotation 可以作为 `canary-by-header` 的补充，可指定请求头为自定义值，包含但不限于 `always` 或 `never`。当请求头的值命中指定的自定义值时，请求将会转发给该 Ingress 定义的对应后端服务，如果是其它值则忽略该 annotation。
* **`nginx.ingress.kubernetes.io/canary-by-header-pattern`**
与 `canary-by-header-value` 类似，区别为该 annotation 用正则表达式匹配请求头的值，而不是只固定某一个值。如果该 annotation 与 `canary-by-header-value` 同时存在，该 annotation 将被忽略。
* **`nginx.ingress.kubernetes.io/canary-by-cookie`**
与 `canary-by-header` 类似，该 annotation 用于 cookie，仅支持 `always` 和 `never`。
* **`nginx.ingress.kubernetes.io/canary-weight`**
表示 Canary Ingress 所分配流量的比例的百分比，取值范围 [0-100]。例如，设置为10，则表示分配10%的流量给 Canary Ingress 对应的后端服务。

>?
>- 以上规则会按优先顺序进行评估，优先顺序为： `canary-by-header -> canary-by-cookie -> canary-weight`。
>- 当 Ingress 被标记为 Canary Ingress 时，除了 `nginx.ingress.kubernetes.io/load-balance` 和  `nginx.ingress.kubernetes.io/upstream-hash-by` 外，所有其他非 Canary 注释都将被忽略。



## 使用示例
>!
>以下示例环境以 TKE 集群为例，您可通过示例快速上手 Nginx Ingress 的金丝雀发布。需注意以下事项：
> - 相同服务的 Canary Ingress 仅能够定义一个，导致后端服务最多支持两个版本。
2. Ingress 里必须配置域名，否则不会有效果。
3. 即便流量完全切到了 Canary Ingress 上，旧版服务仍需存在，否在会出现报错。


### 使用 YAML 创建资源
本文提供以下两种方式使用 YAML 部署工作负载及创建 Servcie：
- 方式1：在单击 TKE 或 EKS 集群详情页右上角的**YAML创建资源**，并将本文示例的 YAML 文件内容输入编辑界面。
- 方式2：将示例 YAML 保存为文件，再使用 kubectl 指定 YAML 文件进行创建。例如 `kubectl apply -f xx.yaml`。


### 部署两个版本的服务
1. 在集群中部署第一个版本的 Deployment，本文以 nginx-v1 为例。YAML 示例如下：

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
2. 再部署第二个版本的 Deployment，本文以 nginx-v2 为例。YAML 示例如下：

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
您可登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster)，在集群的工作负载详情页查看部署情况。如下图所示：
<img src="https://main.qcloudimg.com/raw/4d3411bb5f9301d4ff8bee25066c64be.png">
3. 创建 Ingress，对外暴露服务，指向 v1 版本的服务。YAML 示例如下：

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
4. 执行以下命令，进行访问验证。

``` bash
curl -H "Host: canary.example.com" http://EXTERNAL-IP # EXTERNAL-IP 替换为 Nginx Ingress 自身对外暴露的 IP
```
返回结果如下：
```
nginx-v1
```

### 基于 Header 的流量切分

创建 Canary Ingress，指定 v2 版本的后端服务，并增加 annotation。实现仅将带有名为 Region 且值为 cd 或 sz 的请求头的请求转发给当前 Canary Ingress，模拟灰度新版本给成都和深圳地域的用户。YAML 示例如下：
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
执行以下命令，进行访问测试。
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
可查看当仅有 header `Region` 为 cd 或 sz 的请求才由 v2 版本服务响应。

### 基于 Cookie 的流量切分
使用 Cookie 则无法自定义 value，以模拟灰度成都地域用户为例，仅将带有名为 `user_from_cd` 的 Cookie 的请求转发给当前 Canary Ingress。YAML 示例如下：
>?若您已配置以上步骤创建 Canary Ingress，则请删除后再参考本步骤创建。
>
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
执行以下命令，进行访问测试。
``` bash
$ curl -s -H "Host: canary.example.com" --cookie "user_from_cd=always" http://EXTERNAL-IP # EXTERNAL-IP 替换为 Nginx Ingress 自身对外暴露的 IP
nginx-v2
$ curl -s -H "Host: canary.example.com" --cookie "user_from_bj=always" http://EXTERNAL-IP
nginx-v1
$ curl -s -H "Host: canary.example.com" http://EXTERNAL-IP
nginx-v1
```
可查看当仅有 cookie `user_from_cd` 为 `always` 的请求才由 v2 版本的服务响应。

### 基于服务权重的流量切分
使用基于服务权重的 Canary Ingress 时，直接定义需要导入的流量比例即可。以导入10%流量到 v2 版本为例，YAML 示例如下：
>?若您已配置以上步骤创建 Canary Ingress，则请删除后再参考本步骤创建。
>
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
执行以下命令，进行访问测试。
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
可查看，有十分之一的几率由 v2 版本的服务响应，符合10%服务权重的设置。


## 参考资料

* [Nginx Ingress 金丝雀注解官方文档]( https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#canary)
* [在 TKE 上部署 Nginx Ingress](https://cloud.tencent.com/document/product/457/47293)
