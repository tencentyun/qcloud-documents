新版本 CKafka 实例支持对 topic 进行细粒度的参数配置，用户可以在管理 topic 页面的高级配置中设置如下参数：

![](https://main.qcloudimg.com/raw/54b52b74d021ff478725f8b2144b1d88.png)
参数说明如下：

| 参数名     | 默认值 | 参数范围  |说明|
| :-------- | :--------| :------ |:------ |
|cleanup.policy|delete|delete/compact|支持日志按保存时间删除，或者日志按 key 压缩（kafka connect 时需要使用 compact 模式）。|
|min.insync.replicas|1|-|当 producer 设置 request.required.acks 为 -1 时，min.insync.replicas 指定 replicas  的最小数目。|
|unclean.leader.election.enable|true|true/false|指定是否能够设置不在 ISR 中 replicas 作为 leader。|
|segment.ms|-|1day-30days|Segment 分片滚动的时长，单位为 ms，最小值 86400000ms。 |
|retention.ms|默认为实例的消息保留时间|60000ms-30days|topic 维度的消息保留时间（非独占的实例暂不开放）。|
