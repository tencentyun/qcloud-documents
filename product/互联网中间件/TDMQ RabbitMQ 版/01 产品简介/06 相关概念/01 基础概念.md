本文主要介绍了在使用 TDMQ RabbitMQ 版中常见的名词及解释说明。

| 概念           | 解释                                                         |
| -------------- | ------------------------------------------------------------ |
| Channel        | 在客户端的每个物理 TCP 连接里，可建立多个 Channel，每个 Channel 代表一个会话任务。 |
| Connection     | TCP 连接，生产者或消费者与 TDMQ RabbitMQ 版间的物理 TCP 连接。 |
| Vhost          | 虚拟主机（Virtual Host，Vhost），用作逻辑隔离，分别管理各自的 Exchange、Queue 和 Binding，使得应用安全的运行在不同的 Vhost 实例上，相互之间不会干扰。一个实例下可以有多个 Vhost，一个 Vhost 里面可以有若干个 Exchange 和 Queue。生产者和消费者连接消息队列 RabbitMQ 版需要指定一个 Vhost。 |
| Queue          | Queue（队列）是 RabbitMQ 的内部对象，用于存储消息。每个消息都会被投入到一个或多个 Queue 里。 |
| Exchange       | 生产者将消息发送到 Exchange，由 Exchange 将消息路由到一个或多个 Queue 中（或者丢弃）。Exchange 根据消息的属性或内容路由消息。 |
| Routing key    | 生产者在将消息发送到 Exchange 的时候，一般会指定一个 routing key，来指定这个消息的路由规则，而这个 routing key 需要与 Exchange Type 及 binding key 联合使用才能最终生效。<br/>在 Exchange Type 与 binding key 固定的情况下（在正常使用时一般这些内容都是固定配置好的），我们的生产者就可以在发送消息给 Exchange 时，通过指定 routing key 来决定消息流向哪里。 |
| Binding        | RabbitMQ 中通过 Binding 将 Exchange 与 Queue 关联起来，这样 RabbitMQ 就知道如何正确地将消息路由到指定的 Queue了。 |
| Binding key    | 在绑定（Binding）Exchange 与 Queue 的同时，一般会指定一个 binding key；消费者将消息发送给 Exchange 时，一般会指定一个 routing key；当 binding key 与 routing key 相匹配时，消息将会被路由到对应的 Queue 中。<br/>在绑定多个 Queue 到同一个 Exchange 的时候，这些 Binding 允许使用相同的 binding key。<br/>binding key  并不是在所有情况下都生效，它依赖于 Exchange Type，例如 fanout 类型的 Exchange 就会无视 binding key，而是将消息路由到所有绑定到该 Exchange 的 Queue。 |
| Exchange Types | RabbitMQ 常用的 Exchange Type 有 fanout、direct、topic 等。<li>fanout：fanout 类型的  Exchange 会把所有发送到该 Exchange 的消息路由到所有与它绑定的 Queue 中。</li><li>Direct：Direct 类型的  Exchange 会把消息路由到那些 binding key 与 routing key 完全匹配的 Queue 中。</li><li>Topic：该类型与 direct 类型相似，Topic 类型 Exchange 支持多条件匹配和模糊匹配，即使用 Routing Key 模式匹配和字符串比较的方式将消息路由至与其绑定的 Queue 中。</li> |
