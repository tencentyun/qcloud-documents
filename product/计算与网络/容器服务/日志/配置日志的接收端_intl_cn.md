## 配置日志的消费端

日志收集功能支持指定用户自建的 kafka 实例以及腾讯云 Ckafka 服务的指定实例的 Topic 作为日志内容的消费端，日志收集 Agent 会将收集到的日志发送到指定 Kafka 的指定 Topic。

## 配置 kafka 作为日志输出端

目前仅支持无访问认证的 kafka 实例，且需要保证集群内所有节点都能够访问到用户指定的 kafka Topic。需要注意的是，当配置接收端为 Kafka 时，日志收集功能仅支持无认证的 Kafka。

1. 创建日志收集规则
![][1]
2. 指定采集源
![][2]
3. 指定 Kafka 相应 Topic 作为日志接收端
![][3]


[1]:https://mc.qcloudimg.com/static/img/393ad1a2a9575cd89f1f0a38279bf676/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/852508e37092d197b37646aac6b50ed7/image.jpeg
[3]:https://mc.qcloudimg.com/static/img/0fe6bed71772b09231771e320a789e9d/image.jpeg



