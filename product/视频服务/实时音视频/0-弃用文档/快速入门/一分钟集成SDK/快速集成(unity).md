本文主要介绍如何快速地将腾讯云 TRTC SDK（Unity）集成到您的项目中，只要按照如下步骤进行配置，就可以完成 SDK 的集成工作。

## 环境要求
* Unity 建议版本： 2020.2.1f1c1。
* 目前支持 Android、iOS、Windows、Mac（Mac 还在内测中）平台。
* 需要包含 `Android Build Support`、`iOS Build Support`、 `Winodows Build Support` 和 `MacOs Build Support` 模块。
- 其中 iOS  端开发还需要：
  - Xcode 11.0及以上版本。
  - 请确保您的项目已设置有效的开发者签名。

## 集成 SDK
1. 下载 SDK 及配套的 [Demo 源码](https://tccweb-1258344699.cos.ap-nanjing.myqcloud.com/sdk/trtc/unity/TRTCUnitySDK.zip)。
2. 解压后，把项目中的 `TRTCUnitySDK/Assets/TRTCSDK/SDK` 文件夹拷贝到您项目中的 Assets 目录下。

## 常见问题
### Android 提示网络权限问题？
请将项目中 `/Assets/Plugins/AndroidManifest.xml` 文件放到同级目录下。

### Android 没有音视频的权限？
Android 端的麦克风、摄像头权限要手动申请，具体方法请参见以下代码：
```
#if PLATFORM_ANDROID
if (!Permission.HasUserAuthorizedPermission(Permission.Microphone))
 {
     Permission.RequestUserPermission(Permission.Microphone);
 }
 if (!Permission.HasUserAuthorizedPermission(Permission.Camera))
 {
     Permission.RequestUserPermission(Permission.Camera);
 }
 #endif
```  
