> TSF Serverless目前出于内测阶段，欢迎填写[使用申请](https://cloud.tencent.com/apply/p/om62iz2gqx)。

您可以通过[TSF Serverless 简介](xxxx)了解更多信息，体验 [快速入门](xxxx)，掌握 TSF Serverless 完整的使用流程。

## 监听端口

当前TSF Serverless主要支持南北向 Web 服务场景，您的程序需要主动**监听8080端口**。

## 上传程序包要求

目前 Serverless应用支持的程序包格式包括 **tar.gz 和 zip**。

tar.gz和zip压缩包中需要包含以下内容，**请确保文件名正确**：

- 业务代码**（必须）**：压缩包中需要包含程序运行所需的**全部依赖包（eg. node_modules）**。您的程序必须**监听8080端口**。

- start.sh**（必须）**：启动脚本。我们会通过运行启动脚本拉起您的程序。您可以把启动服务所需的参数填入启动脚本。需要注意的是，启动脚本需要放在**压缩包的根路径下**。以下是一个示例启动脚本：

  ```bash
  #! /bin/bash
  
  node index.js
  ```

- stop.sh**（可选）**：停止脚本。我们会通过运行停止脚本来终止程序运行。需要注意的是，停止脚本需要放在**压缩包的根路径下**。以下是一个示例停止脚本：
  ```bash
  #! /bin/bash
  
  pid=`ps -ef | grep "node index" | grep -v grep | awk '{print $2}'`
  kill -SIGTERM $pid
  ```
	
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

#### 

## 本地临时存储

- 如果您需要在本地写临时文件，只能写到 `/tmp` 路径下，其他路径下写操作会失败。
- `/tmp` 路径下空间有限，您需要定时清理。

