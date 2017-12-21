## 应用云 Analytics服务 Android接入指南

### 集成SDK到你的应用

在你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）添加 应用云 Analytics 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:core:1.0.0'
}
```

### 配置 Analytics 服务

如果你需要编译不同的渠道包，可以在app的AndroidManifest.xml文件中添加meta-data，

```
<meta-data
   	android:name="com.tencent.tac.channel"
	android:value="${tac_channel}" />
```

然后，在应用级的 build.gradle 文件里面设置 **tac_channel**，例如下面的代码，编译了小米和应用宝两个不同的渠道包。

```
android {
	productFlavors {
        xiaomi {
            manifestPlaceholders = [tac_channel: "xiaomi"]
        }
        yingyongbao {
            manifestPlaceholders = [tac_channel: "yingyongbao"]
        }
    }
}
```

### 启动 Analytics 服务

首先确保你已经配置了TAC服务框架，具体详情可参考 [link]。

在你app的Application onCreate方法中，启动 Analytics 服务：

```
TACAnalyticsService.getInstance().start(this);
```

### 上报页面访问

Analytics 在服务启动状态下，默认会统计所有的页面访问，你不需要另外配置。如果需要独立上报页面访问，可以调用：

```
// 页面访问开始
TACAnalyticsService.getInstance().trackPageAppear(context, pageName);

// 页面访问结束
TACAnalyticsService.getInstance().trackPageDisappear(context, pageName);
```

### 上报自定义事件

自定义事件分为两种，单次事件和持续事件。普通事件是指单次事件，而持续事件除了事件本身的属性外，包含了事件的开始和结束时间。

上报单次事件，可以调用：

```
TACAnalyticsService.getInstance().trackEvent(context, TACAnalyticsEvent);

```

上报持续事件，可以调用：

```
// 事件开始
TACAnalyticsService.getInstance().trackEventDurationBegin(context, TACAnalyticsEvent);

// 事件结束
TACAnalyticsService.getInstance().trackEventDurationEnd(context, TACAnalyticsEvent);

```


### 高级设置

[后续补充]

