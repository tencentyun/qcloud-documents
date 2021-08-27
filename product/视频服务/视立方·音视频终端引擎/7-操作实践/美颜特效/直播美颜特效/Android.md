目前，仅原移动直播企业版 SDK，短视频企业版 SDK 以及短视频企业版 Pro SDK 支持高级美颜特效，需要购买原 [移动直播企业版 License](https://cloud.tencent.com/document/product/454/8008)、[短视频企业版 License 或短视频企业版 Pro License](https://cloud.tencent.com/document/product/584/9368) 后，使用对应的功能。

## 功能说明

腾讯云直播团队与优图实验室、天天 P 图团队进行深度合作，结合 **AI 技术与美妆技术**，开发了**大眼、瘦脸、瘦鼻、动效贴纸、AI 抠背以及绿幕**等特效功能，并整合到 LiteAVSDK 的图像处理流程中，以实现更好的视频效果。
![](https://main.qcloudimg.com/raw/55b969c713b9d96f496bcab3d72e3850.png)

## 接入准备

### 1. 申请企业版 License

登录腾讯云，进入 [美颜特效服务开通申请页](https://cloud.tencent.com/product/x-magic)，如实填写相关信息并完成申请。
请着重检查 **iOS bundle ID** 和 **Android 应用包名称（package name）**信息是否填写正确，License 需要校验您的 App 安装包名称是否跟申请时一致。
![](https://main.qcloudimg.com/raw/db664311438d0449ef167776b9afcb42.png)

### 2. 下载企业版 SDK

下载并解压 [企业版 SDK](https://github.com/tencentyun/TRTCSDK/blob/master/SDK%E4%B8%8B%E8%BD%BD.md#%E4%BC%81%E4%B8%9A%E7%89%88-sdk-%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80) ，解压时需要解压密码，解压密码在申请 License 成功后即可获取，解压后的目录结构如下：

| 文件名称                     | 文件内容                                      |
| ---------------------------- | --------------------------------------------- |
| LiteAVSDK_Enterprise_xxx.aar | 企业版 SDK aar 文件，用于 aar 集成方式。      |
| LiteAVSDK_Enterprise_xxx.zip | 企业版 SDK zip 文件，用于 jar+so 的集成方式。 |

其中 LiteAVSDK_Enterprise_xxx.zip 解压后文件目录结构如下：

| 文件名称 | 文件内容                    |
| -------- | --------------------------- |
| assets   | 企业版 SDK 所需要的特效资源 |
| armeabi  | 企业版 SDK so 库            |
| \*.jar   | 企业版 SDK 所有的 jar 文件  |

### 3. 将 SDK 导入您的工程

<dx-tabs>
::: 方式一：aar集成方式
1. 将下载到的 arr 文件拷贝到工程的 app/libs 目录下。
![](https://main.qcloudimg.com/raw/d826e6842b947b113f26795270fafc30.png)
2. 在工程根目录下的 `build.gradle` 中，添加 **flatDir**，指定本地仓库路径。
![](https://main.qcloudimg.com/raw/5ba8aabbf657983c13b5b8dfe7fb9f20.png)
3. 添加 LiteAVSDK 依赖：
在 `app/build.gradle` 中，添加引用 aar 包的代码。
![](https://main.qcloudimg.com/raw/1511152637686ab9e6f46388ff879c76.png)
4. 在 `app/build.gradle` 的 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK 企业版支持 armeabi，armeabi-v7a，arm64-v8a 架构，x64 架构还在开发中）。
```
   defaultConfig {
        ndk {
            abiFilters "armeabi" , "armeabi-v7a" , "arm64-v8a"
        }
    }
```
5. 单击【Sync Now】，完成 LiteAVSDK 的集成工作。
:::
::: 方式二：jar集成方式
 若您不想集成 aar 库，也可以通过导入 jar 和 so 库的方式集成 LiteAVSDK：
1. 解压 `LiteAVSDK_Enterprise_xxx.zip` 文件。
    解压后得到 libs 目录，里面主要包含 jar 文件、 so 文件夹以及资源文件，文件清单如下：
   ![](https://main.qcloudimg.com/raw/f460962b610f2fd80f38ced46c26e5a5.png)
2. 将解压得到的 jar 文件和 armeabi 文件夹拷贝到 `app/libs` 目录下。
   ![](https://main.qcloudimg.com/raw/d9b6339cb52fb85afda42de6001be337.png)
3. 将解压得到的特效资源文件拷贝到 `app/src/main/assets` 目录下。
		- 6.6 之后的版本，assets 资源包被分包了，所以集成时不能简单的把 `assets-static`、`assets-dynamic` 里面的资源文件复制到工程的默认 assets 文件下，动效会无法识别资源。
		- 正确的做法是把 aar 包改成 zip 后缀，然后解压，里面有一个完整的 assets 资源包，把里面文件全复制到工程 assets 文件夹下，就可以正常集成了。
	![](https://main.qcloudimg.com/raw/65fc75c0001bbe4a5004f74e4d09e5d8.png)
4. 在工程根目录下的 `build.gradle` 中，添加 flatDir，指定本地仓库路径。
![](https://main.qcloudimg.com/raw/726771558714a2b4fae8dc1a59c33ffc.png)  
5. 在 `app/build.gradle` 中，添加引用 jar 库的代码。
 ![](https://main.qcloudimg.com/raw/5ec9d68dc37b40f3dc1bf5a9fcc36927.png)
6. 在 `app/build.gradle` 中，添加引用 so 库的代码。
![](https://main.qcloudimg.com/raw/7aa1e2872408ea2acd633c6323fae95e.png)
7. 在 `app/build.gradle` 的 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK 企业版支持 armeabi，armeabi-v7a，arm64-v8a 架构，x64 架构还在开发中）。
```
   defaultConfig {
        ndk {
            abiFilters "armeabi" , "armeabi-v7a" , "arm64-v8a"
        }
    }
```
 7. 单击【Sync Now】，完成 LiteAVSDK 的集成工作。
:::
</dx-tabs>

### 4. 给 SDK 配置 License 授权
申请 [企业版 License](https://cloud.tencent.com/document/product/454/34750) 成功后，您会获得两个字符串：licenseURL 和解密 key。在您的 App 调用企业版 SDK 相关功能前需进行如下设置：
>?建议配置在 Application 类中。

```java
public class MApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        String licenceURL = ""; // 获取到的 licenseURL
        String licenceKey = ""; // 获取到的 licence key
        TXLiveBase.getInstance().setLicence(this, licenceURL, licenceKey);
    }
}
```

### 5. 配置 App 权限

在 AndroidManifest.xml 中配置 App 的权限，SDK 需要以下权限：
```java
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-feature android:name="android.hardware.Camera"/>
<uses-feature android:name="android.hardware.camera.autofocus" /
```

### 6. 设置混淆规则

在 proguard-rules.pro 文件，将 SDK 相关类加入不混淆名单：
```java
-keep class com.tencent.** { *; }
```

### 7.  配置 App 打包参数
![](https://main.qcloudimg.com/raw/dabfd69ee06e4d38bb3b51fc436c0ad1.png)
如上图所示，在 App 的 build.gradle 中配置：

```
packagingOptions {
        pickFirst '**/libc++_shared.so'
        doNotStrip "*/armeabi/libYTCommon.so"
        doNotStrip "*/armeabi-v7a/libYTCommon.so"
        doNotStrip "*/x86/libYTCommon.so"
        doNotStrip "*/arm64-v8a/libYTCommon.so"
}
```

## 功能调用

### 高级美颜接口（大眼、瘦脸）

美妆接口使用 [TXBeautyManager](https://cloud.tencent.com/document/product/454/39382)，只需要对指定的接口调用0 - 9之间的一个数值即可，0表示关闭，数值越大，效果越明显。
<dx-codeblock>
::: java java
// 大眼
public void setEyeScaleLevel(int eyeScaleLevel);

// 瘦脸
public void setFaceSlimLevel(int faceScaleLevel);

// V 脸
public void setFaceVLevel(int faceVLevel);

// 调整下巴拉伸或收缩
public void setChinLevel(int chinLevel);

// 短脸
public void setFaceShortLevel(int faceShortlevel);

// 瘦鼻
public void setNoseSlimLevel(int noseSlimLevel);

// 亮眼
public void setEyeLightenLevel(int eyeLightenLevel);

// 白牙
public void setToothWhitenLevel(int toothWhitenLevel);

// 祛皱
public void setWrinkleRemoveLevel(int wrinkleRemoveLevel);

// 祛眼袋
public void setPounchRemoveLevel(int pounchRemoveLevel);

// 祛法令纹
public void setSmileLinesRemoveLevel(int smileLinesRemoveLevel);

// 调整发际线
public void setForeheadLevel(int foreheadLevel);

// 调整眼距
public void setEyeDistanceLevel(int eyeDistanceLevel);

// 调整眼角
public void setEyeAngleLevel(int eyeAngleLevel);

// 调整嘴型
public void setMouthShapeLevel(int mouthShapeLevel);

// 调整鼻翼
public void setNoseWingLevel(int noseWingLevel);

// 调整鼻子位置
public void setNosePositionLevel(int nosePositionLevel);

// 调整嘴唇厚度
public void setLipsThicknessLevel(int lipsThicknessLevel);

// 调整脸型
public void setFaceBeautyLevel(int faceBeautyLevel);
:::
</dx-codeblock>

[](id:beauty_dynamic)
### 美颜动效（动效贴纸、AI 抠图、美妆、手势）
购买美颜动效素材后，您可以获得对应效果的素材包。每一个素材包就是一个独立的目录，目录里包含了很多资源文件。每个素材包因其复杂度不同，文件数量和大小尺寸也各不相同。

为了节省安装包体积，我们建议您将素材包上传到您的服务器上，并将下载地址配置在您的 App 中，例如：`http://yourcompany.com/hudongzhibo/AISpecial/**/{动效名}.zip`。
在 App 启动后，下载并解压素材包到 Resource 目录下。完成解压后，即可通过以下接口开启动效效果：


```java
/**
 * 选择使用哪一款 AI 动效挂件（企业版有效，其它版本设置此参数无效）
 *
 * @param motionPath 动效所在路径
 */
public void setMotionTmpl(String motionPath);
```

### 绿幕功能

如果要使用绿幕功能，需要先让主播站在一个绿色背景前。开启绿幕功能以后，SDK 会识别出图像中的绿色区域，并将其替换成视频内容。
![](https://main.qcloudimg.com/raw/9af89ec09a300f49821e2b936cb9243d.png)
您需要先准备一个用于播放的 mp4 文件，然后通过调用如下接口即可开启绿幕效果：

```java
/**
 * 设置绿幕背景视频（企业版有效，其它版本设置此参数无效）
 *
 * 此处的绿幕功能并非智能抠背，它需要被拍摄者的背后有一块绿色的幕布来辅助产生特效。
 *
 * @param file 视频文件路径，支持 MP4。null 表示关闭特效。
 */
@TargetApi(18)
public boolean setGreenScreenFile(String file) {
    return mTXTxLivePusherImpl.setGreenScreenFile(file);
}
```

## 常见问题

### Licence 是否正常使用中？

License 设置成功后（需稍等一段时间，具体时间长短视网络情况而定），SDK 会下载 License 文件到手机。可以通过 TXLiveBase 的 getLicenceInfo() 方法查看 License 信息，包含 Licence 的生效和过期时间，绑定的 app package name 信息等。

```java
public void onCreate() {
      super.onCreate();
      String licenceURL = ""; // 获取到的 licenceURL
      String licenceKey = ""; // 获取到的 licenceKey
      TXLiveBase.getInstance().setLicence(this, licenceURL, licenceKey);// 设置 Licence
      
      // 打印 licence 信息
      Handler handler = new Handler(Looper.getMainLooper());
      handler.postDelayed(new Runnable() {
          @Override
          public void run() {
              Log.i(TAG, "onCreate: " + TXLiveBase.getInstance().getLicenceInfo(MApplication.this));
          }
      }, 5 * 1000);//5秒后打印 Licence 的信息
  }

```

若您需要其他协助，可将打印出来的 Licence 信息保存，并联系我们的技术支持。

### 集成遇到异常怎么解决？

```
java.lang.UnsatisfiedLinkError: No implementation found for void com.tencent.ttpic.util.youtu.YTFaceDetectorBase.nativeSetRefine(boolean) (tried Java_com_tencent_ttpic_util_youtu_YTFaceDetectorBase_nativeSetRefine and Java_com_tencent_ttpic_util_youtu_YTFaceDetectorBase_nativeSetRefine__Z)
        at com.tencent.ttpic.util.youtu.YTFaceDetectorBase.nativeSetRefine(Native Method)
```

请检查 build.gradle 中是否存在如下配置，如果您的项目存在多层 module 结构，例如 app module 引用了 lvb module，lvb module 中引用了腾讯云 SDK，那么您需要在 app module 和 lvb module 中都添加如下配置。

```
packagingOptions {
        pickFirst '**/libc++_shared.so'
        doNotStrip "*/armeabi/libYTCommon.so"
        doNotStrip "*/armeabi-v7a/libYTCommon.so"
        doNotStrip "*/x86/libYTCommon.so"
        doNotStrip "*/arm64-v8a/libYTCommon.so"
}
```

添加配置后，请先 clean 工程再重新 build。

### 美容（例如大眼瘦脸）、动效等功能不起作用怎么解决？

1. 请检查移动直播 Licence 的有效期`TXLiveBase.getInstance().getLicenceInfo(mContext)`。
2. 请检查优图实验室 Licence 有效期（购买时通过商务获取）。
3. 请检查您下载的 SDK 版本是否为企业版 SDK（移动直播只有企业版支持 AI 特效）。
    如果您调用接口时发现不生效，请查看 Logcat 是否存在 log 为：`support EnterPrise above!!!`；如果存在，说明下载的 SDK 版本和您使用的 Licence 版本不匹配。

>! 美颜动效请使用最新接口`TXLivePusher getBeautyManager()`。

[查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) 是一个 xcode 工程，目前仅支持在 Mac 上使用，后续会开放其他查询方式。

### 采用动态加载 jar + so 方式集成注意事项
```
YTFaceDetectorBase: (GLThread 5316)
com.tencent.ttpic.util.youtu.YTFaceDetectorBase(54)[c]: nativeInitCommon, ret = -2
YTFaceDetectorBase: (GLThread 5316)com.tencent.ttpic.util.youtu.YTFaceDetectorBase(57)[c]: nativeInitCommon failed, ret = -1001
YTFaceDetectorBase: (GLThread 5316)com.tencent.ttpic.util.youtu.YTFaceDetectorBase(26)[a]: initCommon, ret = -1001
YTFaceDetectorBase: (GLThread 5316)com.tencent.ttpic.util.youtu.YTFaceDetectorBase(28)[a]: initCommon failed, ret = -1001
```
**若您出现以上问题，请检查如下几点：**
1. 检查动态下发的 so 包个数是否存在下发不全的情况，通过`TXLiveBase.setLibraryPath(soPath)`，设置 so 包地址。
>! 不可以部分放到本地，部分动态下发，只能全部动态下发或全部本地集成。
2. jar + so 方式解压开资源分为`assets-static`和`assets-dynamic`两类，其中`assets-static`只能放到本地，不可以动态下发，`asset-dynamic`需要保证动态下发跟 so 同一个目录下。
3. SDK 6.8 以后，不要自己通过系统的方法加载 so 包，SDK 内部会保证 so 包的加载顺序。
