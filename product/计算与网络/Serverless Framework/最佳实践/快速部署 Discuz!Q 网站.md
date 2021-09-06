腾讯云 Serverless 提供了基于 Serverless 架构的 Discuz！Q 全新部署方式。通过 [Serverless Framework Discuz！Q 组件](https://github.com/serverless-components/tencent-discuzq)，您可以三分钟部署一个 Discuz！Q 项目来搭建属于您的社区和论坛。

## 架构简介
该组件主要为您创建以下资源：

| 模块 | 说明 | 
|---------|---------|
| 云函数 SCF | 负责 Serverless Discuz！Q 的接入层实现，从而运行 Discuz！Q。 |
| API 网关| Discuz！Q 的对外入口，实现了 RESTful API。 |
| 文件储存 CFS  | Discuz！Q 代码的挂载和存储仓库。 |
| 私有网络 VPC | 内网打通云函数 SCF、CFS 之间的网络，保障网络隔离。|


## 前提条件
- 已开通 [云函数 SCF 服务](https://console.cloud.tencent.com/scf)。
- 已开通 [文件存储 CFS 服务](https://console.cloud.tencent.com/cfs)。
- 已准备好您的数据库资源，注意配置好网络环境，推荐使用 [TDSQL-C Serverless MySQL 数据库](https://cloud.tencent.com/document/product/1003/50853)。
- （可选）准备好已备案的自定义域名，您也可以通过 Serverless 备案资源包完成备案，详情请参见 [ICP 备案](https://cloud.tencent.com/document/product/1154/50706)。

## 部署步骤
您可以通过**控制台**或**命令行**完成 Serverless Discuz！Q 部署，步骤如下：



### 控制台部署

1. 登录[ Serverless 应用控制台](https://console.cloud.tencent.com/sls?from=wpdocs)，单击**新建应用**。
2. 选择**应用市场** > **快速部署一个Discuz！Q框架**，单击**下一步**。
![](https://main.qcloudimg.com/raw/c93aec460abf0909fe586f3c867b39e4.png)
3. 输入应用名，单击**完成**即可完成应用创建。
![](https://main.qcloudimg.com/raw/d0ca3501aed949fd2e530ceac6c5f9e5.png)
4. 在 Serverless 应用页，单击**安装应用**，按照页面提示，安装您的 Discuz！Q 项目，完成数据库配置、账号密码创建等操作。
>! 请保证您绑定的数据库必须和应用本身在同一个 VPC 网络环境下，如果没有数据库实例，您可以参考 [TDSQL-C Serverless MySQL 数据库](https://cloud.tencent.com/document/product/1003/50853) 文档，创建一个 Serverless 数据库并完成绑定。
![](https://main.qcloudimg.com/raw/5be323ac9c9264443ad555dfa1c36ed5.png)
5. 完成安装后，单击**“访问应用”**，输入您的账户名和密码，即可访问您的 Discuz！Q 论坛。
![](https://main.qcloudimg.com/raw/d89eee226f9dc5f125a6ea2a26d916e1.png)
6. 部署后，您也可以单击您的应用名称，查看资源列表和部署日志。在资源列表页，您可以单击**新增**配置您的自定义域名。
![](https://main.qcloudimg.com/raw/ef07a567abf3524586a72bb1c116ecbf.png)

### 命令行部署

1. 本地创建 `discuzq-demo` 文件夹。
2. 在文件夹内创建 `serverless.yml` 配置文件，完成应用信息配置，参考如下：
<dx-alert infotype="explain" title="">
更多配置内容，请参见 [全量配置文档](https://github.com/serverless-components/tencent-discuzq/blob/main/docs/configure.md)。
</dx-alert>
<dx-codeblock>
:::  yaml
app: discuz-q
stage: dev
component: discuz-q
name: discuz-qDemo
:::
</dx-codeblock>
完成后，您的项目结构如下：
<dx-codeblock>
:::  sh
.discuzq-demo
├── serverless.yml # 配置文件
└── .env # 环境变量文件
:::
</dx-codeblock>
3. 在根目录下，执行 `sls deploy`，即可完成部署。示例如下：
<dx-codeblock>
:::  sh
$ sls deploy

serverless ⚡components
Action: "deploy" - Stage: "dev" - App: "discuz-q" - Name: "discuz-qDemo"

region:        ap-shanghai
zone:          ap-shanghai-2
vpc: 
  region:     ap-shanghai
  zone:       ap-shanghai-2
  ...
cfs: 
  region:       ap-shanghai
  ...
  vpc: 
    ...
apigw: 
  created:     true
  ...
  apis: 
    ...
layer: 
  region:      ap-shanghai
  description: Created by Serverless Component
  ...
  runtimes: 
    - Php7
  version:     1
dzqInitFaas: 
  ...
dzqServerFaas: 
  ...
  layers: 
    ...
:::
</dx-codeblock>
4. 部署成功后，单击 `apigw` 部分输出的 URL，根据指引完成账号密码配置，即可开始使用您的 Discuz！Q 应用。
