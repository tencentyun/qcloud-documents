## 操作场景
消息队列现已兼容部分 Pulsar 社区版 SDK。本文介绍如何使用 Pulsar 社区版 Java SDK 完成接入。

如果您是第一次使用 Pulsar 或者 TDMQ，推荐您选择我们提供的商业版 SDK，商业版 SDK 相较社区版本有所优化，使用商业版 SDK 也能第一时间体验我们新推出的功能（例如事务消息）。



## 操作步骤
Pulsar Java SDK 接入步骤如下：
1. 按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-java/) 添加 Maven 依赖。
   ```xml
   <!-- in your <properties> block -->
   <pulsar.version>2.6.1</pulsar.version>
   
   <!-- in your <dependencies> block -->
   <dependency>
     <groupId>org.apache.pulsar</groupId>
     <artifactId>pulsar-client</artifactId>
     <version>${pulsar.version}</version>
   </dependency>
```
2. 在 `pom.xml` 所在目录执行`mvn clean package`即可下载 Pulsar 社区版 Java SDK。
3. 前往 TDMQ 控制台【[角色管理](https://console.cloud.tencent.com/tdmq/role)】，复制密钥。
4. 在创建 Client 的代码中加入刚复制的密钥，并添加 `listenerName` 参数。
   ```java
   PulsarClient client = PulsarClient.builder()
            .serviceUrl("pulsar://*.*.*.*:6000/")
            .listenerName("custom:1********0/vpc-******/subnet-********")//custom:+路由ID
            .authentication(AuthenticationFactory.token("eyJh****"))
            .build();
   ```
关于 Pulsar 社区版 Java SDK 各种功能的使用方式，请参考 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-java/)。

