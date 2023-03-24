本文主要介绍如何使用 SDWebImage 加载图片。

## 使用数据万象 SDWebImage 功能
安装 SDWebImage-CloudInfinite
```
pod 'CloudInfinite/SDWebImage-CloudInfinite'
```

与 SDWebImage 配合使用数据万象基础图片处理操作（除 TPG 和 AVIF 相关功能外）。
UIImageView+CI，模仿 SDWebImage 调用风格，封装了一组可以传入 transform 的方法。
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


#### 使用图片主色预加载
**Objective-C**
```
// 实例化 CITransformation 类并添加需要使用的操作；
CITransformation * transform = [CITransformation new];
// 加入缩放功能
[tran setViewBackgroudColorWithImageAveColor:YES];
// 使用 UIImageView+CI 类种方法，加载图片
[self.imageView sd_CI_setImageWithURL:[NSURL URLWithString:@"图片链接"] transformation:transform];
```
**swift**
```
// 实例化 CITransformation 类并添加需要使用的操作；
let transform = CITransformation();
// 加入缩放功能
tran.setViewBackgroudColorWithImageAveColor(true);
// 使用 UIImageView+CI 类种方法，加载图片
self.imageView.sd_CI_setImage((with: NSURL.fileURL(withPath: "图片链接"), transformation: transform);
```