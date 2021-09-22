本文主要介绍 TDMQ Pulsar 客户端与连接、客户端与生产/消费者之间的关系，并向开发者介绍客户端合理的使用方式，以便更高效、稳定地使用 TDMQ Pulsar 版的服务。

>**核心原则：**
>- 一个进程一个 PulsarClient 即可。
>- Producer、Consumer 是线程安全的，对于同一个 Topic，可以复用且最好复用。

## 客户端与连接

TDMQ Pulsar 客户端（以下简称 PulsarClient ）是应用程序连接到 TDMQ Pulsar 版的一个基本单位，一个 PulsarClient 对应一个 TCP 连接。一般来说，用户侧的一个应用程序或者进程对应使用一个 PulsarClient，有多少个应用节点，对应就有多少个 Client 数量。若长时间不使用 TDMQ Pulsar 版服务的应用节点，应回收 Client 以节省资源消耗（当前 TDMQ Pulsar 版的连接上限是单个 Topic 2000个 Client 连接）。



## 客户端与生产/消费者

一个 Client 下可以创建多个生产和消费者，用于提升生产和消费的速度。比较常见的用法是，一个 Client 下，利用多线程创建多个 Producer 或 Consumer 对象，用于生产消费，不同 Producer 和 Consumer 之间数据相互隔离。

当前 TDMQ Pulsar 版对生产/消费者的限制为：
- 单个 Topic 生产者上限1000个。
- 单个 Topic 消费者上限500个。



## 最佳实践

生产/消费者的数量不一定取决于业务对象，它们是一个可以复用的资源，通过名称作为唯一标识进行区分。

### 生产者

假设有1000个业务对象在同时生产消息，并不是要创建1000个 Producer，只要是向同一个 Topic 进行投递，每个应用节点可以先统一使用一个 Producer 来进行生产（单例模式），往往单个 Producer 就能吃满单个应用节点的硬件配置。

以下给出一段 Java 消息生产的代码示例。
<dx-codeblock>
:::  java
//从配置文件中获取 serviceURL 接入地址、Token 密钥、Topic 全名和 Subscription 名称（均可从控制台复制）
@Value("${tdmq.serviceUrl}")
private String serviceUrl;
@Value("${tdmq.token}")
private String token;
@Value("${tdmq.topic}")
private String topic;

//声明1个 Client 对象、producer 对象
private PulsarClient pulsarClient;
private Producer<String> producer;

//在一段初始化程序中创建好客户端和生产者对象
public void init() throws Exception {
    pulsarClient = PulsarClient.builder()
            .serviceUrl(serviceUrl)
            .authentication(AuthenticationFactory.token(token))
            .build();
    producer = pulsarClient.newProducer(Schema.STRING)
            .topic(topic)
            .create();
}
:::
</dx-codeblock>


在实际生产消息的业务逻辑中直接引用 `producer` 完成消息的发送。
<dx-codeblock>
:::  java
//在实际生产消息的业务逻辑中直接引用，注意 Producer 通过范式声明的 Schema 类型要和传入对象匹配
public void onProduce(Producer<String> producer){
    //添加业务逻辑
    String msg = "my-message";//模拟从业务逻辑拿到消息
    try {
        //TDMQ Pulsar 版默认开启 Schema 校验, 消息对象一定需要和 producer 声明的 Schema 类型匹配
        MessageId messageId = producer.newMessage()
              .key("msgKey")
          		.value(msg)
          		.send();
        System.out.println("delivered msg " + msgId + ", value:" + value);
    } catch (PulsarClientException e) {
      	System.out.println("delivered msg failed, value:" + value);
      	e.printStackTrace();
    }
}

public void onProduceAsync(Producer<String> producer){
    //添加业务逻辑
    String msg = "my-asnyc-message";//模拟从业务逻辑拿到消息
    //异步发送消息，无线程阻塞，提升发送速率
    CompletableFuture<MessageId> messageIdFuture = producer.newMessage()
          .key("msgKey")
      		.value(msg)
      		.sendAsync();
    //通过异步回调得知消息发送成功与否
    messageIdFuture.whenComplete(((messageId, throwable) -> {
        if( null != throwable ) {
            System.out.println("delivery failed, value: " + msg );
            //此处可以添加延时重试的逻辑
        } else {
            System.out.println("delivered msg " + messageId + ", value:" + msg);
        }
    }));
}
:::
</dx-codeblock>


