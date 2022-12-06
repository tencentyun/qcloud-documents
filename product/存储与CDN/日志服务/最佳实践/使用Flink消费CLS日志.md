本文详细描述了如何使用Flink实时消费CLS日志，使用 Flink-sql 分析Nginx日志数据，

计算Web端的PV/UV 值，并将结果数据实时写入到自建的数据库Mysql 数据库。

**文中使用的组件/应用 及版本如下：**

| 技术组件/     | 版本                          |
|-----------|-----------------------------|
| Nginx     | 1.22                        |
| CLS日志服务   | -                           |
| Java      | openjdk version "1.8.0_232" |
| Scala     | 2.11.12                     |
| Flink sql | flink-1.14.5                |
| Mysql     | 5.7                         |

## 操作步骤
### 步骤1：安装腾讯云Nginx网关
1. 购买腾讯云主机CVM，请参考 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855)。
2. Nginx安装，请参考 [LINUX安装nginx详细步骤](https://cloud.tencent.com/developer/article/1654844)。
3. 成功通过浏览器访问nginx，并可以下图说明安装成功
![](https://qcloudimg.tencent-cloud.cn/raw/707ffb836a3af40d5cfcbaac25fda659.png)


### 步骤2：采集Nginx日志到腾讯云CLS日志服务
1. [配置Nginx日志采集](https://cloud.tencent.com/document/product/614/37735)。
2. CLS 日志服务采集终端 [Loglistener的安装](https://cloud.tencent.com/document/product/614/17414)，Loglistener类似于开源组件Beats，是用来采集日志数据的Agent。
3. 日志主题开启索引后，可以正常查询到Nginx的日志数据，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/270aa21653da799dbda8ef8d2d7acfee.png)
4. 最后，在CLS控制台 [开启kafka消费](https://cloud.tencent.com/document/product/614/72651)，使用 Kafka 协议消费功能，您可以将一个日志主题，当作一个 Kafka Topic 来消费。本文就是使用流计算框架Flink，实时消费Nginx日志数据,将实时计算的结果写入到Mysql。

### 步骤3：搭建MySQL数据库
参考文档：[创建 MySQL 实例](https://cloud.tencent.com/document/product/236/46433)

1. 登录数据库：
```
mysql -h 172.16.1.1 -uroot
```
2. 新建需要使用的db和表，例子中的db名为flink_nginx,表名为mysql_dest。
```
create database if not exists flink_nginx;
create table if not exists mysql_dest(
    ts timestamp,
    pv bigint,
    uv bigint
);
```

 

### 步骤4：部署Flink
1. 部署Flink 时，建议使用如下版本，否则可能会安装不成功。
	- [购买腾讯云主机CVM](https://cloud.tencent.com/document/product/213/4855)
	- [安装 KonaJDK v8.0.0](https://cloud.tencent.com/document/product/1149/38537)
	- [安装Scala 2.11.12](https://www.scala-lang.org/download/2.11.12.html)
2. 安装Flink 1.14.15 ，并进入SQL界面，从 [Apache Flink 官网](https://flink.apache.org/downloads.html#apache-flink-1145) 下载Flink 二进制代码包并开始安装。
```
# 解压缩flink 二进制包
tar -xf flink-1.14.5-bin-scala_2.11.tgz
cd flink-1.14.5

# 下载kafka相关依赖
wget https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka_2.11/1.14.5/flink-connector-kafka_2.11-1.14.5.jar
mv flink-connector-kafka_2.11-1.14.5.jar lib
wget https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.4.1/kafka-clients-2.4.1.jar
mv kafka-clients-2.4.1.jar lib

# 下载mysql相关依赖
wget https://repo1.maven.org/maven2/org/apache/flink/flink-connector-jdbc_2.11/1.14.5/flink-connector-jdbc_2.11-1.14.5.jar
mv flink-connector-jdbc_2.11-1.14.5.jar lib
wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.11/mysql-connector-java-8.0.11.jar
mv mysql-connector-java-8.0.11.jar lib
wget https://repo1.maven.org/maven2/org/apache/flink/flink-table-common/1.14.5/flink-table-common-1.14.5.jar
mv flink-table-common-1.14.5.jar lib

# 启动flink
bin/start-cluster.sh
bin/sql-client.sh
```
3. 当出现以下画面则说明安装成功。注意默认的网页端口是8081。
![](https://qcloudimg.tencent-cloud.cn/raw/d988fff8bdbbdcaad4f4a2452d5c9ec1.png)
![](https://qcloudimg.tencent-cloud.cn/raw/24bafef62a5f676b28f72f0693f851f9.png)
![](https://qcloudimg.tencent-cloud.cn/raw/964a9da5f694cbd8565001f058a5f52f.png)

### 步骤5：使用Flink消费CLS日志数据
1. 在SQL Client界面中，执行如下SQL：
```
-- 建数据源表消费kafka数据
CREATE TABLE `nginx_source`
(
    `remote_user` STRING,           -- 日志中字段，客户端名称
    `time_local` STRING,            -- 日志中字段，服务器本地时间
    `body_bytes_sent` BIGINT,       -- 日志中字段，发送给客户端的字节数
    `http_x_forwarded_for` STRING,  -- 日志中字段，当前端有代理服务器时，记录客户端真实 IP 地址的配
    `remote_addr` STRING,           -- 日志中字段，客户端 IP 地址
    `protocol` STRING,              -- 日志中字段，协议类型
    `status` INT,                   -- 日志中字段，HTTP 请求状态码
    `url` STRING,                   -- 日志中字段，url 地址
    `http_referer` STRING,          -- 日志中字段，访问来源的页面链接地址
    `http_user_agent` STRING,       -- 日志中字段，客户端浏览器信息
    `method` STRING,                -- 日志中字段，HTTP 请求方法
    `partition_id` BIGINT METADATA FROM 'partition' VIRTUAL,    -- kafka分区
    `ts` AS PROCTIME()                
)  WITH (
  'connector' = 'kafka',
  'topic' = 'YourTopic',  -- cls kafka协议消费控制台给出的的主题名称，例如out-633a268c-XXXX-4a4c-XXXX-7a9a1a7baXXXX 
  'properties.bootstrap.servers' = 'kafkaconsumer-ap-guangzhou.cls.tencentcs.com:9096',   -- cls kakfa协议消费控制台给出的服务地址，例子中是广州地域的外网消费地址，请按照您的实际情况填写
  'properties.group.id' = 'kafka_flink', -- kafka 消费组名称
  'scan.startup.mode' = 'earliest-offset', 
  'format' = 'json',
  'json.fail-on-missing-field' = 'false', 
  'json.ignore-parse-errors' = 'true' ,
  'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule required username="your username" password="your password";',--用户名是日志主题所属的日志集合ID，例如ca5cXXXX-dd2e-4ac0-af12-92d4b677d2c6，密码是用户的secretid#secrectkey组合的字符串，比AKIDWrwkHYYHjvqhz1mHVS8YhXXXX#XXXXuXtymIXT0Lac注意不要丢失#。
  'properties.security.protocol' = 'SASL_PLAINTEXT',
  'properties.sasl.mechanism' = 'PLAIN'
);

--- 建立目标表，写入mysql
CREATE TABLE `mysql_dest`
(
    `ts` TIMESTAMP,  
    `pv` BIGINT, 
    `uv` BIGINT 
)  WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://11.150.2.1:3306/flink_nginx?&amp;serverTimezone=Asia/Shanghai', -- 注意这边的时区设置
    'username'= 'username',     -- mysql账号
    'password'= 'password',     -- mysql密码
    'table-name' = 'mysql_dest' -- mysql表名
);

--- 查询kafka数据源表，计算后写入mysql目标表
INSERT INTO mysql_dest (ts,uv,pv)
SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE) start_ts, COUNT(DISTINCT remote_addr) uv,count(*) pv
FROM nginx_source
GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE);
```
2. 在Flink的任务监控页，我们可以看到任务的监控数据：
![](https://qcloudimg.tencent-cloud.cn/raw/9e59652be03ac35c9e4510c2b5cc7de3.png)
3. 进入 Mysql 数据库，就可以看到计算PV、UV的结果数据实时写入了。
![](https://qcloudimg.tencent-cloud.cn/raw/51cbfe4115a1130f03b24a823427b634.png)
