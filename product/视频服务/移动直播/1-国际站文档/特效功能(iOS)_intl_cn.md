# 特效功能（大眼、瘦脸、动效、绿幕）

## 功能说明
大眼、瘦脸、动效贴纸、绿幕等特效功能，是基于优图实验室的人脸识别技术和天天P图的美妆技术为基础开发的特权功能，腾讯云小直播团队通过跟优图和P图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。

## 费用说明
由于采用了优图实验室的专利技术，授权费用约 **50W/年**（目前国内同类图像处理产品授权均在百万左右）。如有需要可以提工单或客服电话（400-9100-100）联系我们，商务同学会提供压缩包解码密码，并替您向优图实验室申请试用 License。

## 版本下载
可以到 [RTMP SDK 开发包](https://cloud.tencent.com/document/product/454/7873) 页面下方下载特权版 SDK 压缩包，压缩包有加密（解压密码 & license 可以跟我们的商务同学获取）, 成功解压后得到一个`txrtmpsdk.jar`和`libtxrtmpsdk.so`等几个so，替换你工程中的非特权版jar和so即可。

> 区分特权版与非特权版，可以查看SDK的bundler id。bundler id为 com.tencent.TXRTMPSDK 表示非特权版，com.tencent.TXRTMPSDK.pitu 表示特权版。
>
> 也可以通过体积直观判断，特权版SDK的体积也比非特权版大很多。



## Xcode工程设置

### 1. 添加Framework

特权版需要额外链接一些系统framework
> 1. AssetsLibrary.framwork
> 2. CoreMedia.framework
> 3. Accelerate.framework

### 2. 添加链接参数

在工程  Build Setting -> Other Link Flags 里，增加 `-ObjC` 选项。

### 3. 添加资源bundle

将zip包中下列文件添加到工程中

> 1. FilterEngine.bundle
> 2. PE.dat
> 3. ufa.bundle
> 4. youtubeauty.bundle

### 4. 添加动效资源

将zip包中Resource目录以folder refrence形式添加到工程中。

![](https://mc.qcloudimg.com/static/img/b7fac6b5e08b0ff245b17d29f7296b18/AAE85661-7601-4473-A338-747FB9A6981C.png)

这些资源非常重要，否则切换到换脸类素材时会发生crash。

### 3. 导入licence文件
特权版需要 licence 验证通过后，相应功能才能生效。您可以向我们的商务同学申请一个免费 30 天的调试用 license。
得到 licence 后，您需要将其命名为**YTFaceSDK.licence**，工程的assets目录下。

> 每个licence都有绑定具体的package name，修改app的package name会导致验证失败。
>
> YTFaceSDK.license的文件名固定，不可修改、且必须放在assets目录下。
> 
> iOS 和 Android 不需要重复申请 license，一个 license 可以同时授权一个 iOS 的 bundleid 和一个 Android 的packageName。

## 功能调用

### 1. 动效贴纸

一个动效模版是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数以和文件大小也不尽相同。

小直播中的示例代码是从后台下载动效资源，再统一解压到Resource目录。您可以在小直播代码中找到动效资源和动效缩略图的下载地址，格式如下

> `https://st1.xiangji.qq.com/yunmaterials/{动效名}.zip`
>
> `https://st1.xiangji.qq.com/yunmaterials/{动效名}.png`
>

强烈建议客户将动效资源放在自己的服务器上，以防小直播变动造成不必要的影响。

当解压完成后，即可通过以下接口开启动效效果

```objective-c
/**
 * 选择动效
 *
 * @param tmplName: 动效名称
 * @param tmplDir: 动效所在目录
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```


### 2. 绿幕功能

使用绿幕需要先准备一个用于播放的mp4文件，通过调用以下接口即可开启绿幕效果

```objective-c
/**
 * 设置绿幕文件
 * 
 * @param file: 绿幕文件路径。支持mp4; nil 关闭绿幕
 */
-(void)setGreenScreenFile:(NSURL *)file;
```

### 3.大眼瘦脸

大眼和瘦脸通过以下方法设置

```objective-c
/**
 * 设置大眼级别
 * 
 *  @param eyeScaleLevel: 大眼级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
 */
-(void)setEyeScaleLevel:(float)eyeScaleLevel;

/**
 * 设置瘦脸级别
 *
 *  @param faceScaleLevel: 瘦脸级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
 */
-(void)setFaceScaleLevel:(float)faceScaleLevel;
```

