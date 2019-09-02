## Storm 简介
&emsp;&emsp;Storm 是一个分布式实时计算框架，能够对数据进行流式处理和提供通用性分布式 RPC 调用，可以实现处理事件亚秒级的延迟，适用于对延迟要求比较高的实时数据处理场景。
## Storm 工作原理
&emsp;&emsp;在 Storm 的集群中有两种节点，控制节点`Master Node`和工作节点`Worker Node`。`Master Node`上运行`Nimbus`进程，用于资源分配与状态监控。`Worker Node`上运行`Supervisor`进程，监听工作任务，启动`executor`执行。整个 Storm 集群依赖`zookeeper`负责公共数据存放、集群状态监听、任务分配等功能。

&emsp;&emsp;用户提交给 Storm 的数据处理程序称为`topology`，它处理的最小消息单位是`tuple`，一个任意对象的数组。`topology`由`spout`和`bolt`构成，`spout`是产生`tuple`的源头，`bolt`可以订阅任意`spout`或`bolt`发出的`tuple`进行处理。
![](https://mc.qcloudimg.com/static/img/93eb9e2621f5ad49fee536ab9d6e8799/image.png)

## Storm with ckafka
&emsp;&emsp;Storm 可以把 CKafka 作为`spout`，消费数据进行处理；也可以作为`bolt`，存放经过处理后的数据提供给其它组件消费。

### 测试环境
**Centos6.8系统**

| package | version |
|----|---- |
|maven |3.5.0|
|storm|1.1.0|
|ssh|5.3|
|Java|1.8|


### 申请创建 CKafka 实例

![](https://mc.qcloudimg.com/static/img/d2ae59d6670c641c73ddcc3d0b7fa364/image.png)

### 创建 Topic

![](https://mc.qcloudimg.com/static/img/0b6d4b8f9b18951cbc5ba3b16cd5ea8a/image.png)

### maven 依赖
pom.xml配置如下
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>storm</groupId>
  <artifactId>storm</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <name>storm</name> 
     <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.apache.storm</groupId>
            <artifactId>storm-core</artifactId>
            <version>1.1.0</version>
			<scope>provided</scope>
        </dependency>

        <dependency>
		    <groupId>org.apache.storm</groupId>
		    <artifactId>storm-kafka</artifactId>
		    <version>1.1.0</version>
		    <exclusions>
		    	<exclusion>
					<groupId>org.apache.kafka</groupId>
					<artifactId>kafka-clients</artifactId>
				</exclusion>
            </exclusions>
		</dependency>
		<dependency>
		    <groupId>org.apache.storm</groupId>
		    <artifactId>storm-kafka-client</artifactId>
		    <version>1.1.1</version>
		</dependency>
        <dependency>
		    <groupId>org.apache.kafka</groupId>
		    <artifactId>kafka_2.11</artifactId>
		    <version>0.10.2.1</version>
		    <exclusions>
		    	<exclusion>
		    		<groupId>org.slf4j</groupId>
		    		<artifactId>slf4j-log4j12</artifactId>
		    	</exclusion>
		    </exclusions>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>3.8.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <artifactId>maven-assembly-plugin</artifactId>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                    <archive>
                        <manifest>
                            <mainClass>ExclamationTopology</mainClass>
                        </manifest>
                    </archive>
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
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```


### 写入 CKafka 
#### 使用 spout/bolt
topology 代码
```java
//KafkaProduceTopology.java
import org.apache.storm.Config;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.storm.generated.StormTopology;
import org.apache.storm.kafka.bolt.KafkaBolt;
import org.apache.storm.kafka.bolt.mapper.FieldNameBasedTupleToKafkaMapper;
import org.apache.storm.kafka.bolt.selector.KafkaTopicSelector;
import org.apache.storm.kafka.bolt.selector.DefaultTopicSelector;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.utils.Utils;

import java.io.Serializable;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

import java.util.Properties;

public class KafkaProduceTopology {
    public static void main(String[] args) throws Exception {
		//申请到的ckafka实例ip:port
		String bootstrapServers = "111.230.216.45:9092";
		//指定要将消息写入的topic
		String topic = "storm-topology-test";
	   	//设置producer属性
	   	//函数参考：https://kafka.apache.org/0100/javadoc/index.html?org/apache/kafka/clients/consumer/KafkaConsumer.html
	   	//属性参考：http://kafka.apache.org/0102/documentation.html
	   	
	   	Properties props = new Properties();
	   	props.put("bootstrap.servers", bootstrapServers);
	   	props.put("acks", "1");
	   	props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
	   	props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
		//创建写入kafka的bolt，默认使用fields("key" "message")作为生产消息的key和message，也可以在FieldNameBasedTupleToKafkaMapper()中指定
	   	KafkaBolt kafkaBolt = new KafkaBolt()
	    	.withProducerProperties(props)
	        .withTopicSelector(new DefaultTopicSelector(topic))
	        .withTupleToKafkaMapper(new FieldNameBasedTupleToKafkaMapper());
	        
	   	TopologyBuilder builder = new TopologyBuilder();
	   	//一个顺序生成消息的spout类，输出field是sentence
		SerialSentenceSpout spout = new SerialSentenceSpout();
		AddMessageKeyBolt bolt = new AddMessageKeyBolt();
	  	builder.setSpout("spout", spout, 1);
	  	//为tuple加上生产到ckafka所需要的fields
		builder.setBolt("add-key", bolt, 1).shuffleGrouping("spout");
		//写入ckafka
	   	builder.setBolt("forwardToKafka", kafkaBolt, 8).shuffleGrouping("add-key");
	   	
		Config conf = new Config();
        //conf.setDebug(true);
        if (args != null && args.length > 0) {
        	conf.setNumWorkers(1);

        	StormSubmitter.submitTopologyWithProgressBar(args[0], conf, builder.createTopology());
        }
        else {
        	LocalCluster cluster = new LocalCluster();
          	cluster.submitTopology("test", conf, builder.createTopology());
          	Utils.sleep(10000);
          	cluster.killTopology("test");
          	cluster.shutdown();
        }
	}
}
```

为`tuple`加上 key、message 两个字段，当 key 为 null 时，生产的消息均匀分配到各个 partition，指定了 key 后将按照 key 值 hash 到特定 partition 上

```java
//AddMessageKeyBolt.java
public class AddMessageKeyBolt extends BaseBasicBolt {
    public void prepare(Map conf, TopologyContext context, OutputCollector collector) {
    }
	//Add key for message
	public void execute(Tuple tuple, BasicOutputCollector collector) {
		String message = tuple.getString(0);
		collector.emit(new Values(null, message));
	}
	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		declarer.declare(new Fields("key", "message"));
	}
}
```

#### 使用 trident
使用 trident 类生成 topology
```java
//TridentKafkaProduceTopology.java
import org.apache.storm.Config;
import org.apache.storm.kafka.trident.TridentKafkaState;
import org.apache.storm.kafka.trident.TridentKafkaStateFactory;
import org.apache.storm.kafka.trident.TridentKafkaUpdater;
import org.apache.storm.kafka.trident.mapper.FieldNameBasedTupleToKafkaMapper;
import org.apache.storm.kafka.trident.selector.DefaultTopicSelector;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.trident.operation.BaseFunction;
import org.apache.storm.trident.operation.TridentCollector;
import org.apache.storm.trident.Stream;
import org.apache.storm.trident.TridentTopology;
import org.apache.storm.trident.tuple.TridentTuple;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.utils.Utils;

import java.io.Serializable;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;
import java.util.List;
import java.util.Properties;

public class TridentKafkaProduceTopology {
	//为tuple加上生产到ckafka所需要的fields
	public static class AddMessageKey extends BaseFunction {
		public void execute(TridentTuple tuple, TridentCollector collector)
		{
			String value = tuple.getString(0);
			int key = value.hashCode();
			//collector.emit(new Values(Integer.toString(key), tuple.getString(0)));
			collector.emit(new Values(null, tuple.getString(0)));
		}
	}
    public static void main(String[] args) throws Exception {
	    //申请到的ckafka实例ip:port
		String bootstrapServers = "111.230.216.45:9092";
		//指定要将消息写入的topic
		String topic = "storm-trident-test";
	   	
	   	//设置producer属性
	   	//函数参考：https://kafka.apache.org/0100/javadoc/index.html?org/apache/kafka/clients/consumer/KafkaConsumer.html
	   	//属性参考：http://kafka.apache.org/0102/documentation.html
	   	Properties props = new Properties();
	   	props.put("bootstrap.servers", bootstrapServers);
	   	props.put("acks", "1");
	   	props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
	   	props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

		//一个批量产生句子的spout,输出field为sentence
		TridentSerialSentenceSpout spout = new TridentSerialSentenceSpout(5);
		//设置trident
		TridentKafkaStateFactory stateFactory = new TridentKafkaStateFactory()
			.withProducerProperties(props)
			.withKafkaTopicSelector(new DefaultTopicSelector(topic))
			//设置使用fields("key", "value")作为消息写入
			.withTridentTupleToKafkaMapper(new FieldNameBasedTupleToKafkaMapper("key", "value"));

		TridentTopology builder = new TridentTopology();
        Stream stream = builder.newStream("spout", spout)
			.each(new Fields("sentence"), new AddMessageKey(), new Fields("key", "value"))
		;
		stream.partitionPersist(stateFactory, new Fields("key", "value"), new TridentKafkaUpdater(), new Fields());

	   	Config conf = new Config();
        //conf.setDebug(true);
        if (args != null && args.length > 0) {
        	conf.setNumWorkers(1);
        	StormSubmitter.submitTopologyWithProgressBar(args[0], conf, builder.build());
        }
        else {
        	LocalCluster cluster = new LocalCluster();
          	cluster.submitTopology("test", conf, builder.build());
          	Utils.sleep(5000);
          	cluster.killTopology("test");
          	cluster.shutdown();
        }
	}
}
```


### 从 CKafka 消费
#### 使用 spout/bolt
```java
//KafkaConsumeTopology.java
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.storm.Config;
import org.apache.storm.kafka.spout.KafkaSpout;
import org.apache.storm.kafka.spout.Func;
import org.apache.storm.kafka.spout.KafkaSpoutConfig;
import org.apache.storm.kafka.spout.KafkaSpoutConfig.FirstPollOffsetStrategy;
import org.apache.storm.kafka.spout.KafkaSpoutRetryExponentialBackoff;
import org.apache.storm.kafka.spout.KafkaSpoutRetryExponentialBackoff.TimeInterval;
import org.apache.storm.kafka.spout.KafkaSpoutRetryService;
import org.apache.storm.kafka.spout.trident.KafkaTridentSpoutOpaque;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.topology.TopologyBuilder;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.utils.Utils;

import java.io.Serializable;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

import static org.apache.storm.kafka.spout.KafkaSpoutConfig.FirstPollOffsetStrategy.LATEST;
import static org.apache.storm.kafka.spout.KafkaSpoutConfig.FirstPollOffsetStrategy.EARLIEST;

public class KafkaConsumeTopology {
    public static void main(String[]  args) throws Exception {
	    //申请到的ckafka实例ip:port
		String bootstrapServers = "111.230.216.45:9092";
		//指定要将消息写入的topic
		String topic = "storm-topology-test";
        Config conf = new Config();
        //conf.setDebug(true);
        conf.setMaxSpoutPending(20);
        conf.setNumWorkers(1);
        //设置重试策略
        KafkaSpoutRetryService kafkaSpoutRetryService =  new KafkaSpoutRetryExponentialBackoff(
            KafkaSpoutRetryExponentialBackoff.TimeInterval.microSeconds(500),
            KafkaSpoutRetryExponentialBackoff.TimeInterval.milliSeconds(2),
            Integer.MAX_VALUE,
            KafkaSpoutRetryExponentialBackoff.TimeInterval.seconds(10));
		//设置consumer参数
		//函数参考http://storm.apache.org/releases/1.1.0/javadocs/org/apache/storm/kafka/spout/KafkaSpoutConfig.Builder.html
		//参数参考http://kafka.apache.org/0102/documentation.html
        KafkaSpoutConfig spoutConf =  KafkaSpoutConfig.builder(bootstrapServers, topic)
            .setGroupId("test-group1")	//设置消费groupId
			.setProp(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true")	//设置自动确认
			.setProp(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, "50000") //设置session超时时间
			.setProp(ConsumerConfig.REQUEST_TIMEOUT_MS_CONFIG, "60000") //设置请求超时时间
            .setOffsetCommitPeriodMs(10_000)	//设置自动确认的时间 ms
            .setFirstPollOffsetStrategy(LATEST)	//设置拉取最新的消息
            .setRetry(kafkaSpoutRetryService)
            .build();
		
        final TopologyBuilder builder = new TopologyBuilder();
        builder.setSpout("kafka-spout", new KafkaSpout(spoutConf), 1);

        if (args != null && args.length > 0) {
            conf.setNumWorkers(3);
            StormSubmitter.submitTopologyWithProgressBar(args[0], conf, builder.createTopology());
        }
        else {
            LocalCluster cluster = new LocalCluster();
            cluster.submitTopology("test", conf, builder.createTopology());
            Utils.sleep(200000);
            cluster.killTopology("test");
            cluster.shutdown();
        }
    }
}
```
#### 使用 trident
```
//TridentKafkaTopology.java
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.storm.Config;
import org.apache.storm.kafka.spout.KafkaSpout;
import org.apache.storm.kafka.spout.Func;
import org.apache.storm.kafka.spout.KafkaSpoutConfig;
import org.apache.storm.kafka.spout.KafkaSpoutConfig.FirstPollOffsetStrategy;
import org.apache.storm.kafka.spout.KafkaSpoutRetryExponentialBackoff;
import org.apache.storm.kafka.spout.KafkaSpoutRetryExponentialBackoff.TimeInterval;
import org.apache.storm.kafka.spout.KafkaSpoutRetryService;
import org.apache.storm.kafka.spout.trident.KafkaTridentSpoutOpaque;
import org.apache.storm.LocalCluster;
import org.apache.storm.StormSubmitter;
import org.apache.storm.trident.Stream;
import org.apache.storm.trident.TridentTopology;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.utils.Utils;

import java.io.Serializable;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

import static org.apache.storm.kafka.spout.KafkaSpoutConfig.FirstPollOffsetStrategy.EARLIEST;
import static org.apache.storm.kafka.spout.KafkaSpoutConfig.FirstPollOffsetStrategy.LATEST;
import com.william.storm.trident.TridentPrinter;

public class TridentKafkaConsumeTopology {
    public static void main(String[]  args) throws Exception {
	    //申请到的ckafka实例ip:port
		String bootstrapServers = "111.230.216.45:9092";
		//指定要将消息写入的topic
		String topic = "storm-trident-test";
        Config conf = new Config();
        
        conf.setMaxSpoutPending(20);
        conf.setNumWorkers(1);
        //设置重试策略
        KafkaSpoutRetryService kafkaSpoutRetryService =  new KafkaSpoutRetryExponentialBackoff(
            KafkaSpoutRetryExponentialBackoff.TimeInterval.microSeconds(500),
            KafkaSpoutRetryExponentialBackoff.TimeInterval.milliSeconds(2),
            Integer.MAX_VALUE,
            KafkaSpoutRetryExponentialBackoff.TimeInterval.seconds(10));
		//设置consumer参数
		//函数参考http://storm.apache.org/releases/1.1.0/javadocs/org/apache/storm/kafka/spout/KafkaSpoutConfig.Builder.html
		//参数参考http://kafka.apache.org/0102/documentation.html
        KafkaSpoutConfig spoutConf =  KafkaSpoutConfig.builder(bootstrapServers, topic)
            .setGroupId("test-group1")	//设置消费groupId
			.setProp(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true")	//设置自动确认
			.setProp(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, "50000") //设置session超时时间
			.setProp(ConsumerConfig.REQUEST_TIMEOUT_MS_CONFIG, "60000") //设置请求超时时间
            .setOffsetCommitPeriodMs(10_000)	//设置自动确认的时间 ms
            .setFirstPollOffsetStrategy(LATEST)	//设置拉取最新的消息
            .setRetry(kafkaSpoutRetryService)
            .build();

		TridentTopology builder = new TridentTopology();
		final Stream stream = builder.newStream("kafka-spout", 
			new KafkaTridentSpoutOpaque(spoutConf))

        if (args != null && args.length > 0) {
            conf.setNumWorkers(3);
            StormSubmitter.submitTopologyWithProgressBar(args[0], conf, builder.build());
        }
        else {
            LocalCluster cluster = new LocalCluster();
            cluster.submitTopology("test", conf, builder.build());
            Utils.sleep(100000);
            cluster.killTopology("test");
            cluster.shutdown();
        }
    }
}
```

### 提交 Storm
使用 mvn package 编译后,可以提交到本地集群进行 debug 测试，也可以提交到正式集群进行运行
```bash
storm jar your_jar_name.jar topology_name
```

```bash
storm jar your_jar_name.jar topology_name tast_name
```
