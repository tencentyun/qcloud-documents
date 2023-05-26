
本文将介绍如何使用 SDWebImage 加载网络 TPG 图片。

### 安装 TPG SDK

**使用 Cocoapods 集成**

1. 在您工程 Podfile 文件中添加模块：
```
    pod 'CloudInfinite/SDWebImage-CloudInfinite'
    pod 'CloudInfinite/TPG'
```
2. 在终端执行安装命令：
```
    pod install
```
### 使用 SDWebImage 直接加载 TPG 图。
SDWebImage-CloudInfinite 模块在app启动时已自动将 TPG 解码器加入到 SDWebImage 解码器队列中，在加载解码器时自动找到 TPG 解码器来解码图片。支持动图，无需额外操作。使用时与 SDWebImage 使用没有任何区别。

**Objective-C**
```
[imageView sd_setImageWithURL:[NSURL URLWithString:@"TPG 图片链接"]];
```

**swift**
```
UIImageView() .sd_setImage(with: NSURL.init(string: ""))
```
>? 图片链接可以携带万象处理参数。

### 使用 SDWebImage 指定加载 TPG 格式并携带万象处理参数。
SDWebImage-CloudInfinite 中 UIImageView+CI 类是模仿 SDWebImage 调用风格，封装了一组可以传入 transform 的方法。

**Objective-C**
```
// 构建 CITransformation实例
CITransformation * transform = [CITransformation new];

// 设置TPG格式以及传参方式
[transform setFormatWith:CIImageTypeTPG options:CILoadTypeUrlFooter];
// transform 可以继续指定其他处理参数
[transform setXXXX:];
// 调用UIImageView+CI 类种方法，加载图片
[self.imageView sd_CI_setImageWithURL:[NSURL URLWithString:@"图片链接"] transformation:transform];
```

**swift**
```
let transform = CITransformation();
transform.setFormatWith(CIImageFormat.typeTPG, options: CILoadTypeEnum.urlFooter);
transform.setXXXX();
UIImageView().sd_CI_setImage(with: NSURL.init(string: "图片链接"), transformation: transform)
```


