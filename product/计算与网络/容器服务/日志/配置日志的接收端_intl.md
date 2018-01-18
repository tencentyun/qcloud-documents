## Configuring Consumer End of Log

Log collection feature allows users to specify the Topic of user-built Kafka pod and that of the specified pod of Tencent Cloud Ckafka service as the consumer end of log content. Log collection Agent sends collected logs to the specified Topic of specified Kafka.

## Configuring Kafka as Output End of Log

Only Kafka pods without access authentication are supported, and it needs to ensure that all nodes in the cluster can access the Kafka Topic specified by users. Please note that, when Kafka is configured as receiver, the log collection feature only supports Kafka without access authentication.

1. Create log collection rule
![][1]
2. Specify the source
![][2]
3. Specify the Topic of Kafka as log receiver
![][3]


[1]:https://mc.qcloudimg.com/static/img/393ad1a2a9575cd89f1f0a38279bf676/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/852508e37092d197b37646aac6b50ed7/image.jpeg
[3]:https://mc.qcloudimg.com/static/img/0fe6bed71772b09231771e320a789e9d/image.jpeg




