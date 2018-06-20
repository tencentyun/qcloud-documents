## 开发准备

### SDK 获取

实时流式语音识别的 iOS SDK 的下载地址：[iOS SDK](https://main.qcloudimg.com/raw/08dc7d8975ede33ecba181d38b1075ae/QCloudAAIClientSDK.zip)

更多示例可参考 Demo：[iOS Demo](https://main.qcloudimg.com/raw/522db7adc9be319ea591d15e5cbec49c/iOSDemo.zip)

### 开发准备

-  只支持 iOS 8.0 及以上版本，不支持 bitcode 版本；
-  实时流式语音识别，需要手机能够连接网络（GPRS、3G 或 Wi-Fi 网络等）；
-  从控制台获取 APP ID、SecretID、SecretKey，详情参考 [基本概念](https://cloud.tencent.com/document/product/441/6194)。


### SDK 配置

#### SDK 导入

iOS SDK 压缩包名称为： QCloudAAIClientSDK.zip。压缩包中包含了一个` .a` 静态库和一个头文件文件夹 include。

#### 工程配置

在 Build Settings 中设置 Other Linker Flags，加入参数 `-ObjC`。

![参数配置](https://mccdn.qcloud.com/static/img/58327ba5d83809c77da158ff95627ef7/image.png)

在工程` info.plist` 文件中设置：

1. App Transport Security Settings 类型，然后在 App Transport Security Settings 下添加 Allow Arbitrary Loads 类型 Boolean，值设为 `YES`；

2. 在程序中初始化 QCloudAAIClient 的实例对象 myClient ，` [myClient openHTTPSrequset:YES]`；（程序可以支持 https）

3. 在工程 `info.plist `文件中添加 Privacy - Microphone Usage Description，获取系统的麦克风的权限；
在工程中添加依赖库，在 build Phases  Link Binary Whith Libraries 中添加以下库：
	- libstdc++.6.0.9.tbd
	- libc++.tbd

## 签名获取

移动端 SDK 中用到的签名，建议由业务服务器来生成，并由移动端向业务服务器请求。业务侧服务器需要进行签名的生成，具体生成和使用请参照 [签名鉴权](https://cloud.tencent.com/document/product/441/6203) 。识别 SDK 签名必须实现 QCloudAAIClient 的 QCloudAAIGetSignDelegate 的协议，对由 SDK 提供(NSString*)param，进行加密处理；

```objective-c
// 获取请求的签名
- (NSString *)getRequestSign:(NSString*)param;
```


## 初始化

引入上传 SDK 的头文件 *QCloudAAIClient .h*，使用目录操作时，需要先实例化 QCloudAAIClient  对象。

#### 方法原型

```objective-c
-(id)initWithAppid:(NSString *)appid secretid:(NSString *)sid  projectId:(NSString *)pid ;
```

#### 参数说明

| 参数名称          | 类型           | 是否必填 | 说明                                       |
| ------------- | ------------ | ---- | ---------------------------------------- |
| appId         | NSString *   | 是    | 项目 ID，即 APPID  |
| sid         | NSString *   | 是    | 项目的 SecretID |
| pid         | NSString *   | 是    | 项目的 ProjectID  |


### STEP1：初始化 QCloudAAIClient

#### 示例

```objective-c
QCloudAAIClient *client= [[QCloudAAIClient alloc] initWithAppid:appid secretid:sid projectId:projectId]];
```
### STEP2：开始语音识别

```
-(BOOL)startDetectionWihtCompletionHandle:(QCloudAAICompletionHandler)handler stateChange:(QCloudAAIChangeHandler)stateChange；
```

#### 示例

```objective-c

 client = [[QCloudAAIClient alloc] initWithAppid:appid secretid:sid projectId:projectId];
  client.delegate = self;
 [client startDetectionWihtCompletionHandle:^(QCloudAAIRsp *rsp) {
        if (rsp.retCode == 0) {
            UITextView *strong = temp;
            if (![t isEqualToString:rsp.voiceId]) {
                t = rsp.voiceId;
                previous = strong.text;
            }
            strong.text= [NSString stringWithFormat:@"%@%@",previous,rsp.text];
        }else{
            NSLog(@"语音识别失败code= %dmsg:%@",rsp.retCode,rsp.descMsg);
        }
       
    }
    stateChange:^(QCloudAAIState state) {
        UITextView *strong = dTemp;
        if (state == QCloudAAIStateOpen) {
            strong.text = [NSString stringWithFormat:@"状态：%@",@"识别中"] ;
        }else if(state == QCloudAAIStateClose){
             strong.text = [NSString stringWithFormat:@"状态：%@",@"识别停止"] ;
        }else if(state == QCloudAAIStateFail){
            strong.text = @"麦克风权限未开，识别失败";
        }
    }];

```
### STEP3：停止语音识别

```objective-c
 [client stop];

```
