## 操作场景

消息队列 CKafka 支持用户转储消息的能力，您可以将 CKafka 消息转储同步转储至消息队列 CKafka，用于 CKafka 集群间的数据同步。

## 前提条件

该功能目前依赖云函数（SCF）、消息队列 CKafka 服务。使用时需提前开通云函数 SCF 相关服务及功能。

## 操作步骤

### 转储消息[](id:1)

转储消息队列 CKafka 的方案将使用 SCF 的 CKafka 触发器进行，通过 CKafka 触发器将消息同步至消息队列另一个集群内。

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击**topic管理**标签页，单击操作列的**消息转储**。
4. 单击**添加消息转储**，选择转储类型为**消息队列（CKafka）**。
   ![](https://main.qcloudimg.com/raw/a0a0aa6c6fb77b0c248b4b51beabed95.png)
    - 转储类型：选择消息队列（CKafka）
    - 转储实例：拉取当前地域的 CKafka 实例列表，如需转储至其他地域或自建 Kafka 请参考 [自定义转储设置](#2)。
    - 转储 Topic：拉取所选实例的 CKafka Topic 信息。
    - 起始位置：转储时历史消息的处理方式，topic offset 设置。
    - 角色授权：使用云函数 SCF 产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
    - 云函数授权：知晓并同意开通创建云函数，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。
5. 创建完成后，单击**提交**，即可完成转储创建。创建完成后不会立即开启转储，需在控制台手动开启。

### 自定义转储设置

在通用创建流程中，无法直接跨地域或对自建 Kafka 进行转储，需对函数进行相关网络或投递信息设置。跨地域转储操作流程如下：

1. [新建 CKafka 转储模版](#1)，并跳转到云函数控制台，投递实例及 Topic 可任意填写。
   ![](https://main.qcloudimg.com/raw/e14ce2d4cf4076455f6a986726ca46dd.png)

2. 在函数配置中修改**环境变量**及**所属网络**配置。
   ![](https://main.qcloudimg.com/raw/b16778df86a40134bc4ca9e9f538e27f.png)

   环境变量配置说明：
   kafka_address ：Kafka IP 地址
   kafka_topic_name： Kafka Topic 名称

   > ?
   > - 如 CKafka 跨地域转储，修改相关环境变量即可，VPC 网络需配置**[对等连接](https://cloud.tencent.com/document/product/553/18836)**。
   > - 如 CVM 自建 Kafka，需修改为与自建 Kafka 相同的 VPC 及 Kafka Topic 信息。
   > - 如其他自建 Kafka，需修改环境变量的 IP 及 Topic 信息为自建信息；如无专线需用云函数公网传输。

3. 保存相关配置，并开启转储功能可完成转储。
   <img src="https://main.qcloudimg.com/raw/db05d6952c00395e8273401a146db8e8.png" width="60%" height="60%" />


## 更多配置说明

#### 接入方式

云函数支持 CKafka 的 `PLAINTEXT` 和 `SASL_PLAINTEXT` 两种接入方式，可在云函数代码中自行修改。

- `PLAINTEXT` 接入方式：
```
kafka_to_kafka = KafkaToKafka(kafka_address)
```

- `SASL_PLAINTEXT` 接入方式
 ```
 kafka_to_kafka= KafkaToKafka(    
    kafka_address    
    security_protocol = "SASL_PLAINTEXT",     
    sasl_mechanism="PLAIN",     
    sasl_plain_username="ckafka-80o10xxx#Taborxx",     
    sasl_plain_password="Taborxxxx",     
    api_version=(0, 10, 2)     
  )    
 ```

 >?sasl_plain_username 包含**实例 ID** 和**用户名**，使用 **#** 拼接。

#### 转储日志查看及排障

CKafka 转储能力基于 SCF 实现，可在 SCF 日志中查询到相关转储的信息及转储状态。
![](https://main.qcloudimg.com/raw/72b610569e7300bfca6edc6bb1c3a119.png)

## 产品限制和费用计算

- 转储速度与 CKafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 Ckafka 实例的峰值带宽。
- CKafkaToCKafka 方案采用 CKafka 触发器，重试策略与最大消息数等设置参考 [CKafka 触发器](https://cloud.tencent.com/document/product/583/17530)。
- 使用消息转储 CKafka 能力，默认转储的信息为 CKafka 触发器的 offset，msgBody 数据，如需自行处理参考 [CKafka 触发器的事件消息结构](https://cloud.tencent.com/document/product/583/17530#ckafka-.E8.A7.A6.E5.8F.91.E5.99.A8.E7.9A.84.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E7.BB.93.E6.9E.84)。 
- 该功能基于云函数 SCF 服务提供。SCF 为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。
