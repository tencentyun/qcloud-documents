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
小直播按照功能不同划分了7个模块，分别为：帐号、列表管理、播放、录制、编辑、发布以及资料模块，代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

### 帐号模块
- 帐号模块负责处理用户登录/注册以及登录缓存的逻辑；
- 如果您已经有自己的帐号体系，可以直接替换该模块；
- 帐号模块通过调用 TCUserMgr 的 register 将用户名，密码注册到小视频的业务后台，调用 TCUserMgr 的 login 方法进行登录，并将登录信息缓存到本地，退出登录，清空本地缓存。


### 主界面和列表管理
#### 模块简介
- 主界面主要负责点播列表、录制、个人资料三个一级功能的切换。
- 进入 App 后，默认展示列表界面；单击录制按钮后，如果未登录，会先跳转到登录界面，如果已经登录，将跳转到推流的界面；单击个人资料按钮，将跳转到个人资料页面。
- 列表管理包含列表的拉取和展示。

#### 相关代码
- Logic:
	- TCLiveListModel: 点播列表的数据层定义以及序列化/反序列化实现。
	- TCLiveListMgr: 列表管理的逻辑层代码，主要负责列表数据的拉取、缓存和更新。目前只支持全量拉取，暂不支持增量拉取。列表拉取的协议设计成分页模式，调用列表拉取接口后，逻辑层循环从后台拉取列表，直至拉取完成，为了提升拉取体验，在拉取到第一页数据后，就立即通知界面刷新展示。
	
- UI:
	- TCNavigationController: 定制的导航栏，主要是设置导航栏的背景颜色。
	- TCMainTabViewController: 主界面的 tab bar 控件，用于切换列表、录制和个人资料页面。
	- TCLiveListCell: 点播列表的 Cell 类，主要展示封面、标题、昵称。
	- TCLiveListViewController: 点播列表的 TableViewController，负责展示点播列表，单击后跳转播放界面。


### 播放模块
#### 模块简介
- 播放模块主要包括：短视频预加载，播放，缓存，分享等功能。

#### 相关代码
- Logic:
	- TCPlayerMgr: 播放模块逻辑层代码，主要是与业务 Server 进行协议通信。
- UI:
	- TCVodPlayViewController ：播放模块主控制器，里面承载了渲染 view，逻辑 view，以及播放相关逻辑，同时也是 SDK 层事件通知的接收者。
	- TCPlayDecorateView：播放模块逻辑 view，里面展示了主播信息，点播控制相关逻辑控件，其中与 SDK 的逻辑交互需要交给主控制器处理。
	- TCPlayViewCell：点播上下滑动 cell，主要实现在播放的过程中，可以上下滑动切换其他主播播放。


### 录制模块
#### 模块简介
- 录制模块主要包括：短视频多段录制，多段回删，多分辨率录制，变速录制等。

#### 相关代码
- Logic:
	- PituMotionAddress: 里面存储了动效的下载路径。
- UI:
	- TCVideoRecordViewController ：录制模块主控制器，里面承载了渲染 view，逻辑 view，以及录制相关逻辑，同时也是 SDK 层事件通知的接收者。
	- TCVideoRecordProcessView：录制进度 view，主要展示视频在录制过程中回删。
	- BeautySettingPanel：录制动效设置 view，这里可以对录制的美颜，美白等进行设置，设置完成之后会回调给录制主控制器。

### 编辑模块
#### 模块简介
- 编辑模块主要包括：短视频裁剪，BGM，滤镜风格，特效，动态贴纸，静态贴纸等。

#### 相关代码
- Logic:
	- VideoInfo: 里面存储了动态贴纸，静态贴纸，普通字幕，气泡字幕相关信息。
- UI:
	- TCVideoCutViewController ：视频裁剪主控制器，里面承载了渲染 view，逻辑 view，以及裁剪相关逻辑。
	- TCVideoEditViewController：视频编辑主控制器，里面承载了渲染 view，逻辑 view，以及编辑相关逻辑。
	- TCVideoLoadingController：视频本地加载主控制器，里面主要实现了本地视频加载相关逻辑，加载完后的视频会发送给裁剪主控制器。
	- VideoPreview ：视频编辑渲染 view，主要用于视频编辑过程中的预览。
	- BottomTabBar ：视频编辑模块切换 view，主要用于视频编辑 BGM,滤镜风格，特效，动态贴纸，静态贴纸等功能切换。
	- VideoCutView：视频微缩图 view，主要用于视频播放进度选择，视频剪切等。
	- EffectSelectView：特效选择 view。
	- PasterAddView：贴纸添加 view，主要用于动态/静态贴纸添加。
	- TextAddView：字幕添加 view，主要用于普通字幕/气泡字幕添加。

### 发布模块
#### 模块简介
- 发布模块主要包括：短视频发布。

#### 相关代码
- UI:
	- TCVideoPublishController ：发布主控制器，里面承载了发布相关逻辑。

### 资料模块
#### 模块简介
- 资料模块主要负责用户资料的展示、存储和修改，并负责将这些操作同步到服务器。
- 用户资料主要包括，用户头像、昵称、性别、直播封面、定位等。 资料模块是 IMSDK 提供的功能，IMSDK 提供扩展自定义字段的功能，方便开发者自定义更加丰富的用户资料。
- 资料模块会从服务器同步用户最新资料到 App，用户可以通过资料模块来浏览自己的相关资料，包括用户头像、昵称和性别等。
- 用户可以通过资料模块修改自己的相关资料，资料模块会将这些操作同步到服务器。
- 其他模块也可以通过资料模块获取，修改用户资料。
	
#### 相关代码
- Logic:
	   - TCUserInfoMgr： 用户资料管理类，负责资料的存储和修改，并负责将操作同步到服务器，或者向服务器查询用户资料。	   
- UI:
	   - TCEditUserInfoController	用户资料修改页面，可在此页面修改用户头像，昵称，性别信息。
	   - TCUserInfoController       用户信息展示界面，在这里可以展示头像，昵称，用户 id 信息。
	   - TCUserInfoTableViewCell    用于绘制展示用户个人信息界面的 tableview。
	   - TCEditUserInfoTableViewCell  用于绘制编辑个人信息页面的 tableview，用于可直接在此 tableview 内编辑个人信息。


  
