TRTCCalling 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1和多人视频通话。TRTCCalling 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [实时视频通话（Android）](https://cloud.tencent.com/document/product/647/42045)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。


<h2 id="TRTCCalling">TRTCCalling API 概览</h2>
 
### SDK 基础函数

| API                                             | 描述                                             |
| ----------------------------------------------- | ------------------------------------------------ |
| [sharedInstance](#sharedinstance)               | 组件单例。                                       |
| [destroySharedInstance](#destroysharedinstance) | 销毁组件单例。                                   |
| [addDelegate](#adddelegate)                     | 增加事件回调。                                   |
| [removeDelegate](#removedelegate)               | 移除回调接口。                                   |
| [destroy](#destroy)                             | 销毁函数，如果无需再运行该实例，请调用该接口。   |
| [login](#login)                                 | 登录组件接口，所有功能需要先进行登录后才能使用。 |
| [logout](#logout)                               | 登出组件接口，登出后无法再进行拨打操作。         |


### 通话操作相关接口函数

| API                     | 描述           |
| ----------------------- | -------------- |
| [call](#call)           | 单人通话邀请。 |
| [groupCall](#groupcall) | 群聊通话邀请。 |
| [accept](#accept)       | 接受当前通话。 |
| [reject](#reject)       | 拒绝当前通话。 |
| [hangup](#hangup)       | 结束当前通话。 |

### 推拉流相关接口函数

| API                                 | 描述                                                   |
| ----------------------------------- | ------------------------------------------------------ |
| [startRemoteView](#startremoteview) | 远端用户的摄像头数据渲染到指定的 TXCloudVideoView 中。 |
| [stopRemoteView](#stopremoteview)   | 停止渲染远端数据。                                     |

### 音视频控制相关接口函数

| API                           | 描述                                             |
| ----------------------------- | ------------------------------------------------ |
| [openCamera](#opencamera)     | 开启摄像头，并渲染在指定的 TXCloudVideoView 中。 |
| [switchCamera](#switchcamera) | 切换前后摄像头。                                 |
| [closeCamara](#closecamara)   | 关闭摄像头。                                     |
| [setMicMute](#setmicmute)     | 静音本地音频采集。                                   |
| [setHandsFree](#sethandsfree) | 设置免提。                                       |

<h2 id="TRTCCallingDelegate">TRTCCallingDelegate API 概览</h2>

### 通用事件回调

| API                 | 描述       |
| ------------------- | ---------- |
| [onError](#onerror) | 错误回调。 |

### 邀请方回调

| API                       | 描述             |
| ------------------------- | ---------------- |
| [onReject](#onreject)     | 拒绝通话回调。   |
| [onNoResp](#onnoresp)     | 对方无回应回调。 |
| [onLineBusy](#onlinebusy) | 通话忙线回调。   |

### 被邀请方回调

| API                                   | 描述                 |
| ------------------------------------- | -------------------- |
| [onInvited](#oninvited)               | 被邀请通话回调。     |
| [onCallingCancel](#oncallingcancel)   | 当前通话被取消回调。 |
| [onCallingTimeOut](#oncallingtimeout) | 当前通话超时回调。   |

### 通用回调

| API                                                          | 描述                       |
| ------------------------------------------------------------ | -------------------------- |
| [onGroupCallInviteeListUpdate](#ongroupcallinviteelistupdate) | 群聊更新邀请列表回调。     |
| [onUserEnter](#onuserenter)                                  | 用户进入通话回调。         |
| [onUserLeave](#onuserleave)                                  | 用户离开通话回调。         |
| [onUserAudioAvailable](#onuseraudioavailable)                | 用户是否开启音频上行回调。 |
| [onUserVideoAvailable](#onuservideoavailable)                | 用户是否开启视频上行回调。 |
| [onUserVoiceVolume](#onuservoicevolume)                      | 用户通话音量回调。         |
| [onCallEnd](#oncallend)                                      | 通话结束回调。             |

## SDK 基础函数

### sharedInstance

sharedInstance 是 TRTCCalling 的组件单例。

```java
public static ITRTCCalling sharedInstance(Context context);
```

### destroySharedInstance

销毁组件单例。

```java
public static void destroySharedInstance();
```

### destroy

销毁函数，如果无需再运行该实例，请调用该接口。

```java
void destroy();
```

### addDelegate

[TRTCCalling](https://cloud.tencent.com/document/product/647/42045) 事件回调，您可以通过 TRTCCallingDelegate 获得 [TRTCCalling](https://cloud.tencent.com/document/product/647/42045) 的各种状态通知。

```java
public abstract void addDelegate(TRTCCallingDelegate delegate);
```

>?TRTCCallingDelegate 是 TRTCCalling 的代理回调。

### removeListener

移除回调接口。

```java
void removeDelegate(TRTCCallingDelegate listener);
```

### login

登录组件。

```java
void login( int sdkAppId,
            final String userId, 
            String userSign, 
            final ActionCallBack callback);
```

参数如下表所示：

| 参数     | 类型           | 含义                                                         |
| -------- | -------------- | ------------------------------------------------------------ |
| sdkAppID | UInt32         | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| user     | String         | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | String         | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |
| callback | ActionCallBack | 登录回调，`onSuccess` 表示登录成功。                         |

### logout

登出组件。

```java
void logout(final ActionCallBack callBack);
```

参数如下表所示：

| 参数     | 类型           | 含义                                 |
| -------- | -------------- | ------------------------------------ |
| callBack | ActionCallBack | 登出回调，`onSuccess` 表示登出成功。 |

## 通话操作相关接口函数

### call

单人通话邀请，当前处于通话中也可继续调用邀请他人。

```java
void call(String userId, int type);
```

参数如下表所示：

| 参数   | 类型   | 含义                             |
| ------ | ------ | -------------------------------- |
| userId | String | 呼叫用户 ID。                    |
| type   | int    | 1 表示语音通话，2 表示视频通话。 |

### groupCall

IM 群组邀请通话，被邀请方会收到 `onInvited()` 回调。如果当前处于通话中，可以继续调用该函数继续邀请他人进入通话，同时正在通话的用户会收到 `onGroupCallInviteeListUpdate()` 回调。

```java
void groupCall(List<String> userIdList, int type, String groupId);
```

参数如下表所示：

| 参数       | 类型               | 含义                             |
| ---------- | ------------------ | -------------------------------- |
| userIdList | List&lt;String&gt; | 邀请 ID 列表。                   |
| type       | int                | 1 表示语音通话，2 表示视频通话。 |
| groupId    | String             | 群 ID。                          |



### accept

接受当前通话。当您作为被邀请方收到 `onInvited()` 的回调时，可以调用该函数接听来电。

```java
void accept();
```



### reject

拒绝当前通话。当您作为被邀请方收到 `onInvited()` 的回调时，可以调用该函数拒绝来电。

```java
void reject();
```



### hangup

挂断当前通话。当您处于通话中，可以调用该函数结束通话。

```java
void hangup();
```


## 推拉流相关接口函数

### startRemoteView

远端用户的摄像头数据渲染到指定的 TXCloudVideoView 中。

```java
void startRemoteView(String userId, TXCloudVideoView txCloudVideoView);
```

参数如下表所示：

| 参数   | 类型             | 含义                 |
| ------ | ---------------- | -------------------- |
| userId | String           | 远端用户 ID。        |
| view   | TXCloudVideoView | 承载视频画面的控件。 |


### stopRemoteView

停止渲染远端数据。

```java
void stopRemoteView(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义          |
| ------ | ------ | ------------- |
| userId | String | 远端用户 ID。 |

## 音视频控制相关接口函数

### openCamera

开启摄像头，并渲染在指定的 TXCloudVideoView 中。

```java
void openCamera(boolean isFrontCamera, TXCloudVideoView txCloudVideoView);
```

参数如下表所示：

| 参数          | 类型             | 含义                                                |
| ------------- | ---------------- | --------------------------------------------------- |
| isFrontCamera | boolean          | true 表示开启前置摄像头，false 表示开启后置摄像头。 |
| view          | TXCloudVideoView | 承载视频画面的控件。                                |

### switchCamera

切换前后摄像头。

```java
void switchCamera(boolean isFrontCamera);
```

参数如下表所示：

| 参数          | 类型    | 含义                                                    |
| ------------- | ------- | ------------------------------------------------------- |
| isFrontCamera | boolean | true 表示切换到前置摄像头，false 表示切换到后置摄像头。 |

### closeCamara

关闭摄像头。

```java
void closeCamera();
```

### setMicMute

静音本地音频采集。

```java
void setMicMute(boolean isMute);
```

参数如下表所示：

| 参数   | 类型    | 含义                                        |
| ------ | ------- | ------------------------------------------- |
| isMute | boolean | true 表示麦克风关闭，false 表示麦克风打开。 |

### setHandsFree

静音远端音频。

```java
void setHandsFree(boolean isHandsFree);
```

参数如下表所示：

| 参数        | 类型    | 含义                                    |
| ----------- | ------- | --------------------------------------- |
| isHandsFree | boolean | true 表示开启免提，false 表示关闭免提。 |

## TRTCCallingDelegate 事件回调

## 通用事件回调

### onError

错误回调。

>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

```java
void onError(int code, String msg);
```

参数如下表所示：

| 参数 | 类型   | 含义       |
| ---- | ------ | ---------- |
| code | int    | 错误码。   |
| msg  | String | 错误信息。 |


## 邀请方回调

### onReject

拒绝通话回调。

```java
void onReject(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义            |
| ------ | ------ | --------------- |
| userId | String | 拒绝用户的 ID。 |

### onNoResp

对方无回应回调。

```java
void onNoResp(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义              |
| ------ | ------ | ----------------- |
| userId | String | 无回应用户的 ID。 |

### onLineBusy

通话忙线回调。

```java
void onLineBusy(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义            |
| ------ | ------ | --------------- |
| userId | String | 忙线用户的 ID。 |

## 被邀请方回调

### onInvited

被邀请通话回调。

```java
void onInvited(String sponsor, List<String> userIdList, boolean isFromGroup, int callType);
```

参数如下表所示：

| 参数        | 类型               | 含义                             |
| ----------- | ------------------ | -------------------------------- |
| sponsor     | String             | 发起方的 ID。                    |
| userIds     | List&lt;String&gt; | 除自己外被邀请 ID 列表。         |
| isFromGroup | boolean            | 是否多人通话邀请。               |
| type        | int                | 1 表示语音通话，2 表示视频通话。 |

### onCallingCancel

当前通话被取消回调。接收方未处理请求，邀请方取消后会收到此回调。

```java
void onCallingCancel();
```



### onCallingTimeOut

当前通话超时回调。

```java
void onCallingTimeout();
```

## 通用回调

### onGroupCallInviteeListUpdate

群聊更新邀请列表回调。

```java
void onGroupCallInviteeListUpdate(List<String> userIdList);
```

参数如下表所示：

| 参数       | 类型               | 含义           |
| ---------- | ------------------ | -------------- |
| userIdList | List&lt;String&gt; | 邀请 ID 列表。 |

### onUserEnter

用户进入通话回调。

```java
void onUserEnter(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义              |
| ------ | ------ | ----------------- |
| userId | String | 进入通话用户 ID。 |

### onUserLeave

用户离开通话回调。

```java
void onUserLeave(String userId);
```

参数如下表所示：

| 参数   | 类型   | 含义              |
| ------ | ------ | ----------------- |
| userId | String | 离开通话用户 ID。 |

### onUserAudioAvailable

用户是否开启音频上行回调。

```java
void onUserAudioAvailable(String userId, boolean available);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userId    | String  | 通话用户 ID。      |
| available | boolean | 用户音频是否可用。 |

### onUserVideoAvailable

用户是否开启视频上行回调。收到通知后，用户可调用 `startRemoteView` 渲染远端视频。

```java
void onUserVideoAvailable(String userId, boolean available);
```

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userId    | String  | 通话用户 ID。      |
| available | boolean | 用户视频是否可用。 |


### onUserVoiceVolume

用户通话音量回调。

```java
void onUserVoiceVolume(Map<String, Integer> volumeMap);
```

参数如下表所示：

| 参数      | 类型                       | 含义                                                         |
| --------- | -------------------------- | ------------------------------------------------------------ |
| volumeMap | Map&lt;String, Integer&gt; | 音量表，根据每个 userid 可以获取对应的音量大小，音量最小值为0，音量最大值为100。 |

### onCallEnd

通话结束回调。

```java
void onCallEnd();
```
