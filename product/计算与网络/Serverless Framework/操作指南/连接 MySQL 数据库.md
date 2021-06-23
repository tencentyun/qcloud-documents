## 操作场景
目前，[腾讯云原生数据库 TDSQL-C](https://cloud.tencent.com/document/product/1003/30505) 已支持 Serverless MySQL 版本，做到按实际使用的计算和存储量计费，按秒计量，按小时结算。Serverless Framework 的 CynosDB 组件也已经支持该类型数据库的创建。

本文以 Node.js 开发语言的函数，指导您快速创建 TDSQL-C Serverless MySQL 实例，并在云函数中进行调用。

##  操作步骤

| 操作步骤 | 操作说明 | 
|---------|---------|
| [步骤1：配置环境变量](#step1)|  - |
| [步骤2：配置私有网络](#step2) | 通过 Serverless Framework VPC 组件 创建 VPC 和 子网，支持云函数和数据库的网络打通和使用。|
| <nobr>[步骤3：配置 Serverless DB](#step3)</nobr> | 通过 Serverless Framework Cynosdb 组件创建 MySQL 实例，为云函数项目提供数据库服务。|
| [步骤4：编写业务代码](#step4) | 通过 Serverless DB SDK 调用数据库，云函数支持直接调用 Serverless DB SDK，连接 PostgreSQL 数据库进行管理操作。|
| [步骤5：部署应用](#step5) |  通过 Serverless Framework 部署项目至云端，并通过云函数控制台进行测试。|
| [步骤6：移除项目（可选）](#remove) | 可通过 Serverless Framework 移除项目。|

### 步骤1：配置环境变量[](id:step1)
1. 在本地建立目录，用于存放代码及依赖模块。本文以  `test-MySQL` 文件夹为例。
```
mkdir test-MySQL && cd test-MySQL
```

2. 由于目前 TDSQL-C Serverless 只支持 `ap-beijing-3`，`ap-guangzhou-4`，`ap-shanghai-2` 和 `ap-nanjing-1` 四个区域，所以这里还需要配置下，只需要在项目根目录下创建 `.env` 文件，然后配置 `REGION` 和 `ZONE` 两个环境变量：
```text
# .env
REGION=xxx  
ZONE=xxx 
```

### 步骤2：配置私有网络[](id:step2)
1. 在 `test-MySQL` 目录下创建文件夹 `VPC`。
```
mkdir VPC && cd VPC
```

2. 在 `VPC` 中新建 serverless.yml 文件，使用[ VPC 组件](https://github.com/serverless-components/tencent-vpc)完成私有网络和子网的创建。
`serverless.yml` 示例内容如下（全量配置参考 [产品文档](https://github.com/serverless-components/tencent-vpc/blob/master/docs/configure.md)）：
<dx-codeblock>
:::  yml
#serverless.yml
app: mysql-app
stage: dev
component: vpc # (required) name of the component. In that case, it's vpc.
name: mysql-app-vpc # (required) name of your vpc component instance.
inputs:
  region: ${env:REGION}
  zone: ${env:ZONE}
  vpcName: serverless-mysql
  subnetName: serverless-mysql
:::
</dx-codeblock>

### 步骤3：配置 Serverless DB[](id:step3)
1. 在 `test-MySQL` 下创建文件夹 `DB`。

2. 在 `DB` 文件夹下新建 `serverless.yml` 文件，并输入以下内容，通过 Serverless Framework 组件完成云开发环境配置。
`serverless.yml` 示例内容如下（全量配置参考 [产品文档](https://github.com/serverless-components/tencent-cynosdb/blob/master/docs/configure.md)）：
<dx-codeblock>
:::  yml
# serverless.yml 
app: mysql-app
stage: dev
component: cynosdb
name: mysql-app-db
inputs:
  region: ${env:REGION}
  zone: ${env:ZONE}
  vpcConfig:
    vpcId: ${output:${stage}:${app}:mysql-app-vpc.vpcId}
    subnetId: ${output:${stage}:${app}:mysql-app-vpc.subnetId}
:::
</dx-codeblock>


### 步骤4：编写业务代码与配置文件[](id:step4)
1. 在 `test-MySQL` 下创建文件夹 `src`，用于存放业务逻辑代码和相关依赖项。

2. 在 `src` 文件夹下创建文件 `index.js`，并输入如下示例代码。在函数中通过  SDK 连接数据库，并在其中完成 MySQL 数据库的调用。
<dx-codeblock>
:::  js
exports.main_handler = async (event, context, callback) => {
  var mysql      = require('mysql2');
  var connection = mysql.createConnection({
    host     : process.env.HOST,
    user     : 'root',
    password : process.env.PASSWORD
  });
  connection.connect();
  connection.query('SELECT 1 + 1 AS solution', function (error, results, fields) {
    if (error) throw error;
    console.log('The solution is: ', results[0].solution);
  });
  connection.end();
 }
:::
</dx-codeblock>

3. 安装所需依赖模块。
```
npm install mysql2
```

4. 完成业务代码编写和依赖安装后，创建 `serverless.yml` 文件，示例文件如下：
<dx-codeblock>
:::  yml
app: mysql-app
stage: dev
component: scf
name: mysql-app-scf

inputs:
  src: ./
  functionName: ${name}
  region: ${env:REGION}
  runtime: Nodejs10.15
  timeout: 30
  vpcConfig:
    vpcId: ${output:${stage}:${app}:mysql-app-vpc.vpcId}
    subnetId: ${output:${stage}:${app}:mysql-app-vpc.subnetId}
  environment:
    variables:
      HOST: ${output:${stage}:${app}:mysql-app-db.connection.ip}
      PASSWORD: ${output:${stage}:${app}:mysql-app-db.adminPassword}
:::
</dx-codeblock>

### 步骤5：快速部署[](id:step5)
完成创建后，项目目录结构如下：
```
   ./test-MySQL
   ├── vpc
   │   └── serverless.yml # vpc 配置文件
   ├── db
   │   └── serverless.yml # db 配置文件
   ├── src
   │   ├── serverless.yml # scf 组件配置文件
   │   ├── node_modules # 项目依赖文件
   │   └── index.js # 入口函数
   └── .env # 环境变量文件
```
1. 使用命令行在 `test-MySQL` 下，执行以下命令进行部署。
```bash
sls deploy
```
 >?
>- 部署时需要扫码授权，如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果是子账号，请参考 [子账号权限配置](https://cloud.tencent.com/document/product/1154/43006#.E5.AD.90.E8.B4.A6.E5.8F.B7.E6.9D.83.E9.99.90.E9.85.8D.E7.BD.AE.3Ca-id.3D.22rightsprofile.22.3E.3C.2Fa.3E) 完成授权。

 返回结果如下所示，即为部署成功。
<dx-codeblock>
::: mysql
mysql-app-vpc: 
  region:        xxx
  zone:          xxx
  vpcId:         xxxx-xxx
  ...

mysql-app-db: 
  dbMode:        xxxx
  region:        xxxx
  zone:          xxxx
  ...

mysql-app-scf: 
  functionName:  xxxx
  description:   xxx
  ...

59s › test-MySQL › "deploy" ran for 3 apps successfully.
:::
</dx-codeblock>

2. 部署成功后，您可通过 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)，查看并进行函数调试，测试成功如下图所示：
![](https://main.qcloudimg.com/raw/f55346a48e68f78771fb746b58b3c1a0.png)


### 步骤6：移除项目（可选）[](id:step6)
在 `test-MySQL` 目录下，执行以下命令可移除项目。
```
sls remove
```
返回如下结果，即为成功移除。
```
serverless ⚡ framework
4s › test-MySQL › Success
```

## 示例代码
### Python
Python 可使用云函数环境已经内置的 **pymysql** 依赖包进行数据库连接。示例代码如下：
<dx-codeblock>
:::  python
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
:::
</dx-codeblock>


### Node.js
Node.js 支持使用连接池进行连接，连接池具备自动重连功能，可有效避免因云函数底层或者数据库释放连接造成的连接不可用情况。示例代码如下：
>?使用连接池前需先安装 **mysql2** 依赖包，详情请参见 [依赖安装](https://cloud.tencent.com/document/product/583/39780)。

<dx-codeblock>
:::  nodejs
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
:::
</dx-codeblock>


### PHP
PHP 可使用 **pdo_mysql** 或 **mysqli** 依赖包进行数据连接。示例代码如下：
- **pdo_mysql**
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

- **mysqli** 
``` php
<?php
function main_handler($event, $context) {
     $host = "";
    $username = "";
    $password = "";
 
    // 创建连接
    $conn = mysqli_connect($servername, $username, $password);

    // 检测连接
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
        }
    echo "连接成功"; 

    mysqli_close($conn);
    echo "断开连接"; 
}
?>
```

### Java
1. 请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780#java-.E8.BF.90.E8.A1.8C.E6.97.B6)，安装以下依赖。
<dx-codeblock>
:::  xml
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
:::
</dx-codeblock>

2. 使用 Hikari 连接池进行连接，示例代码如下：
<dx-codeblock>
:::  java
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
:::
</dx-codeblock>


### SCF DB SDK for MySQL

为了方便使用，云函数团队将 Node.js 和 Python 连接池相关代码封装为 SCF DB SDK for MySQL，请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780) 进行安装使用。通过该 SDK，您可以在云函数代码中连接 [MySQL](https://cloud.tencent.com/document/product/236/5147)、[TDSQL-C](https://cloud.tencent.com/document/product/1003/30488) 或 [TDSQL MySQL版](https://cloud.tencent.com/document/product/557/7700) 数据库，并实现对数据库的插入、查询等操作。

SCF DB SDK for MySQL 具备以下特点：
- 自动从环境变量初始化数据库客户端。
- SDK 会在全局维护一个数据库长连接，并处理连接中断后的重连。
- 云函数团队会持续关注 issue，确保获得连接即可用，不需要关注数据库连接。

**1. Node.js SDK**
<dx-codeblock>
:::  JavaScript
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
:::
</dx-codeblock>

>?Node.js SDK 具体使用方法请参考 [SCF DB SDK for MySQL](https://www.npmjs.com/package/scf-nodejs-serverlessdb-sdk)。


**2. Python SDK**
<dx-codeblock>
:::  Python
from serverless_db_sdk import database

def main_handler(event, context):
    print('Start Serverlsess DB SDK function')

    connection = database().connection(autocommit=False)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM name')
    myresult = cursor.fetchall()

    for x in myresult:
        print(x)
:::
</dx-codeblock>
