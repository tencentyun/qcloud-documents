为方便开发者调试和接入腾讯云游戏多媒体引擎产品 API，这里向您介绍 Native 工程快速接入文档。

GME 快速入门文档只提供最主要的接入接口，协助用户参考接入 Demo 进行接入。


## 使用 GME 重要事项

GME 分为两个部分，提供实时语音服务、语音消息及转文本服务，使用这两个服务都依赖 Init 和 Poll 等核心接口。

<dx-alert infotype="notice" title="关于 Init 接口">
例如使用了实时语音服务，同时也需要使用语音消息服务，**只需要调用一次 Init 初始化接口**。
</dx-alert>

### 接口调用流程图

![image](https://main.qcloudimg.com/raw/ba4f19e0665165c93a2fea33552f088b.png)

### 接入步骤

#### 核心接口


<dx-tag-link link="#Init" tag="接口：Init">初始化 GME</dx-tag-link>
<dx-tag-link link="#Poll" tag="接口：Poll">周期性调用 Poll 触发回调</dx-tag-link>

#### 实时语音

<dx-steps>
-<dx-tag-link link="#EnterRoom" tag="接口：EnterRoom">加入实时语音房间</dx-tag-link>
-<dx-tag-link link="#EnableMic" tag="接口：EnableMic">打开或关闭麦克风</dx-tag-link>
-<dx-tag-link link="#EnableSpeaker" tag="接口：EnableSpeaker">打开或关闭扬声器</dx-tag-link>
-<dx-tag-link link="#ExitRoom" tag="接口：ExitRoom">退出语音房间</dx-tag-link>
</dx-steps>

#### 语音消息

<dx-steps>
-<dx-tag-link link="#ApplyPtt" tag="接口：ApplyPTTAuthbuffer">鉴权初始化</dx-tag-link>
-<dx-tag-link link="#StartRWSR" tag="接口：StartRecordingWithStreamingRecognition">启动流式语音识别</dx-tag-link>
-<dx-tag-link link="#Stop" tag="接口：StopRecording">停止录制</dx-tag-link>
</dx-steps>

<dx-tag-link link="#Init" tag="接口：UnInit">反初始化 GME</dx-tag-link>

## 核心接口接入

### 1. 下载 Demo 

进入下载指引页面，下载对应的客户端 <dx-tag-link link="https://cloud.tencent.com/document/product/607/18521" tag="DownLoad"> Demo 工程代码</dx-tag-link>。


### 2. 引入头文件

<dx-codeblock>
::: Java Java
import com.tencent.TMG.ITMGContext;
import com.tencent.av.sig.AuthBuffer;
import com.tencent.bugly.crashreport.CrashReport;
:::
::: Object-C objetctive-c
#import "GMESDK/TMGEngine.h"
#import "GMESDK/QAVAuthBuffer.h"
:::
::: C++ C++
#include "auth_buffer.h"
#include "tmg_sdk.h"
#include "AdvanceHeaders/tmg_sdk_adv.h"
#include <vector>
:::
</dx-codeblock>


### 3. 获取单例

在使用语音功能时，需要首先获取 ITMGContext 对象。

####  函数原型 

<dx-codeblock>
::: Java Java
public static ITMGContext GetInstance(Context context)
:::
::: Object-C objetctive-c

+ (ITMGContext*) GetInstance;
  :::
  ::: C++ C++
  __UNUSED static ITMGContext* ITMGContextGetInstance(){
  return ITMGContextGetInstanceInner(TMG_SDK_VERSION);
  }
  :::
  </dx-codeblock>

####  示例代码  


<dx-codeblock>
::: Java Java
//MainActivity.java
import com.tencent.TMG.ITMGContext; 
ITMGContext tmgContext = ITMGContext.GetInstance(this);
:::
::: Object-C objetctive-c
//TMGSampleViewController.m
ITMGContext* _context = [ITMGContext GetInstance];
:::
::: C++ C++
ITMGContext* context = ITMGContextGetInstance();
:::
</dx-codeblock>

### 4. 设置回调

接口类采用 Delegate 方法用于向应用程序发送回调通知。将回调函数注册给 SDK，用于接收回调的信息，需要在进房之前设置。

#### 函数原型及示例代码

设置回调，用于接收回调的信息，需要在进房之前设置。

<dx-codeblock>
::: Java Java
//ITMGContext
public abstract int SetTMGDelegate(ITMGDelegate delegate);

//MainActivity.java
tmgContext.SetTMGDelegate(TMGCallbackDispatcher.getInstance());
:::
::: Object-C objetctive-c
ITMGDelegate < NSObject >

//TMGSampleViewController.m
ITMGContext* _context = [ITMGContext GetInstance];
_context.TMGDelegate = [DispatchCenter getInstance];
:::
::: C++ C++
//在初始化 SDK 时候
m_pTmgContext = ITMGContextGetInstance();
m_pTmgContext->SetTMGDelegate(this);
//在析构函数中
CTMGSDK_For_AudioDlg::~CTMGSDK_For_AudioDlg()
{
    ITMGContextGetInstance()->SetTMGDelegate(NULL);
}
:::
</dx-codeblock>

#### 回调示例  

在构造函数中重写此回调函数，对回调参数进行处理。


<dx-codeblock>
::: Java Java
//MainActivity.java
tmgContext.SetTMGDelegate(TMGCallbackDispatcher.getInstance());

//RealTimeVoiceActivity.java
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
        if (type == ITMG_MAIN_EVENT_TYPE_ENTER_ROOM)
		{
			//回调处理
		}
}

