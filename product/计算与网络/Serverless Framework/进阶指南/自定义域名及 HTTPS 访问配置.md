## 操作场景
通过 Serverless Component 快速构建一个 Serverless Web 网站服务后，如果您希望配置自定义域名及支持 HTTPS 的访问，则可以按照本文提供的两种方案快速配置。 

## 前提条件
- 已经部署了网站服务，获取了 COS/API 网关的网站托管地址。具体部署方法参考 [部署 Vue.js+Express.js 全栈应用](https://cloud.tencent.com/document/product/1154/39272) 或 [快速部署 Hexo 博客](https://cloud.tencent.com/document/product/1154/40217)。
- 已拥有自定义域名（例如 www.example.com），并确保输入的域名已 [备案](https://cloud.tencent.com/product/ba)。
- 如果需要 HTTPS 访问，可以申请证书并且 [获得证书 ID](https://console.cloud.tencent.com/ssl) （例如：certificateId : axE1bo3），个人站点可以直接申请 [域名型（DV）免费 SSL 证书](https://cloud.tencent.com/document/product/400/8422)。



## 方案一：通过 CDN 加速配置支持自定义域名的 HTTPS 访问
配置前，需要确保账号实名并已经 [开通 CDN 服务](https://console.cloud.tencent.com/cdn)。

### 增加配置

在 `serverless.yml` 中，增加 CDN 自定义域名配置：
```yml         
# serverless.yml

component: website
name: myWebsite
app: websiteApp
stage: dev

inputs:
   src:
     src: ./public
     index: index.html
     error: index.html
   region: ap-guangzhou
   bucketName: my-hexo-bucket
   protocol: https
   # 新增的 CDN 自定义域名配置
   hosts:
     - host: www.example.com # 希望配置的自定义域名
       https:
         switch: on
         http2: off
         certInfo:
           certId: 'abc'
           # certificate: 'xxx'
           # privateKey: 'xxx'

```
[查看完整配置项说明 >>](https://github.com/serverless-components/tencent-website/blob/master/docs/configure.md)

### 部署服务
再次通过 `sls deploy` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息。

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。
>?`sls` 是 `serverless` 命令的简写。

```bash
$ sls deploy 
  
    myWebsite: 
      url:  https://my-hexo-bucket-1250000000.cos-website.ap-guangzhou.myqcloud.com
      env: 
      host: 
        - https://www.example.com (CNAME: www.example.com.cdn.dnsv1.com）
    17s › myWebsite › done
```
### 添加 CNAME
部署完成后，在命令行的输出中可以查看到一个以 `.cdn.dnsv1.com` 为后缀的 CNAME 域名。参考 [CNAME 配置文档](https://cloud.tencent.com/document/product/228/3121)，在 DNS 服务商处设置好对应的 CNAME 并生效后，即可访问自定义 HTTPS 域名。

## 方案二：对 API 网关域名进行自定义域名配置
### 增加配置
在 `serverless.yml` 中，增加 API 网关自定义域名配置。本文以 egg.js 框架为例，配置如下：
```yml
# serverless.yml

component: apigateway # (必填) 组件名称，此处为 apigateway
name: restApi # (必填) 实例名称
app: appDemo # (可选) 该应用名称
stage: dev # (可选) 用于区分环境信息，默认值为 dev

inputs:
   region: ap-shanghai
   protocols:
     - http
     - https
   serviceName: serverless
   environment: release
   customDomains:
     - domain: www.example.com
       # 如要添加 https，需先行在腾讯云 - SSL 证书进行认证获取 cettificateId
       certificateId: abcdefg
       protocols:
         - http
         - https
   endpoints:
     - path: /users
       method: POST
       function:
         functionName: myFunction # 网关所连接函数名
        
```
[查看完整配置项说明 >>](https://github.com/serverless-components/tencent-apigateway/blob/master/docs/configure.md)
### 部署服务
再次通过 `sls deploy` 命令进行部署，并可以添加 `--debug` 参数查看部署过程中的信息。
如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。
>? `sls` 是 `serverless` 命令的简写。

```bash
$ sls deploy 
    restApi: 
      protocols: 
        - http
        - https
      subDomain:     service-lqhc88sr-1250000000.sh.apigw.tencentcs.com
      environment:   release
      region:        ap-shanghai
      serviceId:     service-lqhc88sr
      apis: 
        - 
          path:   /users
          method: POST
          apiId:  api-e902tx1q
      customDomains: 
        - www.example.com (CNAME: service-lqhc88sr-1250000000.sh.apigw.tencentcs.com) 
    8s › restApi › done
```
### 添加 CNAME 记录
部署完成后，在命令行的输出中可以查看到一个以 `.apigw.tencentcs.com` 为后缀的 CNAME 域名。参考 [添加 CNAME 记录](https://cloud.tencent.com/document/product/302/3450)，在 DNS 服务商处设置好对应的 CNAME 并生效后，即可访问自定义 HTTPS 域名。



