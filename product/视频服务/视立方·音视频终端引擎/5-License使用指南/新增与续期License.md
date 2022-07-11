音视频终端 SDK（腾讯云视立方）包括**直播 License**、**短视频 License**、**视频播放 License**、**终端极速高清 License** 和**腾讯特效 License**，计费购买详情请参见 [腾讯云视立方价格总览](https://cloud.tencent.com/document/product/1449/56972)。购买后可在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 对各 License 进行新增和续期等操作，各 License 解锁相关功能模块如下：

- **直播 License** 用于解锁直播（直播推流 + 视频播放）功能模块的使用权限。
- **短视频 License** 用于解锁短视频（精简版/基础版）（短视频制作基础版 + 视频播放）功能模块的使用权限。
- **视频播放 License** 用于解锁视频播放功能模块的使用权限。
- **腾讯特效 License** 用于解锁腾讯特效 SDK 的使用权限。
- **终端极速高清 License** 用于解锁终端极速高清模块的使用权限。

> !
> - 目前终端极速高清功能模块处于体验期，仅提供测试版 License。
> - 10.1 版本起，直播 License 和短视频 License 包含了视频播放 License 全部能力，因此也可用于解锁播放器 SDK 的视频播放功能。
> - **更多授权解锁详情参见 [腾讯云视立方 License 授权说明](https://cloud.tencent.com/document/product/1449/74203)**。

音视频终端 SDK（腾讯云视立方）下的直播 License、短视频 License、视频播放 License 和终端极速高清 License 新增和续期等操作一致，**本文档将以直播 License 为例**，对四种 License 测试版和正式版的新增与续期等操作进行说明指引。腾讯特效 License 测试版和正式版的新增与续期等操作涉及审核授权，流程有所区别，详细操作指引请参见 [腾讯特效 License 授权使用说明](https://cloud.tencent.com/document/product/1449/56982)。

[](id:test)
## 测试版 License

[](id:creat_test)
### 申请测试版 License

您可以免费申请直播模块的测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。

>!试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
>- 当申请测试开始时间为  `2022-05-25 11:34:55` ，则14天后到期时间为  `2022-06-09 00:00:00` 。
>- 免费续期一次时，若在试用期14天内申请续期，则到期时间为  `2022-06-23 00:00:00` ；若在试用期14天结束后申请续期，申请续期的时间为  `2022-07-03 22:26:20` ，则续期的到期时间为  `2022-07-18 00:00:00` 。

申请测试模块时，您可以选择**新建测试 License 并申请测试功能模块**或在**已创建的测试应用中申请测试新功能模块**两种方式创建测试 License。
<dx-tabs>
::: 方式一：新建测试 License 并申请测试功能模块
1. 登录 [**腾讯云视立方控制台 > 终端 License 管理**](https://console.cloud.tencent.com/vcube)，单击**新建测试 License**。
![](https://qcloudimg.tencent-cloud.cn/raw/4d63d6f14f82ba1775083ed461c5f5db.png)
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块 **直播**（直播推流 + 视频播放），单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/1ff37a853c8dd26d05419af4f5340661.png)
2. 测试版 License 成功创建后，页面会显示生成的 License 信息。**在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。**
![](https://qcloudimg.tencent-cloud.cn/raw/709cf255601e5edd6913f7f8742cbfdd.png)
:::
::: 方法二：已创建的测试应用中申请测试新功能模块
若您想在已创建的测试应用中申请**直播**（直播推流 + 视频播放）功能测试模块，步骤如下：
1. 选择您想测试的应用，单击**测试新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/6be952eb22fdc3db08c931c250a84e9c.png)
2. 勾选功能模块 **直播**（直播推流 + 视频播放），单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/8466ae810b655bf2a704dc72bf715efb.png)
:::
</dx-tabs>

>? 
>- 测试版 License 有效期内可单击右侧的 **编辑**，进入修改 Bundle ID 和 Package Name 信息，单击 **确定** 即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。

[](id:renew_test)
### 续期测试版 License

测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**，单击功能模块 **直播** 右侧的 **续期**，选择 **确定续期** 即可续期该功能模块14天。
![](https://qcloudimg.tencent-cloud.cn/raw/8f50c61fa468eece765a0b626862c550.png)

>? 测试版 License 有效期共28天，**只能续期一次**。若您需继续使用，请购买 [正式版 License](#formal)。

[](id:up_test)
### 升级测试版 License
若您需要将直播功能模块的测试版 License 升级成为正式版 License，获得一年的有效期使用期。具体操作如下：
1. 单击测试版 License 直播功能模块中的 **升级**。
![](https://qcloudimg.tencent-cloud.cn/raw/62b7e523abde11a3155390b9e7a02ccb.png)
2. 进入升级功能模块界面，点击**立即绑定** ，选择需要绑定的云直播流量资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），单击 **确定** 即可升级到直播功能模块的正式版 License。
![image](https://qcloudimg.tencent-cloud.cn/raw/fe1174806fad4fd4234a23483efe226b.png)

[](id:formal)
## 正式版 License
[](id:creat_formal)
### 购买正式版 License
1. 购买方式：
    - [**购买**](https://buy.cloud.tencent.com/vcube) 指定规格的 [直播流量资源包](https://cloud.tencent.com/document/product/1449/56973#live)，获得赠送1年有效期的正式直播 License 使用权限（自资源包购买之日起计算，授权有效期至到期次日00:00:00为止）。
    - [**购买**](https://buy.cloud.tencent.com/vcube) 独立 [直播 License](https://cloud.tencent.com/document/product/1449/56973#live) 获得使用授权（自绑定包名之日起计算，授权有效期为1年后到期次日00:00:00止）。
2. 绑定直播正式版 License。您可以选择**新建正式应用并绑定 License**或在**已创建的应用上解锁直播正式版模块并绑定 License**两种方式进行正式版 License 绑定 。
<dx-tabs>
::: 方式一：新建正式应用并绑定 License
1. 进入 [**腾讯云视立方控制台 > 终端 License 管理**](https://console.cloud.tencent.com/vcube)，单击**新建正式 License**。
![](https://qcloudimg.tencent-cloud.cn/raw/7d7b23dd672ea2c877eab6beb112ea47.png)
2. 填写正式应用的 `App Name`、`Package Name` 和 `Bundle ID` 信息，勾选功能模块**直播**（直播推流 + 视频播放），单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/95aaa471d8cd2480337773b2cd5fb9c5.png)
3. 进入选择资源项并绑定 License 界面，点击**立即绑定** ，选择**未绑定**的直播流量资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），并单击**确定**即可创建应用并生成正式版 License。
![](https://qcloudimg.tencent-cloud.cn/raw/b9ad160f8087363ce859d0477cc037e5.png)
> ?
> - 单击**确定**前需要再次确认 Bundle ID 和 Package Name 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。
> - **选择直播流量包仅用于直播正式版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播流量消耗。**
4. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://qcloudimg.tencent-cloud.cn/raw/63913fd86dd99417ffc3238d984de097.png)
:::
::: 方式二：已创建的正式版应用中解锁模块
1. 选择您需要增加**直播**（直播推流 + 视频播放）功能模块的正式应用，单击**解锁新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/b536ec77d54bd53f9761cb115ebd4b20.png)
2. 选择**直播**（直播推流 + 视频播放），单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/39ab8543abac18c47347566498c2ba7a.png)
3. 进入选择资源项并绑定 License 界面，点击**立即绑定** ，选择**未绑定**的直播流量资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），并单击**确定**即可在应用下生成正式版直播功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/cb9233eac721a33fd0f79e05efca7c4a.png)
:::
</dx-tabs>

[](id:update_formal)
### 更新正式版 License 有效期
您可以登录 [**腾讯云视立方控制台 > 终端 License 管理**](https://console.cloud.tencent.com/vcube) 页面查看直播正式版 License 的有效期，也可通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端 SDK，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。直播正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。若您的直播推流正式版 License 已到期，可进行如下操作进行续期：

1. 选择您需要更新有效期的 License，单击直播功能模块内的 **更新有效期**。
![](https://qcloudimg.tencent-cloud.cn/raw/5f15eea68cf79b9b3078c47bc21991d3.png)
2. 单击**立即绑定** ，选择**未绑定**的直播流量资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/449c863a94e21e9a0f099991b42d745a.png)
3. 查看更新后的有效期情况。

>! **直播正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **新增 License** 重新新增 License 绑定新的包名信息。
