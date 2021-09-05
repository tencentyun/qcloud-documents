## Oceanus 简介

流计算 Oceanus 是位于云端的流式数据汇聚、计算服务。只需几分钟，您就可以轻松构建网站点击流分析、电商精准推荐、物联网 IoT 等应用。流计算基于 Apache Flink 构建，提供全托管的云上服务，您无须关注基础设施的运维，并能便捷对接云上数据源，获得完善的配套支持。

流计算 Oceanus 提供了便捷的控制台环境，方便用户编写 SQL 分析语句或者上传运行自定义 JAR 包，支持作业运维管理。基于 Flink 技术，流计算可以在 PB 级数据集上支持亚秒级的处理延时。

目前 Oceanus 使用的是独享集群模式，用户可以在自己的集群中运行各类作业，并进行相关资源管理。

## 前提条件

已 [创建实例](https://cloud.tencent.com/document/product/597/53207)。

## 操作步骤

### 步骤1：获取 CKafka 实例接入地址

CKafka 实例 与 Oceanus 集群在同一子网时，CKafka 接入地址为：
![Ckafka内网IP与端口](https://main.qcloudimg.com/raw/a28b5599889166095c168510ce1f5e89.png)

CKafka 实例与 Oceanus 集群不在同一子网时，您需要进行以下操作：

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=1)。
2. 在左侧导航栏选择**实例列表**，单击实例的“ID”，进入实例基本信息页面。
3. 在基本信息页面的**接入方式**模块里面，单击**添加路由策略**。
<img src="https://main.qcloudimg.com/raw/ac5165c4b3ddace8d02fe74e929099a5.png" width="600px">
4. **路由类型**选择 VPC 网络，**网络**选择 Oceanus 对应集群的网络。
<img src="https://main.qcloudimg.com/raw/bc0a5a5c981b723886a0ef37070fa430.png" width="600px">

### 步骤2: 创建 Topic

1. 在实例基本信息页面，选择顶部**Topic管理**页签。
2. 在 **Topic 管理**页面，单击**新建**，创建名为 oceanus_test1、oceanus_test2 的两个 Topic。
	 ![](https://main.qcloudimg.com/raw/9a8cb5c4a9679c4c2c8348409a3fa915.png)

### 步骤3: 接入 CKafka

1. 登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/job)。
2. 在**作业管理**页面单击左上角**新建**，创建作业（本文使用 SQL 作业，客户可自行选择作业类型）。
3. 选择已经创建好的“运行集群”。
<img src="https://main.qcloudimg.com/raw/1fe4b3fbcace97782f2da5192b0bc339.png" width="600px">
4. 进行 SQL 作业开发调试（本步骤实现 Oceanus 从 Ckafka 消费数据，并将数据写入 Ckafka 中）。
   1. 创建 source。
      ```sql
       CREATE TABLE `DataInput` (
             `request_time` VARCHAR,
             `client_ip` VARCHAR,
             `request_method` VARCHAR
       ) WITH (
           'connector' = 'kafka',   -- 可选 'kafka','kafka-0.11'. 注意选择对应的内置  Connector
           'topic' = 'oceanus_test1',  -- 替换为您要消费的 Topic
           'scan.startup.mode' = 'earliest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets 的任何一种
           'properties.bootstrap.servers' = 'IP地址:端口',  -- 替换为您的 Kafka 连接地址
           'properties.group.id' = 'testGroup',  -- 必选参数, 一定要指定 Group ID
           -- 定义数据格式 (JSON 格式)
           'format' = 'json',
           'json.ignore-parse-errors' = 'true',     -- 忽略 JSON 结构解析异常
           'json.fail-on-missing-field' = 'false'   -- 如果设置为 true, 则遇到缺失字段会报错 设置为 false 则缺失字段设置为 null
       );
      ```
   2. 创建 sink。
      ```sql
       CREATE TABLE `DataOutput` (
             `request_time` VARCHAR,
             `client_ip` VARCHAR,
             `request_method` VARCHAR
       ) WITH (
           'connector' = 'kafka',   -- 可选 'kafka','kafka-0.11'. 注意选择对应的内置  Connector
           'topic' = 'oceanus_test2',  -- 替换为您要消费的 Topic
           'properties.bootstrap.servers' = 'IP地址:端口',  -- 替换为您的 Kafka 连接地址
           -- 定义数据格式 (JSON 格式)
           'format' = 'json',
           'json.ignore-parse-errors' = 'true',     -- 忽略 JSON 结构解析异常
           'json.fail-on-missing-field' = 'false'   -- 如果设置为 true, 则遇到缺失字段会报错 设置为 false 则缺失字段设置为 null
       );
      ```
   3. 业务逻辑。
      ```sql
       INSERT INTO DataOutput
       SELECT * FROM DataInput;
      ```
   4. 单击**作业参数**，单击**内置Connector**，选择“flink-connector-kafka”，并单击**确认**保存。
<img src="https://main.qcloudimg.com/raw/fcba1d5e7ce69def4deb7e0f4c1124aa.png" width="600px">

>?具体实现请参考 [流计算 Oceanus 文档](https://cloud.tencent.com/document/product/849/48310)。
