# 下载配置文件

Android Studio 说明

1. 下载 tac\_services\_configurations.zip
2. 解压 tac\_services\_configurations.zip 后，将其中的 `tac_service_configurations.json` 文件移动到您的 Android Studio 项目目录下面的 应用模块的 `asserts` 目录下，并将其中的 `tac_service_configurations_unpackage.json` 文件添加到您项目应用模块的根目录下。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/tac_android_configuration.jpg)


# 添加 SDK 

Gradle 说明

MobileLine 移动开发平台核心库会读取您刚才下载的配置文件启动服务。请修改您的 build.gradle 文件以使用服务。

1.使用 jcenter 作为仓库来源

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


2.添加 Android SDK 库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加核心库 SDK 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-core:1.0.0'
}
```

然后，点击 IDE 的 gradle 同步按钮，会自动将依赖包同步到本地。


# 添加初始化代码

1.在应用模块 `Application` 子类的 `onCreate` 方法中添加以下初始化代码:

```
public class MyCustomApp extends Application {

	@Override
	public void onCreate() {
		super.onCreate();
		...
		// 增加这行
		TACApplication.configure(this);
	}
	
}
```

2.在 `AndroidManifest.xml` 添加 自定义的 Application 子类：

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.tac">

    <application
        android:name="com.example.tac.MyCustomApp"
        ...
    </application>
</manifest>
```


