
# 腾讯应用云 Messaging 接入指南

Messaging 是腾讯云提供的一种快速、简单的推送服务，支持 Android 平台的通知栏推送和应用内透传消息。开发者可以将指定的信息推送给需要的用户。


## Andorid Studio 自动集成

### 修改 app 的 build.gradle 文件

用户需要在 app 的 build.gradle 文件中添加如下内容：
 
```
android {
    ......
    defaultConfig {

        // 官网上注册的包名。注意 application ID 和当前的应用包名以及官网上注册应用的包名必须一致。
        applicationId "你的包名" 
        ......

        ndk {
            //根据需要 自行选择添加的对应cpu类型的.so库。 
            abiFilters 'armeabi', 'armeabi-v7a', 'arm64-v8a' 
            // 还可以添加 'x86', 'x86_64', 'mips', 'mips64'
        }

        ......
    }
    ......
}

dependencies {
    ......
   
    compile 'com.tencent.tac:messaging:1.0.0-release' 

}

```

### 注册 Messaging 服务回调
用户需要首先继承 TACMessagingReceiver 类，然后将子类在 manifest.xml 文件中进行如下注册：

```

<receiver android:name="TACMessagingReceiver子类，如com.tencent.tac.tacmessaging.MyReceiver">
	<intent-filter>
	    <action android:name="com.tencent.tac.messaging.action.CALLBACK" />
	</intent-filter>
</receiver>
        
```



## 启动 Messaging 服务

集成好 Messaging 服务后，用户需要自己启动 Messaging 服务，具体代码如下：

```
// 首先获取 TACMessagingService 实例
TACMessagingService messagingService = TACMessagingService.getInstance();

// 调用 start 接口启动 Messaging 服务，context 这里最好是使用应用 context。
messagingService.startReceiveNotification(context);

```




