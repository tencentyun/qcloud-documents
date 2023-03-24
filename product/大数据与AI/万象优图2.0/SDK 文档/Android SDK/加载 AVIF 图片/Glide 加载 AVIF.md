
本文主要介绍如何使用 Glide 加载 AVIF 图片。


### 安装 Glide 和 AVIF SDK

Glide是一个知名开源的图片缓存库。更多信息，请参见 [Glide 官方文档](https://bumptech.github.io/glide/)。

```
implementation 'com.qcloud.cos:avif:1.1.0'   
implementation 'com.github.bumptech.glide:glide:version'
annotationProcessor 'com.github.bumptech.glide:compiler:version' 
```

### 步骤一：注册解码器 GlideModule

通过 AppGlideModule 注册相关解码器实现相应功能。
```
 // 注册自定义 GlideModule
 // 开发者应该创建此类注册相关解码器<br>
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

#### 注册静态 AVIF 图片解码器

```
registry.prepend(Registry.BUCKET_BITMAP, InputStream.class, Bitmap.class, new StreamAvifDecoder(glide.getBitmapPool(), glide.getArrayPool()));
registry.prepend(Registry.BUCKET_BITMAP, ByteBuffer.class, Bitmap.class, new ByteBufferAvifDecoder(glide.getBitmapPool()));
```

#### 注册动图类型 AVIF 图片解码器

```
registry.prepend(InputStream.class, AvifSequenceDrawable.class, new StreamAvifSequenceDecoder(glide.getBitmapPool(), glide.getArrayPool()));
registry.prepend(ByteBuffer.class, AvifSequenceDrawable.class, new ByteBufferAvifSequenceDecoder(glide.getBitmapPool()));
```

### 步骤二：使用 Glide 加载图片

更多信息，请参见 [Glide 官方文档](https://bumptech.github.io/glide/)。

```
Glide.with(context).load(url).into(imageView);
```