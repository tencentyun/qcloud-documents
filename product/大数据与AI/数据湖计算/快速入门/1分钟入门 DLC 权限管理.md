## 用户与工作组
DLC 通过对用户授权和绑定工作组授权两种方式来管理用户权限。
- 工作组：DLC 可以将一批用户绑定到工作组，并授予该组数据、引擎等资源权限，来批量管理用户权限，在同一个工作组的用户具有相同的权限。
- 用户：CAM 中的用户，包括子账号、协作者账号。
>? 当用户被赋予的权限与所在工作组权限不同时，两者权限取并集。

## 操作步骤
1. DLC 左侧导航栏选择**权限管理**。
2. 创建工作组
单击**工作组 > 添加工作组**来创建用户的工作组，创建工作组时可以选择用户进行绑定或创建一个空工作组。详细操作可参见 [用户和用户组](https://cloud.tencent.com/document/product/1342/61976)。
![](https://qcloudimg.tencent-cloud.cn/raw/5f8a3e8abe206f26f16827e805a1e1f0.png)
![](https://qcloudimg.tencent-cloud.cn/raw/0cbe16c1ce39e5809c7a5894cf351c20.png)
3. 工作组授权
创建工作组后单击列表中的**授权**操作，为工作组添加权限，包括**数据权限**和**引擎权限**。
![](https://qcloudimg.tencent-cloud.cn/raw/e9e7fb62f4712bd96a6800bbed6221b3.png)
	1. 数据权限
		- 数据目录权限：包括在数据目录下创建数据库和创建数据目录两种权限。
		- 数据库表权限：可授予库表级别的细粒度权限，包括对库，表，视图，函数的查询、编辑等权限。
![](https://qcloudimg.tencent-cloud.cn/raw/e3d7d65288e73d457620f7825b6accae.png)
	2. 引擎权限
选择数据引擎并授予使用、修改、删除等权限。
![](https://qcloudimg.tencent-cloud.cn/raw/9d95c2c504247a5603b5894901278a02.png)

4. 创建用户
添加用户并绑定工作组：单击**用户 > 添加用户**，添加新用户。选择用户类型为”普通用户“后绑定工作组并获取该工作组的所有权限，选择用户类型为 **DLC 管理员**不需要绑定工作组。
![](https://qcloudimg.tencent-cloud.cn/raw/412c6d544d3954e7f763a9ad62576741.png)
![](https://qcloudimg.tencent-cloud.cn/raw/839ebb3cb6555ed3b1520f3a3725d4ce.png)
5. 授权用户
在用户列表为用户单独进行授权，授权包含”数据权限“和”引擎权限“，同工作组权限。
![](https://qcloudimg.tencent-cloud.cn/raw/11a1edcabe9773ed546ca364aff396e1.png)
更多详细操作参见 [子账号权限管理](https://cloud.tencent.com/document/product/1342/61976)。
