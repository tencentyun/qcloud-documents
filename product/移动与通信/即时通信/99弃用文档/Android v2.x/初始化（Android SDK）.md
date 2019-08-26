## 获取通讯管理器
ImSDK 一切操作都是由通讯管理器 `TIMManager` 开始，SDK 操作第一步需要获取通讯管理器实例 `TIMManager`。

**原型：**
```
public static TIMManager getInstance()
```

**示例：**
```
TIMManager.getInstance();
```

## 新消息通知
在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调 `TIMMessageListener`，在用户登录状态下，会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。

**原型：**

```
/**
 * 添加一个消息监听器
 * @param listener 消息监听器
 *                 默认情况下所有消息监听器都将按添加顺序被回调一次
 *                 除非用户在 onNewMessages 回调中返回 true，此时将不再继续回调下一个消息监听器
 */
public void addMessageListener(TIMMessageListener listener) 
```

添加一个消息监听器，默认情况下所有消息监听器都将按添加顺序被回调一次，除非用户在 `onNewMessages` 回调中返回 true，此时将不再继续回调下一个消息监听器。
**收到新消息回调：**
```
/**
* 收到新消息回调
* @param msgs 收到的新消息
* @return 正常情况下，如果注册了多个listener, SDK会顺序回调到所有的listener。当碰到listener的回调返回true的时候，将终止继续回调后续的listener。
*/
public boolean onNewMessages(List<TIMMessage> msgs)
```

消息监听器被删除后，将不再被调用。
**删除一个消息监听器：**
```
public void removeMessageListener(TIMMessageListener listener)
```

