## 一、下载SDK
你可以在[腾讯云官网](http://cloud.tencent.com/product/ilvb.html)下载互动直播ILVB的SDK。
> http://cloud.tencent.com/product/ilvb.html

## 二、目录讲解
从官网上下载的SDK主要包含以下文件夹：

| 文件夹 | 说明 |
|---------|---------|
| docs | 里面放了一些开发文档，后面会安排人力统一迁移到腾讯云的文档中心，方便开发者查阅。 |
| libs | SDK是以jar和so文件的形式提供给APP使用的，libs文件夹下包含了SDK所有的jar和so文件。 |
## 三、SDK文件简介
libs文件夹中包含了两大SDK的的jar和so文件：

| SDK名 | 说明 |
|---------|---------|
| AVSDK | 实现了音视频通信的核心能力。 |
| IMSDK | 实现了音视频通信中要用到的第三方账号体系接入，账号登录鉴权等能力，还集成了crash上报模块。 |

**特别注意：**这两大SDK的文件，在编译时存在一定的依赖，在运行时互有调用，因此APP开发者在更新替换SDK的时候，务必要保证下文清单中所有文件的完整性。如果仅局部地替换个别文件，很可能会引入异常。

你可以通过以下链接，了解更多IMSDK的信息：
> http://cloud.tencent.com/product/im.html

## 四、SDK文件清单
### 1、AVSDK文件清单
| 序号  | 名称 | 所在文件夹 | 说明 |
|---------|---------|---------|---------|
| 1 | qavsdk.jar | libs\jar | 音视频SDK。|
| 2 | libhwcodec.so | libs\armeabi | 编解码。 |
| 3 | libqav_graphics.so | libs\armeabi | 音视频图形界面。|
| 4 | libqavsdk.so | libs\armeabi |  音视频SDK。|
| 5 | libstlport_shared.so | libs\armeabi | 音视频基础库。 |
| 6 | libTcVpxDec.so | libs\armeabi | 视频组件。|
| 7 | libTcVpxEnc.so | libs\armeabi | 视频组件。 |
| 8 | libtraeimp-armeabi-v7a.so | libs\armeabi | 音频组件。|
| 9 | libxplatform.so | libs\armeabi | 音视频基础库。| 
**特别注意：**APP开发者在更新替换SDK的时候，务必要保证以上所有文件的完整性。如果仅局部地替换个别文件，很可能会引入异常。

### 2、IMSDK文件清单
| 序号  | 名称 | 所在文件夹 | 说明 |
|---------|---------|---------|---------|
| 1 | beacon_1.5.3_imsdk_release.jar | libs\jar | 音视频SDK。|
| 2 | bugly_1.2.8_imsdk_release.jar | libs\jar | 即时聊天crash上报。
| 3 | imsdk.jar | libs\jar | 即时聊天的SDK。|
| 4 | mobilepb.jar | libs\jar | protouf编解码相关。|
| 5 | qalsdk.jar | libs\jar | imsdk网络层。|
| 6 | tls_sdk.jar | libs\jar | 登录相关。|
| 7 | wup-1.0.0-SNAPSHOT.jar | libs\jar | imSdk相关依赖包。|
| 8 | lib_imcore_jni_gyp.so | libs\armeabi |  即时聊天。|
| 9 | libBugly.so | libs\armeabi | crash上报。|
| 10 | libqalcodecwrapper.so | libs\armeabi | qalsdk相关。|
| 11 | libqalmsfboot.so | libs\armeabi | qalsdk相关。|
| 12 | libwtcrypto.so | libs\armeabi | 登录依赖。|
**特别注意：**APP开发者在更新替换SDK的时候，务必要保证以上所有文件的完整性。如果仅局部地替换个别文件，很可能会引入异常。