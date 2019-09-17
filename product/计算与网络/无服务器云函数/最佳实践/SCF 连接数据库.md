## 操作场景
如果您需要在云函数中使用关系型数据库，我们推荐使用连接池以及云函数团队提供的 SDK 来连接关系型数据库。连接池具备自动重连功能，可有效避免因云函数底层或者数据库释放连接，造成连接不可用的情况。


## 注意事项
由于云函数单实例同时处理的请求数均为1，以及为了防止连接数设置过大导致高并发下数据库连接耗尽，在使用连接池时，建议将最大连接数设置为1。

## Serverless DB SDK
为了方便用户使用，云函数团队封装了内置 Node.js 和 Python 语言的 MySQL SDK，支持 MySQL，TDSQL，CynosDB 等 MySQL 协议的数据库。

### Node.js SDK
```
'use strict';
const database = require('scf-nodejs-serverlessdb-sdk').database;

exports.main_handler = async (event, context, callback) => {
  let connection = await database().connection();
  let result = await connection.queryAsync('select * from name');
  console.log(result);
}
```

### Python SDK
```
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

Serverless DB SDK 具备以下特点：
- 自动从环境变量初始化数据库客户端。
- 经验证，SDK 会在全局维护一个数据库长连接，并会处理连接中断后的重连。
- 云函数团队会持续关注 issue，确保获得连接即可用，不需要关注数据库。


结合您的实际情况，进行如下环境变量和私有网络的配置即可使用。
```
VpcConfig:
  VpcId: "vpc-xxxxxxx"
  SubnetId: "subnet-xxxxxxxx"
Environment:
  Variables:
    # 格式 DB_{引用}_XXX，可通过 mysql.database(引用).connection() 拿到初始化好的数据库连接。
    DB_DB1_HOST: "10.0.31.25" # DB1 实例的地址
    DB_DB1_PORT: "3306" # DB1 实例的端口
    DB_DB1_USER: "root" # DB1 实例的用户名
    DB_DB1_PASSWORD: "xxxxxxxxx" # DB1 实例的密码
    DB_DB1_DATABASE: "TEST" # DB1 实例的数据库
    # 填写此配置，mysql.database() 默认使用 DB1，否则需要指定引用 mysql.database("DB1")。
    DB_DEFAULT: "DB1" 
```


## 前提条件
- 已创建云函数。
- 已创建 Serverless 数据库 [CynosDB](https://cloud.tencent.com/document/product/1003/30505)。
>?本文以 CynosDB 数据库为例。您可根据实际需求选用 TencentDB 其他的数据库或自建的数据库。


## 操作步骤

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
        config.setJdbcUrl(System.getenv("DB_URL"));
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
```
<dependencies>
    <dependency>
        <groupId>com.tencentcloudapi</groupId>
        <artifactId>scf-java-events</artifactId>
        <version>0.0.1</version>
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
1. 登录 [CynosDB 控制台](https://console.cloud.tencent.com/cynosdb)，单击已创建的 CynosDB 数据库 ID。
2. 在数据库详情页，获取该数据库的**内网地址**、**所属网络**。如下图所示：
![](https://main.qcloudimg.com/raw/8d4cb9700aacabf5ec669523c057b967.png)
3. 登录 [云函数控制台](https://console.cloud.tencent.com/scf)，单击左侧导航栏中的【函数服务】。
4. 单击需连接数据库的函数 ID，进入该函数的“函数配置”页面，参考以下信息进行配置。
 - 新增**环境变量**参考以下表格填写。如下图所示：
 ![](https://main.qcloudimg.com/raw/a751f79ce20e6be790909a6a5b74fdbe.png)
<table>
<tr>
<th>key</th>
<th>value</th>
</tr>
<tr>
<td>DB_PASSWORD</td>
<td>已创建数据库的 root 帐户密码。</td>
</tr>
<tr>
<td>DB_USER</td>
<td>默认为 root。</td>
</tr>
<tr>
<td>DB_URL</td>
<td>jdbc:mysql://<code>内网地址</code></td>
</tr>
</table>
 - 开启内网访问，并选择和数据库相同的私有网络和子网。如下图所示：
![](https://main.qcloudimg.com/raw/d2f7b877fbb62c92ca2749ffd79ea650.png)





