### 1. 查看CKafka实例，创建topic

申请通过后，您的CKafka控制台中会展示CKafka实例，点击实例信息可以查看实例详情。包括地域，内网vip，端口等信息。

![](https://mc.qcloudimg.com/static/img/fd6e90a028316b0ff8c960a81170dbbe/1.png)
![](https://mc.qcloudimg.com/static/img/a1428709e39e1a6124f7a265e47b6b37/2.png)

在topic管理页面，您可以创建topic，指定topic的分区个数和副本个数。
> 注，当前topic名称输入后无法更改。此外，分区个数指定后，只能进行新增分区的操作。副本数指定后无法更改。 
![](https://mc.qcloudimg.com/static/img/677df5a8c57fc9482867ea4e5ff9f77f/3.png)
创建好topic和分区后，可以通过云主机的kafka客户端对该实例进行生产和消费的操作。

### 2. 本地下载Kafka工具包

#### 2.1 安装JDK环境
本教程在腾讯云主机上搭建CKafka环境，首先可以在购买页[选购云主机](https://buy.qcloud.com/cvm)，并登入。本次测试机器配置如下：
> 机器配置 
操作系统 CentOS 6.8 64位 
CPU 1核 
内存 2GB 
公网带宽 1Mbps 

之后需要给云主机安装JDK。
a 下载JDK，可以通过wget命令获取，如果需要其他不同版本也可以在官网进行下载。
建议使用1.7以上版本的JDK，本教程的版本为jdk1.7.0_79

b 移动到固定文件夹并解压缩：
```
mkdir /usr/local/jdk
mv jdk-7u79-linux-x64.tar.gz /usr/local/jdk/
cd /usr/local/jdk/
tar -xzvf jdk-7u79-linux-x64.tar.gz
```
c 配置环境变量
```
vim /etc/profile
```
在文件末尾加入如下环境变量的配置
```
export JAVA_HOME=/usr/local/jdk/jdk1.7.0_79(JDK的解压目录)  
export JRE_HOME=/usr/local/jdk/jdk1.7.0_79/jre
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH  
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JRE_HOME/lib
```
wq保存退出后，使用`source /etc/profile`命令使文件立即生效

d 验证
通过以下命令验证环境是否安装完成（javac命令也可以），查看版本号是否一致
```
java -version
```
出现下图则证明jdk安装完成。
![](https://mc.qcloudimg.com/static/img/859143ff8986b24e80b3a9c3b31bd511/4.png)

#### 2.2 下载Kafka工具包

下载并解压kafka安装包
Kafka官网地址: http://kafka.apache.org/ 当前CKafka 100%兼容Kafka 0.9版本，建议您下载相应版本的安装包
```
wget "http://mirrors.hust.edu.cn/apache/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz"
tar -xzvf kafka_2.11-0.9.0.1.tgz
mv kafka_2.11-0.9.0.1 /opt/
```
下载解压完成后，无需配置其他环境，直接可用
可以通过telnet指令测试本机是否连通到CKafka实例
```
telnet ip 9092
```
![](https://mc.qcloudimg.com/static/img/c30a8d0e2fe57c109d3f7f1fa55b107f/5.png)

#### 2.3 Kafka API简单测试

发送消息
```
./kafka-console-producer.sh --broker-list xxx.xxx.xxx.xxx:9092 --topic topicName
This is a message
This is another message
```
> 其中broker-list中的ip即为CKafka实例中的vip，topicName为CKafka实例中的topic名称

接收消息(CKafka默认隐藏Zookeeper集群)
```
./kafka-console-consumer.sh --bootstrap-server xxx.xxx.xxx.xxx:9092 --from-beginning --new-consumer --topic topicName
This is a message
This is another message
```
上述命令中，由于没有指定consumer group进行消费，系统会随机生成一个group进行消费。这样做容易达到group上限。因此推荐如下方式接收消息：
**指定Group**
```
./kafka-console-consumer.sh --bootstrap-server xxx.xxx.xxx.xxx:9092 --from-beginning --new-consumer --topic topicName --consumer.config ../config/consumer.properties
```

查看对应的CKafka监控
![](https://mc.qcloudimg.com/static/img/12d49f97cc2562be26c16c193cb4297c/6.png)

### 3. 其他功能
#### 3.1 开启白名单
CKafka支持在topic维度开启ip白名单的功能，有效保证数据安全。
在新建topic和编辑topic页面均可以开启ip白名单。
![](https://mc.qcloudimg.com/static/img/02c8e7d5eeabb7f431b8b9c1f37cc636/7.png)

#### 3.2 设置消息保留时间
CKafka支持设置消息保留时间，以分钟为单位，最短1分钟，最长保留7天。
![](https://mc.qcloudimg.com/static/img/a9c9c921134c4a3a987f03b0f2d2f57e/8.png)
