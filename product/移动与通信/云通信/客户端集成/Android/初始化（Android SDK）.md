## 1 获取通讯管理器
ImSDK一切操作都是由通讯管理器`TIMManager`开始，SDK操作第一步需要获取`TIMManager`单例：
原型：

```
public static TIMManager getInstance()
```

获取通讯管理器实例

**返回：**
TIMManager实例

**示例：**

```
TIMManager.getInstance();
```


## 2 新消息通知

在多数情况下，用户需要感知新消息的通知，这时只需注册新消息通知回调 `TIMMessageListener`，在用户登录状态下，会拉取离线消息，为了不漏掉消息通知，需要在登录之前注册新消息通知。

**原型：**

```
public void addMessageListener(TIMMessageListener listener)
```

添加一个消息监听器，默认情况下所有消息监听器都将按添加顺序被回调一次 除非用户在`OnNewMessages`回调中返回true，此时将不再继续回调下一个消息监听器。


```
public boolean onNewMessages(java.util.Listmsgs)
```

收到新消息回调。


```
public void removeMessageListener(TIMMessageListener listener)
```

删除一个消息监听器，消息监听器被删除后，将不再被调用。

回调消息内容通过参数`TIMMessage`传递，通过`TIMMessage`可以获取消息和相关会话的详细信息，如消息文本，语音数据，图片等等，可参阅（[消息解析](/doc/product/269/消息收发（Android%20SDK）#2.1-.E6.B6.88.E6.81.AF.E8.A7.A3.E6.9E.90)）部分。

**示例：**


```
//设置消息监听器，收到新消息时，通过此监听器回调
TIMManager.getInstance().addMessageListener(new TIMMessageListener() {//消息监听器
 
    @Override
    public boolean onNewMessage(Listmsgs) {//收到新消息
		//消息的内容解析请参考 4.5 消息解析
		return true; //返回true将终止回调链，不再调用下一个新消息监听器
    }
});
```

## 3 网络事件通知

可选设置，如果要用户感知是否已经连接服务器，需要设置此回调，用于通知调用者跟通讯后台链接的连接和断开事件，另外，如果断开网络，等网络恢复后会自动重连，自动拉取消息通知用户，用户无需关心网络状态，仅作通知之用。注意：这里的网络事件不表示用户本地网络状态，仅指明SDK是否与IM云Server连接状态。只要用户处于登录状态，**ImSDK内部会进行断网重连，用户无需关心**。

**原型：**

```
public void setConnectionListener(TIMConnListener listener)
```

设置连接监听器。

**示例：**


```
//设置网络连接监听器，连接建立／断开时回调
TIMManager.getInstance().setConnectionListener(new TIMConnListener() {//连接监听器
    @Override
    public void onConnected() {//连接建立
        Log.e(tag, "connected");
    }
 
    @Override
    public void onDisconnected(int code, String desc) {//连接断开
        //接口返回了错误码code和错误描述desc，可用于定位连接断开原因
        //错误码code含义请参见错误码表
        Log.e(tag, "disconnected");
    }
});
```
## 4 日志事件

SDK内部会进行打印日志，如果调用方有自己统一的日志收集方式，可以设置日志回调事件，把日志通过回调返给调用方，但ImSDK仍然内部仍然会打印，如果需要禁掉，可以通过设置控制台不打印日志，或者设置日志级别。

**原型：**

```
public void setLogListener(TIMLogListener listener)
```

设置日志监听器。

**示例：**


```
//设置日志回调，sdk输出的日志将通过此接口回传一份副本
//[NOTE] 请注意level定义在TIMManager中，如TIMManager.ERROR等， 并不同于Android系统定义
TIMManager.getInstance().setLogListener(new TIMLogListener() {
    @Override
    public void log(int level, String tag, String msg) {
        //可以通过此回调将sdk的log输出到自己的日志系统中
    }
});
```
## 5 用户状态变更

用户状态变更的时候，SDK会有相应的通知。通过`TIMManager`中的`setUserStatusListener`方法可以设置用户状态变更通知监听器来对相应的通知进行监听。目前用户状态变更有两种通知，具体可参见 [用户被踢下线通知](#5.1-.E7.94.A8.E6.88.B7.E8.A2.AB.E8.B8.A2.E4.B8.8B.E7.BA.BF.E9.80.9A.E7.9F.A5) 和 [用户票据过期通知](#5.2-.E7.94.A8.E6.88.B7.E7.A5.A8.E6.8D.AE.E8.BF.87.E6.9C.9F.E9.80.9A.E7.9F.A5)。

**原型：**

```
public void setUserStatusListener(TIMUserStatusListener userStatusListener)
```

设置用户状态变更通知监听器。

**参数：**

参数|说明
---|---
userStatusListener|用户状态变更通知监听器

用户状态变更通知监听器`TIMUserStatusListener`的定义如下：

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

### 5.1 用户被踢下线通知

用户如果在其他终端登录，会被踢下线，这时会收到用户被踢下线的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#5-.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onForceOffline` 中进行相应的处理，出现这种情况常规的做法是提示用户进行操作（退出，或者再次把对方踢下线）。



>注意：
用户如果在离线状态下被踢，下次登录将会失败，可以给用户一个非常强的提醒（登录错误码ERR_IMSDK_KICKED_BY_OTHERS：6208），开发者也可以选择忽略这次错误，再次登录即可。

用户在线情况下的互踢情况如下图所示：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021645_19906.png)

图示中，用户在设备1登录，保持在线状态下，该用户又在设备2登录，这时用户会在设备1上强制下线，收到onForceOffline回调。用户在设备1上收到回调后，提示用户，可继续调用login上线，强制设备2下线。这里是在线情况下互踢过程。
用户离线状态互踢如下图所示：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151015021702_68733.png)

