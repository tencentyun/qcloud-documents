基于腾讯云的 EMR 服务您可以轻松结合腾讯云的 Ckafka 服务实现以下流式应用：

1. 日志信息流式处理
2. 用户行为记录流式处理
3. 告警信息收集及处理
4. 消息系统

在使用本教程之前您需要开通 EMR 服务和 Ckafka 服务。

1. 配置工程依赖  

    在您的工程的 pom.xml 加入以下配置

    ``` XML
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
    ```

    把整个依赖打进一个 jar 包，请参考第一分部的样例。

2. 样例程序

    ``` c++
    public class WordCount {
      public static void main(String[] args) throws InterruptedException {
        String brokers = "your_ckafka_ip"; // ckafka地址
        String topics = "test"; // 订阅的话题，多个话题’,’分隔
        int durationSeconds = 60 * 5; // 间隔时间
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
            .flatMap(x -> 
            Arrays.asList(x.value().toString().split(" ")).iterator())
            .mapToPair(x -> new Tuple2<String, Integer>(x, 1))
            .reduceByKey((x, y) -> x + y);

      // 保存结果
      counts.dstream().saveAsTextFiles(
          "hdfs://your_hdfs_path",
          "result");
      ssc.start(); // 启动sparkstreaming
      ssc.awaitTermination(); // 循环执行
      ssc.close();
      }
    }
    ```

3. 编译运行 

    通过 mvn package 编译工程，并把编译后的 jar 传输到服务器，通过以下命令提交：

    <pre>
    spark-submit --class your_main
    </pre>
