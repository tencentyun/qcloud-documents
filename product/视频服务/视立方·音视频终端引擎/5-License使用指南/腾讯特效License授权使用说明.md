腾讯特效 License 用于解锁腾讯特效 SDK 的使用权限，且提供测试版 License 进行功能体验，您可登录 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 申请腾讯特效测试版 License和购买绑定正式版 License，本文将对此进行详细的操作说明指引。

[](id:test)
## 测试版 License

### 申请测试版 License[](id:create_test)

您可以免费申请腾讯特效模块的测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。测试版 License 统一签发的最高级版本 S1 - 04 的授权，您可以用此版本测试腾讯特效 SDK 的全功能，最高级版本 S1 - 04 功能说明请参见 [功能说明](https://cloud.tencent.com/document/product/616/67043) S 系列高级套餐 S1-04。

> !**腾讯特效功能模块在申请之后，需要审核通过才能签发授权**，测试版授权到期时间以审核通过时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
> - 当提交腾讯特效功能模块测试版审核信息后，进入**审核中状态**，审核时间通常 1-2 个工作日。提交审核信息时间为 `2021-12-31 21:26:23`，审核通过时间为 `2022-01-01 09:39:38`，则开始时间为 `2022-01-01 09:39:38`，14天后到期时间为 `2022-01-16 00:00:00`。
> - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2022-01-30 00:00:00`；若在试用期14天结束后申请续期，申请续期的时间为 `2022-02-06 22:26:20`，则续期的到期时间为 `2022-02-21 00:00:00`。

1. 申请测试模块。您可以选择**新建测试应用并申请测试模块**或在**已创建的测试应用中申请测试模块**两种方式创建测试 License。
<dx-tabs>
::: 方式一：新建测试应用并申请测试模块
1. 登录 [**腾讯云视立方控制台**](https://console.cloud.tencent.com/vcube)，单击**创建测试 License**。
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块 **高级套餐 S1 - 04**的腾讯特效测试套餐，勾选后出现下拉内容。
3. 在下拉内容中准确填写 **公司名称、所属行业类型**，上传**公司营业执照**，单击**确定**提交审核申请，等待人工审核流程。
![](https://qcloudimg.tencent-cloud.cn/raw/21e91f896771a367bdf3b6ebe05616b3.png)
4. 测试版 License 成功创建后，页面会显示生成的 License 信息。此时 Key 和 LicenseURL 两个参数暂未生效，需提交的审核通过后方才生效使用。**在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。**
![](https://qcloudimg.tencent-cloud.cn/raw/5eef9549bdbc3ea997ad93c7f8aa3675.png)

> ?
> - 测试版 License 有效期内可单击右侧的**编辑**，进入修改 Bundle ID 和 Package Name 信息，单击**确定**即可保存，但会导致此测试 License 下生效中的测试版腾讯特效功能模块**重新进入审核流程**，待审核通过后方可继续使用。
>   ![](https://qcloudimg.tencent-cloud.cn/raw/44aa937338a9cf082c84bd41dbd027b4.png)
> - 若无 Package Name 或 Bundle Id，可填写“-”。
:::
::: 方法二：已创建的测试应用中申请测试模块
若您想在已创建的测试应用中申请腾讯特效功能测试模块，步骤如下：
1. 选择您想测试的应用，单击**测试新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/8eb1114c91204dec3669cbf0b6fd15a4.png)
2. 勾选功能模块 **高级套餐 S1 - 04**的腾讯特效测试套餐，勾选后出现下拉内容。
3.在下拉内容中准确填写 **公司名称、所属行业类型**，上传**公司营业执照**，单击**确定**提交审核申请，等待人工审核流程。 
![](https://qcloudimg.tencent-cloud.cn/raw/69fa59e61996870eb84270ca6a899e1a.png)
:::
</dx-tabs>
2. 提交审核申请后模块进入**审核中状态**，审核时间通常 1-2 个工作日。可单击**查看审核信息**查看提交的审核信息。
![](https://qcloudimg.tencent-cloud.cn/raw/2adf2f1d2e707a05778e6c30d80db24e.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8db173d7195b7edf7653b6028968d926.png)
3. 审核通过后，腾讯特效功能模块状态为**生效中**，腾讯特效测试版 License 申请成功，您可开始使用腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/d47acabe4463aa458f4e594dadc3dc89.png)

>? **若审核失败**未通过，单击**审核结果**查看审核结果和审核备注，您可根据审核备注知悉审核失败原因，单击**重新发起审核**。更改审核信息并提交，等待人工审核流程。
>![](https://qcloudimg.tencent-cloud.cn/raw/0c9e3e72b9fa942a16c91c965f9630b3.png)


### 续期测试版 License[](id:renewal_test)
测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块**腾讯特效**右侧的**续期**，单击**确定续期**即可续期该功能模块14天。
![](https://qcloudimg.tencent-cloud.cn/raw/6dd85e6c359d2ffcd931475e4ff6e1f2.png)

> ?测试版 License 有效期共28天，**只能续期一次**。若您需继续使用，请购买 [正式版 License](https://cloud.tencent.com/document/product/616/65879)。

### 升级测试版 License[](id:up_test)

若您需要将腾讯特效模块的测试版 License 升级成为正式版 License，增加使用的有效期，请先 [选择并购买腾讯特效正式版套餐包](https://buy.cloud.tencent.com/vcube?type=magic)，然后执行如下操作：

1. 单击测试版 License 腾讯特效模块中的**升级**。
![](https://qcloudimg.tencent-cloud.cn/raw/dd1539696d3e128cde3961f48f4e8d26.png)
2. 进入升级功能模块界面，选择未绑定的腾讯特效套餐包，单击**确定**即可升级创建同包名的正式应用，同时解锁腾讯特效模块的正式版 License，无需签发审核。若无可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 前往腾讯视立方资源包购买页购买
![](https://qcloudimg.tencent-cloud.cn/raw/4bc67e88b7b4b7fc1e231c4d29550f53.png)

[](id:formal)
## 正式版 License

### 购买正式版 License[](id:formal_create)

您可根据具体需求场景，在 [音视频终端 SDK 购买页](https://buy.cloud.tencent.com/vcube?type=magic) 选择并购买 SDK 套餐，获得相应的正式版 License 使用授权（有效期 1 年至到期次日00:00:00为止）。各版本 SDK 的功能差异请参见 [计费概述](https://cloud.tencent.com/document/product/616/36807)。

> !**腾讯特效功能模块需要通过审核后才能签发授权**，正式版授权到期时间从审核通过时间计算，1年后到期次日00:00:00止。
> 例如，当创建 License、提交腾讯特效功能模块正式版审核信息后，进入**审核中状态**，审核时间通常 1-2 个工作日。提交审核信息时间为 `2022-01-01 16:16:23`，审核通过时间为 `2022-01-02 09:39:38`，则开始时间为 `2022-01-02 09:39:38`，1 年后到期时间为 `2023-01-03 00:00:00`。

具体步骤如下：
1. 绑定腾讯特效正式版 License。您可以选择**新建应用并绑定 License**或在**已创建的应用上解锁腾讯特效正式版模块并绑定 License**两种方式进行正式版 License 绑定 。
<dx-tabs>
::: 方式一：新建正式应用并绑定 License
1. 进入 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)，单击**创建应用并绑定 License**。
2. 填写正式应用的 `App Name`、`Package Name` 和 `Bundle ID` 信息，勾选功能模块**腾讯特效正式版**，勾选后出现下拉内容。
3. 在下拉内容中准确填写 **公司名称、所属行业类型**，上传**公司营业执照**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/43bd4fd0dd6225babf12c17245055c0b.png)
4. 进入选择资源项并绑定 License 界面，选择**未绑定**的腾讯特效套餐包（若没有可绑定的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 购买），并单击**确定**即可提交审核申请，等待人工审核流程，且同时创建应用并生成正式版 License。
> ?单击**确定**前需要再次确认 Bundle ID 和 Package Name 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。
> 
![](https://qcloudimg.tencent-cloud.cn/raw/bb01e653c8e7279635349ea057f92f88.png)
3. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。此时 Key 和 LicenseURL 两个参数暂未生效，需提交的审核通过后方才生效使用。**在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。**
![](https://qcloudimg.tencent-cloud.cn/raw/5658c349d7dc57d97ad72a4de5206ed7.png)
:::
::: 方式二：已创建的正式版应用中解锁模块
1. 选择您需要增加腾讯特效功能模块的正式应用，单击**解锁新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/75889ec1a3a37c14c222d7f89df75622.png)
2. 选择**腾讯特效功能模块** > **正式版**，勾选后出现下拉内容。
3. 在下拉内容中准确填写 **公司名称、所属行业类型**，上传**公司营业执照**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/7855a350c4657a38c53bbcedba6d156b.png)
4. 进入选择资源项并绑定 License 界面，选择**未绑定**的腾讯特效套餐包（若无可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube?type=magic) 前往购买），并单击**确定**即可提交审核申请，等待人工审核流程，且同时在应用下生成正式版腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/1530d7979bf74add8ced5fbbfa583e0d.png)
:::
</dx-tabs>
2. 提交后模块进入**审核中状态**，审核时间通常 1-2 个工作日。可单击**查看审核信息**查看提交的审核信息。
![](https://qcloudimg.tencent-cloud.cn/raw/e0c00c121aa23abddfc144ea8dd5f4bb.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8db173d7195b7edf7653b6028968d926.png)
3. 审核通过后，腾讯特效功能模块状态为**生效中**，腾讯特效正式版 License 申请成功，您可开始使用腾讯特效功能模块。

![](https://qcloudimg.tencent-cloud.cn/raw/ee3164e8f3a28dab1f863ce889999ed3.png)
>?**若审核失败**未通过，单击**审核结果**查看审核结果和审核备注，您可根据审核备注知悉审核失败原因，单击**重新发起审核**，更改审核信息并提交，等待人工审核流程。
>![](https://qcloudimg.tencent-cloud.cn/raw/5c01be9865d33765e3da8d2cf3236a17.png)



### 更新正式版 License 有效期[](id:up_formal)
您可以登录 **[腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)** 页面查看腾讯特效正式版 License 的有效期，若您的腾讯特效正式版 License 已到期，可进行如下操作进行续期：
1. 选择您需要更新有效期的 License，单击腾讯特效模块内的**续期**。
![](https://qcloudimg.tencent-cloud.cn/raw/d313c5916b01efd59ea8ce94682490ed.png)
2. 选择与原 License **同类型的套餐包**资源进行绑定续期，选择后将实时显示续期的起始时间和结束时间，单击**确定**完成续期。
>!目前续期套餐包有效期仅支持同类型的套餐包续期，即若已绑定的 License 套餐包类型为 S1 - 04，则续期是只能选择 S1 - 04 的套餐包进行续期。若想更改绑定的套餐包类型，需 [提交工单](https://console.cloud.tencent.com/workorder/category) 或联系商务进行处理。
>
![](https://qcloudimg.tencent-cloud.cn/raw/1960a514de5e8186353656ab41707f59.png)
3. 查看更新后的有效期情况。
> !**腾讯特效正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击**创建应用并绑定 License**重新创建应用新增 License 绑定新的包名信息。
