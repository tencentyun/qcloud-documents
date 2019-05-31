## 1.工程结构
从github下载小直播代码，使用Android Studio打开工程后，您将看到如下的目录结构：
![](//mc.qcloudimg.com/static/img/af1b516a6c254da0224486bd35e3d2b6/image.png)

|文件/目录 | 说明 | 
|---------|---------|
| base| 小直播各模块用到的公共库|
| logic| 小直播逻辑层代码|
| ui| 小直播界面层代码|
| ui/customviews| 小直播ui用到的自定义控件|
| jniLibs| 小直播依赖的腾讯相关sdk，主要是BuglySDK、TLSSDK、IMSDK及RTMPSDK|
### 依赖第三方库 
- 网络：volley，gson
- 界面:appcompat，design，recyclerview
- 弹幕：dfm

## 2.模块介绍
小直播按照功能不同划分了6个模块，分别为：帐号、列表管理、推流、播放、消息以及资料，代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

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
- Logic:
- TCLoginMgr.java : 登录管理类，提供用户登录/注册相关接口与获取最后登录用户缓存接口
- TCApplication.java ： 初始化TIMManager时注册UserStatusListener监听获取用户签名失效/被踢下线消息

- UI:
- TCLoginActivity.java ： 用户登录页面
- TCRegisterActivity.java ： 用户注册页面

### 主界面&列表管理
#### 模块简介
- 主界面主要负责列表、推流和个人资料三个一级功能的切换
- 登录成功后，默认展示列表界面；点击推流按钮后，将跳转到推流的设置界面；点击个人资料按钮，将跳转到个人资料页面
- 列表管理包含列表的拉取和展示。目前我们的列表拉取协议支持拉取直播列表，点播列表和混合列表三种模式，小直播使用的是第三种模式，混合模式的排序规则是直播在前，点播在后

#### 相关代码 
- Logic:
- TCLiveListMgr.java ： 直播列表管理类，提供接口获取本地内存列表及从服务器更新列表。
- TCLiveInfo.java 直播视频数据
- UI:
- TCLiveListFragment.java ：直播列表展示页面，负责整个列表展示。
- TCLiveListAdapter.java ： 直播列表数据适配层，负责将一个直播数据转为列表的一项。

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
- Logic:
- TCPusherMgr.java： 直播管理类，和后台进行通信，拉取直播地址、通知后台退出直播
- UI:
- TCLivePublisherActivity.java: 推流模块Activity，所有的推流管理、消息管理、动画特效都在该类进行

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
- Logic:
- TCPlayerMgr.java： 播放管理类,和后台进行通信，通知后台进入房间、退出房间、点赞事件
- UI:
- TCLivePlayerActivity.java： 播放模块Activity，包括点播和直播，所有的播放管理、消息管理、动画特效都在该类进行

### 消息
#### 模块介绍
- 小直播的互动消息功能主要基于[ImSDK](https://cloud.tencent.com/doc/product/269/1561)的群聊功能实现，需要在IMSDK登录后才能调用
- 每个直播间都是一个直播大群，推流端在推流之前需要创建直播大群，结束推流时，解散该群；播放端在进入该直播间时，加入该群，退出直播间时，则退出该群
- 通过实现消息收发的监听类，可以在监听接口中获取相应的消息通知，目前实现的消息类型：文本消息、弹幕消息、点赞消息、用户加入/退出消息、群组解散消息
- 各种类型的消息都是以文本消息形式发送，采用统一的JSON格式，在JSON中携带消息类型、发送者id、昵称、头像、消息文本的信息，接收端收到消息后解析JSON格式，向上层回调各种类型的消息

#### 相关代码
- Logic:
- TCChatRoomMgr.java : 消息收发管理类，负责初始化消息循环，消息解析与消息封装，同时向主播提供创建/解散消息群组的接口，向观众提供加入/退出消息的接口
- UI:	
- TCLivePublisherActivity.java : 主播端消息显示界面
- TCLivePlayerActivity.java : 观众端消息显示界面
- TCInputTextMsgDialog.java: 文本消息输入框自定义控件
- TCHeartLayout.java/TCHeartView.java: 点赞飘心自定义控件
- TCDanmuMgr.java： 弹幕组件，弹幕使用Bilibili开源弹幕库

### 资料
#### 模块简介
- 资料模块主要负责用户资料的展示，存储，和 修改，并负责将这些操作同步到服务器。
- 用户资料主要包括，用户头像，昵称，性别，直播封面，定位等。 资料模块是IMSDK提供的功能，IMSDK提供扩展自定义字段的功能，方便开发者自定义更加丰富的用户资料。
- 资料模块会从服务器同步用户最新资料到APP，用户可以通过资料模块来浏览自己的相关资料，包括用户头像，昵称和性别等。
- 用户可以通过资料模块修改自己的相关资料，资料模块会将这些操作同步到服务器。
- 其他模块也可以通过资料模块获取，修改用户资料。

#### 相关代码
- Logic:
- TCUserInfoMgr.java: 用户资料管理类，负责资料的存储和修改，并负责将操作同步到服务器，或者向服务器查询用户资料。
- ITCUserInfoMgrListener.java: 用户资料管理类与服务器通信的结果回调，包括查询资料的结果，修改资料的结果等。
- UI:	
- TCUserInfoFragment.java: 用户资料展示页面
- TCEditUseInfoActivity.java: 用户资料修改页面
- TCLineEditTextView.java: 文本修改控件，对控件EditText的简单封装，可以用来修改文本，并显示相关信息
- TCTextEditActivity.java: 文本修改页面，对控件EditText的封装，使用单独的页面来修改文本，并显示相关信息