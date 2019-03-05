# Android 应用使用腾讯云 MobileLine 平台

Android 开发发展到今天，github上有各种各样的轮子可供使用，可以非常快速的开发一个可用的版本。但是后期随着业务发展，有了一定用户量，我们需要改进我们的应用，就需要更多的工具：

* 提高运营效果，包括移动统计分析、消息推送等
* 提高应用质量，主要是crash统计、热修复等
* 第三方登录和分享，微信，qq等

这里面其实每个工具都有很多平台可供选择，但是缺少一个完整的平台，可以一次性提供所有的能力。Firebase 虽好，在国内却用不了。国内这样的平台很少，最终我们采用的是腾讯云 MobileLine 移动开发平台，基本上包含了我们需要的工具，也提供了统一的控制台集中管理和监控，这里简单介绍下我们用到的功能。

## 移动分析

移动统计分析可以说是最重要的功能了，应用的日活月活、页面的访问频率、用户画像属性及用户细分行为，通过数据可视化展现，可以协助产品运营决策。

首先，当然是去腾讯云控制台创建账号，然后开通 MobileLine 平台，创建一个对应的应用，下载配置文件到工程中。

接入移动统计功能非常简单，在 gradle 里面加入sdk的依赖，

```
dependencies {
    compile 'com.tencent.tac:tac-core:1.0.0'
}
```

然后，代码里面要在 Application 的 onCreate 里面启动 Service，

```
TACAnalyticsService.getInstance().start(this);
```

然后就可以了。因为我们应用目前只是用到了页面统计，没有添加自定义事件，而 SDK 的页面统计是默认启动的，所以就不需要添加任何逻辑了，感觉还是很方便的。

## 消息推送

消息推送也算是现在应用的标配了。由于 Google 自家的 FCM 在国内不能使用（万恶的xxx），国内各大厂商自己都有自己的推送方案了，这里用的推送服务其实也就是腾讯家的信鸽。

消息推送虽然说起来并不复杂，也就是长连接那套东西，但是涉及到进程保活，网络保活，还有各种ROM的平台兼容性等问题，如果是自己写，还是很麻烦的。

集成消息推送的流程也非常简单，在 gradle 里面加入sdk的依赖，

```
dependencies {
    compile 'com.tencent.tac:tac-messaging:1.0.0'
}
```

然后，代码里面要在 Application 的 onCreate 里面启动 Service，

```
TACMessagingService messagingService = TACMessagingService.getInstance();

messagingService.start(context);
```

之后是注册一个收到消息的回调，当收到消息时，我们可以统计用户的行为，

```
<receiver android:name="com.thebestway.TencentMessagingReceiver">
	<intent-filter>
	    <action android:name="com.tencent.tac.messaging.action.CALLBACK" />
	</intent-filter>
</receiver>

```

然后就可以了。测试结果推送的到达率还是很高的，基本可以做到秒级到达，同时控制台上也有很多报表，可以试试看到发送成功率和用户点击率。

## Crash上报

应用的Crash信息对于改进应用的质量非常重要，这个毋容置疑。这里的Crash上报用的其实就是腾讯的 bugly。

集成的流程也非常简单，在 gradle 里面加入 sdk 的依赖，

```
dependencies {
    compile 'com.tencent.tac:tac-crash:1.0.0'
}
```

然后，代码里面要在 Application 的 onCreate 里面启动 Service，

```
TACCrashService crashService = TACCrashService.getInstance();

crashService.start(context);
```

如果你的应用启用了混淆，那还需要上传符号表，这样未来就能定位到具体的行数了，MobileLine 提供了一个插件上传，

```
buildscript {
    dependencies {
        ......
        classpath 'com.tencent.tac:tac-crash-plugin:1.0.0'
    }
}
```
 
然后在app模块的 build.gralde 文件的头部加入，

```
apply plugin: 'com.android.application'
apply plugin: 'com.tencent.tac.crash'	// 这一行
```

就可以了。


## 第三方登录

第三方登录也算是目前很多应用经常采取的方案了，好处是用户不需要再次输入账号密码，直接用微信qq等常用的平台的账号直接一键登录。

因为我们平台有自己的账号系统，所以这里其实是用微信qq登录返回的用户id作为我们平台的唯一标识。

集成流程主要分微信和qq两步，一般应该是两个都集成。

### 添加基本SDK

```
dependencies {
    compile 'com.tencent.tac:tac-authorization:1.0.0'
}
```

### 集成微信登录

#### 1. 注册应用

到 [微信开放平台](https://open.weixin.qq.com/cgi-bin/index?t=home/index&lang=zh_CN) 注册应用，并且获取应用登录能力。

#### 2. 配置应用

在 app 的 assets 文件夹下，新建一个名为 tac\_service\_configurations\_wechat.json 的文件，内容如下：

```
{
  "services": {
    "social": {
      "wechat": {
        "appId": "微信开放平台app id"
      }
    }
  }
}
```

### 集成 QQ 登录

#### 1. 注册应用

先要在 [QQ 互联平台](https://connect.qq.com/) 注册应用。

#### 2. 配置应用

在 app 的 assets 文件夹下，新建一个名为 `tac\_service\_configurations\_qq.json` 的文件，内容如下：

```
{
  "services": {
    "social": {
      "qq": {
        "appId": "QQ互联平台的app id"
      }
    }
  }
}
```


#### 3. 下载 SDK 

下载 [qq登录jar包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/jars/open_sdk_r5923_lite.jar) ，并拷贝到 `libs` 文件夹下。

## 移动支付

支付不算是应用的标配，不过如果是有内购商品的话，可以直接用微信和qq的支付渠道，非常方便。

因为涉及到钱的问题，所以流程还是比较繁琐的，这里贴一下大致的流程吧，具体可以看下官方的 [指引文档](https://cloud.tencent.com/document/product/666/14599)。

1. 注册微信开放平台账号并进行开发者资质认证
2. 提交资料申请微信支付
3. 在微信开放平台上创建应用
3. 在 QQ 钱包商品平台上填写资料
4. 在腾讯开放平台上创建应用
5. 在 MobileLine 平台上的移动支付配置应用信息。

一般流程配置完，Android 端集成流程就很简单了，在 gradle 添加依赖，

```
compile 'com.tencent.tac:tac-payment:1.0.0'
```

qq支付没有远程依赖，只能从 [mqqopenpay.jar](http://tac-android-libs-1253960454.cosgz.myqcloud.com/jars/mqqopenpay.jar) 手动下载放到工程中。

然后真正的支付流程大概是这样的，

![支付过程](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/payment/payment%E6%95%B4%E4%BD%93%E6%B5%81%E7%A8%8B.png)

具体的 API 调用可以参考下官方的 [编程指南](https://cloud.tencent.com/document/product/666/14594)。