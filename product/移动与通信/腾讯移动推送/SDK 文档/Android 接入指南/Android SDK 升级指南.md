## TPNS Android SDK 1.3.2.0
### OPPO 推送 SDK 升级
升级 TPNS OPPO 推送 SDK 1.3.2.0 时，请注意一并加入以下依赖语句，否则可能导致 OPPO 推送注册失败：
```
implementation 'com.google.code.gson:gson:2.6.2'
implementation 'commons-codec:commons-codec:1.15'
```
### 对应各厂商推送依赖版本
- 华为 : 6.3.0.302
- 小米 : 4.9.1
- 魅族 : 4.1.0
- OPPO : 3.0.0
- vivo :  3.0.0.4

## TPNS Android SDK 1.3.1.1
###  AndroidManifest 新增节点
如您通过手动引入 jar 文件，即参考 SDK 集成文档 [Android Studio 手动集成](https://cloud.tencent.com/document/product/548/36652#android-studio-.E6.89.8B.E5.8A.A8.E9.9B.86.E6.88.90) 部分接入 TPNS SDK 的，请注意在应用的 AndroidManifest 文件 application 标签内添加以下节点，或直接参考上述链接重新引入 AndroidManifest 配置。否则可能引起应用在线时收到的推送无法响应通知点击事件。

>! 此项变更仅需要通过手动引入 jar 文件的应用开发者注意。如您通过拉取远程依赖接入 TPNS SDK，可忽略此项配置。

```xml
    <activity
        android:name="com.tencent.android.tpush.InnerTpnsActivity"
        android:exported="false"
        android:launchMode="singleInstance"
        android:theme="@android:style/Theme.Translucent.NoTitleBar">
        <intent-filter>
            <action android:name="${applicationId}.OPEN_TPNS_ACTIVITY_V2" />

            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
        <intent-filter>
            <data
                android:host="${applicationId}"
                android:scheme="stpns" />

            <action android:name="android.intent.action.VIEW" />

            <category android:name="android.intent.category.BROWSABLE" />
            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
        <intent-filter>
            <action android:name="android.intent.action" />
        </intent-filter>
    </activity>
```

## TPNS Android SDK 1.2.7.0

###  新增应用内消息补推能力
新增是否允许应用内消息展示接口，请注意高版本 Android 使用 WebView 的兼容性详见 [Android 接口文档](https://cloud.tencent.com/document/product/548/36659#.E5.BA.94.E7.94.A8.E5.86.85.E6.B6.88.E6.81.AF.E5.B1.95.E7.A4.BA)。

## TPNS Android SDK 1.2.5.0

###  1. 配置工程依赖环境（可选）

如果您在使用 SDK 依赖时遇到依赖拉取不到的情况，可以考虑在项目工程根目录 build.gradle 文件 allprojects.repositories 位置添加谷歌官方推荐镜像源 MavenCentral 和腾讯云镜像源。代码示例如下：
```
allprojects {
    repositories {
        google()
        // 谷歌推荐 MavenCentral 镜像源
        mavenCentral()
        jcenter()
        // 腾讯云镜像源
        maven { url 'https://mirrors.tencent.com/nexus/repository/maven-public/' }
    }
}
```

### 2. 新增配置（必需）
新增的标签查询接口，需要注意在继承 `XGPushBaseReceiver` 的实现类中增加实现方法 `onQueryTagsResult`。代码示例如下：
``` 
public class MessageReceiver extends XGPushBaseReceiver {

    // 其他回调接口
		// ...
		// 标签查询回调接口
    public void onQueryTagsResult(Context context, int errorCode, String data, String operateName) {
        Log.i(LogTag, "action - onQueryTagsResult, errorCode:" + errorCode + ", operateName:" + operateName + ", data: " + data);
    }
}
```
