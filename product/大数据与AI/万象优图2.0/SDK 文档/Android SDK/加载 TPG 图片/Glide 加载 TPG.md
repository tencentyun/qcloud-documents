
本文主要介绍如何使用 Glide 加载 TPG 图片。


### 安装 Glide 和 TPG SDK

Glide是一个知名开源的图片缓存库。更多信息，请参见 [Glide 官方文档](https://bumptech.github.io/glide/)。

```
implementation 'com.qcloud.cos:tpg:1.3.8' 
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
        //注册 TPG 静态图片解码器
        registry.prepend(Registry.BUCKET_BITMAP, InputStream.class, Bitmap.class, new StreamTpgDecoder(glide.getBitmapPool(), glide.getArrayPool()));
        registry.prepend(Registry.BUCKET_BITMAP, ByteBuffer.class, Bitmap.class, new ByteBufferTpgDecoder(glide.getBitmapPool()));
        //注册 TPG 动图解码器
        registry.prepend(InputStream.class, TpgSequenceDrawable.class, new StreamTpgSequenceDecoder(glide.getBitmapPool(), glide.getArrayPool()));
        registry.prepend(ByteBuffer.class, TpgSequenceDrawable.class, new ByteBufferTpgSequenceDecoder(glide.getBitmapPool()));
        /*------------------解码器 结束-------------------------*/
    }
}
```

#### 注册静态 TPG 图片解码器

```
registry.prepend(Registry.BUCKET_BITMAP, InputStream.class, Bitmap.class, new StreamTpgDecoder(glide.getBitmapPool(), glide.getArrayPool()));
registry.prepend(Registry.BUCKET_BITMAP, ByteBuffer.class, Bitmap.class, new ByteBufferTpgDecoder(glide.getBitmapPool()));
```

#### 注册动图类型 TPG 图片解码器

```
registry.prepend(InputStream.class, TpgSequenceDrawable.class, new StreamTpgSequenceDecoder(glide.getBitmapPool(), glide.getArrayPool()));
registry.prepend(ByteBuffer.class, TpgSequenceDrawable.class, new ByteBufferTpgSequenceDecoder(glide.getBitmapPool()));
```

### 步骤二：使用 Glide 加载图片

更多信息，请参见 [Glide 官方文档](https://bumptech.github.io/glide/)。

```
Glide.with(context).load(url).into(imageView);
```