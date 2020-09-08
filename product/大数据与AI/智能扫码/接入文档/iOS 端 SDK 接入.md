## 开发准备

1. 注册腾讯云账号，提交智能扫码服务的申请，等待审核通过后，获得专属密钥。（申请地址：[智能扫码申请](https://console.cloud.tencent.com/ocr/is)）。

2. 从 SDK 下载链接中下载智能扫码 SDK 到本地准备集成。

   

## iOS 端智能扫码 SDK 接入流程

### iOS 端智能扫码 SDK 介绍

SDK 中包含了三个文件和一个文件夹，分别是 **libQBarCode.a**、**ncnn.framework**、**QbarCodeRes.bundle** 和 **include** 包含的头文件。

- libQBarCode.a - 静态文件，是主要的扫码逻辑库
- ncnn.framework - 高性能神经网络前向计算框架
- QbarCodeRes.bundle - 资源文件
- include - 包含接入所需头文件



### 环境依赖

当前 iOS 端智能扫码 SDK 版本适用于 iOS 9.0 及以上的版本。



### 接入步骤

1. 将 **ncnn.framework**、**libQBarCode.a**、**QbarCodeRes.bundle** 添加至项目中，并且 **include** 头文件也添加到项目中。

2. 引入系统的 framework 

   **CoreTelephony.framework**

   **Security.framework**

   **SystemConfiguration.framework**

   **Accelerate.framework**

   **CoreVideo.framework**

   **CoreMedia.framework**

   **Foundation.framework**

   **UIKit.framework**

   **AVFoundation.framework**

   **QuartzCore.framework**

   **Accelerate.framework**
   
   **CoreGraphics.framework**

   ![img](https://main.qcloudimg.com/raw/fa45a18ac4b6287c4aa0053996c948ed.png)            

3. 添加编译选项


- 将 **Compile Sources As** 设置为 **Objective-C++**
![img](https://main.qcloudimg.com/raw/6af43e9c335be5373d7ba0ccdd9e2f10.png)

- 将 **C++ standardLibrary** 设置为 **libc++(LVVM C++ standard library with c++ 11 support)**            
![img](https://main.qcloudimg.com/raw/ce0e9bd18173e14354633c4dc78c16a1.png)

- 将 **bitCode** 设置为 **NO**(不支持 bitcode)
- 将 **Other Linker Flags** 设置为 **\-lz**


4. 权限设置

   智能扫码 SDK 需要手机网络、 摄像头、访问相册的使用权限，请添加对应的权限声明。

```xml
   <key>NSAppTransportSecurity</key>
   <dict>
   <key>NSAllowArbitraryLoads</key>
   <true/>
   </dict>
   <key>Privacy - Camera Usage Description</key>
   <string>扫码需要开启您的摄像头权限，用于识别</string>
   <key>Privacy - Photo Library Usage Description</key>
   <string>扫码需要您开启相册权限，浏览您的照片</string>
```

    

### SDK 接口说明

#### SDK 初始化：

用户初始化智能扫码 SDK，**SECRET_ID** 与 **SECRET_KEY** 传入云服务后台申请的密钥信息（申请地址：[智能扫码申请](https://console.cloud.tencent.com/ocr/is)），同时需要导入 **QBarCodeKit.h** 和 模型文件(**detect_model.bin**、**detect_model.param**、**srnet.bin**、**srnet.param**)。

```objective-c
#import "QBarCodeKit.h"
   
static NSString* const SECRET_ID     = @""; // SECRET_ID 信息
static NSString* const SECRET_KEY    = @""; // SECRET_KEY 信息
static const NSString *ERRCODE = @"errorcode"; // 结果错误码对应的 Key
static const NSString *ERRMSG = @"errormsg"; // 错误信息对应的 Key
static const NSString *CONTENT = @"content"; // 识别结果信息对应的 Key
   
@interface XJBHomeViewController ()<QBarCodeKitSDKDelegate>{
  QBarCodeKit *qBarCodeKit;
}
   
[sdk initQBarCodeKit:SECRET_ID secretKey:SECRET_KEY teamId:teamId resultHandle:^(NSDictionary * _Nonnull resultDic) {
  NSString *errCode = resultDic[ERRCODE]; // errorCode 为0 授权验证通过
  NSString *errMsg= resultDic[ERRMSG];	// 获取初始化失败信息
}];
```



#### 	摄像头数据实时识别：

智能扫码 SDK 提供摄像头实时数据扫码功能，满足您在自定义 UI 布局中的使用需求。	

```objective-c
/**
  摄像头视频流数据解码
  sampleBuffer 桢数据
*/
[qBarCodeKit qBarDecodingWithSampleBuffer:sampleBuffer resuldHandle:^(NSDictionary * _Nonnull resultDic) {
  NSString *msg = resultDic[CONTENT];
  NSLog(@"qBarDecodingWithSampleBuffer result: %@",msg);
}];
```

   

#### 	默认扫描界面识别：

如果您只关注扫码功能不需支持自定义 UI 界面，可以使用智能扫码 SDK 内自带的默认界面完成扫描操作。

```objective-c
[qBarCodeKit startDefaultQBarScan:self delegate:self];
```

结果回调处理示例：

```objective-c
- (void)onResultBack:(nonnull NSDictionary *)result { // 结果回调可能不在主线程
  NSString *errCode = result[@"errorcode"];
  if ([errCode isEqualToString:@"0"]) {
    NSArray *contentArr = result[@"content"]; // 识别结果信息
    NSString *msg = nil;
    if ([contentArr count] >0) {
      msg = [contentArr objectAtIndex:0];
      [[NSOperationQueue mainQueue] addOperationWithBlock:^{
        // UI 线程
        [self showAlertView:msg]; // 识别成功 json 数据
      }];
    } else {
      msg = @"NO DATA";
      [[NSOperationQueue mainQueue] addOperationWithBlock:^{
        // UI 线程
        [self showAlertView:msg];
      }];
    }
  } else {
    NSString *msg = result[@"errormsg"]; // 错误信息
    [[NSOperationQueue mainQueue] addOperationWithBlock:^{
      // UI 线程
      [self.showTextVoew setText:msg];
    }];
  }
}
```



#### 传入图片识别：

除了主动扫描以外，智能扫码 SDK 还支持图片识别功能，只需传入需要识别的图像：

```objective-c
/**
   image  需解码图片
*/
[qBarCodeKit decodeImageWithQBar:image resultHandler:^(NSDictionary * _Nonnull resultDic) {
   NSString *msg = resultDic[CONTENT];
   NSLog(@"decodeImageWithQBar result: %@",msg);
}];
```



### 数据声明

iOS 识别的数据结果也就是从 CONTENT 中获取的值为 Json 格式，先举例说明其内容格式：

```json
{
  "charset":"ISO8859-1",
  "data":"https://cloud.tencent.com/",
  "typeName":"QR_CODE"
}
```

其中 charset 表示内容信息的字符集，data 表示扫码得到的内容信息，typeName 表示扫码类型如条形码、二维码。

