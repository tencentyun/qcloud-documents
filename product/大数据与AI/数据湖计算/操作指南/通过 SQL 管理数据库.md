DLC 的数据库是 DLC 数据表的逻辑分组。数据湖计算 DLC 目前支持用户通过查询分析中的 SQL 编辑器执行 DDL 语句对数据库进行创建、查看基本信息和删除操作。
## 创建数据库
1. 登录 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务所在区域，登录用户需要有创建数据库的权限。
2. 进入查询分析页，鼠标悬停菜单栏的![](https://main.qcloudimg.com/raw/426bfc0a281aef830bd68a64f698f9a2.png)图标，单击**新建数据库**，配置数据库信息。
![](https://qcloudimg.tencent-cloud.cn/raw/d144cc61c3b9fccc0ee69c96feed00bf.png)
3. 在新建数据库页面，输入数据库名称、数据库描述信息，单击**确定**，DLC 自动生成创建数据库的 SQL 语句。
![](https://qcloudimg.tencent-cloud.cn/raw/7a34de46779a9255b494d624385b032b.png)
- 数据库名称：全局唯一，支持英文大小写、数字、“_”，不允许数字开头，最多128个字符。
- 描述信息：支持中英文，最多2048个字符。
4. 选择计算引擎，单击**运行**按钮执行创建数据库的 SQL 语句，完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/b5f4ed2c66014e91df3ecb53acd5ff10.png)

## 查询数据库基本信息
1. 登录 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务所在区域，登录用户需要有数据库的查看权限。
2. 进入查询分析页，鼠标悬停到需要查看信息的**数据库行**，单击![img](https://main.qcloudimg.com/raw/b11192b7791016669333f5321cc6825e.png)图标，在下拉菜单中单击**基本信息**，可以查看对应数据库的基本信息。
![](https://qcloudimg.tencent-cloud.cn/raw/6ebd9825600615b60d7d9eb7968f264c.png)
![](https://qcloudimg.tencent-cloud.cn/raw/014cb67fd16a2262768ba56bdd713ff8.png)

## 删除数据库
1. 登录 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务所在区域，登录用户需要有数据库的删除权限。
2. 进入查询分析页，鼠标悬停到需要查看信息的**数据库行**，单击![img](https://main.qcloudimg.com/raw/b11192b7791016669333f5321cc6825e.png)图标，在下拉菜单中单击**删除数据库**，单击**确认**后即可对数据库进行删除。
![](https://qcloudimg.tencent-cloud.cn/raw/327d63366232c1573a37f372e9949861.png)

>!
>- 删除 DLC 的托管存储下的数据库时，将无法恢复，请谨慎操作。
>- 删除非 DLC 托管存储的数据库，仅会删除 DLC 中存储的元数据信息，不会影响数据源文件。

## 系统约束
- 一个主账户最多可以创建100个数据库。
- 数据库名称在同一个主账号下必须全局唯一。
- 数据库的名称不区分大小写，仅支持英文字符、数字和下划线“_”。
- 数据库名称不可以数字开头。
