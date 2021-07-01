本文主要介绍TDMQ Pulsar 客户端与连接、客户端与生产/消费者之间的关系，并向开发者介绍客户端合理的使用方式，以便更高效、稳定地使用TDMQ Pulsar版的服务。

> 核心原则：
>
> 1. 一个进程一个PulsarClient即可
> 2. Producer、Consumer是线程安全的，对于同一个Topic，可以复用且最好复用

## 客户端与连接

TDMQ Pulsar 客户端（以下简称 PulsarClient ）是应用程序连接到 TDMQ Pulsar版的一个基本单位，一个 PulsarClient 对应一个TCP连接。一般来说，用户侧的一个应用程序或者进程对应使用一个pulsar client，有多少个应用节点，对应就有多少个client数量。若长时间不使用TDMQ服务的应用节点，应回收client以节省资源消耗（当前TDMQ Pulsar版的连接上限是单个Topic 2000个client连接）。



## 客户端与生产/消费者

一个Client下可以创建多个生产和消费者，用于提升生产和消费的速度。比较常见的用法是，一个Client下，利用多线程创建多个Producer或Consumer对象，用于生产消费，不同Producer和Consumer之间数据相互隔离。

当前TDMQ对生产/消费者的限制是：

- 单个Topic生产者上限1000个
- 单个Topic消费者上限500个



## 最佳实践

生产/消费者的数量不一定取决于业务对象，它们是一个可以复用的资源，通过名称作为唯一标识进行区分。

### 生产者

假设有1000个业务对象在同时生产消息，并不是要创建1000个Producer，只要是向同一个Topic进行投递，每个应用节点可以先统一使用一个Producer来进行生产（单例模式），往往单个Producer就能吃满单个应用节点的硬件配置。

以下给出一段 Java 消息生产的代码示例。

```java
//从配置文件中获取serviceURL接入地址、Token密钥、Topic全名和Subscription名称（均可从控制台复制）
@Value("${tdmq.serviceUrl}")
private String serviceUrl;
@Value("${tdmq.token}")
private String token;
@Value("${tdmq.topic}")
private String topic;

//声明1个Client对象，producer对象
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
```

在实际生产消息的业务逻辑中直接引用`producer`完成消息的发送。

```java
//在实际生产消息的业务逻辑中直接引用，注意Producer通过范式声明的Schema类型要和传入对象匹配
public void onProduce(Producer<String> producer){
    //添加业务逻辑
    String msg = "my-message";//模拟从业务逻辑拿到消息
    try {
        //TDMQ默认开启Schema校验, 消息对象一定需要和producer声明的Schema类型匹配
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
```

当一个生产者长时间不使用时需要调用close方法关闭，以避免占用资源；当一个客户端实例长时间不使用时，同样需要调用close方法关闭，以避免连接池被占满。

```java
public void destroy(){
    if (producer != null) {
        producer.close();
    }
    if (pulsarClient != null) {
        pulsarClient.close();
    }
}
```



### 消费者

如同生产者，消费者也最好按照单例模式进行使用，单个消费节点只需要一个客户端实例以及一个消费者实例。一般来说，一个消息队列的消费端的性能瓶颈都在于消费者按照自己业务逻辑处理消息的过程，而并非在接收消息的动作上。所以当出现了消费性能不足的时候，先看消费者的网络带宽消耗，如果趋势上看没有达到一个明显的上限，就应该先根据日志以及消息轨迹信息分析自身处理消息的业务逻辑耗时。

消费侧需要关注的是：

1. 当使用Shared或者Key-Shared模式时，消费者数量不一定小于等于分区数。服务端会有一个负责分发消息的模块按照一定的方式（Shared模式默认是轮询，Key-Shared则是在同一个key内轮询）将消息分发给所有的消费者。
2. 当使用Shared模式，如果生产侧暂停了生产，则到了末尾一部分消息时，可能会出现消费分布不均的情况。
3. 使用多线程消费，即使复用一个consumer对象，消息的顺序也将无法得到保证。

以下给出一个Java基于Spring boot框架用线程池进行多线程消费的完整代码示例。

```java
import lombok.extern.slf4j.Slf4j;
import org.apache.pulsar.client.api.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.RejectedExecutionException;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

@Slf4j
@Service
public class ConsumerService implements Runnable {

    //从配置文件中获取serviceURL接入地址、Token密钥、Topic全名和Subscription名称（均可从控制台复制）
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
    private Thread dispatcherThread;

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
        executor = new ThreadPoolExecutor(10, 10, 0, TimeUnit.SECONDS, new ArrayBlockingQueue<>(100),
                new ThreadPoolExecutor.AbortPolicy());
        start = true;
        //如果要求具备顺序性，则用单线程进行消费，dispatcherThread为单线程消费示例
        //dispatcherThread = new Thread(this, "tdmq-dispatcher");
        //dispatcherThread.setDaemon(false);
        //dispatcherThread.setUncaughtExceptionHandler((t, e) -> logger.error("tdmq consumer uncaught error", e));
        //dispatcherThread.start();
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
        while (start) {
            //一定要用在循环中用try catch包括消息的业务处理流程（onConsume方法），否则可能出现业务卡住影响消费却无法感知
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
        logger.info("tdmq consumer stopped...");
    }

    /**
     * 这里写消费业务逻辑
     *
     * @param message
     * @return return true: 消息ack  return false: 消息nack
     * @throws Exception 消息nack
     */
    private void onConsumer(Message<String> message) throws Exception {
    //    单线程业务逻辑处理,直接在dispatcherThread中处理,严格保证消息顺序性
    //    System.out.println(Thread.currentThread().getName()+" - message receive: " + message.getValue());
    //    try {
    //        Thread.sleep(1000);//模拟业务逻辑处理
    //        tryAck(message);
    //    }catch (Exception exception){
    //        tryNack(message);
    //        logger.error(Thread.currentThread().getName() + " - message processing failed：" + message.getValue());
    //    }

        //多线程业务逻辑处理,消息之间局部顺序不保证
        try {
            executor.submit(() -> {
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
            });
        } catch (RejectedExecutionException e) {
            logger.error("Thread pool is exhausted! message={}", message.getValue());
        }
    }
}
```



