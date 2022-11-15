## 操作场景

与任何客户端-服务器应用程序一样，Kafka 通过一组明确定义的 API 提供对其功能的访问，这些 API 通过 Kafka 协议公开，是一种仅限于 Kafka 的 TCP 二进制协议。与 Kafka API 交互的最佳方式是客户端通过使用 Kafka 协议，Apache Kafka 项目仅正式支持 Java 的客户端库，但除此之外，Confluent 还正式支持 C/C++，C#，Go 和 Python 的客户端库。

一些编程语言缺乏官方支持的 Kafka 生产级客户端，而 HTTP 是一种广泛可用、普遍支持的协议，DataHub 数据接入通过 HTTP 协议公开消息发送 API，以便于简化客户端复杂的配置。

本文介绍 DataHub 服务的 HTTP 数据接入功能中的发送消息结合实际应用场景提供建议。

## 技术架构

HTTP 数据接入层开启后，公网的 HTTP 客户端可通过云 API 直接向 CKafka 所在的实例发送消息。示意图如下：

![](https://qcloudimg.tencent-cloud.cn/raw/37a35f97e9ede93e35b3a3567cc50884.jpg)

### 前提条件

已创建好目标 CKafka 实例和 Topic。

## 操作步骤

### 创建数据接入任务

具体操作请参见 [DataHub 操作指南-HTTP 主动上报](https://cloud.tencent.com/document/product/597/66017)。


### 使用 SDK 发送消息

1. 参见 [SDK中心：Java](https://cloud.tencent.com/document/sdk/Java) 在 Java 项目通过 Maven、Gradle 等方式引入数据上报 SDK。以下是配置项目的 pom.xml 文件。
<dx-codeblock>
:::  xml
<dependency>
    <groupId>com.tencentcloudapi</groupId>
    <artifactId>tencentcloud-sdk-java</artifactId>
    <version>3.1.430</version>
</dependency>
:::
</dx-codeblock>
2. 单击 [数据接入](https://console.cloud.tencent.com/ckafka/datahub-access) 的任务详情， 复制接入点信息到 SDK 中使用，用于写入数据。
![](https://qcloudimg.tencent-cloud.cn/raw/c0cdd9480626d044fbab71b63d35679e.png)
3. 示例中通过 **generateMsgFromUserAccess** 将所有要发送的消息组装起来，复制接入点信息。
<dx-codeblock>
:::  java
List<BatchContent> batchContentList = generateMsgFromUserAccess(userId);
// 其中 ap-xxx 为对应的云API地域简称
CkafkaClient client = new CkafkaClient(
   new Credential("yourSecretId", "yourSecretKey"), "ap-xxx");
   
SendMessageRequest messageRequest = new SendMessageRequest();
// 数据接入任务接入点ID
messageRequest.setDataHubId("datahub-lzxxxxx6");
messageRequest.setMessage(batchContentList.toArray(BatchContent[]::new));

try {
  SendMessageResponse sendMessageResponse = client.SendMessage(messageRequest);
  String[] messageId = sendMessageResponse.getMessageId();
  for (String s : messageId) {
	 LOGGER.info(s)
  }
} catch (TencentCloudSDKException e) {
  LOGGER.error(e.getMessage());
}
:::
</dx-codeblock>
4. 通过 HTTP 接入层发送消息的返回值示例如下。
<dx-codeblock>
:::  json
{
    "Response": {
        "MessageId": [
            "datahub-lxxxxxx6:topicDev:4:2:1648185961342:1648185961398"
        ],
        "RequestId": "3fq3na5r-xxxx-xxxx-xxxx-b2fiv0se7ded"
    }
}
:::
</dx-codeblock>
5. 其中 **MessageId** 内容由一系列发送至 CKafka 实例后返回的元数据组成。如下分别为：
<dx-codeblock>
:::  json
"[datahubId]:[topic名称]:[所在的topic分区数]:[所在分区的offset]:[HTTP接入层收到消息的时间]:[消息发送至Kafka的时间]"
:::
</dx-codeblock>


### 查询消息

通过 [CKafka 控制台](https://cloud.tencent.com/document/product/597/53176) 查询 HTTP 接入层发送的消息，详细操作参见 [消息查询](https://cloud.tencent.com/document/product/597/53176)。如下图，示例 topic 名称为 topicDev 的4号分区查询2号位点消息。
![](https://qcloudimg.tencent-cloud.cn/raw/9aa559445ddd6053bc6bcba0eceb9cbf.png)


### 任务暂停

当您发现数据接入任务影响了正常业务时，可以暂停数据接入。

1. 在 [数据接入](https://console.cloud.tencent.com/ckafka/datahub-access) 页面，单击目标任务的操作栏的**暂停**，可暂停任务。
![](https://qcloudimg.tencent-cloud.cn/raw/d41b251855cc6f057c4cdb2497069f19.png)
2. 出现右上角的提示，则任务暂停成功。
![](https://qcloudimg.tencent-cloud.cn/raw/417a61130eefa1d41ee1a29bfdb4a394.png)
3. 此时通过 HTTP 接入层发送消息得到示例如下：
<dx-codeblock>
:::  json
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "task status suspended [datahub-lxxxxxx6]"
        },
        "RequestId": "5f737a5b-xxxx-xxxx-xxxxx-b2fb703e7ded"
    }
}
:::
</dx-codeblock>

