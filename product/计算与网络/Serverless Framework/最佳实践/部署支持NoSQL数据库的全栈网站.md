## 操作场景
该模板可以快速部署一个基于 **TCB NoSQL DB + SCF + Website** 的全栈 Serverless 应用。主要包含以下组件：  
- **Serverless Website：** 前端通过托管 html 静态页面到 COS 对象存储中。
- **Serverless Cloud Function：** 后端函数部署到云端，通过 HTTP 进行触发调用。
- **TCB 云开发环境：** 通过创建云开发环境并调用 NoSQL DB，为全栈网站提供数据库服务。
   
## 操作步骤
### 前提条件
请登录 [云开发 CloudBase 控制台](https://console.cloud.tencent.com/tcb/env/index)，确定您**没有创建过免费云开发环境**：
- 如果没有，无需任何操作
- 如果有，请记录该环境的环境 ID（如下图）

<img src="https://main.qcloudimg.com/raw/4f202c0e9192433ec9dcf40d222ab219.png" width="50%" height="50%">


### 安装
   
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：
```bash
$ npm install -g serverless
```
   
如果之前您已经安装过 Serverless Framework，可以通过下列命令升级到最新版：
```bash
$ npm update -g serverless
```
   
安装完毕后，通过运行`serverless -v`命令，查看 Serverless Framework 的版本信息，确保版本信息不低于以下版本：
```bash
$ serverless –v
Framework Core: 1.68.0
Plugin: 3.6.6
SDK: 2.3.0
Components: 2.30.1
```
   
### 配置
   
1. 通过 sls init 初始化模版：
```bash
$ sls init fullstack-nosql
```
>?
>- 如果没有腾讯云账号，请先[注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在[ API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取**SecretId**和**SecretKey**。
>- 目前 sls 支持在国内区域访问 TCB，部署时请注意 yaml 文件里的地域设置，其他地域可能会报错。
   
2. **如果您已有 tcb 免费环境：**（如果没有，请跳过此步骤）
	1. 删去 db 文件夹以及文件夹内的 yml 文件。
	2. 在 demo 目录中 **function->serverless.yaml** 中的 **MongoId** 参数里，输入您已有 TCB 环境的 ID。


3. 在`backend->src`文件夹目录下，通过以下命令安装所需依赖：
```bash
$ npm install
```
   
### 部署
配置完成后，进入项目根目录下，通过以下命令进行部署，创建一个新的云开发环境，将后台代码部署到云函数 SCF 平台，并通过 website 组件部署静态网站：
   
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
    Namespace:    default
    Runtime:      Nodejs8.9
    Handler:      index.main
    MemorySize:   128
    Triggers: 
      apigw: 
         - https://service-dlq65ccq-1258834142.gz.apigw.tencentcs.com/release/users

mongoDBDemoWebsite: 
   website: http://my-bucket-1258834142.cos-website.ap-guangzhou.myqcloud.com

78s › tcbdemo › Success

```
 访问命令行输出的 website url，即可查看您的 Serverless 站点。  
>!
>- 由于 sls 运行角色限制，需要用户登录 [访问管理角色页面](https://console.cloud.tencent.com/cam/role)，手动为**SLS_QcsRole**添加**TCBFullAccess**的策略，否则无法正常运行。
>- 当前`deploy --all`指令只支持2.30.1及以上版本 Serverless Framework Component，请确定您的组件已更新至最新版本。
>- 目前 TCB 端仅支持每月最多创建销毁4次环境，请谨慎创建，若超过4次部署将会报错。
   

   
### 移除
   
可通过以下命令移除项目：
   
```bash
$ sls remove --debug
```
   
#### 权限配置
TCB 组件支持扫码一键授权，您也可通过本地配置`.env`文件完成权限配置，具体步骤如下：
   
在项目根目录下中创建`.env`文件，在其中配置对应的腾讯云 SecretId 和 SecretKey 信息：
    
```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
        
#### 更多组件
您可在 [Serverless Component Repo](https://github.com/serverless/components) 中查看更多组件信息。
   
#### Q&A
**报错 "EnvId is invalid"是什么原因？**
   
TCB DB 组件目前默认为用户创建一个免费的 TCB 环境，如果您已有免费环境，通过 Serverless Component 再次创建会失败报错，您可删去 db 文件夹，通过配置  demo 目录中 **backend --> serverless.yml** 中的 **MongoId** 参数，输入您已有 TCB 环境的 ID，完成项目的部署。

