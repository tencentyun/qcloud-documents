## 查看 CKafka 实例，创建 topic

申请通过后，您的 CKafka 控制台中会展示 CKafka 实例，单击实例信息可以查看实例详情。包括地域、内网 VIP、端口等信息。

![](https://mc.qcloudimg.com/static/img/fd6e90a028316b0ff8c960a81170dbbe/1.png)
![](https://main.qcloudimg.com/raw/d4d33971683792a1f97d0a2f5b8ec8c1.png)

在 topic 管理页面，您可以创建 topic、指定 topic 的分区个数和副本个数。
> **注意：**
> 当前 topic 名称输入后无法更改。此外，分区个数指定后，只能进行新增分区的操作。副本数指定后无法更改。 

![](https://main.qcloudimg.com/raw/b8e3f81b1b041d1733fdce4134c98abb.png)
创建好 topic 和分区后，可以通过云服务器的 kafka 客户端对该实例进行生产和消费的操作。
分区数：一个物理上分区的概念，一个Topic可以包含一个或者多个partition，CKafka以partition作为分配单位
副本数：partition的副本个数，用于保障partition的高可用，为保障数据可靠性，当前不支持创建单副本topic，默认开启2副本。
>**注意：**这里的副本数也算分区个数的，比如说客户创建了topic 1个， 分区6 ， 副本2，那么分区额度一共用了1*6*2=12个。
如果超过了购买的最大分区个数，那么就会有提示，类似如下：

![](https://main.qcloudimg.com/raw/03f9a8d66de455120506ca868735b165.png)

## 本地下载 Kafka 工具包

### 1. 安装 JDK 环境
本教程在腾讯云服务器上搭建 CKafka 环境，首先可以在购买页 [选购云服务器](https://buy.cloud.tencent.com/cvm)，并登入。本次测试机器配置如下：
> 机器配置 
操作系统 CentOS 6.8 64 位 
CPU 1核 
内存 2GB 
公网带宽 1Mbps 

之后需要给云服务器安装 JDK。
1.1 下载 JDK，可以通过 wget 命令获取，如果需要其他不同版本也可以在官网进行下载。
建议使用 1.7 以上版本的 JDK，本教程的版本为 jdk1.7.0_79。

1.2 移动到固定文件夹并解压缩
```
mkdir /usr/local/jdk
mv jdk-7u79-linux-x64.tar.gz /usr/local/jdk/
cd /usr/local/jdk/
tar -xzvf jdk-7u79-linux-x64.tar.gz
```
1.3 配置环境变量
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
wq 保存退出后，使用`source /etc/profile`命令使文件立即生效。

1.4 验证
通过以下命令验证环境是否安装完成（javac 命令也可以），查看版本号是否一致：
```
cd  $JAVA_HOME/bin
./java  -version
```
> $JAVA_HOME 为安装的 JDK 的主目录

出现下图则证明 jdk 安装完成。
![](https://mc.qcloudimg.com/static/img/859143ff8986b24e80b3a9c3b31bd511/4.png)

### 2. 下载 Kafka 工具包
> **注意：**

> 以下步骤操作过程中提到的$ip $port 变量，指ckafka的接入ip 和prot；

> ckafka实例可提供多个接入点（接入点指$ip:$port，最多支持6个接入点。）满足多种网络环境下客户端的访问请求，在进行测试时，客户选择对应网络环境的接入点即可。例如 客户端cvm是vpc环境，则选择vpc网络下的ckafka接入点$ip $port 进行测试即可。 接入点信息可以在实例详情页查看。

下载并解压 kafka 安装包。（[Kafka 安装包官网下载地址>>](http://kafka.apache.org/downloads)）
当前 CKafka 100% 兼容 Kafka 0.9 0.10 版本，推荐0.10.2版本的安装包。建议您下载相应版本的安装包。

```
tar -C /opt -xzvf kafka_2.10-0.10.2.0.tgz    //解压到相应的目录中
```

下载解压完成后，无需配置其他环境，直接可用。
可以通过 telnet 指令测试本机是否连通到 CKafka 实例：
```
telnet $ip $port
```
![](https://mc.qcloudimg.com/static/img/c30a8d0e2fe57c109d3f7f1fa55b107f/5.png)

### 3. Kafka API 简单测试

**发送消息：**
```
./kafka-console-producer.sh --broker-list $ip:$port --topic topicName
This is a message
This is another message
```
其中 broker-list 中的 $ip:$port 即为 CKafka 实例的接入点 $ip和$port，topicName 为 CKafka 实例中的 topic 名称。

**接收消息(CKafka 默认隐藏 Zookeeper 集群)：**

```
./kafka-console-consumer.sh --bootstrap-server $ip:$port --from-beginning --new-consumer --topic topicName
This is a message
This is another message
```
上述命令中，由于没有指定 consumer group 进行消费，系统会随机生成一个 group 进行消费。这样做容易达到 group 上限。因此推荐 **指定 Group** 的方式接收消息，首先需要在 consumer.properties 中配置下指定的 group name，如下图所示：

![](https://main.qcloudimg.com/raw/7ec8a2311776ac360ba0f4c18703fd8b.jpg)

配置完成后，指定 consumer group 的命令如下所示：
```
./kafka-console-consumer.sh --bootstrap-server $ip:$port --from-beginning --new-consumer --topic topicName --consumer.config ../config/consumer.properties
```
> **注意：**
ConsumerConfig参数配置中，建议将auto.offset.reset配置为earliest，防止新的消费者分组不存在时，漏消费消息的情况发生。 

> 原因：当创建一个新分组的消费者时，auto.offset.reset 值为 latest 时，表示消费最新的数据，即从 consumer 创建后生产的数据。这样会导致之前产生的数据不消费。

查看对应的 CKafka 监控：
![](https://mc.qcloudimg.com/static/img/12d49f97cc2562be26c16c193cb4297c/6.png)

##  其他功能
###  开启白名单
CKafka 支持在 topic 维度开启 IP 白名单的功能，有效保证数据安全。
在新建 topic 和编辑 topic 页面均可以开启 IP 白名单。
![](https://mc.qcloudimg.com/static/img/02c8e7d5eeabb7f431b8b9c1f37cc636/7.png)

###  设置消息保留时间
CKafka 支持设置消息保留时间，以分钟为单位，最短 1 分钟，最长保留 30 天。
>**注意：**
>这里设置的消息保留时间，过期的消息就会被删除，而删除的机制是按照 ckafka 的分片批量删除的，不是立刻删除的，目前分片的大小是 1G，如果分片不到 1G 就不会删除。因此，假如您设置的是 1 分钟，而分片的数据大小在 1 分钟内无法增到 1G，那么这个时间是无效的，建议延长保留时间，这具体得看您数据的堆积速度。

![](https://mc.qcloudimg.com/static/img/a9c9c921134c4a3a987f03b0f2d2f57e/8.png)


