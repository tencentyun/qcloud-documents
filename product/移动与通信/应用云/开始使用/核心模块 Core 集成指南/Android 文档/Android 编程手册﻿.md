## 修改服务配置

通常我们的服务都是按照默认配置自动启动的。但您也可以根据需要，修改服务配置。您可以参考每个子服务的接入文档，以查看有哪些具体的配置项。

### 在 `Application` 子类中添加代码

如果您自己的应用中已经有了 `Application` 的子类，请重载它的 `attachBaseContext(Context)` 方法，在里面添加配置代码，如果没有，请自创建一个 `Application` 的子类。如：

```
public class MyCustomApp extends Application {
  @Override
  protected void attachBaseContext(Context base) {
		super.attachBaseContext(base);
    	// 实例化一个新的配置
		TACApplicationOptions applicationOptions = TACApplicationOptions.newDefaultOptions(this);

		// 根据需要修改配置，这里是设置行为统计数据上报的策略
		TACAnalyticsOptions analyticsOptions = applicationOptions.sub("analytics");
		analyticsOptions.strategy(TACAnalyticsStrategy.INSTANT); // 立即发送
		
		// 修改其他配置
		... 

		// 让自定义设置生效
		TACApplication.configureWithOptions(this, applicationOptions);
  }
}
```

>**注意：**
>configureWithOptions 只能被调用一次，如果您有多个服务的配置需要修改，请全部修改好再调用 configureWithOptions，让配置生效。

### 在 `AndroidManifest.xml` 文件中注册

在创建好 `Application` 的子类并添加好代码后，您需要在工程的 `AndroidManifest.xml` 文件中注册该 `Application` 类：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.example.tac">
  <application
    <!-- 这里替换成你自己的 Application 子类 -->
    android:name="com.example.tac.MyCustomApp"
    ...>
  </application>
</manifest>
```

>**注意：**
>如果您的 `Application` 子类已经在 `AndroidManifest.xml` 文件中注册，请不要重复注册。


## 获取设备标识

MobileLine 会使用一个全局的 device id，它在所有服务中都唯一地标识了一个设备。如果您需要在代码中获取 device id，可以使用：

```
String deviceId = TACApplication.getDeviceId();
```

## 绑定用户标识

MobileLine 的多项服务（如 Analytics、Messaging 等）都可以在上报信息时带上用户标识，这样通过后台查看数据的时候，可以定位到具体的用户。

### 绑定您账号系统的 user id

您可在用户模块登录之后，调用 bindUserId 方法，绑定用户标识：

```
String userId = "your user id";
TACApplication.bindUserId(userId);
```

### 绑定三方登陆系统的 open id

如果通过微信或者 QQ 等三方登录模块，可调用 useOpenId 方法，绑定用户标识：

```
String openId = "your open id";
TACApplication.useOpenId(openId);
```

绑定用户标识后，我们会自动通知所有服务，后续上报信息时，自动带上用户的 ID。

## 查看调试日志

如果您想查看 SDK 的一些调试日志，可以通过以下两种方式打开日志的 debug 开关。

### 命令行打开 debug 模式

在命令行执行：

```
adb shell setprop log.tag.tacApp DEBUG
```	

### 代码打开日志输出开关

在代码中调用：

```
TACApplicationOptions applicationOptions = TACApplicationOptions.newDefaultOptions(this);
applicationOptions.setLoggingEnable(true);

...

TACApplication.configureWithOptions(this, applicationOptions);
```