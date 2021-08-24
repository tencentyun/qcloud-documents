[](id:structure)
## 1. 工程结构
![](https://main.qcloudimg.com/raw/6dece0a7e9535e3fdb138975ff69452c.png)
小视频主要集成了 UGCKit 作为核心功能库。集成方式参考 [UGCKit](https://github.com/tencentyun/UGSVSDK/tree/master/iOS)（主要负责播放录制）。
小视频的美颜功能，主要集成 BeautySettingkit 实现。集成方式请参见 [类抖音特效](https://cloud.tencent.com/document/product/584/20323)、[动效变脸](https://cloud.tencent.com/document/product/584/13509) 文档，相关代码都可以在 BeautySettingKit 目录下找到。
 
[](id:function)
## 2. 模块介绍
小直播按照功能不同划分了7个模块，分别为：
- 帐号、列表管理、发布以及资料模块（处于小视频目录下）。
- 播放、录制、编辑模块由 UGCKit 负责。

[](id:accounts)
### 帐号模块
- 帐号模块负责处理用户登录/注册，以及登录缓存的逻辑。
- 如果您已经有自己的帐号体系，可以直接替换该模块。
- 账号模块的 UI 逻辑分为 `XiaoShiPin/AppViewControllers/Account` 及 `XiaoShiPin/AppViewControllers/AccountInfo`，前者涉及登录的 UI 模块，后者涉及登录后的资料处理 UI 模块。
- 账号模块的业务逻辑可以在 `XiaoShiPin/Model` 下查看。

[](id:board)
### 主界面和列表管理
#### 模块简介
- 主界面主要负责点播列表、录制、个人资料三个一级功能的切换。
- 进入 App 后，默认展示列表界面。单击录制按钮后，如果未登录，会先跳转到登录界面；如果已经登录，将跳转到推流的界面；单击个人资料按钮，将跳转到个人资料页面。
- 列表管理包含列表的拉取和展示。

#### 相关代码
- Model：
	- TCLiveListModel(`XiaoShiPin/AppViewControllers/mainList`)：点播列表的数据层定义以及序列化/反序列化实现。
- UI：
	- TCNavigationController：定制的导航栏，主要是设置导航栏的背景颜色。
	- TCMainViewController：主界面的 tab bar 控件，用于切换列表、录制和个人资料页面。
	- TCVideoListCell：点播列表的 Cell 类，主要展示封面、标题、昵称。
	- TCLiveListViewController：点播列表的 TableViewController，负责展示点播列表，单击后跳转播放界面。

[](id:play)
### 播放模块
#### 模块简介
播放模块主要包括：短视频预加载、播放、缓存、分享等功能。

#### 相关代码
`/XiaoShiPin/AppViewControllers/VideoPlayer` 目录下，主要处理播放相关的业务逻辑，包含 UI 和业务逻辑。

[](id:record)
### 录制模块
#### 模块简介
录制模块主要包括：短视频多段录制、多段回删、多分辨率录制、变速录制等。

#### 相关代码
`UGCKit/Source/Record`在该目录下可以找到录制相关的所有逻辑。

[](id:edit)
### 编辑模块
#### 模块简介
编辑模块主要包括：短视频裁剪、BGM、滤镜风格、特效、动态贴纸、静态贴纸等。

#### 相关代码
`UGCKit/Source/Edit` 目录下可以找到编辑相关的所有逻辑。

[](id:pod)
### 发布模块
#### 模块简介
发布模块主要包括：短视频发布。

#### 相关代码
`XiaoShiPin/AppViewController/Publish` 目录下可以找到发布相关的所有逻辑。

[](id:file)
### 资料模块
#### 模块简介
- 资料模块主要负责用户资料的展示、存储和修改，并负责将这些操作同步到服务器。
- 用户资料主要包括：用户头像、昵称、性别、直播封面、定位等。 资料模块是 IMSDK 提供的功能，IMSDK 提供扩展自定义字段的功能，方便开发者自定义更加丰富的用户资料。
- 资料模块会从服务器同步用户最新资料到 App，用户可以通过资料模块来浏览自己的相关资料，包括用户头像、昵称和性别等。
- 用户可以通过资料模块修改自己的相关资料，资料模块会将这些操作同步到服务器。
- 其他模块也可以通过资料模块获取，修改用户资料。
	
#### 相关代码
`XiaoShiPin/AppViewController/AccountInfo` 目录下可以找到用户资料相关的所有逻辑。




