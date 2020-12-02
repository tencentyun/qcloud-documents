## Logstash 简介
Logstash 是一个开源的日志处理工具，可以从多个源头收集数据、过滤收集的数据并对数据进行存储作为其他用途。

Logstash 灵活性强，拥有强大的语法分析功能，插件丰富，支持多种输入和输出源。Logstash 作为水平可伸缩的数据管道，与 Elasticsearch 和 Kibana 配合，在日志收集检索方面功能强大。

#### Logstash 工作原理
Logstash 数据处理可以分为三个阶段：inputs → filters → outputs。
1. inputs：产生数据来源，例如文件、syslog、redis 和 beats 此类来源。
2. filters：修改过滤数据， 在 Logstash 数据管道中属于中间环节，可以根据条件去对事件进行更改。一些常见的过滤器包括：grok、mutate、drop 和 clone 等。
3. outputs：将数据传输到其他地方，一个事件可以传输到多个 outputs，当传输完成后这个事件就结束。Elasticsearch 就是最常见的 outputs。

同时 Logstash 支持编码解码，可以在 inputs 和 outputs 端指定格式。
![](https://mc.qcloudimg.com/static/img/17f1ac23a158b043091ebf48071f3a78/00.png)

## Logstash 接入 Kafka 的优势
- 可以异步处理数据：防止突发流量。
- 解耦：当 Elasticsearch 异常的时候不会影响上游工作。

>!Logstash 过滤消耗资源，如果部署在生产 server 上会影响其性能。

![](https://mc.qcloudimg.com/static/img/bb8a396b1953ed487776281ef616a5c8/11.png)


## CKafka 接入
### 版本支持
#### inputs
官网版本兼容性说明如下：

| Kafka 客户端版本 | Logstash 版本 | Plugin 版本 | 
|---------|---------|---------|
| 0.8 | 2.0.0 - 2.x.x | < 3.0.0 |  
| 0.9 | 2.0.0 - 2.3.x | 3.x.x | 
| 0.9 | 2.4.x - 5.x.x | 4.x.x | 
| 0.10.0.x | 2.4.x - 5.x.x | 5.x.x | 

当前最新版本为 v5.1.8 ，其使用 0.10 版本的 Consumer API 进行数据读取。

具体参数配置可见 [Kafka input plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-kafka.html)。

#### outputs
官网版本兼容性说明如下：

| Kafka 客户端版本 | Logstash 版本 | Plugin 版本 |
|---------|---------|---------|
| 0.8 | 2.0.0 - 2.x.x | < 3.0.0 |  
| 0.9 | 2.0.0 - 2.3.x | 3.x.x  | 
| 0.9 | 2.4.x - 5.x.x | 4.x.x | 
| 0.10.0.x | 2.4.x - 5.x.x | 5.x.x  | 
 
当前最新版本为 v5.1.7，其使用 0.10 版本的 Producer API 进行数据生产。

具体参数配置可见 [Kafka output plugin](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-kafka.html)。

### 准备工作
- Java 版本：Java 8
- Logstash 版本：5.5.2 （August 17, 2017）
- Ckafka 实例，并且创建相应 topic

#### 创建 CKafka
1. 拥有实例后，可以从 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 中看到自己的实例信息。
![](https://main.qcloudimg.com/raw/1905d1d7ceb8e3b729af31e1ac7f52ca.png)
2. 单击实例名称可以看到实例分配的具体信息。
![](https://main.qcloudimg.com/raw/9c35869416313690ceff5fa9b9fb6c15.png)
3. 单击【topic管理】，创建 topic，此处名字为**logstash_test**。
![](https://main.qcloudimg.com/raw/2b43cdf1d5c2310d56bfd3837c524877.png)
至此，CKafka 相关的工作环境完成。

### CKafka 作为 inputs 接入
1. 执行`bin/logstash-plugin list`，查看已经支持的插件是否含有 logstash-input-kafka。
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/input1.png)

2. 编写配置文件 input.conf。
此处将标准输出作为数据终点，将 Kafka 作为数据来源。
```
input {
    kafka {
        bootstrap_servers => "172.16.16.12:9092" // ckafka vip 实例地址
        group_id => "logstash_group"  // ckafka groupid 名称
        topics => ["logstash_test"] // ckafka topic 名字
        consumer_threads => 3 // 消费线程数，一般跟 ckafka 分区数一致
        auto_offset_reset => "earliest"
    }
}
output {
    stdout{codec=>rubydebug}
}
```
3. 启动 Logstash，进行消息消费。
![](https://mc.qcloudimg.com/static/img/5c58f08f2fd0fff052cab655d00d4133/input3.png)
可以看到刚才 topic 中的数据现在被消费出来。


### CKafka 作为 outputs 接入
1. 执行 bin/logstash-plugin list，查看已经支持的插件是否含有 logstash-output-kafka。
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/77.png)

2. 编写配置文件 output.conf。
此处将标准输入作为数据来源，将 Kafka 作为数据目的地。
![](https://mc.qcloudimg.com/static/img/661484fed328739fd12bedda0f5e2e67/88.png)

3. 启动 Logstash，进行消息生产。
![](https://mc.qcloudimg.com/static/img/c95bbc69c3f0ca36fa42efbb911b0a36/99.png)

4. 校验上一步的生产数据。
![](https://mc.qcloudimg.com/static/img/ae85758a90a497235a90511770f959d2/10.png)



