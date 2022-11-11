此篇文档为您介绍 GME SDK 合规接入的详细操作。在阅读此文档前，请先充分阅读和了解《[SDK 接入使用说明](https://cloud.tencent.com/document/product/607/81874)》。


## 涉及到个人信息的接口

目前 GME SDK 涉及到个人信息的接口如下：

### 初始化接口
初始化接口用于初始化整个 GME SDK，启动后会收集个人信息。


<dx-alert infotype="notice" title="注意">
确保在用户阅读 App 隐私政策并取得用户授权之后，按APP功能需要在合适时机调用正式初始化函数 Init 初始化 SDK。反之，如果用户不同意《隐私政策》授权，则不能调用正式初始化函数。
</dx-alert>


#### 接口原型
**Android**
```
public abstract int Init(String sdkAppId, String openId);
```

**iOS**
```
-(int)InitEngine:(NSString*)sdkAppID openID:(NSString*)openID;
```

#### 示例代码
**Android**
```
String sdkAppID = "14000xxxxx";
String openID = "100";
int ret = 0;
//在用户同意APP隐私政策之后，按APP功能需要在合适时机再正式初始化SDK
//ret = 0，表示用户同意APP隐私合规政策
//ret = 1，表示用户不同意APP隐私合规政策
//如果用户不授权隐私策略，则 ret 修改为非 0 
if(ret != 0){
    Log.e(TAG,"用户不同意APP隐私合规政策");
}else{
		ITMGContext.GetInstance(this).Init(sdkAppId, openId);
}
```

**iOS**

```
_openId = _userIdText.text;
_appId = _appIdText.text;
int result = 0;
//在用户同意APP隐私政策之后，按APP功能需要在合适时机再正式初始化SDK
//result = 0，表示用户同意APP隐私合规政策
//result = 1，表示用户不同意APP隐私合规政策
//如果用户不授权隐私策略，则 ret 修改为非 0 
if (result == 0) {
	[[ITMGContext GetInstance] InitEngine:SDKAPPID openID:_openId];}
	else{
	log = [NSString stringWithFormat:@"用户不同意APP隐私合规政策"];
}
```


## 可延迟申请权限

请您注意，启动麦克风设备接口会需要用到麦克风权限，建议在需要启动麦克风的时候才对权限进行申请，在用户授权的情况下获取麦克风权限。需要麦克风权限的接口如下：

#### 接口原型
**Android**
```
public abstract int EnableMic(boolean isEnabled);
public abstract int EnableAudioCaptureDevice(boolean isEnabled);
public abstract int StartRecording(String filePath);
public abstract int StartRecordingWithStreamingRecognition (String filePath);
public abstract int StartRecordingWithStreamingRecognition (String filePath,String language,String translatelanguage);
```

**iOS**
```
-(QAVResult)EnableMic:(BOOL)enable;
-(QAVResult)EnableAudioCaptureDevice:(BOOL)enabled;
-(int)StartRecording:(NSString*)filePath;
-(int)StartRecordingWithStreamingRecognition:(NSString *)filePath;
-(int)StartRecordingWithStreamingRecognition:(NSString *)filePath language:(NSString*)speechLanguage translatelanguage:(NSString*)translateLanguage;
```

#### 检查权限
关于麦克风权限的检查，可以通过 GME [TestMic](https://cloud.tencent.com/document/product/607/48324#.E6.A3.80.E6.9F.A5.E9.BA.A6.E5.85.8B.E9.A3.8E.E8.AE.BE.E5.A4.87.E7.8A.B6.E6.80.81) 接口进行实现。


## 可选权限配置
请您注意，SDK 不强制获取可选权限，即使没有获取可选权限，SDK 基本功能也能正常运行。您可以配置可选权限，以便使用 SDK 提供的其他可选功能。建议调用请求前在合适的时机调用 SDK 提供的方法，在用户授权的情况下获取声明中的权限。

### Android 配置可选权限
在 Android 平台中，读写权限不是必须添加的，请根据以下规则进行判断是否添加：

 - 如果使用的是默认的日志路径（/sdcard/Android/data/xxx.xxx.xxx/files），即表示未对 SetLogPath 进行调用，则不需要 WRITE_EXTERNAL_STORAGE 权限。
 - 如果调用 SetLogPath 接口将日志路径放在外部存储设备，以及使用语音消息功能在录制时的存储路径是在外部存储设备，则需要向用户申请 WRITE_EXTERNAL_STORAGE 权限，并得到用户明确批准。

### iOS 配置可选权限
在 iOS 平台中，Required background modes 权限用于允许后台运行，可根据业务决定是否配置。


## 用户权利保障机制

终端用户撤销同意处理其个人信息的授权时，您可通过调用 Uninit 接口停止使用 SDK 功能并停止采集与关闭功能相应的用户数据。

#### 接口原型
**Android**
```
public abstract int Uninit;
```

**iOS**
```
-(int)Uninit;
```
