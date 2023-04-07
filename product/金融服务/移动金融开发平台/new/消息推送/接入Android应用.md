## 集成

### 开发要求
需要安装 Java 开发环境 JDK、Android SDK 及 Android Studio IDE 综合开发环境，完成通用部署。

### 添加SDK
1. 参考[ Android 应用接入-IDE 方式](https://cloud.tencent.com/document/product/1034/85243)或者 [Android 应用接入-Gradle 方式](https://cloud.tencent.com/document/product/1034/85242) ，完成框架接入。
2. 在 module 级别 build.gradle 中，配置依赖。
```groovy
implementation 'com.tencent.tmf.android:profile:+'
implementation 'com.tencent.tmf.android:push:+'
```
   
## 接入厂商推送通道

### 小米推送服务接入

#### 配置小米推送参数
注册小米推送服务步骤，请参见 [Android 厂商通道参数申请指南 > 小米参数获取](https://cloud.tencent.com/document/product/1034/86570#xiaomi)，请根据页面中的申请流程完成开通推送服务并获取 AppID 和 AppKEY，在 build.gradle 文件中声明：
```groovy
manifestPlaceholders = [
        XM_APPID            : rootProject.ext.TMFDemo_push.xiaomiPushAppId,
        XM_APPKEY           : rootProject.ext.TMFDemo_push.xiaomiPushAppKey,
]
```
>?小米推送注册失败回调码查询 [小米服务端错误码参考](https://dev.mi.com/console/doc/detail?pId=1557)。
>

#### 配置小米推送 SDK
在您的 build.gradle 文件中添加小米推送需要用到的 SDK：
```groovy
implementation "com.tencent.tmf.android:xiaomi-push:+"
implementation "com.tencent.tmf.android:push-support-xiaomi:+"
```

### 华为推送服务接入

#### 配置华为推送参数
注册华为推送服务步骤，请参见 [Android 厂商通道参数申请指南 > 华为参数获取](https://cloud.tencent.com/document/product/1034/86570#huawei)，请根据页面的申请流程完成开通推送服务并获取APPID，在build.gradle文件中进行声明：
```groovy
manifestPlaceholders = [
        HW_APPID            : rootProject.ext.TMFDemo_push.huaweiPushAppId,
]
```
>?华为推送注册失败回调码查询 [华为开发文档](https://developer.huawei.com/consumer/cn/service/hms/catalog/huaweipush_agent.html?page=hmssdk_huaweipush_api_reference_errorcode)。
>

#### 配置华为 SDK
1. 下载 agconnect-services.json。
华为旧版 SDK 升级后，官方提供了 `agconnect-services.json` 作为配置文件，需要在官方管理后台下载：
![](https://qcloudimg.tencent-cloud.cn/raw/5c51232568e9e46afcc8781bd9c9bb8b.png)
 将 `agconnect-services.json` 文件拷贝到应用级根目录下。
![](https://qcloudimg.tencent-cloud.cn/raw/676aa2c5df6efecc4aeda9ab5e853c60.png)
2. 配置 HMS Core SDK 的 Maven 仓地址。
![](https://qcloudimg.tencent-cloud.cn/raw/5f7683ce6dbb769a1f5d0b613e79a52c.png)
```groovy
buildscript {
    repositories {
        // 配置HMS Core SDK的Maven仓地址。
        maven {url 'https://developer.huawei.com/repo/'}
    }
    dependencies {
        // 增加agcp插件配置。
        classpath 'com.huawei.agconnect:agcp:1.4.2.300'
    }
}

allprojects {
    repositories {
        // 配置HMS Core SDK的Maven仓地址。
        maven {url 'https://developer.huawei.com/repo/'}
    }
} 
```
3. 添加华为插件和 push sdk。
![](https://qcloudimg.tencent-cloud.cn/raw/928c8f2343138281c34e5128644b5e91.png)
在 App 的 build.gradle 中添加如下配置和依赖：
```groovy
apply plugin: 'com.huawei.agconnect'
```
```groovy
implementation 'com.huawei.hms:push:5.0.4.302'// 推荐使用旧版本，新版本可能无法支持部分旧机型
implementation 'com.tencent.tmf.android:push-support-huawei:+'
```

### 荣耀推送服务接入

#### 配置荣耀推送参数
注册荣耀推送服务步骤，请参见 [Android 厂商通道参数申请指南 > 荣耀参数获取](https://cloud.tencent.com/document/product/1034/86570#honor)，请根据页面介绍完成开通推送服务并获取APPID，在build.gradle文件中进行声明：
```groovy
manifestPlaceholders = [
			HONOR_APPID            : rootProject.ext.TMFDemo_push.honorPushAppId,
]
```
>?荣耀推送注册失败回调码查询 [荣耀开发文档](https://developer.hihonor.com/cn/doc/guides/100455)。
>

#### 配置荣耀 SDK
1. 下载 hcs-services.json。
荣耀官方提供了 `hcs-services.json` 作为配置文件，需要在官方管理后台下载，参考如下：
![](https://qcloudimg.tencent-cloud.cn/raw/f03e9750d7807d930c22f334af7ac0f5.png)
 同华为，将 hcs-services.json 文件拷贝到应用级根目录下即可。 
2. 添加荣耀 push sdk。
```groovy
implementation 'com.tencent.tmf.android:honor-push:+'
implementation 'com.tencent.tmf.android:push-support-honor:+'
```

### OPPO 推送服务接入

#### 配置OPPO推送参数
注册 OPPO 推送服务步骤，请参见 [Android 厂商通道参数申请指南 > OPPO参数获取](https://cloud.tencent.com/document/product/1034/86570#OPPO)，请根据页面说明完成开通推送服务并获取 AppKEY 和 APPSECRET，在build.gradle文件中声明：
```groovy
manifestPlaceholders = [
        OPPO_APPKEY         : rootProject.ext.TMFDemo_push.oppoPushAppKey,
        OPPO_APPSECRET      : rootProject.ext.TMFDemo_push.oppoPushAppSecret
]
```
>?OPPO 推送注册失败回调码查询 [错误代码定义](https://open.oppomobile.com/new/developmentDoc/info?id=11224)。
>


#### 配置 OPPO 推送 SDK
```groovy
implementation 'com.tencent.tmf.android:oppo-push:+'
implementation 'com.tencent.tmf.android:push-support-oppo:+'
```

### vivo 推送服务接入

#### 配置 vivo 推送参数
注册 vivo 推送服务步骤，请参见 [Android 厂商通道参数申请指南 > vivo 参数获取](https://cloud.tencent.com/document/product/1034/86570#vivo)，请根据页面说明完成开通推送服务并获取 AppPID 和 AppKEY，在 build.gradle 文件中声明：
```groovy
manifestPlaceholders = [
        VIVO_APPID          : rootProject.ext.TMFDemo_push.vivoPushAppId,
        VIVO_APPKEY         : rootProject.ext.TMFDemo_push.vivoPushAppKey
]
```
>?vivo 推送注册失败回调码查询 [错误码](https://dev.vivo.com.cn/documentCenter/doc/226)。
>

#### 配置 vivo 推送 SDK
```groovy
implementation 'com.tencent.tmf.android:vivo-push:+'
implementation 'com.tencent.tmf.android:push-support-vivo:+'
```

## 打开 URI 并传参
使用消息推送功能通过通知栏打开页面 URI 或是网页 URI 时，组件内部将按照系统默认的方式展示 URI 内容。当需要使用其它方式打开 URI 时（如：自定义webview），实现该接口，并传入接口实现类，则可实现自定义 URI 打开方式。
**接口定义**
```java
public abstract class TMFPushIntentCreator {
    /**
     * 返回跳转打开uri的intent
     * @param context 打开页面使用的上下文
     * @param type 跳转类型，参考EJumpType定义: 1-APP跳转，2-Url跳转，3-跳转应用内页，4-不跳转
     * @param uri 要打开的uri
     * @param jsonExtras json格式的附加参数
     * @return 需要打开的uri的Intent
     */
    public Intent createIntent(Context context, int type, String uri, String jsonExtras) {
        return null;
    }
}
```
**参数说明**

| 参数名称 | 参数类型 | 参数描述                                                     | 必选 |
| -------- | -------- | ------------------------------------------------------------ | ---- |
| context  | Context  | 供使用的上下文                                               | YES    |
| type     | int      | 跳转类型，参考EJumpType定义: 1-APP跳转，2-Url跳转，3-跳转应用内页，4-不跳转 | YES    |
| uri      | String   | 需要打开的 URI                                               |YES    |
| extra    | String   | 附加参数                                                     | YES    |

**Sample**
```java
//传入打开uri的intent，不传则打开默认浏览器
PushCenter.setPushIntentCreator(new OpenUrlForPushImpl());
```
```java
public class OpenUrlForPushImpl extends TMFPushIntentCreator {
    @Override
    public Intent createIntent(Context context, int type, String uri, String jsonExtras) {
        if (type == EJumpType._EJT_URL && !TextUtils.isEmpty(uri)) {
            Intent intent = new Intent(context, JSapiActivity.class);
            intent.putExtra(JSapiActivity.PAGE_TYPE, JSapiActivity.WEB_PAGE);
            intent.putExtra(JSapiActivity.PAGE_URL, uri);
            return intent;
        }
        return null;
    }
}
```

如果打开 URi 时并获取一些参数，可以在管理后台按照如下设置：
![](https://qcloudimg.tencent-cloud.cn/raw/55aac1c422f9d05054e3e48abe3b8c26.png)

## 实现自定义通知栏[](id:sxzdytzl)
对于通知栏消息的展示，push 组件提供通知栏默认样式，即展示默认 app icon，标题，内容。默认通知栏的展示图标可通过在 mipmap 文件夹下，放置资源图片进行修改。通知栏小图标命名为 ic_notification_small，大图标命名为 ic_notification_large，当 mipmap 文件夹中，放置了对应命名的资源文件时，组件内部将获取资源用于默认通知栏样式展示。（请在对应文件夹下放置对应分辨率的图片）。
![](https://qcloudimg.tencent-cloud.cn/raw/4be90499a60733fc482ae75416274c23.png)
组件提供自定义通知栏样式接口。当需要自定义通知栏样式时，则需实现 ICustomNotificationForPush 接口并将其实现类传入 push 组件。同时，由于通知栏事件由外部处理，组件无法处理事件上报，故提供通知栏事件上报接口，由外部调用上报。
>?接入华为小米等厂商推送 SDK 时，通知栏消息的样式由手机厂商控制，该自定义通知栏样式接口只在自有通道展示。
>
**接口定义**
```java
public interface ICustomNotificationForPush {
    /**
     * 调用自定义通知栏的展示
     * @param tmfPushMessage
     * @return 自定义展示通知栏成功返回true，失败返回false
     */
    public boolean showCustomNotification(TMFPushMessage tmfPushMessage);
}
```
**方法参数**
请参见 [TMFPushMessage（通知栏消息数据结构）](#API) 。
**Sample**
```java
PushCenter.setCustomNotification(new CustomNotificationForPushImpl());//可选，非厂商push时通知栏自定义样式的实现
```
```java
public class CustomNotificationForPushImpl implements ICustomNotificationForPush {

    @Override
    public void showCustomNotification(TMFPushMessage tmfPushMessage) {
      //展示自定义的通知栏
      CustomNCFactory.getInstance()
        .showPushNotification(ContextHolder.sContext,tmfPushMessage);
    }
}
```

## 实现通知栏事件上报接口-自定义通知栏时使用
自定义通知栏样式时，通知栏事件的上报须由调用方发起上报，故提供上报接口如下。
**接口定义**
```java
public interface ICustomNCReporter {
    public static final int NC_EVENT_SHOW = EPushPhase.EPP_Show;//通知栏展示
    public static final int NC_EVENT_CLICK = EPushPhase.EPP_Click;//通知栏点击
    public static final int NC_EVENT_CLEAR = EPushPhase.EPP_Clear;//用户主动清除通知栏
    public static final int NC_EVENT_APP_CANCEL = EPushPhase.EPP_Cancel;//App内部清除通知栏

    /**
     * 上报通知栏事件
     * @param tmfPushMessage 通知栏消息体
     * @param event 通知栏事件
     */
    public void reportNCEvent(TMFPushMessage tmfPushMessage, int event);
}
```
**参数说明**

| 参数名称       | 参数类型       | 参数描述          | 必选 |
| -------------- | -------------- | ----------------- | ---- |
| tmfPushMessage | TmfPushMessage | 通知栏消息数据体  | YES    |
| Event          | int            | 通知栏事件 int 值 | YES    |

**Sample**
```java
//上报通知栏事件-展示
PushCenter.getCustomNCReporter().reportNCEvent(tmfPushMessage, ICustomNCReporter.NC_EVENT_SHOW);
```

## 条件推送设置

### 账号推送
通过控制台推送消息时，可以指定按用户账号推送，当需要使用此功能时，需要在客户端调用接口`setUserId(String userId)`设置 userId，该接口按传值判断绑定/解绑，传入空串即为解绑操作。
**接口定义**
```java
/**
 * 设置UserId
 * @param userId
 */
public static void setUserId(String userId) {}
```
**Sample**
```java
//设置userId的接口示例，用于按用户标识做消息推送，实际使用场景为获取到userId后进行上报
ProfileManager.setUserId("custom_userid_1");

// userId解绑示例
ProfileManager.setUserId("");
```

### 地区推送
通过控制台推送消息时，可以指定按地区推送，当需要使用此功能时，需要在客户端调用地理位置上报接口，将客户端地区信息同步到云端。
**接口定义**
```java
/**
 * 地理位置上报（按地区推送）
 * @param country 国家
 * @param province 省
 * @param city 市
 */
 public static void setLocation(String country,String province,String city){}
```

## API[](id:API)
**TMFPushMessage-通知栏消息数据结构**
接 [实现自定义通知栏](#sxzdytzl)，自定义通知栏样式时，通知栏展示相关的数据将通过 TMFPushMessage 数据体传给调用方。数据体结构如下：
```java
public class TMFPushMessage implements Serializable {

    public static final int OPEN_APP = 1;
    public static final int OPEN_URL = 2;
    public static final int OPEN_ACTIVITY = 3;

    private String title;
    private String content;
    private String jsonExtra;//附加参数
    private int jumpType;//跳转类型:1-打开应用;2-跳转url;3-跳转指定页面
    private String jumpParam;//跳转参数

    ...
}
```

