本方案结合腾讯云消息队列 CKafka、流计算 Oceanus、私有网络 VPC、商业智能分析 BI 等，对视频直播行业数字化运营进行实时可视化分析。分析指标包含观看直播人员的地区分布、各级别会员统计、各模块打赏礼物情况、在线人数等。
![](https://main.qcloudimg.com/raw/360d556df96fda14cd50de604d34a07d.png)

## 方案架构

根据以上视频直播场景所涉及的产品，包括流计算 Oceanus、私有网络 VPC、消息队列 CKafka、云数据库 MySQL、弹性 MapReduce 和商业智能分析 BI，设计的架构图如下：
![](https://main.qcloudimg.com/raw/837a51625ba06675db22a1773a9b0b6e.png)

## 前期准备

购买并创建相应的大数据组件。

### 创建私有网络 VPC

私有网络是一块您在腾讯云上自定义的逻辑隔离网络空间，在构建流计算 Oceanus、消息队列 CKafka、云数据库 MySQL、弹性 MapReduce 等服务时，选择的网络必须保持一致，网络才能互通。否则就需要使用对等连接、VPN 等方式打通网络。登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=8) 创建私有网络，详情请参见 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。

### 创建 Oceanus 集群

流计算 Oceanus 服务兼容原生的 Flink 任务。登录 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/cluster) 选择**集群管理 > 新建**创建集群，选择地域、可用区、VPC、日志、存储、设置密码等。VPC 及子网使用刚创建好的网络，详情可参见 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。创建完后 Flink 的集群如下：
![](https://main.qcloudimg.com/raw/c1da2235044cc634cb84647b26cf1744.png)


### 创建消息队列 Ckafka

消息队列 CKafka（Cloud Kafka）是基于开源 Apache Kafka 消息队列引擎，提供高吞吐性能、高可扩展性的消息队列服务。消息队列 CKafka 完美兼容 Apache kafka 0.9、0.10、1.1、2.4、2.8版本接口，在性能、扩展性、业务安全保障、运维等方面具有超强优势，让您在享受低成本、超强功能的同时，免除繁琐运维工作。

#### 创建 Ckafka 集群

登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka/index?rid=8)，单击**新建**，开始创建 Ckafka 集群，详情请参见 [创建实例](https://cloud.tencent.com/document/product/597/53207)。

>!私有网络和子网需选择之前创建的网络和子网。

![](https://main.qcloudimg.com/raw/03158f91f33ce5318ba6a528c01a9350.png)

#### 创建 topic

Ckafka 集群创建成功后，在实例列表中，单击新建的实例 **ID/名称**，进入实例详情页。
![](https://main.qcloudimg.com/raw/d4ccc00e8d4e38f702504cac0283d6e1.png)
在实例详情页，切换到 **topic 管理**页签，单击**新建**，开始创建 topic。
![](https://main.qcloudimg.com/raw/6855240a401a3909333a5d2f4e5867f7.png)

#### 模拟发送数据到 topic

- kafka 客户端
  进入同子网的 CVM 下，启动 kafka 客户端，模拟发送数据，具体操作参见 [运行 Kafka 客户端](https://cloud.tencent.com/document/product/597/56840)。
- 使用脚本发送
 - 脚本一：Java 参考地址：[使用 SDK 收发消息](https://cloud.tencent.com/document/product/597/54834)
 - 脚本二：Python 脚本生成模拟数据，具体如下：
```
#!/usr/bin/python3
# 首次使用该脚本，需 "pip3 install kafka" 安装kafka模块
import json
import random
import time
from kafka import KafkaProducer

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
PROVINCES = ["北京", "广东", "山东", "江苏", "河南", "上海", "河北", "浙江", "香港",
             "陕西", "湖南", "重庆", "福建", "天津", "云南", "四川", "广西", "安徽",
             "海南", "江西", "湖北", "山西", "辽宁", "台湾", "黑龙江", "内蒙古",
             "澳门", "贵州", "甘肃", "青海", "新疆", "西藏", "吉林", "宁夏"]

broker_lists = ['172.28.28.13:9092']
topic_live_gift_total = 'live_gift_total'
topic_live_streaming_log = 'live_streaming_log'

producer = KafkaProducer(bootstrap_servers=broker_lists,
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))

# 模拟几天前，几小时前的数据
pre_day_count = 0
pre_hour_count = 0
hour_unit = 3600
day_unit = 3600 * 24

def generate_data_live_gift_total():
    # construct time
    update_time = time.time() - day_unit * pre_day_count
    update_time_str = time.strftime(TIME_FORMAT, time.localtime(update_time))
    create_time = update_time - hour_unit * pre_hour_count
    create_time_str = time.strftime(TIME_FORMAT, time.localtime(create_time))
    results = []

    for _ in range(0, 10):
        user_id = random.randint(2000, 4000)
        random_gift_type = random.randint(1, 10)
        random_gift_total = random.randint(1, 100)
        msg_kv = {"user_id": user_id, "gift_type": random_gift_type,
                  "gift_total_amount": random_gift_total,
                  "create_time": create_time_str, "update_time": update_time_str}
        results.append(msg_kv)
    return results


def generate_live_streaming_log():
    # construct time
    update_time = time.time() - day_unit * pre_day_count
    leave_time_str = time.strftime(TIME_FORMAT, time.localtime(update_time))
    create_time = update_time - hour_unit * pre_hour_count
    create_time_str = time.strftime(TIME_FORMAT, time.localtime(create_time))
    results = []

    for _ in range(0, 10):
        user_id = random.randint(2000, 4000)
        random_province = random.randint(0, len(PROVINCES) - 1)
        province_name = PROVINCES[random_province]
        grade = random.randint(1, 5)
        msg_kv = {"user_id": user_id, "ip": "123.0.0." + str(user_id % 255),
                  "room_id": 20210813, "arrive_time": create_time_str,
                  "create_time": create_time_str, "leave_time": leave_time_str,
                  "region": 1122, "grade": (user_id % 5 + 1), "province": province_name}
        results.append(msg_kv)
    return results


def send_data(topic, msgs):
    count = 0

    # produce asynchronously
    for msg in msgs:
        import time
        time.sleep(1)
        count += 1
        producer.send(topic, msg)
        print(" send %d data...\n %s" % (count, msg))

    producer.flush()


if __name__ == '__main__':
    count = 1
    while True:
        time.sleep(60)
    #for _ in range(count):
        msg_live_stream_logs = generate_live_streaming_log()
        send_data(topic_live_streaming_log, msg_live_stream_logs)

        msg_topic_live_gift_totals = generate_data_live_gift_total()
        send_data(topic_live_gift_total, msg_topic_live_gift_totals)
```

### 创建 EMR 集群

弹性 MapReduce 是云端托管的弹性开源泛 Hadoop 服务，支持 Spark、HBase、Presto、Flink、Druid 等大数据框架，本次示例主要需要使用 Hbase 组件。

1. 登录 [弹性 MapReduce 控制台](https://console.cloud.tencent.com/emr)，选择**集群列表 > 新建集群**，开始新建集群，具体可参考 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。新建集群时，需选择安装 HBase 组件。
   ![](https://main.qcloudimg.com/raw/b8de93e041489aed3d8d9f847bd32f95.png)
   如果是生产环境，服务器配置可根据实际情况选择。网络需要选择之前创建好的 VPC 网络，始终保持服务组件在同一 VPC 下。
   ![](https://main.qcloudimg.com/raw/a3a63a677543d6b0f1218ff622861ced.png)
2. 在集群列表中，单击新建的集群 **ID/名称**，进入集群详情页。选择**集群资源 > 资源管理**，即进入 HBase 的 Master 节点。
   ![](https://main.qcloudimg.com/raw/0aed82b69a85b438530a375a4a355493.png)
3. 进入 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)，搜索 EMR **实例 ID**，然后单击**登录**进入服务器。
   ![](https://main.qcloudimg.com/raw/b0bb39c52bbb6bdf0fbc1853e0ed4cf5.png)
4. 创建 Hbase 表。
```
# 进入HBase命令
[root@172~]# hbase shell
# 建表语句
create 'dim_hbase', 'cf'
```

### 创建云数据库 MySQL

云数据库 MySQL（TencentDB for MySQL）是腾讯云基于开源数据库 MySQL 专业打造的高性能分布式数据存储服务，让用户能够在云中更轻松地设置、操作和扩展关系数据库。

登录 [云数据库 TencentDB](https://console.cloud.tencent.com/cdb) 控制台，单击**新建**，新建 MySQL 服务。**网络选择需为上文创建的网络。**
![](https://main.qcloudimg.com/raw/b5ece5f4675d723148cccd95fe5a8e43.png)
创建完 MySQL 服务后，需要修改 binlog 参数，如图修改为 FULL（默认值为 MINIMAL）。
![](https://main.qcloudimg.com/raw/fcbf3d43673bdf39a50993b5e8e22121.png)

修改完参数后，登录 MySQL 创建示例所需要的数据库和数据库表。
1. 进入实例详情页，单击**登录**，登录 MySQL 云数据库。
   ![](https://main.qcloudimg.com/raw/57436002f5ebb5d654008c1223912e77.png)
2. 新建数据库。
   打开 SQL 窗口或可视化页面创建数据库和表。
```
CREATE DATABASE livedb;     --创建数据库列表
```

### 创建商业智能分析
商业智能分析 BI（Business Intelligence，BI）支持自服务数据准备、探索式分析和企业级管控，是新一代的敏捷自助型 BI 服务平台。只需几分钟，您就可以在云端轻松自如地完成数据分析、业务数据探查、报表制作等一系列数据可视化操作。便捷的拖拉拽式交互操作方式，让您无需依赖 IT 人员，无需担心试错成本，快速洞察数据背后的关联、趋势和逻辑。

#### 购买商业智能分析

1. 登录 [商业智能分析 BI](https://cloud.tencent.com/product/bi) 控制台，使用主账号购买资源，购买时需根据创建的子账号数来进行购买。
   ![](https://main.qcloudimg.com/raw/187e6b711f7bcee4fd257f231f0bf584.png)
2. 子用户提出申请。
   ![](https://main.qcloudimg.com/raw/79bc7b2ef892a4fa4566970a0147f803.png)
3. 主账号审核通过。并给子用户授予添加数据源、创建数据集、查看报告的权限。

#### 添加 MySQL 数据源

>?这里选用开启外网方式连接，更多连接方式可参见 [数据库连接方式概览](https://cloud.tencent.com/document/product/590/19294)。

1. 打开购买的 MySQL 实例，开启外网。
   ![](https://main.qcloudimg.com/raw/4a3c22fcb48f1dfccb2818c659d388f8.png)
2. 将 SaaS BI（119.29.66.144:3306）添加到 MySQL 数据库安全组。
   ![](https://main.qcloudimg.com/raw/39817844630b406d5d7b32ec4147175e.png)![](https://main.qcloudimg.com/raw/3bb5e73b19bb62e80f6a255ec61df8cd.png)
   **这里添加的是 MySQL 3306 端口，不是外网映射的端口**。 
   ![](https://main.qcloudimg.com/raw/c21c60a7afea3edf913fddcd83caba9d.png)
3. 创建 MySQL 账户并配置权限。
   创建账户，并设置账号密码，**主机 IP 设置为%**。
   ![](https://main.qcloudimg.com/raw/05808ef1684dbda3cd1c56df70554026.png)![](https://main.qcloudimg.com/raw/34e38bb32d890452caa3499caa2d4289.png)
   设置账号权限。
   ![](https://main.qcloudimg.com/raw/d57797fa6b077da3fd530c52847ee021.png)![](https://main.qcloudimg.com/raw/2d2a619f57f0f62065a970d114f7c045.png)
4. 进入智能商业分析 BI，连接 MySQL 数据库。**添加数据源 > MySQL**，填写完成后单击**测试连接**。

## 方案实现

接下来通过案例为您介绍如何利用流计算服务 Oceanus 实现视频直播数字化运营的实时可视化数据处理与分析。

### 解决方案

#### 业务目标

这里只列举以下3种统计指标： 

- 全站观看直播用户分布
- 礼物总和统计
- 各模块进入直播间人数统计

#### 源数据格式

事件 log：live\_streaming\_log（topic）

| 字段         | 类型    | 含义         |
| :----------- | :------ | :----------- |
| user\_id     | bigint  | 客户号       |
| ip           | varchar | 客户 IP 地址 |
| room\_id     | bigint  | 房间号       |
| arrive\_time | varchar | 进入房间时间 |
| leave\_time  | varchar | 离开房间时间 |
| create\_time | varchar | 创建时间     |
| region\_code | int     | 地区编码     |
| grade        | int     | 会员等级     |
| province     | varchar | 所在省份     |

Ckafka 内部采用 json 格式存储，展现出来的数据如下所示：

```
{
	'user_id': 3165
	, 'ip': '123.0.0.105'
	, 'room_id': 20210813
	, 'arrive_time': '2021-08-16 09:48:01'
	, 'create_time': '2021-08-16 09:48:01'
	, 'leave_time': '2021-08-16 09:48:01'
	, 'region': 1122
	, 'grade': 1
	, 'province': '浙江'
}
```

礼物记录：live\_gift\_total（topic 名）

| 字段                | 类型    | 含义     |
| :------------------ | :------ | :------- |
| user\_id            | bigint  | 客户号   |
| gift\_type          | int     | 礼物类型 |
| gift\_total\_amount | bigint  | 礼物数量 |
| create\_time        | varchar | 创建时间 |
| update\_time        | varchar | 更新时间 |

```
{
     'user_id': 3994
     , 'gift_type': 3
     , 'gift_total_amount': 28
     , 'create_time': '2021-08-16 09:46:51'
     , 'update_time': '2021-08-16 09:46:51'
}
```

模块记录表：dim\_hbase（Hbase 维表）

| 字段       | 例子     | 含义         |
| :--------- | :------- | :----------- |
| rowkey     | 20210813 | 房间号       |
| module\_id | 0000     | 所属直播模块 |

#### Oceanus SQL 作业编写

全网观看直播用户分布（需提前在 MySQL 建表）

1. 定义 source
```sql
CREATE TABLE `live_streaming_log_source` (
     `user_id`       BIGINT,
     `ip`            VARCHAR,
     `room_id`       BIGINT, 
     `arrive_time`   VARCHAR,
     `leave_time`    VARCHAR,
     `create_time`   VARCHAR,
     `region_code`   INT,
     `grade`         INT,
     `province`      VARCHAR
 ) WITH (
     'connector' = 'kafka', 
     'topic' = 'live_streaming_log', 
     'scan.startup.mode' = 'earliest-offset', 
     'properties.bootstrap.servers' = 'xx.xx.xx.xx:xxxx',  
     'properties.group.id' = 'joylyu-consumer-2', 
     'format' = 'json',
     'json.ignore-parse-errors' = 'false', 
     'json.fail-on-missing-field' = 'false'
 );
```
2. 定义 sink
```sql
CREATE TABLE `live_streaming_log_sink` (
     `user_id`       BIGINT,
     `ip`            VARCHAR,
     `room_id`       VARCHAR, 
     `arrive_time`   TIMESTAMP,
     `leave_time`    TIMESTAMP,
     `create_time`   TIMESTAMP,
     `region_code`   VARCHAR,
     `grade`         INT,
     `province`      VARCHAR,
     primary key(`user_id`, `ip`,`room_id`,`arrive_time`) not enforced
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://xx.xx.xx.xx:xxxx/livedb?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai',          -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'live_streaming_log',    -- 需要写入的数据表
    'username' = 'root',                    -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'xxxxxxxxx',               -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '5000', 
    'sink.buffer-flush.interval' = '2s',
    'sink.max-retries' = '3'
);
```
3. 业务逻辑
```sql
INSERT INTO `live_streaming_log_sink`
SELECT 
CASE WHEN `user_id` IS NULL THEN 0000 ELSE `user_id` END AS `user_id`
, `ip`
, CAST(`room_id`     AS VARCHAR)   AS `room_id`
, CAST(`arrive_time` AS TIMESTAMP) AS `arrive_time`
, CAST(`leave_time`  AS TIMESTAMP) AS `leave_time`
, CAST(`create_time` AS TIMESTAMP) AS `create_time`
, CAST(`region_code` AS VARCHAR)   AS `region_code`
, `grade`
, `province`
FROM `live_streaming_log_source`;
```

礼物总和统计（需提前在 MySQL 建表）

1. 定义 source
```sql
 CREATE TABLE `live_gift_total_source` (
    `user_id` BIGINT,
    `gift_type` INT,
    `gift_total_amount` BIGINT,
    `create_time` VARCHAR,
    `update_time` VARCHAR
 ) WITH (
     'connector' = 'kafka',
     'topic' = 'live_gift_total',  -- 替换为您要消费的 Topic
     'scan.startup.mode' = 'earliest-offset',
     'properties.bootstrap.servers' = 'xx.xx.xx.xx:xxxx',  -- 替换为您的 Kafka 连接地址
     'properties.group.id' = 'demo3Group2',  -- 必选参数, 一定要指定 Group ID
     'format' = 'json',
     'json.ignore-parse-errors' = 'false',
     'json.fail-on-missing-field' = 'false'
 );
```
2. 定义 sink
```sql
CREATE TABLE `live_gift_total_amount_sink ` (
    `gift_type`         VARCHAR,
    `gift_total_amount` BIGINT,
    primary key(`gift_type`) not enforced
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://xx.xx.xx.xx:xxxx/livedb?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai',
    'table-name' = 'live_gift_total_amount',   -- 需要写入的数据表
    'username' = 'root',           -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'xxxxxxxxxxxxx',  -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '5000',
    'sink.buffer-flush.interval' = '2s',
    'sink.max-retries' = '3'
);
```
3. 业务逻辑
```sql
INSERT INTO `live_gift_total_amount_sink`
SELECT 
CAST(`gift_type` AS VARCHAR) AS `gift_type`
, SUM(`gift_total_amount`) AS `gift_total_amount_all`
FROM `live_gift_total_source`
GROUP BY CAST(`gift_type` AS VARCHAR);
```

各模块进入直播间人数统计（需提前在 MySQL 建表）

1. 定义 source
```sql
CREATE TABLE `live_streaming_log_source` (
     `user_id`       BIGINT,
     `ip`            VARCHAR,
     `room_id`       BIGINT, 
     `arrive_time`   VARCHAR,
     `leave_time`    VARCHAR,
     `create_time`   VARCHAR,
     `region_code`   INT,
     `grade`         INT,
     `province`      VARCHAR,
     `proc_time`  AS PROCTIME()
 ) WITH (
     'connector' = 'kafka',
     'topic' = 'live_streaming_log',                       -- 替换为您要消费的 Topic
     'scan.startup.mode' = 'earliest-offset',
     'properties.bootstrap.servers' = 'xx.xx.xx.xx:xxxx',  -- 替换为您的 Kafka 连接地址
     'properties.group.id' = 'demo3Group3',                -- 必选参数, 一定要指定 Group ID
     'format' = 'json',
     'json.ignore-parse-errors' = 'false',
     'json.fail-on-missing-field' = 'false'
 );
```
2. 定义 Hbase 维表
```sql
CREATE TABLE `dim_hbase` (
    `rowkey` STRING,
    `cf` ROW <`module_id` STRING>,
    PRIMARY KEY (`rowkey`) NOT ENFORCED
) WITH (
    'connector' = 'hbase-1.4',
    'table-name' = 'dim_hbase',
    'zookeeper.quorum' = 'xx.xx.xx.xx:8121,xx.xx.xx.xx:8121,xx.xx.xx.xx:8121'
);
```
3. 定义 sink
```sql
CREATE TABLE `live_module_number_count_sink` (
    `module_id` BIGINT,
    `module_number_count` BIGINT,
    primary key(`module_id`) not enforced
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://xx.xx.xx.xx:xxxx/livedb?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai',
    'table-name' = 'live_module_number_count',
    'username' = 'root',
    'password' = 'xxxxxxxxxxx',
    'sink.buffer-flush.max-rows' = '5000',
    'sink.buffer-flush.interval' = '2s',
    'sink.max-retries' = '3'
);
```
4. 业务逻辑
```sql
INSERT INTO `live_module_number_count_sink`
SELECT
CAST(dim_hbase.cf.module_id AS BIGINT) AS module_id,
COUNT(live_streaming_log_source.`user_id`) AS module_number_count
FROM `live_streaming_log_source`
JOIN `dim_hbase` for SYSTEM_TIME as of live_streaming_log_source.proc_time
 ON CAST(live_streaming_log_source.room_id AS STRING) = dim_hbase.rowkey
GROUP BY CAST(dim_hbase.cf.module_id AS BIGINT);
```

### 实时大屏可视化展示

#### 添加数据源

进入 [商业智能分析 BI](https://console.cloud.tencent.com/bi) 控制台，选择**添加数据源 > MySQL 数据库**，按上面方法连接到指定 MySQL 数据库，单击**保存**。

#### 创建数据集

选择**创建数据集 > SQL 数据集**（可根据实际业务场景选择其他数据集），从刚才的数据源中添加数据集，单击**保存**。

#### 制作报告

选择**制作报告 > 新建报告**（可选择任意模版），拖拽组件到中间空白处完成报告的制作。

设置实时刷新。选择左上角**报告设置 > 高级**，勾选获取实时数据，刷新间隔设置为3s（根据实际业务情况自行选择），这样可以根据 MySQL 数据源间隔3s一次自动刷新报告。完成后，单击**保存**即可。

具体步骤可参见 [基本操作](https://cloud.tencent.com/document/product/590/19753)。

#### 查看报告

单击**查看报告**，选择刚才保存的报告，可以动态展示报告。**此报告只做演示使用，可参见 [通用美化方法](https://cloud.tencent.com/document/product/590/19784) 优化报告。**如下图所示，大屏中总共6个图表。

- 图表1：用户地区分布。表示观看直播客户在全国范围内的地区分布。
- 图表2：各级别会员人数。表示各个会员等级的总人数。
- 图表3：礼物类型总和。表示收到各礼物类型的总和。
- 图表4：最近6h礼物总数统计。表示最近6小时收到的礼物总计和。
- 图表5：刷礼物排行前10。表示刷礼物最多的10个客户。
- 图表6：在线人数。当天每个时间段进入直播间的人数。

![](https://main.qcloudimg.com/raw/361f88e35da4065000b86fb9a3104396.png)
