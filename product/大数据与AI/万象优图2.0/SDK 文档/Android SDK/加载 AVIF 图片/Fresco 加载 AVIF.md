
本文主要介绍如何使用 Fresco 加载 AVIF 图片。


### 安装 Fresco 和 AVIF SDK

Fresco 是一个知名开源的图片缓存库。更多信息，请参见 [Fresco 官方文档](https://frescolib.org/docs/index.html)。

```
implementation 'com.qcloud.cos:avif:1.1.1'   
//如果出现beacon灯塔冲突，引入-nobeacon即可
//implementation 'com.qcloud.cos:avif-nobeacon:1.1.1'

implementation 'com.facebook.fresco:fresco:version'
// 如果需要支持 avif 动图解码器 则需要加上 fresco:animated-base 依赖
implementation 'com.facebook.fresco:animated-base:version'
```

### 步骤一：配置解码器

#### 全局配置

初始化 Fresco 的时候进行配置，全局生效。配置后按照 Fresco 加载普通图片的方式加载 AVIF 图片即可。

```
// 解码器配置
ImageDecoderConfig imageDecoderConfig = new ImageDecoderConfig.Builder()
         // 配置 AVIF 静态解码器
        .addDecodingCapability(
                AvifFormatChecker.AVIF,
                new AvifFormatChecker(),
                new FrescoAvifDecoder())
        // 配置 AVIF 动图解码器
        .addDecodingCapability(
                AvisFormatChecker.AVIS,
                new AvisFormatChecker(),
                new FrescoAvisDecoder())
        .build();
// 配置 Image Pipeline
ImagePipelineConfig config = ImagePipelineConfig.newBuilder(context)
        .setImageDecoderConfig(imageDecoderConfig)
        .build();
// 初始化 Fresco
Fresco.initialize(context, config);
```

#### 单次请求配置

使用 Fresco 加载图片时配置，本次加载请求 AVIF 解码器会生效。本次图片加载可以加载 AVIF 图片。

```
Uri uri = Uri.parse("https://xxx.com/test.avif");
SimpleDraweeView draweeView = (SimpleDraweeView) findViewById(R.id.my_image_view);
ImageRequest imageRequest = ImageRequestBuilder.newBuilderWithSource(uri)
                .setImageDecodeOptions(ImageDecodeOptions.newBuilder()
                        .setCustomImageDecoder(new FrescoAvifDecoder()) // 配置 AVIF 静态解码器
                      //.setCustomImageDecoder(new FrescoAvisDecoder()) // 配置 AVIF 动图解码器
                        .build())
                .build();
AbstractDraweeController controller = Fresco.newDraweeControllerBuilder().setImageRequest(imageRequest).build();
draweeView.setController(controller);
```

### 步骤二：使用 Fresco 加载图片

更多信息，请参见 [Fresco 官方文档](https://frescolib.org/docs/index.html)。

1. 布局文件中加入 SimpleDraweeView

```
<com.facebook.drawee.view.SimpleDraweeView
    android:id="@+id/my_image_view"
    android:layout_width="130dp"
    android:layout_height="130dp"
    fresco:placeholderImage="@drawable/my_drawable"
  />
```

2. 开始加载图片

如果是全局配置 AVIF 解码器，则直接使用 Fresco 加载图片即可。

```
Uri uri = Uri.parse("https://xxx.com/test.avif");
SimpleDraweeView draweeView = (SimpleDraweeView) findViewById(R.id.my_image_view);
draweeView.setImageURI(uri);
```

然后是单次请求配置 AVIF 解码器，则在加载请求中加入 AVIF 解码器配置，代码示例如下：

```
Uri uri = Uri.parse("https://xxx.com/test.avif");
SimpleDraweeView draweeView = (SimpleDraweeView) findViewById(R.id.my_image_view);
ImageRequest imageRequest = ImageRequestBuilder.newBuilderWithSource(uri)
                .setImageDecodeOptions(ImageDecodeOptions.newBuilder()
                        .setCustomImageDecoder(new FrescoAvifDecoder()) // 配置 AVIF 静态解码器
                      //.setCustomImageDecoder(new FrescoAvisDecoder()) // 配置 AVIF 动图解码器
                        .build())
                .build();
AbstractDraweeController controller = Fresco.newDraweeControllerBuilder().setImageRequest(imageRequest).build();
draweeView.setController(controller);
```

### 设置加载失败后原图重试

>! AVIF SDK 版本需要大于等于 v1.1.1。

当 AVIF 图片加载失败时，自动请求原格式图片，提升用户体验。并将 AVIF 图片加载失败原因返回，用于排查失败原因及时修复。

在 Fresco 加载图片时通过 PipelineDraweeController.addControllerListener 方法设置 OriginalImageRetryControllerListener 实现原图重试功能。

```
String imgUrl = "https://www.test.com/test.avif";
ImageRequestBuilder imageRequestBuilder = ImageRequestBuilder.newBuilderWithSource(Uri.parse(imgUrl));
ImageRequest request = imageRequestBuilder.build();
BaseControllerListener<ImageInfo> controllerListener = new BaseControllerListener<ImageInfo>() {
    @Override
    public void onFinalImageSet(
            String id,
            @Nullable ImageInfo imageInfo,
            @Nullable Animatable anim) {
        // 其他业务onFinalImageSet
    }
    @Override
    public void onFailure(String id, Throwable throwable) {
        // 其他业务onFailure
    }
};
PipelineDraweeControllerBuilder draweeControllerBuilder = Fresco.newDraweeControllerBuilder()
        .setOldController(simpleDraweeView.getController())
        .setControllerListener(controllerListener)
        .setImageRequest(request);
// 原图兜底监听器
OriginalImageRetryControllerListener originalImageRetry = new OriginalImageRetryControllerListener(simpleDraweeView, imageRequestBuilder, draweeControllerBuilder);
originalImageRetry.setOriginalImageRetryCallback(new FrescoOriginalImageRetryCallback() {
    @Nullable
    @Override
    public String buildOriginalImageUrl(String urlStr) {
        // 使用默认的原图格式
        return null;
    }
    @Override
    public void onFailureBeforeRetry(Uri uri, String id, Throwable throwable) {
        // AVIF加载失败在这里上报，统计原图兜底次数和AVIF解码异常信息(不影响真正的图片加载失败率)
        Log.d(TAG, "AVIF onLoadFailed："+ uri.toString());
        if (throwable != null) {
            Log.d(TAG, throwable.getMessage());
            throwable.printStackTrace();
        }
    }
    @Override
    public void onFailure(Uri uri, String id, Throwable throwable) {
        //真正的加载失败在这里上报(影响真正的图片加载成功失败率)
        Log.d(TAG, "Image onLoadFailed："+ uri.toString());
        if (throwable != null) {
            Log.d(TAG, throwable.getMessage());
            throwable.printStackTrace();
        }
    }
    @Override
    public void onFinalImageSet(Uri uri, String id, @Nullable ImageInfo imageInfo, @Nullable Animatable anim) {
        //真正的加载成功在这里上报(影响真正的图片加载成功失败率)
        Log.d(TAG, "Image onLoadSuccess："+ uri.toString());
    }
});
PipelineDraweeController controller = (PipelineDraweeController) draweeControllerBuilder.build();
controller.addControllerListener(originalImageRetry);
simpleDraweeView.setController(controller);
```