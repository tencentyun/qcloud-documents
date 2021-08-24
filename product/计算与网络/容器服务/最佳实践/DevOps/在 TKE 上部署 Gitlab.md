## 操作场景

本文将介绍如何在容器服务 TKE 上部署 Gitlab 作为私有的代码托管平台。

## 前提条件


已创建 [TKE 集群](https://cloud.tencent.com/document/product/457/32189) 并能够通过 Kubectl [连接集群](https://cloud.tencent.com/document/product/457/32191)。



## 操作步骤

### 安装 Gitlab


使用 Helm 安装 Gitlab，并传入本文推荐的 [values.yaml](https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/gitlab/values-gitlab-ce.yaml) 配置（镜像同步 + TKE 适配）。本文提供以下两种方法在 TKE 上部署 Helm 应用：

>?
- 使用控制台部署时，无需安装 Helm 命令。
- 使用 Helm 命令部署时，适用于 CI/CD 流程。




<dx-tabs>
::: 方法1：使用控制台部署
1. 登录容器服务控制台，选择左侧导航栏中的 **[应用市场](https://console.cloud.tencent.com/tke2/market)**。
2. 在“应用市场”页面搜索 Gitlab，并进入 Gitlab 应用页面。
3. 单击**创建应用**，在创建应用窗口中指定要安装的集群，并将 [values.yaml](https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/gitlab/values-gitlab-ce.yaml) 配置粘贴到参数中。如下图所示：
![](https://main.qcloudimg.com/raw/5508def786013ef4e6d5e21e2ade5803.jpg)
4. 单击**创建**即可安装 Gitlab。
:::
::: 方法2：使用\sHelm\s命令部署

1. 安装 [Helm](https://helm.sh/docs/intro/install/)。
2. 通过 Helm 命令安装 Jenkins ，详情请参见 [Jenkins 安装官方文档](https://www.jenkins.io/doc/book/installing/kubernetes/#install-jenkins-with-helm-v3)。

<dx-alert infotype="explain" title="">
执行 helm install 命令时，需添加 `-f values-gitlab-ce.yaml` 替换部署配置。
</dx-alert>


:::
</dx-tabs>



### 获取访问入口与登录方式

安装 Gitlab 后，默认会创建一个 CLB 并使用4层监听器作为 Gitlab 的访问入口，通过以下步骤可在控制台找到对应的 CLB 及其外网 IP：
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2)**。
2. 在“集群管理”列表页面，选择目标集群 ID，进入该集群 “Deployment” 页面。
3. 选择左侧菜单栏中的**服务与路由** > **Service**，进入 “Service” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/6061996aaed6e36a19db885b9ba38b24.png)
 CLB 端口默认为8181，用户名为 root，初始密码从 gitlab-migrations 的 pod 标准输出可以查看，或者从 `gitlab-initial-root-password` 的 secret 中获取。



## 自定义配置说明

 [values.yaml](https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/gitlab/values-gitlab-ce.yaml) 推荐配置中的参数可以根据自身环境和需求进行自定义，详细介绍如下：

### 禁用依赖

Gitlab 的 Chart 包中包含许多其他依赖的可选应用，在多数场景下并不需要安装。不同环境配置不同，若安装全部应用反而可能带来更多不确定性，加大维护难度，建议根据实际环境安装所需的依赖。推荐配置中许多依赖应用已禁用，YAML 示例文件如下：

<dx-codeblock>
:::  yaml
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
:::
</dx-codeblock>


### 安装 Redis 与 PostgreSQL

在测试环境中，可以同时安装依赖的 Redis 与 PostgreSQL，在生产环境则建议您使用相应的专业云产品。本文推荐配置 [values.yaml](https://raw.githubusercontent.com/TencentCloudContainerTeam/manifest/master/gitlab/values-gitlab-ce.yaml) 中默认安装 Redis 与 PostgreSQL，由于 TKE 默认的 StorageClass 为创建云硬盘，且最低容量为10Gi，因此 Redis 与 PostgreSQL 默认申请10Gi的容量用以持久化数据。YAML 示例文件如下：

<dx-codeblock>
:::  yaml
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
:::
</dx-codeblock>




### 配置流量入口

Gitlab 安装后默认会创建一个 CLB 并使用4层监听器（8181端口）作为 Gitlab 的访问入口。YAML 文件如下：
<dx-codeblock>
:::  yaml
gitlab: 
  webservice: 
    service: 
      type: LoadBalancer # 使用四层 LB 暴露
      workhorseExternalPort: 8181 # gitlab 界面对外端口号
:::
</dx-codeblock>

>?可在浏览器输入 `http://<外网IP>:8181` 进行访问。

在生产环境中建议使用 Ingress 来暴露流量，如需使用 HTTPS，将证书配置在 Ingress 上即可。在 TKE 上推荐使用 Nginx-ingress，需要额外安装组件，详情请参见 [Nginx-ingress 介绍](https://cloud.tencent.com/document/product/457/50502)。

1. 如需使用 Nginx-ingress 对外暴露 Gitlab 服务，只需 ClusterIP 即可，Gitlab 本身的 Service 则无需为 LoadBalancer。YAML 示例文件如下：
<dx-codeblock>
:::  yaml
gitlab: 
  webservice: 
    service: 
      type: ClusterIP # 不为 gitlab 自动创建 CLB
:::
</dx-codeblock>
2. 创建 Ingress。您可以通过 TKE 控制台或 YAML 创建 Ingress：
 <dx-tabs>
::: 通过控制台创建\sIngress
参考控制台 [创建 Ingress](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress) 步骤创建 Ingress。其中：

-  **Ingress**：选择**Nginx负载均衡器**，指定使用 Nginx Ingress。
-  **Class**：指定 Nginx Ingress 实例使用的 ingressClass 名称。
- **监听端口**：选择**Https:443**。
- **转发配置**：填写相关信息，其中“后端服务”，需使用 Gitlab webservice 的 service。
- **TLS配置**：填写相关信息，若使用 HTTPS，则需提前创建证书 Secret。
![](https://main.qcloudimg.com/raw/85ccc1cc26831de539f45df660afc478.jpg)

:::
::: 通过\sYAML\s创建\sIngress
参考 YAML [创建 Ingress](https://cloud.tencent.com/document/product/457/31711#.E5.88.9B.E5.BB.BA-ingress2) 步骤创建 Ingress。YAML 示例文件如下：
<dx-codeblock>
:::  yaml
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
:::
</dx-codeblock>
:::
</dx-tabs>
3. 创建 Ingress 后，流量入口 IP 地址为所选 Nginx Ingress 实例的外网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/ed9edaf8f10d4e38f5cac73f41f49a92.png)
4. Nginx Ingress 实例默认 HTTP 端口为80、HTTPS 端口为443。若 Nginx Ingress 部署在国内地域，使用这两个标准端口进行访问，则需要先为其备案。在测试时，如需使用非标准端口访问，可通过执行以下命令，修改 Nginx Ingress 实例的 service，将80或443改为其他端口。
```bash
kubectl -n kube-system edit svc nginx-ingress-nginx-controller # svc 名称带 ingressClass 名称前缀
```
5. 如需暴露 Gitlab 的 SSH 协议，可修改 Nginx Ingress 实例配置以开放22端口。执行以下命令，修改暴露 TCP 的 configmap。示例如下：
```bash
$ kubectl -n kube-system get cm | grep nginx-ingress
nginx-ingress-nginx-controller             6      8d
nginx-ingress-nginx-tcp                    0      8d
nginx-ingress-nginx-udp                    0      8d
qcloud-tke-nginx-ingress-controller        0      14d
$ kubectl -n kube-system edit cm nginx-ingress-nginx-tcp
```
6. 将 Gitlab shell 的22端口暴露在 nginx ingress controller 的22端口上。YAML 文件示例如下：
<dx-codeblock>
:::  yaml
data: 
  22: "devops/gitlab-gitlab-shell:22"
:::
</dx-codeblock>
7. 执行以下命令，修改 nginx ingress controller 的 service。示例如下：
```bash
$ kubectl -n kube-system get svc
nginx-ingress-nginx-controller             LoadBalancer   172.21.252.133   49.233.238.230   8888:30443/TCP,8443:32345/TCP   8d
$ kubectl -n kube-system edit svc nginx-ingress-nginx-controller
```
8. 将 controller 的22端口暴露到 CLB 上。YAML 文件示例如下：
<dx-codeblock>
:::  yaml
  - name: git-ssh
    port: 22
    protocol: TCP
    targetPort: 22
:::
</dx-codeblock>
 
 至此，您在通过 git clone 命令克隆代码时，即可使用 `git@` 开头的地址（SSH 协议）。


### 配置域名

Gitlab 的域名配置主要用于信息展示，例如 git clone 代码时显示的 URL 地址，可以通过以下 YAML 配置进行设置：
<dx-codeblock>
:::  yaml
global: 
  hosts: 
    gitlab: 
      name: gitlab.example.com # 页面展示的域名
      https: true # 展示的 URL 中是否用 https。如果为 ingress 配了证书，这里就置为 true
:::
</dx-codeblock>

