## 唇语人脸核身SaaS服务 IOS-SDK 安装说明

腾讯云万象优图人脸核身服务指通过人脸智能识别技术与OCR技术相结合，在线验证用户自拍视频或照片与身份证照片的匹配关系，秒级确认用户的身份是否真实有效。基于唇语活体检测的人脸核身SaaS产品提供集成了UI的一站式服务，开发者可以轻松集成SDK即可使用人脸核身服务。腾讯云提供IOS与Android的SDK，本文将介绍IOS的SDK的集成方式。

人脸核身SAAS服务通过Framework的方式向您提供服务。在使用本服务之前您需要集成必要的几个framework。

1. QCloudCore
2. QCloudUICore
3. QCloudAIOCR
4. QCloudFaceIn
5. <span style="color:blue">QCloudFaceInUI 该framework为人脸核身SAAS服务的提供者</span>
6. QCloudCamera

这几个服务我们通过一个完整的zip包向您提供，解压后将对应的framework引入到您的工程当中即可：

![](http://ww4.sinaimg.cn/large/006tNbRwgy1fflx22i5jjj31kw0notic.jpg)

您还必须将我们的资源文件（QCloudBundle.bundle）引入到工程之中：

![](http://ww2.sinaimg.cn/large/006tNbRwgy1fflx4jt3kmj31kw0t9tko.jpg)

同时您需要确保我们依赖的系统框架也被正确的引入：

1. MediaPlayer
2. AVFoundation
3. Foundation
4. UIKit
5. Accelerate
6. CoreMedia
7. CoreGraphics
8. SystemConfiguration
9. libz

上述步骤做完，可以运行了。

## FAQ

### 为什么界面上没有任何图片？

请确认您是否正确的引入了QCloudBundle.bundle资源，如果您没有引入该资源。则在界面获取资源的时候会出现问题，现象就是无法展示对应的界面图片。



# 唇语人脸核身SaaS服务 IOS-SDK 使用说明

## 服务配置信息注册并获得服务对象

> 关键类`QCloudFaceInUIService`、`QCloudFaceInUIServiceConfiguration`

QCloudFaceInUIServiceConfiguration是人脸核身UI版本的服务配置信息类，其控制着人脸核身服务关键的配置与接口回调。通过创建QCloudFaceInUIServiceConfiguration的示例，并将关键信息复制给对应的字段可以控制人脸核身UI版的一些行为。而在使用人脸核身服务之前，您必须创建一个配置信息。

```
    QCloudFaceInUIServiceConfiguration* config =[QCloudFaceInUIServiceConfiguration new];
    config.appID = self.appid;
    config.signatureProvider = self;
    config.bucket = self.bucket;
    config.delegate = self;
    config.serviceType = QCloudFaceInServiceTypeLip;
    _faceInUIService = [[QCloudFaceInUIService alloc] initWithConfiguration:config];
```

一个人脸核身服务是一次过程。反映到代码上就是一个QCloudFaceInUIService的实例，请在程序的某个地方强持有该示例。

```
@interface FaceIndemo : UIViewController
{
    QCloudFaceInUIService* _faceInUIService
}
@end
```

如果您没有强持有该实例，则人脸核身过程将会直接失败。

其中以下配置信息您必须特殊添加：

1. appID
2. signatureProvider
3. bucket
4. serviceType
5. delegate

### 配置信息中关键的部分及定义

```
/**
 人脸核身UI服务的配置信息。改类继承自QCloudServiceConfiguration，除了腾讯云服务需要常用配置之外。还需要配置人脸核身需要一些特殊信息：
 * bucket
 * serviceType
 * delegate
 * faceSimilarThreshold
 
 */
@interface QCloudFaceInUIServiceConfiguration : QCloudServiceConfiguration
​
@property (nonatomic, assign) QCloudRegionType regionType NS_UNAVAILABLE;
​
/**
 调用PAAS服务进行存储的容器地址。
 */
@property (nonatomic, strong) NSString* bucket;
​
/**
 本次服务需要的服务类型，目前支持：
 
 * QCloudFaceInUIVideo: 身份证识别+视频人脸核身服务
 * QCloudFaceInUIPhoto: 身份证识别+照片人脸核身服务
 
 */
@property (nonatomic,assign) QCloudFaceInServiceType serviceType;
​
​
/**
 人脸核身服务的委托者。通过实现`QCloudFaceInUIServiceDelegate`协议，委托者可以得到人脸核身UI服务的结果回调。
 */
​
@property (nonatomic, weak) id<QCloudFaceInUIServiceDelegate> delegate;
/**
 人脸核身服务中，判定身份证中照片与用户拍照的头像为本人的相似度阈值。默认值为70。
 */
@property (nonatomic, assign) CGFloat faceSimilarThreshold;
@end
```

```
/**
 QCloud中服务类的配置信息
 */
@interface QCloudServiceConfiguration : NSObject <NSCopying>
​
/**
 签名信息的回调接口，该委托必须实现。签名是腾讯云进行服务时进行用户身份校验的关键手段，同时也保障了用户访问的安全性。该委托中通过函数回调来提供签名信息。
 */
@property (nonatomic, strong) id<QCloudSignatureProvider> signatureProvider;
​
/**
 您的AppID
 */
@property (nonatomic, strong) NSString* appID;
​
/**
 您的服务所在的区域，某些服务可以不用关心该字段。默认值为QCloudRegionBeijing
 */
@property (nonatomic, assign) QCloudRegionType regionType;
@end
```

## 调用服务

在需要调用服务的地方调用start方法，则开始服务

> 需要注意的是，在开始服务的时候，您必须有一个UINavigationController已经展示出来。否则，将会没有任何FaceIn相关的界面。

```
[_faceInUIService start];
```

## 关心结果回调

您在QCloudFaceInUIServiceConfiguration配置了delegate，该delegate实现了协议`QCloudFaceInUIServiceDelegate`。该协议中目前只有成功的方法，当用户人脸核身成功之后，会通过delegate回调，通知您用户人脸核身成功。

> 此处没有人脸核身失败的通知，因为设计到UI操作。用户可以随时退出流程甚至APP，因而错误不是一个出错后必然会掉的结果。因为在第一个版本中，不提供失败通知。

```
/**
 人脸核身服务结果回调协议，关心人脸核身UI服务结果的类，可以通过实现该协议来得到结果。一般情况下，用户会从某个宿主的界面开始进入到人脸核身服务。由于用户的交互过程是个极度复杂的事情，所以目前阶段不提供错误结果通知。只提供成功的通知。
 */
@protocol QCloudFaceInUIServiceDelegate <NSObject>

/**
 人脸核身服务成功时通知函数。通过该函数通知调用方，人脸核身UI服务成功，用户成功通过验证。

 @param service 抛出改结果的人脸核身UI服务实例
 @param idCard 用户OCR识别出来的身份证信息。
 */
- (void) faceInUIService:(QCloudFaceInUIService*)service didFinish:(QCloudOCRIDCardInfo*)idCard;
@end
```