## 操作场景
该教程指导您通过 Serverless Framework 组件，快速创建一个 TDSQL-C Serverless 数据库实例。


## 操作步骤
### 1. 安装 Serverless Framework

通过 npm 全局安装最新版本的 Serverless Framework：

```bash
$ npm install -g serverless
```

### 2. 创建新目录

创建并进入一个全新目录：

```bash
$ mkdir tencent-tdsqlc && cd tencent-tdsqlc
```

### 3. 配置文件

在新目录下创建 `serverless.yml` 文件：
```bash
$ touch serverless.yml
```
在 `serverless.yml` 文件中进行如下配置（[查看全量配置](https://github.com/serverless-components/tencent-cynosdb/tree/master/docs/configure.md)）：
```yml
# serverless.yml
component: cynosdb
name: cynosdbDemo

inputs:
  region: ap-guangzhou
  zone: ap-guangzhou-4
  vpcConfig:
    vpcId: vpc-xxx
    subnetId: subnet-xxx
```

>!当前仅支持**北京三区、广州四区、上海二区、南京一区**四个地域的创建和部署，因此在填写 yaml 中的地域可用区时需要填写为正确的地域和对应的 VPC 子网信息。

### 4. 部署

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过 `sls` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息。

```bash
$ sls deploy
```
>?`sls` 命令是 `serverless` 命令的缩写。
>
部署完成后，可以在命令行看到创建的数据库实例信息：
<img src="https://main.qcloudimg.com/raw/66e70fa9bf9147ff55790db19767dc78.png" width="70%">


#### 4.1 开启外网访问

如果需要数据库实例开启外网访问，只需添加 `enablePublicAccess` 配置为 `true`，如下：
<dx-codeblock>
:::  yml
# serverless.yml
app: appDemo
stage: dev
component: cynosdb
name: cynosdbDemo

inputs:
  region: ap-guangzhou
  zone: ap-guangzhou-4
  enablePublicAccess: true
  vpcConfig:
    vpcId: vpc-xxx
    subnetId: subnet-xxx
:::
</dx-codeblock>


然后重新执行部署：

```bash
$ sls deploy
```

#### 4.2 重置密码

组件只支持重置 `root` 用户密码。例如，需要将密码重置为 `123456@abc` 只需运行如下命令：

```bash
$ sls resetpwd --inputs adminPassword=123456@abc
```

### 5. 查看状态

在 `serverless.yml` 文件所在的目录下，通过如下命令查看部署状态：

```bash
$ sls info
```

### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```bash
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：

```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果没有腾讯云账号，可以在此 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。
