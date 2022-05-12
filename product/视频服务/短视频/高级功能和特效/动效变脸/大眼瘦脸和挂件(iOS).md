目前，仅原移动直播企业版 SDK，短视频企业版 SDK 以及短视频企业版 Pro SDK 支持高级美颜特效，需要购买原 [移动直播企业版 License](https://cloud.tencent.com/document/product/454/8008)、[短视频企业版 License 或短视频企业版 Pro License](https://cloud.tencent.com/document/product/584/9368) 后，使用对应的功能。

## 功能说明

大眼、瘦脸、动效贴纸、绿幕等特效功能，是基于优图实验室的 AI 识别技术和天天 P 图的美妆技术为基础开发的特权功能，腾讯云小视频团队通过跟优图和 P 图团队合作，将这些特效深度整合到 RTMP SDK 的图像处理流程中，以实现更好的视频特效。

## 接入流程
[单击此处](https://cloud.tencent.com/product/x-magic) 申请企业版本 License。

## 版本下载
在 [SDK 下载](https://cloud.tencent.com/document/product/584/9366) 页面下方下载企业版 SDK 压缩包，压缩包有加密（解压密码和 Licence 在接入流程步骤获取），成功解压后得到一个 Demo 和 SDK 文件，特效资源存放在 SDK/Resource 下。

## Xcode 工程设置

具体操作请参见 [工程配置](https://cloud.tencent.com/document/product/584/11638)。 

### 步骤1：添加 Framework

企业版需要额外链接以下 Framework：
> - AssetsLibrary.framwork
> - CoreMedia.framework
> - Accelerate.framework
> - Metal.framework 

### 步骤2：添加链接参数

1. 在工程 **Build Setting** > **Other Link Flags** 里，增加 `-ObjC` 选项。
2. 如果使用了 AI 抠背功能，需要把 **Product** > **Edit Scheme** > **Run** > **Options** > **Metal API Validation** 设置为 Disabled。

### 步骤3：添加动效资源

请检查是否添加动效资源：将 SDK/Resource 下的文件以 groups 的形式添加到工程中，文件列表如下：

> - AECore.metallib
> - FilterEngine.bundle
> - RPNSegmenter.bundle
> - YTHandDetector.bundle
> - detector.bundle
> - e1
> - o1
> - poseest.bundle
> - u1
> - ufa.bundle
> - v1

### 步骤4：导入 Licence 文件
企业版需要 Licence 验证通过后，相应功能才能生效。您可以向我们的商务人员申请一个免费30天的调试用 Licence。
得到 Licence 后，您需要将其命名为 **YTFaceSDK.licence**，然后如上图所示添加到工程。
>?
>- 每个 Licence 都有绑定具体的 Bundle Identifier，修改 app 的 Bundle Identifier 会导致验证失败。
>- YTFaceSDK.licence 的文件名固定，不可修改。
>- iOS 和 Android 不需要重复申请 licence，一个 Licence 可以同时授权一个 iOS 的 bundleid 和一个 Android 的 packageName。


**从9.4版本开始，SDK 支持二合一的 Licence，这种方式不再需要 YTFaceSDK.licence，在从商务人员处获取到 Licence 对应的 key 和 url 后，设置方式和标准版 Licence 设置方式相同。**

## 功能调用

### 动效贴纸

#### 示例
<img src="https://main.qcloudimg.com/raw/c59d34f627b87faef0603a711010176d.png" width="450">

一个动效模板是一个目录，里面包含很多资源文件。每个动效因为复杂度不同，目录个数和文件大小也不尽相同。

短视频中的示例代码是从后台下载动效资源，再统一解压到 Resource 目录。您可以在短视频代码中找到动效资源和动效缩略图的下载地址，格式如下：
- `https://st1.xiangji.qq.com/yunmaterials/{动效名}.zip`
- `https://st1.xiangji.qq.com/yunmaterials/{动效名}.png`

>?建议客户将动效资源放在自己的服务器上，以防短视频变动造成不必要的影响。

当解压完成后，即可通过以下接口开启动效效果：
```objectivec
/**
 * 选择动效
 *
 * @param tmplName: 动效名称
 * @param tmplDir: 动效所在目录
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```

### AI 抠背

#### 示例
<img src="https://main.qcloudimg.com/raw/7c6b11672e8b8ae0a8080ab81cd76f71.png" width="450">

需要下载 AI 抠背的资源，接口跟动效接口相同：
```objectivec
/**
 * 选择抠背动效
 *
 * @param tmplName: 动效名称
 * @param tmplDir: 动效所在目录
 */
- (void)selectMotionTmpl:(NSString *)tmplName inDir:(NSString *)tmplDir;
```

### 高级美颜接口（大眼、瘦脸等）

您可以通过 TXUGCRecord 的 getBeautyManager 方法获取 TXBeautyManager 对象来进行设置各项美颜参数，其方法如下。
<dx-codeblock>
::: objective-c objectivec
/**
 * 设置美颜（磨皮）算法
 *
 * SDK 内部集成了两套风格不同的磨皮算法，一套我们取名叫“光滑”，适用于美女秀场，效果比较明显。
 * 另一套我们取名“自然”，磨皮算法更多地保留了面部细节，主观感受上会更加自然。
 *
 * @param beautyStyle 美颜风格，光滑或者自然，光滑风格磨皮更加明显，适合娱乐场景。
 */
- (void)setBeautyStyle:(TXBeautyStyle)beautyStyle;

/**
 * 设置美颜级别
 * @param level 美颜级别，取值范围0 - 9； 0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setBeautyLevel:(float)level;

/**
 * 设置美白级别
 *
 * @param level 美白级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setWhitenessLevel:(float)level;

/**
 * 设置红润级别
 *
 * @param level 红润级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setRuddyLevel:(float)level;

/**
 * 设置大眼级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 大眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setEyeScaleLevel:(float)level;

/**
 * 设置瘦脸级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 瘦脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceSlimLevel:(float)level;

/**
 * 设置 V 脸级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level V 脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceVLevel:(float)level;

/**
 * 设置下巴拉伸或收缩（企业版有效，其它版本设置此参数无效）
 *
 * @param level 下巴拉伸或收缩级别，取值范围-9 - 9；0 表示关闭，小于0表示收缩，大于0表示拉伸。
 */
- (void)setChinLevel:(float)level;
/**
 * 设置短脸级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 短脸级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceShortLevel:(float)level;

/**
 * 设置瘦鼻级别（企业版有效，其它版本设置此参数无效）
 *
 * @param level 瘦鼻级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setNoseSlimLevel:(float)level;

/**
 * 设置亮眼（企业版有效，其它版本设置此参数无效）
 *
 * @param level 亮眼级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setEyeLightenLevel:(float)level;

/**
 * 设置白牙（企业版有效，其它版本设置此参数无效）
 *
 * @param level 白牙级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setToothWhitenLevel:(float)level;

/**
 * 设置祛皱（企业版有效，其它版本设置此参数无效）
 *
 * @param level 祛皱级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setWrinkleRemoveLevel:(float)level;

/**
 * 设置祛眼袋（企业版有效，其它版本设置此参数无效）
 *
 * @param level 祛眼袋级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setPounchRemoveLevel:(float)level;

/**
 * 设置法令纹（企业版有效，其它版本设置此参数无效）
 *
 * @param level 法令纹级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setSmileLinesRemoveLevel:(float)level;

/**
 * 设置发际线（企业版有效，其它版本设置此参数无效）
 *
 * @param level 发际线级别，取值范围-9 - 9；0表示关闭，小于0表示抬高，大于0表示降低。
 */
- (void)setForeheadLevel:(float)level;

/**
 * 设置眼距（企业版有效，其它版本设置此参数无效）
 *
 * @param level 眼距级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setEyeDistanceLevel:(float)level;

/**
 * 设置眼角（企业版有效，其它版本设置此参数无效）
 *
 * @param level 眼角级别，取值范围-9 - 9；0表示关闭，小于0表示降低，大于0表示抬高。
 */
- (void)setEyeAngleLevel:(float)level;

/**
 * 设置嘴型（企业版有效，其它版本设置此参数无效）
 *
 * @param level 嘴型级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setMouthShapeLevel:(float)level;

/**
 * 设置鼻翼（企业版有效，其它版本设置此参数无效）
 *
 * @param level 鼻翼级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setNoseWingLevel:(float)level;

/**
 * 设置鼻子位置（企业版有效，其它版本设置此参数无效）
 * @param level 鼻子位置级别，取值范围-9 - 9；0表示关闭，小于0表示抬高，大于0表示降低。
 */
- (void)setNosePositionLevel:(float)level;

/**
 * 设置嘴唇厚度（企业版有效，其它版本设置此参数无效）
 * @param level 嘴唇厚度级别，取值范围-9 - 9；0表示关闭，小于0表示拉伸，大于0表示收缩。
 */
- (void)setLipsThicknessLevel:(float)level;

/**
 * 设置脸型（企业版有效，其它版本设置此参数无效）
 * @param   level 美型级别，取值范围0 - 9；0表示关闭，1 - 9值越大，效果越明显。
 */
- (void)setFaceBeautyLevel:(float)level;
:::
</dx-codeblock>

### 绿幕功能

使用绿幕需要先准备一个用于播放的 MP4 文件，通过调用以下接口即可开启绿幕效果。

```objective-c
/**
 * 设置绿幕文件
 * 
 * @param file: 绿幕文件路径。支持 mp4; nil 关闭绿幕
 */
-(void)setGreenScreenFile:(NSURL *)file;
```


## 问题排查
### 1. 工程编译不过？
检查 AssetsLibrary.framwork、CoreMedia.framework、Accelerate.framework、Metal.framework 依赖库是否已经添加。
                 
### 2. 工程运行过程中 crash？  
1. 检查工程是否配置了 -ObjC。  
2. 检查 Metal API Validation 是否设置成了 Disabled。
     
### 3. 工程特效不生效？  
1. 检查是否调用了 `+[TXUGCBase setLicenceURL:key:]` 方法，以及参数是否正确。
2. 调用 TXUGCBase的 getLicenseInfo 方法，带有动效的 Licence 会包含 `pituLicense` 字段。
3. 检查 pitu 资源是否添加正确，尤其要注意 handdetect、handtrack、res18_3M 三个文件要以 folder refrence 形式添加，最简单的方法就是比对自己工程添加的动效文件是否和我们 demo 添加的完全一致。  
4. SDK 会把 Licence 下载到沙盒的 Documents 目录当中, 可以在开发过程中使用 Xcode 菜单中 Window > Devices and Simulators 工具导出并使用 [查询工具（单击下载）](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip)查看有效期。
 [查询工具](https://mc.qcloudimg.com/static/archive/9c0f8c02466d08e5ac14c396fad21005/PituDateSearch.zip) 是一个 xcode 工程，目前仅支持在 mac 上使用， 后续会开放其他查询方式。
