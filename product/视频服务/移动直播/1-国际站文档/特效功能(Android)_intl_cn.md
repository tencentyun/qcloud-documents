# 特效功能（大眼、瘦脸、动效、绿幕）

## 功能说明
大眼、瘦脸、动效贴纸、绿幕等特效功能，是基于优图实验室的人脸识别技术和天天P图的美妆技术为基础开发的特权功能，腾讯云小直播团队通过跟优图和P图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。

## 费用说明
由于采用了优图实验室的专利技术，授权费用约 **50W/年**（目前国内同类图像处理产品授权均在百万左右）。如有需要可以提工单或客服电话（400-9100-100）联系我们，商务同学会提供压缩包解码密码，并替您向优图实验室申请试用 License。

## 版本下载
可以到 [RTMP SDK 开发包](https://cloud.tencent.com/document/product/454/7873) 页面下方下载特权版 SDK 压缩包，压缩包有加密（解压密码 & license文件 可以跟我们的商务同学获取）, 成功解压后得到一个`txrtmpsdk.jar`和`libtxrtmpsdk.so`等几个so，替换你工程中的非特权版jar和so即可。

## 工程设置

### 1. 添加SDK
拷贝SDK里面的txrtmpsdk.jar和libtxrtmpsdk.so等so到工程对应位置，如libs下
> 注意：特权版只支持armeabi架构的so，请删除app里面的其余架构so，避免so加载失败

### 2. 添加资源
将zip包中的`camera`文件夹拷贝到工程的assets目录下
> 注意：camera目录包含了切换动效需要的资源等文件，必须正确放到assets目录下，否则会发生异常

### 3. 导入licence文件
特权版需要 licence 验证通过后，相应功能才能生效。您可以向我们的商务同学申请一个免费 30 天的调试用 license。
得到 licence 后，您需要将其命名为**YTFaceSDK.licence**，工程的assets目录下。

> 每个licence都有绑定具体的package name，修改app的package name会导致验证失败。
>
> YTFaceSDK.license的文件名固定，不可修改、且必须放在assets目录下。
> 
> iOS 和 Android 不需要重复申请 license，一个 license 可以同时授权一个 iOS 的 bundleid 和一个 Android 的packageName。

## 功能调用

### 1. 动效功能

一个动效模版是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数以和文件大小也不尽相同。

小直播中的示例代码是从后台下载动效资源，再统一解压到Resource目录。您可以在小直播代码中找到动效资源和动效缩略图的下载地址，格式如下

> https://st1.xiangji.qq.com/yunmaterials/{动效id}Android.zip
>
> https://st1.xiangji.qq.com/yunmaterials/{动效id}.png
>

强烈建议客户将动效资源放在自己的服务器上，以防小直播变动造成不必要的影响。

当解压完成后，即可通过以下接口开启动效效果

```java
/**
 * setMotionTmpl 设置动效贴图文件位置
 * @param tmplPath
 */
public void setMotionTmpl(String tmplPath);
```


### 2. 绿幕功能

使用绿幕需要先准备一个用于播放的mp4文件，通过调用以下接口即可开启绿幕效果

```java
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


### 3. 大眼瘦脸

> 2.0.0 版 SDK 的大眼和瘦脸功能还在紧张开发中，我们会尽快 release.


