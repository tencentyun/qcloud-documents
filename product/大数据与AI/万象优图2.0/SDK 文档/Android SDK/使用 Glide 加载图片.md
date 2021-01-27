
本文主要介绍如何使用 Glide 加载图片。

## 安装 Glide

```
implementation 'com.github.bumptech.glide:glide:version'
```

## 基础图片处理

与 Glide 配合使用数据万象基础图片处理操作（除 TPG 相关功能外）。

1. 使用 CloudInfinite 和 CITransformation 构建 CIImageLoadRequest。
```
CloudInfinite cloudInfinite = new CloudInfinite();
CITransformation transform = new CITransformation();
transform.thumbnailByScale(50).iradius(60);
CIImageLoadRequest request = cloudInfinite.requestWithBaseUrlSync(url, transform);
```
2. 通过得到的 CIImageLoadRequest 获取 URL，使用 Glide 进行加载。
```
Glide.with(activity).load(request.getUrl().toString()).into(imageview);
```

## 使用数据万象 TPG 功能

安装 TPG SDK 和 cloud-infinite-glide SDK 以及 glide:compiler。
```
implementation 'com.tencent.qcloud:tpg:1.3.1'	
implementation 'com.tencent.qcloud:cloud-infinite-glide:1.2.0'	
annotationProcessor 'com.github.bumptech.glide:compiler:version' 
```
通过 AppGlideModule 注册相关解码器和 loader 实现相应功能。
```
 // 注册自定义 GlideModule
 // 开发者应该创建此类注册 CIImageRequestModelLoader 和 TpgDecoder、ByteBufferTpgGifDecoder<br>
 // 类库开发者可以继承 LibraryGlideModule 创建类似的注册类
@GlideModule
public class MyAppGlideModule extends AppGlideModule {
    @Override
    public void registerComponents(@NonNull Context context, @NonNull Glide glide, Registry registry) {
        //注册支持 CIImageLoadRequest 的 loader
        registry.prepend(CIImageLoadRequest.class, InputStream.class, new CIImageRequestModelLoader.Factory());

        /*------------------解码器 开始-------------------------*/
        //注册 TPG 静态图片解码器
        registry.prepend(InputStream.class, Bitmap.class, new TpgDecoder(glide.getBitmapPool()));
        //注册 TPG 动图解码器
        ByteBufferTpgGifDecoder byteBufferTpgGifDecoder = new ByteBufferTpgGifDecoder(context, glide.getBitmapPool());
        registry.prepend(InputStream.class, GifDrawable.class, new StreamTpgGifDecoder(byteBufferTpgGifDecoder));
        registry.prepend(ByteBuffer.class, GifDrawable.class, byteBufferTpgGifDecoder);
        //注册主色解码器
        registry.prepend(InputStream.class, Bitmap.class, new ImageAveDecoder(glide.getBitmapPool()));
        /*------------------解码器 结束-------------------------*/
    }
}
```

#### 加载静态 TPG 图片

```
registry.prepend(InputStream.class, Bitmap.class, new TpgDecoder(glide.getBitmapPool()));
```

#### 加载动图 GIF 类型 TPG 图片

```
ByteBufferTpgGifDecoder byteBufferTpgGifDecoder = new ByteBufferTpgGifDecoder(context, glide.getBitmapPool());
registry.prepend(InputStream.class, GifDrawable.class, new StreamTpgGifDecoder(byteBufferTpgGifDecoder));
registry.prepend(ByteBuffer.class, GifDrawable.class, byteBufferTpgGifDecoder);
```

#### 使用图片主色预加载

```
//先在 AppGlideModule 中注册主色解码器
registry.prepend(InputStream.class, Bitmap.class, new ImageAveDecoder(glide.getBitmapPool()));

//使用 glide 的 thumbnail 进行主色预加载
Glide.with(context)
               .load(imageUrl)
               .thumbnail(CloudInfiniteGlide.getImageAveThumbnail(context, imageUrl))
               .into(imageview);
```

#### 直接加载 CIImageLoadRequest

目前仅用于格式转换时，header 传输目标图片格式的情况。

```
registry.prepend(CIImageLoadRequest.class, InputStream.class, new CIImageRequestModelLoader.Factory());
```
