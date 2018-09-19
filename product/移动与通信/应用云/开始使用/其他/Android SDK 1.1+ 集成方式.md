## 准备工作

您首先需要一个 Android 工程，这个工程可以是您现有的工程，也可以是您新建的一个空的工程。

## 第一步：创建项目和应用（已完成请跳过）

在使用我们的服务前，您必须先在 MobileLine 控制台上 [创建项目和应用](https://cloud.tencent.com/document/product/666/15345)。

## 第二步：添加配置文件

在您创建好的应用上单击【下载配置】按钮来下载该应用的配置文件的压缩包：

![](http://tacimg-1253960454.file.myqcloud.com/guides/project/downloadConfig.gif)

解压该压缩包，您会得到 `tac_service_configurations.json` 和 `tac_service_configurations_unpackage.json` 两个文件，请您如图所示添加到您自己的工程中去。

![](http://tac-android-libs-1253960454.file.myqcloud.com/tac_android_configuration_1%2B.jpg)

>**注意：**
>请您按照图示来添加配置文件，`tac_service_configurations_unpackage.json` 文件中包含了敏感信息，请不要打包到 apk 文件中，MobileLine SDK 也会对此进行检查，防止由于您误打包造成的敏感信息泄露。

## 集成 SDK 

#### 使用 jcenter 作为仓库来源

在工程根目录下的 build.gradle 使用 jcenter 作为远程仓库：

```
buildscript {
    repositories {
        jcenter()
    }
}

allprojects {
    repositories {
        jcenter()
    }
}
```


#### 添加 Android SDK 库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加所需要的 SDK 的依赖，例如核心库：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-core:1.2.+'
}
```

然后，单击 IDE 的 gradle 同步按钮，会自动将依赖包同步到本地。
