## 概述

LogListener 是日志服务提供的日志采集客户端，通过安装部署 LogListener，可以方便快速地接入日志服务，无需修改应用程序运行逻辑，是一种对应用服务无侵入式的采集方式。

使用 LogListener 采集日志的流程如下图所示：

![image](https://main.qcloudimg.com/raw/43ddc189f8e4019616fbd1d6e1502a8e.jpg)

## 流程说明

1. 下载安装最新版本 [LogListener](https://cloud.tencent.com/document/product/614/17414)。LogListener 成功安装后将自动启动进程，并与日志服务后端保持心跳连接。
2. 前往 [日志服务控制台](https://console.cloud.tencent.com/cls)，创建 [机器组](https://cloud.tencent.com/document/product/614/17412)，并添加机器 IP。
3. 前往日志主题的采集配置页，输入日志路径确定数据源，并绑定机器组。详细操作示例可参阅 [单行全文采集](https://cloud.tencent.com/document/product/614/17421) 文档。
4. 前往日志主题的索引配置页，配置全文或键值索引，并开启索引。详细操作示例可参阅 [单行全文采集](https://cloud.tencent.com/document/product/614/17421) 文档。

至此，LogListener 将按照日志主题的采集配置监听符合规则的日志文件，用户可以通过日志检索查看采集上来的日志数据。






