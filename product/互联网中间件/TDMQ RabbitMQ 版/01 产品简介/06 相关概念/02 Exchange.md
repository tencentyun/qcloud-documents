本文介绍 TDMQ RabbitMQ 版中 Exchange 的概念、类型和使用方式。 

## 概念

Exchange 是 TDMQ RabbitMQ 版的消息路由代理，Producer 将消息发送到 Exchange 中，Exchange 根据消息的属性或内容将消息路由到一个或多个 Queue 中（或者丢弃），Consumer 从 Queue 中拉取消息进行消费。

TDMQ RabbitMQ 版目前支持 Direct、Fanout 和 Topic 三种类型的 Exchange。

- Direct：该类型 Exchange 会把消息路由到 RoutingKey 和 BindingKey 完全匹配的 Queue 中。

- Fanout：该类型 Exchange 会将消息路由到所有与其绑定的 Queue 中。

- Topic：该类型 Exchange 支持多条件匹配和模糊匹配，即使用 RoutingKey 模式匹配和字符串比较的方式将消息路由至与其绑定的Queue中。

## Direct Exchange

**路由规则**：Direct Exchange 会把消息路由到 RoutingKey 和 BindingKey 完全匹配的 Queue 中。

**应用场景**：该类型 Exchange 适用于通过简单字符标识符过滤消息的场景，常用于单播路由。

**使用示例**：

![](https://main.qcloudimg.com/raw/a192868e09939b2319263e40ff14b0eb.svg)

| Message   | Routing Key | Binding Key | Queue   |
| :-------- | :---------- | :---------- | :------ |
| Message 1 | `bizA`      | `bizA`      | Queue 1 |
| Message 2 | `bizB`      | `bizB`      | Queue 2 |

## Fanout Exchange

**路由规则**： 该类型 Exchange 会将消息路由到所有与其绑定的 Queue 中。

**应用场景**：该类型 Exchange 适用于广播消息的场景。例如分发系统使用 Fanout Exchange 来广播各种状态和配置更新。

**使用示例**

![](https://main.qcloudimg.com/raw/71beb7fdab5148b691f335b13990fd7c.svg)

| Message   | Routing Key       | Binding Key                 | Queue            |
| :-------- | :---------------- | :-------------------------- | :--------------- |
| Message 1 | `bazA.wechat_pay` | `bazA.credit`,`bazB.credit` | Queue 1，Queue 2 |
| Message 2 | `bazA.alipay`     | `bazA.credit`,`bazB.credit` | Queue 1，Queue 2 |
| Message 3 | `bazC.credit`     | `bazA.credit`,`bazB.credit` | Queue 1，Queue 2 |

## Topic Exchange

**路由规则**：该类型 Exchange 支持多条件匹配和模糊匹配，即使用 Routing Key 模式匹配和字符串比较的方式将消息路由至与其绑定的 Queue 中。

- Topic Exchange 支持的通配符包括星号“*”和井号“#”。

- 星号“*”代表一个英文单词，例如 sh。

- 井号“#”代表零个、一个或多个英文单词，单词间用英文句号"."分隔，例如 cn.hz。

**应用场景**

该类型 Exchange 常用于多播路由，例如需要使用 Topic Exchange 分发有关于特定地理位置的数据。

**使用示例**

![](https://main.qcloudimg.com/raw/79c7abdb6ae8797037893920149b9f5d.svg)

| Message   | Routing Key   | Binding Key             | Queue            |
| :-------- | :------------ | :---------------------- | :--------------- |
| Message 1 | `cn.hz`       | `cn.hz.#`               | Queue 1          |
| Message 2 | `cn.hz.store` | `cn.hz.#`、`cn.*.store` | Queue 1、Queue 2 |
| Message 3 | `cn.sz.store` | `cn.*.store`            | Queue 2          |
