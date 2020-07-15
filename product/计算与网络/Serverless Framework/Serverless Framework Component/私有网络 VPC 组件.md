## 操作场景
腾讯云 VPC 组件支持通过`serverless.yml`配置，快速创建指定名称的私有网络和子网，并输出 VPCID 和 SubnetID，便于配置其他组件所需的网络信息。

## 操作步骤
### 安装

 通过 npm 安装最新版本的 Serverless Framework： 

```shell
$ npm install -g serverless
```

### 配置
新建一个目录 vpcDemo，在 vpcDemo下创建`serverless.yml`文件：

```shell
$ mkdir vpcDemo && cd vpcDemo
$ touch serverless.yml
```
在`serverless.yml`中进行如下配置：
```yml
# serverless.yml
org: orgDemo # (可选) 用于记录组织信息，默认值为您的腾讯云账户 appid.
app: appDemo # (可选) 该VPC应用名称.
stage: dev # (可选) 用于区分环境信息，默认值是 dev.

component: vpc #  (必填) 引用 component 的名称，当前用到的是 tencent-vpc 组件.
name: vpcDemo # (必填) 该组件创建的实例名称.

inputs:
  region: ap-guangzhou
  zone: ap-guangzhou-2
  vpcName: serverless
  subnetName: serverless
```
[查看详细配置文档 >>](https://github.com/serverless-components/tencent-vpc/blob/master/docs/configure.md )

### 部署

运行 sls deploy 进行部署：

```bash
$ sls deploy
serverless ⚡ framework
Action: "deploy" - Stage: "dev" - App: "appDemo" - Instance: "vpcDemo"

region:     ap-guangzhou
zone:       ap-guangzhou-2
vpcId:      vpc-xxxxxxxx
vpcName:    serverless
subnetId:   subnet-xxxxxxxx
subnetName: serverless


3s › vpcDemo › Success
```

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

>?`sls`是`serverless`命令的简写。

### 查看信息

运行 `sls info` 进行查看部署成功的信息：

```bash
$ sls info

serverless ⚡ framework

Status:       active
Last Action:  deploy (5 minutes ago)
Deployments:  2

region:     ap-guangzhou
zone:       ap-guangzhou-2
vpcId:      vpc-xxxxxxx
vpcName:    serverless
subnetId:   subnet-xxxxxxx
subnetName: serverless

vpcDemo › Info successfully loaded
```


### 移除

通过以下命令移除部署的 VPC：

```bash
$ sls remove

serverless ⚡ framework
Action: "remove" - Stage: "dev" - App: "appDemo" - Instance: "vpcDemo"

6s › vpcDemo › Success
```

### 账号配置（可选）
当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建`.env`文件：

```bash
$ touch .env # 腾讯云的配置信息
```

在`.env`文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：
```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和SecretKey。

