欢迎使用云消息服务CMQ（Cloud Message Queue）。

腾讯云消息队列（Cloud Message Queue，以下简称CMQ）是分布式的消息队列服务，用于存储进程间传输的消息，为分布式部署的不同应用之间或者一个应用的不同组件之间提供基于消息的可靠的异步通信服务。消息被存储在高可靠、高可用的消息队列中，多进程可以同时读写，互不干扰。使用腾讯云CMQ，用户可以在执行不同任务的应用程序的分布式组件之间传递信息，既不会丢失消息，也不要求各个组件始终处于可用状态。

队列在数据发送端以及数据接收端之间起到缓冲作用。这样，在数据发送端的工作速度快于数据接收端的情况下，或者在数据发送端或数据接收端仅间歇性地连接到网络的情况下，队列可解决因此而产生的问题。

传统的进程通信模式由客户端请求服务器端的服务并等待服务器的响应。然而这种模式有很多弊端，比如当网络状况不好的情况下客户端的请求可能会丢失；又如服务器端处理时间过长可能导致客户端长时间等待以致请求超时而失败等。

为此，腾讯云引入了消息队列服务进行消息分发和管理。使用腾讯云CMQ，您可以分离应用程序的组件以便其独立运行，同时还可以简化组件间的消息管理。分布式应用程序的任何组件均可将消息存储在队列中，腾讯云 CMQ 确保每条消息至少传送一次，并且支持多次读取和写入。单个队列可由多个分布式应用程序组件同时使用而无需这些组件之间的互相协作。所有组件均可使用 CMQ API 以编程方式检索和操作消息。

支持的全部操作可参见[API概览页](/doc/api/431/5852)。

