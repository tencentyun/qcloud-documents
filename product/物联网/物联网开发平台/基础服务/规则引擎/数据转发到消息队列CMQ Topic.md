
## 概述
规则引擎支持用户配置规则将符合条件的设备上报数据转发到消息队列 CMQ Topic，您可以使用云 API 订阅 CMQ Topic 后，即可接收到来自 CMQ Topic 的消息推送。 CMQ Topic 的消息推送机制为用户提供了高可靠的异步接收消息的能力。

下图展示了规则引擎将数据转发给 CMQ Topic 的整个过程：
![](https://main.qcloudimg.com/raw/17177d50749d2f18c4b2f740f9f92229.png)


## 配置
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，单击左侧菜单**规则引擎**。
2. 进入规则引擎页面，单击需要配置的规则。
3. 在规则详情页面，单击**添加行为操作**。
>?第一次使用时会提示用户授权访问 CMQ Topic，您需单击**立即授权**才能继续创建。
![image](https://main.qcloudimg.com/raw/ba7c122334eb5be38425ed166a515387.png)
4. 在弹出的“添加规则”窗口，选择“数据转发到消息队列（CMQ-Topic）选项”、地域和 Topic，单击**保存**即可。
![](https://main.qcloudimg.com/raw/bc96f06c7ada505504efed8beb9c2666.png)

## 重发机制

重发机制用于在消息转发过程中发生失败的情况下，进行再次重发以达到接受消息的目的，具体说明如下：
- 若消息转发失败，系统则会进行转发重试，重试按照1s、3s、10s的时间间隔依次进行，若三次重试均失败，则将消息丢弃掉。
- 若用户配置了“转发错误行为操作”，在三次重试失败后，将按“转发错误行为操作”的配置，再进行一次消息转发，如果仍失败，则将消息丢弃掉。


## 示例
使用云 API 创建 CMQ Topic 订阅，更多详情请参见 [使用示例](https://cloud.tencent.com/document/api/406/5853)。

