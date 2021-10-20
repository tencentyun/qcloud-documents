## 操作场景
TDMQ Pulsar 版现已支持 Pulsar 社区版 Java SDK。本文介绍如何使用 Pulsar 社区版 Java SDK 完成接入。

## 操作步骤
Pulsar Java SDK 接入步骤如下：
1. 按照 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-java/) 添加 Maven 依赖。
<dx-codeblock>
:::  xml
``` xml
<!-- in your <properties> block -->
<pulsar.version>2.7.1</pulsar.version>

<!-- in your <dependencies> block -->
<dependency>
	<groupId>org.apache.pulsar</groupId>
	<artifactId>pulsar-client</artifactId>
	<version>${pulsar.version}</version>
</dependency>
```
:::
</dx-codeblock>
2. 在 `pom.xml` 所在目录执行 `mvn clean package` 即可下载 Pulsar 社区版 Java SDK。
3. 前往 TDMQ Pulsar 版控制台 **[角色管理](https://console.cloud.tencent.com/tdmq/role)**，复制密钥。
4. 在创建 Client 的代码中加入刚复制的密钥（集群版本为2.6.1的则还添加 `listenerName` 参数）。
>?您可以点击以下页签，查看不同版本集群的接入示例。
<dx-tabs>
::: 2.7.1版本及以上集群接入示例
<dx-codeblock>
:::  java
PulsarClient client = PulsarClient.builder()
		.serviceUrl("http://***")//完整复制控制台接入点地址
		.authentication(AuthenticationFactory.token("eyJh****"))
		.build();
:::
</dx-codeblock>
:::
::: 2.6.1版本集群接入示例
<dx-codeblock>
:::  java
PulsarClient client = PulsarClient.builder()
		.serviceUrl("pulsar://*.*.*.*:6000/")//接入地址到集群管理-接入点列表完整复制
		.listenerName("custom:********/vpc-******/subnet-********")//custom:+路由ID，到集群管理-接入点列表完整复制
		.authentication(AuthenticationFactory.token("eyJh****"))
		.build();
:::
</dx-codeblock>
:::
</dx-tabs>

关于 Pulsar 社区版 Java SDK 各种功能的使用方式，请参考 [Pulsar 官方文档](http://pulsar.apache.org/docs/en/client-libraries-java/)。

