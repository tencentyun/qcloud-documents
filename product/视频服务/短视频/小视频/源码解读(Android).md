###  小视频代码说明

#### 1 工程结构

下载小视频代码，使用Android Studio打开工程后，您将看到如下的目录结构：

![](https://main.qcloudimg.com/raw/1405849b94d50358803de951eae9b6d3.png)

| 文件/目录    | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| common       | 通用组件，包括各种工具类、自定义界面(美颜、播放器控件)       |
| im           | 互动消息模块                                                 |
| login        | 帐号模块，包括登录以及注册                                   |
| mainui       | 小视频主界面，包括主 Activity 以及视频列表                   |
| play         | 点播播放模块                                                 |
| userinfo     | 个人资料模块                                                 |
| videoeditor  | 短视频编辑模块                                               |
| videojoiner  | 短视频合成模块                                               |
| videopublish | 短视频发布模块                                               |
| videorecord  | 短视频录制模块                                               |
| jniLibs      | 小视频依赖的腾讯相关sdk，主要是BuglySDK、TLSSDK、IMSDK及LiteAVSDK |

#### 商业增值版 (小直播源码中没有)

基于优图实验室的 AI 专利技术，实现了大眼、瘦脸、动效贴纸、绿幕等特效功能。如果没有用到该功能，可以删除相关 so 库。

- libblasV8.so 
- librsjni.so 
- libRSSupport.so

#### 2 模块介绍

小视频按照功能划分成帐号、主界面、播放、短视频（编辑、合成、录制、发布）、资料，代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

#### 帐号模块

##### 模块简介

- 帐号模块负责处理用户登录/注册以及登录缓存的逻辑
- 登录注册功能使用[TLSSDK托管](https://cloud.tencent.com/doc/product/269/%E6%89%98%E7%AE%A1%E6%A8%A1%E5%BC%8F)登录实现
- 如果您已经有自己的帐号体系，可以直接替换该模块，并调用TCLoginMgr的guestLogin接口以游客身份使用IM通道，详情请参考[替换帐号](https://cloud.tencent.com/doc/api/258/6441)
- 在TLSSDK登录鉴权成功后，可以通过鉴权返回的UserId与UserSig调用ImSDK的login接口完成IM模块的登录
- 用户可以通过帐号密码/手机验证码两种方式进行注册与登录
- 帐号模块会缓存最后登录的用户基本信息（UserId与UserSig）在本地，通过接口调用可以获取最近登录的用户信息并判断是否需要重新登录
- 登录实现为互踢机制，登录时间在前的用户会接收到强制下线消息

##### 相关代码

| 类名                    | 描述                                                         |
| ----------------------- | ------------------------------------------------------------ |
| TCApplication.java      | 初始化TIMManager时注册UserStatusListener监听获取用户签名失效/被踢下线消息 |
| TCLoginMgr.java         | 登录管理类，提供用户登录/注册相关接口与获取最后登录用户缓存接口 |
| TCLoginActivity.java    | 用户登录页面                                                 |
| TCRegisterMgr.java      | 注册管理类，提供普通帐号密码注册/手机号码注册接口            |
| TCRegisterActivity.java | 用户注册页面                                                 |
| OnProcessFragment       | 显示进度条的Fragment                                         |

#### 主界面&列表管理

##### 模块简介

- 主界面主要负责短视频列表、短视频拍摄/编辑和个人资料三个一级功能的切换
- 登录成功后，默认展示列表界面；点击+号按钮后，将弹出对话框让你选择录制小视频或编辑本地小视频；点击个人资料按钮，将跳转到个人资料页面
- 列表管理包含列表的拉取和展示。

##### 相关代码

| 类名                       | 描述                                                     |
| -------------------------- | -------------------------------------------------------- |
| TCSplashActivity.java      | 闪屏界面                                                 |
| TCMainActivity.java        | 主界面，用于呈现短视频列表，短视频拍摄/编辑，用户信息页  |
| TCLiveListMgr.java         | 列表管理类，提供接口获取本地内存列表及从服务器更新列表。 |
| TCLiveListFragment.java    | 列表展示界面，负责呈现短视频的数据                       |
| TCLiveListAdapter.java     | 短视频列表适配层                                         |
| TCUGCVideoListAdapter.java | 短视频列表适配层                                         |
| TCLiveInfo.java            | 直播视频数据                                             |

#### 短视频录制模块

##### 模块简介

- 小视频提供录制 一分钟的 [短视频](https://cloud.tencent.com/document/product/584/9453) 功能，但 SDK 本身不显示录制时长。

##### 相关代码

| 类名                       | 描述                 |
| -------------------------- | -------------------- |
| TCVideoRecordActivity.java | 短视频录制界面       |
| RecordProgressView         | 按住拍摄短视频View   |
| ComposeRecordBtn           | 短视频多段拍摄进度条 |


#### 短视频本地文件选择模块

##### 模块简介

- 提供本地文件选择功能，列出了手机中所有mp4视频文件

##### 相关代码

| 类名                          | 描述                                                 |
| ----------------------------- | ---------------------------------------------------- |
| TCVideoChooseActivity.java    | 本地mp4文件选择界面                                  |
| TCVideoEditerListAdapter.java | 本地mp4文件列表适配器                                |
| TCVideoEditerMgr.java         | mp4视频文件管理类，提供接口获取存储在手机中的mp4文件 |
| TCVideoFileInfo.java          | 本地视频数据                                         |

#### 短视频编辑模块

##### 模块简介

- [视频编辑](https://cloud.tencent.com/document/product/584/9502) 包括视频裁剪、慢动作、滤镜、音乐混音、贴纸、添加字幕等功能

##### 相关代码

- videoeditor/ 目录

| 类名                           | 描述                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| TCVideoPreprocessActivity.java | 录制后的视频进入编辑时预处理类的洁面                         |
| TCVideoCutterActivity.java     | 短视频裁剪界面                                               |
| TCVideoEditerActivity.java     | 短视频裁剪后编辑界面，底部有音乐，滤镜，速度，色调，贴纸，字幕等功能 |
| TCVideoEffectActivity.java     | 点击底部按钮，进入短视频添加特效界面                         |
| BaseEditFragment.java          | 特效Fragment的父类，用于控制多个界面特效的播放状态           |
| TCVideoJoinerActivity.java     | 当选择多个文件进行编辑时，先将多个视频文件合成一个视频界面   |

- videoeditor/cutter/目录

  视频裁剪相关


- videoeditor/time/ 目录

  时间特效相关：包括慢动作，重复，视频倒放

- videoeditor/bgm/ 目录

  背景音相关

- videoeditor/paster/ 目录

  贴纸相关：包括动态贴纸和静态贴纸

- videoeditor/motion/ 目录

  动态滤镜相关：包括四种动态滤镜【目前不支持自定义扩展，如需更多滤镜特效，请联系我们】

- videoditor/bubble/ 目录

  气泡字幕相关

- videoeditor/utils/ 目录

  短视频编辑工具相关

- videoeditor/common/目录

  短视频编辑通用组件

- videojoiner/目录

  短视频合成相关

#### 短视频发布模块

##### 模块简介

- 将录制的文件发布到腾讯云视频分发平台（点播系统）中。

##### 相关代码

| 类名                          | 描述           |
| ----------------------------- | -------------- |
| TCVideoPublisherActivity.java | 短视频发布界面 |

#### 短视频播放

##### 模块简介

- 播放已经发布到点播系统中的视频，在小视频列表页面上下滑动可快速切换上/下一个视频

##### 相关代码

| 类名                      | 描述           |
| ------------------------- | -------------- |
| TCLivePlayerActivity.java | 短视频播放界面 |

#### 资料

##### 模块简介

- 资料模块主要负责用户资料的展示，存储，和 修改，并负责将这些操作同步到服务器。
- 用户资料主要包括，用户头像，昵称，性别等。 资料模块是IMSDK提供的功能，IMSDK提供扩展自定义字段的功能，方便开发者自定义更加丰富的用户资料。
- 资料模块会从服务器同步用户最新资料到APP，用户可以通过资料模块来浏览自己的相关资料，包括用户头像，昵称和性别等。
- 其他模块也可以通过资料模块获取，修改用户资料。

##### 相关代码

| 类名                        | 描述                                                         |
| --------------------------- | ------------------------------------------------------------ |
| TCUserInfoMgr.java          | 用户资料管理类，负责资料的存储和修改，并负责将操作同步到服务器，或者向服务器查询用户资料。 |
| ITCUserInfoMgrListener.java | 用户资料管理类与服务器通信的结果回调，包括查询资料的结果，修改资料的结果等。 |
| TCUserInfoFragment.java     | 用户资料展示页面                                             |
| TCAboutActivity             | 展示用户资料的界面                                           |
