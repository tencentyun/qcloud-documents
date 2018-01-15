## 应用云 Analytics 服务 Android 接入指南

### 准备工作

在开始使用应用云 Analytics 服务前，您需要：

 1. 新建或者打开一个 Android 项目。
 2. 配置了应用云服务框架，配置方式请参见[应用云服务框架 Android 配置指南](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/_Drafts/ApplicationBoard/%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Core/Android/%E5%BA%94%E7%94%A8%E4%BA%91%20%E6%9C%8D%E5%8A%A1%E6%A1%86%E6%9E%B6%20Android%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97.md.md)。

### 集成 Analytics 服务到你的应用

#### 通过远程依赖集成 (<font color='red'>推荐</font>)

在你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）添加应用云 Analytics 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:core:1.0.0'
}
```

#### 本地集成

1. 下载 Analytics 服务资源打包文件，并解压。下载资源文件请点击[这里]()。
2. 将资源文件中的 libs 目录拷贝到您的 module 的根目录下。
4. 打开您自己 module 下的 AndroidManifest.xml 文件，然后按照下载的资源文件中的 AndroidManifest.xml 作为范例来修改。

### 配置 Analytics 服务

#### 配置渠道

如果你需要编译不同的渠道包，可以在app的AndroidManifest.xml文件中添加meta-data：

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

#### 启动 Analytics 服务实例

Analytics服务在使用前必须先启动，我们建议你放在Application onCreate方法中执行该操作。

在启动服务前，您可以在代码中修改 Analytics 服务的相关配置。请注意，启动之后配置将不允许被修改。

```
// 请确保已经正确配置好服务框架，否则options()方法会返回null
TACApplicationOptions applicationOptions = TACApplication.options();

// 这里获取 Analytics 服务的配置对象，您可以通过这个对象来配置服务。
TACAnalyticsOptions analyticsOptions = applicationOptions.sub("analytics");

```

然后调用 start 方法启动 Analytics 服务：

```
TACAnalyticsService.getInstance().start(this);
```

### 上报页面访问

Analytics 默认会统计所有的页面访问，你不需要另外配置。如果需要独立上报页面访问，可以调用：

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

