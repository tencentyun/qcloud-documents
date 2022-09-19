播放器 SDK 提供直播播放和点播播放能力，购买指定直播/点播流量资源包即赠送视频播放 License 1年使用权限，或购买独立视频播放 License 获得授权。

购买后需在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 对各 License 进行新增和续期等操作。本文档将对**计费购买**和**视频播放 License 正式版的新增与续期**等操作进行说明指引。

播放器 SDK 提供测试版 License，**测试版 License 包括视频播放 License 和终端极速高清 License**。

- 您可通过**免费申请**视频播放测试版 License 使用授权来体验**视频播放**功能模块，详情请参见 [免费测试](https://cloud.tencent.com/document/product/881/79169)；
- 也可**免费申请**终端极速高清测试版 License 使用授权来体验**终端极速高清**功能模块，其免费申请和续期操作请参见 [终端极速高清 License](https://cloud.tencent.com/document/product/881/72422)。目前终端极速高清功能模块处于体验期，仅提供测试版 License。

>!10.1 版本起，直播 License 和短视频 License 包含了视频播放 License 全部能力，因此也可用于解锁播放器 SDK 的视频播放功能。直播 License 相关参见[ License 计费购买](https://cloud.tencent.com/document/product/454/8008#sdklicense) 和 [新增与续期](https://cloud.tencent.com/document/product/454/34750)，短视频 License 相关参见 [License 计费购买](https://cloud.tencent.com/document/product/584/9368) 和 [新增与续期](https://cloud.tencent.com/document/product/584/54333)。

## 购买并新建正式版 License

### 购买视频播放 License

您可参考以下视频播放 License 获取方式进行购买：

<table>
<thead>
<tr>
<th><strong>License类型</strong></th>
<th><strong>有效期</strong></th>
<th><strong>获取方式</strong></th>
<th><strong>资源包规格</strong></th>
<th><strong>价格（元/年）</strong></th>
</tr>
</thead>
<tbody><tr>
<td rowspan=3>视频播放 License 正式版</td>
<td>1年（自绑定包名起算）</td>
<td><a href="https://buy.cloud.tencent.com/vcube?type=player&amp;pkg-type=lic">直接购买</a></td>
<td>无</td>
<td>12</td>
</tr>
<tr>
<td rowspan=2>1年（自购买资源包起算）</td>
<td><a href="https://buy.cloud.tencent.com/vcube?type=live&amp;pkg-type=100GB">购买云直播资源包免费赠送</a></td>
<td>100GB/500GB/1TB /5TB 直播流量资源包均可免费赠送视频播放 License</td>
<td>26/128/248/1200</td>
</tr>
<tr>
<td><a href="https://buy.cloud.tencent.com/vcube?type=video&amp;pkg-type=100GB">购买云点播资源包免费赠送</a></td>
<td>100GB/500GB/1TB/5TB 点播流量资源包均可免费赠送视频播放 License</td>
<td>19/88/175/869</td>
</tr>
</tbody></table>

### 绑定视频播放正式版 License

购买后，您需要在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 对应用进行 License 绑定使其生效。您可以选择**新建正式应用并绑定 License**或在**已创建的应用上解锁视频播放正式版模块并绑定 License**两种方式进行正式版 License 绑定 。
<dx-tabs>
::: 方式一：新建正式应用并绑定 License

1. 进入 [**腾讯云视立方控制台 > 终端 License 管理**](https://console.cloud.tencent.com/vcube)，单击**新建正式 License**。
![](https://qcloudimg.tencent-cloud.cn/raw/7d7b23dd672ea2c877eab6beb112ea47.png)
2. 填写正式应用的 `App Name`、`Package Name` 和 `Bundle ID` 信息，勾选功能模块**视频播放**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/71c662c0faf0e4255e1da3bc1f01a8ff.png)
3. 进入选择资源项并绑定 License 界面，点击**立即绑定** ，选择**未绑定**的直播/点播流量资源包或独立 License（若没有可绑定的 License 资源，可参考 [购买视频播放 License](https://tcloud-doc.isd.com/document/product/881/74588?!editLang=zh&!preview#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E6.96.B0.E5.BB.BA.E6.AD.A3.E5.BC.8F.E7.89.88-license))，并单击**确定**即可创建应用并生成正式版 License。
![](https://qcloudimg.tencent-cloud.cn/raw/259253529372b59a45bb751aa507d9bf.png)

> ?
>- 单击**确定**前需要再次确认 Bundle ID 和 Package Name 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。
>- **选择直播/点播流量包仅用于视频播放 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播/点播流量消耗。**
4. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。**参考 [配置查看 License](https://cloud.tencent.com/document/product/881/77526) 在 SDK 内传入您的 License URL 和 License Key 即可完成 License 授权。**
![](https://qcloudimg.tencent-cloud.cn/raw/6b69aaa6565e65ad5843fdf363dcf47b.png)
:::
::: 方式二：已创建的正式版应用中解锁模块
1. 选择您需要增加视频播放功能模块的正式应用，单击**解锁新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/b536ec77d54bd53f9761cb115ebd4b20.png)
2. 选择**视频播放**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/46e2161b443c62b0bd9c56a513cbb9ab.png)
3. 进入选择资源项并绑定 License 界面，点击**立即绑定** ，选择**未绑定**的视频播放 License（若没有可绑定的 License 资源，可参考 [购买视频播放 License](https://tcloud-doc.isd.com/document/product/881/74588?!editLang=zh&!preview#.E8.B4.AD.E4.B9.B0.E5.B9.B6.E6.96.B0.E5.BB.BA.E6.AD.A3.E5.BC.8F.E7.89.88-license))，并单击**确定**即可在应用下生成正式版视频播放功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/9c12544f9ec5ff259f12af38fb02988c.png)
:::
</dx-tabs>

[](id:update_formal)
## 更新正式版 License 有效期
您可以登录 [**腾讯云视立方控制台 > 终端 License 管理**](https://console.cloud.tencent.com/vcube) 页面查看视频播放正式版 License 的有效期，也可通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端 SDK，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。视频播放正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。若您的视频播放正式版 License 已到期，可进行如下操作进行续期：
1. 选择您需要更新有效期的 License，单击直播推流模块内的 **更新有效期**。
![](https://qcloudimg.tencent-cloud.cn/raw/8063f52361e98ffbdd904ffa5d640b74.jpg)
2. 选择**未绑定**过的直播/点播流量资源包或独立 License（若没有可绑定的 License 资源，可前往 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube) 购买），单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/c0908161aa4d18f6bc2507322e8e95f5.png)
3. 查看更新后的有效期情况。

>! **视频播放正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **新增 License** 重新新增 License 绑定新的包名信息。

