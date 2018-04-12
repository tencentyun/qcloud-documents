## 1.工程结构
![](https://main.qcloudimg.com/raw/f5f676f1fbbd87cc86fab4682e63de39.png)

|工程目录 | 说明 | 
|---------|---------|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/Login| 小视频登录模块|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/List| 小视频点播列表模块|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/Play| 小视频点播播放模块|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UGCRecord| 小视频录制模块|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UGCEditor| 小视频编辑模块|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UGCPublish| 小视频发布模块|
| TXXiaoShiPinDemo/TXXiaoShiPinDemo/Classes/UserInfo| 小视频用户信息模块|

## 2.模块介绍
小直播按照功能不同划分了7个模块，分别为：帐号、列表管理、播放、消息、资料以及连麦，代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

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
- 主界面主要负责点播列表、录制、个人资料三个一级功能的切换
- 进入app后，默认展示列表界面；点击录制按钮后，如果未登录，会先跳转到登录界面，如果已经登录，将跳转到推流的界面；点击个人资料按钮，将跳转到个人资料页面
- 列表管理包含列表的拉取和展示。

#### 相关代码
- Logic:
	- TCLiveListModel: 点播列表的数据层定义以及序列化/反序列化实现
	- TCLiveListMgr: 列表管理的逻辑层代码，主要负责列表数据的拉取、缓存和更新。目前只支持全量拉取，暂不支持增量拉取。列表拉取的协议设计成分页模式，调用列表拉取接口后，逻辑层循环从后台拉取列表，直至拉取完成，为了提升拉取体验，在拉取到第一页数据后，就立即通知界面刷新展示
	
- UI:
	- TCNavigationController: 定制的导航栏，主要是设置导航栏的背景颜色
	- TCMainTabViewController: 主界面的tab bar控件，用于切换列表、录制和个人资料页面
	- TCLiveListCell: 点播列表的Cell类，主要展示封面、标题、昵称
	- TCLiveListViewController: 点播列表的TableViewController，负责展示点播列表，点击后跳转播放界面


### 播放模块
#### 模块简介
- 播放模块主要包括：短视频预加载，播放，缓存，分享等功能

#### 相关代码
- Logic:
	- TCPlayerMgr: 播放模块逻辑层代码，主要是与业务Server进行协议通信
- UI:
	- TCVodPlayViewController ：播放模块主控制器，里面承载了渲染view，逻辑view，以及播放相关逻辑，同时也是SDK层事件通知的接收者。
	- TCPlayDecorateView：播放模块逻辑view，里面展示了主播信息，点播控制相关逻辑控件，其中与SDK的逻辑交互需要交给主控制器处理。
	- TCPlayViewCell：点播上下滑动cell，主要实现在播放的过程中，可以上下滑动切换其他主播播放


### 录制模块
#### 模块简介
- 录制模块主要包括：短视频多段录制，多段回删，多分辨率录制，变速录制等

#### 相关代码
- Logic:
	- PituMotionAddress: 里面存储了动效的下载路径
- UI:
	- TCVideoRecordViewController ：录制模块主控制器，里面承载了渲染view，逻辑view，以及录制相关逻辑，同时也是SDK层事件通知的接收者。
	- TCVideoRecordProcessView：录制进度view，主要展示视频在录制过程中回删。
	- BeautySettingPanel：录制动效设置view，这里可以对录制的美颜，美白等进行设置，设置完成之后会回调给录制主控制器。

### 编辑模块
#### 模块简介
- 编辑模块主要包括：短视频裁剪，BGM，滤镜风格，特效，动态贴纸，静态贴纸等

#### 相关代码
- Logic:
	- VideoInfo: 里面存储了动态贴纸，静态贴纸，普通字幕，气泡字幕相关信息
- UI:
	- TCVideoCutViewController ：视频裁剪主控制器，里面承载了渲染view，逻辑view，以及裁剪相关逻辑。
	- TCVideoEditViewController：视频编辑主控制器，里面承载了渲染view，逻辑view，以及编辑相关逻辑。
	- TCVideoLoadingController：视频本地加载主控制器，里面主要实现了本地视频加载相关逻辑，加载完后的视频会送给裁剪主控制器。
	- VideoPreview ：视频编辑渲染view，主要用于视频编辑过程中的预览。
	- BottomTabBar ：视频编辑模块切换view，主要用于视频编辑BGM,滤镜风格，特效，动态贴纸，静态贴纸等功能切换。
	- VideoCutView：视频微缩图view，主要用于视频播放进度选择，视频剪切等。
	- EffectSelectView：特效选择view。
	- PasterAddView：贴纸添加view，主要用于动态/静态贴纸添加。
	- TextAddView：字幕添加view，主要用于普通字幕/气泡字幕添加

### 发布模块
#### 模块简介
- 发布模块主要包括：短视频发布

#### 相关代码
- UI:
	- TCVideoPublishController ：发布主控制器，里面承载了发布相关逻辑。

### 资料模块
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


  
