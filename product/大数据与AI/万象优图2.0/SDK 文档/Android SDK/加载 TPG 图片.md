
本文提供加载网络以及加载本地两种方式加载 TPG 图片。


### 安装 TPG SDK

```
implementation 'com.qcloud.cos:tpg:1.3.2'    
```

安装时会自动包含 SO 库，建议在 Module 的 build.gradle 文件中使用 NDK 的“abiFilter”配置，设置支持的 SO 库架构。

```
defaultConfig {
    ndk {
        // 设置支持的 SO 库架构
        abiFilters 'armeabi' //, 'x86', 'armeabi-v7a', 'x86_64', 'arm64-v8a'
    }
}
```

### 方式一：加载网络 TPG 图片

1. 集成 cloud-infinite SDK。
```
implementation 'com.qcloud.cos:cloud-infinite:1.2.1'    
```
2. 在 cloud-infinite SDK 中构建出请求 TPG 格式图片的链接，然后与 [Glide 加载图片](https://cloud.tencent.com/document/product/460/47738)  配合使用，加载网络 TPG 图片。
```
// 实例化 CloudInfinite，用来构建请求图片请求连接；
CloudInfinite cloudInfinite = new CloudInfinite();
// 根据用户所选万象基础功能 options 进行 Transformation；
CITransformation transform = new CITransformation();
transform.format(CIImageFormat.TPG, CIImageLoadOptions.LoadTypeAcceptHeader);
// 构建图片 CIImageLoadRequest
CIImageLoadRequest request = cloudInfinite.requestWithBaseUrlSync(url, transform);
```

### 方式二：加载本地 TPG 图片

应用内置的资源，例如 assets、drawable、raw 等，使用 TPG 格式可以有利于减小安装包大小。

```
//加载 Assets 中的 TPG 图片
TpgImageLoader.displayWithAssets(imageview, assetsName);
//加载 Resource 中的 TPG 图片
TpgImageLoader.displayWithResource(imageview, R.drawable.tpg);
//加载本地文件中的 TPG 图片
TpgImageLoader.displayWithFileUri(imageview, fileUri);
```
