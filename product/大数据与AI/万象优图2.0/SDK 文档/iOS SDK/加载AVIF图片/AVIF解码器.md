
本文提供直接使用解码器解码 AVIF 图片的方法以及简单加载本地 AVIF 图片。

### 安装 AVIF SDK

**使用 Cocoapods 集成**

1. 在您工程 Podfile 文件中添加模块：
```
    pod 'CloudInfinite/AVIF'
```
2. 在终端执行安装命令：
```
    pod install
```

### 直接使用解码器解码
- 判断是否是 AVIF 格式以及动图格式。

**Objective-C**
```
#import "AVIFDecoderHelper.h"

// data为图片NSData类型数据
BOOL isAVIF = [AVIFDecoderHelper isAVIFImage:data];
```
**swift**
```
let isAVIF = AVIFDecoderHelper.isAVIFImage(data);
```

- 解码 AVIF 图片。

**Objective-C**
```
#import "UIImage+AVIFDecode.h"

// data为图片NSData类型数据
UIImage * image = [UIImage AVIFImageWithContentsOfData:data];
```
**swift**
```
let image = UIImage.avifImage(withContentsOf: data);
```

- AVIF图片局部解码
针对AVIF超大图处理，解码器提供局部解码功能以及指定缩放因子解码。

**Objective-C**
```
#import "UIImage+AVIFDecode.h"

// data为图片NSData类型数据
// 缩小两倍 并指定解码的范围( rect 以原图为基准)
UIImage * image = [UIImage AVIFImageWithContentsOfData:imageData scale:2 rect:CGRectMake(x, y, width, height)];
```

**swift**
```
let image = UIImage.avifImage(withContentsOf: imageData, scale: 2, rect: CGRect.init(x: 0, y: 0, width: 100, height: 100));
```

### 简单加载本地图

**Objective-C**
```
// 加载本地文件
[cell.imageView setAvifImageWithPath:[NSURL URLWithString:@"本地文件路径"] loadComplete:^(NSData * _Nullable data, UIImage * _Nullable image, NSError * _Nullable error) {
        
}];
// 加载图片data数据
[cell.imageView setAvifImageWithData:图片data数据 loadComplete:^(NSData * _Nullable data, UIImage * _Nullable image, NSError * _Nullable error) {
        
}];
```

**swift**
```
UIImageView() .setAvifImageWithPath(NSURL.fileURL(withPath: ""))
UIImageView() .setAvifImageWith(data)
```