短视频 License 用于解锁短视频（精简版/基础版）模块的使用权限，您可以在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 对短视频 License 进行新增、升级和续期等操作。


[](id:test)
## 测试版 License
[](id:creat_test)

### 申请测试版 License

您可以免费申请短视频模块基础版的测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。

> !试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
> - 当申请测试开始时间为 `2021-08-12 10:28:41`，则14天后到期时间为 `2021-08-26 10:28:41`。
> - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2021-09-09 10:28:41`；若在试用期14天结束后申请续期，申请续期的时间为 `2021-08-30 22:26:20`，则续期的到期时间为 `2021-09-13 22:26:20`。

具体步骤如下：

1. 登录 **[腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)**，单击 **创建测试 License**。
![](https://main.qcloudimg.com/raw/a623b59b4989ef4d713fc5a2e13927c1.png)
2. 根据实际需求填写 App Name、Package Name 和 Bundle ID，勾选功能模块 **短视频**，单击 **确定**。
![](https://main.qcloudimg.com/raw/d9f3d35b4315a466f6b5fe823831f057.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/72b7376b67bbce7fd922e30addf76614.png)

>? 
>- 测试版 License 有效期内可单击右侧的 **编辑**，进入修改 Bundle ID 和 Package Name 信息，单击 **确定** 即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。


[](id:renew)
### 续期测试版 License

测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块 **短视频** 右侧的 **续期** 按钮，选择 **确定续期** 即可续期该功能模块14天。
![](https://main.qcloudimg.com/raw/348da4abf6673f65035eec391d7310ee.png)

>! 测试版 License 有效期共28天，只能续期一次。若您需继续使用，请 [购买](https://buy.cloud.tencent.com/vcube) 正式版 License。

[](id:update_test)
### 测试版 License 升级
若您需要将短视频测试版 License 升级成为短视频正式版 License，获得一年的有效的使用期。具体操作如下：

1. 单击测试版 License 短视频模块中的 **升级**。
![](https://main.qcloudimg.com/raw/ccb771bafef68ec62507904eb45b0aab.png)
2. 进入升级功能模块界面，选择需要绑定的云点播流量资源包，单击 **确定** 即可升级到短视频（精简版/基础版）的正式版 License。
![](https://main.qcloudimg.com/raw/50183054e3d1ff5a0f74a80b2bc279aa.png)

>!
> - 短视频测试版 License 升级为**短视频精简版**的正式版 License 仅支持选择 10TB 规格的云点播流量资源包。
> - 短视频测试版 License 升级为**短视频基础版**的正式版 License 可选择 50TB、200TB、1PB 规格的云点播流量资源包。

[](id:formal)
## 正式版 License
[](id:creat_formal)
### 购买正式版 License
1. 购买指定规格的 [云点播流量资源包](https://cloud.tencent.com/document/product/1449/56973#video)，获得赠送1年有效期的正式短视频（精简版/基础版）License 使用权限（有效期至到期次日00:00:00止），具体 License 版本对应套餐包如下表：
<table>
<tr><th>License 版本</th><th>套餐包</th>
</tr><tr>
<td>短视频精简版 License</td>
<td>云点播流量资源包 10TB</td>
</tr><tr>
<td>短视频基础版 License</td>
<td>云点播流量资源包 50TB、200TB、1PB</td>
</tr></table>
2. 进入 **[腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)**，单击 **创建应用并绑定License** 按钮。填写 App Name、Package Name 和 Bundle ID并勾选功能模块 **短视频**，根据实际需求选择 **精简版** 或 **基础版**，完成后单击 **下一步**。
![](https://main.qcloudimg.com/raw/d9bb304bb79de0d5cde9db737abd1bd9.png)
3. 进入选择套餐包并绑定 License 界面，选择**未绑定**的云点播流量资源包，单击 **确定** 即可生成短视频（精简版/基础版）正式版 License。
![](https://main.qcloudimg.com/raw/6b0a059af1b106a1e876dc53edabd2b0.png)
>! 单击 **确定** 前需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请提前进行修改，**一旦提交成功将无法再修改 License 信息**。
4. 正式版 License 成功创建后，页面会显示生成的 正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/c46b3a484dbcc8070d9c2d5d728953db.png)


[](id:renew_formal)
### 更新正式版 License
您可以登录 **[腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)** 页面查看短视频正式版 License 的有效期，也可通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端引擎，配置**站内信**/**邮件**/**短信**/**微信**/**企微**等消息接收渠道，接收正式版 License 到期提醒。直播推流正式版 License 将在到期时间距离当前时间为30天、15天、7天、1天时各向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。若您的短视频正式版 License 已到期，可进行如下操作进行续期：
1. 选择您需要更新有效期的短视频 License，单击对应视频模块中的 **更新有效期**。
![](https://main.qcloudimg.com/raw/a0e9a956644566f69a0b8d5293cdbf8e.png)
2. 选择**未绑定**过的云点播流量资源包（如没有可更新有效期的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube) 购买），单击 **确定** 即可。
3. 查看更新后的有效期情况。

>! **短视频（精简版/基础版）的正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **新增 License** 重新新增 License 绑定新的包名信息。


[](id:update_formal)
### 升级正式版 License
若您已经具备短视频（精简版）的正式版 License，且需要变速录制、背景音乐、滤镜特效等更强大的能力，您可以通过以下方式升级为短视频（基础版）的正式版 License，解锁更多功能：
1. 选择需要升级的正式版 License，单击短视频模块内的 **升级**。
![](https://main.qcloudimg.com/raw/7b9766f087097b02baf66d3e47385caa.png)
2. 进入升级功能模块界面，选择需要绑定的云点播流量资源包（规格需可选择为 50TB、200TB 或 1PB），单击 **确定** 即可升级到短视频（基础版）的正式版 License。
![](https://main.qcloudimg.com/raw/48aa2580a6ab0e25a20e986b183ab189.png)

>! **短视频（精简版）正式版 License** 成功升级为**短视频（基础版）正式版 License** 后，原有绑定短视频（精简版）的套餐包（规格为 10TB 的云点播流量资源包）会进行释放，即结束绑定关系，此套餐包可重新绑定其他应用内的短视频 License。





