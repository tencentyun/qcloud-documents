# 集成概述

互动直播集成QQ十多年音视频的研发经验，提供音视频直播 + 音视频多人互动 + IM文本互动的整体解决方案。

本章节主要讲述AVSDK和服务器端的整体集成流程，IM相关请前往[直播场景下的IM集成方案](/doc/product/269/%E7%9B%B4%E6%92%AD%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84IM%E9%9B%86%E6%88%90%E6%96%B9%E6%A1%88)

客户端集成可参见[集成文档](/doc/product/268/%E8%B0%83%E7%94%A8%E6%B5%81%E7%A8%8B%EF%BC%88Android%EF%BC%89)
或参考集成Demo“随心播”（[Android下载](http://android.myapp.com/myapp/detail.htm?apkName=com.tencent.qcloud.suixinbo)、[iOS下载](https://itunes.apple.com/cn/app/sui-xin-bo/id1037944078?mt=8))
Demo源码及源码导读可参见github（[Android源码](https://github.com/zhaoyang21cn/Android_Suixinbo)、 [iOS源码](https://github.com/zhaoyang21cn/iOS_Suixinbo)、 [服务端源码](https://github.com/zhaoyang21cn/SuiXinBoPHPServer) )

**！注意：一定要看随心播的源码导读**

## SDK构成
**互动直播SDK由两部分构成，IMSDK和AVSDK**

![IMSDK+AVSDK交互图](https://mccdn.qcloud.com/static/img/c1f2ab3b3d40eef889fe76dba49de7fa/im%2Bavsdk.png)

其中IMSDK为云通信SDK，为AVSDK提供账号登录、信令通道、IM弹幕消息、日志模块、日志上报等功能

AVSDK提供摄像头采集、编码、解码、美颜等一系列功能（下图为AVSDK整体框架）

![AVSDK构成](https://mccdn.qcloud.com/static/img/423aa6782eaaa503b0c29f7cec5aaca6/image.png)

## 登录交互逻辑
腾讯云互动直播提供两种账号对接方式

- 托管模式
  
	由腾讯提供账号的注册、密码存储及校验
- 独立模式

	由第三方业务自己保存账号体系，使用互动直播时，腾讯对第三方账号体系进行一定程度校验，是目前应用最广泛的一种验证方式。

**本文着重讲解独立模式使用方法**

详细内容参考[账号登录集成说明](https://cloud.tencent.com/doc/product/268/%E8%B4%A6%E5%8F%B7%E7%99%BB%E5%BD%95%E9%9B%86%E6%88%90%E8%AF%B4%E6%98%8E)

1.App登录业务服务器，做用户身份业务方鉴权

2.业务服务器验证成功后，根据用户身份，使用私钥加密用户身份信息后生成**UserSig**返回给客户端

3.将**UserSig**传给IMSDK的login接口，完成腾讯云服务器登录

![图示：派发UserSig流程](https://mccdn.qcloud.com/static/img/fe587958a511ca5211ecae36165833dc/image.png)

## 创建房间交互逻辑
互动直播采用房间的概念进行音视频流交换，即观看者与主播必须同一个房间内才能完成通信。但互动直播不进行**房间管理**操作，相关的房间号分配、房间成员列表、房间的观众主播进出都可由业务来管理（可借助IMSDK实现该功能，详情请见[房间状态通知](https://cloud.tencent.com/doc/product/268/%E6%88%BF%E9%97%B4%E7%8A%B6%E6%80%81%E9%80%9A%E7%9F%A5))

创建房间交互流程如下：

1.主播向业务服务器请求创建房间

2.业务服务器分配房间号

3.主播使用分配的房间号调用AVSDK创建房间接口完成创建

4.通知业务服务器创建房间完成

![图示：创建房间交互流程](//mccdn.qcloud.com/static/img/682b59a66ee6dfd391f1b5841320b799/image.png)

## 观众进入房间交互逻辑
在主播完成房间创建后，业务直播平台已经有当前正在直播的房间列表。观众在登陆后可以看到该房间列表点击后进入房间，可发IM消息或者业务逻辑通知给其他已经在看的观众和主播。详细流程图如下：

**注意：AVSDK不提供观众进入直播间通知，且不维护房间成员数及列表，可使用IMSDK实现或业务自行实现（见示意图虚线部分）**

![图示：观众进入房间交互](//mccdn.qcloud.com/static/img/cc9e2d826186c7e7af274d72827ca5ad/image.png)

## 观众主播IM消息交互逻辑
观众正在欣赏主播表演同时，可以和主播进行IM互动，进行聊天、送花和送礼物等其它操作

当观众需要进行送花、送礼物等计费相关操作时，有两种方案可供选择

- 观众送花，由互动直播云回调业务后台，进行扣费
- 观众送花，由App上行请求至直播平台，完成扣费操作后，直播平台通过[IMSDK REST API](/doc/product/269/%E5%9C%A8%E7%BE%A4%E7%BB%84%E4%B8%AD%E5%8F%91%E9%80%81%E6%99%AE%E9%80%9A%E6%B6%88%E6%81%AF)接口发送该消息

**当直播间内成员较多时，较大消息量可能会引起主播性能问题，业务侧需要优化渲染策略，同时互动直播云（IMSDK）可控制消息频率**

![图示：IM及其他消息互动](//mccdn.qcloud.com/static/img/85ec89b3af73dfad66491abdd75f3f8a/image.png)

## 观众退出房间交互逻辑
观众退出房间时，也需要通知给主播和其它的观众，相关流程可参考[观众进入房间交互逻辑]()

## 主播退出房间交互逻辑
当主播退出房间时，需做以下几件事情

- 通知业务直播平台，直播间销毁
- 通知其它的观众，主播已退出
- 显示直播结束页（展示直播时长、直播热度等）

流程图如下：

![图示：主播退出房间交互](//mccdn.qcloud.com/static/img/1756876dc4b82627d695511d6bd81c1d/image.png)


## 视频连麦
连麦功能是腾讯云互动直播SDK在直播场景下推出的特色功能，可供主播和某一（多）观众进行视频连线，相互交流，其它的观众可看到主播和被邀请的观众的音视频画面（映客、聚美优品等App均实现了该功能）

可下载随心播进行体验，并可参考随心播封装代码（[Android下载](http://android.myapp.com/myapp/detail.htm?apkName=com.tencent.qcloud.suixinbo)、[iOS下载](https://itunes.apple.com/cn/app/sui-xin-bo/id1037944078?mt=8))

上麦的实现流程如下：
![邀请上麦](//mccdn.qcloud.com/static/img/94595a0b1a426415c39b4e81e085c255/image.png)
**注意**
- 邀请A上麦需要发点多点的消息（可使用云通信IMSDK的单聊消息，用CustomElem实现
- 一定要在A完成上麦（开麦克风、摄像头，上传本地画面）完成后，再发送上麦广播通知
- 上麦广播通知可使用云通信的群消息（CustomElem）实现


下麦的实现流程如下：
![A下麦](//mccdn.qcloud.com/static/img/29b14a667d287144e6612262ac39ba4f/image.png)
**注意**
- 主播和观众A下麦都需要考虑（代码中要做好保护）
- 下麦的广播通知和下麦者关闭本地视频上传可同时进行（但建议先发出下麦通知，再关闭本地画面）

## 推流RTMP/HLS（H5或网页端观看）
互动直播SDK可直接由后台将私有协议转码为RTMP和HLS，业务可以将RTMP和HLS进行应用间分享，如分享到微信、QQ、朋友圈、QZone和其它应用内

**``建议使用``**
**推流的TIMAvManager.StreamParam参数可直接设置进行录制，不需要再调用录制API（推流结束录制也结束，生命周期一致）**

**注意**
- 互动直播推流使用了直播的cdn，需要业务申请直播权限（重要）
- 直播有频道数限制，请业务提前申请足够的频道数
- 因各种客户端异常导致没有正常销毁频道，开发者需从腾讯云控制台上手动关闭频道，否则频道会一直存在（占用总频道数）

文档参见[旁路直播开发](/doc/product/268/3226)

## 录制主播视频（回放）
互动直播提供了音视频录制API，可由互动直播后台将主播的音视频录制下来，并且存储到点播服务器上，待转码完成以后，就可以实现回放、分发等其他的功能

**注意**
- 需要开通点播服务
- 录制仅限于主播（第一个进入房间并且有音视频流的人）
- 录制会以60分钟为间隔生成MP4文件
- 转码需要时间
- 需要显式的调用停止录制API

更多文档参见：[录制功能开发](/doc/product/268/3218#6-.E6.B3.A8.E6.84.8F.E4.BA.8B.E9.A1.B9)

# 鉴黄
待补充

## 开发注意事项（必读）
* 观众人数过多时，消息量也会随之增多，**需注意主播端性能**，常见因渲染代码过多导致CPU飙升卡顿
* 主播可能因为某种原因（CRASH、断网等）掉线，业务直播平台需增加主播心跳，实现直播列表的实时更新
* 互动直播不提供房间成员管理等操作，需业务直播平台自行实现，或采用[IMSDK方案](/doc/product/269/%E7%9B%B4%E6%92%AD%E5%9C%BA%E6%99%AF%E4%B8%8B%E7%9A%84IM%E9%9B%86%E6%88%90%E6%96%B9%E6%A1%88)
