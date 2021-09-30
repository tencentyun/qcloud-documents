## 获取通讯管理器
IM SDK 一切操作都是由通讯管理器 `TIMManager` 开始，IM SDK 操作第一步需要获取 `TIMManager` 单例。`getInstance`获取通讯管理器实例原型如下。

**原型：**

```
public static TIMManager getInstance()
```

**示例：**

```
TIMManager.getInstance();
```
## 初始化 IM SDK 配置
在初始化 IM SDK 之前，需要进行简单的 IM SDK 配置，包括 SDKAppID、日志控制等。对应的配置类为 `TIMSdkConfig`。

### 日志事件

IM SDK 内部会进行打印日志，如果调用方有自己统一的日志收集方式，可以通过 `TIMSdkConfig` 中的 `setLogListener` 接口设置日志事件回调，把日志通过回调返给调用方，但 IM SDK 内部仍然会打印，如果需要禁掉，可以通过设置控制台不打印日志，或者设置日志级别。

**原型：**

```
/**
 * 设置当前日志回调监听器， 必须在 IM SDK 初始化之前设置
 * @param logListener 日志回调监听器
 */
public TIMSdkConfig setLogListener(TIMLogListener logListener) 
```

**示例：**

```
//设置日志回调，IM SDK 输出的日志将通过此接口回传一份副本
//[NOTE] 请注意 level 定义在 TIMManager 中，如 TIMManager.ERROR 等， 并不同于 Android 系统定义
mTIMSdkConfig.setLogListener(new TIMLogListener() {
    @Override
    public void log(int level, String tag, String msg) {
        //可以通过此回调将 sdk 的 log 输出到自己的日志系统中
    }
});
```

### 设置日志级别

在权限允许的情况下，IM SDK 的日志默认会写到日志文件中。通过 `TIMSdkConfig` 中的 `setLogLevel` 接口修改 IM SDK 内部写日志级别可以控制 IM SDK 的文件日志输出。

>!
>- 设置写日志等级， **必须在 IM SDK 初始化之前调用**，在 IM SDK 初始化之后设置无效。
>- 可以通过设置日志级别为 TIMLogLevel.OFF 来关闭 IM SDK 的文件日志输出，建议打开日志，方便排查问题。

**原型：**

```
/**
 * 设置写日志等级，必须在 IM SDK 初始化之前调用，在 IM SDK 初始化之后设置无效
 * @param logLevel 日志等级
 */
public TIMSdkConfig setLogLevel(@NonNull TIMLogLevel logLevel) 
```


### 控制台不打印日志

默认 IM SDK 日志会打印到控制台，如果调试期间干扰太多，可选择通过 `TIMSdkConfig` 中的 `enableLogPrint` 关闭控制台日志（此时文件日志仍然会打印，可设置日志级别禁用）。

>! 日志设置， **必须在 IM SDK 初始化之前调用**，在 IM SDK 初始化之后设置无效。


**原型：**

```
/**
 * 设置是否把日志输出到控制台， 必须在 IM SDK 初始化之前设置
 * @param logPrintEnabled true - 日志将会输出到控制台
 */
public TIMSdkConfig enableLogPrint(boolean logPrintEnabled) 
```

### 修改日志路径

为了方便统一管理日志，也可以修改默认的日志存储路径。通过 `TIMSdkConfig` 中的 `setLogPath` 接口可以设置日志文件存储路径。

>!
> * 设置日志路径，**必须在 IM SDK 初始化之前调用**，在 IM SDK 初始化之后设置无效。
> * IM SDK 默认日志存储路径为：SD 卡下，`/tencent/imsdklogs/(your app package name)/`

**原型：**

```
/**
 * 设置日志路径，必须在 IM SDK 初始化之前调用，在 IM SDK 初始化之后设置无效
 * @param logPath 日志路径
 */
public TIMSdkConfig setLogPath(@NonNull String logPath)
```

