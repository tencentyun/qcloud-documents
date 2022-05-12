TSF 从1.23.0版本开始支持 RocketMQ 使用联路追踪能力。

## 链路追踪原理
利用 springboot 提供自动配置原理，加入一个能插手 bean DefaultMQProducer、和 bean DefaultMQPushConsumer 创建过程的自动配置类。使用代理来增强 DefaultMQProducer/DefaultMQPushConsumer，在调用相应方法是加入 tracing 的逻辑，在方法结束时将 tracing 数据搜集起来，统一存储。最后分析展示给前端页面。

## 引入依赖及配置
```
    <!-- TSF 启动器 -->
    <dependency>
        <groupId>com.tencent.tsf</groupId>
        <artifactId>spring-cloud-tsf-starter</artifactId>
    </dependency>
    <!--RocketMQ-->
    <dependency>
        <groupId>org.apache.rocketmq</groupId>
        <artifactId>rocketmq-client</artifactId>
        <version>4.4.0</version>
    </dependency>
apache:
  rocketmq:
    consumer:
      pushConsumer: myConsumer
    producer:
      producerGroup: myProducer
    name-server: xxx.xxx.xx.xx #rocketMq ip
    topic: long-topic
```

## 生产者示例
向 Spring 容器中加入 bean DefaultMQProducer：
```
@Configuration
public class ProducerConfiguration {
    private static final Logger logger = LoggerFactory.getLogger(ProducerConfiguration.class);
    @Value("${apache.rocketmq.name-server}")
    private String namesrvAddr;
    @Value("${apache.rocketmq.producer.producerGroup}")
    private String producerGroup;
    @Bean
    public DefaultMQProducer defaultMQProducer() throws MQClientException {
        DefaultMQProducer producer = new DefaultMQProducer(producerGroup);
        producer.setNamesrvAddr(namesrvAddr);
        producer.setVipChannelEnabled(false);
        producer.setRetryTimesWhenSendAsyncFailed(0);
        producer.start();
        logger.info("rocketmq producer is starting");
        return producer;
    }
}
```

引用 DefaultMQProducer，发送消息：
```
@Service
public class RocketmqService {
    private static  final Logger logger = LoggerFactory.getLogger(RocketmqService.class);
    @Autowired
    private DefaultMQProducer defaultMQProducer;
    // 使用 application.properties 里定义的 topic 属性
    @Value("${apache.rocketmq.topic}")
    private String springTopic;
    private AtomicLong id =new AtomicLong(0);
    @Scheduled(fixedDelayString = "${consumer.auto.test.interval:5000}")
    public String prepareSend() throws InterruptedException, RemotingException, MQClientException, MQBrokerException {
       return send();
    }
    public String send() throws InterruptedException, RemotingException, MQClientException, MQBrokerException {
        String sentText = "rocketmq message: msg id="+id.addAndGet(1);
        Message message = new Message(springTopic,"push", sentText.getBytes());
        message.putUserProperty("traceID","1234567");
        SendResult sendResult = defaultMQProducer.send(message);
        logger.info("消息id:"+id.get()+","+"发送状态:"+sendResult.getSendStatus());
        return sendResult.getMsgId();
    }
}
```

## 消费者示例
```
@Configuration
public class ConsumerConfiguration {
    private static final Logger logger = LoggerFactory.getLogger(ConsumerConfiguration.class);
    @Value("${apache.rocketmq.name-server}")
    private String namesrvAddr;
    @Value("${apache.rocketmq.topic}")
    private String springTopic;
    @Value("${apache.rocketmq.consumer.pushConsumer}")
    private String consumerGroup;
    @Bean
    public DefaultMQPushConsumer pushConsumer() {
        DefaultMQPushConsumer consumer = new DefaultMQPushConsumer(consumerGroup);
        consumer.setNamesrvAddr(namesrvAddr);
        try {
            // 订阅PushTopic下Tag为push的消息,都订阅消息
            consumer.subscribe(springTopic, "push");
            // 程序第一次启动从消息队列头获取数据
            consumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_FIRST_OFFSET);
            //可以修改每次消费消息的数量，默认设置是每次消费一条
            consumer.setConsumeMessageBatchMaxSize(1);
            //在此监听中消费信息，并返回消费的状态信息
            consumer.registerMessageListener((MessageListenerConcurrently) (msgs, context) -> {
                // 会把不同的消息分别放置到不同的队列中
                for (Message msg : msgs) {
                    System.out.println("接收到了消息：" + new String(msg.getBody()));
                    logger.info("接收到了消息：" + new String(msg.getBody()));
                    try {
                        Thread.sleep(50);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
            });
            consumer.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return consumer;
    }
}
```
