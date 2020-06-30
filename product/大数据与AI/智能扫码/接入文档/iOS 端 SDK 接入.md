## 开发准备

请参考 [接入准备](https://cloud.tencent.com/document/product/1214/45793) 。


## iOS 端扫码 SDK 介绍

SDK 中包含了三个文件和一个文件夹，分别是 **libQBarCode.a**、**ncnn.framework**、**QbarCodeRes.bundle** 和 **include** 包含的头文件。

- libQBarCode.a - 静态文件，是主要的扫码逻辑库
- ncnn.framework - 高性能神经网络前向计算框架
- QbarCodeRes.bundle - 资源文件
- include - 包含接入所需头文件

## 环境依赖

当前版本 SDK 适用于 iOS 9.0及以上的版本

## 接入步骤

1. 将 **ncnn.framework**、**libQBarCode.a**、**QbarCodeRes.bundle** 添加至项目中，并且 include 头文件也添加到项目中。

2. 引入系统的 framework 

   CoreTelephony.framework

   Security.framework

   SystemConfiguration.framework

   Accelerate.framework

   CoreVideo.framework

   CoreMedio.framework

   Foundation.framework

   UIKit.framework

   AVFoundation.framework

   QuartzCore.framework

   Accelerate.framework
   
   CoreGraphics.framework

   ![img](https://main.qcloudimg.com/raw/fa45a18ac4b6287c4aa0053996c948ed.png)            

3. 添加编译选项


- 将 **Compile Sources As** 设置为 **Objective-C++**
![img](https://main.qcloudimg.com/raw/6af43e9c335be5373d7ba0ccdd9e2f10.png)

- 将 **C++ standardLibrary** 设置为 **libc++(LVVM C++ standard library with c++ 11 support)**            
![img](https://main.qcloudimg.com/raw/ce0e9bd18173e14354633c4dc78c16a1.png)

- 将 **bitCode** 设置为 **NO**(不支持 bitcode)
- 将 **Other Linker Flags** 设置为 **\-lz**


4. 权限设置

   需要手机网络权限、 摄像头权限、访问相册权限。

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

-     **模式一：仅调用接口返回数据，需要自定义 view 和接口解码**

    需导入头文件 **QBarCode.h** 和模型文件(**detect_model.bin**、**detect_model.param**、**srnet.bin**、**srnet.param**)

    - SDK 初始化

    ```objective-c
    #import "QBarCode.h"
    static NSString* const SECRET_ID     = @"";
    static NSString* const SECRET_KEY    = @"";
    static const NSString *ERRCODE = @"errorcode";
    static const NSString *ERRMSG = @"errormsg";
    @interface XJBViewController () {
    QBarCode *qbarCode;
    }
    ```

    ```objective-c
    qbarCode = [QBarCode sharedInstance];
    [qbarCode startAuthSecretId:SECRET_ID secretKey:SECRET_KEY resultHandler:^(NSDictionary * _Nonnull resultDic) {
        NSString *msg = resultDic[ERRMSG];
        NSLog(@"startAuthSecretId %@",msg);//授权结果
    }];
    ```

    - 视频流数据解码：

    ```objective-c
    /**
    视频流数据解码
    sampleBuffer 桢数据
    */
    [qbarCode qBarDecodingWithSampleBuffer:sampleBuffer resuldHandle:^(NSDictionary * _Nonnull resultDic) {
            NSString *msg = resultDic[ERRMSG];
            NSLog(@"startAuthSecretId %@",msg);
    }];
    ```

    - 图片解码：

    ```objective-c
    /**
    image  需解码图片
    */
    [qbarCode qBarDecodingWithImage:image resultHandler:^(NSDictionary * _Nonnull resultDic) {
            NSString *msg = resultDic[ERRMSG];
            NSLog(@"qBarDecodingWithImage %@",msg);
    }];
    ```

    
 **模式二：已封装好扫码页面，无需用户自定义**

 - SDK 初始化

    ```objective-c
    //当扫码 SDK 正确导入项目时
    #import "QBarCodeKit.h"
    @interface XJBHomeViewController ()<QBarCodeKitSDKDelegate>{ //设置代理 QBarCodeKitSDKDelegate
        QBarCodeKit *sdk;
    }
    ```

    ```objective-c
    //初始化
    sdk = [QBarCodeKit sharedInstance];
    //网络服务正常时执行下面
    if ([self isNetOK]) {
        [sdk startQBarCodeProcessWithSecretId:SECRET_ID secretKey:SECRET_KEY delegate:self resultHandle:^(NSDictionary * _Nonnull resultDic) {
                NSString *errCode = resultDic[@"errorcode"];//errorCode 为 0 授权验证通过
                NSString *errMsg= resultDic[@"errormsg"];
                [[NSOperationQueue mainQueue] addOperationWithBlock:^{
                    [self.showTextVoew setText:errMsg];
                }];
            }];
    }
    ```

    - 进入扫码 SDK 页面：

    ```objective-c
    [sdk startQBarScanWithParentViewController:self];// [vc.navigationController pushViewController:scanViewController animated:YES];
    ```

    - 结果回调：

```objective-c
    - (void)onResultBack:(nonnull NSDictionary *)result { //结果回调可能不在主线程
        NSString *errCode = result[@"errorcode"];
        if ([errCode isEqualToString:@"0"]) {
            NSArray *contentArr = result[@"errormsg"];
            NSString *msg = nil;
            if ([contentArr count] >0) {
            msg = [contentArr objectAtIndex:0];
            [[NSOperationQueue mainQueue] addOperationWithBlock:^{
                // UI线程
                [self showAlertView:msg];//识别成功 json 数据
            }];
            } else {
            msg = @"NO DATA";
            [[NSOperationQueue mainQueue] addOperationWithBlock:^{
                // UI 线程
                [self showAlertView:msg];
            }];
            }
        } else {
            NSString *msg = result[@"errormsg"]; //错误信息
            [[NSOperationQueue mainQueue] addOperationWithBlock:^{
                // UI 线程
                [self.showTextVoew setText:msg];
            }];
        }
    }

```

