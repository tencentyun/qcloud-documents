# 应用云 Messaging 服务 Android 集成指南

## 准备工作

在开始使用应用云 Messaging 服务前，确保您已经完成：

 1. [安装和配置SDK](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/_Drafts/ApplicationBoard/%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Core/Android/GettingStarted.md)

## 添加 SDK

如果希望将 Messaging 库集成至自己的某个项目中，可以通过 gradle 远程依赖或者 jar 包两种方式集成。

### 通过gradle远程依赖集成

如果您使用 Android Studio 作为开发工具或者使用 gradle 编译系统，**我们推荐您使用此方式集成依赖。**

#### 1. 使用jcenter作为仓库来源

在工程根目录下的 build.gradle 使用 jcenter 作为远程仓库：

```
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        ...
    }
}

allprojects {
    repositories {
         jcenter()
    }
}
```

#### 2. 添加 Crash 库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加 Messaging 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-messaging:1.0.0'
}
```

然后，点击您 IDE 的 gradle 同步按钮，会自动将依赖包同步到本地。

### 手动集成

如果您使用 Eclipse 作为开发工具并且使用 Ant 编译系统，您可以通过以下方式手动集成。

#### 1. 下载服务资源压缩包

下载请点击[应用云 Messaging 服务资源]()，并解压。

#### 2. 集成jar包

1. 将资源文件中的 libs 目录下的文件拷贝到您工程的 libs 目录。
2. 将解压后的 jniLibs 目录拷贝到您工程您工程的 libs 目录。

#### 3. 修改您工程的 AndroidManifest.xml 文件

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件

```
<!-- 所需权限   -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.VIBRATE" />
<uses-permission android:name="android.permission.RECEIVE_USER_PRESENT" />
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_SETTINGS" />

<application
  <!-- 消息receiver广播接收 -->
  <receiver android:name="com.tencent.android.tpush.XGPushReceiver"
   	android:process=":xg_service_v3" >
  	<intent-filter android:priority="0x7fffffff" >
  	
      	<action android:name="com.tencent.android.tpush.action.SDK" />
      	<action android:name="com.tencent.android.tpush.action.INTERNAL_PUSH_MESSAGE" />
      	
      	<action android:name="android.intent.action.USER_PRESENT" />
     	<action android:name="android.net.conn.CONNECTIVITY_CHANGE" />
     	<action android:name="android.bluetooth.adapter.action.STATE_CHANGED" />
      	<action android:name="android.intent.action.ACTION_POWER_CONNECTED" />
      	<action android:name="android.intent.action.ACTION_POWER_DISCONNECTED" />
  	</intent-filter>
  </receiver>

  <!-- Messaging receiver，用于接收消息透传和操作结果的回调 -->
  <receiver android:name="com.tencent.tac.messaging.TACMessagingXGReceiver"
      android:exported="true" >
      <intent-filter>
          <!-- 接收消息透传 -->
          <action android:name="com.tencent.android.tpush.action.PUSH_MESSAGE" />
          <!-- 监听注册、反注册、设置/删除标签、通知被点击等处理结果 -->
          <action android:name="com.tencent.android.tpush.action.FEEDBACK" />
      </intent-filter>
  </receiver>

   <!-- 接受通知的activity -->
   <activity
            android:name="com.tencent.android.tpush.XGPushActivity"
            android:exported="false"
            android:theme="@android:style/Theme.Translucent" >
            <intent-filter>	
                <action android:name="android.intent.action" />
            </intent-filter>
   </activity>

   <service
       android:name="com.tencent.android.tpush.service.XGPushServiceV3"
       android:exported="true"
       android:persistent="true"
       android:process=":xg_service_v3" />


  <service
      android:name="com.tencent.android.tpush.rpc.XGRemoteService"
      android:exported="true">
      <intent-filter>
          <action android:name="您的应用包名.PUSH_ACTION" />
      </intent-filter>
   </service>


  <provider
       android:name="com.tencent.android.tpush.XGPushProvider"
       android:authorities="您的应用包名.AUTH_XGPUSH"
       android:exported="true"/>

  <provider
       android:name="com.tencent.android.tpush.SettingsContentProvider"
       android:authorities="您的应用包名.TPUSH_PROVIDER"
       android:exported="false" />

  <provider
       android:name="com.tencent.mid.api.MidProvider"
       android:authorities="您的应用包名.TENCENT.MID.V3"
       android:exported="true" >
  </provider>

	<!-- 请将YOUR_ACCESS_ID修改为APP的AccessId -->
   <meta-data
       android:name="XG_V2_ACCESS_ID"
       android:value="YOUR_ACCESS_ID" />
   <!-- 请将YOUR_ACCESS_KEY修改为APP的AccessKey -->
   <meta-data
       android:name="XG_V2_ACCESS_KEY"
       android:value="YOUR_ACCESS_KEY" />
</application>
```


## 配置服务

Messaging 服务使用默认参数即可，不需要额外配置。如果您已经配置好 TACApplication 单例，这个过程已经自动完成。
