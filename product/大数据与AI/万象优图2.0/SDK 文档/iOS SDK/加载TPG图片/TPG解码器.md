
本文提供直接使用解码器解码 TPG 图片的方法以及简单加载本地 TPG 图片。

### 安装 TPG SDK

**使用 Cocoapods 集成**

1. 在您工程 Podfile 文件中添加模块：
```
    pod 'CloudInfinite/TPG'
```
2. 在终端执行安装命令：
```
    pod install
```

### 直接使用解码器解码
- 判断是否是 TPG 格式以及动图格式。
```
#import "TPGDecoderHelper.h"

// data为图片NSData类型数据
BOOL isTPG = [TPGDecoderHelper isTPGImage:data];
```

- 解码 TPG 图片。
```
#import "UIImage+TPGDecode.h"

// data为图片NSData类型数据
UIImage * image = [UIImage TPGImageWithContentsOfData:data];
```

- TPG图片局部解码
针对TPG超大图处理，解码器提供局部解码功能以及指定缩放因子解码。

```
#import "UIImage+TPGDecode.h"

// data为图片NSData类型数据
// 缩小两倍 并指定解码的范围(rect以原图为基准)
UIImage * image = [UIImage TPGImageWithContentsOfData:imageData scale:2 rect:CGRectMake(x, y, width, height)];
```

### 简单加载本地图
```
// 加载本地文件
[cell.imageView setTpgImageWithPath:[NSURL URLWithString:@"本地文件路径"] loadComplete:^(NSData * _Nullable data, UIImage * _Nullable image, NSError * _Nullable error) {
        
}];
// 加载图片data数据
[cell.imageView setTpgImageWithData:图片data数据 loadComplete:^(NSData * _Nullable data, UIImage * _Nullable image, NSError * _Nullable error) {
        
}];
```
