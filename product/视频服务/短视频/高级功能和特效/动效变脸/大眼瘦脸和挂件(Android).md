目前，仅原移动直播企业版 SDK，短视频企业版 SDK 以及短视频企业版 Pro SDK 支持高级美颜特效，需要购买原 [移动直播企业版 License](https://cloud.tencent.com/document/product/454/8008)、[短视频企业版 License 或短视频企业版 Pro License](https://cloud.tencent.com/document/product/584/9368) 后，使用对应的功能。

## 功能说明

大眼、瘦脸、动效贴纸、绿幕等特效功能，是基于优图实验室的 AI 识别技术和天天 P 图的美妆技术为基础开发的特权功能，腾讯云小视频团队通过跟优图和 P 图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。

## 接入流程

[单击此处](https://cloud.tencent.com/product/x-magic) 申请企业版本 License。

## 版本下载

在 [SDK 开发包](https://cloud.tencent.com/document/product/454/7873) 页面下方下载商用版本 SDK 压缩包，压缩包有加密（解压密码和 Licence 文件 可以跟我们的商务同学获取）, 成功解压后在 SDK 目录下得到一个 `aar` 和 `zip`，分别对应两种集成方式。

## 工程设置

具体操作请参见 [工程配置](https://cloud.tencent.com/document/product/584/11631)。 

### 添加 SDK

#### 使用 aar 方式集成

直接替换工程中的非企业版的 aar，并在 app 目录下的 build.gradle 中修改对应的名称即可。

#### 使用 jar 包方式集成

1. 需要解压 zip，把 libs 下的 so 拷贝到您的 jni 加载路径下。其中跟动效有关的 so 如下：
<table>
<thead>
<tr>
<th>so</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody><tr>
<td>libYTCommon.so</td>
<td>libnnpack.so</td>
<td>libpitu_device.so</td>
</tr>
<tr>
<td>libpitu_tools.so</td>
<td>libWXVoice.so</td>
<td>libgameplay.so</td>
</tr>
<tr>
<td>libCameraFaceJNI.so</td>
<td>libYTFaceTrackPro.so</td>
<td>libimage_filter_gpu.so</td>
</tr>
<tr>
<td>libimage_filter_common.so</td>
<td>libpitu_voice.so</td>
<td>libvoicechanger_shared.so</td>
</tr>
<tr>
<td>libParticleSystem.so</td>
<td>libYTHandDetector.so</td>
<td>libGestureDetectJni.so</td>
</tr>
<tr>
<td>libsegmentern.so</td>
<td></td>
<td></td>
</tr>
</tbody></table>
2. 把解压后的 assets 文件夹下的所有资源拷贝到工程的 assets 目录下，包括 asset 根目录下的文件和 camera 文件夹下的文件。

### 导入 License 文件

商用版需要 License 验证通过后，相应功能才能生效。您可以向我们的商务同学申请一个免费30天的调试用 License。
得到 Licence 后，您需要将其命名为 **YTFaceSDK.licence**，放到工程的 assets 目录下。
>!
>- 每个 License 都有绑定具体的 package name，修改 App 的 package name 会导致验证失败。
>- YTFaceSDK.licence 的文件名固定，不可修改、且必须放在 assets 目录下。
>- iOS 和 Android 不需要重复申请 Licence，一个 License 可以同时授权一个 iOS 的 BundleID 和一个 Android 的 PackageName。


**从9.4版本开始，SDK 支持二合一的 License，这种方式不再需要 YTFaceSDK.licence，在从商务同学处获取到 License 对应的 Key 和 URL 后，设置方式和标准版 License 设置方式相同。**

## 功能调用

### 动效功能

<img src="https://main.qcloudimg.com/raw/487dc3482f0ab432a3e8eccf8b9ba5d4.png" width="300">

一个动效模板是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数以和文件大小也不尽相同。
Demo 中的示例代码是从后台下载动效资源，再统一解压到 sdcard。您可以在 Demo 代码中找到动效资源的下载地址，格式如下：
```
http://dldir1.qq.com/hudongzhibo/AISpecial/Android/156/(动效name).zip
```
>?建议您将动效资源放在自己的服务器上，以防 Demo 变动造成不必要的影响。

当解压完成后，即可通过以下接口开启动效效果。
```
/**
 * setMotionTmpl 设置动效贴图文件位置
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```

### AI 抠背

<img src="https://main.qcloudimg.com/raw/996d47fa97f4b13ac020efacedc15b8d.png" width="300">

需要下载 AI 抠背的资源，接口跟动效接口相同。

```
/**
 * setMotionTmpl 设置动效贴图文件位置
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```

### 高级美颜接口（大眼、瘦脸等）

```
// 大眼效果 0~9
mTXCameraRecord.getBeautyManager().setEyeScaleLevel(eyeLevel);
// 瘦脸效果 0~9
mTXCameraRecord.getBeautyManager().setFaceSlimLevel(faceSlimLevel);
// V脸效果 0~9
 mTXCameraRecord.getBeautyManager().setFaceVLevel(faceVLevel);
// 下巴拉伸或收缩效果 0~9
mTXCameraRecord.getBeautyManager().setChinLevel(chinSlimLevel);
// 缩脸效果 0~9
mTXCameraRecord.getBeautyManager().setFaceShortLevel(faceShortLevel);
// 瘦鼻效果 0~9
mTXCameraRecord.getBeautyManager().setNoseSlimLevel(noseScaleLevel);
// 亮眼效果 0~9
mTXCameraRecord.getBeautyManager().setEyeLightenLevel(eyeLightenLevel);
// 白牙效果 0~9
mTXCameraRecord.getBeautyManager().setToothWhitenLevel(toothWhitenLevel);
// 祛皱效果 0~9
mTXCameraRecord.getBeautyManager().setWrinkleRemoveLevel(wrinkleRemoveLevel);
// 祛眼袋效果 0~9
mTXCameraRecord.getBeautyManager().setPounchRemoveLevel(pounchRemoveLevel);
// 祛法令纹效果 0~9
mTXCameraRecord.getBeautyManager().setSmileLinesRemoveLevel(smileLinesRemoveLevel);
// 调整发际线 0~9
mTXCameraRecord.getBeautyManager().setForeheadLevel(foreheadLevel);
// 调整眼间距 0~9
mTXCameraRecord.getBeautyManager().setEyeDistanceLevel(eyeDistanceLevel);
// 调整眼角 0~9
mTXCameraRecord.getBeautyManager().setEyeAngleLevel(eyeAngleLevel);
// 调整嘴形 0~9
mTXCameraRecord.getBeautyManager().setMouthShapeLevel(mouthShapeLevel);
// 调整鼻翼 0~9
mTXCameraRecord.getBeautyManager().setNoseWingLevel(noseWingLevel);
// 调整鼻子位置 0~9
mTXCameraRecord.getBeautyManager().setNosePositionLevel(nosePositionLevel);
// 调整嘴唇厚度 0~9
mTXCameraRecord.getBeautyManager().setLipsThicknessLevel(lipsThicknessLevel);
// 调整脸型 0~9
mTXCameraRecord.getBeautyManager().setFaceBeautyLevel(faceBeautyLevel);
```

### 绿幕功能

使用绿幕需要先准备一个用于播放的 MP4 文件，通过调用以下接口即可开启绿幕效果。

```
/**
 * 设置绿幕文件:目前图片支持 jpg/png，视频支持 mp4/3gp 等 Android 系统支持的格式
 * API 要求18
 * @param path ：绿幕文件位置，支持两种方式：
 *             1.资源文件放在 assets 目录，path 直接取文件名
 *             2.path 取文件绝对路径
 */
@TargetApi(18)
public void setGreenScreenFile(String path);
```

## 问题排查              
### 1. License 是否正常使用中？
License 设置成功后（需等待一段时间，具体时间视网络情况而定），SDK 会下载 License 文件到手机。可以通过 TXUGCBase 的 getLicenceInfo() 方法查看 Licence 信息，包含 License 的生效和过期时间，绑定的 app package name 信息等。

```java
public void onCreate() {
      super.onCreate();
      String licenceURL = ""; // 获取到的 licenceURL
      String licenceKey = ""; // 获取到的 licenceKey
      TXUGCBase.getInstance().setLicence(this, licenceURL, licenceKey);// 设置 Licence
      
      // 打印 licence 信息
      Handler handler = new Handler(Looper.getMainLooper());
      handler.postDelayed(new Runnable() {
          @Override
          public void run() {
              Log.i(TAG, "onCreate: " + TXUGCBase.getInstance().getLicenceInfo(MApplication.this));
          }
      }, 5 * 1000);//5秒后打印 Licence 的信息
  }

```

若您需要其他协助，可将打印出来的 License 信息保存，并联系我们的 [技术支持](https://cloud.tencent.com/document/product/584/9374)。

### 2. 集成遇到异常怎么解决？
```
java.lang.UnsatisfiedLinkError: No implementation found for void com.tencent.ttpic.util.youtu.YTFaceDetectorBase.nativeSetRefine(boolean) (tried Java_com_tencent_ttpic_util_youtu_YTFaceDetectorBase_nativeSetRefine and Java_com_tencent_ttpic_util_youtu_YTFaceDetectorBase_nativeSetRefine__Z)
        at com.tencent.ttpic.util.youtu.YTFaceDetectorBase.nativeSetRefine(Native Method)
```

请检查项目 build.gradle 中是否存在多层 module 结构。例如，app module 引用了 ugckit module，ugckit module 引用了腾讯云 SDK，则您需要在 app module 和 ugckit 的 module 中添加如下配置：

```
packagingOptions {
        pickFirst '**/libc++_shared.so'
        doNotStrip "*/armeabi/libYTCommon.so"
        doNotStrip "*/armeabi-v7a/libYTCommon.so"
        doNotStrip "*/x86/libYTCommon.so"
        doNotStrip "*/arm64-v8a/libYTCommon.so"
}
```

添加配置后，请 clean 工程后再重新 build。

### 3. 美容（例如大眼瘦脸）、动效等功能不起作用怎么解决？
- 检查移动直播 License 的有效期 `TXUGCBase.getInstance().getLicenceInfo(mContext)`。
- 检查优图实验室 License 有效期（购买时通过商务获取）。
- 检查您下载的 SDK 版本和购买的 SDK 版本是否一致。

移动直播只有 [企业版](https://cloud.tencent.com/product/x-magic) 支持 AI 特效（大眼瘦脸、V 脸隆鼻、动效贴纸、绿幕抠图）。

如果您调用接口发现不生效，请查看 Logcat 是否存在 log：`support EnterPrise above!!!`。如果存在，说明下载的 SDK 版本和您使用的 Licence 版本不匹配。
>!美颜动效请使用最新接口`TXUGCRecord getBeautyManager()`。

[查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) 可以查询 License 的有效期，是一个 xcode 工程，目前仅支持在 mac 上使用，后续会开放其他查询方式。

### 4. 采用动态加载 jar + so 方式集成需要注意什么？

- 检查动态下发的 so 包个数是否存在下发不全的情况，通过 `TXLiveBase.setLibraryPath(soPath);` 设置 so 包地址。
>!不可以一部分放在本地，一部分动态下发，只能全部动态下发或全部本地集成。
- jar + so 方式解压后的资源分为 `assets-static`和`assets-dynamic` 两类，其中 `assets-static` 只能放在本地，不可以动态下发，`asset-dynamic` 需要保证动态下发，跟 so 同一个目录下。
- SDK 6.8 以后，请不要人为通过系统的方法加载 so 包，SDK 内部会保证 so 包的加载顺序。

如果您出现以下问题，请按上述几点进行检查。

```
YTFaceDetectorBase: (GLThread 5316)
com.tencent.ttpic.util.youtu.YTFaceDetectorBase(54)[c]: nativeInitCommon, ret = -2
YTFaceDetectorBase: (GLThread 5316)com.tencent.ttpic.util.youtu.YTFaceDetectorBase(57)[c]: nativeInitCommon failed, ret = -1001
YTFaceDetectorBase: (GLThread 5316)com.tencent.ttpic.util.youtu.YTFaceDetectorBase(26)[a]: initCommon, ret = -1001
YTFaceDetectorBase: (GLThread 5316)com.tencent.ttpic.util.youtu.YTFaceDetectorBase(28)[a]: initCommon failed, ret = -1001
```
