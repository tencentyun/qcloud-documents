短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台申请测试版短视频 License 或续期、查看等操作。

[](id:test)

## 测试版 License

### 注意事项

- 首次申请测试版 License，**试用期为14天，可免费续期一次，合计28天**。试用期内申请测试续期，则续期到期时间以申请测试时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
  - 当申请测试开始时间为 `2021-08-12 10:28:41`，则14天后到期时间为 `2021-08-26 10:28:41`。
  - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2021-09-09 10:28:41`；若在试用期14天结束后申请续期，申请续期的时间为 `2021-08-30 22:26:20`，则续期的到期时间为 `2021-09-13 22:26:20`。
- 测试版 License 使用权限对应正式版短视频 SDK License 中的基础版，支持开放**短视频基础版 SDK** 能力，更多详细的功能说明请参见 [SDK 功能及对应的 License 版本](https://cloud.tencent.com/document/product/584/9368#sdk-.E5.8A.9F.E8.83.BD.E5.8F.8A.E5.AF.B9.E5.BA.94.E7.9A.84-license-.E7.89.88.E6.9C.AC)。

[](id:creat_test)

### 申请测试版 License

1. 登录【[云点播控制台](https://console.cloud.tencent.com/vod/license)】，左侧菜单中选择【License 管理】 >【[SDK License](https://console.cloud.tencent.com/vod/license/video)】，单击【创建测试 License 】。
![](https://main.qcloudimg.com/raw/a623b59b4989ef4d713fc5a2e13927c1.png)
2. 根据实际需求填写 App Name、Package Name 和 Bundle ID，勾选功能模块【短视频】，单击【确定】。
![](https://main.qcloudimg.com/raw/3127c6c454fecae07709f4a82fb41089.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/72b7376b67bbce7fd922e30addf76614.png)

>? 
>- 测试版 License 有效期内可单击右侧的【编辑】，进入修改 Bundle ID 和 Package Name 信息，单击【确定】即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。


[](id:renew)
### 续期测试版 License

您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看测试版 License 的有效期。测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块【短视频】右侧的【续期】按钮，选择【确定续期】即可续期该功能模块14天。
![](https://main.qcloudimg.com/raw/348da4abf6673f65035eec391d7310ee.png)

>! 测试版 License 有效期共28天，只能续期一次。若您需继续使用，请 [购买](https://buy.cloud.tencent.com/vcube) 正式版 License。

[](id:update_test)

### 测试版 License 升级
若您需要将短视频测试版 License 升级成为短视频正式版 License，获得一年的有效的使用期。具体操作如下：

1. 进入云点播控制台，选择 【License 管理】 >【[SDK License](https://console.cloud.tencent.com/vod/license/video)】。
2. 选择测试版 License，单击短视频模块中的【升级】。
    ![](https://main.qcloudimg.com/raw/ccb771bafef68ec62507904eb45b0aab.png)
3. 进入升级功能模块界面，选择需要绑定的云点播流量资源包，单击【确定】即可升级到短视频（精简版/基础版）的正式版 License。
    ![](https://main.qcloudimg.com/raw/ce167424d536f3b051a4d3c72be5adb6.png)

>!
>- 若无已购买资源包，请单击【资源包购买页】前往选购流量资源包10TB、流量资源包50TB、流量资源包200TB中的任意一种。具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
>- 短视频测试版 License 升级为**短视频精简版**的正式版 License 仅支持选择 10TB 规格的云点播流量资源包。
>- 短视频测试版 License 升级为**短视频基础版**的正式版 License 可选择 50TB、200TB、1PB 规格的云点播流量资源包。

[](id:formal)
## 正式版 License

### 注意事项
- **正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于续期 License，请单击【创建应用并绑定License 】重新新增 License 绑定新的包名信息。
- 短视频 SDK License 需要通过 [云点播控制台](https://console.cloud.tencent.com/vod/license) 与 [流量资源包](https://cloud.tencent.com/document/product/266/14667#flow_page) 进行绑定。绑定成功后该资源包视为已使用，不支持5天内无理由退款。

[](id:creat_formal)

### 购买正式版 License
购买指定规格的 [云点播流量资源包](https://cloud.tencent.com/document/product/1449/56973?!preview&!editLang=zh#video)，获得赠送1年有效期的正式短视频 License 使用权限（有效期至到期次日的00:00:00止），具体 SDK 版本 License 与您需要购买的点播套餐包关系对应如下表：

| SDK License 版本                                             | 套餐包                                                       |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [精简版 SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 10TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) |
| [基础版 SDK（UGC）](https://cloud.tencent.com/document/product/584/9366#sdk) | [点播流量资源包 50TB 或 200TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) |
| [企业版 SDK（UGC_Enterprise）](https://cloud.tencent.com/document/product/584/9366#sdk) | 请参见 [申请企业版本 License](#enterpriseli)                 |
| [企业版 Pro SDK（EnterprisePro）](https://cloud.tencent.com/document/product/584/9366#sdk) | 请参见 [申请企业版本 License](#enterpriseli)                 |

#### 操作步骤
1. 进入【[云点播控制台](https://console.cloud.tencent.com/vod/license)】>【License 管理】 >【[SDK License](https://console.cloud.tencent.com/vod/license/video)】，单击【创建应用并绑定License 】按钮。填写 App Name、Package Name 和 Bundle ID并勾选功能模块【短视频】，根据实际需求选择【精简版】或【基础版】，完成后单击【下一步】。
![](https://main.qcloudimg.com/raw/d9bb304bb79de0d5cde9db737abd1bd9.png)
2. 进入选择套餐包并绑定 License 界面，选择**未绑定**的云点播流量资源包，单击【确定】即可生成短视频（精简版/基础版）正式版 License。
![](https://main.qcloudimg.com/raw/df6f65abf5dbcbaf8224876d79d22899.png)
>! 
> - 单击【确定】前需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请提前进行修改，**一旦提交成功将无法再修改 License 信息**。
> - 若无已购买资源包，请单击【购买页】前往选购流量资源包10TB、流量资源包50TB、流量资源包200TB中的任意一种。
> - 各规格资源包均有对应的 SDK License 版本，具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
3. 正式版 License 成功创建后，页面会显示生成的 正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/93188278ef04b78572060e7c87aeaaaa.png)


[](id:renew_formal)
### 更新正式版 License
您可以登录【[云点播控制台](https://console.cloud.tencent.com/vod/license)】>【License 管理】>【[SDK License](https://console.cloud.tencent.com/vod/license) 】页面查看短视频正式版 License 的有效期，正式版本的 License 有效期为一年。若您对指定 License 进行续期，请保证已购买流量资源包的情况下，可进行如下操作进行续期：
1. 选择您需要更新有效期的短视频 License，单击对应视频模块中的【更新有效期】。
![](https://main.qcloudimg.com/raw/87ab786d72d8bad10774b2dc9bdfb8a1.png)
2. 选择**未绑定**过的云点播流量资源包（如没有可更新有效期的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube) 购买），单击【确定】即可。
3. 查看更新后的有效期情况。

>! **短视频正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击【新增 License】重新新增 License 绑定新的包名信息。

[](id:update_formal)

### 升级正式版 License
若您已经具备短视频精简版的正式版 License，且需要变速录制、背景音乐、滤镜特效等更强大的能力，您可以通过以下方式升级为短视频基础版的正式版 License，解锁更多功能：
1. 选择需要升级的正式版 License，单击短视频模块内的【升级】。
![](https://main.qcloudimg.com/raw/7d2b607d2731594eee9c452e59f7efd6.png)
2. 进入升级功能模块界面，选择需要绑定的云点播流量资源包（规格需可选择为 50TB 或 200TB），单击【确定】即可升级到短视频基础版的正式版 License。
![](https://main.qcloudimg.com/raw/2c761460a643335121a34c44595fc70c.png)

>! **短视频精简版正式版 License** 成功升级为**短视频基础版正式版 License** 后，原有绑定短视频精简版的套餐包（规格为 10TB 的云点播流量资源包）会进行释放，即结束绑定关系，此套餐包可重新绑定其他应用内的短视频 License。

[](id:pro)[](id:enterpriseli)

## 企业版本 License

相比于基础版，企业版增加了基于腾讯优图实验室专利技术的人脸特效功能。使用企业版 License 可以开启优图实验室的 AI 功能。

> ? 
> - 企业版 License 基本配置方法与基础版 License 相同，具体请参见 配置查看 License。配置完成后需额外配置 [动效变脸](https://cloud.tencent.com/document/product/584/13509) 功能。
> - 若您需开通企业版 License，请 [单击此处](https://cloud.tencent.com/product/x-magic)。



