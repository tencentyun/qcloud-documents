本文主要介绍 auto.offset.reset 参数的相关概念及使用方式。

## 什么是 auto.offset.reset？

auto.offset.reset 参数定义了当无法获取消费分区的位移时从何处开始消费。例如：当 Broker 端没有 offset（如第一次消费或 offset 超过7天过期）时如何初始化 offset，当收到 OFFSET_OUT_OF_RANGE 错误时如何重置 Offset。

auto.offset.reset 参数设置有如下选项：
- earliest：表示自动重置到 partition 的最小 offset。
- latest：默认为 latest，表示自动重置到 partition 的最大 offset。
- none：不自动进行 offset 重置，抛出 OffsetOutOfRangeException 异常。

## 什么时候会出现 OFFSET_OUT_OF_RANGE？

该错误表示客户端提交的 offset 不在服务端允许的 offset 范围之内。例如：topicA 的分区1的 LogStartOffset 为100，LogEndOffset 为300，此时如果客户端提交的 offset 小于100或者大于300，服务端就会返回该错误，此时就会进行 offset 重置。

以下情况可能会导致客户端触发该错误：
- 客户端设置了 offset，然后一段时间内没有消费，但 Topic 设置了消息保留时间，当过了保留时间后， offset 在服务端已经被删除了，即发生了日志滚动，此时客户端再提交删除了的 offset，则会发生该错误。
- 因为 SDK Bug、网络丢包等问题，导致客户端提交了异常的 offset，则会触发该错误。
- 服务端有未同步副本，此时发生了 leader 切换，触发了 follower 副本的截断，此时如果客户端提交的 offset 在截断的范围之内，则会触发改错误。

## auto.offset.reset=none 使用说明

### 使用背景

不希望发生 offset 自动重置的情况，因为业务不允许发生大规模的重复消费。

>!此时消费组在第一次消费的时候就会找不到 offset 而报错，这时就需要在 catch 里手动设置 offset。


### 使用说明

auto.offset.reset 设置为 None 以后，可以避免 offset 自动重置的问题，但是当增加分区的时候，因为关闭了自动重置机制，客户端不知道新的分区要从哪里开始消费，则会产生异常，此时需要人工去设置消费分组 offset 并消费。

### 使用方式

消费者在消费时，当 consumer 设置 auto.offset.reset=none， 捕获到 NoOffsetForPartitionException 异常，在 catch 里自己设置 offset。您可以根据自身业务情况选择以下方式中的其中一种。

- 指定 offset，这里需要自己维护 offset，方便重试。
- 指定从头开始消费。
- 指定 offset 为最近可用的 offset。
- 根据时间戳获取 offset，设置 offset。

**示例代码如下：**

