短视频 SDK 推荐配合腾讯云点播服务使用，购买指定点播流量资源包，即赠送短视频 License 1年使用权限，资源包与 SDK License 版本对应关系请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。

[](id:test)
## 测试版 License

[](id:create_formal)
### 申请测试版 License

您可以免费申请短视频**基础版**模块的测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。

>!试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
>- 当申请测试开始时间为  `2021-08-12 10:28:41` ，则14天后到期时间为  `2021-08-26 10:28:41` 。
>- 免费续期一次时，若在试用期14天内申请续期，则到期时间为  `2021-09-09 10:28:41` ；若在试用期14天结束后申请续期，申请续期的时间为  `2021-08-30 22:26:20` ，则续期的到期时间为  `2021-09-13 22:26:20` 。

申请测试模块时，您可以选择**新建测试 License 并申请测试模块**或在**已创建的测试应用中申请测试模块**两种方式创建测试 License。
<dx-tabs>
::: 方式一：新建测试 License 并申请测试模块
1. 登录 [**云点播控制台**](https://console.cloud.tencent.com/vod/overview)，在左侧菜单中选择 [ **License 管理**](https://console.cloud.tencent.com/live/license) > **[SDK License](https://console.cloud.tencent.com/vod/license/video)**，单击**创建测试 License**。
![](https://qcloudimg.tencent-cloud.cn/raw/1defdf99f755e854f2ca636ad7a1bb7d.png)
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块 **短视频（基础版）**，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/2502ce5a06fb95a86563295c4b5251a1.png)
3.测试版 License 成功创建后，页面会显示生成的 License 信息。**在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。** ![](https://qcloudimg.tencent-cloud.cn/raw/519f9f3fb2015af411b956280c787f00.png)
:::
::: 方法二：已创建的测试应用中申请测试模块
若您想在已创建的测试应用中申请短视频（基础版）功能测试模块，步骤如下：
1. 选择您想测试的应用，单击**测试新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/9b7703988c5a3aba2036f9af898f86b0.png)
2. 勾选功能模块 **短视频（基础版）**，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/c63e0d7cb1d9daf033288a2b0292adc8.png)
:::
</dx-tabs>

>? 
>- 测试版 License 有效期内可单击右侧的 **编辑**，进入修改 Bundle ID 和 Package Name 信息，单击 **确定** 即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。

[](id:renewal_formal)
### 续期测试版 License

