
## 功能说明

大眼、瘦脸、动效贴纸、绿幕等特效功能，是基于优图实验室的人脸识别技术和天天P图的美妆技术为基础开发的特权功能，腾讯云小视频团队通过跟优图和P图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。

## 接入流程
单击此处 [申请商业版本 license](https://cloud.tencent.com/product/x-magic)。

## 版本下载
可以到 [RTMP SDK 开发包](https://cloud.tencent.com/document/product/454/7873) 页面下方下载特权版 SDK 压缩包，压缩包有加密（解压密码 & licence 在接入流程步骤获取）, 成功解压后得到一个`Demo`和`SDK`文件，特效资源存放在SDK/Resource下。

> 区分特权版与非特权版，可以查看SDK的bundler id。bundler id为 com.tencent.TXRTMPSDK 表示非特权版，com.tencent.TXRTMPSDK.pitu 表示特权版。
>
> 也可以通过体积直观判断，特权版SDK的体积也比非特权版大很多。



## Xcode工程设置

参考 [工程配置](https://cloud.tencent.com/document/product/584/11638) 

### 1. 添加Framework

特权版需要额外链接一些系统framework
> 1. AssetsLibrary.framwork
> 2. CoreMedia.framework
> 3. Accelerate.framework
> 4. Metal.framework 

### 2. 添加链接参数

> 1. 在工程  Build Setting -> Other Link Flags 里，增加 `-ObjC` 选项。
> 2. 如果使用了AI抠背功能，需要把  Product -> Edit Scheme -> Run -> Options -> Metal API Validation 设置为Disabled。

### 3. 添加动效资源

将SDK/Resource下列文件添加到工程中

> 1. 3DFace
> 2. detector.bundle
> 3. FilterEngine.bundle
> 4. model  
> 5. PE.dat
> 6. poseest.bundle
> 7. RPNSegmenter.bundle
> 8. ufa.bundle


将Demo/TXLiteAVDemo/Resource/Beauty/pitu/data/ 下的SegmentationShader.metal文件添加到工程中
> 1. SegmentationShader.metal

### 4. 添加动效资源示例

将zip包中Resource里面的资源以groups refrence形式添加到工程中，这里需要注意的是handdetect,handtrack,res18_3M三个文件要以folder refrence形式添加，SegmentationShader.metal 文件在 Demo/TXLiteAVDemo/Resource/Beauty/pitu/data/ 下，你可以找到直接添加，具体操作如图所示：
![](https://mc.qcloudimg.com/static/img/d9c501a923b7dbc08f9467da07595b58/image.png)  
![](https://mc.qcloudimg.com/static/img/7a4c4c93298ba65b83fdd63b8b52de42/image.png)

这些资源非常重要，否则切换到换脸类素材时会发生crash。

### 5. 导入licence文件
特权版需要 licence 验证通过后，相应功能才能生效。您可以向我们的商务同学申请一个免费 30 天的调试用 licence。
得到 licence 后，您需要将其命名为**YTFaceSDK.licence** ,然后如上图所示添加到工程。

> 每个licence都有绑定具体的Bundle Identifier，修改app的Bundle Identifier会导致验证失败。
>
> YTFaceSDK.licence 的文件名固定，不可修改。
> 
> iOS 和 Android 不需要重复申请 licence，一个 licence 可以同时授权一个 iOS 的 bundleid 和一个 Android 的packageName。
>


**从4.9版本开始，SDK支持二合一的licence, 这种方式不再需要YTFaceSDK.licence, 在从商务同学处获取到licence对应的key和url后，设置方式和标准版licence设置方式相同。**

## 功能调用

### 1. 动效贴纸

示例：

![](https://mc.qcloudimg.com/static/img/a320624ee8d3a82ee07feb05969e5290/A8B81CB6-DBD3-4111-9BF0-90BD02779BFC.png)

一个动效模版是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数和文件大小也不尽相同。

短视频中的示例代码是从后台下载动效资源，再统一解压到Resource目录。您可以在短视频代码中找到动效资源和动效缩略图的下载地址，格式如下

> `https://st1.xiangji.qq.com/yunmaterials/{动效名}.zip`
>
> `https://st1.xiangji.qq.com/yunmaterials/{动效名}.png`
>

强烈建议客户将动效资源放在自己的服务器上，以防短视频变动造成不必要的影响。

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
### 2. AI抠背

示例：

![](https://mc.qcloudimg.com/static/img/0f79b78687753f88af7685530745a8d4/98B403B8-1DEC-4130-B691-D9EB5E321162.png)

需要下载AI抠背的资源，接口跟动效接口相同

```objective-c
/**
 * 选择抠背动效
 *
 * @param tmplName: 动效名称
 * @param tmplDir: 动效所在目录
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```

### 3. 美妆美容

```objective-c
/* setEyeScaleLevel  设置大眼级别（增值版本有效，普通版本设置此参数无效）
 * 参数：
 *          eyeScaleLevel     : 大眼级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
 */
-(void) setEyeScaleLevel:(float)eyeScaleLevel;

/* setFaceScaleLevel  设置瘦脸级别（增值版本有效，普通版本设置此参数无效）
 * 参数：
 *          faceScaleLevel    : 瘦脸级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
 */
-(void) setFaceScaleLevel:(float)faceScaleLevel;

/* setFaceVLevel  设置V脸（增值版本有效，普通版本设置此参数无效）
 * 参数：
 *          faceVLevel    : V脸级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
 */
- (void) setFaceVLevel:(float)faceVLevel;

/* setChinLevel  设置下巴拉伸或收缩（增值版本有效，普通版本设置此参数无效）
 * 参数：
 *          chinLevel    : 下巴拉伸或收缩取值范围 -9 ~ 9； 0 表示关闭 -9收缩 ~ 9拉伸。
 */
- (void) setChinLevel:(float)chinLevel;

/* setFaceShortLevel  设置短脸（增值版本有效，普通版本设置此参数无效）
 * 参数：
 *          faceShortlevel    : 短脸级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
 */
- (void) setFaceShortLevel:(float)faceShortlevel;

/* setNoseSlimLevel  设置瘦鼻（增值版本有效，普通版本设置此参数无效）
 * 参数：
 *          noseSlimLevel    : 瘦鼻级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
 */
- (void) setNoseSlimLevel:(float)noseSlimLevel;

```

### 4. 绿幕功能

使用绿幕需要先准备一个用于播放的mp4文件，通过调用以下接口即可开启绿幕效果

```objective-c
/**
 * 设置绿幕文件
 * 
 * @param file: 绿幕文件路径。支持mp4; nil 关闭绿幕
 */
-(void)setGreenScreenFile:(NSURL *)file;
```
## 问题排查
### 1. 工程编译不过？  
 > 1. 检查AssetsLibrary.framwork、CoreMedia.framework、Accelerate.framework、Metal.framework 依赖库是否已经添加
                 
### 2. 工程运行过程中crash？  
 > 1. 检查工程是否配置了 -ObjC  
 > 2. 检查 Metal API Validation 是否设置成了Disabled
     
### 3. 工程特效不生效？  
 > 1. 检查是否调用了`+[TXUGCBase setLicenceURL:key:]`方法, 以及参数是否正确
 > 2. 调用TXUGCBase的getLicenseInfo方法，带有动效的licence会包含`pituLicense`字段
 > 3. 检查pitu资源是否添加正确，尤其要注意 handdetect,handtrack,res18_3M三个文件要以folder refrence形式添加，最简单的方法就是比对自己工程添加的动效文件是否和我们demo添加的完全一致  
 > 4. SDK会把licence下载到沙盒的Documents目录当中, 可以在开发过程中使用Xcode菜单中Window -> Devices and Simulators工具导出并使用[查询工具(点击下载)](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)查看有效期。
 
##### [查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)是一个xcode工程，目前仅支持在mac上使用， 后续会开放其他查询方式
