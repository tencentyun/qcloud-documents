### 腾讯云主机CKafka环境配置实践

云主机信息：
> 机器配置
操作系统	CentOS 6.8 64位
CPU	1核
内存	2GB
系统盘	20GB(云硬盘)	
数据盘	380GB(高性能云硬盘)	
公网带宽	1Mbps
系统镜像
镜像名称	CentOS 6.8 64位
类型	公有镜像
#### 1. 安装JDK环境
在腾讯云主机上搭建CKafka环境，首先需要安装JDK，
1.1 下载JDK，可以通过wget命令获取，如果需要其他不同版本也可以在官网进行下载。
```
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz  
```
1.2 移动到固定文件夹并解压缩：
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
在文件末尾加入如下环境变量的配置
```
export JAVA_HOME=/usr/local/jdk/jdk1.7.0_79(JDK的解压目录)  
export JRE_HOME=/usr/local/jdk/jdk1.7.0_79/jre
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH  
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JRE_HOME/lib
```
之后:wq保存退出
之后使用`source /etc/profile`命令使文件立即生效

1.4 验证
通过以下命令验证环境是否安装完成（javac命令也可以），查看版本号是否一致
```
java -version
```
出现下图则证明jdk安装完成。
![Alt text](./1494165796522.png)

#### 2.配置ZooKeeper

kafka安装包中自带zookeeper，不过选择自己手动下载安装更好。
1.1 下载解压
创建文件夹，进入文件夹下载并解压。
```
mkdir -p /usr/local/zookeeper
cd /usr/local/zookeeper
wget https://mirrors.tuna.tsinghua.edu.cn/apache/zookeeper/zookeeper-3.4.9/zookeeper-3.4.9.tar.gz
tar -zxvf zookeeper-3.4.9.tar.gz
```
1.2 修改zookeeper配置
进入到 /usr/local/zookeeper/zookeeper-3.4.9/conf 目录中，复制 zoo_sample.cfg 文件的并命名为为 zoo.cfg：
```
cd zookeeper-3.4.9/conf/
cp zoo_sample.cfg zoo.cfg
```
用vim命令打开zoo.cfg文件并修改内容：
```
# 数据文件夹
dataDir=/usr/local/services/zookeeper/zookeeper-3.4.9/data
# 日志文件夹
dataLogDir=/usr/local/services/zookeeper/zookeeper-3.4.9/logs
# 客户端访问 zookeeper 的端口号
clientPort=2181
```
1.3 配置zookeeper 的环境变量class path
```
vim /etc/profile
```
在文件末尾增加ZOOKEEPER_HOME，并更新PATH
```
export ZOOKEEPER_HOME=/usr/local/zookeeper/zookeeper-3.4.9/
export PATH=$ZOOKEEPER_HOME/bin:$PATH
```
之后重新使用`source /etc/profile`命令使文件立即生效
1.4 启动zookeeper服务
```
bin/zkServer.sh start &
```
 如打印如下信息则表明启动成功
  ZooKeeper JMX enabled by default
    Using config: /usr/local/services/zookeeper/zookeeper-3.4.9/bin/../conf/zoo.cfg
    Starting zookeeper ... STARTED
查询zookeeper状态，可以看到zookeeper使用的配置文件，运行模式等信息：
```
bin/zkServer.sh status
```   
![Alt text](./1494167036489.png)


#### 3.配置CKafka

1.1 下载并解压kafka安装包
Kafka官网地址: http://kafka.apache.org/ 
```
wget "http://mirrors.hust.edu.cn/apache/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz"
tar -xzvf kafka_2.11-0.9.0.1.tgz
mv kafka_2.11-0.9.0.1 /opt/
```
1.2 配置环境变量
将kafka_2.11-0.9.0.1/bin添加到path，以方便访问
`vim /etc/profile` 并在末尾添加KAFKA的环境变量
```
KAFKA_HOME=/opt/kafka_2.11-0.9.0.1
PATH=$PATH:$KAFKA_HOME/bin
```
配置完成后，环境变量示意图如下：
![Alt text](./1494165460040.png)

1.3 修改配置文件
```
cd /opt/kafka_2.11-0.9.0.1/config
vi server.properties
```
修改配置文件中的以下内容：
```
broker.id=0        //为依次增长的：0、1、2、3、4，集群中唯一id
log.dirs=/opt/kafka_2.11-0.9.0.1/logs    //日志地址
zookeeper.connect=master:2181,slave1:2181,slave2:2181 //zookeeperServers列表，各节点以逗号分开
```

1.4启动kafka单机模式
首先确保zookeeper已经启动，之后在kafka目录执行以下命令：
```
bin/kafka-server-start.sh config/server.properties &
```
如无报错则说明启动成功。&用于实现在后台启动。
可以使用`jps`命令查看当前所有java进程的pid
![Alt text](./kafka启动.png)

1.5 简单测试
创建topic
```
bin/kafka-topics.sh --zookeeper localhost:2181 --create --topic tinatest --partition 2 --replication-factor 1
bin/kafka-topics.sh --list --zookeepser localhost:2181 
```

