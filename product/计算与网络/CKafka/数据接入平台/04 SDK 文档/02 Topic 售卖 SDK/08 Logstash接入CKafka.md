Logstash 是一个开源的日志处理工具，可以从多个源头收集数据、过滤收集的数据并对数据进行存储作为其他用途。

Logstash 灵活性强，拥有强大的语法分析功能，插件丰富，支持多种输入和输出源。Logstash 作为水平可伸缩的数据管道，与 Elasticsearch 和 Kibana 配合，在日志收集检索方面功能强大。

## Logstash 工作原理

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

## 前提条件

- 下载并安装 Logstash，参见 [Download Logstash](https://www.elastic.co/guide/en/logstash/7.6/installing-logstash.html?spm=a2c4g.11186623.2.10.7d625287CKP6MX)。
- 下载并安装 JDK 8，参见 [Download JDK 8](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)。

## 操作步骤

### 步骤1：准备工作

1. 在 DIP 控制台的 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 页面创建一个 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/f5c42fc6c31b6a3b15ec587a395c1895.png)
2. 单击 Topic 的 “ID” 进入基本信息页面，获取用户名、密码和地址信息。
![](https://qcloudimg.tencent-cloud.cn/raw/d6d42ecac0a414fd23535419f760820c.png)
3. 在**订阅关系**页签，新建一个订阅关系（消费组）。
![](https://qcloudimg.tencent-cloud.cn/raw/ea08126a23715f24c50936d564421655.png)



### 步骤2：接入 CKafka

>?您可以单击以下页签，查看 CKafka 作为 inputs 或者 outputs 接入的具体步骤。



<dx-tabs>
:::作为\sinputs\s接入

1. 执行 `bin/logstash-plugin list`，查看已经支持的插件是否含有 logstash-input-kafka。
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/input1.png)
2. 在 .bin/ 目录下编写配置文件 input.conf。
   此处将标准输出作为数据终点，将 Kafka 作为数据来源。其中 kafka-client-jaas.conf 为 SASL-PLAINTEXT 的用户名和密码配置文件。
<dx-codeblock>
:::  bash
   input {
       kafka {
           bootstrap_servers => "xx.xx.xx.xx:xxxx" // ckafka 接入地址
           group_id => "logstash_group"  // ckafka groupid 名称
           topics => ["logstash_test"] // ckafka topic 名称
           consumer_threads => 3 // 消费线程数，一般与 ckafka 分区数一致
           auto_offset_reset => "earliest"
           security_protocol => "SASL_PLAINTEXT"
           sasl_mechanism => "PLAIN"
           jaas_path => "xx/xx/kafka-client-jaas.conf"
       }
   }
   output {
       stdout{codec=>rubydebug}
   }
:::
</dx-codeblock>kafka-client-jaas.conf 内容如下：
<dx-codeblock>
:::  json
   KafkaClient {
       org.apache.kafka.common.security.plain.PlainLoginModule required
       username="username"
       password="password";
   };
:::
</dx-codeblock>
3. 执行以下命令启动 Logstash，进行消息消费。
<dx-codeblock>
:::  SH
./logstash -f input.conf
:::
</dx-codeblock>返回结果如下：
![](https://mc.qcloudimg.com/static/img/5c58f08f2fd0fff052cab655d00d4133/input3.png)
可以看到刚才 Topic 中的数据被消费出来。

:::

:::作为\soutputs\s接入

1. 执行 `bin/logstash-plugin list`，查看已经支持的插件是否含有 logstash-output-kafka。
![](https://mc.qcloudimg.com/static/img/c5c876ea5ae5ce75307a5e307357e622/77.png)
2. 在.bin/目录下编写配置文件 output.conf。
   此处将标准输入作为数据来源，将 Kafka 作为数据目的地。其中 kafka-client-jaas.conf 为 SASL-PLAINTEXT 的用户名和密码配置文件。
<dx-codeblock>
:::  bash
   input {
         stdin{}
   }
   
   output {
      kafka {
           bootstrap_servers => "xx.xx.xx.xx:xxxx"  // ckafka 接入地址
           topic_id => "logstash_test" // ckafka topic 名称
           security_protocol => "SASL_PLAINTEXT"
           sasl_mechanism => "PLAIN"
           jaas_path => "xx/xx/kafka-client-jaas.conf"
          }
   }
:::
</dx-codeblock>kafka-client-jaas.conf 内容如下：
<dx-codeblock>
:::  json
   KafkaClient {
       org.apache.kafka.common.security.plain.PlainLoginModule required
       username="username"
       password="password";
   };
:::
</dx-codeblock>
3. 执行如下命令启动 Logstash，向创建的 Topic 发送消息。
<dx-codeblock>
:::  bash
./logstash -f output.conf
:::
</dx-codeblock>![](https://mc.qcloudimg.com/static/img/c95bbc69c3f0ca36fa42efbb911b0a36/99.png)
4. 启动 CKafka 消费者，检验上一步的生产数据。
![](https://mc.qcloudimg.com/static/img/ae85758a90a497235a90511770f959d2/10.png)

:::

</dx-tabs>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>bootstrapServers</code></td>
<td align="left">接入地址，在 DIP 控制台的 Topic 基本信息页面获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/7985a94a47d4289e03ced69ea362ad6b.png" alt=""></td>
</tr>
<tr>
<td align="left"><code>username</code></td>
<td align="left">用户名，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>password</code></td>
<td align="left">用户密码，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>topic_id</code></td>
<td align="left">Topic 名称，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>group.id</code></td>
<td align="left">消费组名称，在 DIP 控制台的 <strong>订阅关系</strong>列表获取。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/2599d62324e3aad68721553388c77478.png" alt=""></td>
</tr>
</tbody></table>





