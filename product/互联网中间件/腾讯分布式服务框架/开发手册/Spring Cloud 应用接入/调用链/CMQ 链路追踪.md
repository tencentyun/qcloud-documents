CMQ 组件目前通过 Spring Cloud Stream Binder 方式接入Spring Cloud 体系，对于 CMQ 组件的全链路追踪目前基于`spring-cloud-stream-binder-cmq`扩展实现，使用时需在上下游服务中添加`spring-cloud-stream-binder-cmq`依赖并按照规范进行 CMQ 配置。
```
<!-- 使用 CMQ -->
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>spring-cloud-stream-binder-cmq</artifactId>
    <version>VERSION</version>
</dependency>
```
配置参考：
```plaintext
spring:
  application:
    name: cmq-demo
  cloud:
    stream:
      bindings:
        input:
          destination: test-topic
          group: queue  # 必填，与 input.destination 共同组成消费队列
        output:
          destination: test-topic
      cmq:
        bindings:
          input:
            consumer:
              pollingWaitSeconds: 3
        binder:
          secretId: ***
          secretKey: ***
          endpoint: https://cmq-queue-***.api.qcloud.com
```
