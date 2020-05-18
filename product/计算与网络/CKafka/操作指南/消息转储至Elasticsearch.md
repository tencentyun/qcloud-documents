## 操作场景
消息队列 CKafka 支持用户转储消息的能力，您可以将 Ckafka 消息转储至 Elasticsearch 便于海量数据存储搜索、实时日志分析等操作。

## 前提条件
该功能目前依赖 SCF，Elasticsearch 服务。使用时需提前开通云函数 SCF ，Elasticsearch Service 等相关服务及功能。

## 操作步骤

转储 Elasticsearch 的方案将使用SCF的Ckafka触发器进行，通过Ckafka触发器消息转储到 Elasticsearch。
1. 登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表页，单击目标实例 ID，进入**topic 管理**标签页。
3. 在 topic 管理标签页，单击操作列的【消息转储】。
4. 单击【添加消息转储】，选择转储类型为通用模板
![](https://main.qcloudimg.com/raw/97cb7d280c9939166964e282c5417d86.png)
 起始位置：转储时历史消息的处理方式，topic offset 设置。
5. 创建完成后单击【函数管理】链接，进入云函数控制台进行下一步操作。
![](https://main.qcloudimg.com/raw/c0a47a3ed0d59d92af8f80f7f74d8ec1.png)
6. 在云函数控制台上传 CkafkaToElasticsearch 模板代码 [Github下载地址](https://github.com/canmengfly/scf-demo-repo/tree/master/Python2.7-CkafkaToElasticsearch)，并进行相关参数修改。
![](https://main.qcloudimg.com/raw/41dce628f44c633eb8ff83a2197f97e8.png)
上传完毕后，在 index.py 文件中，将 Elasticsearch 的相关信息进行修改并保存。esIndex 索引需自行创建后填入。
![](https://main.qcloudimg.com/raw/3a7756a68cb7ea2b09384e275b1a74c6.png)
```
esServer = "http://172.16.16.53:9200"  # 修改为es server地址+端口 如：http://172.16.16.53:9200
esUsr = "elastic" # 修改为es用户名 如：elastic
esPw = "PW123213" # 修改为es密码 如：PW2312321321
esIndex = "pre1"  # es中已存在的index索引
```
8. 在云函数的【函数配置】中修改 VPC 网络，将云函数 VPC 网络与 Elasticsearch Service VPC 网络设为一致即可。
![](https://main.qcloudimg.com/raw/d31e7ff8e6204845ab7c1e885dc81b8a.png)
7. 在云函数触发器控制台中打开 Ckakfa 触发器。
![](https://main.qcloudimg.com/raw/2536fce389d053adc8ad23d19bef8bd1.png)

## 产品限制和费用计算
- 转储速度与 Ckafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 Ckafka 实例的峰值带宽。
- CkafkaToES 方案采用 Ckafka 触发器，重试策略与最大消息数等设置参考 [CKafka 触发器](https://cloud.tencent.com/document/product/583/17530)
- 使用消息转储 ES 能力，默认转储的信息为 CKafka 触发器的 msgBody 数据，如需自行处理参考 [CKafka 触发器的事件消息结构](https://cloud.tencent.com/document/product/583/17530#ckafka-.E8.A7.A6.E5.8F.91.E5.99.A8.E7.9A.84.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E7.BB.93.E6.9E.84)。 
- 该功能基于云函数 SCF 服务提供。SCF 为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。
