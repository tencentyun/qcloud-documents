## 开发准备

1. 注册腾讯云账号，提交智能扫码服务的申请，等待审核通过后，获得专属密钥。（申请地址：[智能扫码申请](https://console.cloud.tencent.com/ocr/is)）
2. 从 SDK 下载链接中下载智能扫码 SDK 到本地准备集成。

   

## iOS 端智能扫码 SDK 接入流程

### iOS 端智能扫码 SDK 介绍

SDK中包含了三个文件和一个文件夹，分别是 **libQBarCode.a**、**ncnn.framework**、**openmp.framework**、**QbarCodeRes.bundle** 和 **include** 包含的头文件。

- libQBarCode.a - 静态文件，是主要的扫码逻辑库。
- ncnn.framework与openmp.framework- 高性能神经网络前向计算框架。
- QbarCodeRes.bundle - 资源文件。
- include - 包含接入所需头文件。

### 环境依赖

- 当前 iOS 端智能扫码SDK版本适用于 IOS 9.0及以上的版本。
- Xcode 使用11.0及以上版本开发集成，建议使用最新版。

### 接入步骤

1. 将**ncnn.framework**、**openmp.framework**、**libQBarCode.a**、**QbarCodeRes.bundle**添加至项目中，并且 include 头文件也添加到项目中。
2. 引入系统库 framework。 
```
├── CoreMedio.framework
├── AVFoundation.framework
├── UIKit.framework
├── AVFoundation.framework
└── UIKit.framework
```
![img](https://qcloudimg.tencent-cloud.cn/raw/e15786fdf12bcacce846589e217cb805.jpeg)
3. 添加编译选项
	- 调用 SDK 页面设置为 <strong>Objective-C++ Source</strong>。
	![image](https://qcloudimg.tencent-cloud.cn/raw/ebca57a25d02b28552c9792345fffd5e.jpeg)
	- 将 **bitCode** 设置为 **NO**(不支持bitcode)。
	- 将 **Other Linker Flags** 添加 **-ObjC**。
4. 权限设置
智能扫码 SDK 需要手机网络、 摄像头、访问相册的使用权限，请添加对应的权限声明。
```xml
<key>Privacy - Camera Usage Description</key>
<string>扫码需要开启您的摄像头权限，用于识别</string>
<key>Privacy - Photo Library Usage Description</key>
<string>扫码需要您开启相册权限，浏览您的照片</string>
```


### SDK 接口说明

#### SDK 初始化：
用户初始化智能扫码 SDK，SECRET_ID 与 SECRET_KEY 传入云服务后台申请的密钥信息（申请地址：[智能扫码申请](https://console.cloud.tencent.com/ocr/is)），同时需要导入 QBarCodeKit.h、QBarSDKUIConfig.h 和 QbarCodeRes.bundle 资源文件

```c
#import "QBarCodeKit.h"
   
static NSString* const SECRET_ID     = @""; // SECRET_ID 信息
static NSString* const SECRET_KEY    = @""; // SECRET_KEY 信息
static const NSString *ERRCODE = @"errorcode"; // 结果错误码对应的Key
static const NSString *ERRMSG = @"errormsg"; // 错误信息对应的Key
static const NSString *CONTENT = @"content"; // 识别结果信息对应的Key

   
[sdk initQBarCodeKit:SECRET_ID secretKey:SECRET_KEY teamId:teamId resultHandle:^(NSDictionary * _Nonnull resultDic) {
  NSNumber *errCode = resultDic[ERRCODE]; // errorCode 为0 授权验证通过
  int code = [errCode intValue];
  NSString *errMsg= resultDic[ERRMSG];	// 获取初始化失败信息
}];
```



#### 摄像头数据实时识别：
智能扫码 SDK 提供摄像头实时数据扫码功能，满足您在自定义 UI 布局中的使用需求。	

```c
/**
  摄像头视频流数据解码
  sampleBuffer 桢数据
*/
[qBarCodeKit qBarDecodingWithSampleBuffer:sampleBuffer resuldHandle:^(NSDictionary * _Nonnull resultDic) {
  NSString *msg = resultDic[CONTENT];
  NSLog(@"qBarDecodingWithSampleBuffer result: %@",msg);
}];
```

   

#### 默认扫描界面识别：（推荐）

如果您只关注扫码功能不需支持自定义 UI 界面，可以使用智能扫码 SDK 内自带的默认界面完成扫描操作。

```c
[sdk startDefaultQBarScan:self withResult:^(NSDictionary * _Nonnull resultDic) {
       NSString *msg = [self convertToJsonData:resultDic];
 }];
```

#### 传入图片识别：

除了主动扫描以外，智能扫码 SDK 还支持图片识别功能，只需传入需要识别的图像：

```c
/**
   image  需解码图片 图片大小建议小于1M
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

