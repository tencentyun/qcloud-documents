## 操作场景
vivo 通道是由 vivo 官方提供的系统级推送通道。在 vivo 手机上，推送消息能够通过 vivo 的系统通道抵达终端，并且无需打开应用，即可收到推送，更多详情请参见 [vivo 推送官网](https://dev.vivo.com.cn/home)。

>?
> - 如遇到 debug 版本点击通知后无法拉起 App，请在权限设置中找到后台弹出界面，并开启当前应用的权限开关。
> - vivo 通道暂不支持应用内消息，此类型的消息将通过 TPNS 通道下发。
> - vivo 通道对应用的每日推送量有额度限制，详情请参见 [厂商通道限额说明](https://cloud.tencent.com/document/product/548/43794)，超过限制部分将走 TPNS 通道进行补推发送。
> - vivo 通道7:00 - 23:00允许推送消息，其他时间只能推送系统消息，系统消息申请详情请参见 [vivo 系统消息申请指南](https://cloud.tencent.com/document/product/548/44531#vivozhinan)。
> - vivo 通道单应用单用户每天接收运营消息条数上限为5条，系统消息不限接收条数。
> - vivo 通道仅支持部分较新的机型和对应的系统及以上系统，详情请参见 [vivo 推送常见问题汇总](https://dev.vivo.com.cn/documentCenter/doc/156#w1-08608733)。
> 

## 操作步骤

### 获取密钥
1. 开发者需向 vivo 申请开通推送权限，获取到 AppID 、AppKey、AppSecret 三个密钥参数。详情请参见 [快速接入指引](https://dev.vivo.com.cn/documentCenter/doc/180)。
>? 开发者的应用必须要在 vivo 开放平台通过审核上架后，才会通过消息推送服务审核。
>
2. 复制应用的 AppId、AppKey 和 AppSecret 参数填入 【[移动推送 TPNS 控制台](https://console.cloud.tencent.com/tpns)】>【配置管理】>【基础配置】>【vivo 官方推送通道】栏目中。

###  配置内容
#### AndroidStudio 集成方法

在 App 模块下的 build.gradle 文件内，完成移动推送 TPNS 所需的配置后，再增加以下节点：
1. 配置 vivo 的 AppID 和 AppKey。示例代码如下：
```xml
 manifestPlaceholders = [
	 VIVO_APPID:"xxxx",
     VIVO_APPKEY:"xxxxx",
        ]
```
2. 导入 vivo 推送相关依赖。示例代码如下：
```js
implementation 'com.tencent.tpns:vivo:[VERSION]-release' // vivo  推送 [VERSION] 为当前 SDK 版本号,版本号可在 Android SDK 发布动态查看
```

>? vivo 推送 [VERSION] 为当前 SDK 版本号，版本号可在 [Android SDK 发布动态](https://cloud.tencent.com/document/product/548/44520) 查看。
>


#### Eclipes 集成方法
获取移动推送 TPNS  vivo 通道 SDK 包后，按照移动推送 TPNS 官网手动集成方法，在配置好移动推送 TPNS 主版本的基础下，进行以下设置：

1. 下载 [SDK 安装包](https://console.cloud.tencent.com/tpns/sdkdownload)。
2. 打开 Other-Push-jar 文件夹， 导入 vivo 推送相关 jar 包。
2. 在 `Androidmanifest.xml` 文件中，新增如下配置：
```xml
  <application>
	<service
            android:name="com.vivo.push.sdk.service.CommandClientService"
            android:exported="true" />

        <activity
            android:name="com.vivo.push.sdk.LinkProxyClientActivity"
            android:exported="false"
            android:screenOrientation="portrait"
            android:theme="@android:style/Theme.Translucent.NoTitleBar" />

        <!-- push应用定义消息receiver声明 -->
        <receiver android:name="com.tencent.android.vivopush.VivoPushMessageReceiver" >
            <intent-filter>

                <!-- 接收push消息 -->
                <action android:name="com.vivo.pushclient.action.RECEIVE" />
            </intent-filter>
        </receiver>

        <meta-data
            android:name="com.vivo.push.api_key"
            android:value="vivo的appkey" />
        <meta-data
            android:name="com.vivo.push.app_id"
            android:value="vivo的appid" />

</application>
```


### 开启 vivo 推送
在调用移动推送 TPNS  `XGPushManager.registerPush` 之前，开启第三方推送接口：
```java
//打开第三方推送
XGPushConfig.enableOtherPush(getApplicationContext(), true);


//注册成功的日志如下
I/TPush: [OtherPushClient] handleUpdateToken other push token is : 160612459******08955218 other push type: vivo
I/TPush: [PushServiceBroadcastHandler] >> bind OtherPushToken success ack with [accId = 150000****  , rsp = 0]  token = 01a22fb503a33******66b89fad6be3ed343 otherPushType = vivo otherPushToken = 160612459******08955218

```

### 代码混淆

```xml
-dontwarn com.vivo.push.**
-keep class com.vivo.push.**{*; }
-keep class com.vivo.vms.**{*; }
-keep class com.tencent.android.vivopush.VivoPushMessageReceiver{*;}
```

>? 混淆规则需要放在 App 项目级别的 proguard-rules.pro 文件中。
>


## 常见问题排查

### vivo 推送注册错误码查询方法

若观察到如下类似日志则说明 vivo 厂商通道注册失败，开发者可以通过以下方式获取 vivo 推送注册错误码：
```
[OtherPushClient] handleUpdateToken other push token is :  other push type: vivo
```

推送服务 debug 模式下，过滤关键字 “OtherPush”，查看相关返回码日志（例如 `[OtherPushVivoImpl] vivoPush Register or UnRegister fail, code = 10003`），并前往 [厂商通道注册失败排查指南](https://cloud.tencent.com/document/product/548/45659) 查找对应原因，获取解决办法。

### 推送 vivo 响应失败 code:10045，是什么原因？

应用审核中不可发送正式消息，请前往 vivo 平台确认推送权限审核进度。
