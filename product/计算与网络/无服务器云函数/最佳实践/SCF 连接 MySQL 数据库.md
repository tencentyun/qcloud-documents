## 操作场景
通过云函数团队提供的 SDK 或者连接池，您可以在云函数代码中连接 [MySQL](https://cloud.tencent.com/document/product/236/5147)、[CynosDB](https://cloud.tencent.com/document/product/1003/30488) 或 [TDSQL](https://cloud.tencent.com/document/product/557/7700) 数据库，并实现对数据库的插入、查询等操作。本文介绍如何使用 SCF 连接 MySQL 数据库。



## 前提条件
已注册腾讯云账号并完成实名认证。如未注册，请前往 [注册页面](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。



## 操作步骤

### 创建私有网络 VPC[](id:createVPC)
参考 [快速搭建私有网络](https://cloud.tencent.com/document/product/215/30716) 创建 VPC 和子网。

### 创建数据库实例
1. 参考 [购买方式](http://tapd.oa.com/pro/markdown_wikis/show/#1210114221000482979) 创建 MySQL。
>?配置项“网络”请选择在 [创建私有网络 VPC](#createVPC) 步骤中已创建的 VPC。
>
2. 参考 [初始化 MySQL 数据库](https://cloud.tencent.com/document/product/236/3128) 完成初始化操作，并获取数据库帐户名称及密码。
3. 在 “[MySQL - 实例列表](https://console.cloud.tencent.com/cdb)” 页面，选择实例 ID 进入数据库详情页面，获取该数据库的**内网地址**、**所属网络**、**内网端口**信息。如下图所示：
![](https://main.qcloudimg.com/raw/bb4109d666fca0405d968293c879e72b.png)

### 创建安全组（可选）
可参考 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537) 为您的数据库实例添加安全组。







>?本文提供 [使用 SDK 连接数据库](#SDK) 及 [使用 SCF DB SDK for MySQL 连接数据库](#SCFSDK) 两种方式连接 MySQL 数据库，您可按需进行选择。

### 使用 SDK 连接数据库[](id:SDK)

#### 配置环境变量和私有网络
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的**函数服务**。
2. 单击需连接数据库的函数名，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**，并参考以下表格填写。如下图所示：
![](https://main.qcloudimg.com/raw/94a17932ae2a1968d6ab19be4aa3fb91.png)
<table align=center>
<tr>
<th>key</th>
<th>value</th>
</tr>
<tr>
<td>DB_PASSWORD</td>
<td>数据库密码</td>
</tr>
<tr>
<td>DB_USER</td>
<td>数据库用户名</td>
</tr>
<tr>
<td>DB_HOST</td>
<td>数据库地址</td>
</tr>
<tr>
<td>DB_PORT</td>
<td>数据库端口</td>
</tr>
<tr>
<td>DB_DATABASE</td>
<td>数据库名</code></td>
</tr>
</table>
 - 开启私有网络，并选择和数据库相同的私有网络和子网。如下图所示：
![](https://main.qcloudimg.com/raw/b605a903a25988de2a148d9baac65678.png)


#### 函数代码示例

#### Python
Python 可使用云函数环境已经内置的 **pymysql** 依赖包进行数据库连接。示例代码如下：
```python
# -*- coding: utf8 -*-
from os import getenv

import pymysql
from pymysql.err import OperationalError

mysql_conn = None

def __get_cursor():
    try:
        return mysql_conn.cursor()
    except OperationalError:
        mysql_conn.ping(reconnect=True)
        return mysql_conn.cursor()

def main_handler(event, context):
    global mysql_conn
    if not mysql_conn:
        mysql_conn = pymysql.connect(
        host        = getenv('DB_HOST', '<YOUR DB HOST>'),
        user        = getenv('DB_USER','<YOUR DB USER>'),
        password    = getenv('DB_PASSWORD','<YOUR DB PASSWORD>'),
        db          = getenv('DB_DATABASE','<YOUR DB DATABASE>'),
        port        = int(getenv('DB_PORT','<YOUR DB PORT>')),
        charset     = 'utf8mb4',
        autocommit  = True
        )
    
    with __get_cursor() as cursor:
        cursor.execute('select * from employee')
        myresult = cursor.fetchall()
        print(myresult)
        for x in myresult:
            print(x)
```

#### Node.js
Node.js 支持使用连接池进行连接，连接池具备自动重连功能，可有效避免因云函数底层或者数据库释放连接造成的连接不可用情况。示例代码如下：
>?使用连接池前需先安装 **mysql2** 依赖包，详情请参见 [依赖安装](https://cloud.tencent.com/document/product/583/39780)。
>
```nodejs
'use strict';

const DB_HOST       = process.env[`DB_HOST`]
const DB_PORT       = process.env[`DB_PORT`]
const DB_DATABASE   = process.env[`DB_DATABASE`]
const DB_USER       = process.env[`DB_USER`]
const DB_PASSWORD   = process.env[`DB_PASSWORD`]

const promisePool = require('mysql2').createPool({
  host              : DB_HOST,
  user              : DB_USER,
  port              : DB_PORT,
  password          : DB_PASSWORD,
  database          : DB_DATABASE,
  connectionLimit   : 1
}).promise();

exports.main_handler = async (event, context, callback) => {
  let result = await promisePool.query('select * from employee');
  console.log(result);
}
```

#### PHP
PHP 可使用 **pdo_mysql** 依赖包进行数据连接。示例代码如下：
```php
<?php
function handler($event, $context) {
try{
  $pdo = new PDO('mysql:host= getenv("DB_HOST");dbname= getenv("DB_DATABASE"),getenv("DB_USER"),getenv("DB_PASSWORD")');
  $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}catch(PDOException $e){
  echo '数据库连接失败: '.$e->getMessage();
  exit;
}
}
```

#### JAVA
1. 请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780#java-.E8.BF.90.E8.A1.8C.E6.97.B6)，安装以下依赖。

```xml
<dependencies>
    <dependency>
        <groupId>com.tencentcloudapi</groupId>
        <artifactId>scf-java-events</artifactId>
        <version>0.0.2</version>
    </dependency>
    <dependency>
        <groupId>com.zaxxer</groupId>
        <artifactId>HikariCP</artifactId>
        <version>3.2.0</version>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>8.0.11</version>
    </dependency>
</dependencies>
```
2. 使用 Hikari 连接池进行连接，示例代码如下：

```java
package example;

import com.qcloud.scf.runtime.Context;
import com.qcloud.services.scf.runtime.events.APIGatewayProxyRequestEvent;
import com.qcloud.services.scf.runtime.events.APIGatewayProxyResponseEvent;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

public class Http {
    private DataSource dataSource;

    public Http() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:mysql://" + System.getenv("DB_HOST") + ":"+ System.getenv("DB_PORT") + "/" + System.getenv("DB_DATABASE"));
        config.setUsername(System.getenv("DB_USER"));
        config.setPassword(System.getenv("DB_PASSWORD"));
        config.setDriverClassName("com.mysql.jdbc.Driver");
        config.setMaximumPoolSize(1);
        dataSource = new HikariDataSource(config);
    }

    public String mainHandler(APIGatewayProxyRequestEvent requestEvent, Context context) {
        System.out.println("start main handler");
        System.out.println("requestEvent: " + requestEvent);
        System.out.println("context: " + context);

        try (Connection conn = dataSource.getConnection(); PreparedStatement ps = conn.prepareStatement("SELECT * FROM employee")) {
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                System.out.println(rs.getInt("id"));
                System.out.println(rs.getString("first_name"));
                System.out.println(rs.getString("last_name"));
                System.out.println(rs.getString("address"));
                System.out.println(rs.getString("city"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        APIGatewayProxyResponseEvent apiGatewayProxyResponseEvent = new APIGatewayProxyResponseEvent();
        apiGatewayProxyResponseEvent.setBody("API GW Test Success");
        apiGatewayProxyResponseEvent.setIsBase64Encoded(false);
        apiGatewayProxyResponseEvent.setStatusCode(200);

        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "text");
        headers.put("Access-Control-Allow-Origin", "*");
        apiGatewayProxyResponseEvent.setHeaders(headers);

        return apiGatewayProxyResponseEvent.toString();
    }
}
```



### 使用 SCF DB SDK for MySQL 连接数据库[](id:SCFSDK)
为了方便使用，云函数团队将 Node.js 和 Python 连接池最佳实践封装成了 SCF DB SDK for MySQL，请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780) 进行安装使用。支持 MySQL，CynosDB 及 TDSQL 三种 MySQL 协议的数据库。
>!SCF DB SDK 主要支持 MySQL 协议的数据库，如果您需使用腾讯云 Serverless DB（支持 PostgreSQL 及 NoSQL），推荐使用 [Serverless Framework 组件](https://cloud.tencent.com/document/product/583/45363)。

SCF DB SDK for MySQL 具备以下特点：
- 自动从环境变量初始化数据库客户端。
- SDK 会在全局维护一个数据库长连接，并处理连接中断后的重连。
- 云函数团队会持续关注 issue，确保获得连接即可用，不需要关注数据库连接。

#### 配置环境变量和私有网络
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


#### 函数代码示例
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







