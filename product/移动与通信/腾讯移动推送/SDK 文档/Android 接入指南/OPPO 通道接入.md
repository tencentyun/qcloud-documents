## 操作场景
OPPO 通道是由 OPPO 官方提供的系统级推送通道。在 OPPO 手机上，推送消息能够通过 OPPO 的系统通道抵达终端，无需打开应用就能够收到推送。详情请参见 [OPPO 推送官网](https://push.oppo.com/)。

>?
> - OPPO 通道暂不支持应用内消息的发送，此类型的消息会通过 TPNS 通道进行下发。
> - OPPO 通道对应用的每日推送量有额度限制，详情请参见 [厂商通道限额说明](https://cloud.tencent.com/document/product/548/43794#oppo-.E5.B9.B3.E5.8F.B0.E9.99.90.E5.88.B6)，超过限制部分将走 TPNS 通道进行补推发送。
> - OPPO 通道需要 OPPO 手机系统 ColorOS V3.1 及以上支持。
> 

## 操作步骤
### 开通权限
使用 OPPO 企业开发者帐号，登录 [OPPO 开发平台](https://open.oppomobile.com/)，在**管理中心** > **应用服务平台** > **移动应用列表** > **选择应用** > **开发服务** > **推送服务** 中完成 OPPO PUSH 权限申请。
![](https://main.qcloudimg.com/raw/11f429ba46161b1cea16c233cebc5627.png)
>? 通知栏推送权限申请需要应用在 OPPO 软件商店上架才可通过，且主营业务不为借贷类的应用。
>

### 获取密钥

>? 仅开发者帐号（主帐号）可查看。
>

1. Opush 申请开通成功后，您可在 [**OPPO 推送平台**](https://push.oppo.com/) > **配置管理** > **应用配置页面**，查看 AppKey、AppSecret 和 MasterSecret。
![](https://main.qcloudimg.com/raw/7753e738a004854d63cf4c8e4c07d51c.png)
2. 复制应用的 AppKey、AppSecret 和 MasterSecret 参数填入 [**移动推送 TPNS 控制台**](https://console.cloud.tencent.com/tpns) > **配置管理** > **基础配置** >  **OPPO 官方推送通道** 栏目中。

### 配置推送通道
为兼容安卓8.0及以上版本的 OPPO 手机的通道配置，用户需在 OPPO 管理台上，创建一个 TPNS 推送的默认通道。详情请参见 [OPPO 官方文档](https://open.oppomobile.com/wiki/doc/#id=10198)。
具体内容为：
- “通道 ID”：“default_message”
- “通道名称”：“默认通知”


###  配置内容
#### AndroidStudio 集成方法

导入 OPPO 推送相关依赖。示例代码如下：
```js
implementation 'com.tencent.tpns:oppo:[VERSION]-release'//OPPO 推送 [VERSION] 为当前 SDK 版本号，版本号可在 Android SDK 发布动态查看
```
>? OPPO 推送 [VERSION] 为当前 SDK 版本号，版本号可在 [Android SDK 发布动态](https://console.cloud.tencent.com/tpns/sdkdownload) 查看。
>

#### Eclipes 集成方法

获取移动推送 TPNS  OPPO 通道 SDK 包后，按照移动推送 TPNS 官网手动集成方法，在配置好移动推送 TPNS 主版本的基础下，进行以下设置。

1. 打开 Other-push-jar 文件夹，将 OPPO 推送相关 jar 导入项目工程中。
2. 在主工程添加类资源文件，代码如下：
```java
package com.heytap.mcssdk;
class R {
    public static final class string {
        public static final int system_default_channel = 
	com.tencent.android.tpns.demo.R.string.oppo_system_default_channel;//可更改为自定义字符串资源ID
    }
}
```
3. 在 `Androidmanifest.xml` 文件中新增如下配置（二选一）：
 - TPNS Android SDK 1.2.0.2以前的版本使用以下配置：
```
<!--OPPO 推送服务必须权限-->
<uses-permission android:name="com.coloros.mcs.permission.RECIEVE_MCS_MESSAGE"/>
<uses-permission android:name="com.heytap.mcs.permission.RECIEVE_MCS_MESSAGE"/>
<application>
		<!--OPPO 推送服务必须组件-->
		<service
			android:name="com.heytap.mcssdk.PushService"
			android:permission="com.coloros.mcs.permission.SEND_MCS_MESSAGE">
			<intent-filter>
				<action android:name="com.coloros.mcs.action.RECEIVE_MCS_MESSAGE"/>
			</intent-filter>
		</service>
		<service
			android:name="com.heytap.mcssdk.AppPushService"
			android:permission="com.heytap.mcs.permission.SEND_MCS_MESSAGE">
			<intent-filter>
				<action android:name="com.heytap.mcs.action.RECEIVE_MCS_MESSAGE"/>
			</intent-filter>
		</service>
</application>
```
 - TPNS Android SDK 1.2.0.2以后的版本使用以下配置：
```
<!--OPPO 推送服务必须权限-->
<uses-permission android:name="com.coloros.mcs.permission.RECIEVE_MCS_MESSAGE"/>
<uses-permission android:name="com.heytap.mcs.permission.RECIEVE_MCS_MESSAGE"/>
<application>
		<!-- 以下为1.2.0.2 OPPO版本组件 -->
		<service
			android:name="com.heytap.msp.push.service.CompatibleDataMessageCallbackService"
			android:permission="com.coloros.mcs.permission.SEND_MCS_MESSAGE">
			<intent-filter>
				<action android:name="com.coloros.mcs.action.RECEIVE_MCS_MESSAGE"/>
			</intent-filter>
		</service>
		<service
			android:name="com.heytap.msp.push.service.DataMessageCallbackService"
			android:permission="com.heytap.mcs.permission.SEND_PUSH_MESSAGE">
			<intent-filter>
				<action android:name="com.heytap.mcs.action.RECEIVE_MCS_MESSAGE"/>
				<action android:name="com.heytap.msp.push.RECEIVE_MCS_MESSAGE"/>
			</intent-filter>
		</service>
</application>
```

### 开启 OPPO 推送

在调用移动推送 TPNS  `XGPushManager.registerPush`之前，调用以下代码：
```java
// 注意这里填入的是 Oppo 的 AppKey，不是AppId
XGPushConfig.setOppoPushAppId(getApplicationContext(), "Oppo的AppKey");
// 注意这里填入的是 Oppo 的 AppSecret，不是 AppKey
XGPushConfig.setOppoPushAppKey(getApplicationContext(), "Oppo的AppSecret");
//打开第三方推送
XGPushConfig.enableOtherPush(getApplicationContext(), true);

//注册成功的日志如下
I/TPush: [RegisterReservedInfo] Reservert info: other push token is : CN_fc0f0b38220cba7a1bcbda20857e021b  other push type: oppo
I/TPush: [PushServiceBroadcastHandler] >> bind OtherPushToken success ack with [accId = 150000****  , rsp = 0]  token = 007a4105425********52ac1e1360c6780f3 otherPushType = oppo otherPushToken = CN_fc0f0b3822****7a1bcbda20857e021b

```


### 代码混淆

```xml
-keep public class * extends android.app.Service
-keep class com.heytap.mcssdk.** {*;}
-keep class com.heytap.msp.push.** { *;}
```

>? 混淆规则需要放在 App 项目级别的 proguard-rules.pro 文件中。
>

## 常见问题排查

### OPPO 推送注册错误码查询方法

若观察到如下类似日志则说明 OPPO 厂商通道注册失败，开发者可以通过以下方式获取 OPPO 推送注册错误码：
```
[OtherPushClient] handleUpdateToken other push token is :  other push type: OPPO
```

推送服务 debug 模式下，过滤关键字 “OtherPush”，查看相关返回码日志（例如 `[OtherPushOppoImpl] OppoPush Register failed, code=14, msg=INVALID_APP_KEY`），并前往 [厂商通道注册失败排查指南](https://cloud.tencent.com/document/product/548/45659) 查找对应原因，获取解决办法。

### 推送 OPPO 响应失败 code:30，是什么原因？

应用审核中不可发送正式消息，请前往 OPPO 平台确认推送权限审核进度。
