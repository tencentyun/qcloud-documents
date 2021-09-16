## 描述

.NET SDK 从 5.4.23 版本开始，提供 .NET Framework 4.0 及以下版本的兼容性。具体表现为，增加 COSXML-Compatible.dll 库的方式，能够实现在 .NET Framework 4.0 及以下版本应用中运行。

>! 
> - 兼容的环境可能不支持 NuGet 方式集成，具体集成方式见“添加引用”。
> - 所有高级接口（高级上传、断点续传下载等）在 COSXML-Compatible.dll 均不可用。
> 

## 添加引用

目前仅提供手动添加 .dll 文件的集成方法，集成方式如下：
1. [Releases](https://github.com/tencentyun/qcloud-sdk-dotnet/releases) 中下载 COSXML-Compatible.dll 文件。
2. 在 Visual Studio 项目中选择**项目** > **添加引用** > **浏览** > **COSXML-Compatible.dll** 的方式添加 .NET SDK。

## 使用方式

使用方式与通用版 .NET SDK 基本相同，需要关注如下两点：

1. .NET Framework 4.0 及以下环境通过 HTTPS 访问 COS 可能存在问题，如因设置开启 HTTPS 导致请求失败，可关闭 HTTPS 后重试。
2. .NET 兼容版中不包含高级接口的支持，请使用其他接口访问 COS，具体不兼容接口如下表所示：

| 命名空间           | 类名                          | 说明                            |
| ----------------- | ---------------------------- | ------------------------------- |
| COSXML.Transfer   | COSXMLCopyTask               | 高级 Copy 接口               |
| COSXML.Transfer   | COSXMLDownloadTask           | 高级下载接口                |
| COSXML.Transfer   | COSXMLTask                   | 高级接口抽象类             |
| COSXML.Transfer   | COSXMLUploadTask             | 高级上传接口               |
| COSXML.Transfer   | TransferManager              | 传输任务控制类             |

## 未知问题

目前兼容包处于预发布阶段，如存在其他未列出的使用问题，请向 GitHub 项目提 [issue](https://github.com/tencentyun/qcloud-sdk-dotnet/issues)。
