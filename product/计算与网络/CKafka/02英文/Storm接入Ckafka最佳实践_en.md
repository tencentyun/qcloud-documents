## Introduction to Storm
&emsp;&emsp;Storm is a real-time distributed computing framework, which can perform stream-based data processing and provide common distributed RPC calling, so as to minimize the delay of event processing to sub-seconds. It is suitable for the real-time data processing scenarios with high delay requirements.
## How Does Storm Work
&emsp;&emsp;Two types of nodes are supported in Storm clusters: the control node `Master Node` and the work node `Worker Node`. The `Nimbus` process runs on the `Master Node` for resource assignment and status monitoring. The `Supervisor` process runs on the `Worker Node` for listening on work tasks and starting `executor`. The entire Storm cluster relies on `zookeeper` for public data storage, cluster status listening, task assignment, etc.

&emsp;&emsp;The data processing program submitted to Storm by users is called `topology`. The minimum message unit it processes is `tuple` - an array of arbitrary objects. `topology` consists of `spout` and `bolt`, in which `spout` is the source of `tuple`, and `bolt` can subscribe any `tuple` issued by `spout` or `bolt` for processing.
![](https://mc.qcloudimg.com/static/img/93eb9e2621f5ad49fee536ab9d6e8799/image.png)

## Storm with ckafka
&emsp;&emsp;Storm can use CKafka as `spout` to process consumed data, or as `bolt` to store the processed data and provide the data for other components to consume.

### Testing Environment
**Centos 6.8 System**

| Package | Version |
|----|---- |
| maven | 3.5.0 |
| storm | 1.1.0 |
| ssh | 5.3 |
| Java | 1.8 |


### Applying for the Creation of Ckafka Instance

![](https://mc.qcloudimg.com/static/img/d2ae59d6670c641c73ddcc3d0b7fa364/image.png)

### Creating Topic

![](https://mc.qcloudimg.com/static/img/0b6d4b8f9b18951cbc5ba3b16cd5ea8a/image.png)

### "maven" Dependency
"pom.xml" is configured as follows
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


### Writing in CKafka 
#### Using "spout/bolt"
"topology" Code
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
		//"ip:port" of the CKafka instance you just applied for
		String bootstrapServers = "111.230.216.45:9092";
		//Specify the topic into which the message is written
		String topic = "storm-topology-test";
	   	//Set producer attribute
	   	//Function reference:https://kafka.apache.org/0100/javadoc/index.html?org/apache/kafka/clients/consumer/KafkaConsumer.html
	   	//Attribute reference: http://kafka.apache.org/0102/documentation.html
	   	
	   	Properties props = new Properties();
	   	props.put("bootstrap.servers", bootstrapServers);
	   	props.put("acks", "1");
	   	props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
	   	props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
		//Create a bolt to be written into Kafka. "fields" ("key", "message") is used as the key and message for producing messages by default, which can also be specified in FieldNameBasedTupleToKafkaMapper().
	   	KafkaBolt kafkaBolt = new KafkaBolt()
	    	.withProducerProperties(props)
	        .withTopicSelector(new DefaultTopicSelector(topic))
	        .withTupleToKafkaMapper(new FieldNameBasedTupleToKafkaMapper());
	        
	   	TopologyBuilder builder = new TopologyBuilder();
	   	//A spout class that generates messages in order, and its output field is sentence
		SerialSentenceSpout spout = new SerialSentenceSpout();
		AddMessageKeyBolt bolt = new AddMessageKeyBolt();
	  	builder.setSpout("spout", spout, 1);
	  	//Add the fields required to produce messages to CKafka for tuple
		builder.setBolt("add-key", bolt, 1).shuffleGrouping("spout");
		//Write the following into CKafka
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

Add "key" and "message" fields to `tuple`. If key is null, the produced messages are evenly assigned to each partition. When key is specified, messages are hashed to a specific partition based on the key value.

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

#### Using "trident"
Use the trident class to generate topology
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
	//Add the fields required to produce messages to CKafka for tuple
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
	    //"ip:port" of the CKafka instance you just applied for
		String bootstrapServers = "111.230.216.45:9092";
		//Specify the topic into which the message is written
		String topic = "storm-trident-test";
	   	
	   	//Set producer attribute
	   	//Function reference:https://kafka.apache.org/0100/javadoc/index.html?org/apache/kafka/clients/consumer/KafkaConsumer.html
	   	//Attribute reference: http://kafka.apache.org/0102/documentation.html
	   	Properties props = new Properties();
	   	props.put("bootstrap.servers", bootstrapServers);
	   	props.put("acks", "1");
	   	props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
	   	props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

		//A spout that generates messages in batches, and its output field is sentence
		TridentSerialSentenceSpout spout = new TridentSerialSentenceSpout(5);
		//Set trident
		TridentKafkaStateFactory stateFactory = new TridentKafkaStateFactory()
			.withProducerProperties(props)
			.withKafkaTopicSelector(new DefaultTopicSelector(topic))
			//Set fields ("key", "value") to be used for writing messages
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


### Consuming from CKafka
#### Using "spout/bolt"
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
	    //"ip:port" of the CKafka instance you just applied for
		String bootstrapServers = "111.230.216.45:9092";
		//Specify the topic into which the message is written
		String topic = "storm-topology-test";
        Config conf = new Config();
        //conf.setDebug(true);
        conf.setMaxSpoutPending(20);
        conf.setNumWorkers(1);
        //Set retry policy
        KafkaSpoutRetryService kafkaSpoutRetryService =  new KafkaSpoutRetryExponentialBackoff(
            KafkaSpoutRetryExponentialBackoff.TimeInterval.microSeconds(500),
            KafkaSpoutRetryExponentialBackoff.TimeInterval.milliSeconds(2),
            Integer.MAX_VALUE,
            KafkaSpoutRetryExponentialBackoff.TimeInterval.seconds(10));
		//Set consumer parameter
		//Function reference:http://storm.apache.org/releases/1.1.0/javadocs/org/apache/storm/kafka/spout/KafkaSpoutConfig.Builder.html
		//Attribute reference: http://kafka.apache.org/0102/documentation.html
        KafkaSpoutConfig spoutConf =  KafkaSpoutConfig.builder(bootstrapServers, topic)
            .setGroupId("test-group1")	//Set consumption groupId
			.setProp(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true")	//Set automatic confirmation
			.setProp(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, "50000") //Set session timeout
			.setProp(ConsumerConfig.REQUEST_TIMEOUT_MS_CONFIG, "60000") //Set request timeout
            .setOffsetCommitPeriodMs(10_000)	//Set automatic confirmation time (in ms)
            .setFirstPollOffsetStrategy(LATEST)	//Set to pull the latest messages
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
#### Using "trident"
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
	    //"ip:port" of the CKafka instance you just applied for
		String bootstrapServers = "111.230.216.45:9092";
		//Specify the topic into which the message is written
		String topic = "storm-trident-test";
        Config conf = new Config();
        
        conf.setMaxSpoutPending(20);
        conf.setNumWorkers(1);
        //Set retry policy
        KafkaSpoutRetryService kafkaSpoutRetryService =  new KafkaSpoutRetryExponentialBackoff(
            KafkaSpoutRetryExponentialBackoff.TimeInterval.microSeconds(500),
            KafkaSpoutRetryExponentialBackoff.TimeInterval.milliSeconds(2),
            Integer.MAX_VALUE,
            KafkaSpoutRetryExponentialBackoff.TimeInterval.seconds(10));
		//Set consumer parameter
		//Function reference:http://storm.apache.org/releases/1.1.0/javadocs/org/apache/storm/kafka/spout/KafkaSpoutConfig.Builder.html
		//Attribute reference: http://kafka.apache.org/0102/documentation.html
        KafkaSpoutConfig spoutConf =  KafkaSpoutConfig.builder(bootstrapServers, topic)
            .setGroupId("test-group1")	//Set consumption groupId
			.setProp(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "true")	//Set automatic confirmation
			.setProp(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, "50000") //Set session timeout
			.setProp(ConsumerConfig.REQUEST_TIMEOUT_MS_CONFIG, "60000") //Set request timeout
            .setOffsetCommitPeriodMs(10_000)	//Set automatic confirmation time (in ms)
            .setFirstPollOffsetStrategy(LATEST)	//Set to pull the latest messages
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

### Submitting "Storm"
After being compiled with mvn package, Storm can be submitted to the local cluster for debug testing, or submitted to the formal cluster for running.
```bash
storm jar your_jar_name.jar topology_name
```

```bash
storm jar your_jar_name.jar topology_name tast_name
```

