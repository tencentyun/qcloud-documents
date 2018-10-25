## 一、支持的平台
- SDK支持iOS 7.0及以上系统。

## 二、开发环境
- Xcode 7或更高版本；
- iOS SDK 7.0或更高版本。

## 三、Xcode工程设置
下面通过一个简单的Single View Application工程，说明如何在Xcode工程中集成SDK。
### 1、拷贝SDK文件
在本例中，工程的名字叫做HelloSDK，如下图所示，将《[下载SDK](http://cloud.tencent.com/doc/product/268/%E4%B8%8B%E8%BD%BDSDK%EF%BC%88iOS%EF%BC%89)》中那个包含所有Framework的libs文件夹拷贝到工程文件夹：
![](//mccdn.qcloud.com/static/img/7a8b064e23365eeffefa67626d476147/image.png)

### 2、设置Framework Search Paths
如下图所示，在Build Settings > Search Paths > Framework Search Paths中添加$(PROJECT_DIR)/libs：
![](//mccdn.qcloud.com/static/img/0fdb7f23372c3c75a4c2da3b2261950d/image.png)

### 3、添加SDK Framework
如下图所示，将SDK Framework添加到工程：
![](//mccdn.qcloud.com/static/img/2331e2f9a7be2af9c623dc71c6d8e453/image.png)

### 4、添加其他系统库
如下图所示，将SDK依赖的系统库也添加到工程：
![](//mccdn.qcloud.com/static/img/3a161b0ef3c70f6cfb03441786697705/image.png)
SDK依赖的系统库，按音序排列如下：
> 1. AVFoundation.framework
> 2. AudioToolBox.framework
> 3. CoreGraphics.framework
> 4. CoreMedia.framework
> 5. CoreTelephony.framework
> 6. CoreVideo.framework
> 7. Foundation.framework
> 8. libstdc++.6.tbd
> 9. libsqlite3.tbd
> 10. libz.tbd
> 11. libiconv.tbd
> 12. libc++.tbd
> 13. UIKit.framework


### 5、关闭Bitcode
SDK不支持Bitcode，如下图所示，将Build Setting > Build Options > Enable Bitcode设置为No：
![](//mccdn.qcloud.com/static/img/c9967ba6ceb232d1cc4fd27bda7f541a/image.png)

## 四、验证
下面在HelloSDK的代码中，调用SDK的接口，获取SDK版本信息，以验证工程设置是否正确。
### 1、引用头文件
在ViewController.m开头引用SDK的头文件：
`#import "QAVSDK/QAVSDK.h"`

### 2、添加调用代码
在viewDidLoad方法中添加代码：
```
- (void)viewDidLoad {
    [super viewDidLoad];
    // 打印SDK的版本信息
    NSLog(@"SDK Version = %@", [QAVContext getVersion]);
}
```
### 3、编译运行
如果前面各个步骤都操作正确的话，HelloSDK工程应该可以顺利编译通过。在Debug模式下运行APP，Xcode的Console窗格会打印出SDK的版本信息。
> 2016-04-26 11:35:05.807 HelloSDK[5288:358268] SDK Version = 1.8.0.258
