## ImSDK 集成
本节主要介绍如何创建一个应用，并集成 ImSDK。
### 支持版本
ImSDK 支持 JDK 1.6 和 Android SDK version 14 以上系统。

### 下载 ImSDK

ImSDK 下载地址： [ImSDK](https://cloud.tencent.com/product/im/developer)，包含以下库文件：

```
libs/bugly_1.3.0_imsdk_release.jar
libs/imsdk.jar
libs/mobilepb.jar
libs/qalsdk.jar
libs/tls_sdk.jar
libs/wup-1.0.0-SNAPSHOT.jar
libs/soload.jar
libs/armeabi/lib_imcore_jni_gyp.so
libs/armeabi/libBugly.so
libs/armeabi/libqalcodecwrapper.so
libs/armeabi/libqalmsfboot.so
libs/armeabi/libwtcrypto.so
libs/armeabi-v7a/lib_imcore_jni_gyp.so
libs/armeabi-v7a/libBugly.so
libs/armeabi-v7a/libqalcodecwrapper.so
libs/armeabi-v7a/libqalmsfboot.so
libs/armeabi-v7a/libwtcrypto.so
libs/arm64-v8a/lib_imcore_jni_gyp.so
libs/arm64-v8a/libBugly.so
libs/arm64-v8a/libqalcodecwrapper.so
libs/arm64-v8a/libqalmsfboot.so
libs/arm64-v8a/libwtcrypto.so
libs/x86/lib_imcore_jni_gyp.so
libs/x86/libBugly.so
libs/x86/libqalcodecwrapper.so
libs/x86/libqalmsfboot.so
libs/x86/libwtcrypto.so
libs/x86_64/lib_imcore_jni_gyp.so
libs/x86_64/libBugly.so
libs/x86_64/libqalcodecwrapper.so
libs/x86_64/libqalmsfboot.so
libs/x86_64/libwtcrypto.so
```

| 包名 | 描述 | 
|---------|---------|
| bugly_1.3.0_imsdk_release.jar | crash 上报 JAR 包, 如不需要可删除，并调用 TIMManager 中的 disableCrashReport 进行禁用 |
| imsdk.jar | IMSDK 的 JAR 包 |
| mobilepb.jar | protobuffer 处理相关 JAR 包 |
| qalsdk.jar | SDK 网络层 JAR 包 |
| tls_sdk.jar | 帐号系统 JAR 包 |
| wup-1.0.0-SNAPSHOT.jar | 无线统一协议 JAR 包 |
| soload.jar | 提高 ImSDK so 库的加载成功率 |



### 创建应用

**创建一个新工程，并在 `AndroidManifest.xml` 中添加以下权限：**
```xml
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.READ_LOGS" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

**1.8.0 及以上版本需要在 `AndroidManifest.xml` 的 `<application></application>` 中添加以下配置：**

```xml
<!-- Android 9.0兼容配置 -->
<uses-library android:name="org.apache.http.legacy" android:required="false"/>

<!--  消息收发 service -->
<service
	android:name="com.tencent.qalsdk.service.QalService"
	android:exported="false" 
	android:process=":QALSERVICE" >  
</service> 
<!--  消息收发辅助 service -->
<service  
	android:name="com.tencent.qalsdk.service.QalAssistService"  
	android:exported="false"
	android:process=":QALSERVICE" >
 </service> 
<!--  离线消息广播接收器 -->
<receiver
	android:name="com.tencent.qalsdk.QALBroadcastReceiver"
	android:exported="false">
	<intent-filter>
		<action android:name="com.tencent.qalsdk.broadcast.qal" />
	</intent-filter>
</receiver>
<!--  系统消息广播接收器 -->
<receiver 
	android:name="com.tencent.qalsdk.core.NetConnInfoCenter"  android:process=":QALSERVICE">  
	<intent-filter>
		<action android:name="android.intent.action.BOOT_COMPLETED" />
	</intent-filter>
	<intent-filter>
		<action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
	</intent-filter>
	<intent-filter>
		<action android:name="android.intent.action.TIME_SET" />
	</intent-filter>
	<intent-filter>
		<action android:name="android.intent.action.TIMEZONE_CHANGED" />
	</intent-filter>
</receiver>
```

### 集成 ImSDK

将上述下载得到的 [ImSDK](https://cloud.tencent.com/product/im.html#sdk) 库文件复制到工程 `libs/` 文件夹下。

>注：
>- 集成 ImSDK 1.9.0 以上的版本时，需要引用 Android SDK API LEVEL 23+ 版本的 android-support-v4.jar。
>- 由于从 Android SDK 从 API LEVEL 23 开始去掉了 HTTP 相关特性，所以在用 API LEVEL 23 以上 Android SDK 版本进行编译时，需要增加对 `org.apache.http.legacy.jar` 的引用。具体参考 [Android 6.0 Changes](http://developer.android.com/intl/zh-cn/about/versions/marshmallow/android-6.0-changes.html)。
>- 因为 Android 9.0 彻底废弃了 `org.apache.http.legacy.jar`，但ImSDK又依赖于这个库，所以需要在manifest的`application`节点中增加以下配置：\<uses-library android:name="org.apache.http.legacy" android:required="false"/\>


### 功能开发

在工程中引入上述提及的 [ImSDK](https://cloud.tencent.com/product/im.html#sdk) 库文件，根据后续章节的开发指引进行功能的开发。其中函数调用顺序可参见 [调用顺序介绍](#.E8.B0.83.E7.94.A8.E9.A1.BA.E5.BA.8F.E4.BB.8B.E7.BB.8D)。

### 代码混淆规则

如果您的项目中使用 proguard 等工具做了代码混淆，请保留以下选项。

```
-keep class com.tencent.**{*;}
-dontwarn com.tencent.**

-keep class tencent.**{*;}
-dontwarn tencent.**

-keep class qalsdk.**{*;}
-dontwarn qalsdk.**
```

## ImSDK 基本概念

ImSDK 中会话（Conversation）分为两种：

- **C2C 会话：**表示单聊情况下自己与对方建立的对话，读取消息和发送消息都是通过会话完成。
- **群会话：**表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。

如下图所示，一个会话表示与一个好友的对话。
![](//mccdn.qcloud.com/static/img/6a12c1ea947e7b36a7abe25e55c33608/image.jpg)

**消息：**ImSDK 中消息（Message）表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等。一条消息由若干 `Elem` 组合而成，每种 `Elem` 可以是文本、图片、表情等，消息支持多种 `Elem` 组合发送。

![](//avc.qcloud.com/wiki2.0/im/imgs/20151012094526_95348.png)

**群组 ID：**群组 ID 唯一标识一个群，由后台生成，创建群组时返回。

### ImSDK 对象简介

ImSDK 对象主要分为通讯管理器，会话、消息，群管理，具体的含义参见下表。

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="text-align:center;">
					对象<br>
				</td>
				<td style="text-align:center;">
					介绍<br>
				</td>
				<td style="text-align:center;">
					功能<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager<br>
				</td>
				<td>
					管理器类，负责基本的 SDK 操作<br>
				</td>
				<td>
					初始化登录、注销、创建会话等<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMConversation<br>
				</td>
				<td>
					会话，负责会话相关操作<br>
				</td>
				<td>
					如发送消息，获取会话消息缓存，获取未读计数等<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMMessage<br>
				</td>
				<td>
					消息<br>
				</td>
				<td>
					包括文本、图片等不同类型消息<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMGroupManager <br>
				</td>
				<td>
					群管理器<br>
				</td>
				<td>
					负责创建群，增删成员，以及修改群资料等<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMFriendshipManager<br>
				</td>
				<td>
					资料关系链管理<br>
				</td>
				<td>
					负责获取、修改好友资料和关系链信息<br>
				</td>
			</tr>
		</tbody>
	</table>
	
	
### 调用顺序介绍

ImSDK 调用 API 需要遵循以下顺序，其余辅助方法需要在登录成功后调用。

<table style="width:100%;">
		<tbody>
			<tr>
				<td style="text-align:center;">
					步骤<br>
				</td>
				<td style="text-align:center;">
					对应函数<br>
				</td>
				<td style="text-align:center;">
					说明<br>
				</td>
			</tr>
			<tr>
				<td rowspan="4">
					初始化<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager : setMessageListener<br>
				</td>
				<td>
					设置消息回调<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager : setConnListener<br>
				</td>
				<td>
					设置链接通知回调<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager : init<br>
				</td>
				<td>
					初始化 SDK<br>
				</td>
			</tr>
			<tr>
				<td>
					登录<br>
				</td>
				<td>
					TIMManager : login<br>
				</td>
				<td>
					登录<br>
				</td>
			</tr>
			<tr>
				<td rowspan="2">
					消息收发<br>
				</td>
				<td>
					TIMManager : getConversation<br>
				</td>
				<td>
					获取会话<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMConversation : sendMessage<br>
				</td>
				<td>
					发送消息<br>
				</td>
			</tr>
			<tr>
				<td>
					群组管理<br>
				</td>
				<td>
					TIMGroupManager<br>
				</td>
				<td>
					群组管理<br>
				</td>
			</tr>
			<tr>
				<td>
					资料关系链<br>
				</td>
				<td>
					TIMFriendshipManager<br>
				</td>
				<td>
					资料关系链管理<br>
				</td>
			</tr>
			<tr>
				<td>
					注销<br>
				</td>
				<td>
					TIMManager : logout<br>
				</td>
				<td>
					注销<br>
				</td>
			</tr>
		</tbody>
	</table>
	
