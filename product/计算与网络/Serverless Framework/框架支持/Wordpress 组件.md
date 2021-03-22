腾讯云 Serverless 提供了基于 Serverless 架构的 Wordpress 全新部署方式，通过 [Serverless Framework Wordpress 组件](https://github.com/serverless-components/tencent-wordpress) ，仅需几步，就可以快速部署一个 Wordpress 项目。

## 架构简介
该组件主要为您创建以下资源：

| 模块 | 说明 | 
|---------|---------|
| 云函数 SCF | 负责 Serverless Wordpress 的接入层实现，从而运行 WordPress |
| API 网关| WordPress 的对外入口，实现了 RESTful API |
| CFS  | WordPress 的 Serverless 存储仓库 |
| <nobr>TDSQL-C Serverless</nobr> | 通过创建 TDSQL-C Serverless (原 CynosDB) 的 MySQL 类型数据库，实现数据库按量计费，自动扩缩容|
| VPC | 内网打通SCF云函数、CFS、TDSQL-C Serverless之间的网络，保障网络隔离 |

## 功能优势
- **支持 Wordpress 原生框架**
使用 Serverless Wordpress 组件，您不需要对原生 Wordpress 项目进行任何改造，即可直接完成部署，做到对框架无入侵，也支持后续的版本升级。

- **降低使用成本**
从接入层到计算层到存储层，全部使用 Serverless 资源，真正做到按量计费，弹性伸缩，极大节省成本。

 示例：以一个个人博客网站为例，设定日访问量100、1GB文件存储、1GB数据库存储，每月费用如下：
<table>
<thead>
<tr>
<th>计费项</th>
<th>费用说明</th>
</tr>
</thead>
<tbody><tr>
<td>API 网关</td>
<td>调用次数：100 ÷ 10000 × 0.06 × 30 = 0.018元/月<br>出流量：100 ÷ 30 ÷ 1024 ÷ 1024 × 0.8 × 30 = 0.068元/月</td>
</tr>
<tr>
<td>SCF 云函数</td>
<td>SCF 调用次数：100 × 30=3000次/月 免费额度内，不产生费用<br>SCF 资源使用费用：30 × 1000 × 100 × 30 = 90GBs/月 免费额度内，不产生费用</td>
</tr>
<tr>
<td>CFS 存储费用（月费用）</td>
<td>1 × 0.35 = 0.35元/月</td>
</tr>
<tr>
<td><nobr>Serverless MySQL 数据库</nobr></td>
<td>存储费用：1 × 0.00485元/GB/小时 × 24 × 30=3.49元/月<br> 计算费用：100 × 0.000095 × 30 = 0.285元/月</td>
</tr>
<tr>
<td colspan="2" style="text-align:center;">费用合计：0.018 + 0.068 + 0.35 + 3.49 + 0.285 = 4.211元</td>
</tr>
</tbody></table>
   对比可以发现，与传统自建方案对比，Serverless Wordpress 使用成本极大降低。



- **部署步骤简单**
通过 Serverless Wordpress 组件，只需几行 yml 文件配置，即可快速完成 Wordpress 应用部署，极大降低部署门槛。
>?新用户第一次部署 Wordpress 应用，即可获得 **30元 TDSQL-C**和**5元 CFS 文件存储**代金券，欢迎免费体验。

## 部署步骤
您可以通过**命令行**或**控制台**完成 Serverless Wordpress 部署，步骤如下：

### 部署前提
- 开通 [云函数 SCF 服务](https://console.cloud.tencent.com/scf)
- 开通 [文件存储 CFS 服务](https://console.cloud.tencent.com/cfs)
- （可选）准备好已备案的自定义域名，您也可以通过 Serverless 备案资源包完成备案（参考 [ICP 备案](https://cloud.tencent.com/document/product/1154/50706)）

### 控制台部署
>!目前只支持北京、广州、南京、上海四个区域。

1. 登录[ Serverless 应用控制台](https://console.cloud.tencent.com/sls?from=wpdocs), 单击【新建应用】。
2. 根据指引，填入应用名称，选择"应用模版"--"Wordpress 应用"，单击【创建】既可以完成应用新建。
![](https://main.qcloudimg.com/raw/ced891781e651e85d0c1cf5f2947ebf3.png)
3. 在 Serverless 应用页，单击【访问应用】，即可访问您的 Wordpress 项目，您也可以在应用详情页完成自定义域名的配置。
![](https://main.qcloudimg.com/raw/979fd2eead22b5a4a888f946db836737.png)

### 命令行部署
>!目前只支持 `ap-guangzhou-4`、`ap-shanghai-2`、`ap-beijing-3`、`ap-nanjing-1` 四个可用区。

1. 本地创建 `wordpress-demo` 文件夹，在 [Wordpress 官网](https://wordpress.org/download/ )下载应用到该文件夹内。
2. 在文件夹内创建 `serverless.yml` 配置文件，完成应用信息配置，参考如下（更多配置内容，请参考 [全量配置文档](https://github.com/serverless-components/tencent-wordpress/blob/master/docs/configure.md)）：
<dx-codeblock>
:::  yml
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
```
.wordpress-demo
├── wordpress # wordpress 源文件
├── serverless.yml # 配置文件
└── .env # 环境变量文件
```

3. 在根目录下，执行 `sls deploy`，即可完成部署。
<dx-codeblock>
:::  yml
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
部署成功后，点击 `apigw` 部分输出 url，根据指引完成账号密码配置，即可开始使用您的 Wordpress 应用。
