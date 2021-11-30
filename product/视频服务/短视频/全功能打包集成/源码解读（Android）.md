[](id:structure)
## 工程结构

下载小视频代码，使用 Android Studio 打开工程后，您将看到如下的目录结构：
![](https://main.qcloudimg.com/raw/7e871288732522edc565944b3324a694.png)

| 文件/目录    | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| common       | 通用组件，包括各种工具类、自定义界面(美颜、播放器控件)       |
| login        | 帐号模块，包括登录以及注册                                   |
| mainui       | 小视频主界面，包括主 Activity 以及视频列表                   |
| play         | 点播播放模块                                                 |
| userinfo     | 个人资料模块                                                 |
| videochoose | 短视频文件选择模块 |
| videoeditor  | 短视频编辑模块                                               |
| videojoiner  | 短视频合成模块                                               |
| videopublish | 短视频发布模块                                               |
| videorecord  | 短视频录制模块                                               |
| jniLibs      | 小视频依赖的腾讯相关 sdk，主要是 BuglySDK、文件上传所用的库及 LiteAVSDK |

[](id:effect)
## 动效表情

小视频源代码中默认使用的是普通版短视频 SDK，而非商用版本，所以动效贴纸等功能并不包含。如果您需要此功能，请在 [DOWNLOAD](https://cloud.tencent.com/document/product/584/9366) 中获取商用版本。

[](id:function)
## 模块介绍

小视频按照功能划分成帐号、主界面、播放、短视频（编辑、合成、录制、发布），代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。

[](id:account)
### 帐号模块

#### 模块简介

- 帐号模块负责处理用户登录/注册以及登录缓存的逻辑。
- 如果您已经有自己的帐号体系，可以直接替换该模块。
- 帐号模块通过调用 TCUserMgr 的 register 将用户名，密码注册到小视频的业务后台，调用 TCUserMgr 的 login 方法进行登录，并将登录信息缓存到本地 Sharepreference 中，退出登录，清空本地缓存。

#### 相关代码

| 类名                    | 描述                                                         |
| ----------------------- | ------------------------------------------------------------ |
| TCApplication.java      | sdk 初始化类 |
| TCLoginActivity.java    | 用户登录页面                                                 |
| TCRegisterActivity.java | 用户注册页面                                                 |
| TCUserMgr | 用户登录注册管理类 |
| ProgressFragmentUtil       | 显示进度条的控件                                        |
| TCUserInfoFragment.java     | 用户资料展示页面                                             |
| TCAboutActivity             |  小视频介绍的关于页面                                   |

[](id:board)
### 主界面和列表管理

#### 模块简介

- 主界面主要负责短视频列表、短视频拍摄/编辑和个人资料三个一级功能的切换。
- 登录成功后，默认展示列表界面；单击+号按钮后，将弹出对话框让您选择录制小视频或编辑本地小视频；单击个人资料按钮，将跳转到个人资料页面。
- 列表管理包含列表的拉取和展示。

#### 相关代码

| 类名                       | 描述                                                     |
| -------------------------- | -------------------------------------------------------- |
| TCSplashActivity.java      | 闪屏界面                                                 |
| TCMainActivity.java        | 主界面，用于呈现短视频列表，短视频拍摄/编辑，用户信息页  |
| TCLiveListMgr.java         | 列表管理类，提供接口获取本地内存列表及从服务器更新列表 |
| TCLiveListFragment.java    | 列表展示界面，负责呈现短视频的数据                       |
| TCLiveListAdapter.java     | 短视频列表适配层                                         |
| TCUGCVideoListAdapter.java | 短视频列表适配层                                         |
| TCVideoInfo            | 视频数据                                             |

[](id:record)
### 短视频录制模块

#### 模块简介

小视频提供录制 一分钟的 [短视频](https://cloud.tencent.com/document/product/584/9453) 功能，但 SDK 本身不显示录制时长。

#### 相关代码

| 类名                       | 描述                 |
| -------------------------- | -------------------- |
| TCVideoRecordActivity.java | 短视频录制界面       |
| RecordProgressView         | 按住拍摄短视频 View   |
| ComposeRecordBtn           | 短视频多段拍摄进度条 |

[](id:file)
### 文件选择模块

#### 模块简介

提供本地文件选择功能，列出了手机中所有 mp4 视频文件。

#### 相关代码

| 类名                          | 描述                                                 |
| ----------------------------- | ---------------------------------------------------- |
| TCVideoChooseActivity.java    | 本地 mp4 文件选择界面                                  |
| TCVideoEditerListAdapter.java | 本地 mp4 文件列表适配器                                |
| TCVideoEditerMgr.java         | mp4 视频文件管理类，提供接口获取存储在手机中的 mp4 文件 |
| TCVideoFileInfo.java          | 本地视频数据                                         |

[](id:edit)
### 编辑模块

#### 模块简介

[视频编辑](https://cloud.tencent.com/document/product/584/9502) 包括视频裁剪、慢动作、滤镜、音乐混音、贴纸、添加字幕等功能。

#### 相关代码

- **videoeditor/ 目录：**
<table>
<thead><tr><th>类名</th><th>描述</th></tr></thead>
<tbody><tr>
<td>TCVideoPreprocessActivity.java</td>
<td>录制后的视频进入编辑时预处理类的界面</td>
</tr><tr>
<td>TCVideoCutterActivity.java</td>
<td>短视频裁剪界面</td>
</tr><tr>
<td>TCVideoEditerActivity.java</td>
<td>短视频裁剪后编辑界面，底部有音乐，滤镜，速度，色调，贴纸，字幕等功能</td>
</tr><tr>
<td>TCVideoEffectActivity.java</td>
<td>单击底部按钮，进入短视频添加特效界面</td>
</tr><tr>
<td>BaseEditFragment.java</td>
<td>特效 Fragment 的父类，用于控制多个界面特效的播放状态</td>
</tr><tr>
<td>TCVideoJoinerActivity.java</td>
<td>当选择多个文件进行编辑时，先将多个视频文件合成一个视频界面</td>
</tr>
</tbody></table>
- **videoeditor/cutter/目录**：  视频裁剪相关。
- **videoeditor/time/ 目录**：时间特效相关，包括慢动作，重复，视频倒放。
- **videoeditor/bgm/ 目录**：背景音相关。
- **videoeditor/paster/ 目录**：贴纸相关，包括动态贴纸和静态贴纸。
- **videoeditor/motion/ 目录**：动态滤镜相关，包括四种动态滤镜（不支持自定义扩展，如需更多滤镜特效，请提交工单联系我们）。
- **videoditor/bubble/ 目录**：气泡字幕相关。
- **videoeditor/utils/ 目录**：短视频编辑工具相关。
- **videoeditor/common/目录**：短视频编辑通用组件。
- **videojoiner/目录**：短视频合成相关。


[](id:pod)
### 短视频发布模块

#### 模块简介

将录制的文件发布到腾讯云视频分发平台（点播系统）中。

#### 相关代码

| 类名                          | 描述           |
| ----------------------------- | -------------- |
| TCVideoPublisherActivity.java | 短视频发布界面 |

[](id:play)
### 短视频播放

#### 模块简介

 播放已经发布到点播系统中的视频，在小视频列表页面上下滑动可快速切换上/下一个视频。

#### 相关代码

| 类名                      | 描述           |
| ------------------------- | -------------- |
| TCVodPlayerActivity.java | 短视频播放界面 |





