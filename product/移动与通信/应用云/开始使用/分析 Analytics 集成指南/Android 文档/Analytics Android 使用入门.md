
## 准备工作

在开始使用移动开发平台（MobileLine） Analytics 服务前，确保您已经完成：[安装和配置 SDK](https://cloud.tencent.com/document/product/666/14305)

## 添加 SDK

如果希望将 Analytics 库集成至自己的某个项目中，可以通过 gradle 远程依赖或者 jar 包两种方式集成。

### 通过 gradle 远程依赖集成

如果您使用 Android Studio 作为开发工具或者使用 gradle 编译系统，**我们推荐您使用此方式集成依赖。**

#### 1. 使用 jcenter 作为仓库来源

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

#### 2. 添加 Analytics 库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加 Analytics 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-core:1.0.0'
}
```
 
添加完成后，单击您 IDE 的 【gradle】 同步按钮，会自动将依赖包同步到本地。

### 手动集成

如果您无法采用远程依赖的方式，您可以通过以下方式手动集成。

#### 1. 下载资源压缩包

下载请点击 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。

#### 2. 集成 jar 包

将解压得到的所有 jar 文件拷贝到您工程或模块的 libs 目录下。

#### 3. 修改您工程的 AndroidManifest.xml 文件

请按照下面的示例代码修改您工程下的 AndroidManifest.xml 文件。

```
<!-- 添加 Analytics 需要的权限 -->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
<uses-permission android:name="android.permission.WRITE_SETTINGS"/>

<application>

...

	<!-- 添加 Analytics 的 provider -->
	<provider
		android:name="com.tencent.mid.api.MidProvider"
		android:authorities="你的包名.TENCENT.MID.V3"
		android:exported="true" >
	</provider>

</application>
```

## 配置渠道

您可以编译不同的渠道包，用于运营数据的采集。如果您没有配置渠道，Analytics 仍然可以正常运行。

如果您想要配置渠道信息，可以在您工程的 `AndroidManifest` 文件中添加元数据信息：

```
<application>

<!-- 请将value改为app发布对应的渠道，不同的发布渠道使用不同的名字。-->
<meta-data android:name="com.tencent.tac.channel" android:value="xiaomi"/>
	
</application>
```
 
> **注意：**
> 若填写的渠道为纯数字字符串类型，请不要超过 int 表示的范围。
 
### gradle 自动生成渠道包

如果您是采用 gradle 编译，可以将您的 meta-data 设置为：

```
<meta-data
   	android:name="com.tencent.tac.channel"
	android:value="${tac_channel}" />
```

然后，在应用级的 build.gradle 文件里面设置多个产品，每个产品设置不同的 `tac_channel` 。这样当您通过 gradle 编译不同的包时，AndroidManifest 中元数据的 value 会自动替换成配置的值。例如下面的代码，定义了小米商店和应用宝两个不同的渠道包：

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

## 配置服务

Analytics 服务使用默认参数即可，不需要额外配置。如果您已经配置好 TACApplication 单例，这个过程已经自动完成。

### 高级配置

如果您需要自定义服务的策略，您可以使用 TACAnalyticsOptions 修改一些具体的策略：

```
TACApplicationOptions applicationOptions = TACApplication.options();

TACAnalyticsOptions analyticsOptions = applicationOptions.sub("analytics");
```

具体的 API 请参考 TACAnalyticsOptions 的 API 文档。

>**注意：**
>请在 Analytics 服务启动前完成它对应的参数配置，一旦服务启动，后续所有对它的参数修改都不会生效。
