## 操作场景
随着 Kafka 社区的繁荣，越来越多的用户开始使用 Kafka 来进行日志收集、大数据分析、流式数据处理等操作。而腾讯云消息队列 Ckafka 也借助了开源社区的力量，进行了如下优化：
- 基于 ApacheKafka 的分布式、高可扩展、高吞吐。
- 100%兼容 Apache KafkaAPI（0.9及0.10）。
- 无需部署，直接使用 Kafka 所有功能。
- 封装所有集群细节，无需用户运维。
- 对消息引擎优化，性能比社区最高提升50%。

腾讯云云函数与 Ckafka 也进行了深度联动，并推出了很多实用的功能。借助云函数和 Ckafka 触发器，可以非常方便实现 CKafka 消息转存到 COS、ES、DB 等，本文介绍使用云函数替代 Logstash，实现 Ckafka 消息罗盘 ES。如下图所示：
 ![](https://main.qcloudimg.com/raw/52bfb4c0ee549307c459212b5bbc6ef4.png)

 

## 运行原理
云函数可以实时消费 Ckafka 中的消息。例如，做数据转存、日志清洗、实时消费等。且数据转存的功能已集成到  Ckafka 控制台，用户可以一键开启使用，降低了用户使用的复杂度。如下图所示：
![](https://main.qcloudimg.com/raw/04b45265bc259b12f7c7103595ce7fd3.png)

## 方案优势

对比使用云服务器自建 Ckafka Consumer 的方式，云函数具备以下优势：
- 云函数控制台支持一键开启 Ckafka 触发器，帮助用户自动创建 Consumer，并由云函数平台来维护组件的高可用。
- Ckafka 触发器自身支持很多实用的配置：支持配置 offset 位置、支持配置1 - 1万消息聚合条数、支持配置1 - 1万次重试次数等。
- 基于云函数开发的业务逻辑，天然支持弹性伸缩，无需额外搭建和维护服务器集群等。
 
使用云函数和使用云服务器 CVM 自建 Logstash 对比，云函数具备以下优势：
- 云函数自带 Consumer 组件，可自行聚合。
- 云函数的模板函数已经实现了消息聚合和部分清洗能力，支持自行扩展。
- 云函数集群自带高可用和监控日志能力，业务上线速度更快。
- 云函数采用按实际使用收费，比自建集群费用更低廉，可以节省50%的费用。


## 前提条件
本文以**广州**地域为例：
- 需开启 Elasticsearch Service 服务。
- 需开启 Ckafka 服务。
 

## 操作步骤
### 创建云函数
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)，单击左侧导航栏的【函数服务】。
2. 在“函数服务”上方选择期望创建函数的地域，并单击【新建】，进入函数创建流程。
3. 在“新建函数”页面的“基本信息”步骤中，根据以下信息创建函数，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/9b0c1f124040a2ff3c079b48ccebd212.png)
	- **函数名称**：自定义函数名称，本文以 ckafka_to_es_demo 为例。
	- **运行环境**：选择 “Pyhton 3.6”。
	- **创建方式**：选择【模板函数】。
	- **模糊搜索**：输入“Ckafka”，并进行搜索。
单击模板中的【查看详情】，即可在弹出的“模板详情”窗口中查看相关信息，支持下载操作。
4. 在“函数配置”页面，保持默认配置并单击【完成】，即可完成函数的创建。
5. 进入已创建的云函数“函数配置”页面，单击右上角【编辑】，按以下信息填写函数配置：
 - **环境变量**：新增如下环境变量，参考表格进行填写。如下图所示：
![](https://main.qcloudimg.com/raw/aa4409842f15ca5198d453eeb4c9fa8e.png)
<table>
<tr>
<th>key</th><th>value</th><th>是否必填</th>
</tr>
<tr>
<td>ES_Address</td><td>ES 服务地址</td><td>是</td>
</tr>
<tr>
<td>ES_User</td><td>ES 用户名，默认为 elastic。</td><td>是</td>
</tr>
<tr>
<td>ES_Password</td><td>ES 用户登录密码。</td><td>是</td>
</tr>
<tr>
<td>ES_Index_KeyWord</td><td>ES 关键词索引。</td><td>是</td>
</tr>
<tr>
<td>ES_Log_IgnoreWord</td><td>需要删除的关键词，缺省则全量写入。例如，填写 name 或 password。</td><td>否</td>
</tr>
<tr>
<td>ES_Index_TimeFormat</td><td>按照天或者小时设置 Index，缺省则按照天建立索引。例如填写 hour。</td><td>否</td>
</tr>
</table>
 - **私有网络**：勾选“启用”，并选择与 ES 相同的 VPC。如下图所示：
![](https://main.qcloudimg.com/raw/157c97e4d342a81e2e3c3c574cd80da7.png)
6. 单击【保存】即可完成函数配置。



### 创建 Ckafka 触发器
1. 在“函数配置”页面，选择函数侧边栏【触发管理】，单击【创建触发器】。
2. 在弹出的“创建触发器”窗口中，参考以下信息进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/0e513da4e33ec49292af74e2d95fc9d5.png)
主要参数信息如下，其余参数请保持默认配置：
 - **触发方式**：选择 “Ckafka触发”。
 - **Ckafka实例及 Topic**：按需选择对应的 Topic。
 - **起始位置**：选择“从最开始位置开始消费”。
3. 单击【提交】即可完成触发器创建。





### 查看 ES 和函数运行日志
>!如果您还未将实际数据接入消息队列 Ckafka，您可以通过 [客户端工具](https://cloud.tencent.com/document/product/597/30932) 模拟消息生产。
>
- 选择函数侧边栏【日志查询】，即可查看函数运行日志。如下图所示：
![](https://main.qcloudimg.com/raw/da6d2085affcedc728c1b3e3b1bf6eb4.png)
- 查看 Kibana。详情请参见 [通过 Kibana 访问集群](https://cloud.tencent.com/document/product/845/19541)。
![](https://main.qcloudimg.com/raw/974199a28188cb11a43b5e89e5f660b5.png)





## 扩展能力
若您需实现高级日志清洗逻辑，可在如下图所示的代码位置中修改逻辑：
![](https://main.qcloudimg.com/raw/faa37c5784e21ad5ed250663b933103e.png)