当一个生产者长时间不使用时需要调用 close 方法关闭，以避免占用资源；当一个客户端实例长时间不使用时，同样需要调用 close 方法关闭，以避免连接池被占满。
<dx-codeblock>
:::  java
public void destroy(){
    if (producer != null) {
        producer.close();
    }
    if (pulsarClient != null) {
        pulsarClient.close();
    }
}
:::
</dx-codeblock>


### 消费者

如同生产者，消费者也最好按照单例模式进行使用，单个消费节点只需要一个客户端实例以及一个消费者实例。一般来说，一个消息队列的消费端的性能瓶颈都在于消费者按照自己业务逻辑处理消息的过程，而并非在接收消息的动作上。所以当出现了消费性能不足的时候，先看消费者的网络带宽消耗，如果趋势上看没有达到一个明显的上限，就应该先根据日志以及消息轨迹信息分析自身处理消息的业务逻辑耗时。


>!
- 当使用 Shared 或者 Key-Shared 模式时，消费者数量不一定小于等于分区数。服务端会有一个负责分发消息的模块按照一定的方式（Shared 模式默认是轮询，Key-Shared 则是在同一个 key 内轮询）将消息分发给所有的消费者。
- 当使用 Shared模式，如果生产侧暂停了生产，则到了末尾一部分消息时，可能会出现消费分布不均的情况。
- 使用多线程消费，即使复用一个 consumer 对象，消息的顺序也将无法得到保证。

以下给出一个 Java 基于 Spring boot 框架用线程池进行多线程消费的完整代码示例。
<dx-codeblock>
:::  java
import org.apache.pulsar.client.api.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

@Service
public class ConsumerService implements Runnable {

    //从配置文件中获取 serviceURL 接入地址、Token 密钥、Topic 全名和 Subscription 名称（均可从控制台复制）
    @Value("${tdmq.serviceUrl}")
    private String serviceUrl;
    @Value("${tdmq.token}")
    private String token;
    @Value("${tdmq.topic}")
    private String topic;
    @Value("${tdmq.subscription}")
    private String subscription;

    private volatile boolean start = false;
    private PulsarClient pulsarClient;
    private Consumer<String> consumer;
    private static final int corePoolSize = 10;
    private static final int maximumPoolSize = 10;

    private ExecutorService executor;
    private static final Logger logger = LoggerFactory.getLogger(ConsumerService.class);

    @PostConstruct
    public void init() throws Exception {
        pulsarClient = PulsarClient.builder()
                .serviceUrl(serviceUrl)
                .authentication(AuthenticationFactory.token(token))
                .build();
        consumer = pulsarClient.newConsumer(Schema.STRING)
                .topic(topic)
                //.subscriptionType(SubscriptionType.Shared)
                .subscriptionName(subscription)
                .subscribe();
        executor = new ThreadPoolExecutor(corePoolSize, maximumPoolSize, 0, TimeUnit.SECONDS, new ArrayBlockingQueue<>(100),
                new ThreadPoolExecutor.AbortPolicy());
        start = true;
    }

    @PreDestroy
    public void destroy() throws Exception {
        start = false;
        if (consumer != null) {
            consumer.close();
        }
        if (pulsarClient != null) {
            pulsarClient.close();
        }
        if (executor != null) {
            executor.shutdownNow();
        }
    }

    @Override
    public void run() {
        logger.info("tdmq consumer started...");
        for (int i = 0; i < maximumPoolSize; i++) {
            executor.submit(() -> {
                while (start) {
                    try {
                        Message<String> message = consumer.receive();
                        if (message == null) {
                            continue;
                        }
                        onConsumer(message);
                    } catch (Exception e) {
                        logger.warn("tdmq consumer business error", e);
                    }
                }
            });
        }
        logger.info("tdmq consumer stopped...");
    }

    /**
     * 这里写消费业务逻辑
     *
     * @param message
     * @return return true: 消息ack  return false: 消息nack
     * @throws Exception 消息nack
     */
    private void onConsumer(Message<String> message) {
        //业务逻辑,延时类操作
        try {
            System.out.println(Thread.currentThread().getName() + " - message receive: " + message.getValue());
            Thread.sleep(1000);//模拟业务逻辑处理
            consumer.acknowledge(message);
            logger.info(Thread.currentThread().getName() + " - message processing succeed：" + message.getValue());
        } catch (Exception exception) {
            consumer.negativeAcknowledge(message);
            logger.error(Thread.currentThread().getName() + " - message processing failed：" + message.getValue());
        }
    }
}
:::
</dx-codeblock>