//需要参考 TMGCallbackDispatcher.java、TMGCallbackHelper.java以及 TMGDispatcherBase.java
:::
::: Object-C Object-C
//TMGRealTimeViewController.m
TMGRealTimeViewController ()< ITMGDelegate >


- (void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data {
  NSString *log = [NSString stringWithFormat:@"OnEvent:%d,data:%@", (int)eventType, data];
  [self showLog:log];
  NSLog(@"====%@====", log);
  switch (eventType) {
      // Step 6/11 : Perform the enter room event
      case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM: {
          int result = ((NSNumber *)[data objectForKey:@"result"]).intValue;
          NSString *error_info = [data objectForKey:@"error_info"];

          [self showLog:[NSString stringWithFormat:@"OnEnterRoomComplete:%d msg:(%@)", result, error_info]];
      
          if (result == 0) {
              [self updateStatusEnterRoom:YES];
          }
      }
      break;

  }
  }

//需要参考 DispatchCenter.h、DispatchCenter.m
:::
::: C++ C++
//头文件中声明
virtual void OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data);
//示例代码
void CTMGSDK_For_AudioDlg::OnEvent(ITMG_MAIN_EVENT_TYPE eventType, const char* data)
{
    switch(eventType)
    {
    case ITMG_MAIN_EVENT_TYPE_XXXX_XXXX:
        {
            //对回调进行处理
        }
        break;
    }
}
:::
</dx-codeblock>


| 参数 |               类型               | 含义                     |
| ---- | :------------------------------: | ------------------------ |
| type | ITMGContext.ITMG_MAIN_EVENT_TYPE | 回调的事件类型           |
| data |         Intent 消息类型          | 回调的相关信息，事件数据 |

### [5. 初始化 SDK](id:Init)

