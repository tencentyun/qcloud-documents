## 操作场景
您可通过多个 Service 复用相同负载均衡器 CLB 的能力，来支持在同一个 VIP 同时暴露 TCP 及 UDP 的相同端口。
>!其他场景下均不建议使用多个 Service 复用相同的 CLB。
>



## 说明事项
- **于2020年8月17日前创建的集群，其 Service 创建的 CLB 默认支持复用相同的 CLB。**
开启复用功能的集群，其中 Service 创建的 CLB 将默认配置 `<serviceUUID>:tke-lb-serviceId` 和 `<serviceUUID>_<lb_listener_id>:<lb_listener_id>` 两个标签。每个 CLB 具备单独的 key 和 value，生成的标签数量较多。您可通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 联系我们关闭此类型集群的复用 CLB 功能，并清理标签。
- **于2020年8月17日起创建的集群，默认关闭多 Service 复用相同 CLB 的功能。**
关闭复用功能的集群，其中 Service 创建的 CLB 将默认配置 `tke-lb-serviceuuid:<serviceUUID>` 标签。所有 Service 使用同一批标签 Key，标签 Key 数量可控。您可通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_457) 联系我们开启需要使用多个 Service 复用相同 CLB 的功能。
- 如果您的集群是 EKS 集群，需要添加额外的 Annotation：`service.kubernetes.io/qcloud-share-existed-lb: true`

## 使用限制
- 在 Service 复用场景下，单个负载均衡管理的监听器数量不能超过10个。
- 在 Service 复用场景下，只能使用用户自行创建的负载均衡。因为容器服务 TKE 集群创建的负载均衡在被复用的情况下，负载均衡资源可能因为无法释放而导致泄漏。
- 如果需要使用当前 TKE 创建的负载均衡资源进行复用，可以在当前 Service 添加 `service.kubernetes.io/tke-existed-lbid` 注解，并删除该负载均衡上的 tke-createdBy-flag = yes 标签。
>! 使用当前 TKE 创建的负载均衡资源进行复用后，因为缺少了标签，该 CLB 的生命周期将不由 TKE 侧控制，需要自行管理，请谨慎操作。


## 操作步骤
1. [](id:Step1)参考 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)，创建集群所在 VPC 下的公网或内网类型的负载均衡。
2. 参考 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 或 [创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service)，创建 Loadbalancer 类型的 Service，选择**使用已有**负载均衡，并选择 [步骤1](#Step1) 中创建的负载均衡实例。如下图所示：
![](https://main.qcloudimg.com/raw/c2d52ea72c8270b4416cccb4766d5b7b.png)
3. 重复步骤2，即可完成通过多个 Service 复用相同负载均衡器 CLB。
