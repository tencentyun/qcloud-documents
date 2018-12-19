## 1 环境准备

这里以Xcode为例，开发者需安装了Xcode开发环境。

## 2 SDK集成

iOS SDK下载地址为：[iOS SDK](http://cloud.tencent.com/wiki/%E4%B8%87%E8%B1%A1%E4%BC%98%E5%9B%BESDK%E4%B8%8B%E8%BD%BD#2._iOS_SDK)。

万象优图iOS SDK其中包括上传SDK和下载SDK，上传SDK压缩包QCloudUploadSDK.zip,下载SDK压缩包QCloudDownloadSDK.zip.上传和下载SDK压缩包中分别包含了一个.a静态库和一个包含头文件的文件夹Headers，解压后的内容如下：

上传SDK:
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-1.jpg)

下载SDK:
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-2.jpg)

将解压后的QCloudUPloadSDK和QCloudDownloadSDK拖入工程目录，Xcode会自将其加入链接库列表中。

注：如果只需要上传或下载功能，则只拖入对应的SDK即可。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-3.jpg)

在build Settings中设置Other Linker Flags，加入参数-ObjC

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-4.jpg)

在build Phases -> Link Binary With Libraries中加入以下几个依赖库

1)	SystemConfiguration.framework
2)	CoreTelephony.framework
3)	MobileCoreServices.framework
4)	libxml2.dylib
5)	libz.dylib
6)	libstdc++.6.dylib

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-5.jpg)

注：如果只需要上传或下载功能，则只需要引入对应的动态库：

上传SDK依赖的系统动态库有：

1)	SystemConfiguration.framework
2)	CoreTelephony.framework
3)	libstdc++.6.dylib
4)	libz.dylib

下载SDK依赖的系统动态库有：

1)	SystemConfiguration.framework
2)	CoreTelephony.framework
3)	MobileCoreServices.framework
4)	libxml2.dylib
5)	libz.dylib

## 3 测试

以下所有代码都来源于体验Demo，这里讲述iOS客户端SDK的基本使用方法。Demo的下载地址为：[iOS Demo](/doc/product/275/SDK下载)。

>注意：如果开发者想根据demo做简单测试，请将demo中的项目信息修改为自己的项目信息。具体修改方法如下：
(1) 打开文件QCloudAuthenticationMgr.m文件；
(2) 修改init 函数中的appid （项目id） 和bucket（空间名称）字符串为自己的项目信息；
(3) 确保开发者自己的测试鉴权服务器中的项目信息和(2)中的项目信息一致。

### 3.1 APP注册

在使用其他接口之前必须先调用此方法进行用户信息初始化，即APP注册。

```
 [[QCloudAuthenticationMgr shareInstance] registerAuthentication];
```
 
下面给出函数的一种实现方法，分为两步：


1 从开发者业务服务器获取签名，开发者服务器鉴权服务部署参考[鉴权服务部署示例](/doc/product/275/如何接入#2.2-.E4.B8.80.E8.88.AC.E6.8E.A5.E5.85.A5)

2 上传和下载注册(上传和下载需分别注册)

开发者需要根据业务情况修改相应的代码。

```
- - (void)registerAuthentication
{
    NSString *requestSign = nil;
    //此URL是我们demo的服务器的地址这个地方需要替换成使用者的服务器地址
    requestSign = [self signatureWithURL:@"http://203.195.194.28/php/getsign.php"];
    //请求失败，使用备份签名注册
    self.signature = requestSign;
    
    //上传需要注册appId，应用级sign，userId根据用户需要选填
    [TXYUploadManager authorize:self.appId userId:self.userId sign:self.signature];
    //下载需要注册appId，sign信息由用户填入url参数中
    [TXYDownloader authorize:self.appId userId:self.userId];
}


#pragma mark -- 向业务后台拉取签名
- (NSString *)signatureWithURL:(NSString *)urlString
{
    NSURL *url = [NSURL URLWithString:urlString];
    
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    
    NSHTTPURLResponse *httpResponse = nil;
    NSError *connectionError = nil;
    NSData *signData = [NSURLConnection sendSynchronousRequest:request returningResponse:&httpResponse error:&connectionError];
    
    NSString *signature = nil;
    NSDictionary *responseDic = [NSJSONSerialization JSONObjectWithData:signData options:kNilOptions error:nil];
    signature = [responseDic objectForKey:@"sign"] ;
    
    return signature;
}
```

### 3.2 上传图片

上传图片分为一下两步：

1 初始化上传任务

```
    //1.构造TXYPhotoUploadTask上传任务,
    self.uploadPhotoTask = [[TXYPhotoUploadTask alloc] initWithPath:self.uploadPhotoPath
                                                        expiredDate:0
                                                         msgContext:@"上传成功后，传给用户业务后台的信息"
                                                             bucket:QCLOUD_UPLOAD_PHOTO_BUCKET   //默认上传到"test1"这个bucket
                                                             fileId:nil];                        //自定义fileId

2 用uploadmanager 来执行上传
 //2.调用TXYUploadManager的upload接口
 DECLARE_WEAK_SELF;
 [self.uploadManager upload:self.uploadPhotoTask
                       sign:nil
                   complete:^(TXYTaskRsp *resp, NSDictionary *context) {
                       DECLARE_STRONG_SELF;
                       if (!strongSelf) return;

                       strongSelf.uploadPhotoTask = nil;
                       //retCode大于等于0，表示上传成功
                       if (resp.retCode >= 0) {   
                           //得到图片上传成功后的回包信息
                           TXYPhotoUploadTaskRsp *photoResp = (TXYPhotoUploadTaskRsp *)resp;
                           strongSelf.urlDisplayLabel.text = photoResp.photoURL;
                           strongSelf.uploadStateLabel.text = @"上传成功!";
                           NSLog(@"上传成功!，code:%d desc:%@", resp.retCode, resp.descMsg);
                       }
                       else
                       {
                           strongSelf.uploadStateLabel.text = [NSString stringWithFormat:@"上传失败，code:%d desc:%@", resp.retCode, resp.descMsg];
                           NSLog(@"上传图片失败，code:%d desc:%@", resp.retCode, resp.descMsg);
                       }
                          
                  } progress:^(int64_t totalSize, int64_t sendSize, NSDictionary *context) {
                        DECLARE_STRONG_SELF;
                        if (!strongSelf) return;
                          
                        long progress = (long)(sendSize * 100.0f/totalSize);
                        strongSelf.uploadStateLabel.text = [NSString stringWithFormat:@"上传进度: %ld%%",progress];
                          
                        NSLog(@"上传进度,sendSize %lld,totolSize %lld, progress %ld",sendSize,totalSize,progress);
                }stateChange:^(TXYUploadTaskState state, NSDictionary *context) {
                    DECLARE_STRONG_SELF;
                    if (!strongSelf) return;
                    if(state == TTXYUploadTaskStatePause) {
                        [self.pauseButton setTitle:@"恢复" forState:UIControlStateNormal];
                    }
                    else
                    {
                        [self.pauseButton setTitle:@"暂停" forState:UIControlStateNormal];
                    }
                          
                    NSLog(@"Upload photo task state change %zd",state);
               }];
```

### 3.3 下载图片

下载和其他功能可参考体验demo。