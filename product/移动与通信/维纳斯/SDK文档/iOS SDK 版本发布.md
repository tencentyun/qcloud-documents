#### SDK 历史版本及更新日志

### 版本号：WNS SDK V 3.1.1
[下载](https://main.qcloudimg.com/raw/a56a64276112378ef26816f5dac82185/cloudwns_sdk_ios_v3.1.1.zip)
发布时间：2018.12.03
版本说明：
1.修复某些运营商分配给终端 同时有 IPV4 与 IPV6 地址时，无法网络连接的 BUG。

 -----
### 版本号：WNS SDK V 3.1.0
[下载](https://mc.qcloudimg.com/static/archive/09c89cba2d1417407e7db86c9148fe5f/cloudwns_sdk_ios_v3.1.0.zip)
发布时间：2016.12.19
版本说明：
1.提升 sdk 稳定性。

 -----
### 版本号：WNS SDK V 3.0.9
[下载](https://mc.qcloudimg.com/static/archive/4a3e8405f7947284775a7f98ae00f935/cloudwns_sdk_ios_v3.0.9.zip)
发布时间：2016.12.7
版本说明：
1.兼容 iOS10下ATS 特性
2.支持发送 https 请求
升级指南：
1.WnsSDK.framework 变更为 WnsSDK4Cloud.framework
2.app 链接时需要添加系统库：libresolv.tbd、libc++.dylib
 
-----
### 版本号：WNS SDK V 2.5.21
[下载](https://mc.qcloudimg.com/static/archive/150241dbf21612d2f61ae9d5f849546c/cloudwns_sdk_ios_v2.5.21.zip)
发布时间：2016.9.14
版本说明：
1.暂时移除 iOS10下ATS 特性
2.移除不必要的测速逻辑

-----
### 版本号：WNS SDK V 2.5.20
[下载](https://mc.qcloudimg.com/static/archive/78ff7ea7de94d0097eef116fa026b067/cloudwns_sdk_ios_v2.5.20.zip)
发布时间：2016.9.6
版本说明：
1.兼容 iOS10下ATS 特性
2.增加获取 log 文件路径接口
3.替换 localdns 接口
4.修复 WnsUrlProtocol 多线程冲突导致 crash
5.替换 demo 内测试 http 请求地址

-----

### 版本号：WNS SDK V 2.5.18
[下载](https://mc.qcloudimg.com/static/archive/bf6635d83a1bce9c0fcc347a4ca3a603/cloudwns_sdk_ios_v2.5.18.zip)
发布时间：2016.7.4
版本说明：
1.修正 HTTP 接口的 NSURLResponse 的 URL 为 nil 的问题

-----




### 版本号：WNS SDK V 2.5.17
[下载](https://mc.qcloudimg.com/static/archive/64695aa315419ac390b1a01dadbb4270/cloudwns_sdk_ios_v2.5.17.zip)
发布时间：2016.6.30
版本说明：
1.支持应用在多个环境下配置不同 push 证书
2.简易接入 http 协议的应用
3.增加 PUSH 接收稳定性
4.增加 SDK 稳定性
5.更换腾讯内部应用接入时用到的备份 IP

-----




### 版本号：WNS SDK V 2.5.16
[下载](https://mc.qcloudimg.com/static/archive/e0690df246dfac51a2bf6af456ed4b47/cloudwns_sdk_ios_v2.5.16.zip)
发布时间：2016.4.5
版本说明：
1.修正应用在后台切换到前台时小几率收不到 Push 的问题

-----



### 版本号：WNS SDK V 2.5.15
[下载](https://mc.qcloudimg.com/static/archive/822546ef10e1788166ca7de11d00a1cf/cloudwns_sdk_ios_v2.5.15.zip)
发布时间：2016.3.24
版本说明：
1.修正内部 APP 连到错误的后台环境的问题

-----



### 版本号：WNS SDK V 2.5.14
[下载](https://mc.qcloudimg.com/static/archive/9f4211148bb9ac3510b7f17c780b6074/cloudwns_sdk_ios_v2.5.14.zip)
发布时间：2016.3.22
版本说明：
1.兼容 IPV6 NAT64 环境
2.支持后台新增的 Push flag 特性

-----
### 版本号：WNS SDK V 2.5.13
[下载](https://mc.qcloudimg.com/static/archive/6aa43a8b3abe3c43b5f12f5760c6786f/cloudwns_sdk_ios_v2.5.13.zip)
发布时间：2016.1.15
版本说明：
1.修正 Bug, 增强 SDK 稳定性

-----
### 版本号：WNS SDK V 2.5.12
[下载](https://mc.qcloudimg.com/static/archive/c8b9c48823ef17b9a71c723345c57081/cloudwns_sdk_ios_v2.5.12.zip)
发布时间：2015.12.17
版本说明：
1.支持 Xcode7 的 Bitcode 特性
2.增加了一些逻辑的容错处理

-----


### 版本号：WNS SDK V 2.5.11
[下载](https://mc.qcloudimg.com/static/archive/85ead3d079a2382c40358dd8d07706b8/cloudwns_sdk_ios_v2.5.11.zip)
发布时间：2015.8.19
版本说明：
1.提供关键调试日志拉取
2.提供新的方式发送 HTTP 请求
3.增加了后端调度逻辑的处理
