## 准备工作

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用（已完成请跳过）

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

## 第二步：添加配置文件（已完成请跳过）

在您创建好的应用上点击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/project/downloadConfig.png)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

<img src="http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg" width="50%" height="50%">

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。


## 第三步：集成 SDK

您需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 Authorization 服务依赖：

```
dependencies {
    // 增加这两行
    compile 'com.tencent.tac:tac-core:1.1.0'
    compile 'com.tencent.tac:tac-authorization:1.1.0'
}
```

## 第四步：设置 qq app id

您可以根据需要，选择是否集成qq登录服务，请按照选择查看下面的设置方式。

### 集成 qq 登录服务的设置方式

如果您想要集成qq登录服务，请确保您已经在 [QQ 互联平台](https://connect.qq.com/) 注册了应用，如果没有，请先移步注册。

注册完成之后，您需要在您应用级 build.gradle 文件（通常是 app/build.gradle）中添加 app id：

```
android {
    defaultConfig {
    	 // 添加这行
        manifestPlaceholders = [qqOpenId: "互联平台的 qq app id"]
    }
    ...
}
```


### 不集成 qq 登录服务的设置方式

如果您不需要集成qq登录服务，请在您的应用级 build.gradle 文件（通常是 app/build.gradle）中添加这行：

```
android {
    defaultConfig {
    	 // 添加这行
        manifestPlaceholders = [qqOpenId: ""]
    }
    ...
}
```

到此您已经成功接入了 MobileLine 登录与授权服务。