```java
package com.tencent.tcb.operation.ckafka.plain;

import com.google.common.collect.Lists;
import com.tencent.tcb.operation.ckafka.JavaKafkaConfigurer;
import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Properties;
import org.apache.kafka.clients.CommonClientConfigs;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.NoOffsetForPartitionException;
import org.apache.kafka.clients.consumer.OffsetAndTimestamp;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.PartitionInfo;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.config.SaslConfigs;

public class KafkaPlainConsumerDemo {

    public static void main(String args[]) {
        //设置JAAS配置文件的路径。
        JavaKafkaConfigurer.configureSaslPlain();

        //加载kafka.properties。
        Properties kafkaProperties = JavaKafkaConfigurer.getKafkaProperties();

        Properties props = new Properties();
        //设置接入点，请通过控制台获取对应Topic的接入点。
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, kafkaProperties.getProperty("bootstrap.servers"));

        //接入协议。
        props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
        //Plain方式。
        props.put(SaslConfigs.SASL_MECHANISM, "PLAIN");
        //两次Poll之间的最大允许间隔。
        //消费者超过该值没有返回心跳，服务端判断消费者处于非存活状态，服务端将消费者从Consumer Group移除并触发Rebalance，默认30s。
        props.put(ConsumerConfig.SESSION_TIMEOUT_MS_CONFIG, 30000);
        //每次Poll的最大数量。
        //注意该值不要改得太大，如果Poll太多数据，而不能在下次Poll之前消费完，则会触发一次负载均衡，产生卡顿。
        props.put(ConsumerConfig.MAX_POLL_RECORDS_CONFIG, 30);
        //消息的反序列化方式。
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,
                "org.apache.kafka.common.serialization.StringDeserializer");
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,
                "org.apache.kafka.common.serialization.StringDeserializer");
        //当前消费实例所属的消费组，请在控制台申请之后填写。
        //属于同一个组的消费实例，会负载消费消息。
        props.put(ConsumerConfig.GROUP_ID_CONFIG, kafkaProperties.getProperty("group.id"));

        //消费offset的位置。注意！如果auto.offset.reset=none这样设置，消费组在第一次消费的时候 就会报错找不到offset，第一次这时候就需要在catch里手动设置offset。
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "none");
        //构造消费对象，也即生成一个消费实例。
        KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
        //设置消费组订阅的Topic，可以订阅多个。
        //如果GROUP_ID_CONFIG是一样，则订阅的Topic也建议设置成一样。
        List<String> subscribedTopics = new ArrayList<String>();
        //如果需要订阅多个Topic，则在这里添加进去即可。
        //每个Topic需要先在控制台进行创建。
        String topicStr = kafkaProperties.getProperty("topic");
        String[] topics = topicStr.split(",");
        for (String topic : topics) {
            subscribedTopics.add(topic.trim());
        }
        consumer.subscribe(subscribedTopics);
        //循环消费消息。
        while (true) {
            try {
                ConsumerRecords<String, String> records = consumer.poll(1000);
                //必须在下次Poll之前消费完这些数据, 且总耗时不得超过SESSION_TIMEOUT_MS_CONFIG。 建议开一个单独的线程池来消费消息，然后异步返回结果。
                for (ConsumerRecord<String, String> record : records) {
                    System.out.println(
                            String.format("Consume partition:%d offset:%d", record.partition(), record.offset()));
                }
            } catch (NoOffsetForPartitionException e) {
                System.out.println(e.getMessage());

                //当auto.offset.reset设置为 none时，需要捕获异常 自己设置offset。您可以根据自身业务情况选择以下方式中的其中一种。
                //e.g 1 :指定offset, 这里需要自己维护offset，方便重试。
                Map<Integer, Long> partitionBeginOffsetMap = getPartitionOffset(consumer, topicStr, true);
                Map<Integer, Long> partitionEndOffsetMap = getPartitionOffset(consumer, topicStr, false);
                consumer.seek(new TopicPartition(topicStr, 0), 0);

                //e.g 2:从头开始消费
                consumer.seekToBeginning(Lists.newArrayList(new TopicPartition(topicStr, 0)));

                //e.g 3:指定offset为最近可用的offset。
                consumer.seekToEnd(Lists.newArrayList(new TopicPartition(topicStr, 0)));

                //e.g 4: 根据时间戳获取offset，就是根据时间戳去设置offset。例如重置到10分钟前的offset
                Map<TopicPartition, Long> timestampsToSearch = new HashMap<>();
                Long value = Instant.now().minus(300, ChronoUnit.SECONDS).toEpochMilli();
                timestampsToSearch.put(new TopicPartition(topicStr, 0), value);
                Map<TopicPartition, OffsetAndTimestamp> topicPartitionOffsetAndTimestampMap = consumer
                        .offsetsForTimes(timestampsToSearch);
                for (Entry<TopicPartition, OffsetAndTimestamp> entry : topicPartitionOffsetAndTimestampMap
                        .entrySet()) {
                    TopicPartition topicPartition = entry.getKey();
                    OffsetAndTimestamp entryValue = entry.getValue();
                    consumer.seek(topicPartition, entryValue.offset()); // 指定offset, 这里需要自己维护offset，方便重试。
                }


            }
        }
    }

    /**
     * 获取topic的最早、最近的offset
     * @param consumer
     * @param topicStr
     * @param beginOrEnd true begin; false end
     * @return
     */
    private static Map<Integer, Long> getPartitionOffset(KafkaConsumer<String, String> consumer, String topicStr,
            boolean beginOrEnd) {
        Collection<PartitionInfo> partitionInfos = consumer.partitionsFor(topicStr);
        List<TopicPartition> tp = new ArrayList<>();
        Map<Integer, Long> map = new HashMap<>();
        partitionInfos.forEach(str -> tp.add(new TopicPartition(topicStr, str.partition())));
        Map<TopicPartition, Long> topicPartitionLongMap;
        if (beginOrEnd) {
            topicPartitionLongMap = consumer.beginningOffsets(tp);
        } else {
            topicPartitionLongMap = consumer.endOffsets(tp);
        }
        topicPartitionLongMap.forEach((key, beginOffset) -> {
            int partition = key.partition();
            map.put(partition, beginOffset);
        });
        return map;
    }

}
```
