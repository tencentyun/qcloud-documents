
本文主要介绍如何使用 Glide 加载 AVIF 图片。


### 安装 Glide 和 AVIF SDK

Glide 是一个知名开源的图片缓存库。更多信息，请参见 [Glide 官方文档](https://bumptech.github.io/glide/)。

```
implementation 'com.qcloud.cos:avif:1.1.1'   
//如果出现beacon灯塔冲突，引入-nobeacon即可
//implementation 'com.qcloud.cos:avif-nobeacon:1.1.1'

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

### 设置加载失败后原图重试

>! AVIF SDK 版本需要大于等于 v1.1.1。

当 AVIF 图片加载失败时，自动请求原格式图片，提升用户体验。并将 AVIF 图片加载失败原因返回，用于排查失败原因及时修复。

1. 全局设置：在 AppGlideModule 中通过 GlideBuilder.addGlobalRequestListener 方法设置 GlobalOriginalImageRetryRequestListener 实现原图重试功能。

```
 // 注册自定义 GlideModule
 // 类库开发者可以继承 LibraryGlideModule 创建类似的注册类
@GlideModule
public class MyAppGlideModule extends AppGlideModule {
        @Override
    public void applyOptions(@NonNull final Context context, @NonNull GlideBuilder builder) {
        super.applyOptions(context, builder);
        // 原图兜底监听器
        GlideOriginalImageRetry.GlobalOriginalImageRetryRequestListener originalImageRetry = new GlideOriginalImageRetry.GlobalOriginalImageRetryRequestListener();
        originalImageRetry.setOriginalImageRetryCallback(new GlideOriginalImageRetryCallback() {
            @Nullable
            @Override
            public String buildOriginalImageUrl(String urlStr) {
                // 使用默认的原图格式
                return null;
            }

            @Override
            public void onFailureBeforeRetry(@Nullable GlideException e, Object model, Target<?> target, boolean isFirstResource) {
                // AVIF加载失败在这里上报，统计原图兜底次数和AVIF解码异常信息(不影响真正的图片加载失败率)
                Log.d(TAG, "AVIF onLoadFailed："+ model);
                if (e != null) {
                    Log.d(TAG, e.getMessage());
                    e.printStackTrace();
                }
            }

            @Override
            public void onLoadFailed(@Nullable GlideException e, Object model, Target<?> target, boolean isFirstResource) {
                //真正的加载失败在这里上报(影响真正的图片加载成功失败率)
                Log.d(TAG, "Image onLoadFailed："+ model);
                if (e != null) {
                    Log.d(TAG, e.getMessage());
                    e.printStackTrace();
                }
            }

            @Override
            public void onResourceReady(Object resource, Object model, Target<?> target, DataSource dataSource, boolean isFirstResource) {
                //真正的加载成功在这里上报(影响真正的图片加载成功失败率)
                Log.d(TAG, "Image onLoadSuccess："+ model);
            }
        });

        builder.addGlobalRequestListener(originalImageRetry);
    }
}
```

2. 局部设置：在图片加载过程中通过 RequestBuilder.addListener 方法设置 OriginalImageRetryRequestListener 实现原图重试功能。

```
// 图片加载的Options(没有的话可以不设置)
RequestOptions requestOptions = new RequestOptions()
        .placeholder(R.drawable.placeholder)
        .error(R.drawable.error);
// 图片加载的监听器列表(没有的话可以不设置)
List<RequestListener<Drawable>> requestListeners = new ArrayList<>();
requestListeners.add(new RequestListener<Drawable>() {
    @SuppressLint("DefaultLocale")
    @Override
    public boolean onLoadFailed(@Nullable GlideException e, Object model, Target<Drawable> target, boolean isFirstResource) {
        // 其他业务onLoadFailed
        return false;
    }
    @SuppressLint("DefaultLocale")
    @Override
    public boolean onResourceReady(Drawable resource, Object model, Target<Drawable> target, DataSource dataSource, boolean isFirstResource) {
        // 其他业务onResourceReady
        return false;
    }
});
// 原图兜底监听器
GlideOriginalImageRetry.OriginalImageRetryRequestListener originalImageRetry = new GlideOriginalImageRetry.OriginalImageRetryRequestListener();
originalImageRetry.setRequestOptions(requestOptions);
originalImageRetry.setRequestListeners(requestListeners);
originalImageRetry.setOriginalImageRetryCallback(new GlideOriginalImageRetryCallback() {
    @Nullable
    @Override
    public String buildOriginalImageUrl(String urlStr) {
        // 使用默认的原图格式
        return null;
    }
    @Override
    public void onFailureBeforeRetry(@Nullable GlideException e, Object model, Target<?> target, boolean isFirstResource) {
        // AVIF加载失败在这里上报，统计原图兜底次数和AVIF解码异常信息(不影响真正的图片加载失败率)
        Log.d(TAG, "AVIF onLoadFailed："+ model);
        if (e != null) {
            Log.d(TAG, e.getMessage());
            e.printStackTrace();
        }
    }
    @Override
    public void onLoadFailed(@Nullable GlideException e, Object model, Target<?> target, boolean isFirstResource) {
        //真正的加载失败在这里上报(影响真正的图片加载成功失败率)
        Log.d(TAG, "Image onLoadFailed："+ model);
        if (e != null) {
            Log.d(TAG, e.getMessage());
            e.printStackTrace();
        }
    }
    @Override
    public void onResourceReady(Object resource, Object model, Target<?> target, DataSource dataSource, boolean isFirstResource) {
        //真正的加载成功在这里上报(影响真正的图片加载成功失败率)
        Log.d(TAG, "Image onLoadSuccess："+ model);
    }
});
String imgUrl = "https://www.test.com/test.avif";
// 加载图片
RequestBuilder<Drawable> requestBuilder = Glide.with(this)
        .load(imgUrl)
        .apply(requestOptions)
        .addListener(originalImageRetry);
for (RequestListener<Drawable> listener : requestListeners){
    requestBuilder.addListener(listener);
}
requestBuilder.into(imageView);
```