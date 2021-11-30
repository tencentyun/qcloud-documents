## 概述
规则引擎支持用户配置规则将符合条件的设备上报数据转发到 [消息队列 CKAFKA](https://cloud.tencent.com/product/CKafka) （以下简称 CKAFKA ），用户的应用服务器再从 CKAFKA 中读取数据内容进行处理。以此利用 CKAFKA 高吞吐量的优势，为用户打造高可用性的消息链路。  

下图展示了规则引擎将数据转发给 CKAFKA 的整个过程：
![](https://main.qcloudimg.com/raw/dead88cb3fe3a5c986b6522565967193.png)

## 配置
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，单击左侧菜单**规则引擎**。
2. 进入规则引擎页面，单击需要配置的规则。
3. 在规则详情页面，单击**添加行为操作**。
>?第一次使用时会提示用户授权访问 CKAFKA，您需单击**授权访问 CKAFKA**才能继续创建。
![](https://main.qcloudimg.com/raw/d4a20c9118f9989dba7064d13a4e836e.png)
4. 在弹出的“添加规则”窗口，选择行为“数据转发到消息队列（CKAFKA）”；依次选择 CKAFKA 实例和 Topic，单击**保存**即可。
![avatar](https://main.qcloudimg.com/raw/b2f2b7e9da1d69b98762e28718afbd14.png) 
5. 完成以上配置后，物联网开发平台会将符合规则条件的设备上报数据转发至用户配置的 CKAFKA 。您可以参考 [创建实例和 Topic](https://cloud.tencent.com/document/product/597/30931) 文档，在应用服务器上读取数据并进行处理。



## 重发机制

重发机制用于在消息转发过程中发生失败的情况下，进行再次重发以达到接受消息的目的，具体说明如下：
- 若消息转发失败，系统则会进行转发重试，重试按照1s、3s、10s的时间间隔依次进行，若三次重试均失败，则将消息丢弃掉。
- 若用户配置了“转发错误行为操作”，在三次重试失败后，将按“转发错误行为操作”的配置，再进行一次消息转发，如果仍失败，则将消息丢弃掉。
