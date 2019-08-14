## 开发环境要求

- Android Studio 3.3.2
- Gradle-4.1


## 集成说明

TUIKit 支持 aar 集成、 module 源码和 gradle 接入三种集成方式。


### aar 集成

1. 指定 libs 文件夹下 aar 的名称。
```
android {
    ...
    repositories {
        flatDir {
            dirs 'libs'
        }
    }
}
```

2. 添加依赖。
```
dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    ....
    implementation(name: 'tuikit-xxx版本', ext: 'aar')
}
```
其中，`tuikit-xxx版本`中的`xxx`请替换成 [最新的 aar 版本号](https://github.com/tencentyun/TIMSDK/tree/master/Android/SDK)。

### module 源码集成

```
implementation project(':tuikit')
```


### gradle 接入集成

```
dependencies {
    ...
     compile 'com.tencent.imsdk:tuikit:latest.release'
    ...
}
```

## 初始化

在 Application 的 onCreate 中初始化：

```java
public class DemoApplication extends Application {

    public static final int SDKAPPID = "您的SDKAppId";

    @Override
    public void onCreate() {
        super.onCreate();

       // 配置 Config，请按需配置
       TUIKitConfigs configs = TUIKit.getConfigs();
       configs.setSdkConfig(new TIMSdkConfig(SDKAPPID));
       configs.setCustomFaceConfig(new CustomFaceConfig());
       configs.setGeneralConfig(new GeneralConfig());

       TUIKit.init(this, SDKAPPID, configs);
    }
}
```

init 方法的说明：

<pre>
/**
 * TUIKit 的初始化函数
 *
 * @param context  应用的上下文，一般为对应应用的 ApplicationContext
 * @param sdkAppID 您在腾讯云注册应用时分配的 SDKAppID
 * @param configs  TUIKit 的相关配置项，一般使用默认即可，需特殊配置参考 <a href="https://imsdk-1252463788.cos.ap-guangzhou.myqcloud.com/IM_DOC/Android/TUIKit/com/tencent/qcloud/tim/uikit/config/TUIKitConfigs.html">API 文档</a>
 */
public static void init(Context context, int sdkAppID, TUIKitConfigs configs)
</pre>

