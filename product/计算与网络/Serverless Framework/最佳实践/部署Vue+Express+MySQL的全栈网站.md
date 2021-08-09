## 操作场景
本文主要介绍如何通过 Serverless Framework 的多个组件结合使用，快速部署一个全栈网站。

该项目主要包含以下模块：

| 模块 | 说明 | 
|---------|---------|
| <nobr>Serverless RESTful API</nobr> | 通过云函数和 API 网关构建的 Express 框架实现 RESTful API。|
| Serverless 静态网站 | 前端通过托管 Vue.js 静态页面到 COS 对象存储中。|
| TDSQL-C Serverless | 通过创建 TDSQL-C Serverless (原 CynosDB Serverless) 的 MySQL 类型数据库，为全栈网站提供数据库服务。|
| VPC | 通过创建 VPC 和子网，提供 SCF 云函数和数据库的网络打通和使用。|

## 操作步骤

### 1. 安装 Serverless Framework
通过 npm 全局安装 Serverless Framework：

```
npm install -g serverless
```

如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版：

```
npm update -g serverless
```

安装完毕后，通过运行 `serverless -v` 命令，查看 Serverless Framework 的版本信息，如果有版本信息返回，则已经安装成功。

### 2. 初始化模版

通过如下命令直接下载该模版：

```bash
serverless init fullstack-mysql --name example
cd example
```

### 3. 项目配置

由于目前 TDSQL-C Serverless 只支持 `ap-beijing-3`、`ap-guangzhou-4`、`ap-shanghai-2` 和 `ap-nanjing-1` 四个区域，所以此处需要进行地域配置，只需要在项目根目录下创建 `.env` 文件，然后配置 `REGION` 和 `ZONE` 两个环境变量：

```
REGION=ap-shanghai
ZONE=ap-shanghai-2
```

完成配置后，可以看到项目目录结构如下：
```
.
├── package.json # 依赖项文件目录
├── node_modules # 依赖项文件
├── vpc
│   └── serverless.yml # VPC 组件配置文件，用来创建 VPC 资源
├── db
│   └── serverless.yml # TDSQL-C 配置文件，用来创建 MySQL 数据库
├── api
│   ├── sls.js # Express 框架入口函数文件
│   ├── ...
│   ├── controller
│   │    ├── db.js # 连接数据库函数
│   │    └── user.js  # 管理用户数据函数
│   └── serverless.yml # Express 配置文件，快速部署 Express 上云
├── frontend
│   ├── public
│   ├── src
│   ├── ...
│   └── serverless.yml # Website 配置文件，快速创建静态页面托管
└── .env # 环境变量文件
```

查看 `./api/controller/db.js` 目录，可以具体了解云函数如何连接 MySQL 数据库。


### 4. 部署应用

在 `serverless.yml` 文件所在的项目根目录，运行以下指令，将会弹出二维码，直接扫码授权进行部署：

```bash
sls deploy
```
>?如果鉴权失败，请参考 [权限配置](https://cloud.tencent.com/document/product/1154/43006) 进行授权。

部署成功后，您可以使用浏览器访问项目产生的 website 链接，即可看到生成的网站页面,完成全栈应用部署。
![](https://main.qcloudimg.com/raw/096bd7a5960304864c0122105ea3a73c.png)

### 账号配置（可选）

Serverless 默认支持扫描二维码登录，用户扫描二维码后会自动生成一个 `.env` 文件并将密钥存入其中。
如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件，把从 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取的 SecretId 和 SecretKey 填入其中。
```
# .env file
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。


