本文主要介绍通过 DTS 数据迁移功能实现从其他账号腾讯云数据库实例迁移数据至本账号下云数据库实例。

## 准备工作

在源端云数据库实例所属腾讯云账号中配置，将目标实例所属云账号作为授信云账号，允许通过数据传输服务访问源实例所属云账号的相关云资源。完成权限授权后，即可配置跨账号云数据库迁移任务。

### 授权账号

1. 使用源端云数据库实例所属的腾讯云账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/role)，进入角色管理页面，单击【新建角色】。
2. 在选择角色载体页面，选择【腾讯云账号】方式。
   ![](https://main.qcloudimg.com/raw/937dad52c8b9c9dee558a22f7ed20e5c.png)
3. 在输入角色载体信息页面，配置相关信息，单击【下一步】。

 - 云账号类型：选择【其他主账号】。
 - 账号 ID：填入目标端所属的腾讯云账号 ID，账号 ID 可在目标实例所属账号的 [账号信息](https://console.cloud.tencent.com/developer) 页面查看。

   - 如果目标实例所属账号是子账号，请填写其主账号ID。
 - 外部ID：可依据情况，选择性开启。
    - 注意：如果使用了外部ID，请用户自行记录和保存该ID。无法通过DTS服务查询到该ID。

  ![](https://main.qcloudimg.com/raw/3892938446a46262f55e471dcc8516ae.png)

4. 在选择策略输入框中，输入 QcloudDTSReadOnlyAccess，选中 【QcloudDTSReadOnlyAccess】预设策略，单击【下一步】。
   ![](https://main.qcloudimg.com/raw/ee4a145a7156e5823573951e0bdf0f56.png)
5. 在审阅页面，设置角色名称，单击【完成】后该角色创建完成。此时即完成了对跨账号执行迁移的授权。

  -  需要注意的是，角色名称不要有下划线 “_”。
     ![](https://main.qcloudimg.com/raw/1e1a0d270955967785c6a4ef9f50ae48.png)

### 创建迁移任务
使用目标实例账号，购买一个新的迁移任务，并进入配置页面。根据您的需要选择不同的数据库做迁移。下面以MySQL到MySQL的迁移举例说明。
<img src="https://main.qcloudimg.com/raw/359252c69a0d08f6f21d0fac81d837bf.png" style="zoom: 50%;" />
如图所示，接入类型选择云数据库后，页面会有是否跨账号的选项，点击【跨账号】按钮后补充跨账号相关的参数。跨账号有以下参数需要配置：

- 跨腾讯云账号ID。 这个参数是指源库所属的主账号ID。
- 跨账号授权角色名称。即前文操作中创建的“角色名称”。您可以通过[角色](https://cloud.tencent.com/document/product/598/19420)以及[跨账号角色](https://cloud.tencent.com/document/product/1312/48171)文档 了解更多关于角色的概念。
- 外部角色ID，这个选项可选。这个参数可以通过前文获得。您可以通过[角色](https://cloud.tencent.com/document/product/598/19420)以及[跨账号角色](https://cloud.tencent.com/document/product/1312/48171)文档 了解更多关于角色的概念。

完成上述配置后，选择对应的【所属地域】，即可获取到跨账号下的实例列表，作为迁移源。


### 常见问题
问题一、跨账号拉取实例列表报错：role not exist[InternalError.GetRoleError]

请确认 跨腾讯云账号ID 这个字段填写是否正确，并确认该账号是源库的主账号ID。



问题二、跨账号拉取实例列表报错：you are not authorized to perform operation (sts:AssumeRole) ，resource (qcs::cam::uin/12345:roleName/xxxx) has no permission
<img src="https://main.qcloudimg.com/raw/34a3897aaf15114fc0d3135c4cd3c031.png" style="zoom:50%;" />
出错原因： 您当前创建迁移任务使用的是子账号，并且当前子账号没有sts:AssumeRole权限。

解决方法：

1）使用主账号来创建迁移任务。

2）请求当前主账号持有人，按照下面操作步骤为子账号授权，子账号授权角色文档[链接](https://cloud.tencent.com/document/product/598/19422)。



使用主账号登陆腾讯云控制台，进入[策略页面](https://console.cloud.tencent.com/cam/policy)，点击【新建自定义策略】。并选择【按策略语法创建】。

<img src="https://main.qcloudimg.com/raw/d41b162b1cbf5934020c6c0df89c6351.png" style="zoom:50%;" />

选择【空白模板】，并且点击【下一步】。
<img src="https://main.qcloudimg.com/raw/aea1456bbd3d312a45d69cbd37d440e2.png" style="zoom:50%;" />
创建一个策略，策略的名称以及描述可以根据自己的需求填写，策略语法按照下面的方式来填写。

```

{
 "version": "2.0",
 "statement": [
    {
        "effect": "allow",
        "action": ["name/sts:AssumeRole"],
        "resource": ["qcs::cam::uin/1234:roleName/theRole"]
    }
 ]
}
```
其中语法中的resource，填写报错框中蓝色字段部分。
![](https://main.qcloudimg.com/raw/d978acb50ab95f7b8091854f8b8e17f7.png)
点击【完成】后返回到策略的列表页。
![](https://main.qcloudimg.com/raw/9dde503de5f0091d151c734e6f4c3feb.png)
在列表页中，点击【关联用户/组】按钮，选择创建迁移任务的子账号，点击【确定】，如下图所示。
![](https://main.qcloudimg.com/raw/77c33dd057c17b20242e8aae70406dc3.png)
授权完成后，就可以顺利拉取到实例列表了。

