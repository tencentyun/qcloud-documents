## 1.工程结构
从 [官网](https://cloud.tencent.com/document/product/454/6991) 下载小直播代码，使用Android Studio打开工程后，您将看到如下的目录结构：
![](//mc.qcloudimg.com/static/img/5e39b905d134114aeb752f614313123d/image.png)

|文件/目录 | 说明 | 
|---------|---------|
| common | 通用组件，包括各种工具类、自定义界面(美颜、点赞、弹幕、播放器控件)|
| im | 互动消息模块|
| linkmic | 连麦模块|
| login | 帐号模块，包括登录以及注册|
| mainui | 小直播主界面，包括主 Activity 以及视频列表|
| play | 播放模块，包括直播和点播|
| push | 推流模块，包含摄像头推流和录屏推流|
| thirdparty | 第三方分享组件|
| userinfo | 个人资料模块|
| videoeditor | 短视频编辑模块|
| videojoiner | 短视频合成模块|
| videopublish | 短视频发布模块|
| videorecord | 短视频录制模块|
| jniLibs| 小直播依赖的腾讯相关sdk，主要是BuglySDK、TLSSDK、IMSDK及RTMPSDK|


## 2.库使用说明
#### [直播 SDK](https://cloud.tencent.com/document/product/454/7873)  (必选)
移动直播最主要的 SDK，其提供了推流、直播、点播、连麦、录屏等功能。
- jar 包
txrtmpsdk.jar
- so 库
    移动直播因使用连麦功能，所以选择集成完整版。目前完整版只支持 armeabi 和 armeabi-v7 两种架构。
		
|  库名 | 描述 |
|  --------- | ---------- |
| libtxrtmpsdk.so | 直播核心组件 |
| libtraeimp-rtmp-armeabi.so | 连麦功能库 |
| libstlport_shared.so  | 连麦功能库 |

#### IM SDK  (必选)
提供消息收发功能。
- jar 包

| 包名      |    描述  |
| :--------: | :--------:| 
| imsdk.jar           |   ImSDK基础包，只提供消息、资料关系链管理、群组管理等的最基础功能 | 
| qalsdk.jar |   SDK网络层jar包 |  
| soload.jar      |   提高imsdk so库的加载成功率 | 
| mobilepb.jar |   protobuffer处理相关jar包 |  
| tls_sdk.jar      |   帐号系统jar包 |   
| wup-1.0.0-SNAPSHOT.jar      |   无线统一协议jar包 | 

- so 库
移动直播目前只集成 armeabi 架构
	- lib_imcore_jni_gyp.so
	- libqalcodecwrapper.so
	- libqalmsfboot.so
  - libwtcrypto.so

#### [短视频](https://cloud.tencent.com/document/product/584/9369)（非必选）
UGC 小视频的录制和发布以及编辑功能。
- jar 包


| 包名      |    描述  |
| :--------: | :--------:| 
| ugcupload.jar | UGC 上传文件到点播系统 jar 包|
| sha1utils.jar | UGC 计算上传文件的 SHA 值 jar 包|
| okio-1.6.0.jar | 网络操作 I/O 库 |
| okhttp-3.2.0.jar | 网络请求库 |
| cos-sdk-android.1.4.3.6.jar |  对象存储 COS 相关的 jar 包|

- so 库


| 库名      |    描述  |
| :--------: | :--------:| 
| libTcHevcDec.so | 用于 H265 播放 |
| libTXSHA1.so | UGC 计算上传文件的 SHA 值 |


#### 商业增值版 (小直播源码中没有)
基于优图实验室的 AI 专利技术，实现了大眼、瘦脸、动效贴纸、绿幕等特效功能。如果没有用到该功能，可以删除相关 so 库。
- libblasV8.so   
- librsjni.so  
- libRSSupport.so  

#### volley  (非必选)
第三方的网络请求库

#### Gson  (非必选)
第三方的用来在Java 对象和JSON 数据之间进行映射的Java 类库

#### Glide  (非必选)
第三方的图片加载库

#### dfm  (非必选)
Bilibili 弹幕库。如果您希望在聊天中有弹幕效果，建议保留。


## 3.模块介绍
小直播按照功能不同划分了11个模块，分别为：帐号、互动消息、主界面、推流、播放、连麦、短视频（编辑、合成、录制、发布）、资料，代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

### 帐号模块
#### 模块简介
- 帐号模块负责处理用户登录/注册以及登录缓存的逻辑
- 登录注册功能使用[TLSSDK托管](https://cloud.tencent.com/doc/product/269/%E6%89%98%E7%AE%A1%E6%A8%A1%E5%BC%8F)登录实现
- 如果您已经有自己的帐号体系，可以直接替换该模块，并调用TCLoginMgr的guestLogin接口以游客身份使用IM通道，详情请参考[替换帐号](https://cloud.tencent.com/doc/api/258/6441)
- 在TLSSDK登录鉴权成功后，可以通过鉴权返回的UserId与UserSig调用ImSDK的login接口完成IM模块的登录
- 用户可以通过帐号密码/手机验证码两种方式进行注册与登录
- 帐号模块会缓存最后登录的用户基本信息（UserId与UserSig）在本地，通过接口调用可以获取最近登录的用户信息并判断是否需要重新登录
- 登录实现为互踢机制，登录时间在前的用户会接收到强制下线消息

#### 相关代码 
| 类名      |    描述  |
| :--------: | :--------:| 
| TCApplication.java | 初始化TIMManager时注册UserStatusListener监听获取用户签名失效/被踢下线消息 |
| TCLoginMgr.java | 登录管理类，提供用户登录/注册相关接口与获取最后登录用户缓存接口 |
| TCLoginActivity.java | 用户登录页面 |
| TCRegisterMgr.java | 注册管理类，提供普通帐号密码注册/手机号码注册接口 |
| TCRegisterActivity.java | 用户注册页面 |
| OnProcessFragment | 显示进度条的碎片 |

------------------------------------

### 互动消息
#### 模块简介
- 小直播的互动消息功能主要基于[ImSDK](https://cloud.tencent.com/doc/product/269/1561)的群聊功能实现，需要在IMSDK登录后才能调用
- 每个直播间都是一个直播大群，推流端在推流之前需要创建直播大群，结束推流时，解散该群；播放端在进入该直播间时，加入该群，退出直播间时，则退出该群
- 通过实现消息收发的监听类，可以在监听接口中获取相应的消息通知，目前实现的消息类型：文本消息、弹幕消息、点赞消息、用户加入/退出消息、群组解散消息
- 各种类型的消息都是以文本消息形式发送，采用统一的JSON格式，在JSON中携带消息类型、发送者id、昵称、头像、消息文本的信息，接收端收到消息后解析JSON格式，向上层回调各种类型的消息

#### 相关代码
| 类名      |    描述  |
| :--------: | :--------:| 
| TCChatRoomMgr.java | 消息收发管理类，负责初始化消息循环，消息解析与消息封装，同时向主播提供创建/解散消息群组的接口，向观众提供加入/退出消息的接口 |
| TCChatEntity.java | 消息实体类 |
| TCChatMsgListAdapter.java | 推流界面和直播界面中互动消息列表的设配器 |
| TCIMInitMgr.java | IMSDK 初始化操作类 |
| TCSimpleUserInfo.java | 用户基本信息实体类，主要封装了用户id、昵称、头像地址 |

------------------------------------

### 主界面&列表管理
#### 模块简介
- 主界面主要负责列表、推流和个人资料三个一级功能的切换
- 登录成功后，默认展示列表界面；点击推流按钮后，将弹出对话框让你选择直播推流或录制小视频；点击个人资料按钮，将跳转到个人资料页面
- 列表管理包含列表的拉取和展示。目前我们的列表拉取协议支持拉取直播列表，点播列表和混合列表（既有直播和点播）三种模式。小直播中以直播、回放、小视频三个列表项进行展示。

| 类名      |    描述  |
| :--------: | :--------:| 
| TCSplashActivity.java |  闪屏界面 |
| TCMainActivity.java |  主界面，用于呈现直播列表，开启直播页，用户信息页 |
| TCLiveListMgr.java |  列表管理类，提供接口获取本地内存列表及从服务器更新列表。 |
| TCLiveListFragment.java |  列表展示界面，负责呈现直播、点播、UGC 短视频的数据 |
| TCLiveListAdapter.java |  直播、点播视频列表适配层 |
| TCUGCVideoListAdapter.java |  UGC 短视频列表适配层 |
| TCLiveInfo.java |  直播视频数据 |


------------------------------------

### 推流模块
#### 模块简介
- 推流模块主要包括，主播视频数据采集，渲染，推流，主播和观众消息互动等功能。
- 主播端可以采集自己视频和声音数据推送到视频云服务器，观众可以在其他客户端观看，主播端可以自定义视频采集分辨率，美颜，美白，硬编码等功能。
- 主播端可以创建自己的房间，观众可以加入房间和主播互动，观众可以发送普通消息、弹幕消息以及点赞消息，主播端会在对应的消息列表，弹幕动画位置展示对应的消息，关于消息的详细介绍，请参考“消息”模块
- 主播端可以展示观众列表，当有观众进入，退出房间时候，观众列表会刷新，主播也会收到观众进入或则退出房间消息

#### 推流时序图
![](//mc.qcloudimg.com/static/img/6fb00666a6a1cdea732fbddccc5fc786/image.png)

#### UI层级结构
SDK渲染视频时，startCameraPreview的参数View（即videoParentView）是用来承载SDK渲染层的，SDK会在其之上构建一个用于OpenGL渲染的子view，如果您想要在渲染画面之上实现弹幕、献花之类的UI控件，应该如下图这般创建一个与之平级的view
![](//mc.qcloudimg.com/static/img/3da33f8c62b9339a365faddd2635faa2/image.png)

#### 相关代码 

| 类名      |    描述  |
| :--------: | :--------:| 
| TCPublishSettingActivity.java |  推流设置类，设置推流方法、画质、封面、直播间标题信息  |
| TCPusherMgr.java |  直播管理类，和后台进行通信，拉取直播地址、通知后台退出直播 |
| TCLocationHelper.java |  位置服务类，用于主播推流前设置定位 |
| DetailDialogFragment.java | 直播结束统计信息展示类，用于展示主播在直播过程中观看人数、点赞数以及直播时长|
| TCLivePublisherActivity.java |  推流模块Activity，所有的推流管理、消息管理、动画特效都在该类进行 |
| TCLocationHelper.java |  位置服务类，用于主播推流前设置定位 |
| TCMusicSelectView.java |  背景音乐选择类，选择本地音乐作为背景音乐 |
| MusicListView.java |  本地音乐显示类，以列表形式显示本地音乐 |
| TCAudioControl.java |  背景音乐控制类，提供播放、停止、暂停、调节音量等接口 |
| TCScreenRecordActivity.java | 录屏直播类 |
| TCScreenRecordService.java | 前台服务进程, 监听主播下线通知 |
| CameraPreview.java | 摄像头预览画面渲染类，结合 FloatingCameraView 一起使用 |
| FloatingCameraView.java | 摄像头悬浮窗，主要是在录屏推流场景下提供主播视角 |
| FloatingView.java | 桌面悬浮球类 |


------------------------------------

### 播放模块
#### 模块简介
- 播放模块主要包括：主播视频数据播放、观众和主播消息互动等功能。
- 观众端可以进入主播的房间，可以给主播发送普通消息、弹幕消息以及点赞消息，关于消息的详细介绍，请参考“消息”模块
- 观众端可以展示主播信息，观众列表，当有观众进入，退出房间时候，观众列表会刷新，同时消息列表也会展示其他观众进入，退出房间的消息。

#### 播放时序图
![](//mc.qcloudimg.com/static/img/fb9f9002c2d973d069bb9c1568037e26/image.png)

#### UI层级结构
请参考推流模块的UI层级结构

#### 相关代码

| 类名      |    描述  |
| :--------: | :--------:| 
| TCPlayerMgr.java |  播放管理类,和后台进行通信，通知后台进入房间、退出房间、点赞事件 |
| TCLivePlayerActivity.java | 播放模块Activity，包括点播和直播，所有的播放管理、消息管理、动画特效都在该类进行 |

------------------------------------
### 连麦模块
#### 模块简介

- 连麦功能提供了主播和观众视频互动聊天的功能，目前支持 1 主播和 3 个观众视频互动。
-  在集成连麦功能之前，建议先了解下 [连麦的原理](https://cloud.tencent.com/document/product/454/9855) ，再按照 [对接攻略](https://cloud.tencent.com/document/product/454/9858) 来集成。
- 连麦具体流程：观众通过 IM 向主播发起连麦申请，主播也是通过 IM 回复观众。如果主播同意观众的连麦申请，观众就荣升为小主播。主播和小主播各自先推流，然再互相拉取对方的低延时流。

#### 相关代码
| 类名      |    描述  |
| :--------: | :--------:| 
| TCLinkMicLivePushActivity.java |  连麦之主播推流界面，它以普通推流界面为基础，新增播放小主播低延时流的逻辑 |
| TCLinkMicLivePlayActivity.java |  连麦之播放界面，它基于普通播放界面，增加推流功能 |
| TCLinkMicMgr.java |  连麦管理类，负责处发送和接受连麦的 IM 消息  |
| TCStreamMergeMgr.java |  连麦之云端混流管理类，将云端混流所需的参数发送给小直播后台业务服务器 |
| TCLinkMicPlayItem.java |  连麦之小窗口播放类 |
| TCLivePushListenerImpl.java |  推流状态监听接口的实现类 |
| TCLivePlayListenerImpl.java |  播放状态监听接口的实现类 |

------------------------------------
### 短视频录制模块
#### 模块简介
- 小直播提供录制 一分钟的 [短视频](https://cloud.tencent.com/document/product/584/9453) 功能，但 SDK 本身不显示录制时长。


#### 相关代码
| 类名      |    描述  |
| :--------: | :--------:| 
| TCVideoRecordActivity.java| 短视频录制界面 |

------------------------------------

### 短视频发布模块
#### 模块简介
- 将录制的文件发布到腾讯云视频分发平台（点播系统）中。

#### 相关代码
| 类名      |    描述  |
| :--------: | :--------:| 
| TCVideoPublisherActivity.java| 短视频发布界面 |

------------------------------------
### 短视频编辑模块
#### 模块简介
- [视频编辑](https://cloud.tencent.com/document/product/584/9502) 包括视频裁剪加速、美颜滤镜、音乐混音及添加字幕等功能

#### 相关代码
| 类名      |    描述  |
| :--------: | :--------:| 
| EditPannel.java| 短视频时长裁剪显示框 |
| RangeSlider.java| 短视频时长裁剪左右拖动框 |
| TCHorizontalScrollView.java| 存放短视频每帧画面滚动列表 |
| TCVideoEditerActivity.java| 短视频编辑主界面 |
| TCVideoEditerAdapter.java| 存放短视频每帧画面列表的设配器 |
| TCVideoEditView.java| 短视频裁剪界面 |
| ThumbView.java| 短视频专辑显示界面，扫描本地所有 MP4 文件并显示 |

------------------------------------

### 资料
#### 模块简介
- 资料模块主要负责用户资料的展示，存储，和 修改，并负责将这些操作同步到服务器。
- 用户资料主要包括，用户头像，昵称，性别，直播封面，定位等。 资料模块是IMSDK提供的功能，IMSDK提供扩展自定义字段的功能，方便开发者自定义更加丰富的用户资料。
- 资料模块会从服务器同步用户最新资料到APP，用户可以通过资料模块来浏览自己的相关资料，包括用户头像，昵称和性别等。
- 用户可以通过资料模块修改自己的相关资料，资料模块会将这些操作同步到服务器。
- 其他模块也可以通过资料模块获取，修改用户资料。
	
#### 相关代码
| 类名      |    描述  |
| :--------: | :--------:| 
| TCUserInfoMgr.java | 用户资料管理类，负责资料的存储和修改，并负责将操作同步到服务器，或者向服务器查询用户资料。|
| TCUserInfoMgrListener.java | 用户资料管理类与服务器通信的结果回调，包括查询资料的结果，修改资料的结果等。|
| TCUserInfoFragment.java | 用户资料展示页面|
| TCEditUseInfoActivity.java | 用户资料修改页面 |
| TCLineEditTextView.java | 文本修改控件，对控件EditText的简单封装，可以用来修改文本，并显示相关信息|

------------------------------------

