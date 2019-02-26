## 1.工程结构
[下载](https://cloud.tencent.com/document/product/454/6991)小直播代码后，您将看到TCLVBIMDemo.xcworkspace文件，这是小直播的Xcode工程工作区，用于管理小直播的代码工程和依赖的第三方开源类库（位于Pods目录下），如果您需要编译或浏览小直播相关代码，请打开此文件，请勿直接打开小直播的工程文件TCLVBIMDemo.xcodeproj。打开TCLVBIMDemo.xcworkspace后，您将看到如下的工程目录结构：
![](//mc.qcloudimg.com/static/img/8673bf53392e34a9f38d8a5a8625e8eb/image.jpg)

|工程目录 | 说明 | 
|---------|---------|
| TCLVBIMDemo/TCLVBIMDemo/Classes/LVB/Base| 小直播各模块用到的公共库|
| TCLVBIMDemo/TCLVBIMDemo/Classes/LVB/Logic| 小直播逻辑层代码|
| TCLVBIMDemo/TCLVBIMDemo/Classes/LVB/UI| 小直播界面层代码|
| TCLVBIMDemo/Framework| 小直播依赖的framework，主要是TLSSDK、IMSDK、RTMPSDK以及QALSDK(COS上传组件)|
| TCLVBIMDemo/TCLVBIMDemoUpload| Replaykit方式录屏的扩展的逻辑层代码|
| TCLVBIMDemo/TCLVBIMDemoUploadUI|  Replaykit方式录屏的扩展的界面层代码|
| Pods| 使用CocoaPods管理小直播用到的第三方开源类库|

## 2.编译运行
下载代码后，打开**TCLVBIMDemo.xcworkspace**工程文件（请勿直接打开小直播的工程文件TCLVBIMDemo.xcodeproj），由于小直播目前还不支持模拟器调试，只能在真机调试，所以您需要按照如下步骤配置工程的证书：
**Step1:配置bundle id及签名证书**
![](//mc.qcloudimg.com/static/img/e2c29a0daa9dbba958c970fadc0a3f09/image.jpg)
**Step2:配置完签名后，还需要配置App Groups**
![](//mc.qcloudimg.com/static/img/cd7f2559857e8248efa08551e80e8c05/image.jpg)
**Step3:配置其他TARGETS**
按照Step1和Step2配置另外2个targets：TCLVBIMDemoUpload和TCLVBIMDemoUploadUI，这2个targets是用于replaykit方式的录屏推流，如果您不需要这个功能，可以删除这2个targets

配置完成后，工程就可以在真机上运行，但是如果要真正体验小直播的功能，还需要修改TCConstants.h中的配置，如何配置，请参考[终端集成](https://cloud.tencent.com/document/product/454/7999#4.-.E7.BB.88.E7.AB.AF.E9.9B.86.E6.88.90.E5.8F.8A.E5.9B.9E.E8.B0.83.E8.AE.BE.E7.BD.AE)

## 3.模块介绍
小直播按照功能不同划分了7个模块，分别为：帐号、列表管理、推流、播放、消息、资料以及连麦，代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

### 帐号模块
#### 模块简介
- 帐号模块负责处理用户登录/注册以及登录缓存的逻辑
- 登录注册功能使用[TLSSDK托管](https://cloud.tencent.com/doc/product/269/%E6%89%98%E7%AE%A1%E6%A8%A1%E5%BC%8F)登录实现
- 如果您已经有自己的帐号体系，可以直接替换该模块，并调用TCIMPlatform的guestLogin接口以游客身份使用IM通道，详情请参考[替换帐号](https://cloud.tencent.com/doc/api/258/6441)
- 在TLSSDK登录鉴权成功后，可以通过鉴权返回的UserId与UserSig调用ImSDK的login接口完成IM模块的登录
- 用户可以通过帐号密码/手机验证码两种方式进行注册与登录
- 帐号模块会缓存最后登录的用户基本信息（UserId与UserSig）在本地，通过接口调用可以获取最近登录的用户信息并判断是否需要重新登录
- 登录实现为互踢机制，登录时间在前的用户会接收到强制下线消息

#### 相关代码
- Logic:
	- TCLoginParam: 用来管理用户的登录信息，如登录信息的缓存、过期判断等
	- TCTLSPlatform：TLS注册登录相关接口封装
	- TCIMPlatform: ImSDK登录相关接口封装

- UI:
	- TCLoginViewController: 过度界面，从缓存中读取登录数据，如果可以自动登录，则直接调用imlogin的接口进行im登录，否则拉取登录界面
	- TCTLSLoginViewController：TLS登录界面，包含用户名登录、短信登录以及游客登录
	- TCTLSRegisterViewController：TLS注册界面，包含用户名注册和短信注册

### 主界面&列表管理
#### 模块简介
- 主界面主要负责列表、推流和个人资料三个一级功能的切换
- 登录成功后，默认展示列表界面；点击推流按钮后，将跳转到推流的设置界面；点击个人资料按钮，将跳转到个人资料页面
- 列表管理包含列表的拉取和展示。目前我们的列表拉取协议支持拉取直播列表，点播列表和混合列表三种模式，小直播使用的是第三种模式，混合模式的排序规则是直播在前，点播在后

#### 相关代码
- Logic:
	- TCLiveListModel: 直播/点播列表的数据层定义以及序列化/反序列化实现
	- TCLiveListMgr: 列表管理的逻辑层代码，主要负责列表数据的拉取、缓存和更新。目前只支持全量拉取，暂不支持增量拉取。列表拉取的协议设计成分页模式，调用列表拉取接口后，逻辑层循环从后台拉取列表，直至拉取完成，为了提升拉取体验，在拉取到第一页数据后，就立即通知界面刷新展示
	
- UI:
	- TCNavigationController: 定制的导航栏，主要是设置导航栏的背景颜色
	- TCMainTabViewController: 主界面的tab bar控件，用于切换列表、推流和个人资料页面
	- TCPushSettingViewController: 推流设置页，设置推流的封面、标题及定位功能
	- TCLiveListCell: 直播/点播列表的Cell类，主要展示封面、标题、昵称、在线数、点赞数、定位位置
	- TCLiveListViewController: 直播/点播列表的TableViewController，负责展示直播、点播列表，点击后跳转播放界面

### 推流模块
#### 模块简介
- 推流模块主要包括，主播视频数据采集，渲染，推流，主播和观众消息互动等功能。
- 主播端可以采集自己视频和声音数据推送到视频云服务器，观众可以在其他客户端观看，主播端可以自定义视频采集分辨率，美颜，美白，硬编码等功能。
- 主播端可以创建自己的房间，观众可以加入房间和主播互动，观众可以发送普通消息、弹幕消息以及点赞消息，主播端会在对应的消息列表，弹幕动画位置展示对应的消息，关于消息的详细介绍，请参考“消息”模块
- 主播端可以展示观众列表，当有观众进入，退出房间时候，观众列表会刷新，主播也会收到观众进入或则退出房间消息

#### 推流时序图
![](//mc.qcloudimg.com/static/img/6fb00666a6a1cdea732fbddccc5fc786/image.png)

#### UI层级结构
![](//mc.qcloudimg.com/static/img/df03a372dfdb1fe5ca8a8675dc9e7dcb/image.png)

#### 相关代码
- Logic:
	- TCPusherMgr: 推流模块逻辑层代码，主要是与业务Server进行协议通信
- UI：
	- TCPushController ：推流模块主控制器，里面承载了渲染view，逻辑view，以及推流相关逻辑，同时也是SDK层事件通知的接收者。
	- TCPushDecorateView 推流模块逻辑view，里面展示了消息列表，弹幕动画，观众列表，美颜，美白等UI，其中与SDK的逻辑交互需要交给主控制器处理。

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
	- TCPlayerMgr: 播放模块逻辑层代码，主要是与业务Server进行协议通信
- UI:
	- TCPlayController ：播放模块主控制器，里面承载了渲染view，逻辑view，以及播放相关逻辑，同时也是SDK层事件通知的接收者。
	- TCPlayDecorateView 播放模块逻辑view，里面展示了消息列表，弹幕动画，观众列表等UI，其中与SDK的逻辑交互需要交给主控制器处理。

### 消息
#### 模块介绍
- 小直播的互动消息功能主要基于[ImSDK](https://cloud.tencent.com/doc/product/269/1569)的群聊功能实现，需要在IMSDK登录后才能调用
- 每个直播间都是一个直播大群，推流端在推流之前需要创建直播大群，结束推流时，解散该群；播放端在进入该直播间时，加入该群，退出直播间时，则退出该群
- 通过实现消息收发的监听类，可以在监听接口中获取相应的消息通知，目前实现的消息类型：文本消息、弹幕消息、点赞消息、用户加入/退出消息、群组解散消息
- 各种类型的消息都是以文本消息形式发送，采用统一的JSON格式，在JSON中携带消息类型、发送者id、昵称、头像、消息文本的信息，接收端收到消息后解析JSON格式，向上层回调各种类型的消息
- 通过实现delegate就可以监听对应的消息，需要注意的是，接收群系统消息的delegate需要在登录之前设置

#### 相关代码
- 类说明
	- Logic:
		-TCMsgHandler: 消息相关接口的封装以及回调的实现，主要是对ImSDK的相关接口进行封装以实现对普通文本消息、弹幕消息和点赞消息的发送和接收
	
	- UI:
		- TCMsgBulletView 弹幕动画，里面展示用户发送的弹幕消息，可以自定义弹幕的动画效果。 
		- TCMsgListTableView 消息列表，里面展示用户发送的普通消息，以及退出，进入房间消息。
		- TCMsgListCell 消息列表TCMsgListTableView的cell，展示一条消息信息
		- TCAudienceListTableView 展示观众列表动画
		- TCMsgModel    消息数据model
	
- 动画说明：
   - TCMsgBulletView 弹幕动画，一个TCMsgBulletView的实例就是一行弹幕动画容器,您可以根据自己的需求创建N个实例来展示N行动画，每行弹幕动画容器在init的时候会先创建一个弹幕View，当有弹幕消息来的时候，弹幕View会根据弹幕消息自动计算自己的大小，然后开始动画，当弹幕View动画结束的时候会被放在 unUsedAnimateViewArray容器里面，当有新的弹幕消息来的时候，会先判断 unUsedAnimateViewArray容器里面是否有弹幕View，如果有，会选择容器里面的一个View开启新的动画，如果没有，会再去初始化一个新的弹幕View开启动画，同样当这个新的弹幕View动画结束的时候也会被放在_unUsedAnimateViewArray容器里面。于此同时，TCMsgBulletView还提供了一个对外变量 lastAnimateView，这个变量的目的是记录每一行弹幕动画容器里面最后一个弹幕View的位置，当有新的弹幕消息来的时候，就可以根据每行 lastAnimateView位置来判断这个消息该扔给哪行弹幕动画容器显示。
   
   - TCMsgListTableView 消息列表动画，当有新的消息来得时候，会先判断消息列表是否需要滚动，这个时候要记录两个高度，一个是所有cell的总高度 totalCellHeight，一个是TCMsgListTableView的高度 listTableViewHeight,当 totalCellHeight >= listTableViewHeight的时候，开始滚动。另外当用户拖动消息列表的时候，滚动会暂停，当用户拖动结束，如果listTableViewOffset >= totalCellHeight时候，列表又开始滚动，当然，里面还有不少细节调整，具体代码请参考小直播。

   - TCAudienceListTableView 观众列表动画，因为观众数量不定，而且进出频繁，内存创建与销毁频繁，所以这里没有用scrollView + imageView去做，而是直接使用tableView控件，实现内存复用，通过旋转tableView 90度，达到我们需要的横排显示效果，这里要特别注意tableView的frame设置，具体代码请参考小直播。
   - 因为时间精力限制，上述动画可能在性能，效果上还存在一些不足之处，这里仅提供参考，厂商可以根据自己的需求自定义动画效果。

### 资料
#### 模块简介
- 资料模块主要负责用户资料的展示，存储，和 修改，并负责将这些操作同步到服务器。
- 用户资料主要包括，用户头像，昵称，性别，直播封面，定位等。 资料模块是IMSDK提供的功能，IMSDK提供扩展自定义字段的功能，方便开发者自定义更加丰富的用户资料。
- 资料模块会从服务器同步用户最新资料到APP，用户可以通过资料模块来浏览自己的相关资料，包括用户头像，昵称和性别等。
- 用户可以通过资料模块修改自己的相关资料，资料模块会将这些操作同步到服务器。
- 其他模块也可以通过资料模块获取，修改用户资料。
	
#### 相关代码
- Logic:
	   - TCUserInfoMgr： 用户资料管理类，负责资料的存储和修改，并负责将操作同步到服务器，或者向服务器查询用户资料。	   
- UI:
	   - TCEditUserInfoController	用户资料修改页面，可在此页面修改用户头像，昵称，性别信息
	   - TCUserInfoController       用户信息展示界面，在这里可以展示头像，昵称，用户id信息
	   - TCUserInfoTableViewCell    用于绘制展示用户个人信息界面的tableview
	   - TCEditUserInfoTableViewCell  用于绘制编辑个人信息页面的tableview，用于可直接在此tableview内编辑个人信息
	   - TCUserInfoTableViewCell      用于绘制负责的tableview中的cell如图片，文字等组合控件

### 连麦
#### 模块简介
- 小直播结合SDK的连麦能力以及im的C2C消息接口实现了连麦功能
-  C2C消息主要用于主播和连麦观众的通知和回复：观众发起连麦请求和观众已推流成功需要通知主播，主播做相应回复
- 主播端开始直播后，连麦观众向主播发起连麦请求，主播同意连麦请求后，连麦观众和主播分别通过对方的播放地址拉取视频数据并展示，后台对主播和连麦观众的推流数据进行混流，第三方观众看到的直接是混流后的视频

#### 时序图
![](//mc.qcloudimg.com/static/img/1b80501829fd5528bf41d4c9a84aed2b/image.png)

#### 相关代码
- Logic:
	- TCLinkMicMgr：对C2C消息进行封装，对上层提供通知和回复的接口
- UI:
	- TCLinkMicPushController：连麦主播端的界面实现，继承自TCPushController，实现连麦请求的响应和连麦观众画面的拉取
	- TCLinkMicPlayController：连麦观众端的界面实现，继承自TCPlayController，发起连麦请求、进行推流以及主播端画面的拉取

  
