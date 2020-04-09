## 操作场景
该任务指导您通过 Serverless Framework，在腾讯云上快速创建、配置和部署一个 Serverless 应用。
>?预计2020年4月，Serverless Framework 将提供可视化的页面，您可以从 Serverless 应用的角度查看和管理资源。

## 前提条件
在使用之前，请确保已经 [安装 Serverless Framework 1.67.2 以上版本](https://cloud.tencent.com/document/product/1154/42990)。

## 操作步骤

在空文件夹下输入`serverless`命令，按照引导进行操作，即可部署一个 SCF、Express.js 或者静态网站托管应用。交互流程如下所示：

```
$ serverless
Serverless: 当前未检测到 Serverless 项目，是否希望新建一个项目？ (Y/n) y
Serverless: 请选择您希望创建的 Serverless 应用 (Use arrow keys)
❯ Express.js app 
  SCF Function 
  Website app 
Serverless: 请输入项目名称 tinatest

tinatest 项目已成功创建！
Serverless: 是否希望立即将该项目部署到云端？ (Y/n) y
Please scan QR code login from wechat. 
Wait login...
Login successful for TencentCloud. 

serverless ⚡ framework
Action: "deploy" - Stage: "dev" - App: "scfApp" - Instance: "scfdemo"

FunctionName: scfFunctionName
Description:  
Namespace:    default
Runtime:      Nodejs10.15
Handler:      index.main_handler
MemorySize:   128
Triggers: 
  apigw: 
    - https://service-9k0ggfbe-1250000000.gz.apigw.tencentcs.com/release/index

23s › scfdemo › Success
```

部署完毕后，访问命令行中输出的网页链接，即可访问已经部署成功的应用。
>?如果希望查看部署过程中的详细信息，可以增加`--debug`参数进行查看。


### 查看部署信息

如果希望再次查看应用的部署状态和资源，可以进入到部署成功的文件夹，运行如下命令，查看对应信息：

```
$ cd tinatest
$ sls info
```
>?sls 是 serverless 命令的简写。

### 开发调试

通过运行`sls dev`命令，可以开启部署的实时日志，该能力会自动监测本地代码的更新，并自动部署同步到云端，同时实时输出调用日志。针对 Node.js 10 的应用，还可以启用云端调试能力。详情参考 [Node.js 云端调试](https://cloud.tencent.com/document/product/1154/43220)。

```
$ cd tinatest
$ sls dev
```

### 移除项目

通过`sls remove`命令可以移除云端部署的所有资源，如下所示：

```
$ cd tinatest
$ sls remove

serverless ⚡ framework
Action: "remove" - Stage: "dev" - App: "scfApp" - Instance: "scfdemo"

6s › scfdemo › Success
```

>?如果希望查看移除过程中的详细信息，可以增加`--debug`参数进行查看。

### 配置账户信息（可选）

当前默认支持部署时扫描微信二维码登录，如您希望配置持久的环境变量/密钥信息，也可以参考 [配置账号](https://cloud.tencent.com/document/product/1154/43006) 文档。
