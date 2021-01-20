## 操作场景

本文将介绍如何在 TKE 上部署一套 Gitlab 作为私有的代码托管平台。

## 前提条件

* 已创建 TKE 集群，创建过程可参见 [部署容器服务 TKE](https://cloud.tencent.com/document/product/457/11741)。

## 操作步骤

使用 Helm 安装 Gitlab，传入这里推荐的 [values.yaml](https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/gitlab/values-gitlab-ce.yaml) 配置(镜像同步 + TKE 适配)。在 TKE 上有两种方法部署 Helm 应用，参考以下说明。

### 方法一: 使用应用市场部署

在 [应用市场](https://console.cloud.tencent.com/tke2/market) 搜索 Gitlab 并指定要安装的集群，将 `values.yaml` 配置粘贴到参数中:

![](https://main.qcloudimg.com/raw/273f2dee7675bd6937df7805e7eb35d0.png)

> 直接在界面上操作即可，无需安装 helm 命令。

### 方法二: 使用 helm 命令部署

使用这种方式需要保证自行安装好 helm 命令，参考 [官方安装文档](https://helm.sh/docs/intro/install/)，并且需要保证能够使用 kubectl 操作集群，然后就可以通过 helm 命令安装 Jenkins 了，参考 [Jenkins 安装官方文档](https://www.jenkins.io/doc/book/installing/kubernetes/#install-jenkins-with-helm-v3) (helm install 的时候加下 -f values-gitlab-ce.yaml 替换部署配置)。

> 适合用在 CI/CD 流程，不通过控制台部署。

### 获取访问入口与登录方式

安装好后，默认会创建一个 CLB 并使用 4 层监听器作为 Gitlab 的访问入口，在控制台可找到对应的 CLB 及其外网 IP:

![](https://main.qcloudimg.com/raw/64a6e55d982d81563089082d48a78623.png)

端口默认是 8181，用户名是 root，初始密码从 gitlab-migrations 的 pod 标准输出可以看到，或者从 `gitlab-initial-root-password` 的 secret 中获取。

## 配置说明与自定义

推荐配置中有许多参数可以根据自身环境和需求进行自定义，下面给出说明。

### 不安装过多依赖

Gitlab 的 Chart 包中包含许多其它依赖的应用，它们是可选的，很多可能都用不上，而且不同环境不一样，如果都安装上，反而带来更多不确定性，加大维护难度；若需要，可以根据自身情况单独安装，所以不建议安装太多的依赖，推荐配置中将许多依赖应用已经禁用:

``` yaml
certmanager:
  install: false
nginx-ingress:
  enabled: false
prometheus:
  install: false
gitlab-runner:
  install: false
registry:
  enabled: false
  ingress:
    enabled: false
```

### Redis 与 PostgreSQL

测试时可以顺便将依赖的 redis 与 postgresql 一起安装了，在生产环境还是建议用相应的专业云产品。这里推荐配置中默认安装了 redis 与 posgresql，由于 TKE 默认的 StorageClass 是创建云硬盘，且最低容量 10Gi，所以 redis 与 postgresql 这里默认申请 10Gi 的容量来持久化数据:

``` yaml
redis:
  install: true
  usePassword: true
  password: "123456"
  cluster:
    enabled: false
  master:
    persistence:
      size: 10Gi

postgresql:
  install: true
  postgresqlUsername: gitlab
  postgresqlPostgresPassword: "123456"
  persistence:
    size: 10Gi
```

### 流量入口

默认安装会创建一个 CLB 并使用 4 层监听器 (8181端口) 作为 Gitlab 的访问入口:

``` yaml
gitlab:
  webservice:
    service:
      type: LoadBalancer # 使用四层 LB 暴露
      workhorseExternalPort: 8181 # gitlab 界面对外端口号
```

浏览器输入 `http://<外网IP>:8181` 进行访问。

不过生产环境实际用还是推荐用 Ingress 来暴露流量，如需使用 https，将证书配置在 Ingress 上即可。在 TKE 上推荐使用 nginx-ingress，是需要额外安装的组件，参考 [官方文档说明](https://cloud.tencent.com/document/product/457/50502)。

使用 nginx-ingress 对外暴露 gitlab 服务的话，gitlab 本身的 service 就不需要为 LoadBalancer 了，只需要 ClusterIP 即可:

``` yaml
gitlab:
  webservice:
    service:
      type: ClusterIP # 不为 gitlab 自动创建 CLB
```

然后在 TKE 控制台创建 Ingress:

![](https://main.qcloudimg.com/raw/ac583714b9f93bf4fe4947589c10feb0.png)

当然也可以用 yaml 创建:

``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
  name: gitlab
  namespace: devops
spec:
  rules:
  - host: gitlab.xxxx.io
    http:
      paths:
      - backend:
          serviceName: gitlab-webservice-default
          servicePort: 8181
        path: /
        pathType: ImplementationSpecific
  tls:
  - hosts:
    - gitlab.xxxx.io
    secretName: gitlab-crt-secret
```

Ingress 创建好后，流量入口 IP 地址为所选 nginx-ingress 实例的外网 IP:

![](https://main.qcloudimg.com/raw/747ac14d9efa7ebcce591277d1bfca89.png)

http 端口为 80，https 端口为 443。如果部署在国内，使用这两个标准端口需要备案才能访问，测试时如果想使用非标端口，可以修改 nginx-ingress 实例的 service，将 80/443 改为其它端口:

``` bash
kubectl -n kube-system edit svc nginx-ingress-nginx-controller # svc 名称带 ingressClass 名称前缀
```

如果需要暴露 gitlab 的 ssh 协议，可修改 nginx-ingress 配置，将 22 端口也暴露出来，修改暴露 tcp 的 configmap:

``` bash
$ kubectl -n kube-system get cm | grep nginx-ingress
nginx-ingress-nginx-controller             6      8d
nginx-ingress-nginx-tcp                    0      8d
nginx-ingress-nginx-udp                    0      8d
qcloud-tke-nginx-ingress-controller        0      14d

$ kubectl -n kube-system edit cm nginx-ingress-nginx-tcp
```

将 gitlab shell 的 22 端口暴露在 nginx ingress controller 的 22 端口上:

``` yaml
data:
  22: "devops/gitlab-gitlab-shell:22"
```

再修改 nginx ingress controller 的 service:

``` bash
$ kubectl -n kube-system get svc
nginx-ingress-nginx-controller             LoadBalancer   172.21.252.133   49.233.238.230   8888:30443/TCP,8443:32345/TCP   8d

$ kubectl -n kube-system edit svc nginx-ingress-nginx-controller
```

将 controller 的 22 端口暴露到 CLB 上:

``` yaml
  - name: git-ssh
    port: 22
    protocol: TCP
    targetPort: 22
```

然后 git clone 代码时就可以用 `git@` 开头的地址(ssh 协议)。

### 配置域名

gitlab 的域名配置主要用于信息展示，比如 git clone 代码时显示的 url 地址，可以通过以下配置来设置:

``` yaml
global:
  hosts:
    gitlab:
      name: gitlab.example.com # 页面展示的域名
      https: true # 展示的 URL 中是否用 https。如果为 ingress 配了证书，这里就置为 true
```