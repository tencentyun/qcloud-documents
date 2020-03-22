## 操作场景
如果您需要在云函数中使用关系型数据库，您可使用连接池或云函数团队提供的 SDK 来连接关系型数据库。连接池具备自动重连功能，可有效避免因云函数底层或者数据库释放连接，造成连接不可用的情况。

## 注意事项
由于云函数单实例同时处理的请求数均为1， 详情请参见 [函数并发量](https://cloud.tencent.com/document/product/583/9694#.E5.87.BD.E6.95.B0.E5.B9.B6.E5.8F.91.E9.87.8F)。以及为了防止连接数设置过大导致高并发下数据库连接耗尽，在使用连接池时，建议将最大连接数设置为1。

## 前提条件
已创建数据库。
>?本文档提供了 SCF 连接 [MySQL](https://cloud.tencent.com/document/product/236/5160)、[CynosDB](https://cloud.tencent.com/document/product/1003/30505) 及 [TDSQL](https://cloud.tencent.com/document/product/557/10236) 三种关系型数据库的示例，推荐您使用腾讯云提供的 Serverless 数据库（CynosDB）。





## 使用原生代码连接数据库的操作步骤

### Node.js 使用 mysql2 连接池示例
```JavaScript
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
Npm 依赖如下：
```JSON
"dependencies": {
    "mysql2": "^1.7.0"
}
```

### Python 使用 pymysql 无连接池示例
>?pymysql 无连接池功能。
>
```Python
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
            port        = int(getenv('DB_PORT', '<YOUR DB PORT>')),
            user        = getenv('DB_USER', '<YOUR DB USER>'),
            password    = getenv('DB_PASSWORD', '<YOUR DB PASSWORD>'),
            db          = getenv('DB_DATABASE', '<YOUR DB DATABASE>'),
            charset     = 'utf8mb4',
            autocommit  = True
        )

    with __get_cursor() as cursor:
        cursor.execute('select * from employee')
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
```
PIP 依赖如下：
```
pymysql
```

### Java 使用 Hikari 连接池示例
```Java
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
Maven 依赖如下：
```XML
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

### 配置环境变量和私有网络

####  MySQL 配置环境变量和私有网络
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，单击已创建的 MySQL 数据库 ID。
2. 在数据库详情页，获取该数据库的**内网地址**、**所属网络**。如下图所示：
![](https://main.qcloudimg.com/raw/bb4109d666fca0405d968293c879e72b.png)
>!如果您使用自建的MySQL实例，请根据实际情况填写**内网地址**、**所属网络**。
>
3. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的【函数服务】。
4. 单击需连接数据库的函数 ID，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**参考以下表格填写。如下图所示：
![](https://main.qcloudimg.com/raw/94a17932ae2a1968d6ab19be4aa3fb91.png)
<table>
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
 - 开启内网访问，并选择和数据库相同的私有网络和子网。如下图所示：
![](https://main.qcloudimg.com/raw/d2f7b877fbb62c92ca2749ffd79ea650.png)


####  CynosDB 配置环境变量和私有网络
1. 登录 [CynosDB 控制台](https://console.cloud.tencent.com/cynosdb)，单击已创建的 CynosDB 数据库 ID。
2. 在数据库详情页，获取该数据库的**内网地址**、**所属网络**。如下图所示：
![](https://main.qcloudimg.com/raw/8d4cb9700aacabf5ec669523c057b967.png)
3. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的【函数服务】。
4. 单击需连接数据库的函数 ID，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**参考以下表格填写。如下图所示：
![](https://main.qcloudimg.com/raw/67aa4cfe1852ae4fb72cf14d0271f1f2.png)
<table>
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
 - 开启内网访问，并选择和数据库相同的私有网络和子网。如下图所示：
![](https://main.qcloudimg.com/raw/d2f7b877fbb62c92ca2749ffd79ea650.png)

## 使用 Serverless DB SDK 连接数据库的操作步骤
为了方便使用，云函数团队将上述 Node.js 和 Python 连接池最佳实践封装成了 Serverless DB SDK，并且内置到了运行时中，不需要在依赖文件中导入依赖。支持 MySQL，CynosDB，TDSQL 等 MySQL 协议的数据库。

Serverless DB SDK 具备以下特点：
- 自动从环境变量初始化数据库客户端。
- SDK 会在全局维护一个数据库长连接，并处理连接中断后的重连。
- 云函数团队会持续关注 issue，确保获得连接即可用，不需要关注数据库连接。


### Node.js SDK
```JavaScript
'use strict';
const database = require('scf-nodejs-serverlessdb-sdk').database;

exports.main_handler = async (event, context, callback) => {
  let connection = await database().connection();
  let result = await connection.queryAsync('select * from name');
  console.log(result);
}
```

>?Node.js 已知 Bug 需要在函数返回前自行释放连接，在函数结束时调用 `connection.close()`，此 Bug 将在下一个版本修复。


### Python SDK
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

### 配置环境变量和私有网络
若您使用 Serverless DB SDK，请按照以下步骤进行配置：
1. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的【函数服务】。
2. 单击需连接数据库的函数 ID，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**，请参考以下表格填写，如下图所示：
![](https://main.qcloudimg.com/raw/46c8b2aab4d4463dd16e1e063b318e36.png)
>!
>- 环境变量 key 格式为`DB_{引用}_XXX`，您可通过 `mysql.database(引用).connection()` 获得已初始化的数据库连接。
>- 若您设置添加环境变量 `DB_DEFAULT` 为 `DB1`，则 `mysql.database()` 默认使用 `DB1`，否则需要指定引用 `mysql.database("DB1")`。
>
<table>
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
 - 开启内网访问，并选择和数据库相同的私有网络和子网。如下图所示：
![](https://main.qcloudimg.com/raw/d2f7b877fbb62c92ca2749ffd79ea650.png)





