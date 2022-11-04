腾讯特效 License 提供美颜特效相关能力，购买腾讯特效套餐获得套餐1年使用权限，解锁对应腾讯特效功能。计费购买详情请参见 [价格总览](https://cloud.tencent.com/document/product/616/36807)。

购买后可在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 对腾讯特效 License 进行新增和续期等操作。腾讯特效 License 可以支持移动端或 PC 端绑定，一经绑定不可修改。 
本文将对腾讯特效移动端 License 测试版和正式版的新增和续期等操作进行说明指引。

[](id:test)

## 测试版 License

### 申请测试版 License[](id:create_test)

您可以免费申请腾讯特效模块的测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。测试版 License 您可根据自己的需求选择相应的能力进行申请。您可对美颜特效套餐以及原子能力的测试申请；其中套餐仅支持签发最高级版本 S1 - 04 的授权，您可以用此版本测试腾讯特效 SDK套餐全功能，最高级版本 S1 - 04 功能说明请参见 [功能说明](https://cloud.tencent.com/document/product/616/67043) S 系列高级套餐 S1-04。套餐 S1-04 中包含了 X1-01 人像分割能力，其余能力不包含。

> !**腾讯特效功能模块在申请之后，需要审核通过才能签发授权**，测试版授权到期时间以审核通过时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
> - 当提交腾讯特效功能模块测试版审核信息后，进入**审核中状态**，审核时间通常 1-2 个工作日。提交审核信息时间为 `2022-05-24 12:47:33`，审核通过时间为 `2022-05-24 15:23:46`，则开始时间为 `2022-05-24 15:23:46`，14天后到期时间为 `2022-06-09 00:00:00`。
> - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2022-06-23 00:00:00`；若在试用期14天结束后申请续期，申请续期的时间为 `2022-08-06 22:26:20`，则续期的到期时间为 `2022-08-22 00:00:00`。

1. 申请测试模块。您可以选择**新建测试 License 并申请测试功能模块**或在**已创建的测试应用中申请测试新功能模块**两种方式创建测试 License。
<dx-tabs>
::: 方式一：新建测试 License 并申请测试功能模块
1. 登录 [**腾讯云视立方控制台 > 移动端 License**](https://console.cloud.tencent.com/vcube)，单击**新建测试 License**。
  ![](https://qcloudimg.tencent-cloud.cn/raw/4d63d6f14f82ba1775083ed461c5f5db.png)
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选腾讯特效，选择所需测试的能力高级套餐 S1 - 04**、**原子能力X1 - 01**、**原子能力X1 - 02**，勾选后准确填写 **公司名称、所属行业类型**，上传**公司营业执照**，单击**确定**提交审核申请，等待人工审核流程。
![](https://qcloudimg.tencent-cloud.cn/raw/0c0a37958415de35aab55f6f0f21bef5.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。此时 Key 和 LicenseURL 两个参数暂未生效，需提交的审核通过后方才生效使用。**在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。**
![](https://qcloudimg.tencent-cloud.cn/raw/c78143569f99c2aad80a2e3268a4240a.png)
> ?
> - 测试版 License 有效期内可单击右侧的**编辑**，进入修改 Bundle ID 和 Package Name 信息，单击**确定**即可保存，但会导致此测试 License 下生效中的测试版腾讯特效功能模块**重新进入审核流程**，待审核通过后方可继续使用。
>   ![](https://qcloudimg.tencent-cloud.cn/raw/09de9264eaa7a5bcc5c85d43f97d785c.png)
> - 若无 Package Name 或 Bundle Id，可填写“-”。
:::
::: 方法二：已创建的测试应用中申请测试新功能模块
若您想在已创建的测试应用中申请腾讯特效功能测试模块，步骤如下：
1. 选择您想测试的应用，单击**测试新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/6be952eb22fdc3db08c931c250a84e9c.png)
2. 勾选功能模块**腾讯特效**，在选择能力中勾选自己需要测试的功能，勾选后准确填写 **公司名称、所属行业类型**，上传**公司营业执照**，单击**确定**提交审核申请，等待人工审核流程。 
![](https://qcloudimg.tencent-cloud.cn/raw/7668838fd03e6ed5ee6836cea5ef2476.png)
:::
</dx-tabs>
2. 提交审核申请后模块进入**公司资质审核中**，审核时间通常 1-2 个工作日。可单击**查看审核信息**查看提交的审核信息。
![](https://qcloudimg.tencent-cloud.cn/raw/96ca8e3ee3fd42c22205d76ba5288517.png)
![](https://qcloudimg.tencent-cloud.cn/raw/9ee26ec97685f4fd881804ccf204ebcb.png)
3. 审核通过后，腾讯特效功能模块状态为**正常**，腾讯特效测试版 License 申请成功，您可开始使用腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/a3d6b29b0b824f23a18ea93f5adbf016.png)
>? **若审核失败**未通过，单击**审核结果**查看审核结果和审核备注，您可根据审核备注知悉审核失败原因，单击**重新发起审核**。更改审核信息并提交，等待人工审核流程。
>![](https://qcloudimg.tencent-cloud.cn/raw/79eeef69825781c95061536296be94c0.png)

[](id:renewal_test)
### 续期测试版 License
测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块**腾讯特效**右侧的**续期**，单击**确定续期**即可续期该功能模块14天。
![](https://qcloudimg.tencent-cloud.cn/raw/5da5f8b6b35cf7afe8ef74a6407e9145.png)

> ?测试版 License 有效期共28天，**只能续期一次**。若您需继续使用，请购买 [正式版 License](#create_formal)。

[](id:upgrade_test)
### 升级测试版 License
若您需要将腾讯特效模块的测试版 License 升级成为正式版 License，增加使用的有效期，请先 [选择并购买腾讯特效正式版套餐包](https://buy.cloud.tencent.com/vcube?type=magic)，然后执行如下操作：
1. 单击测试版 License 腾讯特效模块中的**升级**。
![](https://qcloudimg.tencent-cloud.cn/raw/3cf3633ecd1a093d61b4b1561c18d4da.png)
2. 进入升级功能模块界面，单击**立即绑定**，选择未绑定的腾讯特效套餐包，单击**确定**即可升级创建同包名的正式应用，同时解锁腾讯特效模块的正式版 License，无需签发审核。若无可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 前往腾讯视立方资源包购买页购买。
![](https://qcloudimg.tencent-cloud.cn/raw/9c3134446ec1584428cf88b8859fefa9.png)

[](id:formal)
## 正式版 License
[](id:create_formal)
### 购买正式版 License
您可根据具体需求场景，在 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube?type=magic) 选择并购买 SDK 套餐，获得相应的正式版 License 使用授权（有效期 1 年至到期次日00:00:00为止）。各版本 SDK 的功能差异请参见 [计费概述](https://cloud.tencent.com/document/product/616/36807)。

具体步骤如下：
1. 绑定腾讯特效正式版 License。您可以选择**新建正式应用并绑定 License**或在**已创建的应用上解锁腾讯特效正式版模块并绑定 License**两种方式进行正式版 License 绑定。 
<dx-tabs>
::: 方式一：新建正式应用并绑定 License
1. 进入 [**腾讯云视立方控制台 > 移动端 License**](https://console.cloud.tencent.com/vcube)，单击**新建正式 License**。  
![](https://qcloudimg.tencent-cloud.cn/raw/7d7b23dd672ea2c877eab6beb112ea47.png) 
2. 填写正式应用的 `App Name`、`Package Name` 和 `Bundle ID` 信息，勾选功能模块**腾讯特效**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/00bfb0523f61ba86f36381f27c42ad52.png)
3. 进入选择资源项并绑定 License 界面，单击**立即绑定** ，选择**未绑定**的腾讯特效套餐包（若没有可绑定的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 购买），并单击**确定**即可提交审核申请，等待人工审核流程，且同时创建应用并生成正式版 License。 
![](https://qcloudimg.tencent-cloud.cn/raw/1d04924b15bb61ca6e0d816a5b1dab1d.png) 
> ?单击**确定**前需要再次确认 Bundle ID 和 Package Name 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。 
:::
::: 方式二：已创建的正式版应用中解锁模块
1. 选择您需要增加**腾讯特效**功能模块的正式应用，单击**解锁新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/fe4ddea0a0211d4a3a137fd327217374.png)
2. 选择**腾讯特效**，单击**下一步**。  
![](https://qcloudimg.tencent-cloud.cn/raw/d753721e4cbfcd10b224df7ea47d8c87.png)
3. 进入选择资源项并绑定 License 界面，单击**立即绑定** ，选择**未绑定**的腾讯特效套餐包（若没有可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 前往购买），并单击**确定**即可提交审核申请，等待人工审核流程，且同时在应用下生成正式版腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/bda533c60f3217c94a0b3be3fddb952f.png)
:::
</dx-tabs>
2. 腾讯特效功能模块状态为**正常**，腾讯特效正式版 License 申请成功，您可开始使用腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/b3c39bfd71e7ad8e59306ec5404acd0e.png)


[](id:upgrade_formal)
### 更新正式版 License 有效期
您可以登录  [**腾讯云视立方控制台 > 移动端 License 管理**](https://console.cloud.tencent.com/vcube) 页面查看腾讯特效正式版 License 的有效期，若您的腾讯特效正式版 License 已到期，可进行如下操作进行续期：
1. 选择您需要更新有效期的 License，单击腾讯特效模块内的**续期**。
![](https://qcloudimg.tencent-cloud.cn/raw/c4199ac7df499abebc404500e9323c44.png)
2. 选择与原 License **同类型的套餐包**资源进行绑定续期，选择后将实时显示续期的起始时间和结束时间，单击**确定**完成续期。若没有可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 前往购买。
![](https://qcloudimg.tencent-cloud.cn/raw/1147fc8b546152d06f509a32396e48c9.png)
>!目前续期套餐包有效期仅支持同类型的套餐包续期，即若已绑定的 License 套餐包类型为 S1 - 04，则续期是只能选择 S1 - 04 的套餐包进行续期。若想更改绑定的套餐包类型，需 [提交工单](https://console.cloud.tencent.com/workorder/category) 或联系商务进行处理。
3. 查看更新后的有效期情况。
> !**腾讯特效正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击**创建应用并绑定 License**重新创建应用新增 License 绑定新的包名信息。
