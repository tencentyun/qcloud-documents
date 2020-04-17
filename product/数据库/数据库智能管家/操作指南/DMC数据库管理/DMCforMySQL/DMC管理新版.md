本文主要为您介绍 DMC 新版控制台的新建库表、实例会话管理、SQL 窗口、表数据可视化编辑等功能。
>?如需使用数据库实时监控、InnoDB 锁等待管理等功能，可在 DMC 导航栏右上角单击【返回旧版】，可前往旧版 DMC 控制台。

## 新建库表
1. 登录 [DMC 控制台](https://bj-dmc.cloud.tencent.com/v2/qcloudLogin/login)，在导航栏选择【新建】>【新建库】>【新增数据库】或【新建】>【新建表】。
![](https://main.qcloudimg.com/raw/133ef0ed2eb8fee8c9262ea525782ee5.png)
2. 在弹出的对话框中，用户可以对新建的库表进行配置，配置完成后单击【提交】即可。
>?字符集、排序规则介绍可参见 [MySQL 官方文档](https://dev.mysql.com/doc/)。
>
 - 新建库对话框：
![](https://main.qcloudimg.com/raw/258605b4ac20f2136672bab0381e0f3f.png)
 - 新建表对话框：
![](https://main.qcloudimg.com/raw/d2aec4106f019ff9d088be7c27737330.png)

## 实例会话管理
在导航栏单击【实例会话】进入实例会话管理页，用户可查看当前数据库中所有实例的会话详细信息，以及按照会话概览、用户、访问来源和数据库四个不同维度的信息展示。
DMC 提供 kill 会话的功能，方便用户对会话进行管理。
![](https://main.qcloudimg.com/raw/dd87caaefb78386484ebb58bfdbdc6e4.png)

## SQL 窗口
用户可以单击顶部导航中的【SQL 窗口】，或者左侧栏表格“操作”菜单中的【SQL 操作】进入。SQL 窗口支持如下功能：
- SQL 命令执行及结果查看
- SQL 格式优化
- 查看 SQL 命令执行计划
- 常用 SQL 保存
- 模板 SQL
- SQL 结果导出
![](https://main.qcloudimg.com/raw/feca011fc52d88d5ab989b2453a04c0e.png)

## 表数据可视化编辑
新版 DMC for MySQL 增加了对数据增删改的支持。用户可在左侧栏单击“数据表”，对表数据进行批量的增、删、改操作，修改完成后，在“快捷操作”栏单击【确定】预览本次修改的 SQL 语句，二次确认后将批量执行修改。
![](https://main.qcloudimg.com/raw/d0d9b40bc3a6344c4259f6131bc3179a.png)
