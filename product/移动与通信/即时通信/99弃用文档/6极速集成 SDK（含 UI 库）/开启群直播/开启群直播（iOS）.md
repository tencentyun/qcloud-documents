TUIKit 组件在 5.0.10 以上版本开始支持群直播功能，并且支持 iOS 和 Android 平台的互通 ，群直播的实现需要额外集成 [TUIKitLive 组件](#step2) ，群直播界面请参考下图所示：

<table>
<tr><td  style="border-color:white">
<video width="320" height="640" src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/video/startGroupLive.mp4" controls  muted></video>
 </td><td style="border-color:white">
 <video width="320" height="640" src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/video/enterGroupLive.mp4" controls muted>
 </video>
  </td></tr>
 </table>
 
如果您还未开通音视频服务，请按如下步骤开通：

[](id:Step1)

## 步骤1：开通音视频服务

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 单击【开通腾讯实时音视频服务】区域的【立即开通】。
3. 在弹出的开通实时音视频 TRTC 服务对话框中，单击【确认】。
4. 您还可以 [单击购买](https://cloud.tencent.com/act/pro/IMTRTC?from=13947) IM 专业版/旗舰版套餐包和 TRTC 时长包。
>?系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 创建一个与当前 IM 应用相同 SDKAppID 的实时音视频应用，二者帐号与鉴权可复用。

[](id:step2)
## 步骤2：集成 TUIKitLive 组件

1. 在 podfile 文件中添加以下内容。
 ```objectivec
pod 'TXIMSDK_TUIKit_live_iOS'                 // 默认集成了 TXLiteAVSDK_TRTC 音视频库
// pod 'TXIMSDK_TUIKit_live_iOS/Professional' // 默认集成了 TXLiteAVSDK_Professional 音视频库
```
腾讯云的 [音视频库](https://cloud.tencent.com/document/product/647/32689) 不能同时集成，会有符号冲突，如果您使用了非 [TRTC](https://cloud.tencent.com/document/product/647/32689#TRTC) 版本的音视频库，建议 pod 集成 `TXIMSDK_TUIKit_live_iOS/Professional` 版本，该版本依赖的 [LiteAV_Professional](https://cloud.tencent.com/document/product/647/32689#.E4.B8.93.E4.B8.9A.E7.89.88.EF.BC.88professional.EF.BC.89) 音视频库包含了音视频的所有基础能力。

2. 执行以下命令，下载第三方库至当前工程。
```
pod install
```
 如果无法安装 TUIKit 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。
```
 pod repo update
```

[](id:step3)
## 步骤3：初始化 TUIKit 
初始化 TUIKit 需要传入 [步骤1](#Step1) 生成的 SDKAppID（如果您的项目已经集成了 TUIKit，请跳过此步骤）。
 ```objectivec
[[TUIKit sharedInstance] setupWithAppId:SDKAppID];
```

[](id:step4)
## 步骤4：登录 TUIKit
如果未登录 IM，需要先通过 TUIKit 提供的 `login` 接口登录，其中 UserSig 生成的具体操作请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)（如果已经集成了 TUIKit，请跳过此步骤）。

 ```objectivec
[[TUIKit sharedInstance] login:@"userID" userSig:@"userSig" succ:^{
     NSLog(@"-----> 登录成功");
} fail:^(int code, NSString *msg) {
     NSLog(@"-----> 登录失败");
}];
```

[](id:step5)
## 步骤5：打开/关闭群直播
可以通过 `TUIBaseChatViewController.h` 中的 `isEnableLive` 参数设置关闭群直播入口，示例代码如下：

 ```objectivec
TUIC2CChatViewController *vc = [[TUIC2CChatViewController alloc] init];  // c2c 会话
vc.isEnableLive = NO; // isEnableLive    YES：开启；NO：关闭    默认：YES
```
