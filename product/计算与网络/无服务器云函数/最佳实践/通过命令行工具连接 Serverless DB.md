# 通过命令行工具连接 Serverless DB 


## 操作场景
通过[ Serverless Framework 组件](https://cloud.tencent.com/document/product/1154/39270)，您可轻松完成 Serverless DB 的创建部署管理，并通过 SDK 在云函数中轻松完成数据库的连接访问，基于云上 Serverless 服务，实现“0”配置，极速部署，便捷开发，助力业务实现。

目前，Serverless Framework 支持 **PostgreSQL** 与 **NoSQL** 两个类型数据库的部署连接

## 云函数连接 PostgreSQL 

本文以 Node.js 开发语言的函数示例为例，介绍如何通过 Serverless Framework 组件编写函数创建并访问 PostgreSQL 数据库。

### 前提条件
- **安装 Serverless Framework**

  通过 npm 全局安装 [Serverless Framework](https://github.com/serverless/serverless)：
   ```shell
   $ npm install -g serverless
   ```
  
  安装完毕后，通过运行 serverless -v 命令，查看 Serverless Framework 的版本信息，确保版本信息不低于以下版本：

   ```shell
   $ serverless –v
     Framework Core: 1.67.3
     Plugin: 3.6.6
     SDK: 2.3.0
     Components: 2.30.1
    ```

- **创建私有网络**

   通过 [Serverless Framework VPC 组件](https://cloud.tencent.com/document/product/1154/43005)创建 **VPC** 和 **子网**，提供 SCF 云函数和数据库的网络打通和使用。
   
- **创建 PostgreSQL 实例**

   通过 [Serverless Framework PostgreSQL 组件](https://cloud.tencent.com/document/product/1154/43004)创建 PostgreSQL 实例,为云函数项目提供数据库服务。
   
- **通过 Serverless DB SDK调用数据库**

     云函数支持直接调用 Serverless DB SDK，从而连接 PostgreSQL 数据库进行管理操作。

### 具体步骤

1. **身份信息配置**

   在本地建立一个目录，用于存放代码和依赖模块，创建 .env 文件，并在其中配置对应的腾讯云 SecretId、SecretKey、地域和可用区信息。

   ```console
   $ touch .env
   ```

   ```text
   # .env
   TENCENT_SECRET_ID=xxx  // 您账号的 SecretId
   TENCENT_SECRET_KEY=xxx // 您账号的 SecretKey

   # 地域可用区配置
   REGION=ap-guangzhou //资源部署区，该项目中指云函数与静态页面部署区
   ZONE=ap-guangzhou-2 //资源部署可用区 ，该项目中指 DB 部署所在的可用区
   ```
   > 说明：

   > - 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
   > - 如果已有腾讯云账号，请保证您的账号已经授权了 AdministratorAccess 权限。 您可以
  在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId
  和 SecretKey。

2. **VPC 配置**

   在该目录下创建 VPC 文件夹，新建 serverless.yml 文件，完成 VPC 私有网络和子网的配置

```text
org: fullstack
app: fullstack-serverless-db
stage: dev

component: vpc # (required) name of the component. In that case, it's vpc.
name: serverlessVpc # (required) name of your vpc component instance.

inputs:
  region: ${env:REGION}
  zone: ${env:ZONE}
  vpcName: serverless
  subnetName: serverless
```

> 说明：

> - 请务必保证子网和 ZONE 在同一个可用区

3. **Serverless DB 配置**
   
   回到根目录，创建 DB 文件夹，新建 serverless.yml 文件，完成 PostgreSQL 数据库创建配置

```text
org: fullstack
app: fullstack-serverless-db
stage: dev

component: postgresql
name: fullstackDB

inputs:
  region: ${env:REGION}
  zone: ${env:ZONE}
  dBInstanceName: ${name}
  vpcConfig:
    vpcId: ${output:${stage}:${app}:serverlessVpc.vpcId}
    subnetId: ${output:${stage}:${app}:serverlessVpc.subnetId}
  extranetAccess: false
```

4. **编写业务代码**

  继续在根目录下创建 api 文件夹，用于存放业务逻辑代码和相关依赖项，在函数中，通过 Serverless DB SDK 创建连接池，并调用数据库

```
'use strict';

const { Pool } = require('pg');

exports.main_handler = async (event, context, callback) => {
  let pgPool = new Pool({
        connectionString: process.env.PG_CONNECT_STRING,
      });
  await pgPool.query(`CREATE TABLE IF NOT EXISTS users (
        ID serial NOT NULL,
        NAME           TEXT         NOT NULL,
        EMAIL          CHAR(50)     NOT NULL,
        SITE          CHAR(50)     NOT NULL
      );`);
  
  const client = await pgPool.connect();
  const { rows } = await client.query({
      text: 'select * from users',
    });
  await client.end();

  console.log('pgsql query result:',rows)
}

```

完成业务代码编写后，配置 serverless.yml 文件，在环境变量中配置 Serverless DB 的 Connection String

```
org: fullstack
app: fullstack-serverless-db
stage: dev
component: scf

inputs:
  name: ${app}
  src:
    src: ./src
    exclude:
      - .env
  region: ${env:REGION}
  runtime: Nodejs10.15
  handler: index.main_handler
  timeout: 30
  vpcConfig:
    vpcId: ${output:${stage}:${app}:serverlessVpc.vpcId}
    subnetId: ${output:${stage}:${app}:serverlessVpc.subnetId}
  environment:
    variables:
      PG_CONNECT_STRING: ${output:${stage}:${app}:fullstackDB.private.connectionString}

```

### 部署与调试

1. 安装

通过 npm 全局安装
[Serverless Framework](https://github.com/serverless/serverless)：

```shell
$ npm install -g serverless
```

2. 部署

执行以下命令进行部署

```bash
$ sls deploy --all

serverless ⚡ framework

serverlessVpc: 
  region:     ap-guangzhou
  zone:       ap-guangzhou-2
  vpcId:      vpc-0ncak84t
  vpcName:    serverless
  subnetId:   subnet-gi085his
  subnetName: serverless

fullstackDB: 
  region:         ap-guangzhou
  zone:           ap-guangzhou-2
  vpcConfig: 
    subnetId: subnet-gi085his
    vpcId:    vpc-0ncak84t
  dBInstanceName: fullstackDB
  dBInstanceId:   postgres-0y2x3fd3
  private: 
    connectionString: postgresql://tencentdb_0y2x3fd3:GD0U1(q~g7%3D6ySI@10.0.0.10:5432/tencentdb_0y2x3fd3
    host:             10.0.0.10
    port:             5432
    user:             tencentdb_0y2x3fd3
    password:         GD0U1(q~g7=6ySI
    dbname:           tencentdb_0y2x3fd3

fullstack-serverless-db: 
  FunctionName: fullstack-serverless-db
  Description:  
  Namespace:    default
  Runtime:      Nodejs10.15
  Handler:      index.main_handler
  MemorySize:   128

25s › fullstack-serverless-db › Success

```

部署成功后，您可通过[云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1), 查看并进行函数调试

<center>
<img src="https://my-bucket-1258834142.cos.ap-guangzhou.myqcloud.com/slsdb.png" alt="demo" width="500">
</center>

通过 [Serverless Dashboard](https://serverless.cloud.tencent.com/)，可轻松实现部署项目的实时监控 

3. 执行 ```sls remove --all ```，可移除项目。

```bash
$  sls remove --all

serverless ⚡ framework

38s › tencent-fullstack › Success
```

更多 PostgreSQL 数据库用法，可参考[基于 PG SQL+Website 全栈网站最佳实践](https://cloud.tencent.com/document/product/1154/43009)


## 云函数连接 NoSQL DB

除了 PostgreSQL 之外， Serverless Framework 还支持用户在云开发环境下创建并部署 NoSQL DB，具体步骤如下：

### 前提条件
- **安装 Serverless Framework**

   通过 npm 全局安装[Serverless Framework](https://github.com/serverless/serverless)：
   ```shell
   $ npm install -g serverless
   ```
   安装完毕后，通过运行 serverless -v 命令，查看 Serverless Framework 的版本信息，确保版本信息不低于以下版本：

   ```shell
   $ serverless –v
   Framework Core: 1.67.3
   Plugin: 3.6.6
   SDK: 2.3.0
   Components: 2.30.1
   ```

- **创建云开发环境**

   通过 [Serverless Framework 组件](https://cloud.tencent.com/document/product/1154/43005)创建云开发环境，在其中创建并使用 NoSQL 数据库
- **通过 Serverless SDK调用数据库**

   云函数支持直接调用 Serverless SDK，从而创建 NoSQL 数据库并进行管理操作。
  

### 具体步骤

1. **身份信息配置**

Serverless Framework 支持扫码进行身份验证，同时，您也可以在本地项目根目录下创建 .env 文件，并在其中配置对应的腾讯云 SecretId、SecretKey。

```console
$ touch .env
```

```text
# .env
TENCENT_SECRET_ID=xxx  // 您账号的 SecretId
TENCENT_SECRET_KEY=xxx // 您账号的 SecretKey
```
> 说明：

> - 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
> - 如果已有腾讯云账号，请保证您的账号已经授权了 AdministratorAccess 权限。 您可以
  在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId
  和 SecretKey。

2. **创建云开发环境配置文件**

回到根目录，创建 DB 文件夹，新建 serverless.yml 文件，通过 Serverless Framework 组件完成云开发环境配置

```
# serverless.yml 
component: mongodb
name: mongoDBDemoMongo
org: anycodes
app: mongoDBAPP
stage: dev

inputs:
  name: Mydemo
```

3. **编写函数代码，创建配置文件**

继续在根目录下创建 function 文件夹，用于存放业务逻辑代码和相关依赖项，在函数中，通过 Serverless TCB SDK 调用云开发环境，并在其中完成 NoSQL 数据库的调用，示例代码如下：

```
const tcb = require('tcb-admin-node')

const app = tcb.init({
	secretId: process.env.SecretId,
	secretKey: process.env.SecretKey,
	env: process.env.MongoId,
	serviceUrl: 'https://tcb-admin.tencentcloudapi.com/admin'
})

const db = app.database()

const _ = db.command

exports.main = async (event, context) => {

	await db.createCollection('serverless')
	const username = JSON.parse(event.body).username
	const collection = db.collection('serverless')

	if (username) {
			await collection.add({username: username})	
		}
		const userList = await collection.get()
		return userList
}
```

完成业务代码编写后，配置 serverless.yml 文件，在环境变量中配置用户的 **SecretId** 和 **SecretKey**。

```
component: scf
name: mongoDBDemoSCF
org: anycodes
app: mongoDBAPP
stage: dev

inputs:
  name: MongoDBDemo
  src: ./src
  runtime: Nodejs8.9
  region: ap-guangzhou
  handler: index.main
  environment:
    variables:
      SecretId: 请填入您的SecretId
      SecretKey: 请填入您的SecretKey
      MongoId: ${output:${stage}:${app}:mongoDBDemoMongo.EnvId}

```

### 部署与调试

1. 安装

通过 npm 全局安装
[Serverless Framework](https://github.com/serverless/serverless)：

```shell
$ npm install -g serverless
```

2. 部署

执行以下命令进行部署

```bash
$ sls deploy --all

serverless ⚡ framework

mongoDBDemoMongo:
  Region:    ap-guangzhou
  Name:      Mydemo
  EnvID:     Mydemo-dyxfxv
  FreeQuota: basic

mongoDBDemoSCF: 
  FunctionName: MongoDBDemo
  Description:  
    Namespace:    default
    Runtime:      Nodejs8.9
    Handler:      index.main
    MemorySize:   128

25s › tcbdemo › Success

```

部署成功后，您可通过[云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1), 查看并进行函数调试

通过 [Serverless Dashboard](https://serverless.cloud.tencent.com/)，可轻松实现部署项目的实时监控 

> 注意：
>- 由于 sls 运行角色限制，需要用户登录 [访问管理角色页面](https://console.cloud.tencent.com/cam/role)，手动为**SLS_QcsRole**添加**TCBFullAccess**的策略，否则无法正常运行。
>- 当前`deploy --all`指令只支持2.30.1及以上版本 Serverless Framework Component，请确定您的组件已更新至最新版本。
>- 目前 TCB 端仅支持每月最多创建销毁**4**次环境，请谨慎创建，若超过4次部署将会报错。


3. 执行 ```sls remove --all ```，可移除项目。


更多 NoSQL 数据库用法，可参考[基于 NoSQL 全栈网站最佳实践](https://cloud.tencent.com/document/product/1154/44073)