> 注：回调消息内容通过参数 `TIMMessage` 传递，通过 `TIMMessage` 可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等，可参阅 [消息解析](/doc/product/269/消息收发（Android%20SDK）#.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90)。

**示例：**

```
//设置消息监听器，收到新消息时，通过此监听器回调
TIMManager.getInstance().addMessageListener(new TIMMessageListener() {//消息监听器
 
    @Override
    public boolean onNewMessages(List<TIMMessage> msgs) {//收到新消息
		//消息的内容解析请参考消息解析
		return true; //返回 true 将终止回调链，不再调用下一个新消息监听器
    }
});
```

## 网络事件通知
可选设置，如果要用户感知是否已经连接服务器，需要设置此回调，用于通知调用者跟通讯后台链接的连接和断开事件。另外，如果断开网络，等网络恢复后会自动重连，自动拉取消息通知用户，用户无需关心网络状态，仅作通知之用。

> **注意：**
> 这里的网络事件不表示用户本地网络状态，仅指明 SDK 是否与 IM 云 Server 连接的状态。只要用户处于登录状态，**ImSDK 内部会进行断网重连，用户无需关心**。

**原型：**

```
public void setConnectionListener(TIMConnListener listener)
```

**设置连接监听器的示例：**

```
//设置网络连接监听器，连接建立／断开时回调
TIMManager.getInstance().setConnectionListener(new TIMConnListener() {//连接监听器
    @Override
    public void onConnected() {//连接建立
        Log.e(tag, "connected");
    }
 
    @Override
    public void onDisconnected(int code, String desc) {//连接断开
        //接口返回了错误码 code 和错误描述 desc，可用于定位连接断开原因
        //错误码 code 含义请参见错误码表
        Log.e(tag, "disconnected");
    }
});
```
## 日志事件
SDK 内部会进行打印日志，如果调用方有自己统一的日志收集方式，可以设置日志回调事件，把日志通过回调返给调用方，但 ImSDK 仍然内部仍然会打印，如果需要禁掉，可以通过设置控制台不打印日志，或者设置日志级别。

**原型：**
```
public void setLogListener(TIMLogListener listener)
```

**设置日志监听器的示例：**
```
//设置日志回调，SDK 输出的日志将通过此接口回传一份副本
//[NOTE] 请注意 level 定义在 TIMManager 中，如 TIMManager.ERROR 等， 并不同于 Android 系统定义
TIMManager.getInstance().setLogListener(new TIMLogListener() {
    @Override
    public void log(int level, String tag, String msg) {
        //可以通过此回调将 SDK 的 log 输出到自己的日志系统中
    }
});
```

## 用户状态变更
用户状态变更的时候，SDK 会有相应的通知。通过 `TIMManager` 中的 `setUserStatusListener` 方法可以设置用户状态变更通知监听器来对相应的通知进行监听。目前用户状态变更有两种通知，具体可参见 [用户被踢下线通知](#.E7.94.A8.E6.88.B7.E8.A2.AB.E8.B8.A2.E4.B8.8B.E7.BA.BF.E9.80.9A.E7.9F.A5) 和 [用户票据过期通知](#.E7.94.A8.E6.88.B7.E7.A5.A8.E6.8D.AE.E8.BF.87.E6.9C.9F.E9.80.9A.E7.9F.A5)。

**设置用户状态变更通知监听器的原型：**

```
public void setUserStatusListener(TIMUserStatusListener userStatusListener)
```

**参数：**

|参数|说明|
|---|---|
|userStatusListener|用户状态变更通知监听器|

**用户状态变更通知监听器 `TIMUserStatusListener` 的定义如下：**

```
/**
 * 用户状态变更通知监听器
 */
public interface TIMUserStatusListener {

    /**
     * 被踢下线时回调
     */
    public void onForceOffline();

    /**
     * 票据过期时回调
     */
    public void onUserSigExpired();
}
```

**示例：**

```
//设置用户状态变更监听器，在回调中进行相应的处理
TIMManager.getInstance().setUserStatusListener(new TIMUserStatusListener() {
	@Override
	public void onForceOffline() {
		//被踢下线
	}

	@Override
	public void onUserSigExpired() {
		//票据过期，需要换票后重新登录
	}
});
```

### 用户被踢下线通知
用户如果在其他终端登录，会被踢下线，这时会收到用户被踢下线的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onForceOffline` 中进行相应的处理，出现这种情况常规的做法是提示用户进行操作（退出，或者再次把对方踢下线）。

> **注意：**
> 用户如果在离线状态下被踢，下次登录将会失败，可以给用户一个非常强的提醒（登录错误码 `ERR_IMSDK_KICKED_BY_OTHERS：6208`），开发者也可以选择忽略这次错误，再次登录即可。


**用户在线状态互踢：**用户在设备 1 登录，保持在线状态下，该用户又在设备 2 登录，这时用户会在设备 1 上强制下线，收到 `onForceOffline` 回调。用户在设备 1 上收到回调后，提示用户，可继续调用 `login` 上线，强制设备 2 下线。这里是在线情况下互踢过程。如下图所示：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021645_19906.png)

**用户离线状态互踢：**用户在设备 1 登录，没有进行 `logout` 情况下进程退出（此时可接收 iOS 远程推送消息）。该用户在设备 2 登录，此时由于用户不在线，无法感知此事件，为了显式提醒用户，避免无感知的互踢，用户在设备 1 重新登录时，会返回（`ERR_IMSDK_KICKED_BY_OTHERS：6208`）错误码，表明之前被踢，是否需要把对方踢下线。如果需要，则再次调用 `login` 强制上线，设备 2 的登录的实例将会收到 `onForceOffline` 回调。如下图所示：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021702_68733.png)



### 用户票据过期通知

在用户登录（参见 [登录](/doc/product/269/%E7%99%BB%E5%BD%95%EF%BC%88Android%20SDK%EF%BC%89#.E7.99.BB.E5.BD.95)）的时候，需要提供一个用户票据，而这个用户票据在生成的时候是有一个有效使用期限的。在正常使用过程中，如果超过了用户票据的使用期限时，SDK 与服务器的交互会因为票据验证失败而操作失败，这个时候 SDK 会给出用户票据过期的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onUserSigExpired` 中进行相应的处理，出现这种情况，如果仍需要继续与服务器进行交互，则需要更换票据后重新登录。


## Crash 上报

ImSDK 内部集成了 [Bugly 系统](http://bugly.qq.com)，当应用 Crash 后，会自动上报到平台，用户可以根据 Bugly 文档指示上传符号表，显示 Crash 详细信息。如果用户有自己的上报组件，可调用 `disableCrashReport` 接口禁用上报。

> **注意：**
> 禁用 Crash 上报，由用户自己上报，如果需要，必须在 init SDK 之前调用。

**原型：**

```
public void disableCrashReport()
```

**示例：**

```
//禁用 Crash 上报
TIMManager.getInstance().disableCrashReport();
```

## 设置日志级别

在权限允许的情况下，ImSDK 的日志默认会写到日志文件中。通过 `setLogLevel` 修改 ImSDK 内部日志级别，可以控制 ImSDK 的文件日志输出。

> **注意：**
> 设置写日志等级， **必须在 SDK 初始化之前调用**，在 SDK 初始化之后设置无效。

**原型：**
```
public void setLogLevel(TIMLogLevel level)
```

**参数：**
> 注：可以通过设置日志级别为 `TIMLogLevel.OFF` 来关闭 ImSDK 的文件日志输出，提升性能，建议在开发期间打开日志，方便排查问题。

```
level - 日志等级。
```

## 控制台不打印日志或修改日志路径
默认 ImSDK 日志会打印到控制台，如果调试期间干扰太多，可选择关闭控制台日志（此时文件日志仍然会打印，可设置日志级别禁用），另外也可以修改默认的存储路径，方便管理。

> **注意：**
> 初始化日志设置， **必须在 SDK 初始化之前调用**，在 SDK 初始化之后设置无效。

**原型：**
```
public void initLogSettings(boolean isEnableLogPrint, String logPath)
```

**参数：**

> 注：如果不关心 ImSDK 日志路径，可以通过 `setLogPrintEnable` 来设置是否开启控制台日志打印。

```
isEnableLogPrint - 是否开启日志控制台打印。true - 开启， false - 关闭。
logPath - ImSDK 日志文件存储路径，传入 null 时将使用默认路径（SD 卡下，/tencent/imsdklogs/(your app package name)/）。
```

**设置是否开启控制台 log 输出的原型：**
```
public void setLogPrintEnable(boolean isEnable)
```

**参数：**
```
isEnable - 是否开启控制台 log 输出：true开启，false关闭，默认开启。
```

## 禁用存储
默认情况 ImSDK 会进行消息的存储，如无需存储，可选择关闭存储来提升处理性能。

> **注意：**
> 禁用存储，在不需要消息存储的场景可以禁用存储，提升效率。**需要在初始化之后登录之前调用。**

**原型：**

```
public void disableStorage()
```

## 通讯管理器初始化

在使用SDK进一步操作之前，需要初始化SDK。**在存在多进程的情况下，请只在一个进程进行 SDK 初始化。**

**原型：**
```
public void init(Context context)
```

**初始化，参数为应用的 context 的示例：**
```
TIMManager.getInstance().init(context);
```
