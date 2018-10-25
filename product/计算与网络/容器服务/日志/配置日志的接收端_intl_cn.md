## 配置日志的消费端

日志收集功能支持指定用户自建的 kafka 实例、腾讯云 Ckafka 服务的指定实例的 Topic 和腾讯云 日志服务CLS 指定的日志主题作为日志内容的消费端，日志收集 Agent 会将收集到的日志发送到指定 Kafka 的指定 Topic 或指定的 CLS 日志主题。

## 配置 kafka 作为日志输出端

目前仅支持无访问认证的 kafka 实例，且需要保证集群内所有节点都能够访问到用户指定的 kafka Topic。需要注意的是，当配置接收端为 Kafka 时，日志收集功能仅支持无认证的 Kafka。

1. 创建日志收集规则
![][1]

2. 指定收集源
![][2]

3. 指定 Kafka 相应 Topic 作为日志接收端
![][3]

## 配置 日志服务CLS 作为日志输出端

需要注意，日志服务CLS 目前只能支持同地域的容器集群进行日志收集上报。

1. 创建日志收集规则
![][1]

2. 指定收集源
![][2]

3. 如果需要创建日志集，因为容器服务的日志有独立的采集能力，所以新建日志集不需要选择 Agent 采集
![][4]

4. 指定日志主题作为日志接收端
![][5]

[1]:https://mc.qcloudimg.com/static/img/393ad1a2a9575cd89f1f0a38279bf676/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/526919a65957b87d39154510ba8fa76d/collect.png
[3]:https://mc.qcloudimg.com/static/img/2247389b857b20cceabd0c6dccdbcc8a/ckafa.png
[4]:https://mc.qcloudimg.com/static/img/b845c5063884e02c6bdedc4c7184667a/image.png
[5]:https://mc.qcloudimg.com/static/img/4d52a836e1c50cbe46fb7d8d4049bf8a/image.png


