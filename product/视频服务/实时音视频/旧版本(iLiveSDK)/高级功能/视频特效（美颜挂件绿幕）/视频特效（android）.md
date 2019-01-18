本文将指导您如何添加插件美颜  快速实现 美颜/滤镜/绿幕/动效/大眼/瘦脸等视频特效。

## 效果图

美颜|滤镜|大眼/瘦脸/小鼻等|动效|绿幕
:-----:|:-----:|:-----:|:-----:|:-----:
![](https://main.qcloudimg.com/raw/37c82c24b8154081c21293f7c65ddfae.png)|![](https://main.qcloudimg.com/raw/b7b91102c419a5f7ae590215fdb0065c.png)|![](https://main.qcloudimg.com/raw/bd5ebfa2b3078061ca5f2e824db1beb5.png)|![](https://main.qcloudimg.com/raw/53a5e44a06db04fdca6b6929c63820f5.png)|![](https://main.qcloudimg.com/raw/2117efcf754bb9992a5fbc9ba62f1bce.png)

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](https://codeload.github.com/zhaoyang21cn/TILFilterSdk/zip/master?token=ARGVpSHzhZ0WYLDRNtIHFfWu2HyLU0YTks5bANKAwA==)

## 具体实现

### 1. 添加 licence(p 图收费版)
申请 p 图 licence；
将 licence 改名为 YTFaceSDK.licence 放入 app 的 assets 目录下


### 2. 集成美颜插件

p 图收费版：
```
// build.gradle 中，加载p图收费版
compile 'com.tencent.ilivefilter:liteav_pitu:1.1.22'
```
```
defaultConfig{
    ....
    // 指定ndk架构
    ndk {
        // p图收费版；只支持 armeabi 架构
        abiFilters 'armeabi'
    }
}
```
非 p 图普通版：
```
// build.gradle 中，加载非p图普通版
compile 'com.tencent.ilivefilter:liteav_normal:1.1.22'
```
```
defaultConfig{
    ....
    // 指定ndk架构
    ndk {
        // 非p图版，支持'armeabi', 'armeabi-v7a' 两种架构
        abiFilters 'armeabi', 'armeabi-v7a'
    }
}
```

### 3. 初始化美颜插件
```
boolean bGLContext = false;     // iLiveSDK 场景下，设置当前为无 OpenGL 环境
TXCVideoPreprocessor mTxcFilter = new TXCVideoPreprocessor(this, bGLContext);
```
### 4. 处理视频数据
进入房间成功后，设置 iLiveSDK 数据回调，美颜插件处理数据
(**设置数据回调，一定要在进入房间成功后才有效。**)

```
// 设置数据回调
boolean bRet = ILiveSDK.getInstance().getAvVideoCtrl().setAfterPreviewListener(new AVVideoCtrl.AfterPreviewListener(){
    @Override
    public void onFrameReceive(AVVideoCtrl.VideoFrame var1) {

        // 回调的数据，传递给 美颜插件 processFrame 接口处理;并且通过 var1.data 返回处理后的数据
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
            mTxcFilter.processFrame(var1.data, var1.width, var1.height, var1.rotate, var1.videoFormat, var1.videoFormat);
        }
    }
});
```
**例外：**
**p 图版本，并且 iLiveSDK 版本 小于 1.7.0；只能使用 setLocalVideoPreProcessCallback 回调接口，否则 p 图功能无效。**
iLiveSDK 版本，可通过 ILiveSDK.getInstance().getVersion() 获取

**详情参考 [开发说明](https://github.com/zhaoyang21cn/iLiveSDK_Android_Suixinbo/blob/master/doc/ILiveSDK/ilivefiltersdk-README.md)**


### 5. 设置效果参数

根据 API 说明，设置相应的效果， 如：
```
mTxcFilter.setBeautyLevel(5);           // 设置美颜级别,范围 0～10
mTxcFilter.setWhitenessLevel(3);        // 设置美白级别,范围 0～10
mTxcFilter.setRuddyLevel(2);            // 设置红润级别，范围 0～10
```

### 6. 释放资源

**退出房间时，必须释放插件美颜资源，否则下次进入房间，设置特效不生效。**
**日志也会出现 “please realloc new TXCVideoPreprocessor” 错误**
```
ILVLiveManager.getInstance().quitRoom(new ILiveCallBack() {
    @Override
    public void onSuccess(Object data) {
    // 取消 iLiveSDK 相机数据回调（参数传null）
    boolean bRet = ILiveSDK.getInstance().getAvVideoCtrl().setAfterPreviewListener(null);
        // 退出房间后，一定要销毁filter 资源；否则下次进入房间，setFilter将不生效或其他异常
        mTxcFilter.release();
        mTxcFilter = null;
    }
    @Override
    public void onError(String module, int errCode, String errMsg) {
    }
});
```

### 7. 扩展：其他使用场景

如：
1. 自定义采集
2. 需要支持纹理输入-->纹理输出场景
3. 自定义滤镜

**请参考详细文档 [开发说明](https://github.com/zhaoyang21cn/iLiveSDK_Android_Suixinbo/blob/master/doc/ILiveSDK/ilivefiltersdk-README.md)**

## API说明
| 接口名|  接口描述  |参数定义|返回值|
|---------|---------|---------|---------|
| TXCVideoPreprocessor(Context activity, boolean bGLContext) | 构造函数|**activity**：当前Activity的this指针  **bGLContext**：当前是否有Opengl 环境|无|
| **逻辑代码接口** |
| void setListener(TXIVideoPreprocessorListener listener) | 设置sdk数据监听回调|**listener**: sdk数据返回监听（用于接收process* 处理函数返回的数据）|无|
| void setNotifyListener(TXINotifyListener notify) | 设置sdk事件监听回调|**notify**: sdk事件监听；事件为 TXCVideoPreprocessor.EventVideoProcess.*|无|
| int processFrame(int texture, int width, int height, int processAngle, int inputFormat, int outputFormat) | 纹理输入处理|**texture**：输入纹理 **width**：纹理宽 **height**：纹理高 **processAngle**：纹理旋转角度 **inputFormat**：视频输入格式（0：2D纹理输入 1：I420数据输入 2：RGBA 数据输出 3：NV21数据输入 4:外部纹理输入（如相机纹理，需要调用 setInputMatrix 设置旋转矩阵）） **outputFormat**：视频输出格式（0：2D纹理输出 1：I420数据输出 2：RGBA 数据输出 3：NV21数据输出） |-1： 失败 >=0：成功|
| int processFrame(byte[] data, int width, int height, int processAngle, int inputFormat, int outputFormat) | 原始数据输入处理|**data**：输入原始数据 **width**：数据宽 **height**：数据高 **processAngle**：纹理旋转角度 **inputFormat**：视频输入格式（0：2D纹理输入 1：I420数据输入 2：RGBA 数据输出 3：NV21数据输入 4:外部纹理输入（如相机纹理，需要调用 setInputMatrix 设置旋转矩阵）） **outputFormat**：视频输出格式（0：2D纹理输出 1：I420数据输出 2：RGBA 数据输出 3：NV21数据输出） |-1： 失败 >=0：成功|
| void setInputMatrix(float[] mtx) | 设置外部纹理输入时的旋转矩阵（仅在外部纹理输入时，才使用）|**mtx**: 外部纹理输入时，从SurfaceTexture.getTransformMatrix() 中获取|无|
| void release() | 释放sdk资源|无 |无|
| **美颜相关接口** |
| void setBeautyStyle(int style) | 设置美颜风格|**style**: 美颜风格 0: 光滑 1: 自然 2: 朦胧|无|
| void setBeautyLevel(int level) | 设置美颜级别|**level**: 美颜级别 （0 - 9）|无|
| void setWhitenessLevel(int level) | 设置美白级别|**level**: 美白级别（0 - 9）|无|
| void setRuddyLevel(int level) | 设置红润级别|**level**: 红润级别（0 - 9）|无|
| **滤镜相关接口** |
| int setFilterType(int type) | 切换滤镜|**type**: 滤镜编号 1:无  2：浪漫 3：清新 4：唯美 5：粉嫩 6：怀旧 7: 蓝调 8:清凉  9: 日系|-1：失败 0：成功|
| void setFilterImage(Bitmap bmp) | 设置滤镜图片|**bmp**: 滤镜图片|无|
| void setFilterImage(String imagePath) | 设置滤镜图片路径|**imagePath**：滤镜文件路径|无|
| void setFilterMixLevel(final float specialValue) | 设置滤镜程度|**specialValue**：滤镜程度（0.0 - 1.0）|无|
| **视频编辑相关接口** |
| void setCrop(CropRect cutRect) | 设置剪裁大小|**cutRect**：剪裁矩阵 cutRect.x：x轴坐标偏移 cutRect.y：y轴坐标偏移 cutRect.cropWidth：x轴剪裁长度 cutRect.cropHeight：y轴剪裁高度 |无|
| void setRotate(int angle) | 设置输出旋转顺时针角度|**angle**：输出顺时针旋转角度|无|
| void setOutputFrameSize(int width, int height) | 设置输出长宽|**width**：输出数据宽 **height**：输出数据高 |无|
| void setMirror(boolean enable) | 设置输出图像左右镜像|**enable**：true：开启左右镜像 false：不开启左右镜像 |无|
| void setWaterMark(Bitmap bitmap, float x, float y, float width) | 设置水印（位置以左上角为原点）|**bitmap**: 水印图片BitMap **x**：(0.0 - 1.0)归一化坐标，左上角x轴偏移 **y**：(0.0 - 1.0)归一化坐标，左上角y轴偏移 width：(0.0 - 1.0)归一化宽度；左上角x轴宽度|无|
| void setWaterMarkList(final List< WaterMakeTag> markList) | 设置多个水印（setWaterMark 的加强版）|**markList**：多个水印 WaterMakeTag 链表|无|
| **p图收费版相关接口** |
| void setFaceSlimLevel(int level) | 设置瘦脸级别|**level**: 瘦脸级别（0 - 9）|无|
| void setEyeScaleLevel(int level) | 设置大眼级别|**level**: 大眼级别（0 - 9）|无|
| void setFaceVLevel(int level) | 设置V脸级别|**level**: V脸级别（0 - 9）|无|
| void setFaceShortLevel(int level) | 设置短脸级别|**level**: 短脸级别（0 - 9）|无|
| void setChinLevel(int level) | 设置长下巴级别|**level**: 长下巴级别（0 - 9）|无|
| void setNoseSlimLevel(int level)** | 设置小鼻级别|**level**: 小鼻级别（0 - 9）|无|
| void setMotionTmpl(String tmplPath) | 设置动态贴纸路径|**tmplPath**: 动态贴纸路径|无|
| boolean setGreenScreenFile(String path, boolean isLoop) | 设置绿幕文件路径|**path**: 绿幕文件路径(目前图片支持jpg/png/bmp，视频仅支持mp4格式)      **isLoop**：是否循环播放设置的视频文件（只针对视频）|无|
| boolean setGreenScreenParam(TXCGreenScreenParam param) | 设置绿幕参数|**param**.fillMode：绿幕背景填充参数     **param**.xMirror：x轴是否镜像；因为Android相机前置摄像头为左右镜像；所以如果想要主播看到绿幕背景为正，则需要左右镜像绿幕|无|


## 常见问题
#### 为什么 p 图功能不生效？

1. 确认 licence 文件名称是否是 YTFaceSDK.licence；
2. 确认 licence 文件 是否在 assets 目录下；
3. processFrame 传入的processAngle角度，是否正确；iLiveSDK 一般传 var1.rotate；

#### 为什么 licence 存在，但是加载会失败？
 确认 licence 是否过期；可以找申请 licence 时的相关人员确认。

#### p 图版和非 p 图版有什么区别？ 非 p 图版是收费的吗？

1. p 图版，集成了 p 图人脸识别 sdk；支持 美颜/滤镜/水印等基础功能 + 绿幕/动效/大眼/瘦脸等人脸识别相关的 p 图特效，
2. 非 p 图版本，只支持美颜/滤镜/水印等基础功能，
3. 非 p 图版，是免费使用的，


#### 为什么 p 图版本，so 库只支持 armeabi 架构？
1. 市面上大多数手机，都是 armeabi-v7a/arm64-v8a/x86 等架构；而这些架构， 都可以兼容 armeabi；
2. 为了 p 图 sdk 的体积考虑，所以只提供 armeabi 架构的 so 库

#### 为何会分“有 GL 环境”和“无 GL 环境”两种模式？

1. 一般应用场景，只会出现“有 GL 环境”和“无 GL 环境”；从效率和使用方式上考虑，故 sdk 支持两种模式；
2. 如果用户使用场景（如：自定义采集），存在GL环境；为了不与现有 GL 环境冲突，使用“有 GL 环境”模式，支持纹理输入-->处理后纹理输出，效率和兼容性更好；
3. 如果用户使用场景（如：使用 iLiveSDK 采集），无 GL 环境；sdk 会单独开启一个线程，处理传入的原始视频数据，此时不支持纹理输入-->纹理输出，仅支持 原始数据输入-->原始数据输出；

#### 接入 p 图版本，如何收费？
参见上面的“费用说明”

#### 为什么通过` compile  'com.tencent.ilivefilter:****'`,提示 `“Could not get resource '****.aar'”`，提示 aar 无法找到呢？

可能是 jcenter 服务器下载链接的问题；可以改成` compile  'com.tencent.ilivefilter:****@aar' `试试
