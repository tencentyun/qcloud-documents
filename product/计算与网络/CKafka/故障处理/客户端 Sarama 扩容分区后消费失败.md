## 问题概述

[Sarama](https://github.com/Shopify/sarama) 是一个 go 语言编写的 Kafka 客户端，具有较高的消息吞吐性能。

当因为性能达到瓶颈，主动扩容 CKafka 分区后，Sarama 客户端可能会无法感知分区的 reBalance，导致新分区的信息无法被正常生产消费。

## 可能原因

CKafka 由于各种原因对分区进行 reBalance 后，Sarama 需要大约 10 分钟时间间隔感知分区变动，并拉取当前 topic 的 metadata，解析最新的分区数据。由于拉取时间较久，有时会被用户视作拉取失败。

除此之外，在 CKafka 团队长期维护使用中，也发现偶尔会出现 Sarama 客户端拉取最新分区信息失败，导致消息堆积并随机抛出异常的现象。

该场景已经在 Sarama 社区多次提出并且加以关注修复，在迄今为止的最新版本错误出现频率降低，但问题依旧存在。

## 解决方法

如果用户对 reBalance 现象敏感，并且使用 Golang 技术栈，建议尽快迁移使用 Confluent&trade;
维护的客户端 [Confluent-Kafka-go](https://github.com/confluentinc/confluent-kafka-go) 。

## 常用 Golang 客户端对比
<table>
    <thead>
    <tr>
        <th>Golang 客户端</th>
        <th>优点</th>
				<th>局限性</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Sarama</td>
        <td><ul style = "margin-bottom: 0px;"><li>社区活跃度高。Sarama 项目使用者较多，在社区提出问题得到解答与修复的时间较快。</li>
				<li>性能较高。Sarama 采用原生 Golang 语言编写，对于异步以及高并发操作支持度较好。</li></ul></td>
				<td>稳定性一般。Sarama 在扩容分区并 reBalance 后可能会有未知错误。</td>
    </tr>
    <tr>
        <td>Confluent-Kafka-go（推荐）</td>
        <td><ul style = "margin-bottom: 0px;"><li>非常稳定。由于客户端实际上是对于 <a href = "https://github.com/edenhill/librdkafka">librdkafka</a> C++ 库的一层封装， 而 librdkafka
  库已经在多种语言上运行多年，能够提供足够的可靠性。</li>
				<li>性能较高。由于底层使用 C++ 具体实现，所需资源较少，运算速度快。</li></ul></td>
				<td><ul style = "margin-bottom: 0px;"><li>增加编译复杂度。由于导入 C++ 库，Golang 编译器需要引入额外编译配置，增加了编译依赖，提高编译复杂度。</li>
				<li>除此之外，由于不同编译环境 C++ 库实现逻辑不同，引入 librdkafka 库可能会对 Golang 项目交叉编译造成影响。</li></ul></td>
    </tr>
		<tr>
        <td>kafka-go</td>
        <td><ul style = "margin-bottom: 0px;"><li>接口完善。kafka-go 不仅提供顶层接口，同时也暴露底层接口。用户可以更为灵活的调用配置 kafka 客户端。</li>
				<li>操作简单。kafka-go 在进行基础的生产消费所需代码较少，具有较多的缺省配置。</li></ul></td>
				<td>性能与前两款客户端相比性能较差，可能无法满足大规模并发需求。</td>
    </tr>
    </tbody>
</table>


  





