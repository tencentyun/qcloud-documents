
本文主要介绍如何使用 Glide 加载图片。

## 安装 Glide

```
implementation 'com.github.bumptech.glide:glide:version'
```

## 基础图片处理

与 Glide 配合使用数据万象基础图片处理操作（除 TPG 和 AVIF 相关功能外）。

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

## 使用数据万象 Glide 功能

安装 cloud-infinite-glide SDK 以及 glide:compiler。
```
implementation 'com.qcloud.cos:cloud-infinite-glide:1.2.1'	
annotationProcessor 'com.github.bumptech.glide:compiler:version' 
```
通过 AppGlideModule 注册相关解码器和 loader 实现相应功能。
```
 // 注册自定义 GlideModule
 // 开发者应该创建此类注册 CIImageRequestModelLoader 和 ImageAveDecoder<br>
 // 类库开发者可以继承 LibraryGlideModule 创建类似的注册类
@GlideModule
public class MyAppGlideModule extends AppGlideModule {
    @Override
    public void registerComponents(@NonNull Context context, @NonNull Glide glide, Registry registry) {
        //注册支持 CIImageLoadRequest 的 loader
        registry.append(CIImageLoadRequest.class, InputStream.class, new CIImageRequestModelLoader.Factory());

        //注册主色解码器
        registry.append(InputStream.class, Bitmap.class, new ImageAveDecoder(glide.getBitmapPool()));
    }
}
```

#### 使用图片主色预加载

```
//先在 AppGlideModule 中注册主色解码器
registry.append(InputStream.class, Bitmap.class, new ImageAveDecoder(glide.getBitmapPool()));

//使用 glide 的 thumbnail 进行主色预加载
Glide.with(context)
               .load(imageUrl)
               .thumbnail(CloudInfiniteGlide.getImageAveThumbnail(context, imageUrl))
               .into(imageview);
```

#### 直接加载 CIImageLoadRequest

目前仅用于格式转换时，header 传输目标图片格式的情况。

```
registry.append(CIImageLoadRequest.class, InputStream.class, new CIImageRequestModelLoader.Factory());
```



