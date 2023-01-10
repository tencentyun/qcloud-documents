本文主要介绍如何快速运行腾讯云慧眼人脸核身 demo。
## 环境要求
- 最低兼容手机系统版本 iOS 9.0。
- xcode11.0及以上版本（建议使用最新的开发工具开发）。

## 前提条件
- 您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)，已开通人脸核身服务。
- 已申请获取 License 文件。
- 在 [GetFaceIdToken](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=DetectAuth&SignVersion=) 接口获取 token。
- 并将 SDK 的演示 demo 文件下载到本地。

## 操作步骤
1. 打开 Demo 工程。
使用 Xcode 打开 Demo 项目。
![](https://qcloudimg.tencent-cloud.cn/raw/b360c3c3015ef19c0e9c1976a0fe5496.png)

2. 更新替换 License。
替换 Demo 中的 License 文件。

3. 修改 Demo 中的 BundleID。
修改为申请 License 时提供的那个 BundleID。

4. 设置 FaceIdToken。
```objective-c
[[HuiYanSDKKit sharedInstance] setFaceIdTokenCreateFunction:^NSString *{
      return @"填入faceidtoken";
}];
```
5. 编译运行。
>! 真机才能体验慧眼人脸核身 SDK 服务。
