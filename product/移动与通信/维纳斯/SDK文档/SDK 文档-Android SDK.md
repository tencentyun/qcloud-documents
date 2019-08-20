
## 接口 WnsService
public interface WnsService

类说明：
WNS 客户端功能接口 
所有接口只能在使用 WNS 服务的 client 进程调用 
WNS 不支持多进程同时调用


### initAndStartWns
void initAndStartWns(Application app,
                   com.tencent.wns.client.inte.WnsAppInfo info)
接口说明：
初始化 App 信息并启动 wns 

参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| app | Application | 是 | 应用的 Application 类 |
| info | WnsAppInfo | 是 |Wns 应用的基本信息 |

WnsAppInfo类说明：

| 成员 | 类型 |说明|
|---------|---------|---------|
| appId | int | 应用的 id |
| appVersion | String |  应用版本 |
| channelId | String |  应用渠道号 |
| isQuickVerification | boolean | 设置快速验证模式，测速模式下，开发商自己的接口不用接入 wns 系统，wns sdk 会定时发模拟包到 wns 后台，这样开发商可以评估正式接入后的效果。 |
| debugIp | String | debug svr 设置 |


### sendRequest
int sendRequest(java.lang.String cmd,
              int timeout_ms,
              byte[] buff,
              com.tencent.wns.client.inte.IWnsCallback.WnsTransferCallback callback)
							
接口说明：

透传接口

参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| cmd | String | 是 | 命令字 |
| timeout_ms | int | 是 | 超时时间，单位 ms |
| buff | byte[] | 是 | 业务数据 |
| callback | WnsTransferCallback | 是 | 回调透传结果 |



```
public static interface WnsTransferCallback
{
     public abstract void onTransferFinished(IWnsTransferResult re);
}
```

TransferResult 

| 方法 | 返回类型 |说明|
|---------|---------|---------|
| getBizBuffer() | byte[] |  获取业务数据 |
| getWnsCode()  | int | 获取 wns 返回码 |
	

### cancelRequest

   void cancelRequest(int seqNo);

接口说明：
取消请求

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| app | int | 是 | returned from #sendRequest() |


### getWnsHttpClient
HttpClient getWnsHttpClient()

接口说明：
获取 WNS 的ＨttpClient 对象
i)支持 Http 协议透明接入 
i)对于 wns sdk 内部失败，错误提示语放在 reason phrase 字段 
i)自定义 header 请不要使用前缀“wns”,该前缀被预留给 wns sdk 使用


### getWnsHttpUrl

java.net.URL getWnsHttpUrl(java.lang.String url) throws java.net.MalformedURLException

接口说明：
支持 Http 协议透明接入 

返回:
可以使用 HttpURLConnection 库提供的功能


### setDebugIp
void setDebugIp(java.lang.String host, int port)

接口说明:
设置测试环境

参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| host | String | 是 | 测试环境 ip |
| port | int | 是 | 端口号 |

### bind

void bind(java.lang.String uid,
        com.tencent.wns.client.inte.IWnsCallback.WnsBindCallback callback)

接口说明:
第三方 app 登录绑定 uid

参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| uid | String | 是 | 业务用户的唯一标识 |
| callback | WnsBindCallback | 是 | bind 回调 |

  

```
 public static interface WnsBindCallback
 {
       public abstract void onBindFinished(BindResult re);
 }
```

BindResult

| 方法 | 返回类型 |说明|
|---------|---------|---------|
| getBizBuffer() | byte[] |  获取业务数据 |
| getWnsCode()  | int | 获取 wns 返回码 |

### unbind

void unbind(java.lang.String uid,
          com.tencent.wns.client.inte.IWnsCallback.WnsUnbindCallback callback)

接口说明:
与 #bind(String, String, String, int, WnsUnbindCallback)对应的登出方法

BindResult

| 方法 | 返回类型 |说明|
|---------|---------|---------|
| getBizBuffer() | byte[] |  获取业务数据 |
| getWnsCode()  | int | 获取 wns 返回码 |


```
 public static interface WnsBindCallback
 {
       public abstract void onBindFinished(BindResult re);
 }
```
 BindResult
 
| 方法 | 返回类型 |说明|
|---------|---------|---------|
| getBizBuffer() | byte[] |  获取业务数据 |
| getWnsCode()  | int | 获取 wns 返回码 |

### getStatus

java.lang.String getStatus()

接口说明:
获取 sdk 记录的关键步骤信息，便于理解和快速查看

### reset

void reset()

接口说明:
取消当前未完成的所有请求，比如切换帐号时可以调用

### getWid

long getWid()

接口说明:
获取 wid


### setBackgroundMode

void setBackgroundMode(boolean isBackground)

接口说明:
应用在切换前后台时通知 WNS 设置是否后台模式
WNS 启动默认是后台模式，所以该方法一定要使用
后台模式下 15 分钟后进入省电模式 ,省电模式下 WNS 会有一些措施：停止测速、减小心跳频率……

参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| isBackground | boolean | 是 | true 应用进入后台，false 应用进入前台 |

### reportDebugLog

void reportDebugLog(java.lang.String detail,
                  long time,
                  java.util.HashMap<java.lang.String,java.lang.String> externMap)

接口说明:
把 wns 的 log 上报到的服务器

参数:

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| detail | String | 是 | 简短的描述 |
| time | long | 是 | 日志开始时间,上报 time 向前 24h 的日志 |
| externMap | HashMap<String,String> | 是 | 上报 WNS debug 日志 日志上传的扩展 map |




### setStatusCallback
setStatusCallback
void setStatusCallback(WnsService.WnsSDKStatusListener listener)

接口说明：

设置 WNS 服务状态通知监听器

| 参数名 | 类型 | 必选|说明|
|---------|---------|---------|---------|
| listener | WnsSDKStatusListener | 是 | 监听回调 |

WNS 服务状态更新
```
static interface WnsSDKStatusListener
{
       void onWnsStateUpdate(WnsSDKStatus oldState, WnsSDKStatus newState);
}
```
    

枚举 WnsSDKStatus： WNS 服务状态

| 状态名 | 说明|
|---------|---------|
| Disconnected |   网络不可用 |
| Connecting |  网络连接建立中 |
| Connected |   网络连接建立成功 |



