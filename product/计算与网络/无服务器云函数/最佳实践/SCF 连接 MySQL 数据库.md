## 云函数连接 MySQL 数据库

### 操作场景
通过云函数团队提供的 SDK 或者连接池，您可以在云函数代码中连接 [MySQL](https://cloud.tencent.com/document/product/236/5160) 数据库，实现对数据库的插入、查询等操作。此方法还适用于连接  [CynosDB](https://cloud.tencent.com/document/product/1003/30505) 或 [TDSQL](https://cloud.tencent.com/document/product/557/10236) 数据库，本文档将具体介绍连接 MySQL 数据库的方法。

### 前提条件
1. 已注册腾讯云账号并完成实名认证。
2. 根据您实际使用环境，已[购买云数据库 MySQL](https://buy.cloud.tencent.com/cdb?regionId=8&zoneId=800003&engineVersion=5.7&cdbType=Z3&memory=8000&cpu=4&volume=200&protectMode=0&netType=2)。

### 公共配置

#### 创建私有网络 VPC
1. 登录[私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 参阅[快速搭建私有网络](https://cloud.tencent.com/document/product/215/30716)创建 VPC 和子网。

#### 创建数据库实例
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，点击创建实例
2. 根据您的实际使用环境，购买对应的 MySQL 数据库，网络填入您刚创建的 VPC 信息
3. 购买成功后，对实例进行初始化，创建账户名称与密码
4. 在数据库详情页，获取该数据库的**内网地址**、**所属网络**、**内网端口**信息。如下图所示：
![](https://main.qcloudimg.com/raw/bb4109d666fca0405d968293c879e72b.png)

#### 创建安全组（可选）
参阅[云数据库安全组](https://cloud.tencent.com/document/product/236/9537), 为您的数据库实例添加安全组。

### 函数配置

1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的【函数服务】。
2. 单击需连接数据库的函数名，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**参考以下表格填写，以 MySQL 实例下名为 demo 的数据库为例，。如下图所示：
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
![](https://main.qcloudimg.com/raw/1e0489ad2ec96fe2f239e823363a7989.png)

### 函数编写


#### Python

Python 使用 **pymysql** 依赖包进行连接，云函数环境已为您内置 pymysql 依赖包。使用 Python 操作 MySQL 实例，示例代码如下：

```
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
Node.js 支持使用连接池进行连接，连接池具备自动重连功能，可有效避免因云函数底层或者数据库释放连接，造成连接不可用的情况，您需要先安装 **mysql2** 依赖包，参考[依赖安装](https://cloud.tencent.com/document/product/583/39780)。

```
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
使用 PHP 进行访问，需要使用 **pdo_mysql** 依赖包。
```
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
1. 安装以下依赖，参考[依赖安装](https://cloud.tencent.com/document/product/583/39780)。
```
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
2. 使用 Hikari 连接池进行连接

```
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

### 使用 SCF DB SDK for MySQL 连接数据库
为了方便使用，云函数团队将上述 Node.js 和 Python 连接池最佳实践封装成了 SCF DB SDK for MySQL，请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780) 进行安装使用。支持 MySQL，CynosDB 及 TDSQL 三种 MySQL 协议的数据库。
>!SCF DB SDK 主要支持 MySQL 协议的数据库，如果您需使用腾讯云 Serverless DB（支持 PostgreSQL 及 NoSQL），推荐使用 [Serverless Framework 组件](https://cloud.tencent.com/document/product/583/45363)。

SCF DB SDK for MySQL 具备以下特点：
- 自动从环境变量初始化数据库客户端。
- SDK 会在全局维护一个数据库长连接，并处理连接中断后的重连。
- 云函数团队会持续关注 issue，确保获得连接即可用，不需要关注数据库连接。

#### 配置环境变量和私有网络
若您使用 SCF DB SDK for MySQL，请按照以下步骤进行配置：
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的【函数服务】。
2. 单击需连接数据库的函数 ID，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**，请参考以下表格填写，如下图所示：
![](https://main.qcloudimg.com/raw/46c8b2aab4d4463dd16e1e063b318e36.png)
>!
>- 环境变量 key 格式为`DB_{引用}_XXX`，您可通过 `mysql.database(引用).connection()` 获得已初始化的数据库连接（引用为此数据库的标识）。
>- 若您设置添加环境变量 `DB_DEFAULT` 为 `DB1`，则 `mysql.database()` 默认使用 `DB1`，否则需要指定引用 `mysql.database("DB1")`。
>- 更多关于环境变量相关信息，请参见 [环境变量](https://cloud.tencent.com/document/product/583/30228)。


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
![](https://main.qcloudimg.com/raw/1e0489ad2ec96fe2f239e823363a7989.png)

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

