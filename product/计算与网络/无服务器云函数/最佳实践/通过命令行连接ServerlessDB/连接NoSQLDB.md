## 操作场景
通过 [Serverless Framework 组件](https://cloud.tencent.com/document/product/1154/39270)，您可轻松完成 Serverless DB 的创建部署管理，并通过 SDK 在云函数中轻松完成数据库的连接访问，基于云上 Serverless 服务，实现“0”配置，极速部署，便捷开发，助力业务实现。

Serverless Framework 目前支持 **PostgreSQL** 与 **NoSQL** 两个类型数据库的部署连接，本文介绍如何使用云函数连接 NoSQL DB。


## 前提条件
已安装 Serverless Framework，且不低于以下版本。如未安装，请参考 [安装 Serverless Framework](https://cloud.tencent.com/document/product/583/44753) 完成安装。
```
Framework Core: 1.67.3
Plugin: 3.6.6
SDK: 2.3.0
Components: 2.30.1
```




## 注意事项
- 请确保您使用的账户下的 `SLS_QcsRole` 的运行角色已具备 `QcloudTCBFullAccess` 策略。如未具备，请前往 [访问管理控制台](https://console.cloud.tencent.com/cam/role) 进行配置。
- 目前云开发 TCB 端仅支持每月最多创建销毁**4**次环境，请谨慎创建，若超过4次部署将会报错。


## 操作步骤
本文以 Node.js 开发语言的函数为例，介绍如何通过 Serverless Framework 组件编写创建函数，创建并访问 NoSQL DB。配置流程如下：
1. **身份信息配置**：在本地配置腾讯云账户信息。
1. **创建云开发环境配置文件**：通过 [Serverless Framework 组件](https://cloud.tencent.com/document/product/1154/39271) 创建云开发环境，在其中创建并使用 NoSQL DB。
2. **编写业务代码**：通过 Serverless DB SDK 调用数据库，云函数支持直接调用 Serverless DB SDK，创建 NoSQL DB 并进行管理操作。
4. **部署与调试**：通过 Serverless Framework 部署项目至云端，并通过云函数控制台进行测试。
5. **移除项目**：可通过 Serverless Framework 移除项目。



### 身份信息配置
1. 在本地建立目录，用于存放代码及依赖模块。本文以  `test-NoSQL` 文件夹为例。
2. Serverless Framework 支持以下2种方式配置身份信息，请按需选择：
	- 执行以下命令，并使用**微信**扫码进行身份验证。
```
serverless login
```
	- 在 `test-NoSQL` 下创建 `.env` 文件，按照以下内容配置对应的腾讯云 SecretId、SecretKey。
```text
# .env
TENCENT_SECRET_ID=xxx  // 您账号的 SecretId
TENCENT_SECRET_KEY=xxx // 您账号的 SecretKey
```
>?
> - 如果没有腾讯云账号，请 [注册新账号](https://cloud.tencent.com/register)。
> - 如果已有腾讯云账号，请确保您的账号已经授权了 `AdministratorAccess` 权限。同时，您可在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
>


### 创建云开发环境配置文件
1. 在 `test-NoSQL` 下创建文件夹 `DB`。
2. 在 `DB` 文件夹下新建 `serverless.yml` 文件，并输入以下内容，通过 Serverless Framework 组件完成云开发环境配置。
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

### 编写业务代码
1. 在 `test-NoSQL` 下创建文件夹 `function`，用于存放业务逻辑代码和相关依赖项。
2. 在文件夹 `function` 下创建文件夹 `src`，并在命令行中进入 `src` 目录，执行以下命令安装 [tcb 依赖包](https://www.npmjs.com/package/tcb-admin-node)。
```
npm install --save tcb-admin-node@latest
```
3. 在 `src` 文件夹下创建文件 `index.js`，并输入如下示例代码。在函数中通过 Serverless TCB SDK 调用云开发环境，并在其中完成 NoSQL 数据库的调用。
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
	const username = 'serverless'
	const collection = db.collection('serverless')
	if (username) {
			await collection.add({username: username})
				}
		const userList = await collection.get()
		return userList
}
```
5. 完成业务代码编写后，创建 `serverless.yml` 文件，并在环境变量中填写您的 **SecretId** 和 **SecretKey**。
>!若使用如下配置，则会创建免费云开发环境。如您已具备免费云开发环境，请将云开发环境 ID 填入 `MongoId` 中，否则会出现报错。 
>
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
1. 使用命令行在 `test-NoSQL` 下，执行以下命令进行部署。
```bash
sls deploy --all
```
返回结果如下所示，即为部署成功。
```
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
2. 部署成功后，您可通过 [云函数控制台](https://console.cloud.tencent.com/scf/index?rid=1)，查看并进行函数调试。测试步骤请参见 [云端测试](https://cloud.tencent.com/document/product/583/37509#.E4.BA.91.E7.AB.AF.E6.B5.8B.E8.AF.95)，测试成功如下图所示：
![](https://main.qcloudimg.com/raw/46a5f3397cdaac7c6790a5b096cc7c36.png)
>?您还可通过 [Serverless Dashboard](https://serverless.cloud.tencent.com/)，松实现部署项目的实时监控。
>

### 移除项目
在 `test-NoSQL` 目录下，执行以下命令可移除项目。
```
sls remove --all
```
返回如下结果，即为成功移除。
```
serverless ⚡ framework
4s › test-NoSQL › Success
```
更多 NoSQL DB 用法，请参考 [基于 NoSQL 全栈网站最佳实践](https://cloud.tencent.com/document/product/1154/44073)。
