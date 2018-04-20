## 腾讯云实时音视频教程


## 目录

* [产品介绍](#产品介绍)
* [开发前必看](#开发前必看)
    * [功能模块说明](#一-功能模块说明)
    * [基本概念](#二-基本概念) 
        * [实时音视频应用](#实时音视频应用)
        * [用户鉴权](#用户鉴权)
        * [房间](#房间)
        * [角色配置](#角色配置)
    * [主要步骤](#三-主要步骤)
* [客户端集成快速入口](#客户端集成快速入口)
    * [基本功能](#基本功能)
        * [集成](#第一步-集成sdk)
        * [获取userSig并登录](#第二步-获取userSig并登录)
        * [创建并加入房间](#第三步-创建并加入房间)
    * [进阶功能](#进阶功能)
        * [群组消息互动](#群组消息互动)
* [客户端高阶功能](advanced.md)
* [旁路直播、录制、混流、IM功能](server.md)
* [卡顿等问题定位](checkSpeed.md)


### 产品介绍
#### 能力

 * 100ms的超低延迟，1080P的高清分辨率，自适应网络切换
 * Android、ios、pc、mac、linux、H5、小程序、PSTN 全平台互通
 * IM、白板、直播、录制、点播、短视频无缝集成
 * 最高支持50路视频实时互动，多种混流方式自由选择

### 开发前必看

#### 一 功能模块说明

![视频云模块](https://main.qcloudimg.com/raw/aced8634db63acf5f9c77119730e857c.png)

 *  实时音视频负责在不同终端之间传递超低延迟的音视频流；
 *  实时音视频使用IM在不同客户端之间进行消息传递，以实现消息、图片、点赞、自定义信令等功能；
 * 实时音视频使用旁路直播，将音视频数据转码成RTMP，传递给直播系统。以此来实现标准直播流的观看、实时混流、截图鉴黄等功能；
 *  直播系统进行视频录制后，将文件存储于点播系统和cos存储中，为视频的二次处理和点播回看做好准备；


#### 二 基本概念

##### 实时音视频应用
客户首先需要[腾讯云官网](https://cloud.tencent.com/product/trtc)完成服务开通及应用创建。
![实时音视频](https://main.qcloudimg.com/raw/064ed162114ef632401ce20971470f39.png)
创建后，可以拿到应用的sdkAppid和accountType：

 - sdkAppId
 > sdkAppId就是腾讯云后台用来区分不同APP的一个标识，在后台开通服务并且创建应用后，会自动为你的应用生成一个SDKAppId。

 - accountType
 > accountType代表账号类型，在后台配置账号体系之后，也会自动分配一个accountType值


##### 用户鉴权
实时音视频中用户通过identifier来标识用户，使用userSig来对identifier进行鉴权。
- identifier是用户登录开发者系统的账号在腾讯云上的映射。开发者一般直接拿用户名当identifier。
> identifier 长度建议不超过 32 字节。请使用英文字符和下划线，不能全为数字，大小写不敏感。
- 为了确认identiifier不是假冒的，需要开发者后台调用[实时音视频服务器sdk](https://cloud.tencent.com/document/product/268/7656)，为identiifier计算一个userSig，颁发给客户端并填入sdk中。
其中的私钥可以在腾讯云控制台下载:
![私钥](https://main.qcloudimg.com/raw/4c51d3cea6320be6c7a93b99b1196a40.png)
推荐的userSig获取流程:
![计算sig](https://main.qcloudimg.com/raw/a5e79bee89cd0aa33d988313bd0ea286.png)


##### 房间

- 实时音视频使用房间这个虚拟的概念，用于用户之间的相互隔离。
> 房间号是开发者自行维护和分配的，是一个取值范围从1到10000000的数字。
>
> 只有在同一个房间里的用户可以相互看到音视频。
>
> 一个用户同时只能在一个房间内。如果要进入另一个房间，必须从前一个房间内退出，或者调用切换房间接口。

 - 房间回收
 > 房间创建后客户端无法解散，实时音视频后台会以房间内超过30秒没有上行音视频数据时，回收房间(客户端会收到onRoomDisconnect事件)。


##### 角色配置
- 角色配置
> 用户在打开摄像头/麦克风上行音视频流时，需要设置一些基本的配置，如分辨率，采集帧率等等，而这些配置的集合我们定义为角色。
我们在[腾讯云控制后台](https://console.cloud.tencent.com/ilvb)可以为不同的终端平台，根据需要添加一组参数配置，并为这组配置起一个角色名。
![角色配置](https://main.qcloudimg.com/raw/40960a366306f6aa4a1da5b072e2c043.png)

*角色配置修改后，客户端需要重新登录才能够让配置生效*
#### 三 主要步骤
客户端流程图
![数据交互](https://main.qcloudimg.com/raw/92a7e22a358b3219cd82a55495eb9e4b.png "客户端流程图")
整体结构图
![结构图](https://main.qcloudimg.com/raw/ef1fc9b39761532c7c7c6e7c260c6e34.png "客户端流程图")

### 客户端集成快速入口
#### 基本功能
##### 第一步 集成sdk

- [Android教程](android/c_import.md) 
- [iOS教程](ios/c_import.md) 
- [PC教程](windows/c_import.md) 

##### 第二步. 获取userSig并登陆
- 调试期间：

>  可以使用腾讯云控制台的开发辅助工具，手动生成userSig。

![](https://main.qcloudimg.com/raw/1d4cd453e7f4f238a0c1e7230bd45141.png)

- 正式运行时:

> 请参考[用户鉴权](#用户鉴权)

- [Android教程](android/c_login.md) 
- [iOS教程](ios/c_login.md) 
- [PC教程](windows/c_login.md) 

##### 第三步 创建并加入房间

- 分辨率等参数的配置
   
   方法一: 通过腾讯云控制台创建配置
> 我们可以参考[角色配置](#角色配置)配置角色，然后在终端代码中，使用通过角色名配置或切换到设定的参数配置上。   
   方法二: 客户端直接指定参数
   
>    即将推出

- 创建房间的注意事项

> 第一个创建房间的用户即这个房间的所有者，他可以调用sdk接口退出并解散这个房间。
> 
> 如果所有的用户都退出了房间，30s后服务器也会自动解散这个房间。
> 
> 当用户要加入的房间不存在的时候，实时音视频后台会先创建这个房间，然后再把用户加入。

- 创建房间

    - [Android教程](android/c_create.md) 
    - [iOS教程](ios/c_create.md) 
    - [PC教程](windows/c_create.md) 

- 加入房间
    - [Android教程](android/c_join.md) 
    - [iOS教程](ios/c_join.md) 
    - [PC教程](windows/c_join.md)

#### 进阶功能
##### 群组消息互动

实时音视频使用[腾讯云云通讯](https://cloud.tencent.com/document/product/269)来提供用户之间相互发消息的功能。
为了便于一个房间里的用户相互发消息，可以在用户创建或者加入房间的时候，调用sdk接口，创建或者加入一个和房间号一样的云通讯群组。

- [Android教程](android/c_msg.md) 
- [iOS教程](ios/c_msg.md) 
- [PC教程](windows/c_msg.md) 



