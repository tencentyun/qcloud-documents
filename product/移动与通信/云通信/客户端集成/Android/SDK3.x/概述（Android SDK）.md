## ImSDK 集成

本节主要介绍如何创建一个应用，并集成 ImSDK。

>**注意：**
>使用互动直播业务的开发者，请集成 ImSDKv2 版本。

### 支持版本

ImSDK 支持 JDK 1.6 和 Android SDK version 14 以上系统。

### 下载 ImSDK

从 [官网](https://cloud.tencent.com/product/im/developer) 下载 ImSDK ，包含以下库文件：

```
libs
├── armeabi
│   ├── libBugly.so
│   ├── libgnustl_shared.so
│   ├── lib_imcore_group_ext_gyp.so
│   ├── lib_imcore_jni_gyp.so
│   ├── lib_imcore_msg_ext_gyp.so
│   ├── lib_imcore_sns_ext_gyp.so
│   ├── libqalcodecwrapper.so
│   ├── libqalmsfboot.so
│   └── libwtcrypto.so
├── armeabi-v7a
│   └──（此处省略，文件列表与armeabi相同）
├── arm64-v8a
│   └──（此处省略，文件列表与armeabi相同）
├── x86
│   └──（此处省略，文件列表与armeabi相同）
├── x86_64
│   └──（此处省略，文件列表与armeabi相同）
├── bugly_2.4.0_imsdk_release.jar
├── imsdk_group_ext.jar
├── imsdk.jar
├── imsdk_msg_ext.jar
├── imsdk_sns_ext.jar
├── mobilepb.jar
├── qalsdk.jar
├── soload.jar
├── tls_sdk.jar
└── wup-1.0.0-SNAPSHOT.jar

```

| 包名 | 描述 | 
|---------|---------|
| bugly_2.4.0_imsdk_release.jar | Bugly 包，crash 上报用, 如不需要可删除，并调用 TIMSdkConfig 中的 `enableCrashReport(false)` 进行禁用 |
| imsdk.jar | ImSDK 基础包，只提供消息、资料关系链管理、群组管理等的最基础功能 |
| imsdk_group_ext.jar | 群组管理扩展包，提供群组管理的高级功能 |
| imsdk_msg_ext.jar | 消息管理扩展包，提供消息管理的高级功能 |
| imsdk_sns_ext.jar | 资料关系链管理扩展包， 提供个人资料及关系链的高级功能 |
| mobilepb.jar | protobuffer 处理相关 jar 包 |
| qalsdk.jar | SDK 网络层 jar 包 |
| soload.jar | 提高 ImSDK so 库的加载成功率 |
| tls_sdk.jar | 帐号系统 jar 包 |
| wup-1.0.0-SNAPSHOT.jar | 无线统一协议 jar 包 |



### 创建应用
#### 加入 ImSDK 库
将以上步骤中下载得到的库文件复制到工程 `libs/` 文件夹下。

> **注意：**
> - 需要引用 ANDROID SDK API LEVEL 23+ 版本的 android-support-v4.jar。
> - 由于从 ANDROID SDK 从 API LEVEL 23 开始去掉了 HTTP 相关特性，所以在用 API LEVEL 23 以上 ANDROID SDK 版本进行编译时，需要增加对 `org.apache.http.legacy.jar` 的引用。具体参考 [Android 6.0 Changes](http://developer.android.com/intl/zh-cn/about/versions/marshmallow/android-6.0-changes.html)。

#### 添加相关权限

创建一个新工程，并在 `AndroidManifest.xml` 中添加以下权限：
> **注意：**
> Android 6.0 以上的机型，其中一些权限需要在应用中手动申请。可以参照 Demo 的写法。

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

#### 声明相关服务及广播接收器

在 `AndroidManifest.xml` 中添加以下配置：

```xml
<!-- Android 9.0兼容配置 -->
<uses-library android:name="org.apache.http.legacy" android:required="false"/>

<!-- 【必须】消息收发service -->
<service
	android:name="com.tencent.qalsdk.service.QalService"
	android:exported="true"
	android:process=":QALSERVICE" >
</service>
<service  
	android:name="com.tencent.qalsdk.service.QalAssistService"  
	android:exported="false"
	android:process=":QALSERVICE" >
</service>   

<!-- 【必须】 离线消息广播接收器 -->
<receiver
	android:name="com.tencent.qalsdk.QALBroadcastReceiver"
	android:exported="false">
	<intent-filter>
		<action android:name="com.tencent.qalsdk.broadcast.qal" />
	</intent-filter>
</receiver>
<receiver 
	android:name="com.tencent.qalsdk.core.NetConnInfoCenter" android:process=":QALSERVICE">
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
	
	<!-- ImSDK 3.0.2 后添加 -->
	<intent-filter>
		<action android:name="com.tencent.qalsdk.service.TASK_REMOVED" />
	</intent-filter>
</receiver>                
```


### 功能开发
在工程中根据以上说明引入库文件，依照后续章节的开发指引进行功能的开发。

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
**会话：**ImSDK 中会话(Conversation)分为两种，一种是 C2C 会话，表示单聊情况自己与对方建立的对话，读取消息和发送消息都是通过会话完成；另一种是群会话，表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。如下图所示，一个会话表示与一个好友的对话。
![](//mccdn.qcloud.com/static/img/6a12c1ea947e7b36a7abe25e55c33608/image.jpg)

**消息：**ImSDK 中消息(Message)表示要发送给对方的内容，消息包括若干属性，如是否自己已读，是否已经发送成功，发送人帐号，消息产生时间等；一条消息由若干 Elem 组合而成，每种 Elem 可以是文本、图片、表情等等，消息支持多种 Elem 组合发送。

![](//avc.qcloud.com/wiki2.0/im/imgs/20151012094526_95348.png)

**群组 ID：**群组 ID 唯一标识一个群，由后台生成，创建群组时返回。

### ImSDK 对象简介
ImSDK 对象主要分为通讯管理器，会话、消息，群管理，具体的含义参见下表：

| 对象 | 介绍 | 功能 |
| --- | --- | --- |
| TIMManager | 管理器类，负责 SDK 基本操作 | 初始化、登录、注销、创建会话等，可以通过扩展类 `TIMManagerExt` 使用更多管理器相关高级功能 |
| TIMConversation | 会话，负责会话相关操作 | 如发送消息，获取会话消息缓存，获取未读计数等，可以通过扩展类 `TIMConversationExt` 使用更多会话相关高级功能 |
| TIMMessage | 消息 | 包括文本、图片等不同类型消息。可以通过扩展类 `TIMMessageExt` 使用更多消息相关高级功能 | 
| TIMGroupManager | 群组管理器 | 负责创建群组、加群、退群等，可以通过扩展类 `TIMGroupManagerExt` 使用更多群组相关高级功能 |
| TIMFriendshipManager | 资料关系链管理器 | 负责资料获取、修改和关系链信息，可以通过扩展类 `TIMFriendshipManagerExt` 使用更多资料关系链管理相关高级功能 |
	
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
				<td rowspan="5">
					初始化<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMSdkConfig<br>
				</td>
				<td>
					设置 SDK 基本配置，比如 sdkappid、日志等级等<br>
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
					TIMManager : setUserConfig<br>
				</td>
				<td>
					设置用户基本配置<br>
				</td>
			</tr>
			<tr>
				<td>
					TIMManager  :  addMessageListener<br>
				</td>
				<td>
					设置消息监听<br>
				</td>
			</tr>
			<tr>
				<td rowspan="2">
					登录<br>
				</td>
			</tr>
			<tr>
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

## 从 ImSDK2.x 升级到 ImSDK3.x

### 包路径调整

ImSDK3.x 对包路径进行了调整，由原来的 `com.tencent` 调整为 `com.tencent.imsdk` 。例如，类 `TIMManager` 在2.x 版本时类路径为 `com.tencent.TIMManager`，而在 3.x 版本时类路径为 `com.tencent.imsdk.TIMManager`。

### 模块接口调整

ImSDK3.x 对模块的功能及类的接口进行了优化调整。为了让 ImSDK 更加的灵活轻便，在 3.x 的时候对 ImSDK 进行了模块功能调整。原来的 `imsdk.jar` 只保留了基本的功能，一些高级功能分离到了相应的扩展包中。调整后原来的 `imsdk.jar` 变成了如下几个包：

+ 基础功能包 —— `imsdk.jar`
+ 消息扩展包 —— `imsdk_msg_ext.jar`
+ 群组扩展包 —— `imsdk_group_ext.jar`
+ 资料关系链扩展包 —— `imsdk_sns_ext.jar`

同时，配合着模块功能的调整，接口也有相应的优化与调整。这里只列出名字变更或者移到其他类的接口，参数变更请参考下载好的 SDK 包中的 API Javadoc 文档。具体见下表：

2.x类|2.x接口|3.x类|3.x接口
---|---|---|---
**TIMManager**|configOfflinePushSettings|**TIMManager**|setOfflinePushSettings
**TIMManager**|disableCrashReport<br>setLogPrintEnable<br>setLogLevel<br>setLogListenCallbackLevel<br>setLogListener<br>setSoLibPath|**TIMSdkConfig**|enableCrashReport<br>enableLogPrint<br>setLogLevel<br>setLogCallbackLevel<br>setLogListener<br>setSoLibPath
**TIMManager**|setConnectionListener<br>initFriendshipSettings<br>setGroupEventListener<br>initGroupSettings<br>setRefreshListener<br>setUploadProgressListener<br>setUserStatusListener |**TIMUserConfig**|setConnectionListener<br>setFriendshipSettings<br>setGroupEventListener<br>setGroupSettings<br>setRefreshListener<br>setUploadProgressListener<br>setUserStatusListener
**TIMManager**|disableAutoReport<br>enableReadReceipt<br>disableRecentContact<br>disableRecentContactNotify<br>disableStorage<br>setMessageReceiptListener |**TIMUserConfigMsgExt**|enableAutoReport<br>enableReadReceipt<br>enableRecentContact<br>enableRecentContactNotify<br>enableStorage<br>setMessageReceiptListener
**TIMManager**|enableFriendshipStorage<br>setFriendshipProxyListener|**TIMUserConfigSnsExt**|enableFriendshipStorage<br>setFriendshipProxyListener
**TIMManager**|enableGroupInfoStorage<br>setGroupAssistantListener|**TIMUserConfigGroupExt**|enableGroupStorage<br>setGroupAssistantListener
**TIMManager**|initLogSettings<br>setGroupMemberUpdateListener<br>getConversationByIndex|**TIMManager**|已废弃
**TIMManager**|deleteConversation<br>deleteConversationAndLocalMsgs<br>getConversationCount<br>getConversationList<br>initStorage<br>sendMessageToMultiUsers |**TIMManagerExt**|deleteConversation<br>deleteConversationAndLocalMsgs<br>getConversationCount<br>getConversationList<br>initStorage<br>sendMessageToMultiUsers
**TIMConversation**|所有接口 |**TIMConversation**|仅保留以下接口，其他接口均由 TIMConversationExt 提供<br>getType<br>getPeer<br>sendMessage<br>sendOnlineMessage
**TIMMessage**|getCustomInt<br>getCustomStr<br>hasGap<br>isPeerReaded<br>isRead<br>remove<br>setCustomInt<br>setCustomStr<br>convertToImportedMsg<br>setSender<br>setTimestamp |**TIMMessageExt**|getCustomInt<br>getCustomStr<br>hasGap<br>isPeerReaded<br>isRead<br>remove<br>setCustomInt<br>setCustomStr<br>convertToImportedMsg<br>setSender<br>setTimestamp
**TIMFileElem**<br>**TIMImageElem**<br>**TIMSoundElem**|所有接口|**TIMFileElem**<br>**TIMImageElem**<br>**TIMSoundElem**|上传下载方式仅保留指定文件路径的方式，废弃 byte 数组方式
**TIMFriendshipManager**|所有接口|**TIMFriendshipManager**|仅保留以下接口，其他接口均由 TIMFriendshipManagerExt 提供<br>getSelfProfile<br>getUsersProfile
**TIMFriendshipManager**|setAllowType<br>setBirthday<br>setCustomInfo<br>setFaceUrl<br>setGender<br>setLanguage<br>setLocation<br>setNickName<br>setSelfSignature|**TIMFriendshipManager**|modifyProfile
**TIMFriendshipManager**|setFriendCustom<br>setFriendRemark|**TIMFriendshipManagerExt**|modifySnsProfile
**TIMFriendshipProxyListener**|所有接口|**TIMFriendshipProxyListener**|所有与好友分组相关回调及 OnProxyStatusChange 已废弃
**TIMGroupManager**|所有接口|**TIMGroupManager**|仅保留以下接口，其他接口均由 TIMGroupManagerExt 提供<br>applyJoinGroup<br>createGroup<br>deleteGroup<br>quitGroup
**TIMGroupManager**|modifyGroupAddOpt<br>modifyGroupCustomInfo<br>modifyGroupFaceUrl<br>modifyGroupIntroduction<br>modifyGroupName<br>modifyGroupNotification<br>modifyGroupSearchable<br>modifyGroupVisible|**TIMGroupManagerExt**|modifyGroupInfo
**TIMGroupManager**|modifyGroupMemberInfoSetCustomInfo<br>modifyGroupMemberInfoSetNameCard<br>modifyGroupMemberInfoSetRole<br>modifyGroupMemberInfoSetSilence<br>ModifyReceiveMessageOpt|**TIMGroupManagerExt**|modifyMemberInfo
