## AVIF 简介

AVIF 是一种基于 AV1 视频编码的新一代图像格式，相对于 JPEG、WEBP 这类图片格式来说，它的压缩率更高，并且画面细节更好。AVIF 格式适用于网络环境不稳定、流量不足等情况下访问图片的场景。AVIF 格式图片在保持图片质量不变的情况，尽可能的减小图片大小，以达到节省图片存储空间、减少图片访问流量、提升图片访问速度的效果。最关键的是，AV1 由谷歌发起的 AOM（开放媒体联盟）推动，在 VP9 的基础上继续演进，无专利授权费用（而且腾讯也是 AOM 的创始成员）。

## App 显示 AVIF 图片

由于 AVIF 目前只在 iOS16、Android12 上得到原生支持，要想覆盖所有主流机型，单靠原生支持肯定是不够的。因此需要客户端开发时集成 AVIF 解码器自行解码。一般做法是使用下面的解码库，自行编译 Android 和 iOS 解码器产物，以及写一些 JNI 代码，如果您的 App 使用 Glide、SDWebImage 等图片库，还需再按照图片库的要求进行封装集成。

- 业内开源编解码库：[开源编解码库](https://github.com/AOMediaCodec/libavif)。
- 腾讯自研编解码库：本文的数据万象 AVIF SDK 基于该编解码库。

显然，这种方法有不少的工作量，那么有没有更快的方法？您可以选择接入数据万象 AVIF SDK 提高工作效率。本文将为您介绍如何快速集成 AVIF 解码器，兼容所有机型。

## 数据万象 AVIF 图片 SDK

### Android 集成

#### 使用 Glide 图片库

1. 安装 Glide 和 AVIF SDK
```
implementation 'com.qcloud.cos:avif:1.1.0'   
implementation 'com.github.bumptech.glide:glide:version'
annotationProcessor 'com.github.bumptech.glide:compiler:version' 
```

2. 注册解码器 GlideModule
```
// 注册自定义 GlideModule
// 开发者应该创建此类注册相关解码器
// 类库开发者可以继承 LibraryGlideModule 创建类似的注册类
@GlideModule
public class MyAppGlideModule extends AppGlideModule {
    @Override
    public void registerComponents(@NonNull Context context, @NonNull Glide glide, Registry registry) {
        /*------------------解码器 开始-------------------------*/
        //注册 AVIF 静态图片解码器
        registry.prepend(Registry.BUCKET_BITMAP, InputStream.class, Bitmap.class, new StreamAvifDecoder(glide.getBitmapPool(), glide.getArrayPool()));
        registry.prepend(Registry.BUCKET_BITMAP, ByteBuffer.class, Bitmap.class, new ByteBufferAvifDecoder(glide.getBitmapPool()));
        //注册 AVIF 动图解码器
        registry.prepend(InputStream.class, AvifSequenceDrawable.class, new StreamAvifSequenceDecoder(glide.getBitmapPool(), glide.getArrayPool()));
        registry.prepend(ByteBuffer.class, AvifSequenceDrawable.class, new ByteBufferAvifSequenceDecoder(glide.getBitmapPool()));
        /*------------------解码器 结束-------------------------*/
    }
}
```

3. 使用 Glide 加载图片
   像普通 jpg、png 图片那样加载图片即可，请参见 [Glide 官方文档](https://bumptech.github.io/glide/)。
```
Glide.with(context).load(url).into(imageView);
```

#### 使用 Fresco 图片库

1. 安装 Fresco 和 AVIF SDK
```
implementation 'com.qcloud.cos:avif:1.1.0'   
implementation 'com.facebook.fresco:fresco:version'
// 如果需要支持 avif 动图解码器 则需要加上 fresco:animated-base 依赖
implementation 'com.facebook.fresco:animated-base:version'
```

2. 配置解码器
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

3. 使用 Fresco 加载图片
   像普通 jpg png 图片那样加载图片即可，请参见 [Fresco 官方文档](https://frescolib.org/docs/index.html)。
```
<com.facebook.drawee.view.SimpleDraweeView
    android:id="@+id/my_image_view"
    android:layout_width="130dp"
    android:layout_height="130dp"
    fresco:placeholderImage="@drawable/my_drawable"
  />


Uri uri = Uri.parse("https://xxx.com/test.avif");
SimpleDraweeView draweeView = (SimpleDraweeView) findViewById(R.id.my_image_view);
draweeView.setImageURI(uri);
```

### iOS 集成

1. 安装 SDWebImage 和 AVIF SDK
   在您工程 Podfile 文件中添加模块：
```
pod 'CloudInfinite/SDWebImage-CloudInfinite'
pod 'CloudInfinite/AVIF'
```
在终端执行安装命令：
```
pod install
```

2. 使用 SDWebImage 直接加载 AVIF 图片
   SDWebImage-CloudInfinite 模块在 App 启动时已自动将 AVIF 解码器加入到 SDWebImage 解码器队列中，在加载解码器时自动找到 AVIF 解码器来解码图片。支持动图，无需额外操作。使用时与 SDWebImage 使用没有任何区别。
   Objective-C：
```
[imageView sd_setImageWithURL:[NSURL URLWithString:@"AVIF 图片链接"]];
```
Swift：
```
UIImageView() .sd_setImage(with: NSURL.init(string: "AVIF 图片链接"))
```

## 数据万象 AVIF SDK 其他功能

### 基础解码器

用于直接将 AVIF 数据解码为 bitmap、UIImage，以及判断图片数据是否为 AVIF 格式。

Android：

```
import com.tencent.qcloud.image.avif.Avif;

// 图片的字节数组
byte[] buffer = new byte[XXX];
// 是否是 AVIF 格式
boolean isAvif = Avif.isAvif(buffer);
// 是否是 AVIF 动图 
boolean isAvis = Avif.isAvis(buffer);

// 原图解码
Bitmap bitmap = Avif.decode(buffer);

// 宽度等比解码
// 目标宽度
int dstWidth = 500; 
Bitmap bitmap = Avif.decode(buffer, dstWidth);

// 区域缩放解码
// 区域左上角x坐标
int x = 0;
// 区域左上角y坐标
int y = 0;
// 区域宽度
int width = 100;
// 区域高度
int height = 100;
// 缩放比, 大于1的时候才生效，小于等于1的情况下不作缩放
int inSampleSize = 2;
Bitmap bitmap = Avif.decode(buffer, x, y, width, height, inSampleSize);
```

iOS：

```
#import "AVIFDecoderHelper.h"
#import "UIImage+AVIFDecode.h"

//判断是否是 AVIF 格式以及动图格式
// data为图片NSData类型数据
BOOL isAVIF = [AVIFDecoderHelper isAVIFImage:data];

//解码 AVIF 图片
// data为图片NSData类型数据
UIImage * image = [UIImage AVIFImageWithContentsOfData:data];

/ data为图片NSData类型数据
// 缩小两倍 并指定解码的范围( rect 以原图为基准)
UIImage * image = [UIImage AVIFImageWithContentsOfData:imageData scale:2 rect:CGRectMake(x, y, width, height)];
```

### Android 超大图采样图片库

1. 安装 subsampling-scale-image-view 和 AVIF SDK
```
implementation 'com.qcloud.cos:avif:1.1.0'   

implementation 'com.davemorrissey.labs:subsampling-scale-image-view:3.10.0'

// AndroidX 请使用
// implementation 'com.davemorrissey.labs:subsampling-scale-image-view-androidx:3.10.0'
```

2. 获取 SubsamplingScaleImageView 控件并注册解码器
```
SubsamplingScaleImageView subsamplingScaleImageView = findViewById(R.id.subsampling_scale_image_view);

// 设置 AVIF 图片解码器
subsamplingScaleImageView.setBitmapDecoderClass(AvifSubsamplingImageDecoder.class);
subsamplingScaleImageView.setRegionDecoderClass(AvifSubsamplingImageRegionDecoder.class);
```

3. 使用 subsampling-scale-image-view 加载图片
   像普通 jpg、png 图片那样加载图片即可，请参见 [subsampling-scale-image-view 官方文档](https://github.com/davemorrissey/subsampling-scale-image-view)。
```
// 加载 uri 图片
subsamplingScaleImageView.setImage(ImageSource.uri(uri));

// 加载 assets 图片
subsamplingScaleImageView.setImage(ImageSource.asset("test.avif"));

// 加载 resource 图片
subsamplingScaleImageView.setImage(ImageSource.resource(R.raw.avif));
```

## 总结

数据万象 AVIF SDK 封装了 AVIF 解码器、Android iOS 常用的图片库生态，直接使用数据万象 AVIF SDK 即可帮您轻松实现将 AVIF 图片显示到 App 中。更加详细的使用说明，请参考 [数据万象 Android SDK](https://cloud.tencent.com/document/product/460/87905)、[数据万象 iOS SDK](https://cloud.tencent.com/document/product/460/88480)。
