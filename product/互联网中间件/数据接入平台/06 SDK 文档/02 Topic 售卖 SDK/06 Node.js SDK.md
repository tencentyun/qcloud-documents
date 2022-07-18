## 操作场景

本文介绍使用  Node.js 客户端连接数据接入平台 Topic 并收发消息的操作步骤。

## 前提条件
- [安装 GCC](https://gcc.gnu.org/install/)
- [安装 Node.js](https://nodejs.org/en/download/)

## 操作步骤

### 步骤1：准备环境

#### 安装 C++依赖库
1. 执行以下命令切换到 yum 源配置目录 `/etc/yum.repos.d/`。
<dx-codeblock>
:::  bash
 cd /etc/yum.repos.d/
:::
</dx-codeblock>
2. 创建 yum 源配置文件 confluent.repo。
<dx-codeblock>
:::  repo
   [Confluent.dist]
   name=Confluent repository (dist)
   baseurl=https://packages.confluent.io/rpm/5.1/7
   gpgcheck=1
   gpgkey=https://packages.confluent.io/rpm/5.1/archive.key
   enabled=1   
   [Confluent]
   name=Confluent repository
   baseurl=https://packages.confluent.io/rpm/5.1
   gpgcheck=1
   gpgkey=https://packages.confluent.io/rpm/5.1/archive.key
   enabled=1
:::
</dx-codeblock>
3. 执行以下命令安装 C++ 依赖库。
<dx-codeblock>
:::  bash
yum install librdkafka-devel
:::
</dx-codeblock>

#### 安装 Node.js 依赖库
1. 执行以下命令为预处理器指定 OpenSSL 头文件路径。
<dx-codeblock>
:::  bash
export CPPFLAGS=-I/usr/local/opt/openssl/include
:::
</dx-codeblock>
2. 执行以下命令为连接器指定 OpenSSL 库路径。
<dx-codeblock>
:::  bash
export LDFLAGS=-L/usr/local/opt/openssl/lib
:::
</dx-codeblock>
3. 执行以下命令安装 Node.js 依赖库。
<dx-codeblock>
:::  bash
npm install i --unsafe-perm node-rdkafka
:::
</dx-codeblock>




### 步骤2：创建 Topic 和订阅关系

1. 在 DIP 控制台的 [Topic 列表](https://console.cloud.tencent.com/ckafka/datahub-topic) 页面创建一个 Topic。
![](https://qcloudimg.tencent-cloud.cn/raw/fcc78f33e0c82f8f1f99eabdf0d0f27c.png)
2. 单击 Topic 的 “ID” 进入基本信息页面，获取用户名、密码和地址信息。
![](https://qcloudimg.tencent-cloud.cn/raw/95b50b49c6240528c6743464beb77380.png)
3. 在**订阅关系**页签，新建一个订阅关系（消费组）。
   ![img](https://qcloudimg.tencent-cloud.cn/raw/ea08126a23715f24c50936d564421655.png)



### 步骤2：添加配置文件
<dx-codeblock>
:::  js
module.exports = {
    'sasl_plain_username': 'your_user_name',
    'sasl_plain_password': 'your_user_password',
    'bootstrap_servers': ["xxx.xx.xx.xx:port"],
    'topic_name': 'xxx',
    'group_id': 'xxx'
}
:::
</dx-codeblock>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><code>bootstrapServers</code></td>
<td align="left">接入地址，在 DIP 控制台的 Topic 基本信息页面获取。<img src="https://qcloudimg.tencent-cloud.cn/raw/2744b45621e463c3f7ff3d05493aa5dc.png" alt=""></td>
</tr>
<tr>
<td align="left"><code>sasl_plain_username</code></td>
<td align="left">用户名，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>sasl_plain_password</code></td>
<td align="left">用户密码，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>topic_name</code></td>
<td align="left">Topic 名称，在 DIP 控制台的 Topic 基本信息页面获取。</td>
</tr>
<tr>
<td align="left"><code>group.id</code></td>
<td align="left">消费组名称，在 DIP 控制台的 <strong>订阅关系</strong>列表获取。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/35b5e6e376fa3a3fbbe0ccedcafe8f69.png" alt=""></td>
</tr>
</tbody></table>







### 步骤3：生产消息

1. 编写生产消息程序 producer.js
<dx-codeblock>
:::  js
   const Kafka = require('node-rdkafka');
   const config = require('./setting');
   console.log("features:" + Kafka.features);
   console.log(Kafka.librdkafkaVersion);

   var producer = new Kafka.Producer({
       'api.version.request': 'true',
       'bootstrap.servers': config['bootstrap_servers'],
       'dr_cb': true,
       'dr_msg_cb': true,
       'security.protocol' : 'SASL_PLAINTEXT',
       'sasl.mechanisms' : 'PLAIN',
       'sasl.username' : config['sasl_plain_username'],
       'sasl.password' : config['sasl_plain_password']
   });

   var connected = false

   producer.setPollInterval(100);

   producer.connect();

   producer.on('ready', function() {
   connected = true
   console.log("connect ok")

   });

   function produce() {
   try {
       producer.produce(
       config['topic_name'],
       new Buffer('Hello CKafka SASL'),
       null,
       Date.now()
       );
   } catch (err) {
       console.error('Error occurred when sending message(s)');
       console.error(err);
   }
   }

   producer.on("disconnected", function() {
   connected = false;
   producer.connect();
   })

   producer.on('event.log', function(event) {
       console.log("event.log", event);
   });

   producer.on("error", function(error) {
       console.log("error:" + error);
   });

   producer.on('delivery-report', function(err, report) {
       console.log("delivery-report: producer ok");
   });
   // Any errors we encounter, including connection errors
   producer.on('event.error', function(err) {
       console.error('event.error:' + err);
   })

   setInterval(produce,1000,"Interval");
:::
</dx-codeblock>
2. 执行以下命令发送消息。
<dx-codeblock>
:::  bash
node producer.js
:::
</dx-codeblock>
3. 查看运行结果。
![](https://main.qcloudimg.com/raw/195f4aee06ba86755407b4a75812c256.png)

### 步骤4：消费消息
1. 创建消费消息程序 consumer.js。
<dx-codeblock>
:::  js
    consumer.on('event.log', function(event) {
       console.log("event.log", event);
   });

   consumer.on('error', function(error) {
       console.log("error:" + error);
   });

   consumer.on('event', function(event) {
           console.log("event:" + event);
   });
   const Kafka = require('node-rdkafka');
   const config = require('./setting');
   console.log(Kafka.features);
   console.log(Kafka.librdkafkaVersion);
   console.log(config)

   var consumer = new Kafka.KafkaConsumer({
       'api.version.request': 'true',
       'bootstrap.servers': config['bootstrap_servers'],
       'security.protocol' : 'SASL_PLAINTEXT',
       'sasl.mechanisms' : 'PLAIN',
       'message.max.bytes': 32000,
       'fetch.message.max.bytes': 32000,
       'max.partition.fetch.bytes': 32000,
       'sasl.username' : config['sasl_plain_username'],
       'sasl.password' : config['sasl_plain_password'],
       'group.id' : config['group_id']
   });

   consumer.connect();

   consumer.on('ready', function() {
   console.log("connect ok");
   consumer.subscribe([config['topic_name']]);
   consumer.consume();
   })

   consumer.on('data', function(data) {
   console.log(data);
   });

   consumer.on('event.log', function(event) {
       console.log("event.log", event);
   });

   consumer.on('error', function(error) {
       console.log("error:" + error);
   });

   consumer.on('event', function(event) {
           console.log("event:" + event);
   });
:::
</dx-codeblock>
2. 执行以下命令消费消息。
<dx-codeblock>
:::  bash
node consumer.js
:::
</dx-codeblock>
3. 查看运行结果。
![](https://main.qcloudimg.com/raw/deecbf58c00e07531b4ea703c4046b46.png)