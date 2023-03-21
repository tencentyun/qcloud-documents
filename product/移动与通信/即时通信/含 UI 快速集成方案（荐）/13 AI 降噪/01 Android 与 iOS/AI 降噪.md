
## 功能描述
为了使语音消息录制得更加明亮、清晰，`TUIChat` 发送语音消息时，可录制带 AI 降噪和自动增益的语音消息，能有效过滤背景噪声，提升语音质量。
下面是使用两台华为 P10 在下雨天同时录制的语音消息对比：

<table style="text-align:center;vertical-align:middle;width: 800px">
  <tr>
    <th style="text-align:center;" >系统录制的语音消息<br></th>
    <th style="text-align:center;" >录制的带 AI 降噪和自动增益的语音消息<br></th>
  </tr>
  <tr>
    <td style="text-align:center;" >
      <audio id="audio" controls="" preload="none" >
			<source id="m4a" src="https://im.sdk.cloudcachetci.com/tools/resource/rain_system_record.m4a">
      </audio>
    </td>
    <td style="text-align:center;" >
      <audio id="audio" controls="" preload="none">
			<source id="m4a" src="https://im.sdk.cloudcachetci.com/tools/resource/rain_tuicallkit_record_with_agc_aidenoise.m4a">
      </audio>
    </td>
  </tr>
</table>

> ? 
> - 该功能需要集成 `TUIChat` 和 `TUICallKit`，并且需要购买 [音视频通话 SDK](https://cloud.tencent.com/document/product/1640/79968) 群组通话版及以上版本。
> - 该功能仅 7.0 及以上版本支持。
> - 当套餐过期后，录制语音消息会自动切换到系统 API 进行录音。

## 集成步骤
### 步骤1：开通音视频服务
1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片，进入应用的基础配置页面。
2. 在开通腾讯实时音视频服务功能区，单击**免费体验**即可开通 `TUICallKit` 的 7 天免费试用服务。
3. 在弹出的开通实时音视频 TRTC 服务对话框中，单击确认，系统将为您在 [实时音视频控制台](https://console.cloud.tencent.com/trtc) 创建一个与当前 IM 应用相同 SDKAppID 的实时音视频应用，二者帐号与鉴权可复用。

### 步骤2：配置工程文件
参考文档 集成基础功能（[Android](https://cloud.tencent.com/document/product/269/37059) / [iOS](https://cloud.tencent.com/document/product/269/37060)），添加对 `TUIChat` 和 `TUICallKit` 的依赖。
<dx-tabs>
::: Android
```java
api project(':tuichat')
api project(':tuicallkit')
```
:::
::: iOS
```objectivec
// 1. 在 podfile 文件中添加以下内容。
pod 'TUIChat'          
pod 'TUICallKit'                  
// 2. 执行以下命令，下载第三方库至当前工程。
pod install

// 如果无法安装 TUIKit 最新版本，执行以下命令更新本地的 CocoaPods 仓库列表。
pod repo update
```
:::
</dx-tabs>

### 步骤3：使用录音接口
示例代码如下：
<dx-tabs>
::: Android
```java
// 开始录制
AudioRecorder.getInstance().startRecord(new AudioRecorder.Callback() {
	@Override
	public void onCompletion(Boolean success) {
		// 录制结束
	}

	@Override
	public void onVoiceDb(double db) {
		// 暂不支持
	}
});

// 结束录制
AudioRecorder.getInstance().stopRecord();
```
:::
::: iOS
```objectivec
TUIAudioRecorder *recorder = [[TUIAudioRecorder alloc] init];
// 开始录制
[recorder record];
// 结束录制
[recorder stop];
// 取消录制，会清理录制文件
[recorder cancel];

// TUIAudioRecorderDelegate
// isGranted 表示用户是否授权；isFirstTime 表示是否是首次安装授权（首次安装授权处理流程可能有所不同，需要区分）
- (void)audioRecorder:(TUIAudioRecorder *)recorder didCheckPermission:(BOOL)isGranted isFirstTime:(BOOL)isFirstTime {
	// UI 弹框提示等
}
// 录制的音量发生变化
- (void)audioRecorder:(TUIAudioRecorder *)recorder didPowerChanged:(float)power {
	// 更新 UI
}
// 录制的时间发生变化
- (void)audioRecorder:(TUIAudioRecorder *)recorder didRecordTimeChanged:(NSTimeInterval)time {
	// 更新 UI
}
```
:::
</dx-tabs>

## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:40%;"/>
