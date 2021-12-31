移动直播 SDK 推荐配合腾讯云直播服务使用，购买指定直播流量资源包，即送直播推流 License（原移动直播基础版 License）1年使用权限，资源包与 SDK License 版本对应关系请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。

[](id:test)

## 测试版 License
[](id:creat_test)

### 申请测试版 License
您可以免费申请直播推流测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。

> !试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
> - 当申请测试开始时间为 `2021-08-12 10:28:41`，则14天后到期时间为 `2021-08-26 10:28:41`。
> - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2021-09-09 10:28:41`；若在试用期14天结束后申请续期，申请续期的时间为 `2021-08-30 22:26:20`，则续期的到期时间为 `2021-09-13 22:26:20`。

具体步骤如下：

1. 登录云直播控制台，在左侧菜单中选择  **直播 SDK** >[ **License管理** ](https://console.cloud.tencent.com/live/license)，单击 **创建测试License** 。
![](https://main.qcloudimg.com/raw/a623b59b4989ef4d713fc5a2e13927c1.png)
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块 **直播推流**，单击 **确定**。
![](https://main.qcloudimg.com/raw/b471d5f1b85b292de034fde0a5b6650f.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/53635bb1119911b9a17bea79ab327283.png)

>? 
>- 测试版 License 有效期内可单击右侧的 **编辑**，进入修改 Bundle ID 和 Package Name 信息，单击 **确定** 即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。

[](id:renew_test)
### 续期测试版 License
测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**，单击功能模块 **直播推流** 右侧的 **续期**，选择 **确定续期** 即可续期该功能模块14天。
![](https://main.qcloudimg.com/raw/491ac2dd3ce48e54c7530e8be7575a5d.png)

> ? 测试版 License 有效期共28天，**只能续期一次**。若您需继续使用，请购买 [正式版 License](#formal)。

### 测试版 License 升级

若您需要将直播推流测试版 License 升级成为正式版 License，获得一年的有效期使用期。具体操作如下：
1. 单击测试版 License 直播推流模块中的 **升级**。
![](https://main.qcloudimg.com/raw/71c0043f58745eabbd8d8c9203d99244.png)
2. 进入升级功能模块界面，选择需要绑定的云直播流量资源包，单击 **确定** 即可升级到直播推流正式版 License（原移动直播基础版 License）。
![](https://main.qcloudimg.com/raw/636f1237e64229e05308475861ce70eb.png)

[](id:formal)
## 正式版 License
[](id:creat_formal)

### 购买正式版 License
1. 购买指定规格的 [直播流量包](https://buy.cloud.tencent.com/vcube?sdk-version=2&function-module=LIVE)，获得赠送1年有效期的正式直播推流 License（原移动直播基础版 License）使用权限（有效期至到期次日的00:00:00止），具体价格请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。
2. 进入  **直播 SDK**>**[License 管理](https://console.cloud.tencent.com/live/license)**，单击 **创建应用并绑定 License** 按钮。填写 `App Name`、`Package Name` 和 `Bundle ID` 并勾选功能模块 **直播推流**，完成后单击 **下一步**。
![](https://main.qcloudimg.com/raw/cc803e51118a8c33e9f29405a58ed210.png)
>?
> - 单击 **确定** 前需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请提前进行修改，**一旦提交成功将无法再修改 License 信息**。
> - **正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于续期 License，请单击 **新增 License** 重新新增 License 绑定新的包名信息。
3. 进入选择套餐包并绑定 License 界面，选择**未绑定**的直播流量资源包，并单击 **确定** 即可生成正式版 License。
![](https://main.qcloudimg.com/raw/6a62f95943713c1a8a36779315d84194.png)
>! 
>**选择直播流量包仅用于直播推流 License（原移动直播基础版 License）绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播流量消耗。**
	例如，您的标准直播服务是日结流量计费，在2021年08月01日 15:50:24购买了10TB的直播流量包，为直播 App 创建了直播推流 License A；在2021年09月01日 09：23:44购买了50TB的直播流量包，为另一个直播 App 创建了直播推流 License B。
	则 A 和 B 可共用60TB的流量，其中10TB流量包于2022年08月01日 15:50:24到期，License A 都在2022年08月02日00:00:00到期；50TB流量包于2022年09月01日 09：23:44到期，License B 都在2022年09月02日00:00:00到期。
4. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/3335b76fb8558a3f967149c20bf73b90.png)


[](id:update_formal)
### 更新正式版 License 有效期
您可以登录  **直播 SDK**>**[License 管理](https://console.cloud.tencent.com/live/license)** 页面查看直播推流正式版 License（原直播基础版 License）的有效期，也可通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端引擎，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。直播推流正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。若您的直播推流正式版 License 已到期，可进行如下操作进行续期：
1. 购买指定规格的 [直播流量包](https://buy.cloud.tencent.com/vcube?sdk-version=2&function-module=LIVE)，赠送1年有效期的正式直播推流 License（原直播基础版 License）使用权限，具体价格请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。
2. 选择您需要更新有效期的 License，单击直播推流模块内的 **更新有效期**。
![](https://main.qcloudimg.com/raw/72e03f5ff392eac9e6d82cb20dcbf79d.png)
3. 选择**未绑定**的直播流量资源包（若没有可绑定的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube) 购买），单击 **确定** 即可。
![](https://main.qcloudimg.com/raw/627e142976b084212c8d9df060578b37.png)
4. 查看更新后的有效期情况。
>! **直播推流正式版 License（原移动直播基础版 License）不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **新增 License** 重新新增 License 绑定新的包名信息。

## 企业版 License

相比于全功能版，企业版增加了基于腾讯优图实验室专利技术的人脸特效功能。使用企业版 License 可以开启优图实验室的 AI 功能，具体详情请参见 [美颜特效](https://cloud.tencent.com/product/x-magic)。
