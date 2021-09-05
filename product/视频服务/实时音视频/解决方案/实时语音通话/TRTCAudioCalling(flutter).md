TRTCCalling 是基于腾讯云实时音视频（TRTC）和即时通信 IM 服务组合而成的，支持1v1音视频通话。TRTCCalling 是一个开源的 Class，依赖腾讯云的两个闭源 SDK，具体的实现过程请参见 [实时语音通话（Flutter）](https://cloud.tencent.com/document/product/647/56293)。

- TRTC SDK：使用 [TRTC SDK](https://cloud.tencent.com/document/product/647) 作为低延时音视频通话组件。
- IM SDK：使用 [IM SDK](https://cloud.tencent.com/document/product/269) 发送和处理信令消息。


<h2 id="TRTCCalling">TRTCCalling API 概览</h2>

### SDK 基础函数

| API                                             | 描述                                             |
| ----------------------------------------------- | ------------------------------------------------ |
| [sharedInstance](#sharedinstance)               | 组件单例。                                       |
| [destroySharedInstance](#destroysharedinstance) | 销毁组件单例。                                   |
| [registerListener](#registerlistener)                     | 增加事件回调。                                   |
| [unRegisterListener](#unregisterlistener)               | 移除回调接口。                                   |
| [destroy](#destroy)                             | 销毁函数，如果无需再运行该实例，请调用该接口。   |
| [login](#login)                                 | 登录组件接口，所有功能需要先进行登录后才能使用。 |
| [logout](#logout)                               | 登出组件接口，登出后无法再进行拨打操作。         |


### 通话操作相关接口函数

| API                     | 描述           |
| ----------------------- | -------------- |
| [call](#call)           | 单人通话邀请。 |
| [accept](#accept)       | 接受当前通话。 |
| [reject](#reject)       | 拒绝当前通话。 |
| [hangup](#hangup)       | 结束当前通话。 |


### 音频控制相关接口函数

| API                           | 描述                                             |
| ----------------------------- | ------------------------------------------------ |
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
| 
| [onUserEnter](#onuserenter)                                  | 用户进入通话回调。         |
| [onUserLeave](#onuserleave)                                  | 用户离开通话回调。         |
| [onUserAudioAvailable](#onuseraudioavailable)                | 用户是否开启音频上行回调。 |
| [onUserVoiceVolume](#onuservoicevolume)                      | 用户通话音量回调。         |
| [onCallEnd](#oncallend)                                      | 通话结束回调。             |

## SDK 基础函数

### sharedInstance

sharedInstance 是 TRTCCalling 的组件单例。

```java
static Future<TRTCCalling> sharedInstance();
```

### destroySharedInstance

销毁组件单例。

```java
static void destroySharedInstance();
```

### destroy

销毁函数，如果无需再运行该实例，请调用该接口。

```java
void destroy();
```

### registerListener

[TRTCCalling](https://cloud.tencent.com/document/product/647/42045) 事件回调，您可以通过 TRTCCallingDelegate 获得 [TRTCCalling](https://cloud.tencent.com/document/product/647/42045) 的各种状态通知。

```java
void registerListener(VoiceListenerFunc func);
```


### unRegisterListener

移除回调接口。

```java
void unRegisterListener(VoiceListenerFunc func);
```

### login

登录组件。

```java
Future<ActionCallback> login(int sdkAppId, String userId, String userSig);
```

参数如下表所示：

| 参数     | 类型           | 含义                                                         |
| -------- | -------------- | ------------------------------------------------------------ |
| sdkAppID | int         | 您可以在实时音视频控制台 >【[应用管理](https://console.cloud.tencent.com/trtc/app)】> 应用信息中查看 SDKAppID。 |
| userId     | String         | 当前用户的 ID，字符串类型，只允许包含英文字母（a-z 和 A-Z）、数字（0-9）、连词符（-）和下划线（\_）。 |
| userSig  | String         | 腾讯云设计的一种安全保护签名，获取方式请参考 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。 |

### logout

登出组件。

```java
Future<ActionCallback> logout();
```

## 通话操作相关接口函数

### call

单人通话邀请，当前处于通话中也可继续调用邀请他人。

```java
Future<ActionCallback> call(String userId, int type);
```

参数如下表所示：

| 参数   | 类型   | 含义                             |
| ------ | ------ | -------------------------------- |
| userId | String | 呼叫用户 ID。                    |
| type   | int    | 1 表示语音通话，2 表示视频通话。 |

### accept

接受当前通话。当您作为被邀请方收到 `onInvited()` 的回调时，可以调用该函数接听来电。

```java
Future<ActionCallback> accept();
```

### reject

拒绝当前通话。当您作为被邀请方收到 `onInvited()` 的回调时，可以调用该函数拒绝来电。

```java
Future<ActionCallback> reject();
```

### hangup

挂断当前通话。当您处于通话中，可以调用该函数结束通话。

```java
void hangup();
```


## 音频控制相关接口函数

### setMicMute

静音本地音频采集。

```java
void setMicMute(bool isMute);
```

参数如下表所示：

| 参数   | 类型    | 含义                                        |
| ------ | ------- | ------------------------------------------- |
| isMute | bool | true 表示麦克风关闭，false 表示麦克风打开。 |

### setHandsFree

静音远端音频。

```java
void setHandsFree(bool isHandsFree);
```

参数如下表所示：

| 参数        | 类型    | 含义                                    |
| ----------- | ------- | --------------------------------------- |
| isHandsFree | bool | true 表示开启免提，false 表示关闭免提。 |

## TRTCCallingDelegate 事件回调

## 通用事件回调

### onError

错误回调。

>?SDK 不可恢复的错误，一定要监听，并分情况给用户适当的界面提示。

参数如下表所示：

| 参数 | 类型   | 含义       |
| ---- | ------ | ---------- |
| code | int    | 错误码。   |
| msg  | String | 错误信息。 |


## 邀请方回调

### onReject

拒绝通话回调。

参数如下表所示：

| 参数   | 类型   | 含义            |
| ------ | ------ | --------------- |
| userId | String | 拒绝用户的 ID。 |

### onNoResp

对方无回应回调。

参数如下表所示：

| 参数   | 类型   | 含义              |
| ------ | ------ | ----------------- |
| userId | String | 无回应用户的 ID。 |

### onLineBusy

通话忙线回调。


参数如下表所示：

| 参数   | 类型   | 含义            |
| ------ | ------ | --------------- |
| userId | String | 忙线用户的 ID。 |

## 被邀请方回调

### onInvited

被邀请通话回调。

参数如下表所示：

| 参数        | 类型               | 含义                             |
| ----------- | ------------------ | -------------------------------- |
| sponsor     | String             | 发起方的 ID。                    |
| userIds     | List&lt;String&gt; | 除自己外被邀请 ID 列表。         |
| isFromGroup | bool          | 是否多人通话邀请。               |
| type        | int                | 1 表示语音通话，2 表示视频通话。 |

### onCallingCancel

当前通话被取消回调。接收方未处理请求，邀请方取消后会收到此回调。


### onCallingTimeOut

当前通话超时回调。


## 通用回调

### onUserEnter

用户进入通话回调。

参数如下表所示：

| 参数   | 类型   | 含义              |
| ------ | ------ | ----------------- |
| userId | String | 进入通话用户 ID。 |

### onUserLeave

用户离开通话回调。

参数如下表所示：

| 参数   | 类型   | 含义              |
| ------ | ------ | ----------------- |
| userId | String | 离开通话用户 ID。 |

### onUserAudioAvailable

用户是否开启音频上行回调。

参数如下表所示：

| 参数      | 类型    | 含义               |
| --------- | ------- | ------------------ |
| userId    | String  | 通话用户 ID。      |
| available | boolean | 用户音频是否可用。 |


### onUserVoiceVolume

用户通话音量回调。

参数如下表所示：

| 参数      | 类型                       | 含义                                                         |
| --------- | -------------------------- | ------------------------------------------------------------ |
| userVolumes | List | 所有正在说话的房间成员的音量，取值范围：0 - 100。 |
| totalVolume | int| 所有远端成员的总音量, 取值范围：0 - 100。|

### onCallEnd

通话结束回调。
