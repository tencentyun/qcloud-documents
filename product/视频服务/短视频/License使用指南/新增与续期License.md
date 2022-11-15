短视频 SDK 推荐配合腾讯云点播服务使用，购买指定点播流量资源包即赠送短视频 License 1年使用权限，或购买独立短视频 License 获得授权。计费购买详情请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。

购买后可在 [云点播控制台](https://console.cloud.tencent.com/vod/license/video) 对短视频 License 进行新增和续期等操作。本文档将对短视频 License 正式版的新增与续期等操作进行说明指引。

短视频 SDK 提供测试版 License，您可通过**免费申请**短视频 SDK 测试版 License 使用授权来体验**短视频制作**功能模块，详情请参见 [免费测试](https://cloud.tencent.com/document/product/584/78929)。

> !购买短视频 License 授权可解锁**短视频制作 + 视频播放**功能模块。10.1 版本起，若您仅使用 SDK 中视频播放功能，也可购买 [视频播放 License](https://cloud.tencent.com/document/product/881/20193#.E8.AE.A1.E8.B4.B9.E4.BB.B7.E6.A0.BC)  授权解锁**视频播放**功能模块，操作指引参见 [视频播放 License](https://cloud.tencent.com/document/product/881/74588#.E6.B5.8B.E8.AF.95.E7.89.88-license)。

[](id:create_formal)

## 购买并新建正式版 License
1. 购买方式：
	- [**购买**](https://buy.cloud.tencent.com/vcube) 指定规格的  [云点播流量资源包](https://cloud.tencent.com/document/product/1449/56973#video)，获得赠送1年有效期的正式短视频（精简版/基础版） License 使用权限（自资源包购买之日起计算，授权有效期至到期次日00:00:00为止）。
	- [**购买**](https://buy.cloud.tencent.com/vcube) 独立 [短视频 License](https://cloud.tencent.com/document/product/1449/56973#video) 获得使用授权（自绑定包名之日起计算，授权有效期为1年后到期次日00:00:00止）。
<table>
<thead>
<tr>
<th>License 版本</th>
<th>购买方式</th>
</tr>
</thead>
<tbody><tr>
<td rowspan=2>短视频精简版 License</td>
<td>云点播流量资源包 10TB</td>
</tr>
<tr>
<td>独立精简版 License</td>
</tr>
<tr>
<td rowspan=2>短视频基础版 License</td>
<td>云点播流量资源包 50TB、200TB、1PB</td>
</tr>
<tr>
<td>独立基础版 License</td>
</tr>
</tbody></table>
2. 绑定短视频正式版 License。您可以选择**新建正式应用并绑定 License**或在**已创建的应用上解锁短视频正式版模块并绑定 License**两种方式进行正式版 License 绑定 。
<dx-tabs>
::: 方式一：新建正式应用并绑定 License
1. 登录 [云点播控制台](https://console.cloud.tencent.com/vod)，在左侧菜单中选择  **License 管理** > **[SDK License](https://console.cloud.tencent.com/vod/license/video)**，单击**新建正式 License**。
![](https://qcloudimg.tencent-cloud.cn/raw/7d7b23dd672ea2c877eab6beb112ea47.png)
2. 填写正式应用的 `App Name`、`Package Name` 和 `Bundle ID` 信息，勾选功能模块**短视频**（短视频制作基础版 + 视频播放），选择**精简版**或**基础版**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/352fc93095618009e52804d723630373.png)
3. 进入选择资源项并绑定 License 界面，点击**立即绑定** ，选择**未绑定**的点播流量资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），并单击**确定**即可创建应用并生成正式版 License。
![](https://qcloudimg.tencent-cloud.cn/raw/40f2e0e41cf140424a46fd744129af60.png)
> ?
> - 单击**确定**前需要再次确认 Bundle ID 和 Package Name 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。
> - 各规格资源包均有对应的 SDK License 版本，具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
> - **选择点播流量包仅用于短视频正式版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 点播流量消耗。**
4. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://qcloudimg.tencent-cloud.cn/raw/dfa5d56f0e98584272eeb91975ae6bc7.png)
:::
::: 方式二：已创建的正式版应用中解锁模块
1. 选择您需要增加短视频（短视频制作基础版 + 视频播放）功能模块的正式应用，单击**解锁新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/b536ec77d54bd53f9761cb115ebd4b20.png)
2. 选择**短视频精简版或基础版**（短视频制作基础版 + 视频播放），单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/0a746a1f456b1664244b80a95dde9d1a.png)
3. 进入选择资源项并绑定 License 界面，点击**立即绑定** ，选择**未绑定**的点播流量资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），并单击**确定**即可在应用下生成正式版短视频功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/5fe00ab6ce271c6e58e2d367d9e7eea2.png)
:::
</dx-tabs>

[](id:update_formal)
## 更新正式版 License 有效期
您可以登录  **License 管理** > **[SDK License](https://console.cloud.tencent.com/vod/license/video)** 页面查看短视频正式版 License 的有效期，也可通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端 SDK，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。短视频正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。若您的短视频正式版 License 已到期，可进行如下操作进行续期：

1. 选择您需要更新有效期的 License，单击短视频模块内的 **更新有效期**。
![](https://qcloudimg.tencent-cloud.cn/raw/97d5ed0f8757c2a9b4d0d2592cae0c9b.png)
2. 单击**立即绑定** ，选择**未绑定**的短视频资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/70eab637b221fc5861b8b712276b67bf.png)
3. 查看更新后的有效期情况。

>! **短视频正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **新增 License** 重新新增 License 绑定新的包名信息。


[](id:upgrate_formal)
## 升级正式版 License
若您已经具备短视频**精简版**的正式版 License，且需要变速录制、背景音乐、滤镜特效等更强大的能力，您可以通过以下方式升级为短视频基础版的正式版 License，解锁更多功能：
1. 选择需要升级的正式**精简版** License，单击短视频功能模块内的 **升级**。
![](https://qcloudimg.tencent-cloud.cn/raw/e4a50084b13d1da84d88d0063637f31c.png)
2. 进入升级功能模块界面，点击**立即绑定** ，选择需要绑定的云点播流量资源包（规格需可选择为 50TB / 200TB/1PB）或独立基础版 License，单击**确定**即可升级到短视频基础版的正式版 License。
![](https://qcloudimg.tencent-cloud.cn/raw/ad2e3e96c7ec295e754bd4734e880b85.png)

>! **短视频精简版正式版 License** 成功升级为**短视频基础版正式版 License** 后，原有绑定短视频精简版的套餐包（规格为 10TB 的云点播流量资源包）会进行释放，即结束绑定关系，此套餐包可重新绑定其他应用内的短视频 License。
