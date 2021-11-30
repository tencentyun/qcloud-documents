## 操作场景
腾讯云 Kubernetes 集群实现蓝绿发布或灰度发布通常需向集群额外部署其他开源工具，例如 Nginx Ingress、Traefik 或将业务部署至服务网格 Service Mesh，利用服务网格的能力实现。这些方案均具有一定难度，若您的蓝绿发布或灰度需求不复杂，且不期望集群引入过多的组件或复杂的用法，则可参考本文利用 Kubernetes 原生的特性以及腾讯云容器服务 TKE、弹性容器服务 EKS 集群自带的 LB 插件实现简单的蓝绿发布和灰度发布。
>!本文仅适用于 TKE 集群及 EKS 集群。

## 原理介绍
用户通常使用 Deployment、StatefulSet 等 Kubernetes 自带的工作负载来部署业务，每个工作负载管理一组 Pod。以 Deployment 为例，示意图如下：
<img style="width:30%" src="https://main.qcloudimg.com/raw/bcbda91a3bd75840afd4a23fbc136310.png" data-nonescope="true">
通常还会为每个工作负载创建对应的 Service，Service 通过 selector 来匹配后端 Pod，其他服务或者外部通过访问 Service 即可访问到后端 Pod 提供的服务。如需对外暴露可直接将 Service 类型设置为 LoadBalancer，LB 插件会自动为其创建腾讯云负载均衡 CLB 作为流量入口。 

### 蓝绿发布原理
以 Deployment 为例，集群中已部署两个不同版本的 Deployment，其 Pod 拥有共同的 label。但有一个 label 值不同，用于区分不同的版本。Service 使用 selector 选中了其中一个版本的 Deployment 的 Pod，此时通过修改 Service 的 selector 中决定服务版本的 label 的值来改变 Service 后端对应的 Deployment，即可实现让服务从一个版本直接切换到另一个版本。示意图如下：
<img style="width:90%" src="https://main.qcloudimg.com/raw/f38aec8893abdcb311e05a132ec37440.png" data-nonescope="true">

### 灰度发布原理
用户通常会为每个工作负载创建一个 Service，但 Kubernetes 未限制 Servcie 需与工作负载一一对应。Service 通过 selector 匹配后端 Pod，若不同工作负载的 Pod 被同一 selector 选中，即可实现一个 Service 对应多个版本工作负载。调整不同版本工作版本的副本数即调整不同版本服务的权重。示意图如下：
<img style="width:90%" src="https://main.qcloudimg.com/raw/e271e9d585524b899807c6059afac03d.png" data-nonescope="true">


## 操作步骤
### 使用 YAML 创建资源
本文提供以下两种方式使用 YAML 部署工作负载及创建 Servcie：
 - 方式1：单击 TKE 或 EKS 集群详情页右上角的**YAML创建资源**，并将本文示例的 YAML 文件内容输入编辑界面。
 - 方式2：将示例 YAML 保存为文件，再使用 kubectl 指定 YAML 文件进行创建。例如 `kubectl apply -f xx.yaml`。


### 部署多版本工作负载
1. 在集群中部署第一个版本的 Deployment，本文以 nginx 为例。YAML 示例如下：

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
2. 再部署第二个版本的 Deployment，本文以 nginx 为例。YAML 示例如下：

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
您可登录 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster)，在集群的工作负载详情页查看部署情况。如下图所示：
<img style="width:80%" src="https://main.qcloudimg.com/raw/4d3411bb5f9301d4ff8bee25066c64be.png">

### 实现蓝绿发布

1. 为部署的 Deployment 创建 LoadBalancer 类型的 Service 对外暴露服务，指定使用 v1 版本的服务。YAML 示例如下：
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
2. 执行以下命令，测试访问。
``` bash
for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
```
返回结果如下，均为 v1 版本的响应。
```
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
3. 通过控制台或 kubectl 方式修改 Service 的 selector，使其选中 v2 版本的服务：
 - **通过控制台修改**：
    1. 进入集群详情页，选择左侧**服务与路由** > **Service**。
    2. 在 “Service” 页面中选择需修改 Service 所在行右侧的**编辑YAML**。如下图所示：
<img style="width:80%" src="https://main.qcloudimg.com/raw/fd90554aa91b092e2c9cb4706ba45ab4.png" data-nonescope="true"></img>
修改 selector 部分为如下内容：
``` yaml
  selector:
    app: nginx
    version: v2
```
  - **通过 kubectl 修改**：
``` bash
kubectl patch service nginx -p '{"spec":{"selector":{"version":"v2"}}}'
```
4. 执行以下命令，再次测试访问。
``` bash
$ for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
```
返回结果如下，均为 v2 版本的响应，成功实现了蓝绿发布。
```
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


### 实现灰度发布
1. 对比蓝绿发布，不指定 Service 使用 v1 版本服务。即从 selector 中删除 `version` 标签，让 Service 同时选中两个版本的 Deployment 的 Pod。YAML 示例如下：
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
2. 执行以下命令，测试访问。
``` yaml
for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
```
返回结果如下，一半是 v1 版本的响应，另一半是 v2 版本的响应。
```
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
3. 通过控制台或 kubectl 方式调节 v1 和 v2 版本的 Deployment 的副本，将 v1 版本调至 1 个副本，v2 版本调至 4 个副本：
 - **通过控制台修改**：
    1. 进入集群 “Deployment” 管理页，选择 v1 版本 Deployment 所在行右侧的**更多** > **编辑YAML**。
    2. 在 YAML 编辑页面，将 v1 版本的 `replicas` 修改为1并单击**完成**。
    3. 重复上述步骤，将 v2 版本的 `replicas` 修改为4并单击**完成**。
 - **通过 kubectl 修改**：
``` bash
kubectl scale deployment/nginx-v1 --replicas=1
kubectl scale deployment/nginx-v2 --replicas=4
```
4. 执行以下命令，再次进行访问测试。
``` bash
for i in {1..10}; do curl EXTERNAL-IP; done; # 替换 EXTERNAL-IP 为 Service 的 CLB IP 地址
```
返回结果如下，10次访问中仅2次返回了 v1 版本，v1 与 v2 的响应比例与其副本数比例一致，为 1:4。通过控制不同版本服务的副本数就实现了灰度发布。
```
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
