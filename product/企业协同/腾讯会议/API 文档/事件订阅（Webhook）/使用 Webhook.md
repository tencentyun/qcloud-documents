
购买腾讯会议企业版或者商业版后，腾讯会议将自动开通企业 API 接入能力和消息事件订阅能力，您可以通过以下步骤进行配置：
1. 企业管理员可登录 [腾讯会议官网](https://meeting.tencent.com/)。
2. 单击页面右上角**用户中心**。
3. 选择左侧菜单栏中的**高级 > restApi**。
4. 单击**添加应用**添加新应用，或在应用列表中找到需要开启通知的应用。确保该应用的**应用状态**处于“启用中”后，单击最右侧的**消息通知**。
5. 在弹出的窗口中，单击**添加消息通知**进行事件订阅配置。
6. 使用 OAuth 鉴权用户请参见 [事件订阅配置介绍](https://cloud.tencent.com/document/product/1095/58770#event)。

>! 
>1. 只有企业管理员才有设置权限。
>2. 设置**消息通知**的前提是已添加应用且该应用处于“启用中”状态。

![](https://main.qcloudimg.com/raw/c7b07aacd5d8573de2dea671eb915791.png)


## 配置回调服务
配置回调服务需要三个配置项，分别是：URL、TOKEN、EVENT_TYPE，具体内容如下：

### URL 配置项
URL 是由企业开发者搭建的回调服务地址。
>! 回调服务需满足接口要求，详情请参见 [企业回调服务介绍](https://cloud.tencent.com/document/product/1095/51608)。

### TOKEN 配置项
Token 用于计算签名，由英文或数字组成且长度为25位的字符串；由于企业开发者提供的 URL 公开可访问，掌握该 URL 的信息即可向该链接推送消息，因此 URL 服务需要解决以下两个问题：
1. 如何分辨出回调消息是否为腾讯会议来源。
2. 如何分辨出回调消息的内容是否被篡改。

**解决方法**
通过数字签名可以解决上述问题，具体方式为：约定 Token 作为签名密钥，仅限企业开发者和腾讯会议可查看，且在传输中不可见，以此用于签名的计算。腾讯会议在推送消息时，将消息内容与 Token 计算出签名。企业开发者在接收到回调消息时，也按相同的算法计算出签名，如果签名一致，则可信任来源为腾讯会议，并且内容不被篡改。
- 如果非腾讯会议的回调，由于攻击者未提供正确的 Token，则无法计算出正确的签名；
- 如果消息内容被篡改，由于开发者将接收到的回调消息内容与 Token 重算一次签名，该值与回调参数的签名不一致，则拒绝该请求。


### 会议事件类型配置项

会议事件类型（EVENT_TYPE）是该回调服务所对应的事件，目前事件仅支持会议相关事件（后续将补齐其他类型的事件通知），其中包括以下几种类型：

| 会议事件类型             | 事件名                                  |
| ------------------------ | --------------------------------------- |
| 会议创建                 | meeting.created                         |
| 会议更新                 | meeting.updated                         |
| 会议取消                 | meeting.canceled                        |
| 会议开始                 | meeting.started                         |
| 会议结束                 | meeting.end                             |
| 用户入会                 | meeting.participant-joined              |
| 用户离会                 | meeting.participant-left                |
| 用户等待主持人入会       | meeting.participant-jbh-waiting         |
| 用户进入等候室           | meeting.participant-joined-waiting-room |
| 用户离开等候室           | meeting.participant-left-waiting-room   |
| 用户从等候室进入会议     | meeting.participant-admitted            |
| 用户从会议中被移入等候室 | meeting.participant-put-in-waiting-room |
