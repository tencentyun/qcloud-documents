
## 准备工作

在开始使用移动开发平台（MobileLine） Authorization 服务前，确保您已经完成：[安装和配置 SDK](https://cloud.tencent.com/document/product/666/14305)

## 添加 Authorization SDK

如果希望将 Authorization 库集成至自己的某个项目中，可以通过 gradle 远程依赖或者 jar 包两种方式集成。

### 通过 gradle 远程依赖集成

如果您使用 Android Studio 作为开发工具或者使用 gradle 编译系统，我们推荐您使用此方式集成依赖。

#### 1. 使用 jcenter 作为仓库来源。

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

#### 2. 添加 Authorization 库依赖。

在您的应用级 build.gradle（通常是 app/build.gradle）添加 Authorization 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-authorization:1.0.0'
}
```

然后，单击 IDE 的 【gradle】 同步按钮，会自动将依赖包同步到本地。

### 手动集成

如果您无法采用远程依赖的方式，您可以通过以下方式手动集成。

#### 1. 下载服务资源压缩包

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。
2. 下载 [移动开发平台（MobileLine） Authorization 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-authorization-1.0.0.zip)，并解压。

#### 2. 集成 jar 包

将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。

## 配置服务

Authorization 服务使用默认参数即可，不需要额外配置。如果您已经配置好 TACApplication 单例，这个过程已经自动完成。

**Authorization 服务需要配合微信或者 QQ 登录才能工作**，您可以根据业务需要，自行选择同时集成两种登录方式，或者选择其中一种。


## 集成微信登录


### 1. 注册应用

如果您还没有在 [微信开放平台](https://open.weixin.qq.com/cgi-bin/index?t=home/index&lang=zh_CN) 注册您的应用，请先移步注册您的应用，并且获取应用登录能力。

### 2. 配置应用

在您的应用模块的 assets 文件夹下，新建一个名为 tac\_service\_configurations\_wechat.json 的文件，内容如下：

```
{
  "services": {
    "social": {
      "wechat": {
        "appId": "您的微信开放平台app id"
      }
    }
  }
}
```

### 3. 添加 SDK

#### 通过 gradle 远程依赖集成

如果您是采用 gradle 编译系统，Authorization 库已经包含了微信所需要的库文件，您不需要做任何设置。

#### 手动集成

移动开发平台（MobileLine） Authorization 资源包已经包含了微信的 SDK，您不需要另外下载。

然后，在您的 AndroidManifest.xml 文件中添加以下 SDK 需要的权限：

```
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

## 集成 QQ 登录

### 1. 注册应用

如果您还没有在 [QQ 互联平台](https://connect.qq.com/) 注册应用，请先移步注册您的应用。

### 2. 配置应用

在您的应用模块的 assets 文件夹下，新建一个名为 `tac\_service\_configurations\_qq.json` 的文件，内容如下：

```
{
  "services": {
    "social": {
      "qq": {
        "appId": "您的QQ互联平台的app id"
      }
    }
  }
}
```


### 3. 下载 SDK 

下载 [jar 包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/jars/open_sdk_r5923_lite.jar) ，并拷贝到应用模块的 `libs` 文件夹下。


### 4. 添加 SDK 依赖

#### 通过 gradle 远程依赖集成

如果您是采用 gradle 编译系统，确保应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）文件中已经包含了对 libs 目录的依赖：

```
dependencies {
    compile fileTree(dir: 'libs', include: ['*.jar'])
}
```

#### 手动集成

请把下载的 QQ open jar 包添加到 classpath 中，并在 AndroidManifest.xml 文件中添加以下权限和 Activity：

```
	<uses-permission android:name="android.permission.INTERNET" />
   	<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application>
    	...
    	
        <activity
            android:name="com.tencent.tauth.AuthActivity"
            android:launchMode="singleTask"
            android:noHistory="true">
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />

                <!--<data android:scheme="${tencentOpenAppId}" />-->
            </intent-filter>
        </activity>

        <activity
            android:name="com.tencent.connect.common.AssistActivity"
            android:screenOrientation="behind"
            android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:configChanges="orientation|keyboardHidden">
        </activity>
    </application>
```
