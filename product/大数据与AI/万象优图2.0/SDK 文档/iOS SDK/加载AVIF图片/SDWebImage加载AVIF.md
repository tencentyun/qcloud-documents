
本文提供加载网络以及使用 AVIF 模块两种方式加载 AVIF 图片。

### 安装 AVIF SDK

**使用 Cocoapods 集成**

>? 推荐使用 cocoapod 方式.

1. 在您工程 Podfile 文件中添加模块：
```
    pod 'CloudInfinite/SDWebImage-CloudInfinite'
    pod 'CloudInfinite/AVIF'
```
2. 在终端执行安装命令：
```
    pod install
```

### 使用SDWebImage 直接加载AVIF图片链接。
SDWebImage-CloudInfinite 模块在APP启动时已自动将AVIF解码器加入到SDWebImage解码器队列中，在加载解码器时自动找到AVIF解码器来解码图片。
支持动图，无需额外操作。
使用时与SDWebImage使用没有任何区别。
```
[imageView sd_setImageWithURL:[NSURL URLWithString:@"AVIF图片链接"]];
```
>? 图片链接可以携带万象处理参数。

### 使用SDWebImage指定加载AVIF格式并携带万象处理参数。
SDWebImage-CloudInfinite 中 UIImageView+CI类是模仿 SDWebImage 调用风格，封装了一组可以传入 transform 的方法。
```
// 构建 CITransformation实例
CITransformation * transform = [CITransformation new];

// 设置TPG格式以及传参方式
[transform setFormatWith:CIImageTypeAVIF options:CILoadTypeUrlFooter];
// transform 可以继续指定其他处理参数
[transform setXXXX:];
// 调用UIImageView+CI 类种方法，加载图片
[self.imageView sd_CI_setImageWithURL:[NSURL URLWithString:@"图片链接"] transformation:transform];
```


