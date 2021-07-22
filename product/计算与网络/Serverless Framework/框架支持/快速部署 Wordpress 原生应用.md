腾讯云 Serverless 提供了基于 Serverless 架构的 Wordpress 全新部署方式，通过 [Serverless Framework Wordpress 组件](https://github.com/serverless-components/tencent-wordpress) ，仅需几步，就可以快速部署一个 Wordpress 项目。

## 架构简介
该组件主要为您创建以下资源：

| 模块 | 说明 | 
|---------|---------|
| 云函数 SCF | 负责 Serverless Wordpress 的接入层实现，从而运行 WordPress |
| API 网关| WordPress 的对外入口，实现了 RESTful API |
| CFS  | WordPress 的 Serverless 存储仓库 |
| <nobr>TDSQL-C Serverless</nobr> | 通过创建 TDSQL-C Serverless (原 CynosDB) 的 MySQL 类型数据库，实现数据库按量计费，自动扩缩容|
| VPC | 内网打通 SCF 云函数、CFS、TDSQL-C Serverless 之间的网络，保障网络隔离 |

## 功能优势
- **支持 Wordpress 原生框架**
使用 Serverless Wordpress 组件，您无需对原生 Wordpress 项目进行任何改造，即可直接完成部署，做到对框架无入侵，也支持后续的版本升级。
- **降低使用成本**
从接入层到计算层到存储层，全部使用 Serverless 资源，真正做到按量计费，弹性伸缩，极大节省成本。
- **部署步骤简单**
通过 Serverless Wordpress 组件，只需几行 YAML 文件配置，即可快速完成 Wordpress 应用部署，极大降低部署门槛。
>?新用户第一次部署 Wordpress 应用，即可获得**30元 TDSQL-C** 和**5元 CFS 文件存储**代金券，欢迎免费体验。

## 部署步骤
您可以通过**命令行**或**控制台**完成 Serverless Wordpress 部署，步骤如下：

### 前提条件
- 已开通 [云函数 SCF 服务](https://console.cloud.tencent.com/scf)。
- 已开通 [文件存储 CFS 服务](https://console.cloud.tencent.com/cfs)。
- （可选）准备好已备案的自定义域名，您也可以通过 Serverless 备案资源包完成备案（详情请参见 [ICP 备案](https://cloud.tencent.com/document/product/1154/50706)）。

### 控制台部署
>!目前只支持北京、广州、南京、上海四个区域。

1. 登录[ Serverless 应用控制台](https://console.cloud.tencent.com/sls?from=wpdocs), 单击【新建应用】。
2. 根据指引，填入应用名称，选择【应用模版】>【Wordpress 应用】，单击【创建】既可以完成应用新建。
![](https://main.qcloudimg.com/raw/ced891781e651e85d0c1cf5f2947ebf3.png)
3. 在 Serverless 应用页，单击【访问应用】，即可访问您的 Wordpress 项目，您也可以在应用详情页完成自定义域名的配置。
![](https://main.qcloudimg.com/raw/979fd2eead22b5a4a888f946db836737.png)

### 命令行部署
>!目前只支持 `ap-guangzhou-4`、`ap-shanghai-2`、`ap-beijing-3`、`ap-nanjing-1` 四个可用区。

1. 本地创建 `wordpress-demo` 文件夹，在 [Wordpress 官网](https://wordpress.org/download/) 下载应用到该文件夹内。
2. 在文件夹内创建 `serverless.yml` 配置文件，完成应用信息配置，参考如下（更多配置内容，请参见 [全量配置文档](https://github.com/serverless-components/tencent-wordpress/blob/master/docs/configure.md)）：
<dx-codeblock>
:::  yaml
app: wordpress
stage: dev
component: wordpress
name: wordpressDemo
inputs: 
  region: ap-shanghai # 项目所在区域
  zone: ap-shanghai-2
  src: #  项目路径，选择您的 wordpress 路径
     src: ./wordpress
     exclude: 
       - .env
  apigw: #  api网关配置
    customDomains: # （可选）自定义域名绑定
      - domain: abc.com # 待绑定的自定义的域名
        certId: abcdefg # 待绑定自定义域名的证书唯一 ID
        customMap: true # 是否自定义路径
        pathMap: 
          - path: /
            environment: release
        protocols: # 绑定自定义域名的协议类型，默认与服务的前端协议一致。
          - http
          - https
:::
</dx-codeblock>
完成后，您的项目结构如下：
<dx-codeblock>
:::  sh
.wordpress-demo
├── wordpress # wordpress 源文件
├── serverless.yml # 配置文件
└── .env # 环境变量文件
:::
</dx-codeblock>
3. 在根目录下，执行 `sls deploy`，即可完成部署。示例如下：
<dx-codeblock>
:::  sh
$ sls deploy
serverless ⚡framework
Action: "deploy" - Stage: "dev" - App: "appDemo" - Instance: "wordpressDemo"
region:       ap-shanghai
zone:         ap-shanghai-2
vpc: 
  ...
cfs: 
  ...
db: 
  ...
apigw: 
  created:     true
  url:         https://service-xxxxx.sh.apigw.tencentcs.com/release/
  ...
layer: 
  ...
wpInitFaas: 
  ...
wpServerFaas: 
  ...
:::
</dx-codeblock>
4. 部署成功后，单击 `apigw` 部分输出的 URL，根据指引完成账号密码配置，即可开始使用您的 Wordpress 应用。


## 常见问题


#### 权限问题导致部署失败该如何处理？

- 主账号/子账号需确认是否有以下权限：
	- 确认角色：**SCF_QcsRole、SLS_QcsRole、CODING_QcsRole**
	- 确认权限：
		- SCF_QcsRole 须拥有 **CFSFullAccess** 权限
		- CODING_QCSRole 须拥有 **QcloudSLSFullAccess、QcloudSSLFullAccess、QcloudAccessForCODINGRole** 权限
- 子账号还需确认以下权限：
账号本身有 **SLS、SCF、CFS、CynosDB、CODING** 使用权限。



#### 绑定自定义域名后，显示报错 {"message":"There is no api match env_mapping '\/'"}？

在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service?rid=1) 修改自定义映射，如下图所示：
![](https://main.qcloudimg.com/raw/b6bbb75df052e307e8abb4e82e500c3b.png)



#### 如何通过修改 php.ini 修改上传文件大小限制？

1. 修改 layer 代码。将 etc 文件夹中的 php.ini 文件移到 etc/php.d 文件夹下，您也可以直接使用我们提供的 [压缩包](https://github.com/serverless-components/tencent-wordpress/blob/master/src/fixtures/layer/wp-layer.zip)。
重新打包上传 layer 时，注意打包层级结构，只打包父文件夹下的文件，否则会出现函数初始化失败：
![](https://main.qcloudimg.com/raw/46fcf29a9f846b84db0c0a19fe65ce35.png)
2. 按照如下修改 wp-server-xxx 函数的 bootstrap 代码：
```
#!/bin/bash
export PATH="/opt/bin:$PATH"
export LD_LIBRARY_PATH=/opt/lib/:$LD_LIBRARY_PATH
export PHP_INI_SCAN_DIR=/opt/etc/php.d
php -d extension_dir=/opt/lib/php/modules/ sl_handler.php 1>&2
```


#### 如何处理报错 "event too large"？

函数目前只支持最大**6MB**的事件上传，超过该大小文件不支持上传。

目前 API 网关 base 64转码会将用户本身代码大小扩大1.5倍左右，因此上传文件时，建议文件大小控制在**3.5MB**以内。


#### 如何修改 Wordpress 根目录文件？

目前文件挂载在文件存储 CFS 上，无法直接修改，建议通过安装 File Manager 插件管理根目录文件。

