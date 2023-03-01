
本文主要介绍如何使用 SDWebImage 加载图片。

## 基础图片处理

与 SDWebImage 配合使用数据万象基础图片处理操作（除 TPG、AVIF、WEBP 相关功能外）。

1. 在使用数据万象基础图片处理操作时，需要集成 CloudInfinite/SDWebImage-CloudInfinite 模块。
```
   pod 'CloudInfinite/SDWebImage-CloudInfinite'
```
2. 使用 UIImageView+CI，模仿 SDWebImage 调用风格，封装了一组可以传入 transform 的方法。
**Objective-C**
```
// 实例化 CITransformation 类并添加需要使用的操作；
CITransformation * transform = [CITransformation new];
// 加入缩放功能
[transform setZoomWithPercent:50 scaleType:ScalePercentTypeOnlyWidth];
// 加入圆角功能
[transform setCutWithRRadius:100];
// 根据实际需求加入相应的功能
...
// 使用 UIImageView+CI 类种方法，加载图片
[self.imageView sd_CI_setImageWithURL:[NSURL URLWithString:@"图片链接"] transformation:transform];
```
**swift**
```
// 实例化 CITransformation 类并添加需要使用的操作；
let transform = CITransformation();
// 加入缩放功能
transform.setZoomWithPercent(50, scale: ScalePercentType.onlyWidth)
// 加入圆角功能
transform.setCutWithRRadius(100)
// 根据实际需求加入相应的功能
...
// 使用 UIImageView+CI 类种方法，加载图片
imageView.sd_CI_setImage(with: NSURL.fileURL(withPath: "图片链接"), transformation: transform)
```

## 使用数据万象 TPG 功能

与 SDWebImage 配合使用数据万象 TPG 功能，支持 TPG 动图加载，无需额外处理。在使用 TPG 功能时，SDWebImage-CloudInfinite 需要依赖 CloudInfinite/TPG 模块。
```
pod 'CloudInfinite/TPG'
```
SDWebImage-CloudInfinite 提供了两种加载 TPG 图片的方式：

### 方式一：调用 UIImageView+CI 加载 TPG

**Objective-C**

```
// 构建 CITransformation实例
CITransformation * tran = [CITransformation new];

// 设置TPG格式以及传参方式
[tran setFormatWith:CIImageTypeTPG options:CILoadTypeUrlFooter];

// 调用UIImageView+CI 类种方法，加载图片
[self.imageView sd_CI_setImageWithURL:[NSURL URLWithString:@"图片链接"] transformation:transform];
```

**swift**

```
// 构建 CITransformation 实例
 let transform = CITransformation();

 // 设置 TPG 格式以及传参方式
transform.setFormatWith(CIImageFormat.typeTPG, options: CILoadTypeEnum.urlFooter);

 // 调用 UIImageView+CI 类种方法，加载图片
imageView.sd_CI_setImage(with: NSURL.init(string: "图片链接"), transformation: transform)
```

### 方式二：全局配置加载 TPG 

#### 适用场景

1. 如果整个项目都需要使用 TPG，或为已有项目接入 TPG。
2. 或者某些固定模式的图片链接需要使用 TPG。

#### 使用方法

**Objective-C**
```
// 在项目启动时给 CIDownloaderConfig 添加需要使用 TPG 图片的链接正则表达式；满足这个正则的图片链接都使用 TPG 格式加载；
// 所有图片都使用 TPG 加载
[[CIDownloaderConfig sharedConfig] addTPGRegularExpress:@"http(s)?:.*" paramsType:CILoadTypeUrlFooter];

// 如果有的链接不需要使用 TPG，给 CIDownloaderConfig 添加排除的正则；
// 请求图片主题色排除
[[CIDownloaderConfig sharedConfig] addExcloudeTPGRegularExpress:@"http(s)?:.*imageAve"];
```
**swift**
```
// 在项目启动时给 CIDownloaderConfig 添加需要使用 TPG 图片的链接正则表达式；满足这个正则的图片链接都使用 TPG 格式加载；
// 所有图片都使用 TPG 加载
CIDownloaderConfig.shared().addTPGRegularExpress("http(s)?:.*", paramsType: CILoadTypeEnum.urlFooter)

// 如果有的链接不需要使用 TPG，给 CIDownloaderConfig 添加排除的正则；
// 请求图片主题色排除
CIDownloaderConfig.shared().addExcloudeTPGRegularExpress("http(s)?:.*imageAve")
```


## 使用数据万象 WEBP 功能

与 SDWebImage 配合使用数据万象 WEBP 功能，支持 WEBP 动图加载，无需额外处理。
#### 准备工作
在使用 WEBP 功能时，SDWebImage-CloudInfinite 需要依赖 SDWebImageWebPCoder 库。
```
pod 'SDWebImageWebPCoder'
```

#### 加载 WEBP 图片

**Objective-C**

```
// 实例化 CITransformation 类
CITransformation * tran = [CITransformation new];
// 设置转换为 webp 格式
[tran setFormatWith:CIImageTypeWEBP options:CILoadTypeUrlFooter];
// 加载图片
[self.imageView sd_CI_setImageWithURL:[NSURL URLWithString:@"图片链接"] transformation:tran];
```

**swift**

```
// 构建 CITransformation 实例
let transform = CITransformation();

// 设置 TPG 格式以及传参方式
transform.setFormatWith(CIImageFormat.typeWEBP, options: CILoadTypeEnum.urlFooter);

// 调用 UIImageView+CI 类种方法，加载图片
imageView.sd_CI_setImage(with: NSURL.init(string: "图片链接"), transformation: transform)

```

## 使用数据万象 AVIF 功能

与 SDWebImage 配合使用数据万象 AVIF 功能，支持 AVIF 动图加载，无需额外处理。在使用 AVIF 功能时，SDWebImage-CloudInfinite 需要依赖 CloudInfinite/AVIF 模块。
```
pod 'CloudInfinite/AVIF'
```


### 调用 UIImageView+CI 加载 AVIF

**Objective-C**

```
// 构建 CITransformation实例
CITransformation * tran = [CITransformation new];

// 设置AVIF格式以及传参方式
[tran setFormatWith:CIImageTypeAVIF options:CILoadTypeUrlFooter];

// 调用UIImageView+CI 类种方法，加载图片
[self.imageView sd_CI_setImageWithURL:[NSURL URLWithString:@"图片链接"] transformation:transform];
```

**swift**

```
// 构建 CITransformation 实例
 let transform = CITransformation();

 // 设置 AVIF 格式以及传参方式
transform.setFormatWith(CIImageFormat.typeAVIF, options: CILoadTypeEnum.urlFooter);

 // 调用 UIImageView+CI 类种方法，加载图片
imageView.sd_CI_setImage(with: NSURL.init(string: "图片链接"), transformation: transform)
```

