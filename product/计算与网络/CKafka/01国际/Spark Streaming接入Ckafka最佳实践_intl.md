## Introduction to Spark Streaming
Spark Streaming is an extension of Spark Core, which is used for high-throughput and fault-tolerant processing of the continuous data. The external inputs now supported include Kafka, Flume, HDFS/S3, Kinesis, Twitter, and TCP socket.
 
![Alt text](https://mc.qcloudimg.com/static/img/b95ad071d2273bde7b9d8b64894c7ce6/111.png)

Spark Streaming abstracts the continuous data into a DStream (Discretized Streams), while the DStream consists of a range of continuous RDDs (Resilient Distributed Datasets), and each RDD is the data generated within a certain time interval. The processing of DStream using functions is actually the processing of these RDDs.

![Alt text](https://mc.qcloudimg.com/static/img/f6f2869bc18bffc9a8e4e807276dd5a6/222.png)

Now, Spark Streaming's support for Kafka as data input is divided into stable version and experimental version:

| Kafka Version | spark-streaming-kafka-0.8 |   spark-streaming-kafka-0.10   |
| :-------- | :--------| :------|
| Broker Version	| 0.8.2.1 or higher |	0.10.0 or higher |
| Api Stability	| Stable |	Experimental |
| Language Support	| Scala, Java, Python |	Scala, Java |
| Receiver DStream	| Yes	| No |
| Direct DStream	| Yes	| Yes |
| SSL/TLS Support	| No	| Yes |
| Offset Commit Api	| No |	Yes |
| Dynamic Topic Subscription |	No |	Yes |


Now, the following versions of CKafka are supported: 0.9.0.x, 0.10.0.x, 0.10.1.x, and 0.10.2.x. The Kafka dependency of version 0.10.2.1 is used in this practice scenario.

## Connecting Spark Streaming to CKafka

### Applying for Ckafka Instance
![Alt text](https://mc.qcloudimg.com/static/img/186d7220a24ec7140859da3c5c9a2767/10775-01.jpg)

Confirm whether the network type matches the network that is now used
### Creating Topic
![Alt text](https://mc.qcloudimg.com/static/img/2565adebaee73ee5ab96d0a64d0916f6/10775-02.jpg)

We create a topic named spark_test here, and take this topic as an example to show how to produce and consume messages
[Private IP and Port] is the bootstrap-server to be used for production and consumption
### CVM Environment
**Centos 6.8 System**

| Package  | Version | 
| :-------- | :--------| 
| sbt    |   0.13.16 |  
| hadoop | 2.7.3 |
| spark | 2.1.0 |
| protobuf | 2.5.0 |
| ssh | CentOS installed by default |
| Java | 1.8 |

### Production in Ckafka
Now, the following versions of CKafka are supported: 0.9.0.x, 0.10.0.x, 0.10.1.x, and 0.10.2.x.
The kafka dependency of version 0.10.2.1 is used here.
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
    props.put("bootstrap.servers", "172.16.16.12:9092") //Private IP and port in the instance information

    props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")

    val producer = new KafkaProducer[String, String](props)
    val TOPIC="test"  //Specify the topic to be produced
    for(i<- 1 to 50){
	        val record = new ProducerRecord(TOPIC, "key", s"hello $i") //Produce a message with key being "key" and value being "hello i"
	        producer.send(record)
    }
    val record = new ProducerRecord(TOPIC, "key", "the end "+new java.util.Date)
    producer.send(record)
    producer.close() //To be disconnected at last.
}
```
For more usages of ProducerRecord, please see
https://kafka.apache.org/0100/javadoc/org/apache/kafka/clients/producer/ProducerRecord.html
### Consuming from CKafka
#### DirectStream
Add dependency to `build.sbt`
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
	        //Output the obtained messages
            rdd.foreach{iter =>
                val i = iter.value
                println(s"${i}")
            }
            //Obtain the offset
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
The configuration of `build.sbt` is the same as above
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
        //Pull the messages in the corresponding offset range to partition in order. The request is blocked if these messages cannot be pulled until the waiting time expires or the number of produced messages reaches the number for pulling.
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
For more usages of `kafkaParams`, please see http://kafka.apache.org/documentation.html#newconsumerconfigs

### Configuration of Environment
#### Installing "sbt"
1. Download sbt package from [sbt's official website](http://www.scala-sbt.org/download.html)
2. Create a sbt_run.sh script in the sbt directory after decompression, and add the execution permission
The content of script is as follows:
```bash
#!/bin/bash
SBT_OPTS="-Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled -XX:MaxPermSize=256M"
java $SBT_OPTS -jar `dirname $0`/bin/sbt-launch.jar "$@"
```
```bash
chmod u+x ./sbt_run.sh
```

3. Execute
```bash
./sbt-run.sh sbt-version
```
The display of sbt version indicates a normal operation

#### Installing "protobuf"
1. Download an appropriate version of [protobuf](https://github.com/google/protobuf/releases)
2. Decompress to enter the directory
```bash
./configure
make && make install
```
*You need to pre-install gcc-g++, and the root permission may be required during installation*
3. Log in again, and enter the following in the command line
```bash
protoc --version
```
4. The display of protobuf version indicates a normal operation

#### Installing "hadoop"
1. Go to [hadoop's official website](http://hadoop.apache.org/releases.html) to download the required version
2. Add hadoop users
```bash
useradd -m hadoop -s /bin/bash
```
3. Add admin permission
```bash
visudo
```
4. Add the following in a new line under `root ALL=(ALL) ALL`
`hadoop ALL=(ALL) ALL`
Save and exit
5. Use hadoop to operate
```bash
su hadoop
```
6. Configure ssh for password-less login
```bash
cd ~/.ssh/                     # If the directory does not exists, execute ssh localhost first
ssh-keygen -t rsa              # Just press Enter when prompted
cat id_rsa.pub >> authorized_keys  # Add authorization
chmod 600 ./authorized_keys    # Modify file permission
```
7. Install java
```bash
sudo yum install java-1.8.0-openjdk java-1.8.0-openjdk-devel
```
8. Configure ${JAVA_HOME}
```bash
vim /etc/profile
```
*Add the following at the end of text*
```vim
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.121-0.b13.el6_8.x86_64/jre
export PATH=$PATH:$JAVA_HOME
```
*Modify the corresponding path according to the installation*
9. Decompress hadoop, and go to the directory
```bash
./bin/hadoop version
```
The display of version information indicates a normal operation
10. Configure a pseudo-distribution stand-alone cluster (you can build different types of clusters as needed)
```bash
vim /etc/profile
```
*Add the following at the end of text*
```vim
export HADOOP_HOME=/usr/local/hadoop
export PATH=$HADOOP_HOME/bin:$PATH
```
*Modify the corresponding path according to the installation*
11. Modify `/etc/hadoop/core-site.xml`
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
12. Modify `/etc/hadoop/hdfs-site.xml`
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
13. Change JAVA_HOME in `/etc/hadoop/hadoop-env.sh` to java path
```vim
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.121-0.b13.el6_8.x86_64/jre
```
14. Format NameNode
```bash
./bin/hdfs namenode -format
```
The appearance of 'Exitting with status 0' indicates a successful installation
15. Start hadoop
```bash
./sbin/start-dfs.sh
```
`NameNode`, `DataNode` and `SecondaryNameNode` processes exist upon a successful startup

#### Installing "spark"
Go to [spark's official website](http://spark.apache.org/downloads.html) to download the required version
Since hadoop has been installed, use *Pre-build with user-provided Apache Hadoop* here
**Use `hadoop` user as well to operate here**
1. Decompress to enter the directory
2. Modify the configuration file
```bash
cp ./conf/spark-env.sh.template ./conf/spark-env.sh
vim ./conf/spark-env.sh
```
Add the following in the first line
```vim
export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)
```
*Modify the path according to the installation of hadoop*
3. Run the example
```bash
bin/run-example SparkPi
```
The display of an approximate value of π output by the program indicates a successful installation


