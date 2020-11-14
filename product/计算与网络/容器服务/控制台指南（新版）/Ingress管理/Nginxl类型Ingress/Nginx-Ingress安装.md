## Nginx-Ingress安装
### Nginx-ingress安装方式
Nginx-ingress在TKE中您可以使用多种按照方案， 适用于您不通的业务场景需求。

#### 安装Nginx-ingress组件（前提）
1. 选择部署安装Nginx-ingress组件的集群。
2. 进入集群组件管理页面
3. 新建Nginx-ingress组件
4. 完成。

#### 通过DaementSet形式在指定节点池部署（推荐）
Nginx作为关键的流量接入网关， 是至关重要的组件， 不建议您将Nginx于其他业务部署在相同的节点内。 
推荐您使用指定的节点池来部署Nginx-ingress。 部署架构如下：

![](https://main.qcloudimg.com/raw/217e17c24988adbd643cec9b7af2a56c.png)

1. 提前准备用于部署Nginx-ingress的节点池，同时设置污点taint(防止其他Pod调度到该节点池)。 更多可查看[节点池相关说明](https://cloud.tencent.com/document/product/457/43719)
2. 在集群组件页面安装好Nginx-ingress组件。
3. 进入Nginx-ingress详情，创建Nginx实例（一个集群内可以同时存在多个Nginx）, 并设置容忍污点和节点池标签调度。
 - Nginx部署选项选择指定DaementSet节点池部署。
 - 设置容忍污点。
 - Nginx 的Requst需设置比节点池的机型配置小（节点本身有资源预留）， Limit可不设置。
 - 其他参数根据业务需要设置即可。
 4. 完成安装。

使用这种安装方式，您可以完整享有节点池快速扩缩容的能力， 后续您只要调整节点池的数量，即可扩缩容Nginx的副本。

#### 通过Deployment + HPA形式并指定调度规则部署
另一种部署方式是通过Deployment+HPA的形式部署。部署图如下：
![](https://main.qcloudimg.com/raw/5147b2ffbbf056bb1ef468780a3c4669.png)

1. 在集群中设置即将部署Nginx的节点的Lable。
2. 在集群组件页面安装好Nginx-ingress组件。
3. Nginx部署选项选择指定Deployment+HPA部署
4. 指定Nginx的调度规则
5. 设置Nginx Request和Limit
6. 完成安装。

使用Deployment + HPA形式， 您也可以根据业务需要配置污点和容忍将 Nginx和 业务Pod分散部署。 同时搭配HPA， 可设置nginx根据CPU/内存等指标进行弹性伸缩。


#### Nginx前端接入LB部署方式
仅部署Nginx在集群内，是无法接收外部流量， 您还需配置nginx的前端LB. 当前TKE已提供产品化的安装能力，您也可以根据业务需要选择不同的部署模式。
##### VPC-CNI模式集群使用CLB直通Nginx的Serivce（推荐）
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

### Nginx-ingress安装参数
#### TKE安装Nginx-ingress的默认参数

hongyu帮提供下
#### 您可以设置的Nginx-ingress参数和设置方式
##### 参数设置方式
您可以在Nginx-ingress组件详情页，Ningx参数tab中选择的Nginx-ingress实例进行YAML编辑。
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













