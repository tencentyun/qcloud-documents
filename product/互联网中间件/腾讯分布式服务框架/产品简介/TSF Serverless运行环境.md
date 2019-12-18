目前，TSF serverless 支持的运行环境如下，可在创建应用时选取所需的运行环境：

* Java 8
* Golang 1
* Python 2.7  
* Python 3.6  
* Nodejs 8.9
* Nodejs 10.15

## 执行方法

目前，支持程序包上传的方式运行环境。通过添加 start.sh 启动脚本来拉起程序，您可以把启动服务所需的参数填入启动脚本。需要注意的是，启动脚本需要放在压缩包的根路径下。以 Java 为例启动脚本如下：

```
#!/bin/bash
java -classpath ./ HelloWorld
```

相应的上传的程序包路径如下所示：

```
.
├── HelloWorld$TestHandler.class
├── HelloWorld.class 
├── HelloWorld.java
└── start.sh            //    启动脚本
```

## 示例下载

TSF serverless 提供各个版本的demo示例包与 start.sh 书写规范，可直接在上传程序包中下载使用示例，或者点击下发链接下载：


|运行环境|下载地址|
| -------------------------------- |---------------|
| Java 8                | [点击下载](https://gzdemotsfs-1253665819.cos.ap-guangzhou.myqcloud.com/helloworld/Java8-helloworld.zip) |
| Golang 1             |[点击下载](https://gzdemotsfs-1253665819.cos.ap-guangzhou.myqcloud.com/helloworld/Golang1-helloworld.zip)|
| Python 2.7                 |[点击下载](https://gzdemotsfs-1253665819.cos.ap-guangzhou.myqcloud.com/helloworld/Python2.7-helloworld.zip)|
| Python 3.6                   |[点击下载](https://gzdemotsfs-1253665819.cos.ap-guangzhou.myqcloud.com/helloworld/Python3.6-helloworld.zip)|
| Nodejs 8.9        |[点击下载](https://gzdemotsfs-1253665819.cos.ap-guangzhou.myqcloud.com/helloworld/Nodejs8.9-helloworld.zip)|
| Nodejs 10.15                |[点击下载](https://gzdemotsfs-1253665819.cos.ap-guangzhou.myqcloud.com/helloworld/Nodejs10.15-helloworld.zip)|


## 更多指引
您可参考以下文档，使用相关功能：
- [TSF Serverless 使用须知](https://cloud.tencent.com/document/product/649/38960)
- [使用 CLI 快速创建并部署 Serverless 应用](<https://cloud.tencent.com/document/product/649/39890>)




