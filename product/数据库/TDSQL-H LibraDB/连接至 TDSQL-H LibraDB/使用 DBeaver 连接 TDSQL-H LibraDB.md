TDSQL-H LibraDB 支持您通过数据库管理工具 DBeaver 访问实例，进行数据管理操作。本文为您介绍如何通过 DBeaver 的 ClickHouse (Legacy) 驱动连接 TDSQL-H LibraDB 实例并管理数据。

## 背景信息

DBeaver 是一款免费的多平台数据库工具，适用于开发人员、数据库管理员、分析师和所有需要使用数据库的人员。更多 DBeaver 信息，请参见 [DBeaver](https://dbeaver.io/)。

## 前提条件

- 已 [创建 TDSQL-H LibraDB 实例](https://cloud.tencent.com/document/product/1488/63546)。
- 已获取访问 TDSQL-H LibraDB 实例的帐号和密码。
- 获取 DBeaver 连接 TDSQL-H LibraDB 实例时的主机地址。访问 TDSQL-H LibraDB 实例方式不同，获取的主机地址不同，请根据实际选择。
  - 若通过搭建代理使用外网访问 TDSQL-H LibraDB 实例，请获取搭建代理时使用的 **CVM 云服务器的公网 IP**，并确保外网连接使用的 CVM 云服务器安全组已添加 TCP:8123、TCP:9000 协议端口。本文中的操作以此方式为例。
    搭建代理的具体操作，请参见 [连接实例分析引擎](https://cloud.tencent.com/document/product/1488/63547) 中的**外网连接**相关内容。
  - 若使用镜像为 Windows 的 CVM 云服务器，安装 DBeaver 并连接 TDSQL-H LibraDB 实例，请获取 **TDSQL-H LibraDB 实例的内网 IP**。
    镜像为 Windows 的 CVM 云服务器与 TDSQL-H LibraDB 实例必须为相同的 VPC，并确保 CVM 云服务器安全组已添加 TCP:8123、TCP:9000 协议端口。
- 已下载并安装 [DBeaver](https://dbeaver.io/download/)。更多安装 DBeaver 操作，请参见 [Install](https://dbeaver.io/download/)。
  推荐使用 DBeaver 版本 DBeaver Community 22.1.2，其他版本可能存在兼容性问题。本文中的 DBeaver 示例版本为 DBeaver Community 22.1.2。

## 步骤1：连接 DBeaver 和 TDSQL-H LibraDB 实例

1. 启动 DBeaver，进入 DBeaver 界面。
2. 在顶部菜单栏单击![](https://qcloudimg.tencent-cloud.cn/raw/069ebc343aa0241b09d360a12758ee11.png)图标后，在**选择您的数据库**对话框选择 **SQL > ClickHouse (Legacy)**，单击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4f6ff50d068e97e445944c5e8f73cfa7.png)
3. 在**通用 JDBC 连接设置**对话框中，单击**编辑驱动设置**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/0f666ab6c36560675a1f10c090d43488.png)
4. 在**编辑驱动 'ClickHouse (Legacy)'** 对话框的**库**页签，单击**下载/更新**，在**下载驱动文件**对话框中单击**下载**，待下载完成后，在**编辑驱动 'ClickHouse (Legacy)'** 对话框单击**确定**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d9246690af70b69fbd552fcc65ebb1d8.png)
5. 在**通用 JDBC 连接设置**对话框的**主要**页签中，填写以下信息，并单击**测试连接**。
   - 主机：填写前提条件已获取的 CVM 云服务器公网 IP。
   - 用户名、密码：填写前提条件已获取的访问 TDSQL-H LibraDB 实例的帐号和密码。
   - 其他参数：保持默认。
   ![](https://qcloudimg.tencent-cloud.cn/raw/79b6e92105f4847302f172fa96feba64.png)
6. 连接成功后依次单击**确定**、**完成**，成功连接 TDSQL-H LibraDB 实例。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c50f1348162cdc4874542110b314ced3.png)

## 步骤2：使用 DBeaver 查询及分析数据

连接 DBeaver 和 TDSQL-H LibraDB 实例后，您可以在 DBeaver 左侧查看到新建的 TDSQL-H LibraDB 实例连接，并通过 SQL 管理 TDSQL-H LibraDB 实例。

可通过 DBeaver 执行的数据库操作示例如下。更多操作，请参见 [DBeaver 帮助](https://github.com/dbeaver/dbeaver/wiki)。

- 查看所有数据库及表
  在创建的 TDSQL-H LibraDB 实例连接下查看所有库表信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/9c034282137229c834067ff89d8ebed4.png)
- 查看表结构
  在创建的 TDSQL-H LibraDB 实例连接下，在目标表处单击右键，选择**查看 表**，即可查看表结构信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/af8bf1b218b3e0d061680a1cbc3e4df8.png)
  ![](https://qcloudimg.tencent-cloud.cn/raw/14035ceeaac26e234f03a0dc06ce1da3.png)
- 查看表数据
  在创建的 TDSQL-H LibraDB 实例连接下，在目标表处单击右键，选择**查看 表**后，在**数据**页签即可查看表数据信息。
  ![](https://qcloudimg.tencent-cloud.cn/raw/a4707c2e9caa21247b63f2982cb7b933.png)

## 步骤3：使用 DBeaver 执行 SQL

连接 DBeaver 和 TDSQL-H LibraDB 实例后，您可以在 DBeaver 左侧查看到新建的 TDSQL-H LibraDB 实例连接，并可通过 SQL 编辑器执行 SQL。

可通过 SQL 编辑器执行 SQL 语句的操作示例如下。更多执行 SQL 操作，请参见 [SQL 编辑器](https://github.com/dbeaver/dbeaver/wiki/SQL-Editor)。

1. 在创建的 TDSQL-H LibraDB 实例连接下，在界面顶部选择 **SQL 编辑器 > 新建 SQL 编辑器**。
  ![](https://qcloudimg.tencent-cloud.cn/raw/4d22eb276f4b01885eceaaeed64b9478.png)
2. 在 **SQL 编辑器**中输入 SQL 语句，选中需要执行的语句，选择**执行 > 执行 SQL 语句**。
  也可直接在 **SQL 编辑器**窗口左侧的主工具栏单击<img src="https://qcloudimg.tencent-cloud.cn/raw/4f426d89fd039593fc1d94726e705038.png" style="zoom:50%;" />执行SQL语句。
  ![](https://qcloudimg.tencent-cloud.cn/raw/e84b4139e9b068a934b305f8b1e5c66f.png)
  执行结果如下：
  ![](https://qcloudimg.tencent-cloud.cn/raw/8a6f9bd94b3f13775137007f55baf7d3.png)

 
