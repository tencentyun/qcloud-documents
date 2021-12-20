## 操作场景

消息队列 CKafka 支持用户转储消息的能力，您可以将 CKafka 消息转储至 Elasticsearch Service（ES）便于海量数据存储搜索、实时日志分析等操作。

## 前提条件

该功能目前依赖 SCF、Elasticsearch 服务。使用时需提前开通云函数 SCF、Elasticsearch Service 等相关服务及功能。

## 操作步骤

### 转储消息[](id:1)

转储 Elasticsearch 的方案将使用 SCF 的 CKafka 触发器进行，通过 CKafka 触发器将消息转储到 Elasticsearch。

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，点击**topic管理**标签页，单击操作列的**消息转储**。
4. 单击**添加消息转储**，转储类型选择**Elasticsearch Service**。
   ![](https://main.qcloudimg.com/raw/ef35ef87117791731fffff3b6c8a28ff.png)
    - 转储类型：选择Elasticsearch Service 
    - 自建集群：如 ES 集群为自建集群，请将自建集群开关保持开启状态，并填写示例 IP。如 Elasticsearch 集群为腾讯云集群，则直接选取相关集群信息即可。
    - 实例集群：选取腾讯云 Elasticsearch Service 实例集群信息。
    - 实例用户名：输入 Elasticsearch 实例用户名，腾讯云 Elasticsearch 默认用户名为 elastic，且不可更改。
    - 实例密码：输入  Elasticsearch 实例密码。
    - 起始位置：转储时历史消息的处理方式，topic offset 设置。
    - 角色授权：使用云函数 SCF 产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
    - 云函数授权：知晓并同意开通创建云函数，该函数创建后需用户前往云函数设置更多高级配置及查看监控信息。
5. 创建完成后，单击**提交**，即可完成转储创建。创建完成后不会立即开启转储，需在控制台手动开启。

### 数据清洗设置

在创建流程中，无法直接跨进行数据清洗或字段定义等操作，需对函数代码进行自定义改造。数据清洗操作流程如下：

1. [新建 Elasticsearch 转储](#1)，并跳转到云函数控制台。
   ![](https://main.qcloudimg.com/raw/dcf1b93b0f91e90171977a63af50dead.png)
2. 在函数代码中修相关配置信息。
   ![](https://main.qcloudimg.com/raw/d53d4fd5aec72743c44be5b8efa623be.png)

当前模版代码拥有显性注释，可根据注释填写，主要配置列举：
```
# 自定义es索引
def createIndex(ES_Index_KeyWord, ES_Index_TimeFormat):
    # 这里可以自行更改自定义索引
    if ES_Index_TimeFormat == "day":
        ES_Index_TimeFormat = "%Y-%m-%d"
    elif ES_Index_TimeFormat == "hour":
        ES_Index_TimeFormat = "%Y-%m-%d-%H"

    index = ES_Index_KeyWord + '-' + datetime.datetime.now().strftime(ES_Index_TimeFormat)
    return index

# 定制日志清洗功能,将字符串中的敏感信息替换成***
def cleanData(data):
    try:
        if isinstance(data, str):
            for word in ES_Clean_Word:
                data = data.replace(word, "***")
        return data
    except:
        logger.error("Error occured when cleanning data")
        raise
```

### 日志查看与排障

CKafka 转储能力基于 SCF 实现，可在 [SCF 控制台](https://console.cloud.tencent.com/scf) 的日志中查询到相关转储的信息及转储状态。
![](https://main.qcloudimg.com/raw/70f36ef4d426b6aae1ca30301514bf56.png)

## 产品限制和费用计算

- 转储速度与 CKafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 CKafka 实例的峰值带宽。
- CKafkaToES 方案采用 CKafka 触发器，重试策略与最大消息数等设置参考 [CKafka 触发器](https://cloud.tencent.com/document/product/583/17530)。
- 使用消息转储 ES 能力，默认转储的信息为 CKafka 触发器的 msgBody 数据，如需自行处理参考 [CKafka 触发器的事件消息结构](https://cloud.tencent.com/document/product/583/17530#ckafka-.E8.A7.A6.E5.8F.91.E5.99.A8.E7.9A.84.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E7.BB.93.E6.9E.84)。 
- 该功能基于云函数 SCF 服务提供。SCF 为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。
