## Logstash 简介
Logstash 是一个开源的日志处理工具，它可以从多个源头收集数据、过滤收集的数据以及对数据进行存储作为其他用途。

Logstash 灵活性强并且拥有强大的语法分析功能，其插件丰富，支持多种输入和输出源；同时其作为水平可伸缩的数据管道与 Elasticsearch 和 Kibana 配合在日志收集检索方面功能强大。

### Logstash 工作原理
Logstash 数据处理可以分为三个阶段：inputs → filters → outputs。
1. inputs：产生数据来源，例如文件、syslog、redis 和 beats 此类来源。
2. filter：修改过滤数据， 在 Logstash 数据管道中属于中间环节，可以根据条件去对事件进行更改。一些常见的过滤器如下：grok、mutate、drop 和 clone 等。
3. outputs：将数据传输到其他地方，一个事件可以传输到多个 outputs，当传输完成后这个事件就结束。Elasticsearch 就是最常见的 outputs。

同时 Logstash 支持编码解码，可以在 inputs 和 outputs 端指定格式。
![](https://mc.qcloudimg.com/static/img/17f1ac23a158b043091ebf48071f3a78/00.png)

## Logstash 接入 Kafka 的优势

![](https://mc.qcloudimg.com/static/img/bb8a396b1953ed487776281ef616a5c8/11.png)
- 可以异步处理数据，防止突发流量。
- 解耦，当 Elasticsearch 异常的时候不会影响上游工作。
- Logstash 过滤消耗资源，如果部署在生产 server 上会影响其性能。

## CKafka 接入
### 版本支持
#### inputs
官网版本兼容性说明如下：
![](https://mc.qcloudimg.com/static/img/7a25c5c3381a9f615701e88964ee8204/22.png)

当前最新版本为 v5.1.8 ，其使用 0.10 版本的 Consumer API 进行数据读取。

具体参数配置可见 [Kafka input plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-kafka.html)。
#### outputs
官网版本兼容性说明如下：

![](https://mc.qcloudimg.com/static/img/bd2ca98c3b0d392abe77a337450bb132/33.png)

当前最新版本为 v5.1.7，其使用 0.10 版本的 producer api 进行数据生产。

具体参数配置可见 [Kafka output plugin](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-kafka.html)。
### 准备工作
- Java 版本：java 8
- Logstash 版本：5.5.2 （August 17, 2017）
- Ckafka 实例，并且创建相应 topic

#### CKafka 创建
1. 拥有实例后，可从控制台中可以看到自己的实例信息。
![](https://mc.qcloudimg.com/static/img/67f19ef17a73e768fba188d58ae08f9a/44.png)
2. 单击实例名称可以看到实例分配的具体信息。
![](https://mc.qcloudimg.com/static/img/3841d4eb19ad992d35e60196b38498ce/55.png)
3. 单击 topic管理，创建 topic，此处名字为**logstash_test**。
![](https://mc.qcloudimg.com/static/img/30a006c20b8a9ba0a644336d5ddc501a/66.png)

至此，CKafka 相关的工作环境完成。

### CKafka 作为 inputs 接入
1. 执行`bin/logstash-plugin list`，查看已经支持的插件是否含有 logstash-input-kafka。
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/input1.png)

2. 编写配置文件 input.conf。
此处将标准输出作为数据重点，将 Kafka 作为数据来源。
```
input {
    kafka {
        bootstrap_servers => "172.16.16.12:9092" // ckafka vip 实例地址
        group_id => "logstash_group"  // ckafka groupid 名称
        topics => ["logstash_test"] // ckafka topic 名字
        consumer_threads => 3 // 消费线程数，一般跟 ckafka 分区数一致
        auto_offset_rest => "earliest"
    }
}
output {
    stdout{codec=>rubydebug}
}
```
3. 启动 Logstash，进行消息消费。
![](https://mc.qcloudimg.com/static/img/5c58f08f2fd0fff052cab655d00d4133/input3.png)
可以看到刚才 topic 中的数据现在被消费出来。

关于 Kafka 作为 output 的配置更多参数请参考 [Kafka output plugin](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-kafka.html#plugins-inputs-kafka-auto_offset_reset)。

### CKafka 作为 outputs 接入
1. 执行 bin/logstash-plugin list，查看已经支持的插件是否含有 logstash-output-kafka。
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/77.png)

2. 编写配置文件 output.conf。
此处将标准输入作为数据来源，将 Kafka 作为数据目的地。
![](https://mc.qcloudimg.com/static/img/661484fed328739fd12bedda0f5e2e67/88.png)

3. 启动 Logstash，进行消息生产。
![](https://mc.qcloudimg.com/static/img/c95bbc69c3f0ca36fa42efbb911b0a36/99.png)

4. 校验刚刚的生产数据。
![](https://mc.qcloudimg.com/static/img/ae85758a90a497235a90511770f959d2/10.png)

关于 Kafka 作为 output 的配置更多参数请参考 [Kafka output plugin](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-kafka.html)。




