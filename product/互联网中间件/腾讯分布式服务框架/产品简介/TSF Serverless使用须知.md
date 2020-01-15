> TSF Serverless目前出于内测阶段，欢迎填写[使用申请](https://cloud.tencent.com/apply/p/om62iz2gqx)。

您可以通过[TSF Serverless 简介](xxxx)了解更多信息，体验 [快速入门](xxxx)，掌握 TSF Serverless 完整的使用流程。

## 监听端口

当前 TSF Serverless 主要支持东西向调用场景Spring Cloud，Mesh无需监听端口。兼容南北向调用，南北向 Web 服务场景下暂时不支持东西向功能，使用南北向访问您的程序需要主动监听8080端口。

## 上传程序包要求

目前 Serverless应用支持的程序包格式包括 **tar.gz 和 zip**。

tar.gz和zip压缩包中需要包含以下内容，**请确保文件名正确**：

- 业务代码**（必须）**：压缩包中需要包含程序运行所需的**全部依赖包（eg. node_modules）**。您的程序必须**监听8080端口**。

- start.sh**（必须）**：启动脚本。我们会通过运行启动脚本拉起您的程序。您可以把启动服务所需的参数填入启动脚本。需要注意的是，启动脚本需要放在**压缩包的根路径下**。以下是一个示例启动脚本：

  ```bash
  #! /bin/bash
  
  node index.js
  ```

- stop.sh**（必须）**：停止脚本。我们会通过运行停止脚本来终止程序运行。需要注意的是，停止脚本需要放在**压缩包的根路径下**。以下是一个示例停止脚本：
  ```bash
  #! /bin/bash
  
  pid=`ps -ef | grep "node index" | grep -v grep | awk '{print $2}'`
  kill -SIGTERM $pid
  ```

- cmdline**（必填）**：用于检查应用进程是否存在。cmdline 检测进程脚本，agent 通过ps -ef | grep 'cmdline 内容'来检测进程是否存在，示例如下：：
```bash
node index.js
```

 [更多cmdline介绍](https://cloud.tencent.com/document/product/649/30359)
	
以 node.js 为例,程序包结构如下：

```
.
├── node_modules  
├── index.js            
├── package.json
├── start.sh          //   启动脚本
└── stop.sh          //    停止脚本
```

您需要**在项目的根路径（start.sh所在路径）下**执行打包命令：

```bash
zip code.zip * -r
```

## 本地临时存储

- 如果您需要在本地写临时文件，只能写到 `/tmp` 路径下，其他路径下写操作会失败。
- `/tmp` 路径下空间有限，您需要定时清理。

## 日志采集
- 当前 TSF Serverless 只支持从 **stdout** 采集日志，例如 console.log() 方式打印的日志。
- 如果您的程序原先是输出日志到本地日志文件，则需要调整输出位置到 **stdout**。
- 我们后续（2019年12月左右）会通过开放日志配置项，来支持从本地日志文件采集日志。


## 旧版部署组/应用迁移相关

为提供更好的服务并全面支持微服务平台相关能力，我们在[1.19.0](https://cloud.tencent.com/document/product/649/19020)版本中对Serverless 应用及部署组进行了升级。关于历史部署组，有以下几点需要注意：

历史部署组上的业务可照常运行。但为了保证您能享受新版本功能，我们强烈建议您重新创建部署组，并对旧版部署组做迁移。点击<部署组> - <新建部署组>即可。
[1.19.0](https://cloud.tencent.com/document/product/649/19020)版本后默认历史集群不可新建部署组，请重新创建并选择新的集群进行操作
[1.19.0](https://cloud.tencent.com/document/product/649/19020)版本后的访问管理入口将从<应用>迁移到<部署组>，
> 如果需要查看历史部署组的域名，您可以通过登录API网关控制台，基于TSF应用名查找对应API网关。
如：旧版应用名为 demo ，则对应API网关的默认域名为 demo-<appid>.<region>.apigw.tencentcs.com
[1.19.0](https://cloud.tencent.com/document/product/649/19020) 版本后Serverless应用的程序包需同时包含start.sh，stop.sh，cmdline三个文件，详见 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359) 。

#### 部署组迁移指引：

1. 新建Serverless部署组
注意:历史部署组不可直接创建Serverless集群
![](https://main.qcloudimg.com/raw/ff452959fb414689c1f615d87dba5bd8.png)
2. 新建Serverless应用
![](https://main.qcloudimg.com/raw/69940f64bed2f94ec1953abd94cef6c9.png)
3. 上传程序包
注意:本次程序包上传必须同时**包含start.sh，stop.sh，cmdline**，详见 [上传程序包要求](https://cloud.tencent.com/document/product/649/30359)
![](https://main.qcloudimg.com/raw/44dbab3118490a90bf3be3eee54d6bc6.png)
4. 新建Serverless部署组
![](https://main.qcloudimg.com/raw/66e93be226b92ffc65be7b4ed2ee7790.png)
5. 部署应用
![](https://main.qcloudimg.com/raw/0891c58b8349a4f3ab8848fabb393839.png)
6. 开启外网访问
注意:外网访问已迁移至部署组维度
![](https://main.qcloudimg.com/raw/3283f0002c3359e315609ab7e8ec14fb.png)