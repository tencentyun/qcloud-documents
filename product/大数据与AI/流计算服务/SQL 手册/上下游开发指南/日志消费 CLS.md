## 介绍
CLS 提供了一站式的日志数据解决方案，在 Oceanus 中可以作为数据源（Source）。用户可以通过新建 CLS 日志主题，将 CLS 日志数据投递到 CLS 自行维护的 Kafka 中，通过 Kafka 的形式供 Oceanus 消费。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围

CLS 支持用作数据源表（Source）。

## 配置网络

建立 CLS Source 表前，需要配置网络信息，具体步骤如下：

1. 打开 [CLS 日志主题](https://console.cloud.tencent.com/cls/topic?region=ap-guangzhou) 页面中选择**日志主题 > 创建日志主题**，创建日志主题。
   ![](https://main.qcloudimg.com/raw/cfff31fc07d67bc51056788d90a6baf2.png)
2. 日志主题创建成功后，在列表页单击新建日志主题的**日志主题名称/ID** 进入到详情页面。
   ![](https://main.qcloudimg.com/raw/eb910d7411bf3bb131772b589ae9a680.png)
3. 在详情页，切换到**实时消费**页签，打开实时消费的功能。
   ![](https://main.qcloudimg.com/raw/d25a35c7b8ca7188f04ae4628bd184ac.png)
   开启后的状态如下：
   ![](https://main.qcloudimg.com/raw/f0ebde3e05ccc3d09bb12f355b704936.png)
4. 在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/cluster) 中，单击**集群名称/ID**，在集群详情页**集群信息**中，单击 **VPC** 网络。

>?由于 Oceanus VPC 的网络安全严格性，需要用户找到 CLS 团队拿到 Kafka VIP 的另外几个 IP 和端口一起配置到 VPC 下的 NAT 网关中。
>
>![](https://main.qcloudimg.com/raw/5b32339416ed805f85cefd8c31d2344f.png)
>在 VPC **网络资源**中，需自行配置 NAT 网关。
>![](https://main.qcloudimg.com/raw/9bf28a875a22449b061c1446c2547119.png)
>在 NAT 网关中新增路由策略。

 - 目的端：ping CLS 开放出的地址域名获取 IP 填写（IP 地址为上文提到的从 CLS 团队中提供的地址）
 - 下一跳类型：选择 NAT 网关
   ![](https://main.qcloudimg.com/raw/7f78c8bd464fd33a1439b77a52240c87.png)

5. NAT 网关配置完成后，即可使用 CLS 的实时消费功能。
   与消费 Kafka 数据方式一样，若有参数不清楚的地方，可参考 [消息队列 Kafka](https://cloud.tencent.com/document/product/849/48310)。

## Oceanus 建表语句示例

```sql 
-- 建表语句如下
CREATE TABLE `表名` (
       `Id` INT,
       `Name` VARCHAR
 ) WITH (
     'connector' = 'kafka',
     'topic' = '填入 CLS 实时消费发放的 Topic',
     'scan.startup.mode' = 'latest-offset', -- 可以是 latest-offset / earliest-offset / specific-offsets / group-offsets 的任何一种
     'properties.bootstrap.servers' = '填入 CLS 实时消费发放的 Kafka 地址',
     'properties.group.id' = 'Group Id',  -- 必选参数, 一定要指定 Group ID
 
     -- 定义数据格式 (JSON 格式)
     'format' = 'json',
     'json.ignore-parse-errors' = 'true',     -- 忽略 JSON 结构解析异常
     'json.fail-on-missing-field' = 'false',   -- 如果设置为 true, 则遇到缺失字段会报错 设置为 false 则缺失字段设置为 null

     'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="实例ID#用户名" password="用户密码";',
     'properties.security.protocol' = 'SASL_PLAINTEXT',
     'properties.sasl.mechanism' = 'PLAIN'
 );
```

## 注意事项
1. 支持实时消费的地域如下：
   广州、广州 Open、深圳金融、上海、上海金融、北京、北京金融、成都、重庆、中国台北、中国香港、新加坡、曼谷、孟买、首尔、东京、硅谷、弗吉尼亚（美国）、法兰克福、莫斯科。
2. CLS 提供的 Topic，集群带宽50MB/s（待定），您将和其它正在消费日志的租户共享这个带宽。如果需要高性能吞吐，可以单独购买 Ckafka 进行消费。
3. 需要找 CLS 团队给账号开白名单（暂时）。
4. CLS 实时消费功能使用费用：0.8元/GB的公网流量。
