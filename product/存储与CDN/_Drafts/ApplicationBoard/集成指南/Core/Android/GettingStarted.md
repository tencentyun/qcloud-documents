# 应用云 Android 集成指南

## 准备工作

### 创建项目

在使用我们的服务前，您必须先在 TAC 平台上创建项目和应用，首先登录 [TAC 平台](https://console.qcloud.com/tac)，然后点击【创建项目】按钮来创建一个新的项目：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_new_project.png?raw=true)


### 创建应用

创建好项目后，选择该项目，然后点击【创建应用】按钮在该项目下新建一个应用：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_new_app.png)

 1. 输入您应用的包名，这个包名必须是唯一的，并且和您最终发布的应用包名一致。
 2. 根据提示，下载配置文件压缩包，并在本地解压。您可以随时重新下载此文件。
 3. 将 tac\_service_configurations.json 文件并放到您应用模块的 assets 文件夹下。
 4. 将 tac\_service_configurations_unpackage.json 文件并放到您应用模块的根目录下。

## 添加 SDK

如果希望将应用云的库集成至自己的某个项目中，可以通过 gradle 远程依赖或者 jar 包两种方式集成。

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


#### 2. 添加应用云库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加应用云库的依赖。您可以添加自己希望的 SDK 的依赖项。最基础的依赖是 com.tencent.tac:tac-core，它可以提供 Analytics 功能。具体请参阅文档下方的可用库列表。

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-core:1.0.0'
}
```

然后，点击您 IDE 的 gradle 同步按钮，会自动将依赖包同步到本地。

### 手动集成

如果您使用 Eclipse 作为开发工具并且使用 Ant 编译系统，您可以通过以下方式手动集成。对于每个依赖库，我们都提供了手动集成的方式，具体请参考每个依赖库的集成文档。

## 配置 SDK

应用云所有服务都必须在 TACApplication 单例配置完成之后才能正常使用。因此，我们建议您在 Application 的 onCreate 方法中执行该操作。

请注意，如果您使用了多个应用云服务，只要配置一次即可。**TACApplication 单例必须且只允许配置一次**。

您可以有两种方式配置，默认配置和高级配置。通常情况下，您使用默认配置即可。


### 使用默认配置

默认配置可以使用 TACApplication 的 configure(Context) 方法，应用云会自动依照下载的配置文件，完成配置工作。

```
TACApplication.configure(context);
```

### 使用高级配置

如果您需要自定义配置某些服务，可以使用 TACApplication 的 configureWithOptions(Context, TACApplicationOptions) 方法。下面是自定义配置的示例代码：

```
// 获取一个新的默认配置实例
TACApplicationOptions applicationOptions = TACApplicationOptions.newDefaultOptions(context);

// 获取您想要自定义配置的服务参数，例如 Analytics
TACAnalyticsOptions analyticsOptions = applicationOptions.sub("analytics");
// 修改 Analytics 的上报策略，具体配置项请参考每个依赖库的API文档
analyticsOptions.strategy(TACAnalyticsStrategy.INSTANT);

// 修改完成后，用新参数用配置SDK
TACApplication.configureWithOptions(context, applicationOptions);
```

每个服务都对应一个参数配置，可以通过服务的名称获取，例如获取 推送 服务的配置参数，可以使用：

```
TACMessagingOptions messagingOptions = applicationOptions.sub("messaging");
```

具体的服务名称列表可以参考文档下方的可用库列表。

### 获取当前配置

配置完成之后，您任何时候都可以使用 TACApplication 的 options() 方法获取当前的配置参数。**您可以再次修改参数，但请在每个服务启动前完成它对应的参数配置。一旦服务启动，后续所有对它的参数修改都不会生效**。

```
TACApplicationOptions currentOptions = TACApplication.options();

```

### debug模式

如果你想打开debug模式，查看应用云的日志，可以通过以下命令开启：

```
adb shell setprop log.tag.tac DEBUG
```

## 可用的库

以下库分别对应各种应用云的功能。

| gradle | 服务名称 | 功能 |
|:----|:-----------|:-----------|
|  com.tencent.tac:tac-core:1.0.0   |  analytics | 分析 |
|  com.tencent.tac:tac-messaging:1.0.0   |  messaging | 推送 |
|  com.tencent.tac:tac-crash:1.0.0   |  crash     | Crash |
|  com.tencent.tac:tac-storage:1.0.0   |  storage   | Cloud Storage |
|  com.tencent.tac:tac-social:1.0.0   |  social | 登录 |
|  com.tencent.tac:tac-payment:1.0.0   |  payment | 支付 |
