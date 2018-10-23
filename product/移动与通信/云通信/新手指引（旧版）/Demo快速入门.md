## 即时通信Demo简介

为了直观的体现ImSDK所支持的功能，并且起到接口使用的示范作用，即时通信提供了iOS和Android平台的Demo示例，用户可以下载Demo编译运行，体验ImSDK的功能，同时可以修改相应的参数，在此基础上进行开发自己的app。通过本文档可以快速找到登录参数进行修改，替换为开发者自己申请的sdkappid，以及快速熟悉Demo的使用方法。

即通通信Demo包含了一个类似手机QQ的IM功能，包括以下功能：

* 帐号（手机号码）注册，登录，设置帐号昵称
* C2C关系链维护：添加删除拉黑
* 群关系链维护：分公开群、讨论组和聊天室三种类型。可以创建，加群，退群
* 群资料维护：群名称、简介，公告修改
* 群成员管理：角色修改、禁言
* C2C沟通功能：收发文字，图片，表情，文件，语音，双人音视频
* 群沟通功能：收发文字，图片，表情，文件，语音

请单击[即时通信SDK下载体验](http://cloud.tencent.com/product/im.html#sdk)，包括ImSDK以及Demo的源码。
或者单击[Demo GitHub](https://github.com/zhaoyang21cn/iOS_Suixinliao)，参考Demo的源码。

## iOS Demo使用说明

### SDK的参数配置

开发者可以不用修改任何参数体验demo的功能。开发者申请接入腾讯音视频云通信后，如果选择的是托管模式集成自有帐号，可以在GlobalData.h中配置ios客户端SDK全局参数：kSdkAccountType（即accountType）、kSdkAppId（即SdkAppid）、kAppidAt3rd（同SdkAppid）,开发者可将下面的参数替换成自己申请的，此时demo就类似于开发者自己的app了，demo里的各种功能也是可以正常使用的。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084704_63682.png)

在AppDelegate.m中，配置TLS SDK参数，其中hostIp和hostPort分别设置为nil和0表示连接TLS

SDK的正式环境，localId设置语言为简体中文，countryId设置地区为中国大陆。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084717_54496.png)

在UserConfig.m中，配置音视频SDK参数，isTestServer和sdkAppIdToken使用默认配置。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084730_30000.png)

### Demo使用简介

1、单击“注册新用户”,用手机号码获取验证码注册

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084806_31629.jpg)

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084819_68248.jpg)

2、返回到登录界面登录

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084900_60955.jpg)

3、添加好友、群维护入口

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084923_33292.jpg)

4、建群或添加群

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911084942_83594.png)

5、单击好友或群进行消息收发操作

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085002_23609.jpg)

## Android Demo使用说明

### SDK的参数配置

开发者可以不用修改任何参数体验demo的功能。开发者申请接入腾讯音视频云通信后，如果选择的是托管模式集成自有帐号，可以在com.example.mydemo.utils.Constant中配置android客户端SDK全局参数：ACCOUNT_TYPE（即accountType）、SDK_APPID（即sdkAppid）,将这两个参数替换成自己申请的，此时demo就类似于开发者自己的app了，demo里的各种功能也是可以正常使用的。

![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085024_95357.png)

### Demo使用简介

1、单击“注册新用户”，用手机号码获取验证码注册
![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085044_90665.png)
![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085125_94859.png)
2、返回到登录界面登录
![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085224_87741.png)
3、添加好友、群维护入口
![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085242_91666.png)
4、建群或添加群
![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085303_43838.png)
5、单击好友或群进行消息收发操作
![](//avc.qcloud.com/wiki2.0/im/imgs/20150911085320_28112.png)
