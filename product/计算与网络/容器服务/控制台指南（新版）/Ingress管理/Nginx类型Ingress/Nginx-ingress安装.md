




您可以根据不同的业务场景需求，使用多种安装方案在容器服务 TKE 中安装 Nginx-ingress。

## 安装 Nginx-ingress 组件<span id="Nginx-ingress"></span>

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【集群】。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的【组件管理】，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择【新建】，并在“新建组件”页面中勾选 Nginx-ingress。
5. 单击【完成】即可安装组件。


## 安装方式

## （推荐）通过 DaementSet 形式在指定节点池部署

Nginx 作为关键的流量接入网关，是至关重要的组件，不建议您将 Nginx 与其他业务部署在相同的节点内。推荐您使用指定的节点池来部署 Nginx-ingress。部署架构如下图所示：
![](https://main.qcloudimg.com/raw/217e17c24988adbd643cec9b7af2a56c.png)
### 安装步骤
1. 提前准备用于部署 Nginx-ingress 的节点池，同时设置污点 taint（防止其他 Pod 调度到该节点池）。部署节点池详情可参见 [节点池相关说明](https://cloud.tencent.com/document/product/457/43719)。
2. 在集群中 [安装 Nginx-ingress 组件](#Nginx-ingress)。
3. 进入 Nginx-ingress 详情，创建 Nginx 实例（一个集群内可以同时存在多个 Nginx），并设置容忍污点和节点池标签调度。
 - Nginx 部署选项选择指定 DaementSet 节点池部署。
 - 设置容忍污点。
 - Nginx 的 Requst 需设置比节点池的机型配置小（节点本身有资源预留），Limit 可不设置。
 - 其他参数根据业务需要设置即可。
4. 完成安装。

>? 使用以上安装方式，您可以完整享有节点池快速扩缩容的能力，后续您只要调整节点池的数量，即可扩缩容 Nginx 的副本。

## 通过 Deployment + HPA 形式并指定调度规则部署

通过 Deployment + HPA 的形式部署 Nginx-ingress。部署架构如下图所示：
![](https://main.qcloudimg.com/raw/5147b2ffbbf056bb1ef468780a3c4669.png)

### 安装步骤
1. 在集群中设置即将部署 Nginx 的节点的 Lable。
2. 在集群中 [安装 Nginx-ingress 组件](#Nginx-ingress)。
3. Nginx 部署选项选择指定 Deployment + HPA 部署。
4. 指定 Nginx 的调度规则。
5. 设置 Nginx Request 和 Limit。
6. 完成安装。

使用 Deployment + HPA 形式，您也可以根据业务需要配置污点和容忍将 Nginx 和业务 Pod 分散部署。同时搭配 HPA，可设置 Nginx 根据 CPU / 内存等指标进行弹性伸缩。


### Nginx 前端接入 LB 部署方式

仅部署 Nginx 在集群内将无法接收外部流量。还需配置 Nginx 的前端 LB。TKE 现已提供产品化的安装能力，您也可以根据业务需要选择不同的部署模式。

#### VPC-CNI 模式集群使用 CLB 直通 Nginx 的 Serivce（推荐）

如果您的集群是VPC-CNI模式的集群，我们推荐您使用CLB直通Nginx的Serivce。我们以节点池部署的负载示例。
![](https://main.qcloudimg.com/raw/d74dd402599c1a44e7c18bdb3c1868a1.png)
当前方案性能好，而且不需要手动维护 clb，是最理想的方案。需要集群支持 VPC-CNI，如果你的集群本身用的 VPC-CNI 网络插件，或者用的 Global Router 网络插件并开启了 VPC-CNI 的支持(两种模式混用)，那么建议直接使用这种方案。

##### Globalrouter模式集群使用普通Loadbalancer模式的Service

如果您的集群不支持VPC-CNI模式网络， 您也可以通过常规的Loadbalancer模式Service接入流量。 
当前TKE 上 LoadBalancer 类型的 Service 默认实现是基于 NodePort，CLB 会绑定各节点的 NodePort 作为后端 RS，将流量转发到节点的 NodePort，然后节点上再通过 iptables 或 ipvs 将请求路由到 Service 对应的后端 Pod.这种方案是最简单的方案，流量会经过一层 NodePort，会多一层转发。可能存在以下问题：

1. 转发路径较长，流量到了 NodePort 还会再经过 k8s 内部负载均衡，通过 iptables 或 ipvs 转发到 nginx，会增加一点网络耗时。
2. 经过 NodePort 必然发生 SNAT，如果流量过于集中容易导致源端口耗尽或者 conntrack 插入冲突导致丢包，引发部分流量异常。
3. 每个节点的NodePort也充当一个负载均衡器，CLB如果绑定大量节点的NodePort，负载均衡的状态就分散在每个节点上，容器导致全局负载不均。
4. CLB 会对 NodePort 进行健康探测，探测包最终会被转发到 nginx ingress 的 Pod，如果 CLB 绑定的节点多，nginx ingress 的 Pod 少，会导致探测包对 nginx ingress 造成较大的压力。



##### 使用HostNetwork+LB模式

当前页面暂不支持， 您可以手动修改Nginx工作负载的Yaml配置网络模式为HostNetwork, 手动创建CLB绑定Nginx暴露的节点端口。
需要注意使用 hostNetwork，nginx ingress 的 pod 就不能被调度到同一节点避免端口监听冲突。

### Nginx-ingress 安装参数

#### TKE 安装 Nginx-ingress 的默认参数

hongyu帮提供下

#### 您可以设置的 Nginx-ingress 参数和设置方式

##### 参数设置方式

您可以在 Nginx-ingress 组件详情页，Ningx 参数 tab 中选择的 Nginx-ingress 实例进行 YAML 编辑。
注意，默认情况下配置参数不会重启nginx，生效时间有细微延迟。
补充截图


配置参数示例：

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-ingress-controller
# nginx ingress 性能优化: https://www.nginx.com/blog/tuning-nginx/
data:
  # nginx 与 client 保持的一个长连接能处理的请求数量，默认 100，高并发场景建议调高。
  # 参考: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#keep-alive-requests
  keep-alive-requests: "10000"
  # nginx 与 upstream 保持长连接的最大空闲连接数 (不是最大连接数)，默认 32，在高并发下场景下调大，避免频繁建联导致 TIME_WAIT 飙升。
  # 参考: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#upstream-keepalive-connections
  upstream-keepalive-connections: "200"
  # 每个 worker 进程可以打开的最大连接数，默认 16384。
  # 参考: https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#max-worker-connections
  max-worker-connections: "65536"
```

根据业务需要可配置的参数，可查看[官方文档](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/)













