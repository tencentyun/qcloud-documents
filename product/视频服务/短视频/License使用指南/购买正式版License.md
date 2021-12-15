短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台上对短视频 SDK 进行新增、升级和续期。

[](id:formal)
## 正式版 License

### 注意事项
- **正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于续期 License，请单击 **创建应用并绑定License** 重新新增 License 绑定新的包名信息。
- 短视频 SDK License 需要通过 [云点播控制台](https://console.cloud.tencent.com/vod/license/video) 与 [流量资源包](https://cloud.tencent.com/document/product/266/14667#flow_page) 进行绑定。绑定成功后该资源包视为已使用，不支持5天内无理由退款。
- 短视频 License 用于腾讯云视立方·音视频终端引擎管理功能模块的授权解锁，您可以通过在 [消息订阅](https://console.cloud.tencent.com/message/subscription) 中订阅音视频终端引擎，接收 License 到期提醒，以及更多各渠道消息通知。短视频 License 将在到期时间距离当前时间为30天、15天、7天、1天时向您发送一次到期提醒，提示您及时续费以免影响正常业务运行。

[](id:creat_formal)

### 购买正式版 License
购买指定规格的 [云点播流量资源包](https://cloud.tencent.com/document/product/584/9368)，获得赠送1年有效期的正式短视频 License 使用权限（有效期至到期次日的00:00:00止），具体 SDK 版本 License 与您需要购买的点播套餐包关系对应如下表：

| SDK License 版本                                             | 套餐包                                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [精简版 SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 10TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) |
| [基础版 SDK（UGC）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 50TB、200TB 或 1PB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) |
| [企业版 SDK（UGC_Enterprise）](https://cloud.tencent.com/document/product/584/9366#sdk) | 请参见 [申请企业版本 License](#enterpriseli)                 |
| [企业版 Pro SDK（EnterprisePro）](https://cloud.tencent.com/document/product/584/9366#sdk) | 请参见 [申请企业版本 License](#enterpriseli)                 |

#### 操作步骤
1. 进入 **[云点播控制台](https://console.cloud.tencent.com/vod/license/video)**>**License 管理**>**[SDK License](https://console.cloud.tencent.com/vod/license/video)**，单击 **创建应用并绑定License** 按钮。填写 App Name、Package Name 和 Bundle ID并勾选功能模块 **短视频**，根据实际需求选择 **精简版** 或 **基础版**，完成后单击 **下一步**。
![](https://main.qcloudimg.com/raw/d9bb304bb79de0d5cde9db737abd1bd9.png)
2. 进入选择套餐包并绑定 License 界面，选择**未绑定**的云点播流量资源包，单击 **确定** 即可生成短视频（精简版/基础版）正式版 License。
![](https://main.qcloudimg.com/raw/6b0a059af1b106a1e876dc53edabd2b0.png)
>! 
> - 单击 **确定** 前需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请提前进行修改，**一旦提交成功将无法再修改 License 信息**。
> - 若无已购买资源包，请单击 **购买页** 前往选购流量资源包10TB、流量资源包50TB、流量资源包200TB中的任意一种。
> - 各规格资源包均有对应的 SDK License 版本，具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
3. 正式版 License 成功创建后，页面会显示生成的 正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/c46b3a484dbcc8070d9c2d5d728953db.png)


[](id:renew_formal)
### 更新正式版 License
您可以登录 **云点播控制台** > **License 管理**>**[SDK License](https://console.cloud.tencent.com/vod/license/video)** 页面查看短视频正式版 License 的有效期，正式版本的 License 有效期为一年。若您对指定 License 进行续期，请保证已购买流量资源包的情况下，可进行如下操作进行续期：
1. 选择您需要更新有效期的短视频 License，单击对应视频模块中的 **更新有效期**。
![](https://main.qcloudimg.com/raw/a0e9a956644566f69a0b8d5293cdbf8e.png)
2. 选择**未绑定**过的云点播流量资源包（如没有可更新有效期的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube?sdk-version=3&function-module=SHORT_VIDEO) 购买），单击 **确定** 即可。
3. 查看更新后的有效期情况。

>! **短视频正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **新增 License** 重新新增 License 绑定新的包名信息。

[](id:update_formal)

### 升级正式版 License
若您已经具备短视频精简版的正式版 License，且需要变速录制、背景音乐、滤镜特效等更强大的能力，您可以通过以下方式升级为短视频基础版的正式版 License，解锁更多功能：
1. 选择需要升级的正式版 License，单击短视频模块内的 **升级**。
![](https://main.qcloudimg.com/raw/7b9766f087097b02baf66d3e47385caa.png)
2. 进入升级功能模块界面，选择需要绑定的云点播流量资源包（规格需可选择为 50TB 或 200TB），单击 **确定** 即可升级到短视频基础版的正式版 License。
![](https://main.qcloudimg.com/raw/48aa2580a6ab0e25a20e986b183ab189.png)

>! **短视频精简版正式版 License** 成功升级为**短视频基础版正式版 License** 后，原有绑定短视频精简版的套餐包（规格为 10TB 的云点播流量资源包）会进行释放，即结束绑定关系，此套餐包可重新绑定其他应用内的短视频 License。

[](id:pro)[](id:enterpriseli)

## 企业版本 License

相比于基础版，企业版增加了基于腾讯优图实验室专利技术的人脸特效功能。使用企业版 License 可以开启优图实验室的 AI 功能。

> ? 
> - 企业版 License 基本配置方法与基础版 License 相同，具体请参见 配置查看 License。配置完成后需额外配置 [动效变脸](https://cloud.tencent.com/document/product/584/13509) 功能。
> - 若您需开通企业版 License，请 [单击此处](https://cloud.tencent.com/product/x-magic)。




