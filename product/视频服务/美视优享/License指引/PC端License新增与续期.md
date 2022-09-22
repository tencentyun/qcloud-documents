腾讯特效 License 提供美颜特效相关能力，购买腾讯特效套餐获得套餐1年使用权限，解锁对应腾讯特效功能。计费购买详情请参见 [价格总览](https://cloud.tencent.com/document/product/616/36807)。

购买后可在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube/pc) 对腾讯特效 License 进行新增和续期等操作。腾讯特效 License 可以支持移动端或PC端绑定，一经绑定不可修改。 
本文将对腾讯特效 PC 端 License 测试版和正式版的新增和续期等操作进行说明指引。

[](id:test)
## 测试版 License

### 申请测试版 License[](id:create_test)

您可以免费申请腾讯特效模块的测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。测试版 License 统一签发的最高级版本 S1 - 04 的授权，您可以用此版本测试腾讯特效 SDK 的全功能，最高级版本 S1 - 04 功能说明请参见 [功能说明](https://cloud.tencent.com/document/product/616/67043) S 系列高级套餐 S1-04。

> !**腾讯特效功能模块在申请之后，需要审核通过才能签发授权**，测试版授权到期时间以审核通过时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
> - 当提交腾讯特效功能模块测试版审核信息后，进入**审核中状态**，审核时间通常 1-2 个工作日。提交审核信息时间为 `2022-05-24 12:47:33`，审核通过时间为 `2022-05-24 15:23:46`，则开始时间为 `2022-05-24 15:23:46`，14天后到期时间为 `2022-06-09 00:00:00`。
> - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2022-06-23 00:00:00`；若在试用期14天结束后申请续期，申请续期的时间为 `2022-08-06 22:26:20`，则续期的到期时间为 `2022-08-22 00:00:00`。

您可以通过**新建测试 License 并申请测试功能模块**方式创建测试 License。
1. 登录 [**腾讯云视立方控制台 > PC端 License**](https://console.cloud.tencent.com/vcube/pc)，单击**新建测试 License**。
![](https://qcloudimg.tencent-cloud.cn/raw/4d63d6f14f82ba1775083ed461c5f5db.png)
2. 根据实际需求填写 `App Name`、`WinProcess Name` 和 `MacBundle ID`，勾选功能模块 **高级套餐 S1 - 04**的腾讯特效测试套餐，勾选后准确填写 **公司名称、所属行业类型**，上传**公司营业执照**，单击**确定**提交审核申请，等待人工审核流程。
![](https://qcloudimg.tencent-cloud.cn/raw/61c6d407a3cc8a8a325720e28ed0faca.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。此时 Key 和 LicenseURL 两个参数暂未生效，需提交的审核通过后方才生效使用。**在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。**
![](https://qcloudimg.tencent-cloud.cn/raw/54586dc116c54c34a353a722644cfc2b.png)
> ?
> - 测试版 License 有效期内可单击右侧的**编辑**，进入修改 WinProcess Name 和 MacBundle ID 信息，单击**确定**即可保存，但会导致此测试 License 下生效中的测试版腾讯特效功能模块**重新进入审核流程**，待审核通过后方可继续使用。
> ![](https://qcloudimg.tencent-cloud.cn/raw/0878baa41e6e2c3994a96084a5650a93.png)
> - 若无 WinProcess Name 或 MacBundle ID，可填写“-”。
3. 提交审核申请后模块进入**公司资质审核中**，审核时间通常 1-2 个工作日。可单击**查看审核信息**查看提交的审核信息。
![](https://qcloudimg.tencent-cloud.cn/raw/322566e2669d5abd2dc028ad0d05658b.png)
4. 审核通过后，腾讯特效功能模块状态为**正常**，腾讯特效测试版 License 申请成功，您可开始使用腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/d15a827aa7f3b6da346f353b5d8534f6.png)
>? **若审核失败**未通过，单击**审核结果**查看审核结果和审核备注，您可根据审核备注知悉审核失败原因，单击**重新发起审核**。更改审核信息并提交，等待人工审核流程。
>![](https://qcloudimg.tencent-cloud.cn/raw/938f4469e145c8c2e2ddd1b1729b1b3c.png)

[](id:renewal_test)
### 续期测试版 License
测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块**腾讯特效**右侧的**续期**，单击**确定续期**即可续期该功能模块14天。
![](https://qcloudimg.tencent-cloud.cn/raw/6acba158d0a2b614012285e0488913af.png)

> ?测试版 License 有效期共28天，**只能续期一次**。若您需继续使用，请购买 [正式版 License](#formal)。

[](id:upgrade_test)
### 升级测试版 License
若您需要将腾讯特效模块的测试版 License 升级成为正式版 License，增加使用的有效期，请先 [选择并购买腾讯特效正式版套餐包](https://buy.cloud.tencent.com/vcube?type=magic)，然后执行如下操作：
1. 单击测试版 License 腾讯特效模块中的**升级**。
![](https://qcloudimg.tencent-cloud.cn/raw/1653a71d4863f7fb341478a9efe84937.png)
2. 进入升级功能模块界面，单击**立即绑定**，选择未绑定的腾讯特效套餐包，单击**确定**即可升级创建同包名的正式应用，同时解锁腾讯特效模块的正式版 License，无需签发审核。若无可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 前往腾讯视立方资源包购买页购买。
![](https://qcloudimg.tencent-cloud.cn/raw/d1fb4dbaabaa9ada6736d77d54ee6bcf.png)

[](id:formal)
## 正式版 License
[](id:create_formal)
### 购买正式版 License
您可根据具体需求场景，在 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube?type=magic) 选择并购买 SDK 套餐，获得相应的正式版 License 使用授权（有效期 1 年至到期次日00:00:00为止）。各版本 SDK 的功能差异请参见 [计费概述](https://cloud.tencent.com/document/product/616/36807)。


具体步骤如下：
1. 绑定腾讯特效正式版 License。您可以通过**新建正式应用并绑定 License**方式进行正式版 License 绑定 。
新建正式应用并绑定 License
1. 进入 [**腾讯云视立方控制台 > PC端 License**](https://console.cloud.tencent.com/vcube/pc)，单击**新建正式 License**。
![](https://qcloudimg.tencent-cloud.cn/raw/7d7b23dd672ea2c877eab6beb112ea47.png)
2. 填写正式应用的 `App Name`、`WinProcess Name` 和 `MacBundle ID` 信息，勾选功能模块**腾讯特效**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/89bebe864ff57bf97ed104c5718847bc.png)
3. 进入选择资源项并绑定 License 界面，单击**立即绑定** ，选择**未绑定**的腾讯特效套餐包（若没有可绑定的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 购买），并单击**确定**即可同时创建应用并生成正式版 License。
![](https://qcloudimg.tencent-cloud.cn/raw/b2eeb18cf4122712126eb335155c582d.png)
> ?单击**确定**前需要再次确认 WinProcess Name 和 MacBundle ID 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。
2. 腾讯特效功能模块状态为**正常**，腾讯特效正式版 License 申请成功，您可开始使用腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/bf819ff40fe3d795412bfa24e9258a01.png)


[](id:upgrade_formal)
### 更新正式版 License 有效期
您可以登录  [**腾讯云视立方控制台 > PC端 License 管理**](https://console.cloud.tencent.com/vcube/pc) 页面查看腾讯特效正式版 License 的有效期，若您的腾讯特效正式版 License 已到期，可进行如下操作进行续期：
1. 选择您需要更新有效期的 License，单击腾讯特效模块内的**续期**。
![](https://qcloudimg.tencent-cloud.cn/raw/1266e5c25ad64c700cec69ec4a5bde9a.png)
2. 选择与原 License **同类型的套餐包**资源进行绑定续期，选择后将实时显示续期的起始时间和结束时间，单击**确定**完成续期。若没有可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 前往购买。
![](https://qcloudimg.tencent-cloud.cn/raw/1147fc8b546152d06f509a32396e48c9.png)
>!目前续期套餐包有效期仅支持同类型的套餐包续期，即若已绑定的 License 套餐包类型为 S1 - 04，则续期是只能选择 S1 - 04 的套餐包进行续期。若想更改绑定的套餐包类型，需 [提交工单](https://console.cloud.tencent.com/workorder/category) 或联系商务进行处理。
3. 查看更新后的有效期情况。
> !**腾讯特效正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击**创建应用并绑定 License**重新创建应用新增 License 绑定新的包名信息。
