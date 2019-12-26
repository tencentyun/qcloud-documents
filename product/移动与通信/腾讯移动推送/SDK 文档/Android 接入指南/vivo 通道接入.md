
## 操作场景
vivo 通道是由 vivo 官方提供的系统级推送通道。在 vivo 手机上，推送消息能够通过 vivo 的系统通道抵达终端，并且无需打开应用，即可收到推送，更多详情请参见 [vivo 推送官网](https://dev.vivo.com.cn/home)。

>?
- 如遇到 debug 版本点击通知后无法拉起 App，请在权限设置中找到后台弹出界面，并开启当前应用的权限开关。
- vivo 通道暂不支持应用内消息，此类型的消息会以通知的形式展示。
- vivo 通道对应用的每日推送量（包含通知和透传消息）有一定的限制，限制量官方未给出明确说明，超过限制部分会走 TPNS 自建通道进行补推发送。

## 操作步骤
### 获取密钥
开发者需向 vivo 申请开通推送权限，获取到 AppID 、AppKey、AppSecret 三个密钥。详情请参见 [快速接入指引](https://dev.vivo.com.cn/documentCenter/doc/180)。

###  配置内容
#### AndroidStudio 集成方法

在 App 模块下的 build.gradle 文件内，完成腾讯移动推送所需的配置后，再增加以下节点：
1. 配置 vivo 的 AppID 和 AppKey。示例代码如下：
```xml
 manifestPlaceholders = [
	 VIVO_APPID:"xxxx",
     VIVO_APPKEY:"xxxxx",
        ]
```
2. 导入 vivo 推送相关依赖。示例代码如下：
```js
implementation 'com.tencent.tpns:vivo:[VERSION]-release' // vivo  推送 [VERSION] 为当前SDK版本号,版本号可在SDK下载页查看
```




#### Eclipes 集成方法
获取腾讯移动推送 vivo 通道 SDK 包后，按照腾讯移动推送官网手动集成方法，在配置好腾讯移动推送主版本的基础下，进行以下设置：

1. 导入 vivo 推送相关 jar 包，将 vivo4tpns1.1.2.1.jar 导入项目工程中。
2. 在 ```Androidmanifest.xml``` 文件中，新增如下配置：

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
在调用腾讯移动推送 ```XGPushManager.registerPush``` 之前，开启第三方推送接口：

```java
//打开第三方推送
XGPushConfig.enableOtherPush(getApplicationContext(), true);


//注册成功的日志如下
 I/XINGE: [XGOtherPush] other push token is : 15646472431991408944055  other push type: vivo
I/XINGE: [PushServiceBroadcastHandler]  bind OtherPushToken success ack with [accId = 1500xxxxxx  , rsp = 0]  token = 0139f9840030882cfe7cc791aebc800ed270 otherPushType = vivo otherPushToken = 15646472431991408944055

```


### 代码混淆

```xml
-dontwarn com.vivo.push.**
-keep class com.vivo.push.**{*; }
-keep class com.vivo.vms.**{*; }
-keep class com.tencent.android.vivopush.VivoPushMessageReceiver{*;}

```

>?混淆规则需要放在 App 项目级别的 proguard-rules.pro 文件中。
