
本文主要为您介绍 DMC 控制台的新建库表、库管理、实例监控、实例会话、表数据可视化编辑等功能。

## 新建库表
1. 登录 [DMC 控制台](https://bj-dmc.cloud.tencent.com/v2/qcloudLogin/login)，在导航栏选择**新建** > **新建库** > **新建数据库**或**新建** > **新建表**。
![](https://qcloudimg.tencent-cloud.cn/raw/30357c01321cbc26e4042958ae87563c.png)
2. 在弹出的对话框，对新建的库表进行相关配置。
>?字符集、排序规则介绍可参见 [MySQL 官方文档](https://dev.mysql.com/doc/)。
>
 - 新建库对话框：
![](https://main.qcloudimg.com/raw/1e235d6d79732444adaeb6efb6bf7dfc.png)
 - 新建表对话框：
![](https://main.qcloudimg.com/raw/6815a20c6e92943b229cfe5d18ed0c46.png)

## 库管理
登录 [DMC 控制台](https://bj-dmc.cloud.tencent.com/v2/qcloudLogin/login)，在导航栏单击**库管理**，进入数据库管理页面，用户可新建、编辑、删除数据库。
![](https://qcloudimg.tencent-cloud.cn/raw/b34bb60e8c78a93d9d1d738e4e5cedc4.png)

## 实例会话
登录 [DMC 控制台](https://bj-dmc.cloud.tencent.com/v2/qcloudLogin/login)，在导航栏单击**实例会话**，进入实例会话页面，用户可查看当前数据库中所有实例的会话详细信息，以及按照会话概览、用户、访问来源和数据库四个不同维度的信息展示。
DMC 提供 kill 会话的功能，方便用户对会话进行管理。
![](https://main.qcloudimg.com/raw/26f08e7b47be3ba94842372d40f36961.png)

## SQL 窗口
登录 [DMC 控制台](https://bj-dmc.cloud.tencent.com/v2/qcloudLogin/login)，单击顶部导航中的**SQL 窗口**，或者左侧栏表格**操作**菜单中的**SQL 操作**进入SQL 窗口页面。SQL 窗口支持如下功能：
- SQL 命令执行及结果查看
- SQL 格式优化
- 查看 SQL 命令执行计划
- 常用 SQL 保存
- 模板 SQL
- SQL 结果导出
![](https://qcloudimg.tencent-cloud.cn/raw/4336273188ad65cb1875be86ec364e4b.png)

## 数据管理
登录 [DMC 控制台](https://bj-dmc.cloud.tencent.com/v2/qcloudLogin/login)，在导航栏选择**导入导出**，然后在下方可选择数据库进行数据导入或数据导出。
![](https://qcloudimg.tencent-cloud.cn/raw/6db820b43fefd1dcec79f4b52da40076.png)

## 表数据可视化编辑
DMC for MySQL 增加了对数据增删改的支持。用户可在左侧栏单击**数据表**，对表数据进行批量的增、删、改操作，修改完成后，在**快捷操作**栏单击**确定**预览本次修改的 SQL 语句，二次确认后将批量执行修改。
![](https://main.qcloudimg.com/raw/4488c0191fbbd19b221af38a0daffc76.png)
