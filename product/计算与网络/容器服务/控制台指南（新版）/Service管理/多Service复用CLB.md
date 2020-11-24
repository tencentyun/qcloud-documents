## 操作场景
您可通过多个 Service 复用相同负载均衡器 CLB 的能力，来支持在同一个 VIP 同时暴露 TCP 及 UDP 的相同端口。
>!其他场景下均不建议使用多个 Service 复用相同的 CLB。
>



## 说明事项
- **于2020年8月17日前创建的集群，其 Service 创建的 CLB 默认支持复用相同的 CLB。**
开启复用功能的集群，其中 Service 创建的 CLB 将默认配置 `<serviceUUID>:tke-lb-serviceId` 和 `<serviceUUID>_<lb_listener_id>:<lb_listener_id>` 两个标签。每个 CLB 具备单独的 key 和 value，生成的标签数量较多。您可通过 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1%20TKE&step=1) 联系我们关闭此类型集群的复用 CLB 功能，并清理标签。
- **于2020年8月17日起创建的集群，默认关闭多 Service 复用相同 CLB 的功能。**
关闭复用功能的集群，其中 Service 创建的 CLB 将默认配置 `tke-lb-serviceuuid:<serviceUUID>` 标签。所有 Service 使用同一批标签 Key，标签 Key 数量可控。您可通过 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1%20TKE&step=1) 联系我们开启需要使用多个 Service 复用相同 CLB 的功能。

## 使用限制
- 在 Service 复用场景下，单个负载均衡管理的监听器数量不能超过10个。
- 在 Service 复用场景下，只能使用用户自行创建的负载均衡。因为容器服务 TKE 集群创建的负载均衡在被复用的情况下，负载均衡资源可能因为无法释放而导致泄漏。如果需要使用当前 TKE 创建的负载均衡资源进行复用，可以删除该负载均衡上的 `tke-createdBy-flag = yes` 标签。


## 操作步骤
1. <span id="Step1"></span>参考 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)，创建集群所在 VPC 下的公网或内网类型的负载均衡。
2. 参考 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 或 [创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service)，创建 Loadbalancer 类型的 Service，选择【使用已有】负载均衡，并选择 [步骤1](#Step1) 中创建的负载均衡实例。如下图所示：
![](https://main.qcloudimg.com/raw/055d05c1b455e7aad1c43b5de85d4f65.png)
3. 重复步骤2，即可完成通过多个 Service 复用相同负载均衡器 CLB。
