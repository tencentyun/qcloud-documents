## 操作场景
为了方便使用，云函数团队将 Node.js 和 Python 连接池相关代码封装为 SCF DB SDK for MySQL，请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780) 进行安装使用。通过该 SDK，您可以在云函数代码中连接 [MySQL](https://cloud.tencent.com/document/product/236/5147)、[TDSQL-C](https://cloud.tencent.com/document/product/1003/30488) 或 [TDSQL MySQL版](https://cloud.tencent.com/document/product/557/7700) 数据库，并实现对数据库的插入、查询等操作。本文介绍如何使用 SCF 连接 MySQL 数据库。

>! SCF DB SDK 主要支持 MySQL 协议的数据库，如果您需使用腾讯云 Serverless DB（支持 PostgreSQL 及 MySQL），推荐使用 [Serverless Framework 组件](https://cloud.tencent.com/document/product/583/45363)。

SCF DB SDK for MySQL 具备以下特点：
- 自动从环境变量初始化数据库客户端。
- SDK 会在全局维护一个数据库长连接，并处理连接中断后的重连。
- 云函数团队会持续关注 issue，确保获得连接即可用，不需要关注数据库连接。



## 前提条件
已注册腾讯云账号并完成实名认证。如未注册，请前往 [注册页面](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。



## 操作步骤

### 创建私有网络 VPC[](id:createVPC)
参考 [快速搭建私有网络](https://cloud.tencent.com/document/product/215/30716) 创建 VPC 和子网。

### 创建数据库实例
1. 参考 [购买方式](https://cloud.tencent.com/document/product/236/5160) 创建 MySQL。
<dx-alert infotype="explain" title="">
配置项“网络”请选择在 [创建私有网络 VPC](#createVPC) 步骤中已创建的 VPC。
</dx-alert>
2. 参考 [初始化 MySQL 数据库](https://cloud.tencent.com/document/product/236/3128) 完成初始化操作，并获取数据库帐户名称及密码。
<dx-alert infotype="explain" title="">
腾讯云原生数据库 TDSQL-C（原 CynosDB）目前已支持 Serverless 版本 MySQL，实现按需付费。详情请参见 [Serverless 服务](https://cloud.tencent.com/document/product/1003/50853)。
</dx-alert>
3. 在 “[MySQL - 实例列表](https://console.cloud.tencent.com/cdb)” 页面，选择实例 ID 进入数据库详情页面，获取该数据库的**内网地址**、**所属网络**、**内网端口**信息。如下图所示：
![](https://main.qcloudimg.com/raw/6fd6650feb37f558bfc100c7c01936c6.png)

### 创建安全组（可选）
可参考 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537) 为您的数据库实例添加安全组。



### 配置环境变量和私有网络
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的**函数服务**。
2. 单击需连接数据库的函数 ID，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**，请参考以下表格填写，如下图所示：
![](https://main.qcloudimg.com/raw/46c8b2aab4d4463dd16e1e063b318e36.png)
>!
>- 环境变量 key 格式为 `DB_{引用}_XXX`，您可通过 `mysql.database(引用).connection()` 获得已初始化的数据库连接（引用为此数据库的标识）。
>- 若您设置添加环境变量 `DB_DEFAULT` 为 `DB1`，则 `mysql.database()` 默认使用 `DB1`，否则需要指定引用 `mysql.database("DB1")`。
>- 更多关于环境变量相关信息，请参见 [环境变量](https://cloud.tencent.com/document/product/583/30228)。
>
<table align=center>
<tr>
<th>key</th>
<th>value</th>
<th>是否可选</th>
</tr>
<tr>
<td>DB_DB1_HOST</td>
<td>DB1 实例的地址。</td>
<td>否</td>
</tr>
<tr>
<td>DB_DB1_PORT</td>
<td>DB1 实例的端口。</td>
	<td>否</td>
</tr>
<tr>
<td>DB_DB1_USER</td>
<td>DB1 实例的用户名。</td>
	<td>否</td>
</tr>
<tr>
<td>DB_DB1_PASSWORD</td>
<td>DB1 实例的密码。</td>
	<td>否</td>
</tr>
<tr>
<td>DB_DB1_DATABASE</td>
<td>DB1 实例的数据库。</td>
	<td>否</td>
</tr>
<tr>
<td>DB_DEFAULT</td>
<td>本示例中为 “DB1”。</td>
<td>是</td>
</tr>
</table>
 - 开启私有网络，并选择和数据库相同的私有网络和子网。如下图所示：
![](https://main.qcloudimg.com/raw/b605a903a25988de2a148d9baac65678.png)


### 函数代码示例
#### Node.js SDK
```JavaScript
'use strict';
const database = require('scf-nodejs-serverlessdb-sdk').database;

exports.main_handler = async (event, context, callback) => {
  let pool = await database('TESTDB2').pool()
  pool.query('select * from coffee',(err,results)=>{
    console.log('db2 callback query result:',results)
  })
  // no need to release pool
 
  console.log('db2 query result:',result)
}
```
>?Node.js SDK 具体使用方法请参考 [SCF DB SDK for MySQL](https://www.npmjs.com/package/scf-nodejs-serverlessdb-sdk)。


#### Python SDK
```Python
from serverless_db_sdk import database

def main_handler(event, context):
    print('Start Serverlsess DB SDK function')

    connection = database().connection(autocommit=False)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM name')
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
```
