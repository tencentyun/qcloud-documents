基于腾讯云的 EMR 服务您可以轻松结合腾讯云的 Ckafka 服务实现以下流式应用：
- 日志信息流式处理
- 用户行为记录流式处理
- 告警信息收集及处理
- 消息系统

## 1. 开发准备
- 因为任务中需要访问腾讯云消息队列 CKafka，所以需要先创建一个 CKafka 实例，具体见 [消息队列 CKafka](https://cloud.tencent.com/product/CKafka)。
- 确认您已开通腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群时需要在软件配置界面选择 Spark 组件。

## 2. 在 EMR 集群使用 Kafka 工具包
首先需要查看 CKafka 的内网 IP 与端口号。登录消息队列 CKafka 的控制台，选择您要使用的 CKafka 实例，在基本消息中查看其内网 IP 为 $kafkaIP，而端口号一般默认为9092。在 topic 管理界面新建一个 topic 为 spark_streaming_test。

登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里可选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入目录 `/usr/local/service/spark`：
```
[root@172 ~]# su hadoop
[root@172 root]$ cd /usr/local/service/spark
```

从 [Kafka 官网](http://kafka.apache.org/downloads) 下载安装包，注意选择合适的版本，具体可参考 [EMR 各版本 Kafka 与 Spark 版本说明](https://cloud.tencent.com/document/product/589/39697)。kafka 客户端版和腾讯云 ckafka 兼容性强，安装对应的 kafka 客户端版本即可。解压压缩包并将解压出来的文件夹移动到`/opt`目录下：
```
[hadoop@172 data]$ tar -xzvf kafka_2.10-0.10.2.0.tgz
[hadoop@172 data]$ mv kafka_2.10-0.10.2.0 /opt/
```
解压完成后，Kafka 工具直接能使用。可以使用`telnet`命令来测试 EMR 集群是否能够连接到 CKafka 实例：
```
[hadoop@172 kafka_2.10-0.10.2.0]$ telnet $kafkaIP 9092
Trying $kafkaIP...
Connected to $kafkaIP.
```
其中 $kafkaIP 为您创建的 CKafka 实例的内网 IP 地址。

下面可以简单测试 Kafka 工具包，同时用两个 WebShell 登录 EMR 集群并切换到 Hadoop 用户，进入 Kafka 的安装路径：
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /opt/kafka_2.10-0.10.2.0/
```
在第一个终端上连接 CKafka，并向其发送消息：
```
[hadoop@172 kafka_2.10-0.10.2.0]$ bin/kafka-console-producer.sh --broker-list $kafkaIP:9092 
--topic spark_streaming_test
hello world
this is a message
```
在另一个终端上连接 CKafka，并作为消费者获得其中的数据：
```
[hadoop@172 kafka_2.10-0.10.2.0]$ bin/kafka-console-consumer.sh --bootstrap-server 
$kafkaIP:9092 --from-beginning --new-consumer --topic spark_streaming_test
hello world
this is a message
```

## 3. 使用 SparkStreaming 对接 CKafka 服务
在消费者一端，我们利用 Spark Streaming 从 CKafka 中不断拉取数据进行词频统计，即对流数据进行 WordCount 的工作。在生产者一端，也采用程序不断的产生数据，来不断输送给 CKafka。

首先 [下载并安装 Maven](http://maven.apache.org/download.cgi)，配置好 Maven 的环境变量，如果您使用 IDE，请在 IDE 中设置好 Maven 相关配置。

### 创建 Spark Streamin 消费者工程
在本地命令行下进入您想要新建工程的目录，例如`D://mavenWorkplace`中，输入如下命令新建一个 Maven 工程：
```
mvn   archetype:generate   -DgroupId=$yourgroupID   -DartifactId=$yourartifactID 
-DarchetypeArtifactId=maven-archetype-quickstart
```
其中 $yourgroupID 即为您的包名。$yourartifactID 为您的项目名称，maven-archetype-quickstart 表示创建一个 Maven Java 项目。工程创建过程中需要下载一些文件，请保持网络通畅。

创建成功后，在`D://mavenWorkplace`目录下就会生成一个名为 $yourartifactID 的工程文件夹。其中的文件结构如下所示：
```
simple
　　　---pom.xml　　　　核心配置，项目根下
　　　---src
　　　　　---main　　　　　　
　　　　　　　---java　　　　Java 源码目录
　　      　---resources　  Java 配置文件目录
　　　　---test
　　　　　　---java　　　　测试源码目录
　　　　　　---resources　  测试配置目录
```
其中我们主要关心 pom.xml 文件和 main 下的 Java 文件夹。pom.xml 文件主要用于依赖和打包配置，Java 文件夹下放置您的源代码。

首先在 pom.xml 文件中添加 Maven 依赖：
```
<dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>2.0.2</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-streaming_2.11</artifactId>
            <version>2.0.2</version>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-streaming-kafka-0-10_2.11</artifactId>
            <version>2.0.2</version>
        </dependency>
</dependencies>
```
继续在 pom.xml 文件中添加打包和编译插件：
```
<build>
<plugins>
  <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
      <source>1.8</source>
      <target>1.8</target>
      <encoding>utf-8</encoding>
    </configuration>
  </plugin>
  <plugin>
    <artifactId>maven-assembly-plugin</artifactId>
    <configuration>
      <descriptorRefs>
      <descriptorRef>jar-with-dependencies</descriptorRef>
      </descriptorRefs>
    </configuration>
    <executions>
      <execution>
        <id>make-assembly</id>
        <phase>package</phase>
        <goals>
          <goal>single</goal>
        </goals>
      </execution>
    </executions>
  </plugin>
</plugins>
</build>
```
>!修改其中的 $yourgroupID 和 $yourartifactID 为您自己的设置。

接下来添加样例代码，在 main>Java 文件夹下新建一个 Java Class 取名为 KafkaTest.java，并将以下代码加入其中：
```
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.streaming.Durations;
import org.apache.spark.streaming.api.java.JavaInputDStream;
import org.apache.spark.streaming.api.java.JavaPairDStream;
import org.apache.spark.streaming.api.java.JavaStreamingContext;
import org.apache.spark.streaming.kafka010.ConsumerStrategies;
import org.apache.spark.streaming.kafka010.KafkaUtils;
import org.apache.spark.streaming.kafka010.LocationStrategies;
import scala.Tuple2;

import java.util.*;
import java.util.concurrent.TimeUnit;

/**
 * Created by tencent on 2018/7/3.
 */
public class KafkaTest {
    public static void main(String[] args) throws InterruptedException {
        String brokers = "$kafkaIP:9092";
        String topics = "spark_streaming_test1";  // 订阅的话题，多个话题','分隔
        int durationSeconds = 60;  // 间隔时间
        SparkConf conf = new SparkConf().setAppName("spark streaming word count");
        JavaSparkContext sc = new JavaSparkContext(conf);
        JavaStreamingContext ssc = new JavaStreamingContext(sc, Durations.seconds(durationSeconds));
        Collection<String> topicsSet = new HashSet<>(Arrays.asList(topics.split(",")));
        //kafka相关参数
        Map<String, Object> kafkaParams = new HashMap<>();
        kafkaParams.put("metadata.broker.list", brokers) ;
        kafkaParams.put("bootstrap.servers", brokers);
        kafkaParams.put("group.id", "group1");
        kafkaParams.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        kafkaParams.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        kafkaParams.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        //创建连接
        JavaInputDStream<ConsumerRecord<Object,Object>> lines = KafkaUtils.createDirectStream(
                ssc,
                LocationStrategies.PreferConsistent(),
                ConsumerStrategies.Subscribe(topicsSet, kafkaParams)
        );
        //wordcount逻辑
        JavaPairDStream<String, Integer> counts = lines
                .flatMap(x -> Arrays.asList(x.value().toString().split(" ")).iterator())
                .mapToPair(x -> new Tuple2<String, Integer>(x, 1))
                .reduceByKey((x, y) -> x + y);
        // 保存结果
        counts.dstream().saveAsTextFiles("$hdfsPath","result");
//
        ssc.start();
        ssc.awaitTermination();
        ssc.close();
    }
}
```
代码中要注意以下几点设置：
- brokers 变量要设置为在第二步中查找到的 CKafka 实例的内网 IP。
- topics 变量要设置为自己创建的 topic 的名字，这里为 spark_streaming_test1。
- durationSeconds 为程序去 CKafka 中消费数据的时间间隔，这里为60秒。
- $hdfsPath 为 HDFS 中的路径，结果将会输出到该路径下。

使用本地命令行进入工程目录，执行以下指令对工程进行编译打包：
```
mvn package
```
显示 build success 表示操作成功，在工程目录下的 target 文件夹中能够看到打包好的文件。

使用 scp 或者 sftp 工具来把打包好的文件上传到 EMR 集群，注意一定要上传依赖一起打包的 jar 包：
```
scp $localfile root@公网IP地址:$remotefolder
```
其中，$localfile 是您的本地文件的路径加名称，root 为 CVM 服务器用户名，公网 IP 可以在 EMR 控制台的节点信息中或者在云服务器控制台查看。$remotefolder 是您想存放文件的 CVM 服务器路径。上传完成后，在 EMR 集群命令行中即可查看对应文件夹下是否有相应文件。

### 创建 Spark Streaming 生产者工程
在本地命令行下进入您想要新建工程的目录，例如`D://mavenWorkplace`中，输入如下命令新建一个 Maven 工程：
```
mvn archetype:generate -DgroupId=$yourgroupID -DartifactId=$yourartifactID 
-DarchetypeArtifactId=maven-archetype-quickstart
```
首先在 pom.xml 文件中添加 Maven 依赖：
```
<dependencies>
        <dependency>
            <groupId>org.apache.kafka</groupId>
            <artifactId>kafka_2.11</artifactId>
            <version>0.10.1.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.kafka</groupId>
            <artifactId>kafka-clients</artifactId>
            <version>0.10.1.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.kafka</groupId>
            <artifactId>kafka-streams</artifactId>
            <version>0.10.1.0</version>
        </dependency>
    </dependencies>
```
继续在 pom.xml 文件中添加打包和编译插件：
```
<build>
<plugins>
  <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
      <source>1.8</source>
      <target>1.8</target>
      <encoding>utf-8</encoding>
    </configuration>
  </plugin>
  <plugin>
    <artifactId>maven-assembly-plugin</artifactId>
    <configuration>
      <descriptorRefs>
      <descriptorRef>jar-with-dependencies</descriptorRef>
      </descriptorRefs>
    </configuration>
    <executions>
      <execution>
        <id>make-assembly</id>
        <phase>package</phase>
        <goals>
          <goal>single</goal>
        </goals>
      </execution>
    </executions>
  </plugin>
</plugins>
</build>
```
>!修改其中的 $yourgroupID 和 $yourartifactID 为您自己的设置。

接下来添加样例代码，在 main>Java 文件夹下新建一个 Java Class 取名为 SendData.java，并将以下代码加入其中：
```
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import java.util.Properties;


/**
 * Created by tencent on 2018/7/4.
 */
public class SendData {
    public static void main(String[] args) {

        Properties props = new Properties();
        props.put("bootstrap.servers", "$kafkaIP:9092");
        props.put("acks", "all");
        props.put("retries", 0);
        props.put("batch.size", 16384);
        props.put("linger.ms", 1);
        props.put("buffer.memory", 33554432);
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        //生产者发送消息
        String topic = "spark_streaming_test1";
        org.apache.kafka.clients.producer.Producer<String, String> procuder = new KafkaProducer<String,String>(props);
        while(true){
            int num = (int)((Math.random())*10);
            for (int i = 0; i <= 10; i++) {
                int tmp = (num+i)%10;
                String value = "value_" + tmp;
                ProducerRecord<String, String> msg = new ProducerRecord<String, String>(topic, value);
                procuder.send(msg);
            }

            try {Thread.sleep(1000*10);}
            catch (InterruptedException e) {}
        }
    }
}
```
**修改其中的 $kafkaIP 为您的 CKafka 的内网 IP 地址**。

这个程序每10秒向 CKafka 发送10条消息从 value_0 到 value_9，其开始的顺序随机。程序中的参数信息参考消费者程序。

使用本地命令行进入工程目录，执行以下指令对工程进行编译打包：
```
mvn package
```
显示 build success 表示操作成功，在工程目录下的 target 文件夹中能够看到打包好的文件。

使用 scp 或者 sftp 工具来把打包好的文件上传到 EMR 集群，注意一定要上传依赖一起打包的 jar 包：
```
scp $localfile root@公网IP地址:$remotefolder
```

### 使用程序消费 CKafka 的数据
使用两个界面分别登录 EMR 集群的 Web Shell。

**第一个界面：**登录 EMR 集群的 Master 节点，并且切换到 Hadoop 用户如2节中所示，使用以下命令执行样例：
```
[hadoop@172 ~]$ bin/spark-submit --class KafkaTest --master yarn-cluster $consumerpackage 
```
其中参数如下：
- --class 参数表示要执行的入口类，在本例中即为 KafkaTest。
- --master 为集群主要的 URL。
- $ consumerpackage 是您的消费者打包后的包名。

程序开始执行后，将会在 yarn 集群上一直运行，使用以下指令可以查看到程序运行的状态：
```
[hadoop@172 ~]$ yarn application –list
```
**第二个界面：**登录 EMR 的 Web Shell，然后运行生产者程序，以便 Spark Streaming 能够从中取数据消费。
```
[hadoop@172 spark]$ bin/spark-submit --class SendData $producerpackage
```
其中 $producerpackage 为您的生产者打包后的包名。等待一段时间后，会在指定的 HDFS 文件夹中输出 wordcount 的结果，可以到 HDFS 中查看 Spark Streaming 消费 CKafka 数据后输出的结果：
```
[hadoop@172 root]$ hdfs dfs -ls /user
Found 9 items
drwxr-xr-x - hadoop supergroup  0 2018-07-03 16:37 /user/hadoop
drwxr-xr-x - hadoop supergroup  0 2018-06-19 10:10 /user/hive
-rw-r--r-- 3 hadoop supergroup 0 2018-06-29 10:19 /user/pythontest.txt
drwxr-xr-x - hadoop supergroup 0 2018-07-05 20:25 /user/sparkstreamingtest-1530793500000.result

[hadoop@172 root]$ hdfs dfs -cat /user/sparkstreamingtest-1530793500000.result/*
(value_6,16)
(value_7,22)
(value_8,18)
(value_0,18)
(value_9,17)
(value_1,18)
(value_2,17)
(value_3,17)
(value_4,16)
(value_5,17)
```
最后需要退出 yarn 集群中的 KafkaTest 程序：
```
[hadoop@172 ~]$ yarn application –kill $Application-Id
```
其中 $Application-Id 为使用`yarn application –list`命令查找到的 ID。

更多 Kafka 的相关信息请查看 [官方文档](http://kafka.apache.org/)。
