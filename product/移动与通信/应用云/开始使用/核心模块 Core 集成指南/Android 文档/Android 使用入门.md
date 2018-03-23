
## 准备工作

在开始使用移动开发平台（MobileLine）服务前，您需要一个移动开发平台（MobileLine）项目和适用于您的应用的配置文件：

### 创建项目

在使用我们的服务前，您必须先在 TAC 平台上创建项目和应用，首先登录 [TAC 平台](https://console.cloud.tencent.com/tac)，然后点击【创建项目】按钮来创建一个新的项目：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_new_project.png?raw=true)


### 创建应用

创建好项目后，选择该项目，然后点击【创建应用】按钮在该项目下新建一个应用：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_new_app.png)

 1. 输入您应用的包名，这个包名必须是唯一的，并且和您最终发布的应用包名一致。
 2. 根据提示，下载配置文件压缩包，并在本地解压。您可以随时重新下载此文件。
 3. 将 tac\_service_configurations.json 文件并放到您应用模块的 assets 文件夹下。
 4. 将 tac\_service_configurations_unpackage.json 文件并放到您应用模块的根目录下。

## 配置 服务框架SDK

您并不需要额外单独安装移动开发平台（MobileLine）的 `服务框架SDK` 到您的应用中。当您集成某个移动开发平台（MobileLine）的服务时，我们已经自动为您添加了框架 SDK。配置 SDK 的前提是您已经集成了一个或者多个移动开发平台（MobileLine）服务。

移动开发平台（MobileLine）所有服务都必须在 TACApplication 单例配置完成之后才能正常使用。因此，我们建议您在 Application 的 onCreate 方法中执行该操作。

请注意，如果您使用了多个移动开发平台（MobileLine）服务，只要配置一次即可，**TACApplication 单例必须且只允许配置一次**。

您可以有两种方式配置，默认配置和高级配置，通常情况下您使用默认配置即可。


### 使用默认配置

默认配置可以使用 TACApplication 的 configure(Context) 方法，移动开发平台（MobileLine）会自动依照下载的配置文件，完成配置工作。

```
TACApplication.configure(context);
```

### 使用配置文件自定义配置

移动开发平台（MobileLine） SDK 统一配置服务，会读取所有位于您位于应用模块的 assets 里面符合正则条件：`tac_services_configurations*.json`，并合并其里面的内容，然后传递给配置服务，进行对应的服务配置。

例如以下文件名都是合法的配置文件：

```
tac_services_configurations_custom.json
tac_services_configurations_payment.json
```

在读取配置文件的时候，我们会按照字典顺序依次读取( a > z )，并对所有的配置进行合并。如果在多个配置文件中存在多个重复的 Key，则会以顺序靠后的配置文件中的内容为准。

例如文件 `tac_services_configurations_payment.json ` 与 `tac_services_configurations_custom.json` 都存在以 `payment` 为 Key 的内容，则会用 `tac_services_configurations_payment.json ` 中的覆盖掉  `tac_services_configurations_custom.json ` 中的。

每个配置文件的格式都必须和 `tac_services_configurations.json` 保持一致，然后覆写您需要修改的参数，例如

```
{
  "services": {
    "crash": {
      "excludeModuleFilters": [
      ]
    }
  }
}
```

因此，如果您有自定义配置参数的需求，可以通过这种多文件配置的方式，而不需要修改代码。


### 代码动态修改配置

如果您需要在代码中动态修改一些服务的配置，可以使用 TACApplication 的 configureWithOptions(Context, TACApplicationOptions) 方法，下面是修改 Analytics 配置的示例代码：

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

每个服务都对应一个参数配置，可以通过服务的名称获取，例如获取推送服务的配置参数，可以使用：

```
TACMessagingOptions messagingOptions = applicationOptions.sub("messaging");
```

具体的服务名称列表可以参考文档下方的可用库列表。

### 获取当前配置

配置完成之后，您任何时候都可以使用 TACApplication 的 options( ) 方法获取当前的配置参数。**您可以再次修改参数，但请在每个服务启动前完成它对应的参数配置，一旦服务启动，后续所有对它的参数修改都不会生效**：

```
TACApplicationOptions currentOptions = TACApplication.options( );

```

## debug 模式

如果你想打开 debug 模式，查看移动开发平台（MobileLine）的日志，可以通过以下命令开启：

```
adb shell setprop log.tag.tac DEBUG
```

## 示例工程

您可以访问我们的 [示例工程](https://github.com/tencentyun/qcloud-sdk-android-samples)，里面包含了我们所有服务的集成和调用的示例代码。您可以参考代码的编写，也可以下载到本地运行体验。

## 可用的库

以下库分别对应各种移动开发平台（MobileLine）的功能。

| gradle | 服务名称 | 功能 |
|:----|:-----------|:-----------|
|  com.tencent.tac:tac-core:1.0.0   |  analytics | 分析 |
|  com.tencent.tac:tac-messaging:1.0.0   |  messaging | 推送 |
|  com.tencent.tac:tac-crash:1.0.0   |  crash     | 异常上报 |
|  com.tencent.tac:tac-storage:1.0.0   |  storage   | Cloud Storage |
|  com.tencent.tac:tac-authorization:1.0.0   |  social | 登录 |
|  com.tencent.tac:tac-payment:1.0.0   |  payment | 支付 |
