## 操作场景

该模板可以快速部署一个基于 Vue + Express + PostgreSQL 的全栈 Serverless 应用。主要包含以下组件：

- Serverless RESTful API：通过**云函数**和 **API 网关**构建的 Express 框架实现
  RESTful API。
- Serverless 静态网站：前端通过托管 Vue.js 静态页面到 **COS 对象存储**中。
- PostgreSQL Serverless：通过创建 **PostgreSQL DB** 为全栈网站提供数据库服务。
- VPC：通过创建 **VPC** 和 **子网**，提供 SCF 云函数和数据库的网络打通和使用。

## 前提条件

- 已安装 [Node.js](https://nodejs.org/en/)（**2020年9月1日起，Serverless 组件不再支持 Node.js10.0 以下版本，请注意升级**）
- 账号已经配置 **QcloudPostgreSQLFullAccess** 策略，配置方法详见 [账号和权限配置](https://cloud.tencent.com/document/product/1154/43006)

## 操作步骤

### 安装

通过 npm 全局安装 [Serverless Framework](https://github.com/serverless/serverless)：

```shell
npm install -g serverless
```

如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版：

```shell
npm update -g serverless
```

安装完毕后，通过运行 serverless -v 命令，查看 Serverless Framework 的版本信息，确保版本信息不低于以下版本。返回结果如下所示：

```shell
$ serverless –v
Framework Core: 1.74.1 (standalone)
Plugin: 3.6.14
SDK: 2.3.1
Components: 2.31.6
```

### 配置

1. 新建一个本地文件夹，使用 `serverless init` 命令，下载相关 template。
```console
serverless init fullstack
```

2. 在项目根目录下新建 .env 文件，并在其中配置对应的腾讯云 SecretId、SecretKey、地域和可用区信息。
```text
# .env
TENCENT_SECRET_ID=xxx  // 您账号的 SecretId
TENCENT_SECRET_KEY=xxx // 您账号的 SecretKey

# 地域可用区配置
REGION=ap-guangzhou //资源部署区，该项目中指云函数与静态页面部署区
ZONE=ap-guangzhou-2 //资源部署可用区 ，该项目中指 DB 部署所在的可用区
```
 >?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，请保证您的账号已经授权了 AdministratorAccess 权限。 您可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
>- ZONE 目前只支持 ap-beijing-3 、ap-guangzhou-2、ap-shanghai-2。

3. 通过执行以下命令，安装所需依赖：
```bash
npm run bootstrap
```

### 部署

1. 执行 `sls deploy --all` 命令进行部署。返回信息如下所示：
<dx-codeblock>
:::  console
$ sls deploy --all

serverless ⚡ framework

serverlessVpc:
  region:     ap-guangzhou
  zone:       ap-guangzhou-2
  vpcId:      vpc-xxx
  vpcName:    serverless
  subnetId:   subnet-xxx
  subnetName: serverless

fullstackDB:
  region:         ap-guangzhou
  zone:           ap-guangzhou-2
  vpcConfig:
    subnetId: subnet-100000
    vpcId:    vpc-1000000
  dBInstanceName: fullstackDB
  dBInstanceId:   postgres-100000
  private:
    connectionString: postgresql://tencentdb_100000xxxxxxxxxxxxx@172.16.250.15:5432/tencentdb_1000000
    host:             172.16.250.15
    port:             5432
    user:             tencentdb_100000
    password:         xxxxxxxx
    dbname:           tencentdb_100000

fullstack-api:
  region: ap-guangzhou
  apigw:
    serviceId:   service-100000
    subDomain:   service-100000-123456789.gz.apigw.tencentcs.com
    environment: release
    url:         https://service-100000-123456789.gz.apigw.tencentcs.com/release/
  scf:
    functionName: fullstack-api
    runtime:      Nodejs10.15
    namespace:    default

fullstack-frontend:
  website: https://fullstack-serverless-db-123456789.cos-website.ap-guangzhou.myqcloud.com

50s › tencent-fullstack › Success 
:::
</dx-codeblock>

 部署成功后，您可以使用浏览器访问项目产生的 website 链接，即可看到生成的网站。
>?本项目云函数因 VPC，导致无法直接访问外网，如需访问外网请参考 [云函数网络配置]( https://cloud.tencent.com/document/product/583/38202 )。

2. 执行 `sls remove --all`，可移除项目。返回信息如下所示：
```bash
$  sls remove --all

serverless ⚡ framework

38s › tencent-fullstack › Success
```
