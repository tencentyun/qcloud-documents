## 1. 工程结构
下载小直播代码，使用Android Studio打开工程后，您将看到如下的目录结构：
![](https://main.qcloudimg.com/raw/677aefb020ad979e1a667281f1c0afa3.png)

<table>
<tr align="center">
<th width="200px">文件/目录</th>
<th width="700px">说明</th>
</tr>
<tr align="center">
<td>liveroom</td>
<td><a href="https://cloud.tencent.com/document/product/454/14606">直播连麦（LiveRoom）组件</a></td>
</tr>
<tr align="center">
<td>roomutil</td>
<td>LiveRoom组件用到的一些基础组件</td>
</tr>
<tr align="center">
<td>common</td>
<td>通用组件，包括各种工具类、自定义界面(美颜、点赞、弹幕、播放器控件)</td>
</tr>
<tr align="center">
<td>im</td>
<td>im消息的各种定义类，包括消息体、消息列表、用户信息</td>
</tr>
<tr align="center">
<td>login</td>
<td>帐号模块，包括登录以及注册</td>
</tr>
<tr align="center">
<td>mainui</td>
<td>小直播主界面，包括主 Activity 以及视频列表</td>
</tr>
<tr align="center">
<td>play</td>
<td>播放模块，包括直播和点播</td>
</tr>
<tr align="center">
<td>push</td>
<td>推流模块，包含摄像头推流和录屏推流</td>
</tr>
<tr align="center">
<td>userinfo</td>
<td>个人资料模块</td>
</tr>
<tr align="center">
<td>jniLibs</td>
<td>小直播依赖的腾讯相关sdk，主要是BuglySDK、TLSSDK、IMSDK及LiteAVSDK</td>
</tr>
</table>

## 2. 库使用说明
### [移动直播 SDK](https://cloud.tencent.com/document/product/454/7873)  (必选)
移动直播最主要的 SDK，其提供了推流、直播、点播、连麦、录屏等功能。
- aar
LiteAVSDK_Professional.aar

### IM SDK  (必选)
提供消息收发功能。
- jar 包

<table>
<tr align="center">
<th width="200px">包名</th>
<th width="700px">描述</th>
</tr>
<tr align="center">
<td>imsdk.jar</td>
<td>ImSDK基础包，只提供消息、资料关系链管理、群组管理等的最基础功能</td>
</tr>
<tr align="center">
<td>qalsdk.jar</td>
<td>SDK网络层jar包</td>
</tr>
<tr align="center">
<td>soload.jar</td>
<td>提高imsdk so库的加载成功率</td>
</tr>
<tr align="center">
<td>mobilepb.jar</td>
<td>protobuffer处理相关jar包</td>
</tr>
<tr align="center">
<td>tls_sdk.jar</td>
<td>帐号系统jar包</td>
</tr>
<tr align="center">
<td>wup-1.0.0-SNAPSHOT.jar</td>
<td>无线统一协议jar包</td>
</tr>
</table>

- so 库
移动直播目前只集成 armeabi 架构
	- lib_imcore_jni_gyp.so
	- libqalcodecwrapper.so
	- libqalmsfboot.so
	- libwtcrypto.so

### 商业增值版 (小直播源码中没有)
基于优图实验室的 AI 专利技术，实现了大眼、瘦脸、动效贴纸、绿幕等特效功能。如果没有用到该功能，可以删除相关 so 库。
- libblasV8.so   
- librsjni.so  
- libRSSupport.so  

### volley  (非必选)
第三方的网络请求库

### Gson  (非必选)
第三方的用来在Java 对象和JSON 数据之间进行映射的Java 类库

### Glide  (非必选)
第三方的图片加载库

### dfm  (非必选)
Bilibili 弹幕库。如果您希望在聊天中有弹幕效果，建议保留。


## 3. 模块介绍
小直播按照功能不同划分了7个模块，分别为：帐号、互动消息、主界面、推流、播放、资料以及连麦，代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

### 帐号模块
#### 模块简介
- 帐号模块负责处理用户登录/注册以及登录缓存的逻辑。
- 登录注册功能使用IM的[独立模式](https://cloud.tencent.com/document/product/269/1508)实现。
- 用户登录时，在自有帐号登录服务器验证成功后，服务器使用私钥派发签名（UserSig）给客户端。客户端使用UserId与UserSig调用ImSDK的login接口完成IM模块的登录。
- 用户可以通过帐号、密码进行注册与登录。
- 帐号模块会缓存最后登录的用户基本信息（UserId与UserSig）在本地，通过接口调用可以获取最近登录的用户信息并判断是否需要重新登录。

#### 相关代码 
<table>
<tr align="center">
<th width="200px">类名</th>
<th width="700px">描述</th>
</tr>
<tr align="center">
<td>TCUserMgr.java</td>
<td>登录管理类，提供用户登录/注册相关接口与获取最后登录用户缓存接口</td>
</tr>
<tr align="center">
<td>TCLoginActivity.java</td>
<td>用户登录页面</td>
</tr>
<tr align="center">
<td>TCRegisterActivity.java</td>
<td>用户注册页面</td>
</tr>
</table>


### 互动消息
#### 模块简介
- 小直播的互动消息功能主要基于[ImSDK](https://cloud.tencent.com/doc/product/269/1561)的群聊功能实现，需要在IMSDK登录后才能调用
- 每个直播间都是一个直播大群，推流端在推流之前需要创建直播大群，结束推流时，解散该群；播放端在进入该直播间时，加入该群，退出直播间时，则退出该群
- 通过实现消息收发的监听类，可以在监听接口中获取相应的消息通知，目前实现的消息类型：文本消息、弹幕消息、点赞消息、用户加入/退出消息、群组解散消息
- 各种类型的消息都是以文本消息形式发送，采用统一的JSON格式，在JSON中携带消息类型、发送者id、昵称、头像、消息文本的信息，接收端收到消息后解析JSON格式，向上层回调各种类型的消息

#### 相关代码
<table>
<tr align="center">
<th width="200px">类名</th>
<th width="700px">描述</th>
</tr>
<tr align="center">
<td>BaseRoom.java</td>
<td>房间管理类，负责初始化消息循环，消息解析与消息封装，同时向主播提供创建/解散消息群组的接口，向观众提供加入/退出群的接口</td>
</tr>
<tr align="center">
<td>TCChatMsgListAdapter.java</td>
<td>推流界面和直播界面中互动消息列表的设配器</td>
</tr>
<tr align="center">
<td>TCSimpleUserInfo.java</td>
<td>用户基本信息实体类，主要封装了用户id、昵称、头像地址</td>
</tr>
</table>


### 主界面&列表管理
#### 模块简介
- 主界面主要负责列表、推流和个人资料三个一级功能的切换
- 登录成功后，默认展示列表界面；点击推流按钮后，将弹出对话框让你选择直播推流；点击个人资料按钮，将跳转到个人资料页面
- 列表管理包含列表的拉取和展示。小直播中以直播、回放两个列表项进行展示。

<table>
<tr align="center">
<th width="200px">类名</th>
<th width="700px">描述</th>
</tr>
<tr align="center">
<td>TCSplashActivity.java</td>
<td>闪屏界面</td>
</tr>
<tr align="center">
<td>TCMainActivity.java</td>
<td>主界面，用于呈现直播列表，开启直播页，用户信息页</td>
</tr>
<tr align="center">
<td>TCLiveListFragment.java</td>
<td>列表展示界面，负责呈现直播、点播数据</td>
</tr>
<tr align="center">
<td>TCLiveListAdapter.java</td>
<td>直播、点播列表适配层</td>
</tr>
</table>


### 推流模块
#### 模块简介
- 推流模块主要包括，主播视频数据采集，渲染，推流，主播和观众消息互动等功能。
- 主播端可以采集自己视频和声音数据推送到视频云服务器，观众可以在其他客户端观看，主播端可以自定义视频采集分辨率，美颜，美白，硬编码等功能。
- 主播端可以创建自己的房间，观众可以加入房间和主播互动，观众可以发送普通消息、弹幕消息以及点赞消息，主播端会在对应的消息列表，弹幕动画位置展示对应的消息，关于消息的详细介绍，请参考“消息”模块
- 主播端可以展示观众列表，当有观众进入，退出房间时候，观众列表会刷新，主播也会收到观众进入或则退出房间消息


#### UI层级结构
SDK渲染视频时，startCameraPreview的参数View（即videoParentView）是用来承载SDK渲染层的，SDK会在其之上构建一个用于OpenGL渲染的子view，如果您想要在渲染画面之上实现弹幕、献花之类的UI控件，应该如下图这般创建一个与之平级的view
![](http://mc.qcloudimg.com/static/img/3da33f8c62b9339a365faddd2635faa2/image.png)

#### 相关代码 

<table>
<tr align="center">
<th width="200px">类名</th>
<th width="700px">描述</th>
</tr>
<tr align="center">
<td>TCPublishSettingActivity.java</td>
<td>位置服务类，用于主播推流前设置定位</td>
</tr>
<tr align="center">
<td>TCLocationHelper.java</td>
<td>位置服务类，用于主播推流前设置定位</td>
</tr>
<tr align="center">
<td>DetailDialogFragment.java</td>
<td>直播结束统计信息展示类，用于展示主播在直播过程中观看人数、点赞数以及直播时长</td>
</tr>
<tr align="center">
<td>TCLivePublisherActivity.java</td>
<td>推流Activity，动画特效在这里实现，调用LiveRoom封装的接口处理推流管理、消息管理等</td>
</tr>
<tr align="center">
<td>TCMusicSelectView.java</td>
<td>背景音乐选择类，选择本地音乐作为背景音乐</td>
</tr>
<tr align="center">
<td>MusicListView.java</td>
<td>本地音乐显示类，以列表形式显示本地音乐</td>
</tr>
<tr align="center">
<td>TCAudioControl.java</td>
<td>背景音乐控制类，提供播放、停止、暂停、调节音量等接口</td>
</tr>
<tr align="center">
<td>TCScreenRecordActivity.java</td>
<td>录屏直播类</td>
</tr>
<tr align="center">
<td>CameraPreview.java</td>
<td>摄像头预览画面渲染类，结合 FloatingCameraView 一起使用</td>
</tr><tr align="center">
<td>FloatingCameraView.java</td>
<td>摄像头悬浮窗，主要是在录屏推流场景下提供主播视角</td>
</tr>
<tr align="center">
<td>FloatingView.java</td>
<td>桌面悬浮球类</td>
</tr>
</table>

小直播推流模块使用的是 [直播连麦( LiveRoom )方案](https://cloud.tencent.com/document/product/454/14606)。具体代码模块如下：

![](https://main.qcloudimg.com/raw/935de49904f9129ae84e440c96921770.png)


### 播放模块
#### 模块简介
- 播放模块主要包括：主播视频数据播放、观众和主播消息互动等功能。
- 观众端可以进入主播的房间，可以给主播发送普通消息、弹幕消息以及点赞消息，关于消息的详细介绍，请参考“消息”模块
- 观众端可以展示主播信息，观众列表，当有观众进入，退出房间时候，观众列表会刷新，同时消息列表也会展示其他观众进入，退出房间的消息。

#### UI层级结构
请参考推流模块的UI层级结构

#### 相关代码

<table>
<tr align="center">
<th width="200px">类名</th>
<th width="700px">描述</th>
</tr>
<tr align="center">
<td>TCLivePlayerActivity.java</td>
<td>播放类</td>
</tr>
</table>

### 资料
#### 模块简介
- 资料模块主要负责用户资料的展示，存储，和 修改，并负责将这些操作同步到服务器。
- 用户资料主要包括，用户头像，昵称，性别，直播封面，定位等。 资料模块是IMSDK提供的功能，IMSDK提供扩展自定义字段的功能，方便开发者自定义更加丰富的用户资料。
- 资料模块会从服务器同步用户最新资料到APP，用户可以通过资料模块来浏览自己的相关资料，包括用户头像，昵称和性别等。
- 用户可以通过资料模块修改自己的相关资料，资料模块会将这些操作同步到服务器。
- 其他模块也可以通过资料模块获取，修改用户资料。
	
#### 相关代码

<table>
<tr align="center">
<th width="200px">类名</th>
<th width="700px">描述</th>
</tr>
<tr align="center">
<td>TCUserInfoFragment.java</td>
<td>用户资料展示页面</td>
</tr>
<tr align="center">
<td>TCEditUseInfoActivity.java</td>
<td>用户资料修改页面</td>
</tr>
<tr align="center">
<td>TCLineEditTextView.java</td>
<td>文本修改控件，对控件EditText的简单封装，可以用来修改文本，并显示相关信息</td>
</tr>
</table>

### 连麦
#### 模块简介
- 小直播的连麦功能采用的是[LiveRoom](https://cloud.tencent.com/document/product/454/14606)方案。

#### 连麦交互流程图
![](https://main.qcloudimg.com/raw/52c2eaa6d4ade76fbc71d81e479fd50c.jpg)
