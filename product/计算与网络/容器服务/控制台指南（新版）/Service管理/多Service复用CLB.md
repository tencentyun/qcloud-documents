## 操作场景
您可通过多个 Service 复用相同负载均衡器 CLB 的能力，来支持在同一个 VIP 同时暴露 TCP 及 UDP 的相同端口。
>!其他场景下均不建议使用多个 Service 复用相同的 CLB。
>



## 说明事项
- **于2020年7月20日前创建的集群，其 Service 创建的 CLB 默认支持复用相同的 CLB。**
开启复用功能的集群，其中 Service 创建的 CLB 默认将配置 `tke-lb-serviceId:` 和 `<lb_listener_id>:<lb_listener_id>` 两个标签。每个 CLB 具备单独的 key 和 value，生成的标签数量较多。您可通过 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1%20TKE&step=1) 联系我们关闭此类型集群的复用 CLB 功能，并清理标签。
- **于2020年7月20日起创建的集群，默认关闭多 Service 复用相同 CLB 的功能。**
关闭复用功能的集群，其中 Service 创建的 CLB 默认将配置 `tke-lb-serviceId:` 和 `<lb_listener_id>:<lb_listener_id>` 两个标签。所有 Service 管理 CLB 复用同一批标签 Key，标签 Key 数量可控。

   

## 操作步骤
1. 参考 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment)，创建 Loadbalancer 类型的 Service。
2. <span id="Step2"></span>等待 Service 创建成功后，记录生成 CLB 的 ID 及名称。如下图所示： 
![](https://main.qcloudimg.com/raw/b3188b0c60ca1029d22bf4e5947bc12a.png)
3. 再次参考 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment)，使用 [步骤2](#Step2) 中已有的 CLB 创建第二个 Service。
