本文介绍使用 DTS 数据迁移功能跨账号（腾讯云账号）进行实例间的数据迁移操作。

## 支持范围
源数据库为腾讯云的云数据库实例，具体为 MySQL、MongoDB、PostgreSQL、Redis（需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请）、Tendis（需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请）、SQL Server。

## 前提条件
已创建目标数据库实例。

## 注意事项
本操作中涉及多处账号信息配置，如下列出了主要配置逻辑，以方便用户理解和正确配置。
- 数据迁移方向：源数据库（其他账号的数据库实例）> 目标数据库（本账号的数据库实例）。
- 执行迁移任务的账号可以是目标数据库的主账号，也可以目标数据库的子账号。
 - 使用主账号执行迁移任务。操作任务前，需要请求源数据所属主账号持有人进行角色授权（给目标数据库的主账号），使目标数据库主账号可以访问源数据库。
 - 使用子账号执行迁移任务。操作任务前，需要先请求源数据所属主账号持有人进行角色授权（给目标数据库的主账号），使目标数据库主账号通过角色访问源数据库。然后再请求目标数据库所属主账号持有人进行策略授权（对目标数据库的子账号），使目标数据库子账号可以访问源数据库。

[](id:SQZH)
## 授权账号
**使用主账号执行迁移任务，请操作步骤1 - 6，使用子账号执行迁移任务，请操作步骤1 - 11。**
1. 使用源数据库所属的腾讯云主账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/role)（如果子账号有 CAM 和角色相关的权限，也可以使用子账号登录）。
2. 左侧导航单击角色，进入角色管理页面，然后单击**新建角色**。
3. 在选择角色载体页面，选择腾讯云账户方式。
![](https://qcloudimg.tencent-cloud.cn/raw/86d2d4bb2608bdb2648d3a1225df6c58.png)
4. 在**输入角色载体信息**页面，配置相关信息，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/536c1b2c3ca6738df7c21863c28a744c.png)
 - 云账号类型：选择**其他主账号**。
 - 账号 ID：填入目标数据库所属的腾讯云主账号 ID，主账号 ID 可在 [账号信息](https://console.cloud.tencent.com/developer) 中查看。目标数据库实例属于子账号名下时，此处也填写主账号 ID。
 - 外部 ID：可依据情况，选择性开启。
>?如果使用了外部 ID，请用户自行记录和保存该 ID。无法通过 DTS 服务查询到该 ID。
5. 在**配置角色策略**页面，选择 DTS 策略和源数据库服务对应策略，单击**下一步**。
 - DTS 服务策略，选择 QcloudDTSReadOnlyAccess。
 - 源数据库服务对应的策略，需要选择源数据库的只读服务策略和获取列表策略。
 例如源数据库为云数据库 SQL Server，则添加 QcloudSQLServerReadOnlyAccess（获取云数据库 SQL Server 相关资源只读访问权限）。
>?源数据库必须添加 QcloudCDBReadOnlyAccess，否则配置迁移任务时无法获取到源库实例列表信息。
>
![](https://qcloudimg.tencent-cloud.cn/raw/f1d379ccba454694ceb3fda8524a8b46.png)
6. 配置角色标签，然后在**审阅**页面，设置角色名称，单击**完成**后该角色创建完成。
>?角色名称配置后请记录，后续创建迁移任务时需要输入。
>
![](https://qcloudimg.tencent-cloud.cn/raw/1b753b0476af9c87bebce3985ac00f6a.png)
>?如果执行迁移任务的账号为主账号，授权步骤到此结束；如果为子账号，还需要继续进行如下步骤7-11，请求当前主账号持有人，对子账号进行策略授权。
>
7. （可选）使用目标数据库所属的腾讯云主账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/role)，在左侧导航单击**策略**，然后在右侧单击**新建自定义策略**，并选择**按策略语法创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/0e14b343f3e2c72ac8a075b3411874e5.png)
8. （可选）选择**空白模板**，然后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/886ff22b2fdf38a5dbfa4316f616abc7.png)
9. （可选）创建一个策略，策略的名称以及描述可以根据自己的需求填写，策略内容复制示例代码后，将红框中的内容替换成对应的信息。
![](https://qcloudimg.tencent-cloud.cn/raw/ca063529415f14948313d45de827383c.png)
策略语法示例：
```
{
    "version": "2.0",
    "statement": [
    {
        "effect": "allow",
        "action": ["name/sts:AssumeRole"],
  "resource": ["qcs::cam::uin/10*******8:roleName/DTS-role"]
    }
 ]
}
```
10. （可选）单击**完成**后返回到策略列表页，在列表页中单击**关联用户/组**。
![](https://qcloudimg.tencent-cloud.cn/raw/56ade4a8f86feb026220994584b97dc5.png)
11. （可选）选择目标数据库实例所属子账号（即执行迁移任务的子账号），单击**确定**，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/1c710af06c1c15398c761c5653fd8be7.png)

## 创建迁移任务
1. 使用目标数据库实例所属腾讯云账号，登录 [DTS 控制台](https://console.cloud.tencent.com/dts/overview)。
2. 选择**数据迁移 > 新建迁移任务**，购买一个新的迁移任务。
3. 购买完成后，返回数据迁移列表，单击**操作**列的**配置**，进入配置迁移任务页面。
4. 在设置源和目标数据库页面，配置源库和目标库信息。
跨账号关键参数配置如下：
 - 接入类型：选择云数据库，表示源数据库属于腾讯云数据库实例。
 - 是否跨账号：选择跨账号。
 - 跨腾讯云账号 ID： 填入源数据库所属的主账号 ID。
 - 跨账号授权角色名称。即前文 [授权账号](#SQZH) 步骤6中创建的**角色名称**。您可以通过 [角色](https://cloud.tencent.com/document/product/598/19420) 以及 [跨账号角色](https://cloud.tencent.com/document/product/1312/48171) 了解更多关于角色的概念。
 - 角色外部 ID：这个选项可选。这个参数可以通过前文获得。您可以通过 [角色](https://cloud.tencent.com/document/product/598/19420) 以及 [跨账号角色](https://cloud.tencent.com/document/product/1312/48171) 了解更多关于角色的概念。
 >?完成上述配置后，选择对应的所属地域，即可获取到跨账号下的实例列表，如果获取实例出现报错，则可能为配置错误，或者未授权，请参考 [常见问题](#CJWT) 进行处理。
5. 在设置迁移选项和迁移对象页面，对数据迁移选项、迁移对象选项进行设置，在设置完成后单击**保存并下一步**。
6. 在校验任务页面，完成校验并全部校验项通过后，单击**启动任务**。
7. 如果校验任务不通过，可以参考 [校验不通过处理方法](https://cloud.tencent.com/document/product/571/61639) 修复问题后重新发起校验任务。
8. 返回数据迁移任务列表，任务开始进入**运行中**状态。

[](id:CJWT)
## 常见问题
**1. 跨账号拉取实例列表报错：role not exist[InternalError.GetRoleError]**
请确认**跨腾讯云账号 ID**（应该为源数据库的主账号 ID）和**跨账号授权角色名称**（应该为 [授权账号](#SQZH) 步骤6中创建的角色名称）配置是否正确。

**2. 获取云数据库实例列表失败：InternalError:InternalInnerCommonError**
![](https://qcloudimg.tencent-cloud.cn/raw/48063dacddf9c2a52e21a6d5db635e8f.png)
角色中没有授权源数据库所属的腾讯云服务策略，请参考 [授权账号](#SQZH) 中的步骤5进行授权。

**3. 跨账号拉取实例列表报错：you are not authorized to perform operation (sts:AssumeRole) ，resource (qcs::cam::uin/1xx5:roleName/xxxx) has no permission**
![](https://qcloudimg.tencent-cloud.cn/raw/536938ca75067384a4374618fa27ec1c.png)
**出错原因**：您当前创建迁移任务使用的账号是子账号，并且当前子账号没有 sts:AssumeRole 权限。
**解决方法**：
- 使用主账号来创建迁移任务。
- 请求目标数据库所属的主账号持有人，参考 [授权账号](#SQZH) 对子账号授权，策略语法中的 resource，填写报错框中蓝色字段部分。
![](https://qcloudimg.tencent-cloud.cn/raw/07d125c0a11ff0a27b34dc65d5f1ab57.png)

