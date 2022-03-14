## 操作场景
本文主要介绍消息队列 CMQ 版控制流接口列表和 SDK 使用方式。

消息队列 CMQ 版控制流接口列表如下：

| 接口名称                                                     | 接口功能                       |
| :----------------------------------------------------------- | :----------------------------- |
| [CreateCmqQueue](https://cloud.tencent.com/document/api/1179/55917) | 创建 TDMQ CMQ 版队列接口       |
| [CreateCmqSubscribe](https://cloud.tencent.com/document/api/1179/55916) | 创建 TDMQ CMQ 版订阅接口       |
| [CreateCmqTopic](https://cloud.tencent.com/document/api/1179/55915) | 创建 TDMQ CMQ 版主题           |
| [DeleteCmqQueue](https://cloud.tencent.com/document/api/1179/55914) | 删除 TDMQ CMQ 版队列           |
| [DeleteCmqSubscribe](https://cloud.tencent.com/document/api/1179/55913) | 删除 TDMQ CMQ 版订阅           |
| [DeleteCmqTopic](https://cloud.tencent.com/document/api/1179/55912) | 删除 TDMQ CMQ 版主题           |
| [DescribeCmqDeadLetterSourceQueues](https://cloud.tencent.com/document/api/1179/55911) | 枚举 TDMQ CMQ 版死信队列源队列 |
| [DescribeCmqQueueDetail](https://cloud.tencent.com/document/api/1179/55910) | 查询 TDMQ CMQ 版队列详情       |
| [DescribeCmqQueues](https://cloud.tencent.com/document/api/1179/55909) | 查询 TDMQ CMQ 版全量队列       |
| [DescribeCmqSubscriptionDetail](https://cloud.tencent.com/document/api/1179/55908) | 查询 TDMQ CMQ 版订阅详情       |
| [DescribeCmqTopicDetail](https://cloud.tencent.com/document/api/1179/55907) | 查询 TDMQ CMQ 版主题详情       |
| [DescribeCmqTopics](https://cloud.tencent.com/document/api/1179/55906) | 枚举 TDMQ CMQ 版全量主题       |
| [ModifyCmqQueueAttribute](https://cloud.tencent.com/document/api/1179/55905) | 修改 TDMQ CMQ 版队列属性       |
| [ModifyCmqSubscriptionAttribute](https://cloud.tencent.com/document/api/1179/55904) | 修改 TDMQ CMQ 版订阅属性       |
| [ModifyCmqTopicAttribute](https://cloud.tencent.com/document/api/1179/55903) | 修改 TDMQ CMQ 版主题属性       |
| [RewindCmqQueue](https://cloud.tencent.com/document/api/1179/55902) | 回溯 TDMQ CMQ 版队列           |
| [UnbindCmqDeadLetter](https://cloud.tencent.com/document/api/1179/55901) | 解绑 TDMQ CMQ 版死信队列       |


## 操作步骤
消息队列 CMQ 版控制流 SDK 使用新版 API，以**创建 TDMQ CMQ 版队列接口**为例，具体使用方式如下。



#### 1. 登录 [云 API 控制台](https://console.cloud.tencent.com/api/explorer)。

#### 2. 选择 **API Explore** > **分布式消息队列** > **CMQ 管理相关接口**。

#### 3. 选择具体的接口，并填写输入参数。
输入参数说明如下：

| 参数名称            | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| QueueName           | 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。 |
| MaxMsgHeapNum       | 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。 |
| PollingWaitSeconds  | 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。         |
| VisibilityTimeout   | 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。 |
| MaxMsgSize          | 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。 |
| MsgRetentionSeconds | 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。 |
| RewindSeconds       | 队列是否开启回溯消息能力，该参数取值范围0-msgRetentionSeconds，即最大的回溯时间为消息在队列中的保留周期，0表示不开启。 |
| Transaction         | 1 表示事务队列，0 表示普通队列。                             |
| FirstQueryInterval  | 第一次回查间隔。                                             |
| MaxQueryCount       | 最大回查次数。                                               |
| DeadLetterQueueName | 死信队列名称。                                               |
| Policy              | 死信策略。0为消息被多次消费未删除，1为 Time-To-Live 过期。   |
| MaxReceiveCount     | 最大接收次数 1-1000。                                        |
| MaxTimeToLive       | polic 为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds。 |
| Trace               | 是否开启消息轨迹追踪，当不设置字段时，默认为不开启，该字段为 true 表示开启，为 false  表示不开启。 |

#### 4. 在线调用

输入参数填写完成后，在页面上方选择**在线调用**页签，单击**发送请求**，返回结果如下。

![](https://qcloudimg.tencent-cloud.cn/raw/cdb47132f961ffbb7573417b905db6a4.png)

#### 5. 生成代码示例

验证完成后，在**代码生成**页签的代码框中选择自己需要的语言，即可生成对应的代码示例。
以 Java 语言为例：

```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.tdmq.v20200217.TdmqClient;
import com.tencentcloudapi.tdmq.v20200217.models.*;

public class CreateCmqQueue
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey,此处还需注意密钥对的保密
            // 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
            Credential cred = new Credential("SecretId", "SecretKey");
            // 实例化一个 http 选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("tdmq.tencentcloudapi.com");
            // 实例化一个client选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的 client 对象,clientProfile 是可选的
            TdmqClient client = new TdmqClient(cred, "ap-guangzhou", clientProfile);
            // 实例化一个请求对象,每个接口都会对应一个 request 对象
            CreateCmqQueueRequest req = new CreateCmqQueueRequest();
            req.setQueueName("queen");
            req.setPollingWaitSeconds(10L);
            req.setVisibilityTimeout(10L);
            req.setMaxMsgSize(1048576L);
            req.setMsgRetentionSeconds(345600L);
            // 返回的 resp 是一个 CreateCmqQueueResponse 的实例，与请求对象对应
            CreateCmqQueueResponse resp = client.CreateCmqQueue(req);
            // 输出 json 格式的字符串回包
            System.out.println(CreateCmqQueueResponse.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
}
```

