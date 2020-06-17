## 操作场景
消息队列 CKafka 支持用户转储消息的能力，您可以将 Ckafka 消息转储同步转储至消息队列 Ckafka，用于 Ckafka 集群间的数据同步。

## 前提条件
该功能目前依赖云函数（SCF）、消息队列 Ckafka 服务。使用时需提前开通云函数 SCF 相关服务及功能。

## 操作步骤

转储消息队列 Ckafka 的方案将使用 SCF 的 Ckafka 触发器进行，通过 Ckafka 触发器将消息同步至消息队列另一个集群内。
1. 登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表页，单击目标实例 ID，进入**topic 管理**标签页。
3. 在 topic 管理标签页，单击操作列的【消息转储】。
4. 单击【添加消息转储】，选择转储类型为通用模板
![](https://main.qcloudimg.com/raw/97cb7d280c9939166964e282c5417d86.png)
 起始位置：转储时历史消息的处理方式，topic offset 设置。
5. 创建完成后单击【函数管理】链接，进入云函数控制台进行下一步操作。
![](https://main.qcloudimg.com/raw/c0a47a3ed0d59d92af8f80f7f74d8ec1.png)
6. 在云函数控制台上传 CkafkaToCkafka 模板代码 [Github下载地址](https://github.com/tencentyun/scf-demo-repo/tree/master/Python2.7-CkafkaToCkafka)。
![](https://main.qcloudimg.com/raw/41dce628f44c633eb8ff83a2197f97e8.png)
7. 在云函数的【函数代码】中添加修改如下内容：
![](https://main.qcloudimg.com/raw/47205fb8eadbe4694b693c6a40b77c41.png)
```
Servers = "10.100.112.15:9092"  # 修改为Ckafka内网IP 地址+端口 E.g. 10.100.112.15:9092
Topic = "kafka2kafka" # 修改为 Ckafka Topic 名称 E.g. kafka2kafka
```
8. 在云函数的【函数配置】中修改 VPC 网络，将云函数 VPC 网络与想要同步投递的Ckafka集群 VPC 网络保持一致即可。
![](https://main.qcloudimg.com/raw/d31e7ff8e6204845ab7c1e885dc81b8a.png)
9. 在云函数触发器控制台中打开 Ckakfa 触发器。
![](https://main.qcloudimg.com/raw/2536fce389d053adc8ad23d19bef8bd1.png)


## 产品限制和费用计算
- 转储速度与 Ckafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 Ckafka 实例的峰值带宽。
- CkafkaToCkafka 方案采用 Ckafka 触发器，重试策略与最大消息数等设置参考 [CKafka 触发器](https://cloud.tencent.com/document/product/583/17530)
- 使用消息转储 Ckafka 能力，默认转储的信息为 CKafka 触发器的 offset，msgBody 数据，如需自行处理参考 [CKafka 触发器的事件消息结构](https://cloud.tencent.com/document/product/583/17530#ckafka-.E8.A7.A6.E5.8F.91.E5.99.A8.E7.9A.84.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E7.BB.93.E6.9E.84)。 
- 该功能基于云函数 SCF 服务提供。SCF 为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。
