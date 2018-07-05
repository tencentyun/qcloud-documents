## Configuring Consumer End of Log

Log collection feature allows users to specify the Topic of user-built Kafka pod， Topic of specified Tencent Cloud Ckafka pod， and specified CLS log topic as the consumer of log content. Log collection Agent sends collected logs to the specified Topic of specified Kafka or specified CLS log topic.

## Configuring Kafka as Output End of Log

Only Kafka pods without access authentication are supported, and it needs to ensure that all nodes in the cluster can access the Kafka Topic specified by users. Please note that, when Kafka is configured as receiver, the log collection feature only supports Kafka without access authentication.

1. Create log collection rule
![][1]

2. Specify the collecting source
![][2]

3. Specify the Topic of Kafka as log receiver
![][3]

## Configuring CLS as the log output end

Please note that CLS collects only logs of container clusters in the same region.

1. Create log collection rule
![][1]

2. Specify the collecting source
![][2]

3. As TKE has independent log collection capability, you don't need to select Agent creating a log collection
![][4]

4. Specified the log topic as the log receiver
![][5]

[1]:https://mc.qcloudimg.com/static/img/393ad1a2a9575cd89f1f0a38279bf676/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/526919a65957b87d39154510ba8fa76d/collect.png
[3]:https://mc.qcloudimg.com/static/img/2247389b857b20cceabd0c6dccdbcc8a/ckafa.png
[4]:https://mc.qcloudimg.com/static/img/b845c5063884e02c6bdedc4c7184667a/image.png
[5]:https://mc.qcloudimg.com/static/img/4d52a836e1c50cbe46fb7d8d4049bf8a/image.png





