## 操作场景
本文介绍如何使用已有 SDK 在云函数代码中连接 [MySQL](https://cloud.tencent.com/document/product/236/5147) 数据库，并实现对数据库的插入、查询等操作。同时还支持连接 [TDSQL-C](https://cloud.tencent.com/document/product/1003/30488) 或 [TDSQL MySQL版](https://cloud.tencent.com/document/product/557/7700) 数据库，您可按需进行相应操作。



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
![](https://main.qcloudimg.com/raw/b75a1d566c8e43f435e191777064f24e.png)

### 创建安全组（可选）
可参考 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537) 为您的数据库实例添加安全组。


### 配置环境变量和私有网络
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


### 函数代码示例

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











