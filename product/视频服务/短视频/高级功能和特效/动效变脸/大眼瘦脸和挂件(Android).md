

## 功能说明

大眼、瘦脸、动效贴纸、绿幕等特效功能，是基于优图实验室的人脸识别技术和天天 P 图的美妆技术为基础开发的特权功能，腾讯云小视频团队通过跟优图和 P 图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。

## 接入流程

[单击此处](https://cloud.tencent.com/product/x-magic) 申请企业版本 License。

## 版本下载

在 [SDK 开发包](https://cloud.tencent.com/document/product/454/7873) 页面下方下载商用版本 SDK 压缩包，压缩包有加密（解压密码和 licence 文件 可以跟我们的商务同学获取）, 成功解压后在 SDK 目录下得到一个`aar`和`zip`，分别对应两种集成方式。

## 工程设置

参考 [工程配置](https://cloud.tencent.com/document/product/584/11631)。 

### 添加 SDK

#### 使用 aar 方式集成

直接替换工程中的非企业版的 aar，并在 app 目录下的 build.gradle 中修改对应的名称即可。

#### 使用 jar 包方式集成

1. 需要解压 zip，把 libs 下的 so 拷贝到您的 jni 加载路径下。其中跟动效有关的 so 如下：

| so                        |                      |                           |
| ------------------------- | -------------------- | ------------------------- |
| libYTCommon.so            | libnnpack.so         | libpitu_device.so         |
| libpitu_tools.so          | libWXVoice.so        | libgameplay.so            |
| libCameraFaceJNI.so       | libYTFaceTrackPro.so | libimage_filter_gpu.so    |
| libimage_filter_common.so | libpitu_voice.so     | libvoicechanger_shared.so | 
| libParticleSystem.so      | libYTHandDetector.so | libGestureDetectJni.so    |
| libsegmentern.so          |||

2. 把解压后的 assets 文件夹下的所有资源拷贝到工程的 assets 目录下，包括 asset 根目录下的文件和 camera 文件夹下的文件。

### 导入 licence 文件

商用版需要 licence 验证通过后，相应功能才能生效。您可以向我们的商务同学申请一个免费30天的调试用 licence。
得到 licence 后，您需要将其命名为 **YTFaceSDK.licence**，放到工程的 assets 目录下。
>!
>- 每个 licence 都有绑定具体的 package name，修改 app 的 package name 会导致验证失败。
>- YTFaceSDK.licence 的文件名固定，不可修改、且必须放在 assets 目录下。
>- iOS 和 Android 不需要重复申请 licence，一个 licence 可以同时授权一个 iOS 的 bundleid 和一个 Android 的 packageName。


**从4.9版本开始，SDK 支持二合一的 licence, 这种方式不再需要 YTFaceSDK.licence, 在从商务同学处获取到 licence 对应的 key 和 url 后，设置方式和标准版 licence 设置方式相同。**

## 功能调用

### 1. 动效功能

示例：
![](https://mc.qcloudimg.com/static/img/a320624ee8d3a82ee07feb05969e5290/A8B81CB6-DBD3-4111-9BF0-90BD02779BFC.png)
一个动效模版是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数以和文件大小也不尽相同。
Demo 中的示例代码是从后台下载动效资源，再统一解压到 sdcard。您可以在 Demo 代码中找到动效资源的下载地址，格式如下
> ```
> http://dldir1.qq.com/hudongzhibo/AISpecial/Android/156/(动效name).zip
> ```

>?强烈建议客户将动效资源放在自己的服务器上，以防 Demo 变动造成不必要的影响。

当解压完成后，即可通过以下接口开启动效效果。
```
/**
 * setMotionTmpl 设置动效贴图文件位置
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```

### 2. AI 抠背

示例：
![](https://mc.qcloudimg.com/static/img/0f79b78687753f88af7685530745a8d4/98B403B8-1DEC-4130-B691-D9EB5E321162.png)
需要下载 AI 抠背的资源，接口跟动效接口相同。

```
/**
 * setMotionTmpl 设置动效贴图文件位置
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```

### 3. 美妆美容

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

### 4. 绿幕功能

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
### 1. 工程运行过程中 crash？  
 > 1. 检查 build.gradle 设置，目前只支持 armeabi、armeabi-v7a、arm64-v8a 架构。
 > 2. 如果是 jar 集成方式，检查动效对应的 so 是否都拷到工程 jniLibs 目录下。
     
### 2. 工程特效不生效？  
 > 1. 检查是否调用了`TXUGCBase.getInstance().setLicence(Context context, String url, String key)`方法, 以及参数是否正确。 
 > 2. 调用 TXUGCBase 的 getLicenseInfo 方法，带有动效的 licence 会包含`pituLicense`字段。
 > 3. 如果是 jar 集成方式，检查 pitu 资源是否添加正确（SDK 解压出来的 assets 目录内容都要拷贝到工程的 assets 目录下）。
 > 4. SDK 会把 P 图的 licence 保存到`/sdcard/android/data/您的应用包名/files/YTFaceSDK.licence`，可以查询 licence 的有效期（下载 [查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) 或 [联系我们](https://cloud.tencent.com/document/product/584/9374))，另外如果工程更换了 licence，请先 clean 工程，删除本地安装包，重新编译。       
 [查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) 是一个 xcode 工程，目前仅支持在 mac 上使用，后续会开放其他查询方式。
