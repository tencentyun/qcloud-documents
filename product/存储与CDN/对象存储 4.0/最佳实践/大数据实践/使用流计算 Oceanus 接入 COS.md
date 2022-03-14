## Oceanus 简介  

[流计算 Oceanus](https://cloud.tencent.com/document/product/849/16785) 是大数据生态体系的实时化分析利器。只需几分钟，您就可以轻松构建网站点击流分析、电商精准推荐、物联网 IoT 等应用。流计算基于 Apache Flink 构建，提供全托管的云上服务，您无须关注基础设施的运维，并能便捷对接云上数据源，获得完善的配套支持。

流计算 Oceanus 提供了便捷的控制台环境，方便用户编写 SQL 分析语句或者上传运行自定义 JAR 包，支持作业运维管理。基于 Flink 技术，流计算可以在 PB 级数据集上支持亚秒级的处理延时。

目前 Oceanus 使用的是独享集群模式，用户可以在自己的集群中运行各类作业，并进行相关资源管理。本文将为您详细介绍如何使用 Oceanus 对接 COS。

## 准备工作

#### 创建 Oceanus 集群

进入 [Oceanus 控制台](https://console.cloud.tencent.com/oceanus/overview)，单击左侧【集群管理】，单击左上方【创建集群】，具体可参见 [创建独享集群](https://cloud.tencent.com/document/product/849/48298) 文档。

#### 创建 COS 存储桶

进入 [COS 控制台](https://console.cloud.tencent.com/cos5)，单击左侧【存储桶列表】，单击【创建存储桶】，具体可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。

> ?当写入 COS 时，Oceanus 作业所运行的地域必须和 COS 在同一个地域。

## 实践步骤

进入 [Oceanus 控制台](https://console.cloud.tencent.com/oceanus/overview)，单击左侧【作业管理】，创建 SQL 作业，集群选择与 COS 在相同地域的集群。

#### 1. 创建 Source

```sql
CREATE TABLE `random_source` ( 
  f_sequence INT, 
  f_random INT, 
  f_random_str VARCHAR 
  ) WITH ( 
  'connector' = 'datagen', 
  'rows-per-second'='10',                  -- 每秒产生的数据条数
  'fields.f_sequence.kind'='random',       -- 随机数
  'fields.f_sequence.min'='1',             -- 随机数的最小值
  'fields.f_sequence.max'='10',            -- 随机数的最大值
  'fields.f_random.kind'='random',         -- 随机数
  'fields.f_random.min'='1',               -- 随机数的最小值
  'fields.f_random.max'='100',             -- 随机数的最大值
  'fields.f_random_str.length'='10'        -- 随机字符串的长度
);
```

> ?此处选用内置 connector `datagen`，请根据实际业务需求选择相应数据源，详情参见 [Oceanus 上下游开发指南](https://cloud.tencent.com/document/product/849/48310)。

#### 2. 创建 Sink

```sql
-- 请将<存储桶名称>和<文件夹名称>替换成您实际的存储桶名称和文件夹名称
CREATE TABLE `cos_sink` (
  f_sequence INT, 
  f_random INT, 
  f_random_str VARCHAR
) PARTITIONED BY (f_sequence) WITH (
    'connector' = 'filesystem',
    'path'='cosn://<存储桶名称>/<文件夹名称>/',                 --- 数据写入的目录路径
    'format' = 'json',                                       --- 数据写入的格式
    'sink.rolling-policy.file-size' = '128MB',               --- 文件最大大小
    'sink.rolling-policy.rollover-interval' = '30 min',      --- 文件最大写入时间
    'sink.partition-commit.delay' = '1 s',                   --- 分区提交延迟
    'sink.partition-commit.policy.kind' = 'success-file'     --- 分区提交方式
);
```

> ?更多 Sink 的 WITH 参数，请参见 [Filesystem (HDFS/COS)](https://cloud.tencent.com/document/product/849/53852) 文档。

#### 3. 业务逻辑

```sql
INSERT INTO `cos_sink`
SELECT * FROM `random_source`;
```

> !此处只做展示，无实际业务目的。

#### 4. 作业参数设置

在【内置 Connector】选择`flink-connector-cos`，在【高级参数】中对 COS 的地址进行如下配置：

```shell
fs.AbstractFileSystem.cosn.impl: org.apache.hadoop.fs.CosN
fs.cosn.impl: org.apache.hadoop.fs.CosFileSystem
fs.cosn.credentials.provider: org.apache.flink.fs.cos.OceanusCOSCredentialsProvider
fs.cosn.bucket.region: <COS 所在地域>
fs.cosn.userinfo.appid: <COS 所属用户的 appid>
```

作业配置说明如下：

- 请将`<COS 所在地域>`替换为您实际的 COS 地域，例如：ap-guangzhou。
- 请将`<COS 所属用户的 appid>`替换为您实际的 APPID，具体请进入 [账号中心](https://console.cloud.tencent.com/developer) 查看。 

> ?具体的作业参数设置请参见 [Filesystem (HDFS/COS)](https://cloud.tencent.com/document/product/849/53852) 文档。

#### 5. 启动作业

依次单击【保存】>【语法检查】>【发布草稿】，等待 sql 作业启动后，即可前往相应 COS 目录中查看写入数据。
