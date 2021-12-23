Spark Streaming 是 Spark Core 的一个扩展，用于高吞吐且容错地处理持续性的数据，目前支持的外部输入有 Kafka、Flume、HDFS/S3、Kinesis、Twitter 和 TCP socket。
![Alt text](https://mc.qcloudimg.com/static/img/b95ad071d2273bde7b9d8b64894c7ce6/111.png)

Spark Streaming 将连续数据抽象成 DStream（Discretized Stream），而 DStream 由一系列连续的 RDD（弹性分布式数据集）组成，每个 RDD 是一定时间间隔内产生的数据。使用函数对 DStream 进行处理其实即为对这些 RDD 进行处理。
![Alt text](https://mc.qcloudimg.com/static/img/f6f2869bc18bffc9a8e4e807276dd5a6/222.png)

使用 Spark Streaming 作为 Kafka 的数据输入时，可支持 Kafka 稳定版本与实验版本：

| Kafka Version              | spark-streaming-kafka-0.8 | spark-streaming-kafka-0.10 |
| :------------------------- | :------------------------ | :------------------------- |
| Broker Version             | 0.8.2.1 or higher         | 0.10.0 or higher           |
| Api Maturity               | Deprecated                | Stable                     |
| Language Support           | Scala、Java、Python       | Scala、Java                |
| Receiver DStream           | Yes                       | No                         |
| Direct DStream             | Yes                       | Yes                        |
| SSL / TLS Support          | No                        | Yes                        |
| Offset Commit Api          | No                        | Yes                        |
| Dynamic Topic Subscription | No                        | Yes                        |


目前 CKafka 兼容 0.9及以上的版本，本次实践使用 0.10.2.1 版本的 Kafka 依赖。

此外，EMR 中的 Spark Streaming 也支持直接对接 CKafka，详见 [SparkStreaming 对接 CKafka 服务](https://cloud.tencent.com/document/product/589/12305)。

## 操作步骤

### 步骤1：获取 CKafka 实例接入地址

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏选择**实例列表**，单击实例的“ID”，进入实例基本信息页面。
3. 在实例的基本信息页面的**接入方式**模块，可获取实例的接入地址，接入地址是生产消费需要用到的 bootstrap-server。
   ![](https://main.qcloudimg.com/raw/a28b5599889166095c168510ce1f5e89.png)

### 步骤2：创建 Topic

1. 在实例基本信息页面，选择顶部**Topic管理**页签。
2. 在 Topic 管理页面，单击**新建**，创建一个名为 test 的 Topic，接下来将以该 Topic 为例介绍如何生产消费。
   ![](https://main.qcloudimg.com/raw/3576875138eb4447622571433312907f.png)



### 步骤3：准备云服务器环境

**Centos6.8 系统**

| package  | version         |
| :------- | :-------------- |
| sbt      | 0.13.16         |
| hadoop   | 2.7.3           |
| spark    | 2.1.0           |
| protobuf | 2.5.0           |
| ssh      | CentOS 默认安装 |
| Java     | 1.8             |

具体安装步骤参考 [配置环境](#配置环境)。

### 步骤4：对接 CKafka

<dx-tabs>
:::向\sCKafka\s中生产消息

这里使用 0.10.2.1 版本的 Kafka 依赖。

1. 在 `build.sbt` 添加依赖：

```scala
name := "Producer Example"
version := "1.0"
scalaVersion := "2.11.8"
libraryDependencies += "org.apache.kafka" % "kafka-clients" % "0.10.2.1"
```

2. 配置 `producer_example.scala`：
   <dx-codeblock>
   :::  scala
   import java.util.Properties
   import org.apache.kafka.clients.producer._
   object ProducerExample extends App {
    val  props = new Properties()
    props.put("bootstrap.servers", "172.16.16.12:9092") //实例信息中的内网 IP 与端口

    props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")

    val producer = new KafkaProducer[String, String](props)
    val TOPIC="test"  //指定要生产的 Topic
    for(i<- 1 to 50){
           val record = new ProducerRecord(TOPIC, "key", s"hello $i") //生产 key 是"key",value 是 hello i 的消息
           producer.send(record)
    }
    val record = new ProducerRecord(TOPIC, "key", "the end "+new java.util.Date)
    producer.send(record)
    producer.close() //最后要断开
   }
   :::
   </dx-codeblock>


更多有关 ProducerRecord 的用法请参考 [ProducerRecord](https://kafka.apache.org/0100/javadoc/org/apache/kafka/clients/producer/ProducerRecord.html) 文档。

:::

:::从\sCKafka\s消费消息

<span id="build.sbt"></span>

#### DirectStream

1. 在 `build.sbt` 添加依赖：

```scala
name := "Consumer Example"
version := "1.0"
scalaVersion := "2.11.8"
libraryDependencies += "org.apache.spark" %% "spark-core" % "2.1.0"
libraryDependencies += "org.apache.spark" %% "spark-streaming" % "2.1.0"
libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka-0-10" % "2.1.0"
```

2. 配置 `DirectStream_example.scala`：

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

1. 配置`build.sbt`（配置同上，[单击查看](#build.sbt)）。
2. 配置`RDD_example`：

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
        //按顺序向 parition 拉取相应 offset 范围的消息，如果拉取不到则阻塞直到超过等待时间或者新生产消息达到拉取的数量
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

更多 `kafkaParams` 用法参考 [kafkaParams](http://kafka.apache.org/documentation.html#newconsumerconfigs) 文档。

:::

</dx-tabs>

### 配置环境[](id:配置环境)

#### 安装 sbt

1. 在 [sbt 官网](http://www.scala-sbt.org/download.html) 上下载 sbt 包。
2. 解压后在 sbt 的目录下创建一个 sbt_run.sh 脚本并增加可执行权限，脚本内容如下：
```bash
#!/bin/bash
SBT_OPTS="-Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled -XX:MaxPermSize=256M"
java $SBT_OPTS -jar `dirname $0`/bin/sbt-launch.jar "$@"
```
 ```bash
chmod u+x ./sbt_run.sh
 ```
 
3. 执行以下命令。
```bash
./sbt-run.sh sbt-version
```

若能看到 sbt 版本说明可以正常运行。

#### 安装 protobuf

1. 下载 [protobuf](https://github.com/google/protobuf/releases) 相应版本。
2. 解压后进入目录。
```bash
./configure
make && make install
```
 需要预先安装 gcc-g++，执行中可能需要 root 权限。

3. 重新登录，在命令行中输入下述内容。
```bash
protoc --version
```

4. 若能看到 protobuf 版本说明可以正常运行。

#### 安装 Hadoop

1. 访问 [Hadoop 官网](http://hadoop.apache.org/releases.html) 下载所需要的版本。
2. 增加 Hadoop 用户。
```bash
useradd -m hadoop -s /bin/bash
```

3. 增加管理员权限。
```bash
visudo
```

4. 在`root ALL=(ALL) ALL`下增加一行。
   `hadoop ALL=(ALL) ALL`
   保存退出。
5. 使用 Hadoop 进行操作。
```bash
su hadoop
```

6. SSH 无密码登录。
```bash
cd ~/.ssh/                     # 若没有该目录，请先执行一次ssh localhost
ssh-keygen -t rsa              # 会有提示，都按回车就可以
cat id_rsa.pub >> authorized_keys  # 加入授权
chmod 600 ./authorized_keys    # 修改文件权限
```

7. 安装 Java。
```bash
sudo yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel
```

8. 配置 ${JAVA_HOME}。
```bash
vim /etc/profile
```
 在文末加上下述内容：
```vim
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.121-0.b13.el6_8.x86_64/jre
export PATH=$PATH:$JAVA_HOME
```
 根据安装情况修改对应路径。

9. 解压 Hadoop，进入目录。
```bash
./bin/hadoop version
```
 若能显示版本信息说明能正常运行。

10. 配置单机伪分布式（可根据需要搭建不同形式的集群）。
```bash
vim /etc/profile
```
 在文末加上下述内容：
```vim
export HADOOP_HOME=/usr/local/hadoop
export PATH=$HADOOP_HOME/bin:$PATH
```
 根据安装情况修改对应路径。

11. 修改 `/etc/hadoop/core-site.xml`。
<dx-codeblock>
:::  xml
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
:::
</dx-codeblock>


12. 修改 `/etc/hadoop/hdfs-site.xml`。
<dx-codeblock>
:::  xml
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
:::
</dx-codeblock>


13. 修改 `/etc/hadoop/hadoop-env.sh` 中的 JAVA_HOME 为 Java 的路径。
```vim
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.121-0.b13.el6_8.x86_64/jre
```

14. 执行 NameNode 格式化。
```bash
./bin/hdfs namenode -format
```
 显示`Exitting with status 0`则表示成功。

15. 启动 Hadoop。
```bash
./sbin/start-dfs.sh
```
成功启动会存在 `NameNode` 进程，`DataNode` 进程，`SecondaryNameNode` 进程。

#### 安装 Spark

访问 [Spark 官网](http://spark.apache.org/downloads.html) 下载所需要的版本。
因为之前安装了 Hadoop，所以选择使用 *Pre-build with user-provided Apache Hadoop*。
>?本示例同样使用 `hadoop` 用户进行操作。

1. 解压进入目录。
2. 修改配置文件。
```bash
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
vim ./conf/spark-env.sh
```
 在第一行添加下述内容：
```vim
export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)
```
 根据 hadoop 安装情况修改路径。

3. 运行示例。
```bash
bin/run-example SparkPi
```

 若成功安装可以看到程序输出 π 的近似值。

