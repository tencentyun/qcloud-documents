## 操作场景
该任务指导您在购买 CKafka 服务后，使用 Kafka API。在腾讯云服务器上搭建 CKafka 环境后，本地下载并解压 Kafka 工具包，并对 Kafka API 进行简单测试。

## 前提条件
- 已 [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985)
- 已 [购买云服务器](https://buy.cloud.tencent.com/cvm)

## 操作步骤
### 1. 安装 JDK 环境
您需要先登录云服务器购买页 [选购云服务器](https://buy.cloud.tencent.com/cvm)，本次测试机器配置如下：
- 操作系统：CentOS 6.8 64 位 
- CPU：1核 
- 内存：2GB 
- 公网带宽：1Mbps 

完成选购后，给云服务器安装 JDK。具体操作步骤如下：

**1.1 下载 JDK**
可以通过`wget`命令获取，如果需要其他不同版本也可以在官网进行下载。
建议使用1.7以上版本的 JDK，本教程的版本为 jdk1.7.0_79。

**1.2 移动到固定文件夹并解压缩**
```
mkdir /usr/local/jdk
mv jdk-7u79-linux-x64.tar.gz /usr/local/jdk/
cd /usr/local/jdk/
tar -xzvf jdk-7u79-linux-x64.tar.gz
```
**1.3 配置环境变量**
```
vim /etc/profile
```
在文件末尾加入如下环境变量的配置：
```
export JAVA_HOME=/usr/local/jdk/jdk1.7.0_79(JDK的解压目录)  
export JRE_HOME=/usr/local/jdk/jdk1.7.0_79/jre
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH  
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JRE_HOME/lib
```
`wq`保存退出后，使用`source /etc/profile`命令使文件立即生效。

**1.4 验证**
通过以下命令验证环境是否安装完成（javac 命令也可以），查看版本号是否一致：
```
cd  $JAVA_HOME/bin
./java  -version
```
> ? `$JAVA_HOME` 为安装的 JDK 的主目录。

出现下图则证明 JDK 安装完成。
![](https://mc.qcloudimg.com/static/img/859143ff8986b24e80b3a9c3b31bd511/4.png)

### 2. 下载 Kafka 工具包
>!
> - 以下操作过程中提到的 $ip $port 变量，均指 CKafka 的接入 IP 和 port。
> - CKafka 实例可提供多个接入点（接入点指 $ip $port，最多支持6个接入点），满足多种网络环境下客户端的访问请求。在进行测试时，客户选择对应网络环境的接入点即可，例如客户端云服务器是私有网络环境，则选择私有网络下的 CKafka 接入点 $ip $port 进行测试即可。 接入点信息可以在实例详情页查看。

下载并解压 Kafka 安装包。（[Kafka 安装包官网下载地址>>](http://kafka.apache.org/downloads)）
当前 CKafka 100%兼容 Kafka 0.9 0.10版本，推荐0.10.2版本的安装包。建议您下载相应版本的安装包。

```
tar -C /opt -xzvf kafka_2.10-0.10.2.0.tgz    //解压到相应的目录中
```

下载解压完成后，无需配置其他环境，直接可用。
可以通过 telnet 指令测试本机是否连通到 CKafka 实例：
```
telnet $ip $port
```
![](https://mc.qcloudimg.com/static/img/c30a8d0e2fe57c109d3f7f1fa55b107f/5.png)

### 3. Kafka API 测试

**发送消息：**
```
./kafka-console-producer.sh --broker-list $ip:$port --topic topicName
This is a message
This is another message
```
其中 broker-list 中的 IP 即为 CKafka 实例中的 VIP，topicName 为 CKafka 实例中的 topic 名称。

**接收消息(CKafka 默认隐藏 Zookeeper 集群)：**
```
./kafka-console-consumer.sh --bootstrap-server $ip:$port --from-beginning --new-consumer --topic topicName
This is a message
This is another message
```
上述命令中，由于没有指定 Consumer Group 进行消费，系统会随机生成一个 Group 进行消费。这样做容易达到 Group 上限。因此推荐**指定 Group**的方式接收消息，首先需要在 consumer.properties 中配置下指定的 group name，如下图所示：
![](https://main.qcloudimg.com/raw/7ec8a2311776ac360ba0f4c18703fd8b.jpg)

配置完成后，指定 consumer group 的命令如下所示：
```
./kafka-console-consumer.sh --bootstrap-server $ip:$port --from-beginning --new-consumer --topic topicName --consumer.config ../config/consumer.properties
```
> ?ConsumerConfig 参数配置中，建议将 auto.offset.reset 配置为 earliest，防止新的消费者分组不存在时，遗漏消费消息的情况发生。 
原因：当创建一个新分组的消费者时，auto.offset.reset 值为 latest 时，表示消费最新的数据，即从 consumer 创建后生产的数据。这样会导致之前产生的数据不消费。

查看对应的 CKafka 监控：
![](https://main.qcloudimg.com/raw/0f958700c2ce2fa1654269f918660584.png)
