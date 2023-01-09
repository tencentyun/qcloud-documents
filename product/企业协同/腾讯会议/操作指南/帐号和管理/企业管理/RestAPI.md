## 添加应用
- 创建企业自建应用供企业内部使用，企业自建应用使用 JSON Web Token 鉴权方式。
- 企业自建应用分为企业级和应用级类型。
	- 企业级类型：企业级可以获取到您企业账户下的所有数据，包括通过腾讯会议 App、腾讯会议 API 接口等不同途径创建的用户数据，也可跨应用获取。
	- 应用级类型：应用级则仅能获取该应用所对应的相关数据，无法跨应用获取。

![](https://qcloudimg.tencent-cloud.cn/raw/0525c8607123bdd497ac37067c9a3de6.png)
- 应用创建完成后，您可以通过 AppID、SDKID、SecretKey、SecretID 进行鉴权，完成接口调用。详细鉴权方式请参见 [企业内部应用鉴权](https://cloud.tencent.com/document/product/1095/42413)。

## REST API 调试
给开发者提供调试工具，方便开发者开发。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/3d47919b12b01435d13d1d5d62717ca1.png" />

## 事件订阅
- 启用通知状态，单击**消息通知**后进行事件配置。
![](https://qcloudimg.tencent-cloud.cn/raw/a3c96b79843a3bcf32e09446a74659f5.png)
- 单击右上角**添加消息通知**，填写消息通知名称、接收消息通知的 URL 地址、选择需要订阅的事件类型，即可完成消息事件订阅。
![](https://qcloudimg.tencent-cloud.cn/raw/b42b23532b86913f60b5692750108088.png)

## 应用详情
单击操作栏**查看详情**可查看应用详情，包括接口调用明细和预定会议列表信息。
![](https://qcloudimg.tencent-cloud.cn/raw/715023c26af456d5314568b34d3dd5c4.png)
