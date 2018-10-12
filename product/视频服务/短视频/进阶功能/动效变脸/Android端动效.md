# 特效功能（大眼、瘦脸、动效、绿幕等）

## 功能说明

大眼、瘦脸、动效贴纸、绿幕等特效功能，是基于优图实验室的人脸识别技术和天天P图的美妆技术为基础开发的特权功能，腾讯云小视频团队通过跟优图和P图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。

## 接入流程

申请步骤如下：

1. 提工单或客服电话（400-9100-100）联系我们商务同学。

2. 下载[示例表格](https://mc.qcloudimg.com/static/archive/766c9092424d0440a31c56c81f34a629/archive.xlsx)，按照表格填好信息后，邮件发送到 jerryqian@tencent.com 并抄送给您联系的商务同学（重要）。

3. 敦促商务同学回复邮件确认，未经腾讯云商务同学确认的邮件，我们可能会视为骚扰邮件不予处理。

4. 确认后，我们会第一时间替您向优图实验室申请试用 Licence，并同压缩包解压密码一起发给您。

   Licence 有两种：

   - 试用Licence：**有效期为一个月**，用于调试和测试动效SDK，如果您用试用Licence发布了您的应用，会导致有效期过后动效的功能不可用。
   - 正式Licence：有效期根据最终的合同而定，一般为一年。

## 版本下载

可以到 [SDK 开发包](https://cloud.tencent.com/document/product/454/7873) 页面下方下载商用版本 SDK 压缩包，压缩包有加密（解压密码 & Licence文件 可以跟我们的商务同学获取）, 成功解压后得到一个`LiteAVSDK_Enterprise_3.9.2749.aar`和`LiteAVSDK_Enterprise_3.9.2749.zip`，分别对应两种集成方式。

## 工程设置

参考 [工程配置](https://cloud.tencent.com/document/product/584/11631) 

### 添加SDK

#### 使用aar方式集成

直接把LiteAVSDK_Enterprise_3.9.2749.aar替换你工程中的非商业版的aar，并在app目录下的build.gradle中修改对应的名称即可，相对简单

#### 使用jar包方式集成

1. 需要解压LiteAVSDK_Enterprise_3.9.2749.zip，把libs下的jar包和so拷贝到你的jni加载路径下。其中跟动效有关的jar包和so如下：


| jar                     |                          |                   |
| ----------------------- | ------------------------ | ----------------- |
| filterengine.bundle.jar | ptu_algo_cb6bc16f389.jar | segmenter-lib.jar |
| video_module.jar        | YTCommon.jar             |                   |

| so                     |                           |                        |
| ---------------------- | ------------------------- | ---------------------- |
| libalgo_rithm_jni.so   | libalgo_youtu_jni.so      | libformat_convert.so   |
| libGestureDetectJni.so | libimage_filter_common.so | libimage_filter_gpu.so |
| libnnpack.so           | libParticleSystem.so      | libpitu_tools.so       |
| libsegmentern.so       | libsegmentero.so          | libYTCommon.so         |
| libYTFaceTrackPro.so   | libYTHandDetector.so      | libYTIllumination.so   |

2. 把解压后的assets文件夹下的资源拷贝到你的工程的assets目录下，包括asset根目录下的文件和camera文件夹下的文件

### 导入licence文件

商用版需要 licence 验证通过后，相应功能才能生效。您可以向我们的商务同学申请一个免费 30 天的调试用 Licence。
得到 licence 后，您需要将其命名为**YTFaceSDK.licence**，放到工程的assets目录下。

> 每个licence都有绑定具体的package name，修改app的package name会导致验证失败。
>
> YTFaceSDK.Licence的文件名固定，不可修改、且必须放在assets目录下。
>
> iOS 和 Android 不需要重复申请 Licence，一个 Licence 可以同时授权一个 iOS 的 bundleid 和一个 Android 的packageName。

## 功能调用

### 1.动效功能

示例：

![](https://mc.qcloudimg.com/static/img/a320624ee8d3a82ee07feb05969e5290/A8B81CB6-DBD3-4111-9BF0-90BD02779BFC.png)

一个动效模版是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数以和文件大小也不尽相同。

DEMO中的示例代码是从后台下载动效资源，再统一解压到sdcard。您可以在DEMO代码中找到动效资源的下载地址，格式如下

> ```
> http://dldir1.qq.com/hudongzhibo/AISpecial/Android/156/(动效name).zip
> ```

强烈建议客户将动效资源放在自己的服务器上，以防DEMO变动造成不必要的影响。

当解压完成后，即可通过以下接口开启动效效果

```
/**
 * setMotionTmpl 设置动效贴图文件位置
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```

### 2. AI抠背

示例：

![](https://mc.qcloudimg.com/static/img/0f79b78687753f88af7685530745a8d4/98B403B8-1DEC-4130-B691-D9EB5E321162.png)

需要下载AI抠背的资源，接口跟动效接口相同

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
mTXCameraRecord.setEyeScaleLevel(eyeScaleLevel);
// 瘦脸效果 0~9
mTXCameraRecord.setFaceScaleLevel(faceScaleLevel);
// V脸效果 0~9
mTXCameraRecord.setFaceVLevel(level)
// 下巴拉伸或收缩效果 0~9
mTXCameraRecord.setChinLevel(scale)
// 缩脸效果 0~9
mTXCameraRecord.setFaceShortLevel(level)
// 瘦鼻效果 0~9
mTXCameraRecord.setNoseSlimLevel(scale)
```

### 4. 绿幕功能

使用绿幕需要先准备一个用于播放的mp4文件，通过调用以下接口即可开启绿幕效果

```
/**
 * 设置绿幕文件:目前图片支持jpg/png，视频支持mp4/3gp等Android系统支持的格式
 * API要求18
 * @param path ：绿幕文件位置，支持两种方式：
 *             1.资源文件放在assets目录，path直接取文件名
 *             2.path取文件绝对路径
 */
@TargetApi(18)
public void setGreenScreenFile(String path);
```

## 问题排查              
### 1. 工程运行过程中crash？  
 > 1. 检查build.gradle设置，abiFilters是否设置为armeabi，目前只支持armeabi架构
 > > 2. 如果是jar集成方式，检查动效对应的so是否都考到工程jniLibs目录下

### 2. 工程特效不生效？  
 > 1. 检查YTFaceSDK.licence 命名是否正确，YTFaceSDK.licence必须放在assets根目录下  
 > > 2. 检查licence是否过期（下载[查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)或则联系我们的开发同学）    
 > > 3. 如果是jar集成方式，检查pitu资源是否添加正确（sdk解压出来的assets目录内容都要拷贝到工程的assets目录下）  
 > > 4. 如果客户更新了licence，请确保使用的是最新的licence，如果不确定，可以查下licence的有效期（下载[查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)或则联系我们开发同学)，另外如果工程更换了licence，请先clean工程，删除本地安装包，重新编译       

##### [查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)是一个xcode工程，目前仅支持在mac上使用， 后续会开放其他查询方式