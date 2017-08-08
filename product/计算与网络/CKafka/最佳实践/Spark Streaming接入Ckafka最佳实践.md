## Spark Streaming简介
Spark Streaming是Spark Core的一个扩展，用于高吞吐且容错地处理持续性的数据，目前支持的外部输入有Kafka，Flume，HDFS/S3，Kinesis，Twitter和TCP socket。
 
![Alt text](https://mc.qcloudimg.com/static/img/b95ad071d2273bde7b9d8b64894c7ce6/111.png)

Spark Streaming将连续数据抽象成DStream(Discretized Stream)，而DStream由一系列连续的RDD(弹性分布式数据集)组成，每个RDD是一定时间间隔内产生的数据。使用函数对DStream进行处理其实即为对这些RDD进行处理。

![Alt text](https://mc.qcloudimg.com/static/img/f6f2869bc18bffc9a8e4e807276dd5a6/222.png)

目前Spark Streaming对kafka作为数据输入的支持分为稳定版本与实验版本：

| Kafka Version | spark-streaming-kafka-0.8 |   spark-streaming-kafka-0.10   |
| :-------- | :--------| :------|
| Broker Version	| 0.8.2.1 or higher |	0.10.0 or higher |
| Api Stability	| Stable |	Experimental |
| Language Support	| Scala, Java, Python |	Scala, Java |
| Receiver DStream	| Yes	| No |
| Direct DStream	| Yes	| Yes |
| SSL / TLS Support	| No	| Yes |
| Offset Commit Api	| No |	Yes |
| Dynamic Topic Subscription |	No|	Yes|


目前ckafka支持0.9.0.x，0.10.0.x，0.10.1.x，0.10.2.x版本，本次实践使用0.10.2.1版本的kafka依赖

## Spark Streaming接入CKafka

### 申请Ckafka实例
![Alt text](https://mc.qcloudimg.com/static/img/d7ee601da4d342cb2651d6a39db99e45/1501596501359.png)

确认网络类型是否与当前使用网络相符
### 创建topic
![Alt text](https://mc.qcloudimg.com/static/img/2d07bc5d5cac3be1ff03e7da099783f1/1501596195835.png)

这里创建了一个名为test的topic，接下来将以该topic为例子介绍如何生产消费
[内网IP与端口]即为生产消费需要用到的bootstrap-server
### 云主机环境
**Centos6.8系统**

| package  | version | 
| :-------- | :--------| 
| sbt    |   0.13.16 |  
| hadoop | 2.7.3 |
| spark | 2.1.0 |
| protobuf | 2.5.0 |
| ssh | CentOS默认安装 |
| Java | 1.8 |

### 向Ckafka中生产
目前ckafka支持0.9.0.x，0.10.0.x，0.10.1.x，0.10.2.x版本
这里使用0.10.2.1版本的kafka依赖
`build.sbt`
```scala
name := "Producer Example"
version := "1.0"
scalaVersion := "2.11.8"
libraryDependencies += "org.apache.kafka" % "kafka-clients" % "0.10.2.1"
```
`producer_example.scala`
```scala
import java.util.Properties
import org.apache.kafka.clients.producer._

object ProducerExample extends App {
    val  props = new Properties()
    props.put("bootstrap.servers", "172.16.16.12:9092") //实例信息中的内网ip与端口

    props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")

    val producer = new KafkaProducer[String, String](props)
    val TOPIC="test"  //指定要生产的topic
    for(i<- 1 to 50){
	        val record = new ProducerRecord(TOPIC, "key", s"hello $i") //生产key是"key",value是 hello i的消息
	        producer.send(record)
    }
    val record = new ProducerRecord(TOPIC, "key", "the end "+new java.util.Date)
    producer.send(record)
    producer.close() //最后要断开
}
```
有关更多ProducerRecord的用法可以查阅
https://kafka.apache.org/0100/javadoc/org/apache/kafka/clients/producer/ProducerRecord.html
### 从Ckafka消费
#### DirectStream
在`build.sbt`添加依赖
```scala
name := "Consumer Example"
version := "1.0"
scalaVersion := "2.11.8"
libraryDependencies += "org.apache.spark" %% "spark-core" % "2.1.0"
libraryDependencies += "org.apache.spark" %% "spark-streaming" % "2.1.0"
libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka-0-10" % "2.1.0"
```

`DirectStream_example.scala`
```scala
import org.apache.kafka.clients.consumer.ConsumerRecord
import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.kafka.common.TopicPartition
import org.apache.spark.streaming.kafka010._
import org.apache.spark.streaming.kafka010.LocationStrategies.PreferConsistent
import org.apache.spark.streaming.kafka010.ConsumerStrategies.Subscribe
import org.apache.spark.streaming.kafka010.KafkaUtils
import org.apache.spark.streaming.kafka010.OffsetRange
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import collection.JavaConversions._
import Array._

object Kafka {
    def main(args: Array[String]) {
        val kafkaParams = Map[String, Object](
            "bootstrap.servers" -> "172.16.16.12:9092",
            "key.deserializer" -> classOf[StringDeserializer],
            "value.deserializer" -> classOf[StringDeserializer],
            "group.id" -> "spark_stream_test1",
            "auto.offset.reset" -> "earliest",
            "enable.auto.commit" -> "false"
        )

        val sparkConf = new SparkConf()
        sparkConf.setMaster("local")
        sparkConf.setAppName("Kafka")
        val ssc = new StreamingContext(sparkConf, Seconds(5))
        val topics = Array("spark_test")

        val offsets : Map[TopicPartition, Long] = Map()

        for (i <- 0 until 3){
            val tp = new TopicPartition("spark_test", i)
            offsets.updated(tp , 0L)
        }
        val stream = KafkaUtils.createDirectStream[String, String](
            ssc,
            PreferConsistent,
            Subscribe[String, String](topics, kafkaParams)
        )
        println("directStream")
        stream.foreachRDD{ rdd=>
	        //输出获得的消息
            rdd.foreach{iter =>
                val i = iter.value
                println(s"${i}")
            }
            //获得offset
            val offsetRanges = rdd.asInstanceOf[HasOffsetRanges].offsetRanges
            rdd.foreachPartition { iter =>
                val o: OffsetRange = offsetRanges(TaskContext.get.partitionId)
                println(s"${o.topic} ${o.partition} ${o.fromOffset} ${o.untilOffset}")
            }
        }

        // Start the computation
        ssc.start()
        ssc.awaitTermination()
    }
}
```
#### RDD
`build.sbt`配置同上
`RDD_example`
```scala
import org.apache.kafka.clients.consumer.ConsumerRecord
import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.spark.streaming.kafka010._
import org.apache.spark.streaming.kafka010.LocationStrategies.PreferConsistent
import org.apache.spark.streaming.kafka010.ConsumerStrategies.Subscribe
import org.apache.spark.streaming.kafka010.KafkaUtils
import org.apache.spark.streaming.kafka010.OffsetRange
import org.apache.spark.streaming.{Seconds, StreamingContext}
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import collection.JavaConversions._
import Array._


object Kafka {
    def main(args: Array[String]) {
        val kafkaParams = Map[String, Object](
            "bootstrap.servers" -> "172.16.16.12:9092",
            "key.deserializer" -> classOf[StringDeserializer],
            "value.deserializer" -> classOf[StringDeserializer],
            "group.id" -> "spark_stream",
            "auto.offset.reset" -> "earliest",
            "enable.auto.commit" -> (false: java.lang.Boolean)
        )
        val sc = new SparkContext("local", "Kafka", new SparkConf())
        val java_kafkaParams : java.util.Map[String, Object] = kafkaParams
        //按顺序向parition拉取相应offset范围的消息，如果拉取不到则阻塞直到超过等待时间或者新生产消息达到拉取的数量
        val offsetRanges = Array[OffsetRange](
            OffsetRange("spark_test", 0, 0, 5),
            OffsetRange("spark_test", 1, 0, 5),
            OffsetRange("spark_test", 2, 0, 5)
        )
        val range = KafkaUtils.createRDD[String, String](
            sc,
            java_kafkaParams,
            offsetRanges,
            PreferConsistent
        )
        range.foreach(rdd=>println(rdd.value))
        sc.stop()
    }
}
```
更多`kafkaParams`用法参考http://kafka.apache.org/documentation.html#newconsumerconfigs

### 配置环境
#### 安装sbt
1. 在[sbt官网](http://www.scala-sbt.org/download.html)上下载sbt包
2. 解压后在sbt的目录下创建一个sbt_run.sh脚本并增加可执行权限
脚本内容如下：
```bash
#!/bin/bash
SBT_OPTS="-Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled -XX:MaxPermSize=256M"
java $SBT_OPTS -jar `dirname $0`/bin/sbt-launch.jar "$@"
```
```bash
chmod u+x ./sbt_run.sh
```

3. 执行
```bash
./sbt-run.sh sbt-version
```
若能看到sbt版本说明可以正常运行
#### 安装protobuf
1. 下载[protobuf](https://github.com/google/protobuf/releases)相应版本
2. 解压后进入目录
```bash
./configure
make && make install
```
*需要预先安装gcc-g++，执行中可能需要root权限*
3. 重新登录，在命令行中输入
```bash
protoc --version
```
4. 若能看到protobuf版本说明可以正常运行

#### 安装hadoop
1. 访问[hadoop官网](http://hadoop.apache.org/releases.html)下载所需要的版本
2. 增加hadoop用户
```bash
useradd -m hadoop -s /bin/bash
```
3. 增加管理员权限
```bash
visudo
```
4. 在`root ALL=(ALL) ALL`下增加一行
`hadoop ALL=(ALL) ALL`
保存退出
5. 使用hadoop进行操作
```bash
su hadoop
```
6. ssh无密码登录
```bash
cd ~/.ssh/                     # 若没有该目录，请先执行一次ssh localhost
ssh-keygen -t rsa              # 会有提示，都按回车就可以
cat id_rsa.pub >> authorized_keys  # 加入授权
chmod 600 ./authorized_keys    # 修改文件权限
```
7. 安装java
```bash
sudo yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel
```
8. 配置${JAVA_HOME}
```bash
vim /etc/profile
```
*在文末加上*
```vim
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.121-0.b13.el6_8.x86_64/jre
export PATH=$PATH:$JAVA_HOME
```
*根据安装情况修改对应路径*
9. 解压hadoop，进入目录
```bash
./bin/hadoop version
```
若能显示版本信息说明能正常运行
10. 配置单机伪分布式(可根据需要搭建不同形式的集群)
```bash
vim /etc/profile
```
*在文末加上*
```vim
export HADOOP_HOME=/usr/local/hadoop
export PATH=$HADOOP_HOME/bin:$PATH
```
*根据安装情况修改对应路径*
11. 修改`/etc/hadoop/core-site.xml`
```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```
12. 修改`/etc/hadoop/hdfs-site.xml`
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/data</value>
    </property>
</configuration>
```
13. 修改`/etc/hadoop/hadoop-env.sh`中的JAVA_HOME为java的路径
```vim
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.121-0.b13.el6_8.x86_64/jre
```
14. 执行NameNode格式化
```bash
./bin/hdfs namenode -format
```
看到`Exitting with status 0`说明成功
15. 启动hadoop
```bash
./sbin/start-dfs.sh
```
成功启动会存在`NameNode`进程，`DataNode`进程，`SecondaryNameNode`进程
#### 安装spark
访问[spark官网](http://spark.apache.org/downloads.html)下载所需要的版本
这里因为之前安装了hadoop选择使用*Pre-build with user-provided Apache Hadoop*
**这里同样使用`hadoop`用户进行操作**
1. 解压进入目录
2. 修改配置文件
```bash
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
vim ./conf/spark-env.sh
```
在第一行添加
```vim
export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)
```
*根据hadoop安装情况修改路径*
3. 运行例子
```bash
bin/run-example SparkPi
```
若成功安装可以看到程序输出π的近似值

