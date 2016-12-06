## 一 下载Demo
点击下载[iOS Demo](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos)的代码。代码里包含两个示例：<br/>

1. tdemolive目录下是一个最简单的互动直播示例，演示了最关键的几个接口的调用。使用方法可以参考github上的说明。
2. suixinbo目录下是新版随心播代码。演示了包括界面和后台交互的完整的直播流程。


## 二 下载并导入Frameworks
* [下载ILiveSDK，TILLiveSDK，AVSDK，IMSDK](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos)，并解压到工程目录suixinbo/Frameworks 下,工程最后的目录如下图：
Frameworks目录

  ![Frameworks目录](http://mc.qcloudimg.com/static/img/139b6e97a13c9274c7371a6af6a0a530/image.png)
  
  AVSDK目录
  
  ![AVSDK目录](http://mc.qcloudimg.com/static/img/73d52880bdd252174f75e964b7d9c8eb/image.png)
  
  IMSDK目录
  
  ![IMSDK目录](http://mc.qcloudimg.com/static/img/819ee738975ccf61b510a58a9469b4ea/image.png)

* 导入Frameworks,将下载好的SDK复制到工程目录下，工程目录右键，Add Files to " you projectname",在demo中如下图所示：

  ![SDK导入工程](http://mc.qcloudimg.com/static/img/7922154e7bdbbd0a6c24756d5b0a8866/image.png)

## 三 运行
编译运行工程。(如果xcode8编译不过，修改 Bundle Identifier, 随心播工程上的Bundle Identifier在用户真机上可能无法运行，用户重新修改下Bundle Identifier即可，比如在原有id后面加1)

* <div align=center>
<img src="https://mc.qcloudimg.com/static/img/1be6185cdb0f61756c85e230a9fc0514/2.png"/>
</div>
* ![](https://mc.qcloudimg.com/static/img/ccf7ca496a22ec0aed9d4446f30ba85f/1.png)

## 四 集成到开发者自己的代码工程里
### 1 引入SDK并导入项目 

参照以上 第二步 

### 2 修改工程配置
将下载好的SDK复制到工程目录下，工程目录右键，Add Files to " you projectname",在demo中如下图所示：

1. Build Settings/Linking/Other Linker Flags，增加 -ObjC 配置，如下图所示：
![](http://mc.qcloudimg.com/static/img/f473f6c580a4196af7d3d33edf140bdb/image.png)

2. Build Settings/Linking/Bitcode，增加 Bitcode 配置，设置为NO，如下图所示:
![](http://mc.qcloudimg.com/static/img/f473f6c580a4196af7d3d33edf140bdb/image.png)

3. iOS10及以上系统，需在Info.plist中增加设备访问权限配置
![](http://mc.qcloudimg.com/static/img/e7b7897cb79a5cb9a984938dd4b3fda3/image.png)
若上述步骤均无误，则工程编译可以通过了。

### 3 修改后台地址
目前随心播后台主要用来维护直播房间列表。如果复用随心播客户端代码，需要修改随心播后台地址为业务方自己部署的服务器地址。 <br />     

| 请求类| 说明 | 修改文件 | 修改方法 |
|---------|---------|---------|---------|
| LiveAVRoomIDRequest | 获取自己分配的房间号 |LiveAVRoomIDRequest.m|- (NSString *)url |
| LiveStartRequest | 创建新房间 |LiveStartRequest.m|- (NSString *)url |
| LiveEndRequest | 退出房间 |LiveEndRequest.m|- (NSString *)url |
| LiveListRequest | 获取房间列表 |LiveListRequest.m| - (NSString *)url |
| LiveHostHeartBeatRequest | 房间心跳 |LiveHostHeartBeatRequest.m|- (NSString *)url |
| LiveImageSignRequest | 图片上传相关 |LiveImageSignRequest.m|- (NSString *)url |

### 4 添加系统库
添加以下系统库比较方便的方法是直接从随心播工程中，将SystemLibrarys组拖到自己的工程目录下

|  需要增加的系统库 |
|------------|
|libc++.tbd|
|libstdc++.tbd|
|libstdc++.6.tbd|
|libz.tbd|
|libbz2.tbd|
|libiconv.tbd|
|libresolv.tbd|
|libsqlite3.tbd|
|libprotobuf.tbd|
|UIKit.framework|
|CoreVideo.framework|
|CoreMedia.framework|
|Accelerate.framework|
|Foundation.framework|
|AVFoundation.framework|
|VideoToolbox.framework|
|CoreGraphics.framework|
|CoreTelephony.framework|
|SystemConfiguration.framework|

## 五 库类介绍
-----
|Frameworks文件夹|说明|
|---|---|
|AVSDK|包括音视频相关的所有SDK|
|IMSDK|包括即时通讯相关的所有SDK|
|ILiveSDK|包括ILiveSDK和TILLiveSDK|

### 库类清单
|序号|名称|所在文件夹|说明|
|---|---|---|---|
|1|QAVSDK.framework|Frameworks/AVSDK/|音视频SDK|
|2|xplatform.framework|Frameworks/AVSDK/|音视频SDK所依赖的SDK|
|3|IMCore.framework|Frameworks/IMSDK/|即时通讯核心库|
|4|ImSDK.framework|Frameworks/IMSDK/|即时通讯SDK|
|5|IMSDKBugly.framework|Frameworks/IMSDK/|上报SDK|
|6|QALSDK.framework|Frameworks/IMSDK/|即时通讯网络模块SDK|
|7|TLSSDK.framework|Frameworks/IMSDK/|登录服务SDK|
|8|ILiveSDK.framework|Frameworks/ILiveSDK/|互动直播基础功能SDK|
|9|TILLiveSDK.framework|Frameworks/ILiveSDK/|直播SDK(针对直播场景封装的SDK，包括互动连麦等功能)|
