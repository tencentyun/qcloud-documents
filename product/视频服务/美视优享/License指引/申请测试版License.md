腾讯特效 License 用于解锁腾讯特效 SDK 的使用权限，您可以在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 申请腾讯特效测试版 License。新增和续期正式版 License 等操作请参见 [购买正式版 License](https://cloud.tencent.com/document/product/616/65879)。

## 申请测试版 License[](id:create)
您可以免费申请腾讯特效模块的测试版 License（免费测试有效期为14天，可续期1次，共28天）体验测试。测试版 License 统一签发的最高级版本 S1 - 04 的授权，您可以用此版本测试腾讯特效 SDK 的全功能。

> !**腾讯特效功能模块在申请之后，需要审核通过才能签发授权**，测试版授权到期时间以审核通过时刻为准；若试用期结束后申请测试续期，则续期到期时间以申请测试续期时刻为准。
> - 当提交腾讯特效功能模块测试版审核信息后，进入**审核中状态**，审核时间通常 1-2 个工作日。提交审核信息时间为 `2021-12-31 21:26:23`，审核通过时间为 `2022-01-01 09:39:38`，则开始时间为 `2022-01-01 09:39:38`，14天后到期时间为 `2022-01-15 23:59:59`。
> - 免费续期一次时，若在试用期14天内申请续期，则到期时间为 `2022-01-29 23:59:59`；若在试用期14天结束后申请续期，申请续期的时间为 `2022-02-06 22:26:20`，则续期的到期时间为 `2022-02-20 23:59:59`。

1. 申请测试模块。您可以选择**新建测试应用并申请测试模块** 或在**已创建的测试应用中申请测试模块** 两种方式创建测试 License。
<dx-tabs>
::: 方式一：新建测试应用并申请测试模块
1. 登录 [**腾讯云视立方控制台**](https://console.cloud.tencent.com/vcube)，单击 **创建测试 License**。
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块 **高级套餐 S1 - 04** 的腾讯特效测试套餐，单击 **确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/8184955b25fe97b1a79c4571897b2195.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://qcloudimg.tencent-cloud.cn/raw/f570acd4b527a49b98f9b412627dd83b.png)
> ?
> - 测试版 License 有效期内可单击右侧的 **编辑**，进入修改 Bundle ID 和 Package Name 信息，单击 **确定** 即可保存，但会导致此测试 License 下生效中的测试版腾讯特效功能模块**重新进入审核流程**，待审核通过后方可继续使用。
 ![](https://qcloudimg.tencent-cloud.cn/raw/44aa937338a9cf082c84bd41dbd027b4.png)
> - 若无 Package Name 或 Bundle Id，可填写“-”。
:::
::: 方法二：已创建的测试应用中申请测试模块
若您想在已创建的测试应用中申请腾讯特效功能测试模块，步骤如下：
1. 选择您想测试的应用，单击 **测试新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/8eb1114c91204dec3669cbf0b6fd15a4.png)
2. 勾选功能模块 **高级套餐 S1 - 04** 的腾讯特效测试套餐，单击 **确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/7dee1f7c25f389fc304717258ddb489d.png)
:::
</dx-tabs>
2. 腾讯特效 License 需要通过签发审核后才能使用。应用中，创建成功的腾讯特效功能模块此时为**未审核状态**，单击 **发起审核**。
![](https://qcloudimg.tencent-cloud.cn/raw/24f12986408c123318fe79eaa82132fd.png)
3. 在审批申请页中准确填写 **公司名称、所属行业类型**，上传**公司营业执照** ，单击**保存并提交**提交审核申请，等待人工审核流程。
![](https://qcloudimg.tencent-cloud.cn/raw/f70d0af2f373345511b266591311ee6a.png)
4. 提交后模块进入**审核中状态**，审核时间通常 1-2 个工作日。可单击 **查看审核信息** 查看提交的审核信息。
![](https://qcloudimg.tencent-cloud.cn/raw/1effb751cb28557ca4ee9296e1455a53.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8db173d7195b7edf7653b6028968d926.png)
5. 审核通过后，腾讯特效功能模块为**生效中状态**，腾讯特效测试版 License 申请成功，您可开始使用腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/8c7706d4fe5cbb5b2b8387098d46a2d0.png)
>? **若审核失败**未通过，单击 **审核结果** 查看审核结果和审核备注，您可根据审核备注知悉审核失败原因，单击 **重新发起审核**。更改审核信息并提交，等待人工审核流程。
>![](https://qcloudimg.tencent-cloud.cn/raw/0c9e3e72b9fa942a16c91c965f9630b3.png)


## 续期测试版 License[](id:renewal)
测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块 **腾讯特效** 右侧的 **续期**，单击 **确定续期** 即可续期该功能模块14天。
![](https://qcloudimg.tencent-cloud.cn/raw/6dd85e6c359d2ffcd931475e4ff6e1f2.png)
> ?测试版 License 有效期共28天，**只能续期一次**。若您需继续使用，请购买 [正式版 License](https://cloud.tencent.com/document/product/616/65879)。

## 升级测试版 License[](id:upgrade)
若您需要将腾讯特效模块的测试版 License 升级成为正式版 License，增加使用的有效期。具体操作如下：
1. 单击测试版 License 腾讯特效模块中的 **升级**。
![](https://qcloudimg.tencent-cloud.cn/raw/dd1539696d3e128cde3961f48f4e8d26.png)
2. 进入升级功能模块界面，选择未绑定的腾讯特效套餐包，单击 **确定** 即可升级创建同包名的正式应用，同时解锁腾讯特效模块的正式版 License，无需签发审核。若无可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube) 前往腾讯视立方资源包购买页购买。
![](https://qcloudimg.tencent-cloud.cn/raw/4bc67e88b7b4b7fc1e231c4d29550f53.png)

