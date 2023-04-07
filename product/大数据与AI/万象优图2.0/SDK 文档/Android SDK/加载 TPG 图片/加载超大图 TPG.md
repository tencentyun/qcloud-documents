
本文主要介绍如何使用 subsampling-scale-image-view 加载 TPG 超大图片。


### 安装 subsampling-scale-image-view 和 TPG SDK

subsampling-scale-image-view是一个知名开源的图片缓存库。更多信息，请参见 [官方文档](https://github.com/davemorrissey/subsampling-scale-image-view)。

```
implementation 'com.qcloud.cos:tpg:1.3.8' 

implementation 'com.davemorrissey.labs:subsampling-scale-image-view:3.10.0'

// AndroidX请使用
// implementation 'com.davemorrissey.labs:subsampling-scale-image-view-androidx:3.10.0'
```

### 步骤一：获取 SubsamplingScaleImageView 控件

```
SubsamplingScaleImageView subsamplingScaleImageView = findViewById(R.id.subsampling_scale_image_view);
```

### 步骤二：注册解码器

```
// 设置TPG图片解码器
subsamplingScaleImageView.setBitmapDecoderClass(TpgSubsamplingImageDecoder.class);
subsamplingScaleImageView.setRegionDecoderClass(TpgSubsamplingImageRegionDecoder.class);
```

如果要切换会普通图片加载，请切换会默认解码器，如下：
```
// 设置普通图片解码器
subsamplingScaleImageView.setBitmapDecoderClass(SkiaImageDecoder.class);
subsamplingScaleImageView.setRegionDecoderClass(SkiaImageRegionDecoder.class);
```

### 步骤三：使用 subsampling-scale-image-view 加载图片

更多信息，请参见 [subsampling-scale-image-view 官方文档](https://github.com/davemorrissey/subsampling-scale-image-view)。

```
// 加载 uri 图片
subsamplingScaleImageView.setImage(ImageSource.uri(uri));

// 加载 assets 图片
subsamplingScaleImageView.setImage(ImageSource.asset("test.tpg"));

// 加载 resource 图片
subsamplingScaleImageView.setImage(ImageSource.resource(R.raw.tpg));
```