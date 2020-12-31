## 开发环境要求

- Android Studio 3.6.1
- Gradle-5.1.1


## 集成说明

TUIKit 支持 gradle 接入、aar 集成和 module 源码集成。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2765-53354?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

>?更多实操教学视频请参见：[极速集成 TUIKit（Android）](https://cloud.tencent.com/edu/learning/course-3130-56399)。

### gradle 接入集成

```
dependencies {
    ...
    implementation 'com.tencent.imsdk:tuikit:xxx版本'
    ...
}
```
其中，`xxx版本`中的`xxx`请替换成 [最新的 aar 版本号](https://github.com/tencentyun/TIMSDK/tree/master/Android/SDK)。

### module 源码集成

```
implementation project(':tuikit')
```

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


## 初始化

在 Application 的 onCreate 中初始化：

```java
public class DemoApplication extends Application {

    public static final int SDKAPPID = 0; // 您的 SDKAppID

    @Override
    public void onCreate() {
        super.onCreate();

       // 配置 Config，请按需配置
       TUIKitConfigs configs = TUIKit.getConfigs();
       configs.setSdkConfig(new V2TIMSDKConfig());
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

