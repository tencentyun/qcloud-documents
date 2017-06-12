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