## 初始化 IM SDK

在使用 IM SDK 进一步操作之前，需要初始化 IM SDK。

>! 在存在**多进程**的情况下，请只在一个进程进行 IM SDK 初始化，调用接口`SessionWrapper.isMainProcess(Context context)`判断。

**原型：**

```
/**
 * 初始化 IM SDK
 * @param context  application context
 * @param config IM SDK 全局配置
 * @return true - 初始化成功， false - 初始化失败
 */
public boolean init(@NonNull Context context, @NonNull TIMSdkConfig config)
```

**示例：**

```
//初始化 IM SDK 基本配置
//判断是否是在主线程
if (SessionWrapper.isMainProcess(getApplicationContext())) {
	TIMSdkConfig config = new TIMSdkConfig(sdkAppId)
			.enableCrashReport(false)  //接口已废弃
			.enableLogPrint(true)
			.setLogLevel(TIMLogLevel.DEBUG)
			.setLogPath(Environment.getExternalStorageDirectory().getPath() + "/justfortest/");

	//初始化 SDK
	TIMManager.getInstance().init(getApplicationContext(), config);
}
```
## 用户配置

在初始化 IM SDK 后，登录 IM SDK 之前，可以通过 TIMUserConfig 进行用户配置。配置完成后，**在登录前**，通过通讯管理器 `TIMManager` 的接口 `setUserConfig` 将用户配置与当前通讯管理器进行绑定。

**原型：**
```
/**
 * 设置当前用户的用户配置，登录前设置
 * @param userConfig 用户配置
 */
public void setUserConfig(TIMUserConfig userConfig) 
```

**示例：**
```
//基本用户配置
TIMUserConfig userConfig = new TIMUserConfig()
		//设置用户状态变更事件监听器
		.setUserStatusListener(new TIMUserStatusListener() {
			@Override
			public void onForceOffline() {
				//被其他终端踢下线
				Log.i(tag, "onForceOffline");
			}

			@Override
			public void onUserSigExpired() {
				//用户签名过期了，需要刷新 userSig 重新登录 IM SDK
				Log.i(tag, "onUserSigExpired");
			}
		})
		//设置连接状态事件监听器
		.setConnectionListener(new TIMConnListener() {
			@Override
			public void onConnected() {
				Log.i(tag, "onConnected");
			}

			@Override
			public void onDisconnected(int code, String desc) {
				Log.i(tag, "onDisconnected");
			}

			@Override
			public void onWifiNeedAuth(String name) {
				Log.i(tag, "onWifiNeedAuth");
			}
		})
		//设置群组事件监听器
		.setGroupEventListener(new TIMGroupEventListener() {
			@Override
			public void onGroupTipsEvent(TIMGroupTipsElem elem) {
				Log.i(tag, "onGroupTipsEvent, type: " + elem.getTipsType());
			}
		})
		//设置会话刷新监听器
		.setRefreshListener(new TIMRefreshListener() {
			@Override
			public void onRefresh() {
				Log.i(tag, "onRefresh");
			}

			@Override
			public void onRefreshConversation(List<TIMConversation> conversations) {
				Log.i(tag, "onRefreshConversation, conversation size: " + conversations.size());
			}
		});

//禁用本地所有存储
userConfig.disableStorage();
//开启消息已读回执
userConfig.enableReadReceipt(true);
		
//将用户配置与通讯管理器进行绑定
TIMManager.getInstance().setUserConfig(userConfig);
```

### 网络事件通知

可选设置，如果要用户感知是否已经连接服务器，需要通过 `TIMUserConfig` 来设置此回调，用于通知调用者跟通讯后台链接的连接和断开事件，另外，如果断开网络，等网络恢复后会自动重连，自动拉取消息通知用户，用户无需关心网络状态，仅作通知之用。

>!这里的网络事件不表示用户本地网络状态，仅指明 IM SDK 是否与 IM 云 Server 连接状态。只要用户处于登录状态，**IM SDK 内部会进行断网重连，用户无需关心**。