测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**，单击功能模块 **短视频** 右侧的 **续期**，选择 **确定续期** 即可续期该功能模块14天。
![](https://qcloudimg.tencent-cloud.cn/raw/2e20f1e6c7436555f617794b8807351f.png)

>? 测试版 License 有效期共28天，**只能续期一次**。若您需继续使用，请购买 [正式版 License](#formal)。

[](id:upgrate_formal)
### 测试版 License 升级
若您需要将直播推流模块的测试版 License 升级成为正式版 License，获得一年的有效期使用期。具体操作如下：
1. 单击测试版 License 直播推流模块中的 **升级**。
![](https://qcloudimg.tencent-cloud.cn/raw/42988885dbf0ab7a9d356e9629cdedc5.png)
2. 进入升级功能模块界面，选择需要绑定的云直播流量资源包，单击 **确定** 即可升级到直播推流模块的正式版 License。
![](https://main.qcloudimg.com/raw/50183054e3d1ff5a0f74a80b2bc279aa.png)

>!
>- 短视频测试版 License 升级为**短视频精简版**的正式版 License 仅支持选择 10TB 规格的云点播流量资源包。
>- 短视频测试版 License 升级为**短视频基础版**的正式版 License 可选择 50TB、200TB、1PB 规格的云点播流量资源包。

[](id:formal)
## 正式版 License

[](id:create_formal)
### 购买正式版 License
1. 购买指定规格的 [云点播流量资源包](https://cloud.tencent.com/document/product/1449/56973#video)，获得赠送1年有效期的正式短视频（精简版/基础版）License 使用权限（有效期至到期次日00:00:00为止）。
<table>
<thead>
<tr>
<th>License 版本</th>
<th>资源包</th>
</tr>
</thead>
<tbody><tr>
<td>短视频精简版 License</td>
<td>云点播流量资源包 10TB</td>
</tr>
<tr>
<td>短视频基础版 License</td>
<td>云点播流量资源包 50TB、200TB、1PB</td>
</tr>
</tbody></table>
2. 绑定直播推流正式版 License。您可以选择**新建应用并绑定 License**或在**已创建的应用上解锁直播推流正式版模块并绑定 License**两种方式进行正式版 License 绑定 。
<dx-tabs>
::: 方式一：新建正式应用并绑定 License
1. 登录 [云点播控制台](https://console.cloud.tencent.com/vod)，在左侧菜单中选择 [ **License 管理**](https://console.cloud.tencent.com/live/license) > **[SDK License](https://console.cloud.tencent.com/vod/license/video)**，单击**创建应用并绑定 License**。
2. 填写正式应用的 `App Name`、`Package Name` 和 `Bundle ID` 信息，勾选功能模块**短视频**，选择**基础版**或**精简版**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/e84acce0a53e6f4f69cb2fcfb8a58630.png)
3. 进入选择资源项并绑定 License 界面，选择**未绑定**的点播流量资源包（若没有可绑定的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube?sdk-version=3&function-module=SHORT_VIDEO) 购买），并单击**确定**即可创建应用并生成正式版 License。
![](https://main.qcloudimg.com/raw/6b0a059af1b106a1e876dc53edabd2b0.png)
> ?
> - 单击**确定**前需要再次确认 Bundle ID 和 Package Name 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。
> - 各规格资源包均有对应的 SDK License 版本，具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
> - **选择点播流量包仅用于短视频正式版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 点播流量消耗。**
4. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/c46b3a484dbcc8070d9c2d5d728953db.png)
:::
::: 方式二：已创建的正式版应用中解锁模块
1. 选择您需要增加短视频功能模块的正式应用，单击**解锁新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/75889ec1a3a37c14c222d7f89df75622.png)
2. 选择**短视频**，单击**下一步**。
![](https://main.qcloudimg.com/raw/cc803e51118a8c33e9f29405a58ed210.png)
3. 进入选择资源项并绑定 License 界面，选择**未绑定**的点播流量资源包（若无可绑定的点播流量资源包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube) 前往购买），并单击**确定**即可在应用下生成正式版短视频功能模块。
![](https://main.qcloudimg.com/raw/6a62f95943713c1a8a36779315d84194.png)
:::
</dx-tabs>

[](id:update_formal)
### 更新正式版 License 有效期
您可以登录 **[云点播控制台](https://console.cloud.tencent.com/vod)**，在左侧菜单中选择 [ **License 管理**](https://console.cloud.tencent.com/live/license) > **[SDK License](https://console.cloud.tencent.com/vod/license/video)**，查看短视频正式版 License 的有效期，也可通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端 SDK，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。短视频正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。若您的短视频正式版 License 已到期，可进行如下操作进行续期：

1. 选择您需要更新有效期的 License，单击短视频模块内的 **更新有效期**。
![image](https://main.qcloudimg.com/raw/a0e9a956644566f69a0b8d5293cdbf8e.png)
2. 选择**未绑定**过的短视频资源包（若没有可绑定的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube?sdk-version=3&function-module=SHORT_VIDEO) 购买），单击 **确定** 即可。
![image](https://main.qcloudimg.com/raw/627e142976b084212c8d9df060578b37.png)
3. 查看更新后的有效期情况。

>! **短视频正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **新增 License** 重新新增 License 绑定新的包名信息。


[](id:upgrate_formal)
### 升级正式版 License
若您已经具备短视频精简版的正式版 License，且需要变速录制、背景音乐、滤镜特效等更强大的能力，您可以通过以下方式升级为短视频基础版的正式版 License，解锁更多功能：

1. 选择需要升级的正式版 License，单击短视频模块内的 **升级**。
![](https://main.qcloudimg.com/raw/7b9766f087097b02baf66d3e47385caa.png)
2. 进入升级功能模块界面，选择需要绑定的云点播流量资源包（规格需可选择为 50TB / 200TB/1PB），单击 **确定** 即可升级到短视频基础版的正式版 License。
![](https://main.qcloudimg.com/raw/48aa2580a6ab0e25a20e986b183ab189.png)

>! **短视频精简版正式版 License** 成功升级为**短视频基础版正式版 License** 后，原有绑定短视频精简版的套餐包（规格为 10TB 的云点播流量资源包）会进行释放，即结束绑定关系，此套餐包可重新绑定其他应用内的短视频 License。