- 此接口用于初始化 GME 服务，建议应用侧在应用初始化时候调用。
- **参数 sdkAppId 获取请参见 [语音服务开通指引](https://cloud.tencent.com/document/product/607/10782)**。
- **OpenId 用于唯一标识一个用户，目前只支持 INT64，规则由 App 开发者自行制定，App 内不重复即可**。

#### 函数原型

<dx-codeblock>
::: Java Java
public abstract int Init(String sdkAppId, String openId);
:::
::: Object-C objetctive-c
-(int)InitEngine:(NSString*)sdkAppID openID:(NSString*)openID;
:::
::: C++ C++
ITMGContext virtual int Init(const char* sdkAppId, const char* openId)
:::
</dx-codeblock>


| 参数     |  类型  | 含义                                                         |
| -------- | :----: | ------------------------------------------------------------ |
| sdkAppId | String | 来自 [腾讯云控制台](https://console.cloud.tencent.com/gamegme) 的 GME 服务提供的 AppId。 |
| OpenId   | String | OpenId 只支持 Int64 类型（转为 string 传入）。               |

#### 示例代码 

<dx-codeblock>
::: Java Java
//MainActivity.java
int nRet = tmgContext.Init(appId, openId);
if (nRet == AV_OK )
{
    GMEAuthBufferHelper.getInstance().setGEMParams(appId, key, openId);
    // Step 4/11: Poll to trigger callback
    //https://cloud.tencent.com/document/product/607/15210#.E8.A7.A6.E5.8F.91.E4.BA.8B.E4.BB.B6.E5.9B.9E.E8.B0.83
    EnginePollHelper.createEnginePollHelper();
    showToast("Init success");
}else if (nRet == AV_ERR_HAS_IN_THE_STATE) // 已经初始化过了,可以认为本次操作是成功的
{
    showToast("Init success");
}else
{
    showToast("Init error errorCode:" + nRet);
}
:::
::: Object-C objetctive-c
//TMGSampleViewController.m
QAVResult result = [_context InitEngine:self.appIDTF.text openID:self.openIDTF.text];
if (result == QAV_OK) {
    self.isSDKInit = YES;
}
:::
::: C++ C++
#define SDKAPPID3RD "14000xxxxx"
cosnt char* openId="10001";
ITMGContext* context = ITMGContextGetInstance();
context->Init(SDKAPPID3RD, openId);
:::
</dx-codeblock>


### [6. 触发事件回调](id:Poll)

通过在 update 里面周期的调用 Poll 可以触发事件回调。GME 需要周期性的调用 Poll 接口触发事件回调。如果没有调用 Poll 的话，会导致整个 SDK 服务运行异常。

可参考 Demo 中的 EnginePollHelper.java 文件。

#### 示例代码

<dx-codeblock>
::: Java Java
//MainActivity.java
[EnginePollHelper createEnginePollHelper];

//EnginePollHelper.java
private Handler mhandler = new Handler();
    private Runnable mRunnable = new Runnable() {
        @Override
        public void run() {
            if (s_pollEnabled) {
                if (ITMGContext.GetInstance(null) != null)
                    ITMGContext.GetInstance(null).Poll();
            }
            mhandler.postDelayed(mRunnable, 33);
        }
    };
//周期性调用 Poll 请参考 EnginePollHelper.java 写法
:::
::: Object-C objetctive-c
//TMGSampleViewController.m
[EnginePollHelper createEnginePollHelper];
//需要参考 EnginePollHelper.m 以及 EnginePollHelper.h
:::
::: C++ C++
void TMGTestScene::update(float delta)
{
  ITMGContextGetInstance()->Poll();
}
:::
</dx-codeblock>

### 7. 鉴权信息

生成 AuthBuffer，用于相关功能的加密和鉴权。    
语音消息及转文本获取鉴权时，房间号参数必须填 null。

#### 函数原型

<dx-codeblock>
::: Java Java
AuthBuffer public native byte[] genAuthBuffer(int sdkAppId, String roomId, String openId, String key)
:::
::: Object-C objetctive-c
//TMGSampleViewController.m
[EnginePollHelper createEnginePollHelper];
//需要参考 EnginePollHelper.m 以及 EnginePollHelper.h
:::
::: C++ C++
void TMGTestScene::update(float delta)
{
  ITMGContextGetInstance()->Poll();
}
:::
</dx-codeblock>

| 参数   |  类型  | 含义                                                         |
| ------ | :----: | ------------------------------------------------------------ |
| appId  |  int   | 来自腾讯云控制台的 AppId 号码。                              |
| roomId | string | 房间号，最大支持127字符（离线语音房间号参数必须填 null）。   |
| openId | string | 用户标识。与 Init 时候的 openId 相同。                        |
| key    | string | 来自腾讯云 [控制台](https://console.cloud.tencent.com/gamegme) 的权限密钥。 |


####  示例代码  

<dx-codeblock>
::: Java Java
//GMEAuthBufferHelper.java
import com.tencent.av.sig.AuthBuffer;//头文件
public byte[] createAuthBuffer(String roomId)
    {
        byte[] authBuffer;
        // Generate AuthBuffer for encryption and authentication of relevant features. For release in the production environment,
        // please use the backend deployment key as detailed in https://intl.cloud.tencent.com/document/product/607/12218
        if (TextUtils.isEmpty(roomId))
        {
            authBuffer =  AuthBuffer.getInstance().genAuthBuffer(Integer.parseInt(mAppId), "0", mOpenId, mKey);
        }else
        {
            authBuffer =  AuthBuffer.getInstance().genAuthBuffer(Integer.parseInt(mAppId), roomId, mOpenId, mKey);
        }
        return authBuffer;
    }
:::
::: Object-C objetctive-c
//实时语音鉴权 
NSData* authBuffer = [QAVAuthBuffer GenAuthBuffer:SDKAPPID3RD.intValue roomID:self.roomIdTF.text openID:_openId key:_key];
//语音消息鉴权
NSData* authBuffer =  [QAVAuthBuffer GenAuthBuffer:(unsigned int)SDKAPPID3RD.integerValue roomID:nil openID:self.openId key:AUTHKEY];
:::
::: C++ C++
unsigned int bufferLen = 512;
unsigned char retAuthBuff[512] = {0};
QAVSDK_AuthBuffer_GenAuthBuffer(atoi(SDKAPPID3RD), roomId, "10001", AUTHKEY,retAuthBuff,bufferLen);
:::
</dx-codeblock>


## 实时语音接入

###  [1. 加入房间](id:EnterRoom)

用生成的鉴权信息进房，会收到消息为 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM 的回调。加入房间默认不打开麦克风及扬声器。返回值为 AV_OK 的时候代表成功。

房间音频类型请参考 [音质选择](https://cloud.tencent.com/document/product/607/18522)。

#### 函数原型

<dx-codeblock>
::: Java Java
public abstract int EnterRoom(String roomID, int roomType, byte[] authBuffer);
:::
::: Object-C objetctive-c
-(int)EnterRoom:(NSString*) roomId roomType:(int)roomType authBuffer:(NSData*)authBuffer;
:::
::: C++ C++
ITMGContext virtual int EnterRoom(const char*  roomID, ITMG_ROOM_TYPE roomType, const char* authBuff, int buffLen);
:::
</dx-codeblock>

| 参数       |  类型  | 含义                    |
| ---------- | :----: | ----------------------- |
| roomId     | String | 房间号，最大支持127字符 |
| roomType   |  int   | 房间音频类型            |
| authBuffer | byte[] | 鉴权码                  |

#### 示例代码  

<dx-codeblock>
::: Java Java
//RealTimeVoiceActivity.java
byte[] authBuffer =  GMEAuthBufferHelper.getInstance().createAuthBuffer(roomId);
ITMGContext.GetInstance(this).EnterRoom(roomId, roomType, authBuffer);
:::
::: Object-C objetctive-c
//TMGRealTimeViewController.m
[[ITMGContext GetInstance] EnterRoom:self.roomIdTF.text roomType:(int)self.roomTypeControl.selectedSegmentIndex + 1 authBuffer:authBuffer];
:::
::: C++ C++
ITMGContext* context = ITMGContextGetInstance();
context->EnterRoom(roomID, ITMG_ROOM_TYPE_STANDARD, (char*)retAuthBuff,bufferLen);
:::
</dx-codeblock>

#### 加入房间事件回调

加入房间完成后会发送信息 ITMG_MAIN_EVENT_TYPE_ENTER_ROOM，在 OnEvent 函数中进行判断回调后处理。如果回调为成功，即此时进房成功，开始进行**计费**；如果本日通话总时长 < 700 分钟则免费。

<dx-fold-block title="计费问题参考">
[购买指南。](https://cloud.tencent.com/document/product/607/17808)
[计费相关问题。](https://cloud.tencent.com/document/product/607/51459)
[使用实时语音后，如果客户端掉线了，是否还会继续计费？](https://cloud.tencent.com/document/product/607/51459#.E4.BD.BF.E7.94.A8.E5.AE.9E.E6.97.B6.E8.AF.AD.E9.9F.B3.E5.90.8E.EF.BC.8C.E5.A6.82.E6.9E.9C.E5.AE.A2.E6.88.B7.E7.AB.AF.E6.8E.89.E7.BA.BF.E4.BA.86.EF.BC.8C.E6.98.AF.E5.90.A6.E8.BF.98.E4.BC.9A.E7.BB.A7.E7.BB.AD.E8.AE.A1.E8.B4.B9.EF.BC.9F)
</dx-fold-block>

- **示例代码**  
回调处理相关参考代码，包括加入房间事件以及断网事件。
<dx-codeblock>
::: Java Java
//RealTimeVoiceActivity.java
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
    if (type == ITMG_MAIN_EVENT_TYPE_ENTER_ROOM)
    {
        // Step 6/11 : Perform the enter room event
        int nErrCode = TMGCallbackHelper.ParseIntentParams2(data).nErrCode;
        String strMsg = TMGCallbackHelper.ParseIntentParams2(data).strErrMsg;
        if (nErrCode == AV_OK)
        {
            appendLog2MonitorView("EnterRomm success");
        }else
        {
            appendLog2MonitorView(String.format(Locale.getDefault(), "EnterRomm errCode:%d errMsg:%s", nErrCode, strMsg));
        }
    }
}		
:::
::: Object-C objetctive-c
//TMGRealTimeViewController.m

- (void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data {
  NSString *log = [NSString stringWithFormat:@"OnEvent:%d,data:%@", (int)eventType, data];
  [self showLog:log];
  NSLog(@"====%@====", log);
  switch (eventType) {
      // Step 6/11 : Perform the enter room event
      case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM: {
          int result = ((NSNumber *)[data objectForKey:@"result"]).intValue;
          NSString *error_info = [data objectForKey:@"error_info"];

          [self showLog:[NSString stringWithFormat:@"OnEnterRoomComplete:%d msg:(%@)", result, error_info]];
      
          if (result == 0) {
              [self updateStatusEnterRoom:YES];
          }
      }
      break;

  }
  :::
  ::: C++ C++
  void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
  switch (eventType) {
      case ITMG_MAIN_EVENT_TYPE_ENTER_ROOM:
      {
          ListMicDevices();
          ListSpeakerDevices();
              std::string strText = "EnterRoom complete: ret=";
          strText += data;
          m_EditMonitor.SetWindowText(MByteToWChar(strText).c_str());
          }
  }
  }
  :::
  </dx-codeblock>
- **错误码**
<table>
<thead>
<tr>
<th>错误码值</th>
<th>原因及建议方案</th>
</tr>
</thead>
<tbody><tr>
<td>7006</td>
<td>鉴权失败，原因如下：<ul><li>AppID 不存在或者错误</li><li>authbuff 鉴权错误</li><li>鉴权过期 </li><li>openId 不符合规范</li></ul></td>
</tr>
<tr>
<td>7007</td>
<td>已经在其它房间</td>
</tr>
<tr>
<td>1001</td>
<td>已经在进房过程中，然后又重复了此操作。建议在进房回调返回之前不要再调用进房接口</td>
</tr>
<tr>
<td>1003</td>
<td>已经进房了在房间中，又调用一次进房接口</td>
</tr>
<tr>
<td>1101</td>
<td>确保已经初始化 SDK，确保 openId 是否符合规则，或者确保在同一线程调用接口，以及确保 Poll 接口正常调用</td>
</tr>
</tbody></table>





### [2. 开启或关闭麦克风](id:EnableMic)

此接口用来开启关闭麦克风。加入房间默认不打开麦克风及扬声器。

#### 示例代码  

<dx-codeblock>
::: Java Java
//RealTimeVoiceActivity.java
ITMGContext.GetInstance(this).GetAudioCtrl().EnableMic(true);
:::
::: Object-C objetctive-c
//TMGRealTimeViewController.m
[[[ITMGContext GetInstance] GetAudioCtrl] EnableMic:YES];
:::
::: C++ C++
ITMGContextGetInstance()->GetAudioCtrl()->EnableMic(true);
:::
</dx-codeblock>

### [3. 开启或关闭扬声器](id:EnableSpeaker)

此接口用于开启关闭扬声器。

#### 示例代码  

<dx-codeblock>
::: Java Java
//RealTimeVoiceActivity.java
ITMGContext.GetInstance(this).GetAudioCtrl().EnableSpeaker(true);
:::
::: Object-C objetctive-c
//TMGRealTimeViewController.m
[[[ITMGContext GetInstance] GetAudioCtrl] EnableSpeaker:YES];
:::
::: C++ C++
ITMGContextGetInstance()->GetAudioCtrl()->EnableSpeaker(true);
:::
</dx-codeblock>


### [4. 退出房间](id:ExitRoom)

通过调用此接口可以退出所在房间。这是一个异步接口，返回值为 AV_OK 的时候代表异步投递成功。

#### 示例代码  

<dx-codeblock>
::: Java Java
//RealTimeVoiceActivity.java
ITMGContext.GetInstance(this).ExitRoom();
:::
::: Object-C objetctive-c
//TMGRealTimeViewController.m
[[ITMGContext GetInstance] ExitRoom];
:::
::: C++ C++
ITMGContext* context = ITMGContextGetInstance();
context->ExitRoom();
:::
</dx-codeblock>


#### 退出房间回调

退出房间完成后会有回调，消息为 ITMG_MAIN_EVENT_TYPE_EXIT_ROOM。示例代码如下：
<dx-codeblock>
::: Java Java
//RealTimeVoiceActivity.java
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVENT_TYPE_EXIT_ROOM == type)
        {
            //收到退房成功事件
        }
}
:::
::: Object-C objetctive-c
//TMGRealTimeViewController.m
-(void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary *)data{
NSLog(@"OnEvent:%lu,data:%@",(unsigned long)eventType,data);
switch (eventType) {
    case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM：
    {
        //收到退房成功事件
    }
        break;
	}
}
:::
::: C++ C++
void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
switch (eventType) {
    case ITMG_MAIN_EVENT_TYPE_EXIT_ROOM:
    {
        //进行处理
        break;
        }
    }
}
:::
</dx-codeblock>



## 语音消息接入


### [1. 鉴权初始化](id:ApplyPtt)

在初始化 SDK 之后调用鉴权初始化，authBuffer 的获取参见上文实时语音鉴权信息接口 genAuthBuffer。

#### 函数原型  

<dx-codeblock>
::: Java Java
public abstract int ApplyPTTAuthbuffer(byte[] authBuffer);
:::
::: Object-C objetctive-c
-(QAVResult)ApplyPTTAuthbuffer:(NSData *)authBuffer;
:::
::: C++ C++
ITMGPTT virtual int ApplyPTTAuthbuffer(const char* authBuffer, int authBufferLen)
:::
</dx-codeblock>

| 参数       |  类型  | 含义 |
| ---------- | :----: | ---- |
| authBuffer | String | 鉴权 |

#### 示例代码  

<dx-codeblock>
::: Java Java
//VoiceMessageRecognitionActivity.java
byte[] authBuffer = GMEAuthBufferHelper.getInstance().createAuthBuffer("");
ITMGContext.GetInstance(this).GetPTT().ApplyPTTAuthbuffer(authBuffer);
:::
::: Object-C objetctive-c
//TMGPTTViewController.m
NSData* authBuffer =  [QAVAuthBuffer GenAuthBuffer:(unsigned int)SDKAPPID3RD.integerValue roomID:nil openID:self.openId key:AUTHKEY];
[[[ITMGContext GetInstance] GetPTT] ApplyPTTAuthbuffer:authBuffer];
:::
::: C++ C++
ITMGContextGetInstance()->GetPTT()->ApplyPTTAuthbuffer(authBuffer,authBufferLen);
:::
</dx-codeblock>

### [2. 启动流式语音识别](id:StartRWSR)

此接口用于启动流式语音识别，同时在回调中会有实时的语音转文字返回，可以指定语言进行识别，也可以将语音中识别到的信息翻译成指定的语言返回。**停止录音调用 StopRecording**，停止之后才有回调。

#### 函数原型  

<dx-codeblock>
::: Java Java
public abstract int StartRecordingWithStreamingRecognition (String filePath);
public abstract int StartRecordingWithStreamingRecognition (String filePath,String language,String translatelanguage);
public abstract int StopRecording();
:::
::: Object-C objetctive-c
-(int)StartRecordingWithStreamingRecognition:(NSString *)filePath;
-(int)StartRecordingWithStreamingRecognition:(NSString *)filePath language:(NSString*)speechLanguage translatelanguage:(NSString*)translatelanguage;
-(QAVResult)StopRecording;
:::
::: C++ C++
ITMGPTT virtual int StartRecordingWithStreamingRecognition(const char* filePath) 
ITMGPTT virtual int StartRecordingWithStreamingRecognition(const char* filePath,const char* translateLanguage,const char* translateLanguage)
ITMGPTT virtual int StopRecording()
:::
</dx-codeblock>


| 参数              |  类型  | 含义                                                         |
| ----------------- | :----: | ------------------------------------------------------------ |
| filePath          | String | 存放的语音路径                                               |
| speechLanguage    | String | 识别成指定文字的语言参数，参数请参考 [语音转文字的语言参数参考列表](https://cloud.tencent.com/document/product/607/30282) |
| translateLanguage | String | 翻译成指定文字的语言参数，参数请参考 [语音转文字的语言参数参考列表](https://cloud.tencent.com/document/product/607/30282)（此参数暂不可用,请填写与 speechLanguage 相同的参数） |

#### 示例代码  

<dx-codeblock>
::: Java Java
//VoiceMessageRecognitionActivity.java
ITMGContext.GetInstance(this).GetPTT().StartRecordingWithStreamingRecognition(recordfilePath,"cmn-Hans-CN");
:::
::: Object-C objetctive-c
//TMGPTTViewController.m
QAVResult ret = [[[ITMGContext GetInstance] GetPTT] StartRecordingWithStreamingRecognition:[self pttTestPath] language:@"cmn-Hans-CN"];
if (ret == 0) {
    self.currentStatus = @"开始流式录音";
} else {
    self.currentStatus = @"开始流式录音失败";
}
:::
::: C++ C++
ITMGContextGetInstance()->GetPTT()->StartRecordingWithStreamingRecognition(filePath,"cmn-Hans-CN","cmn-Hans-CN");
:::
</dx-codeblock>

#### 流式语音识别回调

启动流式语音识别后，需要在回调函数 OnEvent 中监听回调消息，事件消息分为 `ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE` ，在停止录制并完成识别后才返回文字，相当于一段话说完才会返回识别的文字。

根据需求在 OnEvent 函数中对相应事件消息进行判断。传递的参数包含以下4个信息。

| 消息名称  |                    含义                     |
| --------- | :-----------------------------------------: |
| result    |    用于判断流式语音识别是否成功的返回码     |
| text      |            语音转文字识别的文本             |
| file_path |             录音存放的本地地址              |
| file_id   | 录音在后台的 url 地址，录音在服务器存放90天 |

- **示例代码**  
<dx-codeblock>
::: Java Java
//VoiceMessageRecognitionActivity.java
import static com.tencent.TMG.ITMGContext.ITMG_MAIN_EVENT_TYPE.ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE;
public void OnEvent(ITMGContext.ITMG_MAIN_EVENT_TYPE type, Intent data) {
	if (type == ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE)
        {
            // Step 1.3/3 handle ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE event
            mIsRecording = false;
            if (nErrCode ==0)
            {
                String recordfilePath = data.getStringExtra("file_path");
                mRecFilePathView.setText(recordfilePath);

                String recordFileUrl = data.getStringExtra("file_id");
                mRecFileUrlView.setText(recordFileUrl);
            }
            else
            {
                appendLog2MonitorView("Record and recognition fail errCode:" + nErrCode);
            }
        }

}
:::
::: Object-C objetctive-c
//TMGPTTViewController.m

- (void)OnEvent:(ITMG_MAIN_EVENT_TYPE)eventType data:(NSDictionary*)data
  {
  NSNumber *number = [data objectForKey:@"result"];
  switch (eventType)
  {
  	case ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE:
  	{
            if (data != NULL &&[[data objectForKey:@"result"] intValue]== 0)
            {
                self.translateTF.text = [data objectForKey:@"text"] ;
                 self.currentStatus = @"流式转换完成";
            }
        }
  	break;
  }
  :::
  ::: C++ C++
  void TMGTestScene::OnEvent(ITMG_MAIN_EVENT_TYPE eventType,const char* data){
    switch (eventType) {
        case ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_COMPLETE:
        {
            HandleSTREAM2TEXTComplete(data,true);
            break;
        }
        ...
        case ITMG_MAIN_EVNET_TYPE_PTT_STREAMINGRECOGNITION_IS_RUNNING:
        {
            HandleSTREAM2TEXTComplete(data, false);
            break;
        }
    }
  }
  void CTMGSDK_For_AudioDlg::HandleSTREAM2TEXTComplete(const char* data, bool isComplete)
  {
    std::string strText = "STREAM2TEXT: ret=";
    strText += data;
    m_EditMonitor.SetWindowText(MByteToWChar(strText).c_str());
    Json::Reader reader;
    Json::Value root;
    bool parseRet = reader.parse(data, root);
    if (!parseRet) {
        ::SetWindowText(m_EditInfo.GetSafeHwnd(),MByteToWChar(std::string("parse result Json error")).c_str());
    }
        else
        {
            if (isComplete) {
                                ::SetWindowText(m_EditUpload.GetSafeHwnd(), MByteToWChar(root["file_id"].asString()).c_str());
                            }
                            else {
                                    std::string isruning = "STREAMINGRECOGNITION_IS_RUNNING";
                                    ::SetWindowText(m_EditUpload.GetSafeHwnd(), MByteToWChar(isruning).c_str());
                                 }
    }
  }
  :::
  </dx-codeblock>
- **错误码**
<table>
<thead>
<tr>
<th>错误码</th>
<th align="center">含义</th>
<th align="center">处理方式</th>
</tr>
</thead>
<tbody><tr>
<td>32775</td>
<td align="center">流式语音转文本失败，但是录音成功</td>
<td align="center">调用 UploadRecordedFile 接口上传录音，再调用 SpeechToText 接口进行语音转文字操作</td>
</tr>
<tr>
<td>32777</td>
<td align="center">流式语音转文本失败，但是录音成功，上传成功</td>
<td align="center">返回的信息中有上传成功的后台 url 地址，调用 SpeechToText 接口进行语音转文字操作</td>
</tr>
<tr>
<td>32786</td>
<td align="center">流式语音转文本失败</td>
<td align="center">在流式录制状态当中，请等待流式录制接口执行结果返回</td>
</tr>
</tbody></table>



### [3. 停止录音](id:Stop)

此接口用于停止录音。此接口为异步接口，停止录音后会有录音完成回调，成功之后录音文件才可用。

#### 函数原型  

<dx-codeblock>
::: Java Java
public abstract int StopRecording();
:::
::: Object-C objetctive-c
-(QAVResult)StopRecording;
:::
::: C++ C++
ITMGPTT virtual int StopRecording();
:::
</dx-codeblock>


#### 示例代码  

<dx-codeblock>
::: Java Java
//VoiceMessageRecognitionActivity.java
ITMGContext.GetInstance(this).GetPTT().StopRecording();
:::
::: Object-C objetctive-c
//TMGPTTViewController.m

- (void)stopRecClick {
  // Step 3/12 stop recording,  need handle ITMG_MAIN_EVNET_TYPE_PTT_RECORD_COMPLETE event
  // https://cloud.tencent.com/document/product/607/15221#.E5.81.9C.E6.AD.A2.E5.BD.95.E9.9F.B3
  QAVResult ret =  [[[ITMGContext GetInstance] GetPTT] StopRecording];
   if (ret == 0) {
       self.currentStatus = @"停止录音";
   } else {
        self.currentStatus = @"停止录音失败";
   }
  }
  :::
  ::: C++ C++
  ITMGContextGetInstance()->GetPTT()->StopRecording();
  :::
  </dx-codeblock>

	
