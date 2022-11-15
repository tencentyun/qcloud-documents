## 操作场景
您可通过多个 Service 复用相同负载均衡器 CLB 的能力，来支持在同一个 VIP 同时暴露 TCP 及 UDP 的相同端口。
>!其他场景下均不建议使用多个 Service 复用相同的 CLB。
>



## 说明事项 
- **于2020年8月17日前创建的 TKE 集群，其 Service 创建的 CLB 默认支持复用相同的 CLB。**
- **于2020年8月17日起创建的 TKE 集群，默认关闭多 Service 复用相同 CLB 的功能。**
关闭复用功能的集群，其中 Service 创建的 CLB 将默认配置 `tke-lb-serviceuuid:<serviceUUID>` ，`tke-createdBy-flag:yes`，`tke-clusterId:集群ID`这三个标签。所有 Service 使用同一批标签 Key，标签 Key 数量可控。您可通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 联系我们开启需要使用多个 Service 复用相同 CLB 的功能。
- **如果您的集群是 TKE Serverless 集群，集群默认已开启了 CLB 复用能力，但需要注意以下内容：**
	1. 用于复用的 CLB 必须为用户手动购买，而非 Serverless 集群自动购买。Serverless 集群自动购买的 CLB 在复用时会报错，是为了保护复用 CLB 的 Service 的 CLB 不被 Serverless 集群回收。
	2. CLB 购买成功后，需要在 Service 里添加两个 Annotation：
		- service.kubernetes.io/qcloud-share-existed-lb:"true"
		- service.kubernetes.io/tke-existed-lbid:lb-xxx
- Service 和 CLB 之间配置的管理和同步是由以 CLB ID 为名字的 LoadBalancerResource 类型的资源对象，请勿对该 CRD 进行任何操作，否则容易导致 Service 失效。


## 使用限制
- 在 Service 复用场景下，单个负载均衡管理的监听器数量由 CLB 的 TOTAL_LISTENER_QUOTA 限制，更多请[查看](https://cloud.tencent.com/document/product/214/47704)。
- 在 Service 复用场景下，只能使用用户自行创建的负载均衡。因为容器服务 TKE 集群创建的负载均衡在被复用的情况下，负载均衡资源可能因为无法释放而导致泄漏。

>! 使用当前 TKE 创建的负载均衡资源进行复用后，因为缺少了标签，该 CLB 的生命周期将不由 TKE 侧控制，需要自行管理，请谨慎操作。


## 操作步骤
1. [](id:Step1)参考 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)，创建集群所在 VPC 下的公网或内网类型的负载均衡。
2. 参考 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 或 [创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service)，创建 Loadbalancer 类型的 Service，选择**使用已有**负载均衡，并选择 [步骤1](#Step1) 中创建的负载均衡实例。如下图所示：
![](https://main.qcloudimg.com/raw/c2d52ea72c8270b4416cccb4766d5b7b.png)
3. 重复步骤2，即可完成通过多个 Service 复用相同负载均衡器 CLB。
