## 功能说明
腾讯云直播团队与优图实验室、天天 P 图团队进行深度合作，结合**人脸识别技术与美妆技术**，开发了**大眼、瘦脸、瘦鼻、动效贴纸、AI 抠背以及绿幕**等特效功能，并整合到 LiteAVSDK 的图像处理流程中，以实现更好的视频效果。
![](https://main.qcloudimg.com/raw/6fa6d2c76e389ddaaf2540f547061b90.jpg)

## 接入准备

### 1. 申请商业版 License

登录 [美颜特效 SDK（优图美视）控制台](https://cloud.tencent.com/product/x-magic) ，单击【立即申请】，如实填写相关信息并完成申请。
请着重检查 **iOS bundle ID** 和 **Android 应用包名称（package name）**信息是否填写正确，License 需要校验您的 App 安装包名称是否跟申请时一致。
![](https://main.qcloudimg.com/raw/66660d7082f1615b71b37f6fcea57642.png)

### 2. 下载商业版 SDK

下载并解压 [商业版 SDK](https://github.com/tencentyun/TRTCSDK/blob/master/SDK%E4%B8%8B%E8%BD%BD.md#%E4%BC%81%E4%B8%9A%E7%89%88-sdk-%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80) ，解压时需要解压密码，解压密码在申请 License 成功后即可获取，解压后的目录结构如下：

| 文件名称                     | 文件内容                                      |
| ---------------------------- | --------------------------------------------- |
| LiteAVSDK_Enterprise_xxx.aar | 商业版 SDK aar 文件，用于 aar 集成方式。      |
| LiteAVSDK_Enterprise_xxx.zip | 商业版 SDK zip 文件，用于 jar+so 的集成方式。 |

其中 LiteAVSDK_Enterprise_xxx.zip 解压后文件目录结构如下：

| 文件名称 | 文件内容                    |
| -------- | --------------------------- |
| assets   | 商业版 SDK 所需要的特效资源 |
| armeabi  | 商业版 SDK so 库            |
| \*.jar   | 商业版 SDK 所有的 jar 文件  |

### 3. 将 SDK 导入您的工程

- **方式一：aar 集成方式**

 1.将下载到的 arr 文件拷贝到工程的 app/libs 目录下。
  ![](https://main.qcloudimg.com/raw/d826e6842b947b113f26795270fafc30.png)
 2.在工程根目录下的 build.gradle 中，添加 **flatDir**，指定本地仓库路径。
  ![](https://main.qcloudimg.com/raw/5ba8aabbf657983c13b5b8dfe7fb9f20.png)
 3.添加 LiteAVSDK 依赖：  
  在 app/build.gradle 中，添加引用 aar 包的代码。
  ![](https://main.qcloudimg.com/raw/1511152637686ab9e6f46388ff879c76.png)
 4.在 app/build.gradle 的 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK 商业版支持 armeabi  和 armeabi-v7a 架构，x64 架构还在开发中）。
```
   defaultConfig {
        ndk {
            abiFilters "armeabi" , "armeabi-v7a"
        }
    }
```

 5.单击【Sync Now】，完成 LiteAVSDK 的集成工作。

- **方式二：jar 集成方式**
 若您不想集成 aar 库，也可以通过导入 jar 和 so 库的方式集成 LiteAVSDK：
 1.解压 LiteAVSDK_Enterprise_xxx.zip 文件。
  解压后得到 libs 目录，里面主要包含 jar 文件、 so 文件夹以及资源文件，文件清单如下：
  ![](https://main.qcloudimg.com/raw/11370b61f1e4b2ebbcebb0d904f98d40.png)
 2.将解压得到的 jar 文件和 armeabi 文件夹拷贝到 app/libs 目录下。
  ![](https://main.qcloudimg.com/raw/54976997e5e6000393a419b925273872.png)
 3.将解压得到的特效资源文件拷贝到 app/src/main/assets 目录下。
  ![](https://main.qcloudimg.com/raw/734797453f3d00b99e3bcd3fd810f869.png)
 4.在 app/build.gradle 中，添加引用 jar 库的代码。
  ![](https://main.qcloudimg.com/raw/5ec9d68dc37b40f3dc1bf5a9fcc36927.png)			
 5.在 app/build.gradle 中，添加引用 so 库的代码。
  ![](https://main.qcloudimg.com/raw/7aa1e2872408ea2acd633c6323fae95e.png)
 6.在 app/build.gradle 的 defaultConfig 中，指定 App 使用的 CPU 架构（目前 LiteAVSDK 商业版支持 armeabi  和 armeabi-v7a 架构，x64 架构还在开发中）。
```
   defaultConfig {
        ndk {
            abiFilters "armeabi" , "armeabi-v7a"
        }
    }
```

7.单击【Sync Now】，完成 LiteAVSDK 的集成工作。

### 4. 给 SDK 配置 License 授权
申请商业版 License 成功后，您会获得两个字符串：licenseURL 和解密 key。在您的 App 调用商业版 SDK 相关功能前需进行如下设置：
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

## 功能接口

### 美妆接口（大眼、瘦脸）

美妆接口的调用比较简单，只需要对指定的接口调用0 - 9之间的一个数值即可，0表示关闭，数值越大，效果越明显。

```java
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
```

### AI 贴纸

购买商业版 License 后，您可以获得20个 AI 贴纸素材包。每一个素材包就是一个独立的目录，目录里包含了很多资源文件。每个素材包因其复杂度不同，文件数量和大小尺寸也各不相同。
为了节省安装包体积，我们建议您将素材包上传到您的服务器上，并将下载地址配置在您的 App 中，例如：`http://yourcompany.com/hudongzhibo/AISpecial/**/{动效名}.zip`。
在 App 启动后，下载并解压素材包到手机任意目录（推荐下载并解压在 App 的 data 目录）。完成解压后，即可通过以下接口开启动效效果：
```java
/**
 * 选择使用哪一款 AI 动效挂件（商业版有效，其它版本设置此参数无效）
 *
 * @param motionPath 动效所在路径
 */
public void setMotionTmpl(String motionPath);
```

### 绿幕功能

如果要使用绿幕功能，需要先让主播站在一个绿色背景前。开启绿幕功能以后，SDK 会识别出图像中的绿色区域，并将其替换成视频内容。
![](https://main.qcloudimg.com/raw/f1b345135deb4c01ed2a691958ce34f2.jpg)
您需要先准备一个用于播放的 mp4 文件，然后通过调用如下接口即可开启绿幕效果：

```java
/**
 * 设置绿幕背景视频（商业版有效，其它版本设置此参数无效）
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

### LiteAVSDK 商业版是否支持 arm64 ？

目前商业版 SDK 由于特效处理库尚不支持 arm64 下的一些汇编指令，所以暂时还不支持 arm64 架构，请注意指定 App 的架构配置。
>?x64 架构还在开发中。
	
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
