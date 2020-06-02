## iOS SDK 介绍

### 内容
- libQBarCode.a - 静态文件，是主要扫码逻辑库
- ncnn.framework - 高性能神经网络前向计算框架
- Auth.framework - 授权模块
- QbarCodeRes.bundle - 资源文件
- include - 头文件

### 功能
实时识别二维码/条形码，图形二维码/条形码的识别、检测。

### 环境依赖
SDK 适用于 iOS 9.0 及以上的版本。

### SDK 来源
SDK 可在 [智能扫码控制台](https://console.cloud.tencent.com/ocr/is) 申请后下载。

## iOS SDK 接入步骤
1. 将 framework 静态文件资源包引入项目中，已经添加 include 头文件引用。
2. 引入系统的 framework

```
- ImageIo.framework
- CoreTelephony.framework
- security.framework
- SystemConfiguration.framework
- Accelerate.framework
- CoreVideo.framework
- CoreMedio.framework
- Foundation.framework
- UIKit.framework
- AVFoundation.framework
- QuartzCore.framework
- Accelerate.framework
- CoreGraphics.framework

```

3. 添加编译选项


- Compile Sources As 设置 Objective-C++
- C++ standardLibrary libc++(LVVM C++ standard library with c++ 11 support)
- bitCode 设置为 NO(暂不支持bitcode)
权限设置
需要 Iphone 手机联网授权 - 摄像头权限、访问相册权限。

```
<key>Privacy - Camera Usage Description</key>
<string>扫码需要开启您的摄像头权限，用于识别</string>
<key>Privacy - Photo Library Usage Description</key>
<string>扫码需要您开启相册权限，浏览您的照片</string>

```

如果您使用 HTTP 访问服务器，需要做如下配置（否则不需要）：

```
<key>NSAppTransportSecurity</key>
<dict>
<key>NSAllowArbitraryLoads</key>
<true/>
</dict>
```

4. 初始化 SDK

```
#import "QBarCodeKit.h"
//在需要调用的 ViewController 设置代理 QBarCodeKitSDKDelegate
@interface HomeViewController ()<QBarCodeKitSDKDelegate>{
    QBarCodeKit *sdk;
}
- (instancetype)init{
    self = [super init];
    if (self) {
        sdk = [QBarCodeKit sharedInstance];//获取实例
      //设置密钥
        [sdk startQBarCodeProcessWithSecretId:SECRET_ID secretKey:SECRET_KEY delegate:self];
    }
    return self;
}

```

5. 进入 SDK 页面

```
UIBarButtonItem *backBtn = [[UIBarButtonItem alloc] init];
backBtn.image = nil;
backBtn.title = @"返回";
self.navigationItem.backBarButtonItem = backBtn;
[sdk startQBarScanWithParentViewController:self];

```

6. SDK 结果回调

```
- (void)onResultBack:(nonnull NSDictionary *)result {
    NSString *errCode = result[@"errorcode"];
    if ([errCode isEqualToString:@"0"]) {//识别成功
        NSArray *contentArr = result[@"errormsg"];
        NSString *msg = nil;
        if ([contentArr count] >0) {
           msg = [contentArr objectAtIndex:0];
           [[NSOperationQueue mainQueue] addOperationWithBlock:^{
               // UI 更新代码
               [self showAlertView:msg];
           }];
        } else {
           msg = @"NO DATA";
           [[NSOperationQueue mainQueue] addOperationWithBlock:^{
               // UI 更新代码
               [self showAlertView:msg];
           }];
        }
    } else { // 结果返回错误信息
        NSString *msg = result[@"errormsg"];
        [[NSOperationQueue mainQueue] addOperationWithBlock:^{
                // UI 更新代码
            [self.showTextVoew setText:msg];
            [self showAlertView:msg];
        }];
    }
}

```





