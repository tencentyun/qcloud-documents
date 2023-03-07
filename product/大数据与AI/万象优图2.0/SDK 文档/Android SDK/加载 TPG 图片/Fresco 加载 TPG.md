
本文主要介绍如何使用 Fresco 加载 TPG 图片。


### 安装 Fresco 和 TPG SDK

Fresco是一个知名开源的图片缓存库。更多信息，请参见 [Fresco 官方文档](https://frescolib.org/docs/index.html)。

```
implementation 'com.qcloud.cos:tpg:1.3.8' 
implementation 'com.facebook.fresco:fresco:version'
// 如果需要支持 tpg 动图解码器 则需要加上 fresco:animated-base 依赖
implementation 'com.facebook.fresco:animated-base:version'
```

### 步骤一：配置解码器

#### 全局配置

初始化 Fresco 的时候进行配置，全局生效。配置后按照 Fresco 加载普通图片的方式加载 TPG 图片即可。

```
// 解码器配置
ImageDecoderConfig imageDecoderConfig = new ImageDecoderConfig.Builder()
        // 配置 TPG 静态解码器
        .addDecodingCapability(
                TpgFormatChecker.TPG,
                new TpgFormatChecker(),
                new FrescoTpgDecoder())
        // 配置 TPG 动图解码器
        .addDecodingCapability(
                TpgAnimatedFormatChecker.TPGAnimated,
                new TpgAnimatedFormatChecker(),
                new FrescoTpgAnimatedDecoder())
        .build();
// 配置 Image Pipeline
ImagePipelineConfig config = ImagePipelineConfig.newBuilder(context)
        .setImageDecoderConfig(imageDecoderConfig)
        .build();
// 初始化 Fresco
Fresco.initialize(context, config);
```

#### 单次请求配置

使用 Fresco 加载图片时配置，本次加载请求 TPG 解码器会生效。本次图片加载可以加载 TPG 图片。

```
Uri uri = Uri.parse("https://xxx.com/test.tpg");
SimpleDraweeView draweeView = (SimpleDraweeView) findViewById(R.id.my_image_view);
ImageRequest imageRequest = ImageRequestBuilder.newBuilderWithSource(uri)
                .setImageDecodeOptions(ImageDecodeOptions.newBuilder()
                        .setCustomImageDecoder(new FrescoTpgDecoder()) // 配置 TPG 静态解码器
                      //.setCustomImageDecoder(new FrescoTpgAnimatedDecoder()) // 配置 TPG 动图解码器
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

如果是全局配置 TPG 解码器，则直接使用 Fresco 加载图片即可。

```
Uri uri = Uri.parse("https://xxx.com/test.tpg");
SimpleDraweeView draweeView = (SimpleDraweeView) findViewById(R.id.my_image_view);
draweeView.setImageURI(uri);
```

然后是单次请求配置 TPG 解码器，则在加载请求中加入 TPG 解码器配置，代码示例如下：

```
Uri uri = Uri.parse("https://xxx.com/test.tpg");
SimpleDraweeView draweeView = (SimpleDraweeView) findViewById(R.id.my_image_view);
ImageRequest imageRequest = ImageRequestBuilder.newBuilderWithSource(uri)
                .setImageDecodeOptions(ImageDecodeOptions.newBuilder()
                        .setCustomImageDecoder(new FrescoTpgDecoder()) // 配置 TPG 静态解码器
                      //.setCustomImageDecoder(new FrescoTpgAnimatedDecoder()) // 配置 TPG 动图解码器
                        .build())
                .build();
AbstractDraweeController controller = Fresco.newDraweeControllerBuilder().setImageRequest(imageRequest).build();
draweeView.setController(controller);
```