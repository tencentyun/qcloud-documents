## 功能简介
EdgeOne 开启 gRPC 协议，可以同时支持 HTTP/HTTPS/gRPC 协议，根据用户请求协议自动适配，即请求 HTTP，则使用 HTTP 协议；请求 gRPC，则使用 gRPC 协议。

## 什么是 gRPC ？
gRPC (gRPC Remote Procedure Calls) 是 Google 发起的一个开源远程过程调用（Remote procedure call）系统。 该系统基于 HTTP/2 标准设计，具备诸如双向流、流控、头部压缩、单 TCP 连接上的多复用请求等特性。

## 前提条件
gRPC 是基于全链路 HTTP/2实现的，即请求和回源均需要开启 HTTP/2，详情请参见  [HTTP/2](https://cloud.tencent.com/document/product/1552/70780)。

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，在左侧菜单栏中，单击**站点加速** > **网络优化**。
2. 在网络优化页面，选择所需站点，单击 gRPC 模块的“开关”，开启或关闭 gRPC 功能。
![](https://qcloudimg.tencent-cloud.cn/raw/ff5a1b12879baee16815a07c5b2f7fc5.png)
**参数说明：**
 - 关闭状态（默认）：不支持 gRPC 协议。
 - 开启状态：支持 gRPC 协议。目前只支持 Simple RPC、Server-side streaming RPC 两种模式。
