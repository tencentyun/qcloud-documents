腾讯特效 License 用于解锁腾讯特效 SDK 的使用权限，您可登录 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 购买绑定正式版 License。腾讯特效 SDK 提供测试版 License 进行功能体验，详情请参见 [申请测试版 License](https://cloud.tencent.com/document/product/616/65878)。

## 购买正式版 License[](id:create)
您可根据具体需求场景，在 [腾讯云视立方·音视频终端引擎购买页](https://buy.cloud.tencent.com/vcube) 选择并购买 SDK 套餐，获得相应的正式版 License 使用授权（有效期 1 年至到期次日00:00:00为止）。各版本 SDK 的功能差异可参考 [计费概述](https://cloud.tencent.com/document/product/616/36807) 文档。

> !**腾讯特效功能模块需要通过审核后才能签发授权**，正式版授权到期时间从审核通过时间计算，1年后到期次日00:00:00止。
> 例如，当创建 License、提交腾讯特效功能模块正式版审核信息后，进入**审核中状态**，审核时间通常 1-2 个工作日。提交审核信息时间为 `2022-01-01 16:16:23`，审核通过时间为 `2022-01-02 09:39:38`，则开始时间为 `2022-01-02 09:39:38`，1 年后到期时间为 `2023-01-03 00:00:00`。

具体步骤如下：
1. 绑定腾讯特效正式版 License。您可以选择**新建应用并绑定 License** 或在**已创建的应用上解锁腾讯特效正式版模块并绑定 License** 两种方式进行正式版 License 绑定 。
<dx-tabs>
::: 方式一：新建正式应用并绑定 License
1. 进入 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)，单击 **创建应用并绑定 License**。
2. 填写正式应用的 `App Name`、`Package Name` 和 `Bundle ID` 信息，勾选功能模块 **腾讯特效正式版**，单击 **下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/37b2497169e623692e45fa286b396e9c.png)
2. 进入选择资源项并绑定 License 界面，选择**未绑定**的腾讯特效套餐包（若没有可绑定的资源包，可前往 [资源包购买页](https://buy.cloud.tencent.com/vcube) 购买），并单击 **确定** 即可创建应用并生成正式版 License。
> ?单击 **确定** 前需要再次确认 Bundle ID 和 Package Name 与业务使用包名信息一致，如与提交到商店的不一致，请在提交前进行修改，**正式版 License 一旦提交成功将无法再修改 License 信息**。
> 
![](https://qcloudimg.tencent-cloud.cn/raw/bb01e653c8e7279635349ea057f92f88.png)
3. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://qcloudimg.tencent-cloud.cn/raw/7701a0f878af542bead25b34fb539bba.png)
:::
::: 方式二：已创建的正式版应用中解锁模块
1. 选择您需要增加腾讯特效功能模块的正式应用，单击 **解锁新功能模块**。
![](https://qcloudimg.tencent-cloud.cn/raw/75889ec1a3a37c14c222d7f89df75622.png)
2. 选择**腾讯特效功能模块 正式版**，单击 **下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/50b40a0491a024ee85957be34a3b9dc4.png)
3. 进入选择资源项并绑定 License 界面，选择**未绑定**的腾讯特效套餐包（若无可绑定的腾讯特效套餐包，可单击 [资源包购买页](https://buy.cloud.tencent.com/vcube) 前往购买），并单击 **确定** 即可在应用下生成正式版腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/1530d7979bf74add8ced5fbbfa583e0d.png)
:::
</dx-tabs>
2. 腾讯特效 License 需要通过签发审核后才能使用。应用中，创建成功的腾讯特效功能模块此时为**未审核状态**，单击 **发起审核**。
![](https://qcloudimg.tencent-cloud.cn/raw/f9d787fad71b0473cf12c14f8a5d3d4b.png)
3. 在审批申请页中准确填写 **公司名称、所属行业类型**，上传**公司营业执照** ，单击**保存并提交**提交审核申请，等待人工审核流程。
![](https://qcloudimg.tencent-cloud.cn/raw/f70d0af2f373345511b266591311ee6a.png)
4. 提交后模块进入**审核中状态**，审核时间通常 1-2 个工作日。可单击 **查看审核信息** 查看提交的审核信息。
![](https://qcloudimg.tencent-cloud.cn/raw/e0c00c121aa23abddfc144ea8dd5f4bb.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8db173d7195b7edf7653b6028968d926.png)
5. 审核通过后，腾讯特效功能模块为**生效中状态**，腾讯特效正式版 License 申请成功，您可开始使用腾讯特效功能模块。
![](https://qcloudimg.tencent-cloud.cn/raw/0f48382f8b2797452e89b0c189c293ca.png)
>? **若审核失败**未通过，单击 **审核结果** 查看审核结果和审核备注，您可根据审核备注知悉审核失败原因，单击 **重新发起审核**，更改审核信息并提交，等待人工审核流程。
>![](https://qcloudimg.tencent-cloud.cn/raw/5c01be9865d33765e3da8d2cf3236a17.png)

## 更新正式版 License 有效期[](id:upgrade)
您可以登录 **[腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)** 页面查看腾讯特效正式版 License 的有效期，若您的腾讯特效正式版 License 已到期，可进行如下操作进行续期：
1. 选择您需要更新有效期的 License，单击腾讯特效模块内的 **续期**。
![](https://qcloudimg.tencent-cloud.cn/raw/d313c5916b01efd59ea8ce94682490ed.png)
2. 选择套餐包资源进行绑定续期，选择后将实时显示续期的起始时间和结束时间，单击 **确定** 完成续期。
![](https://qcloudimg.tencent-cloud.cn/raw/1960a514de5e8186353656ab41707f59.png)
3. 查看更新后的有效期情况。
> !**腾讯特效正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击 **创建应用并绑定 License** 重新创建应用新增 License 绑定新的包名信息。


