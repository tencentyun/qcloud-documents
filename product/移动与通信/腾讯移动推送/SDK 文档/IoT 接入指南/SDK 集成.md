本文介绍关于 SDK 的接入以及 demo 的使用方法。

## SDK 组成
SDK 目录文件和功能说明如下：

- application：应用入口及 API 使用样例。  
- doc： 源代码相关说明文档存放目录。
- include： SDK 头文件 xgAgent.h 存放目录。  
- lib： SDK 静态库 libxgIoT.a 存放目录。   
- Makefile： 工程管理文件。 
- README.md： SDK 使用说明。



## 使用方法
#### 编译

1. 进入 Demo 源码根目录，运行命令编译：
```
make
```
编译完成后，可在根目录查看 xgDemo 文件生成。
2. 清除编译文件，运行命令：
```
make clean
```


#### 启动 Demo
启动时需要将应用的 AccessID、AccessKey、deviceName 传入到测试应用，命令格式如下：
1. 按以下格式运行：
```
./xgDemo [accessID] [accessKey] [deviceName]
```
2. 当出现以下消息时，表示设备运行成功：
```xml
level":"D","message":"xgMqttRpcResult(811):cmd account "}
[20190909_20:14:44]{"time":"2019-0909-12:14:43.830","level":"D","message":"agentSetStatusFlag(297):xgStatusFlag 0x1F "}
```

#### 推送消息到 Demo
在控制台或使用 REST API 进行消息推送，当在 xgDemo 日志中看到以下内容，表示推送成功。

```xml
[20190909_20:15:22][demo Debug]$$$$$$$$$$$$$$$$$$$$$$$
[20190909_20:15:22][demo Debug]Recv data 39Byte: {"audience_type":"all","Key1":"Value1"}
```


## 集成步骤
1. 将 `lib/libxgIoT.a` 和 `include/xgAgent.h` 拷贝到自定义的源码目录中。
2. 修改 Makefile，在编译选项中添加以下代码：
```c
-lxgIoT -lpthread -lrt
```
3. 参考 application 目录下的 main.c 的代码，将 SDK 的 API 集成到自己的源码中。
