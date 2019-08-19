

## 操作场景
OPPO 通道是由 OPPO 官方提供的系统级推送通道。在 OPPO 手机上，推送消息能够通过 OPPO 的系统通道抵达终端，并且无需打开应用就能够收到推送，而且在 Color OS 3.1 手机上，App 只要注册 OPPO 推送，即可自动打开通知接收权限，否则默认是关闭的，需要用户手动设置开启。详情请参见 [OPPO 推送官网](https://push.oppo.com/)。

## 操作步骤
### 获取密钥
开发者需向 OPPO 申请开通推送权限，获取到 AppKey、AppSecret、master secret 三个密钥。详情请参见 [快速接入指引](https://open.oppomobile.com/wiki/doc#id=1019 )。


###  配置内容
#### AndroidStudio 集成方法

1. 在 App 模块下的 build.gradle 文件内，完成腾讯移动推送所需要的配置后，再增加以下节点：
2. 导入 OPPO 推送相关依赖。示例代码如下：
```js
/* Oppo 1.0.9.0版
 */
implementation 'com.tencent.tpns:oppo:1.1.0.0-release'//oppo推送
```




#### Eclipes 集成方法
获取腾讯移动推送 OPPO 通道 SDK 包后，按照腾讯移动推送官网手动集成方法，在配置好腾讯移动推送主版本的基础下，进行以下设置。

1. 导入 OPPO 推送相关 jar 包 ，将```com.coloros.mcssdk.jar```放在```libs```文件夹里。
2. 在 ```Androidmanifest.xml``` 文件中新增如下配置：

```xml
<uses-permission android:name="com.coloros.mcs.permission.RECIEVE_MCS_MESSAGE"/>

<application>
	<!--
	如果应用需要解析和处理Push消息（如透传消息），则继承PushService来处理，并在此申明
	如果不需要处理Push消息，则直接申明PsuhService即可
	 -->
	<service
		android:name="
com.tencent.android.oppopush.PushMessageService"
		android:permission="com.coloros.mcs.permission.SEND_MCS_MESSAGE">
		<intent-filter>
			<action android:name="com.coloros.mcs.action.RECEIVE_MCS_MESSAGE"/>
		</intent-filter>
	</service>

</application>
```


### 开启 OPPO 推送
在调用腾讯移动推送 ```XGPushManager.registerPush``` 之前，调用以下代码：

```java
XGPushConfig.setOppoPushAppId(getApplicationContext(), "Oppo的AppKey"); // 注意这里填入的是Oppo的AppKey
XGPushConfig.setOppoPushAppKey(getApplicationContext(), "Oppo的APP_SECRET"); // 注意这里填入的是Oppo的APP_SECRET，不是AppKey
// 打开
//打开第三方推送
XGPushConfig.enableOtherPush(getApplicationContext(), true);


//注册成功的日志如下
 I/XINGE: [XGOtherPush] other push token is : CN_93394e648ee5a73f5c5a0835b2a7e3d5  other push type: oppo
 I/XINGE: [h] >> bind OtherPushToken success ack with [accId = 1500xxxxxx  , rsp = 0]  token = 0114d716bfe01d75f861d05a920cca8c8226 otherPushType = oppo otherPushToken = CN_93394e648ee5a73f5c5a0835b2a7e3d5
 
```


### 代码混淆
```xml
-keep public class * extends android.app.Service
-keep class com.coloros.mcssdk.**  {*;}
```


