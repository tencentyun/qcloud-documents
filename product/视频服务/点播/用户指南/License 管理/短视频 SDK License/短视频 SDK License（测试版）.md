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

1. 登录**[云点播控制台](https://console.cloud.tencent.com/vod/license)**，左侧菜单中选择**License 管理** >**[SDK License](https://console.cloud.tencent.com/vod/license/video)**，单击**创建测试 License **。
![](https://main.qcloudimg.com/raw/a623b59b4989ef4d713fc5a2e13927c1.png)
2. 根据实际需求填写 App Name、Package Name 和 Bundle ID，勾选功能模块**短视频**，单击**确定**。
![](https://main.qcloudimg.com/raw/d9f3d35b4315a466f6b5fe823831f057.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/72b7376b67bbce7fd922e30addf76614.png)

>? 
>- 测试版 License 有效期内可单击右侧的**编辑**，进入修改 Bundle ID 和 Package Name 信息，单击**确定**即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。


[](id:renew)
### 续期测试版 License

您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license/videoe) 查看测试版 License 的有效期。测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块**短视频**右侧的**续期**按钮，选择**确定续期**即可续期该功能模块14天。
![](https://main.qcloudimg.com/raw/348da4abf6673f65035eec391d7310ee.png)

>! 测试版 License 有效期共28天，只能续期一次。若您需继续使用，请 [购买](https://buy.cloud.tencent.com/vcube) 正式版 License。

[](id:update_test)

### 测试版 License 升级
若您需要将短视频测试版 License 升级成为短视频正式版 License，获得一年的有效的使用期。具体操作如下：

1. 进入云点播控制台，选择 **License 管理** >**[SDK License](https://console.cloud.tencent.com/vod/license/video)**。
2. 选择测试版 License，单击短视频模块中的**升级**。
![](https://main.qcloudimg.com/raw/ccb771bafef68ec62507904eb45b0aab.png)
3. 进入升级功能模块界面，选择需要绑定的云点播流量资源包，单击**确定**即可升级到短视频（精简版/基础版）的正式版 License。
![](https://main.qcloudimg.com/raw/50183054e3d1ff5a0f74a80b2bc279aa.png)

>!
>- 若无已购买资源包，请单击**资源包购买页**前往选购流量资源包10TB、流量资源包50TB、流量资源包200TB中的任意一种。具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
>- 短视频测试版 License 升级为**短视频精简版**的正式版 License 仅支持选择 10TB 规格的云点播流量资源包。
>- 短视频测试版 License 升级为**短视频基础版**的正式版 License 可选择 50TB、200TB、1PB 规格的云点播流量资源包。
