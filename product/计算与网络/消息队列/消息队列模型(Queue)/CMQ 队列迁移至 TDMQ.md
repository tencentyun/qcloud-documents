## 操作场景

本文以一个 Java 客户端为例，为您介绍将 CMQ 队列迁移至 TDMQ CMQ 版的操作步骤。

**迁移原理**
<img src="https://main.qcloudimg.com/raw/bd0a7851575796b8c954eeeb6dcf8144.png" width="569">


**方案总览**
<img src="https://main.qcloudimg.com/raw/a6e13ca122d8524b365c83b53ec05c9b.png" width="569">


**整体流程**
<dx-steps>
-在控制台上将 CMQ 的队列和主题元数据迁移至 TDMQ CMQ 版中。
-旧的消费者保持不动，消费端新建消费者，接入到 TDMQ CMQ 版的队列中。
-生产者停止向原 CMQ 队列生产消息，并切换生产流接入到 TDMQ CMQ 版队列中。
-旧的消费者继续消费原 CMQ 队列中的存量消息，消费完成后下线 CMQ 业务消费者。
</dx-steps>


## 前提条件

参考 [SDK 文档](https://cloud.tencent.com/document/product/406/35818)部署好 CMQ 队列的生产端和消费端服务，并且运行正常。以下迁移步骤以 TCP SDK 为例。

## 操作步骤

### 步骤1：迁移元数据

1. 登录 [CMQ 控制台](https://console.cloud.tencent.com/cmq)。
2. 在左侧导航栏选择**队列**，选择好**地域**后，单击页面上方的**同步到 TDMQ**。
3. 在弹出的窗口中单击**启动**，将该地域下的所有队列和主题元数据迁移至 TDMQ CMQ 版中。
   ![](https://main.qcloudimg.com/raw/0d1d65697c56dfa776c6036a52eb3d79.png)
4. 迁移完成后，登录 [TDMQ 控制台](https://console.cloud.tencent.com/tdmq)。
5. 在左侧导航栏选择**队列服务**，选择相同的**地域**可看到迁移到 TDMQ CMQ 版的队列。
	 ![](https://main.qcloudimg.com/raw/f74407c4a979dc3b01cb18c4d37ed729.png)

### 步骤2：新建消费者

1. 在消费端新建一个消费者，并接入到 TDMQ CMQ 版队列中。
```java
Consumer consumer = new Consumer();
        // 私有网络地址： http://{region}.mqadapter.cmq.tencentyun.com 支持腾讯云私有网络的云服务器内网访问
        // 公网地址：    https://cmq-{region}.public.tencenttdmq.com
        consumer.setNameServerAddress("http://****.com");
        // 设置SecretId，在控制台上获取，必须设置
        consumer.setSecretId("****");
        // 设置SecretKey，在控制台上获取，必须设置
        consumer.setSecretKey("****");
        // 设置签名方式，可以不设置，默认为SHA1
        consumer.setSignMethod(ClientConfig.SIGN_METHOD_SHA256);
        // 批量拉取时最大拉取消息数量，范围为1-16
        consumer.setBatchPullNumber(16);
        // 设置没有消息时等待时间，默认10s。可在consumer.receiveMsg等方法中传入具体的等待时间
        consumer.setPollingWaitSeconds(6);
        // 设置请求超时时间， 默认3000ms
        // 如果设置了没有消息时等待时间为6s，超时时间为5000ms，则最终超时时间为(6*1000+5000)ms
        consumer.setRequestTimeoutMS(5000);
        // 消息拉取的队列名称
        final String queue = "****";
```
	- NameServerAddress：API 调用地址，在[ TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **API请求地址**处复制。
![](https://main.qcloudimg.com/raw/bbc5dc77a8475304377d00cc92028e01.png)

	- SecretId、SecretKey：云API密钥，登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在**访问密钥** > **API密钥管理**页面复制。
		![](https://main.qcloudimg.com/raw/867837e2b1e6d347ecb04d7085938c08.png)
	- queue：填写队列名称。

2. 运行代码，查看消费端服务是否能正常运行无报错。

3. 通过 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq) 的**队列服务** > **发送消息**向消息接收侧发送测试消息，验证消费者服务是否可以正常消费。
   ![](https://main.qcloudimg.com/raw/1c2f1532860b51440bbf2a42285fb644.png)
如图则为正常消费：
   ![](https://main.qcloudimg.com/raw/959a9b688673054d7449913d71f89b4b.png)


### 步骤3：切换生产流

1. 将原生产者的 NameServer 修改为 TDMQ CMQ 版队列的接入地址，在 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq)的**队列服务** > **API请求地址**处复制。
2. 运行生产消息程序，验证生产者服务是否可以正常发送消息。
   ![](https://main.qcloudimg.com/raw/7c258f9b7cfd517f1bb6f735416c0f44.png)

### 步骤4：下线旧消费者

等待旧的消费者继续消费完原 CMQ 队列中的存量消息后，下线 CMQ 业务消费者。

在 [CMQ 控制台](https://console.cloud.tencent.com/cmq) 的**队列服务** > **队列** > **监控**页面可查看 CMQ 队列中堆积的消息数量，当堆积消息数量为0时，代表原 CMQ 队列中的存量消息已被消费完成。

![](https://main.qcloudimg.com/raw/30e7cd4d0a9ccad13a72a8d4c6bfe2e6.png)
