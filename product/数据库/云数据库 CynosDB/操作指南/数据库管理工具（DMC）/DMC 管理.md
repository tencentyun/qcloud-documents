本文为您介绍 DMC 数据库管理控制台的新建库表、库管理、实例会话、数据导入导出、表数据可视化编辑等功能。

## 新建库表
1. 登录数据库管理控制台。
 - 直接登录 [DMC 控制台](https://dms.cloud.tencent.com/#/login)。
 - 或在 [TDSQL-C MySQL 版](https://console.cloud.tencent.com/cynosdb/mysql#/) 集群列表单击**操作**列的**登录**（列表视图）。
 - 或在 [TDSQL-C MySQL 版](https://console.cloud.tencent.com/cynosdb/mysql#/) 集群列表下单击目标集群，进入集群管理页，在集群管理页右上方单击**登录**（页签视图）。
2. 在导航栏选择**新建** > **新建库** > **新建数据库**，或者**新建** > **新建表**。
![](https://qcloudimg.tencent-cloud.cn/raw/634c1ad8a604b370b4e4dc0909896097.png)
3. 在弹出的对话框，对新建的库或表进行相关配置。
 - 新建库对话框：
 ![](https://qcloudimg.tencent-cloud.cn/raw/7d9342300c29d9af1701e0f88528115d.png)
 - 新建表对话框：
 ![](https://qcloudimg.tencent-cloud.cn/raw/c76c28cca3eb0d922625dc8b4ab61547.png)
 
>?字符集、排序规则介绍可参见 [官方文档](https://dev.mysql.com/doc/)。

## 库管理
登录 [DMC 控制台](https://dms.cloud.tencent.com/#/login)，在导航栏单击**库管理**，进入数据库管理页面，用户可新建、编辑、删除数据库。
![](https://qcloudimg.tencent-cloud.cn/raw/10a4125bf6ed9ad50b85d76ea793307d.png)

## 实例会话
登录 [DMC 控制台](https://dms.cloud.tencent.com/#/login)，在导航栏单击**实例会话**，进入实例会话页面，用户可查看当前数据库中所有实例的会话详细信息，以及按照会话概览、用户、访问来源和数据库四个不同维度的信息展示。
DMC 提供 kill 会话的功能，方便用户对会话进行管理。
![](https://qcloudimg.tencent-cloud.cn/raw/230b16a5960fa1bc8fe15f524c01b071.png)

## SQL 窗口
登录 [DMC 控制台](https://dms.cloud.tencent.com/#/login)，单击顶部导航中的 **SQL 窗口**，或者左侧栏表格操作菜单中的 SQL 操作进入 SQL 窗口页面。SQL 窗口支持如下功能：
- SQL 命令执行及结果查看
- SQL 格式优化
- 查看 SQL 命令执行计划
- 常用 SQL 保存
- 模板 SQL
- SQL 结果导出

![](https://qcloudimg.tencent-cloud.cn/raw/b28a436b0fe43f8e9ac29152d937cfec.png)

## 导入导出
登录 [DMC 控制台](https://dms.cloud.tencent.com/#/login)，在导航栏选择**导入导出** > **数据导入**或**数据导出**，可对数据库进行数据导入导出操作。
![](https://qcloudimg.tencent-cloud.cn/raw/45091f6747778b212e090b34426a1fd8.png)

## 表数据可视化编辑
DMC for TDSQL-C MySQL 版增加了对数据增删改的支持。用户可在左侧栏单击数据表，对表数据进行批量的增、删、改操作，修改完成后，在快捷操作栏单击确定预览本次修改的 SQL 语句，二次确认后将批量执行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/a17e87345cf712fa22821a91030206fe.png)

