





## 安装 NginxIngress 组件[](id:Nginx-ingress)

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 NginxIngress。
5. 单击**完成**即可安装组件。


## 安装方式
您可以根据不同的业务场景需求，使用以下几种安装方案在容器服务 TKE 中安装 Nginx-ingress。
- [通过 DaemonSet 形式在指定节点池部署](#DaemonSet)
- [通过 Deployment + HPA 形式并指定调度规则部署](#Deployment+HPA)
- [Nginx 前端接入 LB 部署方式](#LB)




### 通过 DaemonSet 形式在指定节点池部署（推荐）[](id:DaemonSet)

Nginx 作为关键的流量接入网关，不建议您将 Nginx 与其他业务部署在相同的节点内。推荐您使用指定的节点池来部署 Nginx-ingress。部署架构如下图所示：
![](https://main.qcloudimg.com/raw/217e17c24988adbd643cec9b7af2a56c.png)
请参考以下步骤进行安装：
>? 使用此安装方式，您可以完整享有节点池快速扩缩容的能力，后续您只要调整节点池的数量，即可扩缩容 Nginx 的副本。
>
1. 准备用于部署 Nginx-ingress 的节点池，同时设置污点 taint（防止其他 Pod 调度到该节点池）。部署节点池详情可参见 [节点池相关说明](https://cloud.tencent.com/document/product/457/43719)。
2. 在集群中 [安装 NginxIngress 组件](#Nginx-ingress)。
3. 在新建的 Nginx Ingress 组件详情页，单击**新增Nginx Ingress实例**（一个集群内可以同时存在多个 Nginx）。
![](https://main.qcloudimg.com/raw/75edc57adda78df364f9430a844eb1b5.png)
4. 在弹出的窗口中，选择部署选项中的**指定DaemonSet节点池部署**，并按需设置其他参数。如下图所示：
![](https://main.qcloudimg.com/raw/d640a06f25185e3a37d546533442e118.png)
 - 节点池：配置节点池。
 - Nginx 配置：Requst 需设置比节点池的机型配置小（节点本身有资源预留）。Limit 可不设置。
4. 单击**确定**即可完成安装。



### 通过 Deployment + HPA 形式并指定调度规则部署[](id:Deployment+HPA)
使用 Deployment + HPA 的形式部署 Nginx-ingress，您可以根据业务需要配置污点和容忍将 Nginx 和业务 Pod 分散部署。同时搭配 HPA，可设置 Nginx 根据 CPU / 内存等指标进行弹性伸缩。部署架构如下图所示：
![](https://main.qcloudimg.com/raw/5147b2ffbbf056bb1ef468780a3c4669.png)


#### 安装步骤
1. 在集群中设置即将部署 Nginx 的节点的 Label，设置步骤可参见 [设置节点 Label](https://cloud.tencent.com/document/product/457/32768)。
2. 在集群中 [安装 NginxIngress 组件](#Nginx-ingress)。
3. 在新建的 Nginx Ingress 组件详情页，单击**新增Nginx Ingress实例**（一个集群内可以同时存在多个 Nginx）。
4. 在弹出的窗口中，选择部署选项中的**自定义Deployment+HPA 部署**，并按需设置其他参数。如下图所示：
![](https://main.qcloudimg.com/raw/650626808a60e00fc989a09e8a5477bd.png)
 - 节点调度策略：需自行指定。
 - Nginx 配置：Requst 需设置比节点池的机型配置小（节点本身有资源预留）。Limit 可不设置。
5. 单击**确定**即可完成安装。




### Nginx 前端接入 LB 部署方式[](id:LB)

仅部署 Nginx 在集群内将无法接收外部流量，还需配置 Nginx 的前端 LB。TKE 现已提供产品化的安装能力，您也可以根据业务需要选择不同的部署模式。

#### VPC-CNI 模式集群使用 CLB 直通 Nginx 的 Serivce（推荐）

如果您的集群是 VPC-CNI 模式的集群，推荐您使用 CLB 直通 Nginx 的 Serivce。下图为以节点池部署的负载示例。
![](https://main.qcloudimg.com/raw/d74dd402599c1a44e7c18bdb3c1868a1.png)
当前方案性能好，而且不需要手动维护 CLB，是最理想的方案。需要集群支持 VPC-CNI，如果您的集群已配置 VPC-CNI 网络插件，或者已配置 Global Router 网络插件并开启了 VPC-CNI 的支持（两种模式混用），建议使用此方案。

#### Globalrouter 模式集群使用普通 Loadbalancer 模式的 Service

如果您的集群不支持 VPC-CNI 模式网络，您也可以通过常规的 Loadbalancer 模式 Service 接入流量。 
当前 TKE 上 LoadBalancer 类型的 Service 默认实现是基于 NodePort，CLB 会绑定各节点的 NodePort 作为后端 RS，将流量转发到节点的 NodePort，然后节点上再通过 iptables 或 ipvs 将请求路由到 Service 对应的后端 Pod。这种方案是最简单的方案，但流量会经过一层 NodePort，会多一层转发。可能存在以下问题：
- 转发路径较长，流量到了 NodePort 还会再经过 k8s 内部负载均衡，通过 iptables 或 ipvs 转发到 Nginx，会增加一点网络耗时。
- 经过 NodePort 必然发生 SNAT，如果流量过于集中容易导致源端口耗尽或者 conntrack 插入冲突导致丢包，引发部分流量异常。
- 每个节点的 NodePort 也充当一个负载均衡器，CLB 如果绑定大量节点的 NodePort，负载均衡的状态会分散在每个节点上，容器导致全局负载不均。
- CLB 会对 NodePort 进行健康探测，探测包最终会被转发到 nginx ingress 的 Pod，如果 CLB 绑定的节点多，Nginx-ingress 的 Pod 少，会导致探测包对 Nginx-ingress 造成较大的压力。



#### 使用 HostNetwork + LB 模式

控制台暂不支持，您可以手动修改 Nginx 工作负载的 Yaml 配置网络模式为 HostNetwork，手动创建 CLB 绑定 Nginx 暴露的节点端口。
需要注意使用 hostNetwork 时，为避免端口监听冲突，Nginx-ingress 的 Pod 不能被调度到同一节点。



## TKE 安装 Nginx-ingress 默认参数



### Nginx-ingress 参数设置方式

您可以在 Nginx-ingress 组件详情页，Ningx 参数 tab 中选择的 Nginx-ingress 实例进行 YAML 编辑。
>! 默认情况下配置参数不会重启 Nginx，生效时间有细微延迟。

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入 “组件列表” 页面。
4. 单击需要设置参数的组件右侧的**更新Nginx配置**，进入“Nginx配置”页面。
5. 选择 Nginx Ingress 实例，并单击**编辑YAML**。
6. 在“更新ConfigMap”页面进行编辑，单击**完成**即可配置参数。

### 配置参数示例


```yaml
apiVersion: v1
kind: ConfigMap
metadata:
     name: alpha-ingress-nginx-controller
     namespace: kube-system
data:
     access-log-path: /var/log/nginx/nginx_access.log
     error-log-path: /var/log/nginx/nginx_error.log
     log-format-upstream: $remote_addr - $remote_user [$time_iso8601] $msec "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" $request_length $request_time [$proxy_upstream_name] [$proxy_alternative_upstream_name] [$upstream_addr] [$upstream_response_length] [$upstream_response_time] [$upstream_status] $req_id
     keep-alive-requests: "10000"
     max-worker-connections: "65536"
     upstream-keepalive-connections: "200"
```

>!
- 请勿修改 `access-log-path ` 、`error-log-path`、`log-format-upstream`。若修改则会对 CLS 日志采集造成影响。
- 若您需要根据业务配置不同的参数，可参见 [官方文档](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/)。