**原型：**

```
/**
 * 设置连接监听器
 * @param listener 连接监听器
 */
public TIMUserConfig setConnectionListener(TIMConnListener listener) 
```

**示例：**

请参考 [用户配置](#.E7.94.A8.E6.88.B7.E9.85.8D.E7.BD.AE) 中的示例。

### 用户状态变更

用户状态变更的时候，IM SDK 会有相应的通知。通过 `TIMUserConfig` 设置用户状态变更通知监听器来对相应的通知进行监听。目前用户状态变更有两种通知，具体可参见 [用户被踢下线通知](#.E7.94.A8.E6.88.B7.E8.A2.AB.E8.B8.A2.E4.B8.8B.E7.BA.BF.E9.80.9A.E7.9F.A5) 和 [用户票据过期通知](#.E7.94.A8.E6.88.B7.E7.A5.A8.E6.8D.AE.E8.BF.87.E6.9C.9F.E9.80.9A.E7.9F.A5)。

**原型：**

```
/**
 * 设置用户状态通知回调
 * @param userStatusListener 用户状态通知回调
 */
public TIMUserConfig setUserStatusListener(TIMUserStatusListener userStatusListener)
```

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

请参考 [用户配置](#.E7.94.A8.E6.88.B7.E9.85.8D.E7.BD.AE) 中的示例。


### 用户被踢下线通知

用户如果在其他终端登录，会被踢下线，这时会收到用户被踢下线的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法`onForceOffline`中进行相应的处理，出现这种情况常规的做法是提示用户进行操作（退出，或者再次把对方踢下线）。


>!用户如果在离线状态下被踢，下次登录将会失败，可以给用户一个非常强的提醒（登录错误码 ERR_IMSDK_KICKED_BY_OTHERS：6208），开发者也可以选择忽略这次错误，再次登录即可。

用户在线情况下的互踢情况如下图所示。用户在设备 1 登录，保持在线状态下，该用户又在设备 2 登录，这时用户会在设备 1 上强制下线，收到 `onForceOffline` 回调。用户在设备 1 上收到回调后，提示用户，可继续调用 `login` 上线，强制设备 2 下线。这里是在线情况下互踢过程。

![](https://main.qcloudimg.com/raw/5f4091568e3bae2b625112add7ae60fe.png)

用户离线状态互踢如下图所示。用户在设备 1 登录，没有进行 `logout` 情况下杀掉应用进程。该用户在设备 2 登录，此时由于应用进程已不在了，设备 1 无法感知此事件，为了显式提醒用户，避免无感知的互踢，用户重新在设备 1 登录时，会返回（`ERR_IMSDK_KICKED_BY_OTHERS：6208`）错误码，表明之前被踢，是否需要把对方踢下线。如果需要，则再次调用`login`强制上线，设备2的登录的实例将会收到 `onForceOffline` 回调。
![](https://main.qcloudimg.com/raw/4fb97b610d233d87c0057031f91cf683.png)

### 用户票据过期通知

在用户登录（参见 [登录](https://cloud.tencent.com/doc/product/269/9233#.E7.99.BB.E5.BD.951)）的时候，需要提供一个用户票据，而这个用户票据在生成的时候是有一个有效使用期限的。在正常使用过程中，如果超过了用户票据的使用期限时，SDK 与服务器的交互会因为票据验证失败而操作失败，这个时候 SDK 会给出用户票据过期的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onUserSigExpired` 中进行相应的处理，出现这种情况，如果仍需要继续与服务器进行交互，则需要更换票据后重新登录。


### 禁用存储
默认情况 IM SDK 会进行消息、资料、会话等存储，如无需存储，可选择通过 `TIMUserConfig` 关闭存储来提升处理性能。

>! 禁用本地存储，**需要在登录之前调用**。

**原型：**
```
/**
 * 禁用本地存储
 */
public TIMUserConfig disableStorage() 
```

### 会话刷新监听

默认登录后会异步获取 C2C 离线消息、最近联系人以及同步资料数据（如果有开启 IM SDK 存储，可参见 [关系链资料存储](https://cloud.tencent.com/doc/product/269/9231#7.-.E5.85.B3.E7.B3.BB.E9.93.BE.E8.B5.84.E6.96.99.E5.AD.98.E5.82.A8) 及 [群资料存储](https://cloud.tencent.com/doc/product/269/9236#8.-.E7.BE.A4.E8.B5.84.E6.96.99.E5.AD.98.E5.82.A837)），同步完成后会通过会话刷新监听器 `TIMRefreshListener` 中的 `onRefresh` 回调通知更新界面，用户得到这个消息时，可以刷新界面，例如会话列表的未读等。

>!如果不需要离线消息，可以在发消息时 [发送在线消息](https://cloud.tencent.com/doc/product/269/9232#.E5.9C.A8.E7.BA.BF.E6.B6.88.E6.81.AF)。

在多终端情况下，未读消息计数由 Server 下发同步通知，IM SDK 在本地更新未读计数后，通知用户更新会话。通知会通过 `TIMRefreshListener` 中的 `onRefreshConversation` 接口来进行回调，对于关注多终端同步的用户，可以在这个接口中进行相关的同步处理。所以建议在登录之前，通过 `TIMUserConfig` 中的 `setRefreshListener` 接口来设置会话刷新监听。

**原型：**

```
/**
 * 设置数据刷新通知监听器
 * @param listener 数据刷新通知监听器
 */
public TIMUserConfig setRefreshListener(TIMRefreshListener listener)
```

### 消息撤回通知监听

IM SDK 3.1.0 开始提供了消息撤回功能。通过 `TIMUserConfig` 的 `setMessageRevokedListener` 可以设置消息撤回通知监听器。

**原型：**
```
/**
 * 设置消息撤回通知监听器
 * @param listener 消息撤回通知监听器
 * @since 3.1.0
 */
public TIMUserConfig setMessageRevokedListener(@NonNull TIMMessageRevokedListener listener)
```

## 新消息通知

在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调 `TIMMessageListener`，在用户登录的时候，会拉取 C2C 离线消息和最近联系人，为了不漏掉消息通知，建议在登录之前注册新消息通知。

>! 只要是本地没有的消息，IM SDK 都会通过注册的消息通知回调给上层应用。

以下为添加一个消息监听器的原型。默认情况下所有消息监听器都将按添加顺序被回调一次。除非用户在 `onNewMessages` 回调中返回 true，此时将不再继续回调下一个消息监听器。

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

**以下为收到新消息回调：**

```
/**
* 收到新消息回调
* @param msgs 收到的新消息
* @return 正常情况下，如果注册了多个listener, IM SDK会顺序回调到所有的listener。当碰到listener的回调返回true的时候，将终止继续回调后续的listener。
*/
public boolean onNewMessages(List<TIMMessage> msgs)
```

消息监听器被删除后，将不再被调用。**以下为删除一个消息监听器的原型：**

```
public void removeMessageListener(TIMMessageListener listener)
```

回调消息内容通过参数 `TIMMessage` 传递，通过 `TIMMessage` 可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等等，可参阅 [消息解析](https://cloud.tencent.com/doc/product/269/消息收发（Android%20SDK）#.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90) 部分。

**示例：**

```
//设置消息监听器，收到新消息时，通过此监听器回调
TIMManager.getInstance().addMessageListener(new TIMMessageListener() {//消息监听器
    @Override
    public boolean onNewMessages(List<TIMMessage> msgs) {//收到新消息
		//消息的内容解析请参考消息收发文档中的消息解析说明
		return true; //返回true将终止回调链，不再调用下一个新消息监听器
    }
});
```