用户在设备1登录，没有进行logout情况下进程退出（此时可接收iOS远程推送消息）。该用户在设备2登录，此时由于用户不在线，无法感知此事件，为了显式提醒用户，避免无感知的互踢，用户在设备1重新登录时，会返回（ERR_IMSDK_KICKED_BY_OTHERS：6208）错误码，表明之前被踢，是否需要把对方踢下线。如果需要，则再次调用login强制上线，设备2的登录的实例将会收到onForceOffline回调。

### 5.2 用户票据过期通知

在用户登录（参见 [登录](/doc/product/269/%E7%99%BB%E5%BD%95%EF%BC%88Android%20SDK%EF%BC%89#1-.E7.99.BB.E5.BD.95)）的时候，需要提供一个用户票据，而这个用户票据在生成的时候是有一个有效使用期限的。在正常使用过程中，如果超过了用户票据的使用期限时，SDK与服务器的交互会因为票据验证失败而操作失败，这个时候SDK会给出用户票据过期的通知。如果设置了用户状态变更通知监听器（参见 [用户状态变更](#5-.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4)），则可以在监听器的回调方法 `onUserSigExpired` 中进行相应的处理，出现这种情况，如果仍需要继续与服务器进行交互，则需要更换票据后重新登录。


## 6 Crash上报

ImSDK内部集成了[Bugly系统](http://bugly.qq.com)，当应用crash后，会自动上报到平台，用户可以根据Bugly文档指示上传符号表，显示crash详细信息，如果用户有自己的上报组件，可调用`disableCrashReport`接口禁用上报。

**原型：**

```
public void disableCrashReport()
```

禁用crash上报，由用户自己上报，如果需要，必须在init Sdk之前调用。

**示例：**

```
//禁用crash上报
TIMManager.getInstance().disableCrashReport();
```

## 7 设置日志级别

在权限允许的情况下，ImSDK的日志默认会写到日志文件中。通过`setLogLevel`修改ImSDK内部日志级别，可以控制ImSDK的文件日志输出。

**原型：**

```
public void setLogLevel(TIMLogLevel level)
```

设置写日志等级， 必须在sdk初始化之前调用，在sdk初始化之后设置无效。

**参数：**

level - 日志等级。

可以通过设置日志级别为`TIMLogLevel.OFF`来关闭ImSDK的文件日志输出，提升性能，建议在开发期间打开日志，方便排查问题。


## 8 控制台不打印日志或修改日志路径

默认ImSDK日志会打印到控制台，如果调试期间干扰太多，可选择关闭控制台日志（此时文件日志仍然会打印，可设置日志级别禁用），另外也可以修改默认的存储路径，方便管理。

**原型：**
```
public void initLogSettings(boolean isEnableLogPrint, String logPath)
```
初始化日志设置， 必须在sdk初始化之前调用，在sdk初始化之后设置无效。

**参数：**
isEnableLogPrint - 是否开启日志控制台打印。true - 开启， false - 关闭。
logPath - ImSDK日志文件存储路径，传入null时将使用默认路径（*SD卡下，/tencent/imsdklogs/(your app package name)/*）。

如果不关心ImSDK日志路径，可以通过`setLogPrintEnable`来设置是否开启控制台日志打印。

**原型：**
```
public void setLogPrintEnable(boolean isEnable)
```
设置是否开启控制台log输出。

**参数：**
isEnable - 是否开启控制台log输出：true开启，false关闭，默认开启。

## 9 禁用存储
默认情况ImSDK会进行消息的存储，如无需存储，可选择关闭存储来提升处理性能。

**原型：**
```
public void disableStorage()
```
禁用存储，在不需要消息存储的场景可以禁用存储，提升效率。**需要在初始化之后登录之前调用。**

## 10 通讯管理器初始化

在使用SDK进一步操作之前，需要初始化SDK。**在存在多进程的情况下，请只在一个进程进行SDK初始化。**

**原型：**

```
public void init(Context context)
```

初始化，参数为应用的context。

**示例：**

```
TIMManager.getInstance().init(context);
```
