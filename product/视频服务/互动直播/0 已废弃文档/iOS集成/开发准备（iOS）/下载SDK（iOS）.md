## 一、下载SDK
你可以在[腾讯云官网](http://cloud.tencent.com/product/ilvb.html)下载互动直播ILVB的SDK。
> http://cloud.tencent.com/product/ilvb.html

## 二、目录讲解
从官网上下载的SDK主要包含以下文件夹：

| 文件夹 | 说明 |
|---------|---------|
| docs | 里面放了一些开发文档，后面会安排人力统一迁移到腾讯云的文档中心，方便开发者查阅。 |
| libs | SDK是以Framework的形式提供给APP使用的，libs文件夹下包含了所有的Framework。 |
## 三、SDK文件简介
libs文件夹中包含了两大SDK的Framework：

| 名称 | 说明 |
|---------|---------|
| AVSDK | 实现了音视频通信的核心能力。 |
| IMSDK | 实现了音视频通信中要用到的第三方账号体系接入，账号登录鉴权等能力，还集成了crash上报模块。 |

**特别注意：**这两大SDK的Framework，在编译时存在一定的依赖，在运行时互有调用，因此APP开发者在更新替换SDK的时候，务必要保证下文清单中所有Framework的完整性。如果仅局部地替换个别Framework，很可能会引入异常。

你可以通过以下链接，了解更多IMSDK的信息：
> http://cloud.tencent.com/product/im.html

## 四、SDK文件清单
### 1、AVSDK文件清单
| 序号 | 名称 | 说明 |
|---------|---------|---------|
| 1 | AVFoundationEx.framework | AVFoundation扩展包。|
| 2 | QAVSDK .framework | 音视频核心功能包。|
**特别注意：**APP开发者在更新替换SDK的时候，务必要保证以上所有Framework的完整性。如果仅局部地替换个别Framework，很可能会引入异常。
### 2、IMSDK文件清单
| 序号 | 名称 | 说明 |
|---------|---------|---------|
| 1 | Analytics.framework | 灯塔统计SDK。|
| 2 | IMCore.framework | IMSDK内部核心包。|
| 3 | ImSDK.framework | 即时通信SDK（封装IMCore）。|
| 4 | IMSDKBugly.framework | Bugly上报。|
| 5 | QALSDK.framework |  联网层sdk，实现app和后台之间的安全连接通道。|
| 6  | TLSSDK.framework | 腾讯云TLS登录包。|
**特别注意：**APP开发者在更新替换SDK的时候，务必要保证以上所有Framework的完整性。如果仅局部地替换个别Framework，很可能会引入异常。