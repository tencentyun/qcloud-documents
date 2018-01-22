# 应用云 Authorization 服务 Android 集成指南

## 准备工作

在开始使用应用云 Authorization 服务前，确保您已经完成：

 1. [安装和配置SDK](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/_Drafts/ApplicationBoard/%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Core/Android/GettingStarted.md)

## 添加 SDK

如果希望将 Authorization 库集成至自己的某个项目中，可以通过 gradle 远程依赖或者 jar 包两种方式集成。

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

#### 2. 添加 Authorization 库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加 Authorization 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-authorization:1.0.0'
}
```

然后，点击您 IDE 的 gradle 同步按钮，会自动将依赖包同步到本地。

### 手动集成

如果您使用 Eclipse 作为开发工具并且使用 Ant 编译系统，您可以通过以下方式手动集成。

#### 1. 下载服务资源压缩包

下载请点击[应用云 Authorization 服务资源]()，并解压。

#### 2. 集成jar包

将资源文件中的 libs 目录下的文件拷贝到您工程的 libs 目录

#### 3. 修改您工程的 AndroidManifest.xml 文件

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件

```
<!-- 添加 Analytics 需要的权限 -->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_SETTINGS"/>

<application>

<provider
	android:name="com.tencent.mid.api.MidProvider"
	android:authorities="你的包名.TENCENT.MID.V3"
	android:exported="true" >
</provider>

<!-- 请添加这行，否则无法编译通过 -->
<meta-data android:name="TA_APPKEY" android:value=""/>

<!-- 如果您需要配置渠道，请将value改为app发布对应的渠道，否则不需要进行修改。-->
<meta-data android:name="InstallChannel" android:value=""/>

</application>
```

## 配置服务

Authorization 服务使用默认参数即可，不需要额外配置。如果您已经配置好 TACApplication 单例，这个过程已经自动完成。


## 集成微信登录


在您的应用级 build.gradle（通常是 app/build.gradle）添加微信 OpenSDK 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.mm.opensdk:wechat-sdk-android-without-mta:+'
}
```

## 集成QQ登录

将 [QQ互联的Android Jar包](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/Android_SDK_V3.3.0.lite.zip) 拷贝到应用模块的libs文件夹下，同时确保你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）文件中已经添加了对libs的依赖：

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```
