`TUIKit`组件在`5.0.10`以上版本开始支持群直播功能，并且支持 iOS 和 Android 平台的互通 ，群直播的实现需要额外[集成 TUIKitLive 组件](#step2) ，群直播界面请参考下图所示：
<table>
<tr><td  style="border-color:white">
<video width="320" height="640" src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/video/startGroupLive.mp4" controls  muted></video>
 </td><td style="border-color:white">
 <video width="320" height="640" src="https://liteav-test-1252463788.cos.ap-guangzhou.myqcloud.com/video/enterGroupLive.mp4" controls muted>
 </video>
  </td></tr>
 </table>
 
如果您还未开通音视频服务，请按如下步骤开通：

[](id:step1)

## 步骤1：开通音视频服务
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 单击【开通腾讯实时音视频服务】区域的【立即开通】。
3. 在弹出的开通实时音视频 TRTC 服务对话框中，单击【确认】。
4. 您还可以 [单击购买](https://cloud.tencent.com/act/pro/IMTRTC?from=13947) IM 专业版/旗舰版套餐包和 TRTC 时长包。
>? 系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 创建一个与当前 IM 应用相同 SDKAppID 的实时音视频应用，二者帐号与鉴权可复用。

[](id:step2)
## 步骤2：集成 TUIKitLive 
建议使用源码集成``TUIKit``和``TUIKit-Live``，以便于您修改源码满足自身的业务需求。在`build.gradle`文件中加入：

```groovy
implementation project(':tuikit')
implementation project(':tuikit-live')
```

[](id:step3)
## 步骤3：初始化 TUIKit 
初始化`TUIKit`需要传入 [步骤1](#step1) 生成的`SDKAppID`（如果您的项目已经集成了`TUIKit`，请跳过此步骤）。
```java
TUIKit.init(Context, SDKAppID, new ConfigHelper().getConfigs());
```

[](id:step4)
## 步骤4：登录 TUIKit
如果未登录 IM，需要先通过`TUIKit`提供的 `login` 接口登录，其中 UserSig 生成的具体操作请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)（如果已经集成了`TUIKit`，请跳过此步骤）。

```java
TUIKit.login("userId", "userSig", new IUIKitCallBack() {
	@Override
	public void onError(String module, final int code, final String desc) {
		Log.i(TAG, "onError: 登录失败");
	}

	@Override
	public void onSuccess(Object data) {
		Log.i(TAG, "onSuccess: 登录成功");
	}
});
```

[](id:step5)
## 步骤5：打开/关闭群直播
`TUIKit-Live`中默认打开了群直播，如果您不需要集成群直播，可在通过`TUIKit-Live`模块中的`TUIKitLiveChatController.java`文件配置关闭群直播入口即可，代码如下：

```java
// enableGroupLiveEntry	true：开启；false：关闭	默认：true
private boolean enableGroupLiveEntry = false;
```
