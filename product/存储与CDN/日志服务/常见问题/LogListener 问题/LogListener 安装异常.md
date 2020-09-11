如何安装使用日志服务 LogListener，详情请参见 [ LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414) 文档，并了解 [ LogListener 机制](https://cloud.tencent.com/document/product/614/17415)。

## 可能原因

以下原因可能会导致无法正确安装 LogListener：

1. 内核版本仅支持64位。
2. 安装方式出错。
3. 最新特性功能依赖较高版本 LogListener。


## 处理步骤

1. 确认内核版本。
   LogListener 安装目录下的 bin 目录中的可执行文件只支持 Linux 64位内核，执行命令 **uname -a**， 确认内核版本是否为 x86_64。
2. 确认安装执行命令是否正确。
   具体请参见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414) 文档进行操作。
3. 确认 Loglistener 版本。
   日志服务最新特性可能依赖新版 LogListener，若确认是使用新特性异常，请下载 LogListener 最新版本。LogListener 下载及详细安装步骤请参见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414)。
4. 验证 LogListener 成功安装。
   参考如何使用 [LogListener 快速诊断工具](https://cloud.tencent.com/document/product/614/17414#loglistener-.E5.B8.B8.E7.94.A8.E6.93.8D.E4.BD.9C) 检查 LogListener 进程、心跳和拉配置是否正常。 