请确保在使用这些接口前，已充分了解了[CMQ产品说明](https://cloud.tencent.com/doc/product/406)。

**注意：协助者帐号目前不能用于cmq的操作。**

## 队列模型

### 术语表
本文档涉及的一些常用术语如下：

| 术语 | 全称  | 中文 | 说明 |
|---------|---------|---------|---------|
| CMQ | Cloud Message Queue | 云消息服务 | 腾讯云的消息服务包括了队列模型，主题模型，高性能消息服务等等。|
| Queue | Queue | 队列 | 队列是一种先进先出的数据模型，生产者可并发地往队列尾部添加数据，消费者可并发地从队列头部拉取(pull)数据。|
| Active | Active | 可被消费（可见）状态 | 消息处于active状态时，可被所有消费者争抢消费，但只有一个消费者能成功将其消费，此时消息变为inactive状态，对其他消费者不可见。|
| Inactive | Inactive | 不可被消费（不可见）状态 | 消息处于Inactive状态时，说明消息正在被某个消费者消费的过程中，其他消费者不能消费该消息。|
| (Batch)ReceiveMessage | (Batch) Receive Message | 消费消息 | ReceiveMessage操作仅仅会把消息从active状态置为inactive状态，使得该消息不能被其他消费者消费到。但消费完后要显式调用(Batch)DeleteMessage操作才能把消息从队列中删除掉，否则消息过了visibilityTimeout指定的时间后，重新变为active状态，又可被其他消费者消费到，造成意料之外地重复消息。|
| maxMsgHeapNum | Maximum Message Heap Number | 最大消息堆积数 | 为防止消息未被及时消费导致消息丢失，消息服务具有堆积消息的功能，但堆积的消息数是有上限的。超过上限后生产者不能再往队列中添加消息。等消息被消费完删除后，生产者又可以往队列中添加消息。|
| pollingWaitSeconds | Polling Wait Seconds |  消息接收长轮询等待时间 | 消费者想向队列中拉取消息进行消费时，队列可能暂时没有数据。消费者可能不想马上返回（类似于非阻塞模式），想等待一段时间看看会不会有消息过来（类似于阻塞模式），pollingWaitSeconds类似于阻塞模式下的超时时间，超过这个时间，不管有没有消息，都会返回。如果想非阻塞地消费消息，把该值置为0即可。|
| msgRetentionSeconds | Message Retention Seconds | 消息保留周期 | 堆积在队列中的消息是有保留时间的，超过该时间仍未被消费者消费，则会被队列删除掉，消费者再也无法消费到。|
| receiptHandle | Receipt Handle | 消息收据句柄 | 该句柄是消息被消费时返回的，只有当前正在消费该消息的句柄才能删除消息。如果消费时间过长，超过了visibilityTimeout，则消息又被其他消费者消费到，那之前消费者的获取该消息的句柄就会失效，不能用于删除消息。|
| qps throttling | QPS Throttling | qps 限制 | 该术语本来的含义是每秒钟请求数限制，但实际上是每秒钟消息数的限制。对于单次接口(SendMessage, ReceiveMessage, DeleteMessage)，还是每秒钟请求次数。但是对于批量接口(BatchSendMessage, BatchReceiveMessage, BatchDeleteMessage)，则是1s内，所有批量值之和。这样限制的目的是为了给用户提供一个更加稳定和公平的产品。如果您需要更大的消息数限制值，可以提[工单](https://console.cloud.tencent.com/workorder/category)向我们申请。|




### 输入参数与返回参数释义
- limit 和 offset

	>用来控制分页的参数；当相应结果是列表形式时，如果数量超过了 limit 所限定的值，那么只返回limit个值。用户可以通过 limit 和 offset 两个参数来控制分页：limit 为单次返回的最多条目数量，offset 为偏移量。
	>举例来说，参数 offset=0&limit=20 返回第0到20项，offset=20&limit=20 返回第20到40项，offset=40&limit=20 返回第40到60项；以此类推。
	
- id.n

	>同时输入多个参数的格式。当遇到形如这样的格式时，那么该输入参数可以同时传多个。例如：
	
	> id.0=“10.12.243.21”&id.1=“10.12.243.21”&id.2=“10.12.243.21”&id.3=“10.12.243.21”...
	
	> 以此类推（以下标0开始）。


## API快速入门

用户可以通过[CMQ SDK](https://cloud.tencent.com/product/cmq#sdk) （推荐，目前提供多个语言版本），或直接调用云API（较为麻烦，建议SDK语言之外的用户使用）使用CMQ的服务：

1. 选择地域和内外网。与其他云产品不同，消息队列 API 的请求域名随地域不同而变化，需选择地域对应的域名，请求域名的构成规则形如 `cmq-queue-region.api.qcloud.com/v2/index.php` ，其中 region 字段需用具体地域替换：gz（广州），sh（上海），bj（北京）。如果是用户使用的机器是腾讯云服务器，则应优先选择内网域名，否则选外网域名。

2. [创建队列](/doc/api/431/5832)。SDK（或云API）调用 CreateQueue 接口。

3. [发送消息](/doc/api/431/5837)。SDK（或云API）调用 SendMessage(或BatchSendMessage) 接口。

4. [消费消息](/doc/api/431/5839)。SDK（或云API）调用 ReceiveMessage(或BatchReceiveMessage) 接口。

5. [删除消息](/doc/api/431/5840)。SDK（或云API）调用 DeleteMessage(或BatchDeleteMessage) 接口。

6. [删除队列](/doc/api/431/5836)。SDK（或云API）调用 DeleteQueue 接口。

## 主题模型

### 术语表
本文档涉及的一些常用术语如下：

| 术语 | 英文 | 说明 |
|---------|---------|---------|
| 订阅者	| Subscriber | 指CMQ-topic模式下，服务的订阅方 |
| 生产	| Produce	| 指生产者，往topic内写入消息的操作 |
| 投递	| Subscription	| 指topic像订阅者投递消息的过程 |
| 消息接收模式（PUSH）|	Message-receiving model（PUSH）| CMQ的TOPIC模型，已支持主动推送的 PUSH 模式 |
| 重试策略	| NotifyStrategy	| 订阅的NotifyStrategy属性，向接收端推送消息出现错误时的重试策略。该策略默认开启。有两个选项，二选一：a.退避重试：重试3次，间隔时间10-20s之间的一个随机值，超过3次后，该条消息对于该订阅者丢弃，不会再重试； b. 衰退指数重试：重试176次，总计重试时间为1天，间隔时间依次为：2^0，2^1, …, 512, 512, …, 512秒。默认勾选 衰退指数重试策略。两者必须勾选1个 |
| 消息生命周期 | msgRetentionSeconds | 消息在TOPIC中最长的存活时间，从发送到该队列开始经过此参数指定的时间后，不论消息是否被取出过都将被删除；单位为秒，默认值为86400s（1天），不允许修改 |
| 消息最大长度 | MaxMsgSize | 限定允许发送到该队列的消息体的最大长度；单位为byte， 有效值范围为1024-65536 也即1K到64K |
| 消息堆积 | MessageRetentionPeriod | 默认开启。存在生产者的消息，还未触发投递到订阅者，或订阅者接收消息失败，暂时堆积到TOPIC中，进行多次重试。该项目无法配置，最大堆积时间为1天 |
| 重试验证 | Status code | TOPIC投递到订阅者后，若https返回码为200，则认为成功 |
| 添加订阅者标签 |	FilterTag | 添加订阅者时，可增加FilterTag，增加filtertag后，该订阅者仅能收到带该filtertag的消息。单个tag不超过16个字符的字符串，单个订阅者可最多添加个tag。只要其中某个tag，能匹配topic的过滤标签，都能收到该次topic投递的消息，若消息不带任何标签，则该订阅者无法收到该类型消息 |
| 添加消息过滤标签 | Messagetag	| 即消息标签、消息类型，用来区分某个CMQ的Topic下的消息分类。MQ允许消费者按照Tag对消息进行过滤，确保消费者最终只消费到他关心的消息类型。该功能默认不开启，未开启时，所有消息向所有订阅者发送，当订阅者设置了tag时，由于不匹配，该订阅者无法收到消息。消息过滤标签描述了该订阅中消息过滤的标签（标签一致的消息才会被推送）。单个tag不超过16个字符的字符串，单个message可最多添加5个tag |
| 开启日志轨迹 |	LoggingEnabled | 是否开启日志管理功能，True表示启用，False表示停用。启用后，CMQ的原始log会写入COS对象存储。且用户可通过CMQ控制台，做LOG聚合查询，免除自行搭建分析系统的繁琐 |

### 输入参数与返回参数释义
- limit 和 offset

	>用来控制分页的参数；当相应结果是列表形式时，如果数量超过了 limit 所限定的值，那么只返回limit个值。用户可以通过 limit 和 offset 两个参数来控制分页：limit 为单次返回的最多条目数量，offset 为偏移量。
	>举例来说，参数 offset=0&limit=20 返回第0到20项，offset=20&limit=20 返回第20到40项，offset=40&limit=20 返回第40到60项；以此类推。
	
- id.n

	>同时输入多个参数的格式。当遇到形如这样的格式时，那么该输入参数可以同时传多个。例如：
	
	> id.0=“10.12.243.21”&id.1=“10.12.243.21”&id.2=“10.12.243.21”&id.3=“10.12.243.21”...
	
	> 以此类推（以下标0开始）。


## API快速入门

用户可以通过CMQ SDK（推荐，目前提供多个语言版本），或直接调用云API（较为麻烦，建议SDK语言之外的用户使用）使用CMQ的服务：

1. 选择地域和内外网。与其他云产品不同，消息队列 API 的请求域名随地域不同而变化，需选择地域对应的域名，请求域名的构成规则形如 `cmq-topic-region.api.qcloud.com/v2/index.php` ，其中 region 字段需用具体地域替换：gz（广州），sh（上海），bj（北京）。如果是用户使用的机器是腾讯云服务器，则应优先选择内网域名，否则选外网域名。

2. [创建主题](/doc/api/406/7405)。SDK（或云API）调用 CreateTopic 接口。

3. [修改主题属性](/doc/api/406/7406)。SDK（或云API）调用 SetTopicAttributes接口。

4. [获取主题列表](/doc/api/406/7407)。SDK（或云API）调用 ListTopic 接口。

5. [获取主题属性](/doc/api/406/7408)。SDK（或云API）调用 GetTopicAttributes 接口。

6. [删除主题](/doc/api/406/7409)。SDK（或云API）调用 DeleteTopic 接口。

7. [发布消息](/doc/api/406/7411)。SDK（或云API）调用 PublishMessage 接口。

8. [批量发布消息](/doc/api/406/7412)。SDK（或云API）调用 BatchPublishMessage 接口。

9. [投递消息](/doc/api/406/7420)。

10. [创建订阅](/doc/api/406/7414)。SDK（或云API）调用 Subscribe 接口。

11. [获取订阅列表](/doc/api/406/7415)。SDK（或云API）调用 ListSubscriptionByTopic 接口。

12. [修改订阅属性](/doc/api/406/7416)。SDK（或云API）调用 SetSubscriptionAttributes 接口。

13. [获取订阅属性](/doc/api/406/7418)。SDK（或云API）调用 GetSubscriptionAttributes 接口。

14. [删除订阅](/doc/api/406/7417)。SDK（或云API）调用 Unsubscribe 接口。






