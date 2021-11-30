本文为您介绍在 MySQL 节点新建 MySQL 集群后，通过数据管理平台 DMC 或内外网地址来连接 MySQL 集群。

## 前提条件

已完成 [新建 MySQL 集群](https://cloud.tencent.com/document/product/1081/62046)。

## 连接方式

连接 MySQL 集群的方式如下：

- **通过数据管理平台 DMC 连接**：通过数据管理平台（Database Management Console，DMC）访问 MySQL 集群。
- **通过内网地址连接**：通过内网地址连接 MySQL 集群，使用自研节点或云服务器 CVM 直接连接云数据库的内网地址，这种连接方式使用内网高速网络，延迟低。
   - 自研节点或云服务器和数据库须是同一账号，且同一个[ VPC](https://cloud.tencent.com/document/product/215/20046) 内（保障同一个地域）。
   - 内网地址系统默认提供，可在 MySQL 节点的集群列表或集群详情页查看。
>?对于不同的 VPC 下（包括同账号/不同账号，同地域/不同地域）的云服务器和数据库，内网连接方式请参见 [云联网](https://cloud.tencent.com/document/product/877)。
>
- **通过外网地址连接**：通过外网地址连接 MySQL 集群。外网地址需 [手动开启](#waiwang)，可在 MySQL 节点的集群详情页查看，不需要时也可关闭。
   - 开启外网地址，会使您的数据库服务暴露在公网上，可能导致数据库被入侵或攻击。建议您使用内网连接数据库。 
   - MySQL 集群外网访问适用于开发或辅助管理数据库，不建议正式业务访问使用，因为可能存在不可控因素会导致外网访问不可用（例如 DDOS 攻击、突发大流量访问等）。

## 通过数据管理平台 DMC 连接 MySQL 集群
1. 在 MySQL节点的集群列表页，单击”操作“列的**登录**，进入数据管理控制台的登录界面。
2. 在数据管理控制台的登录界面，帐号输入 root，密码为之前在创建集群时配置的 root 帐户的密码，单击**登录**。
![](https://main.qcloudimg.com/raw/d07b1477bd524f23fbaa9450c352c49f.png)

>?DMC 平台可便捷地访问实例、操作库表级、管理实例会话、实时监控、InnoDB 锁等待、SQL 窗口等。



## 通过内外网连接 MySQL 集群
### 从自研节点连接

您可以在自研节点中，通过内网 VPC 快速链接您的 MySQL 集群。

1. 确认自研节点和 MySQL 集群在同一个 VPC 下。若 MySQL 集群已创建，且与自研节点不在同一个 VPC，可通过修改 MySQL 集群的网络，使自研节点和 MySQL 集群在同一个 VPC 下。
>? 建议先通过自研节点新建服务，选择由系统推荐的 VPC，并在新建 MySQL 集群时将集群部署在该 VPC 中。
>
2. 按照正常连接数据库的方式编写您的业务代码，并将其打包为镜像上传到镜像仓库。
>? 您可以参考 [函数代码示例](#code) 构建可连接数据库的业务代码。
>
3. 为自研节点的服务新建版本，选择相应镜像，并在托管配置页面新增**环境变量**，并参考以下表格填写。

| key      | value        |
| :------- | :----------- |
| HOST     | 数据库地址   |
| USER     | 数据库用户名 |
| PASSWORD | 数据库密码   |

如下图所示：
![](https://main.qcloudimg.com/raw/df0db89b0f9fdc7a6a774a7bb3720215.jpg)


### 从 Linux 云服务器连接
1. 登录到 Linux 云服务器，请参见 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
2. 以 CentOS 7.2 64 位系统的云服务器为例，执行如下命令安装 MySQL 客户端：
```
yum install mysql
```
提示 `Complete!` 说明 MySQL 客户端安装完成。
![](https://main.qcloudimg.com/raw/16c77e28c40ae9be9a182b1c61843ecd.png)
3. 根据不同连接方式，选择相应的操作：
 - **内网连接时：**
    1. 执行如下命令，登录到 MySQL 集群。
```
mysql -h hostname -u username -p
```
		- hostname：替换为目标 MySQL 集群的内网地址，在 MySQL 节点的集群详情页可查看内网地址。
		- username：替换为默认的用户名 root。
	2. 在提示`Enter password：`后输入 MySQL 集群的 root 帐号对应的密码，如忘记密码可在 MySQL 节点的账号管理页进行修改。
    本例中提示`MySQL [(none)]>`说明成功登录到 MySQL 集群。![](https://main.qcloudimg.com/raw/83b8a95cf4b99919b5899510691289b4.png)
 - **外网连接时：**
    1. 执行如下命令，登录到 MySQL 集群。
```
mysql -h hostname -P port -u username -p
```
		- hostname：替换为目标 MySQL 集群的外网地址，在 MySQL 节点的集群详情页可查看外网地址和端口号。若外网地址未开启，请参见 [开启外网地址](#waiwang) 开启。
		- port：替换为外网端口号。
		- username：替换为外网连接用户名，用于外网连接，建议您在控制台单独创建帐号便于连接控制管理。
    2. 在提示`Enter password：`后输入外网连接用户名对应的密码，如忘记密码可在 MySQL 节点的账号管理页进行修改。
    本例中 hostname 为 59281c4exxx.myqcloud.com，外网端口号为15311。
    ![](https://main.qcloudimg.com/raw/16839344da3a588be93d814de224277a.png)
4. 在 `MySQL \[(none)]>` 提示符下可以发送 SQL 语句到要执行的 MySQL 集群，具体命令行请参见 [mysql Client Commands](https://dev.mysql.com/doc/refman/5.7/en/mysql-commands.html)。
下图中以`show databases;`为例：
![](https://main.qcloudimg.com/raw/bde01ce4635ed30f038588c4601b464a.png)

### 从 Windows 云服务器连接

1. 登录到 Windows 云服务器，请参见 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764)。
2. 下载一个标准的 SQL 客户端。
>?推荐您下载 MySQL Workbench，并根据您的系统来下载适配版本的安装程序，详情请见 [下载地址](https://dev.mysql.com/downloads/workbench)。
>
>![](https://main.qcloudimg.com/raw/851ab46468c554097a0cf742017157b7.png)
3. 界面将提示 **Login**、**Sign Up** 和 **No, thanks, just start my download.**， 选择 **No thanks, just start my download.** 来快速下载。
![](https://main.qcloudimg.com/raw/47b195fb37ff584f21038ee54342d362.png)
4. 在此台云服务器上安装 MySQL Workbench。
>?
>- 此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。
>- 您可以单击 MySQL Workbench 安装向导中的 **Download Prerequisites**，跳转至对应页面下载并安装这两个软件，然后安装 MySQL Workbench。
>
>![](https://main.qcloudimg.com/raw/1af292f989f03f3e02e1200b77cb70c1.png)
5. 打开 MySQL Workbench，选择 **Database**>**Connect to Database**，输入 MySQL 数据库实例的内网（或外网）地址和用户名、密码，单击 **OK** 进行登录。
 - Hostname：输入内网（或外网）地址。在 MySQL 节点的集群详情页可查看到目标数据库的内网（或外网）地址。若为外网地址，请确认是否已开启，请参见 [开启外网地址](#waiwang)。
 - Port：内网（或外网）对应端口。
 - Username：默认为 root。
 - Password：Username 对应的密码。如忘记密码可在 MySQL 节点的集群详情页进行修改。
![](https://main.qcloudimg.com/raw/9c9e5dcc8a2bb9fa15fa4d98a18308f1.png)
6. 登录成功的页面如图 所示，在此页面上您可以看到数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/33f081e99c384258bbc5ed3683ed4d7d.png)

[](id:waiwang)
## 附录1：开启外网连接地址
>?使用外网连接时，需要先开启数据库的外网地址。
>
1. 在 MySQL 节点的集群列表页，单击集群名，进入集群详情页面。
2. 在集群详情页的”集群连接外网地址“处，单击**开启**。
![](https://main.qcloudimg.com/raw/09b186229ae121fe32c53317727ef8b8.png)
3. 在弹出的对话框，单击**确定**。
>?
>- 开启成功后，即可在连接信息中查看外网地址。
>- 通过开关可以关闭外网访问权限，重新开启外网，域名对应的外网 IP 不变。

[](id:code)
## 附录2：函数代码示例

<dx-tabs>
::: Python
Python 可使用 **pymysql** 依赖包进行数据库连接。示例代码如下：
<dx-codeblock>
:::  python
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
:::
</dx-codeblock>
:::
::: Node.js
Node.js 支持使用连接池进行连接，连接池具备自动重连功能，可有效避免因云函数底层或者数据库释放连接造成的连接不可用情况。示例代码如下：
<dx-alert infotype="explain" title="">
使用连接池前需先安装 **mysql2** 依赖包。
</dx-alert><dx-codeblock>
:::  js
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
:::
</dx-codeblock>
:::
::: PHP
PHP 可使用 **pdo_mysql** 或 **mysqli** 依赖包进行数据连接。示例代码如下：
<dx-codeblock>
:::  php

```

function handler($event, $context) {
try{
    $pdo = new PDO('mysql:host= getenv("DB_HOST");dbname= getenv("DB_DATABASE"),getenv("DB_USER"),getenv("DB_PASSWORD")');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  }catch(PDOException $e){
    echo '数据库连接失败: '.$e->getMessage();
    exit;
  }
}

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

```
:::
</dx-codeblock>
:::
