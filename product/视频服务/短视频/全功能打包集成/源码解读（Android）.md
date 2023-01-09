[](id:structure)

## 工程结构

工程共包含四个模块，[app](#app)、[ugckit](#ugckit)、[xmagickit](#xmagickit)、[beautysettingkit](#beautysettingkit)

## app[](id:app)
### 目录介绍
<img src="https://qcloudimg.tencent-cloud.cn/raw/94254bf5017089b5cfe0a2de144dd419.png" width=500>

| 文件/目录    | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| common       | 通用组件，包括各种工具类、自定义界面(美颜、播放器控件)       |
| login        | 帐号模块，包括登录以及注册                                   |
| logoff | 账号注销页面 |
| mainui       | 小视频主界面，包括主 Activity 以及视频列表                   |
| manager | 权限处理模块 |
| play         | 点播播放模块                                                 |
| userinfo     | 个人资料模块                                                 |
| videochoose | 短视频文件选择模块 |
| videoeditor  | 短视频编辑模块                                               |
| videojoiner  | 短视频合成模块                                               |
| videopublish | 短视频发布模块                                               |
| videorecord  | 短视频录制模块                                               |
| webview | 用于承载H5页面 |

[](id:function)
### 模块介绍
小视频按照功能划分成帐号、主界面、播放、短视频（编辑、合成、录制、发布），代码上也是按照这种划分进行分类，下面我们将分别介绍这些模块以及相应实现。
[](id:account)
#### 帐号模块
- 帐号模块负责处理用户登录/注册以及登录缓存的逻辑。
- 如果您已经有自己的帐号体系，可以直接替换该模块。
- 帐号模块通过调用 TCUserMgr 的 register 将用户名，密码注册到小视频的业务后台，调用 TCUserMgr 的 login 方法进行登录，并将登录信息缓存到本地 Sharepreference 中，退出登录，清空本地缓存。

**相关代码：**

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
#### 主界面和列表管理
- 主界面主要负责短视频列表、短视频拍摄/编辑和个人资料三个一级功能的切换。
- 登录成功后，默认展示列表界面；单击+号按钮后，将弹出对话框让您选择录制小视频或编辑本地小视频；单击个人资料按钮，将跳转到个人资料页面。
- 列表管理包含列表的拉取和展示。

**相关代码：**

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
#### 短视频录制模块
小视频提供录制 一分钟的 [短视频](https://cloud.tencent.com/document/product/584/9453) 功能，但 SDK 本身不显示录制时长。
**相关代码：**

| 类名                       | 描述                 |
| -------------------------- | -------------------- |
| TCVideoRecordActivity.java | 短视频录制界面       |
| RecordProgressView         | 按住拍摄短视频 View   |
| ComposeRecordBtn           | 短视频多段拍摄进度条 |

[](id:file)
#### 文件选择模块
提供本地文件选择功能，列出了手机中所有 mp4 视频文件。
**相关代码：**

| 类名                          | 描述                                                 |
| ----------------------------- | ---------------------------------------------------- |
| TCVideoChooseActivity.java    | 本地 mp4 文件选择界面                                  |
| TCVideoEditerListAdapter.java | 本地 mp4 文件列表适配器                                |
| TCVideoEditerMgr.java         | mp4 视频文件管理类，提供接口获取存储在手机中的 mp4 文件 |
| TCVideoFileInfo.java          | 本地视频数据                                         |

[](id:edit)
#### 编辑模块
[视频编辑](https://cloud.tencent.com/document/product/584/9502) 包括视频裁剪、慢动作、滤镜、音乐混音、贴纸、添加字幕等功能。

**相关代码：**
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
#### 短视频发布模块
将录制的文件发布到腾讯云视频分发平台（点播系统）中。
**相关代码：**

| 类名                          | 描述           |
| ----------------------------- | -------------- |
| TCVideoPublisherActivity.java | 短视频发布界面 |

[](id:play)
#### 短视频播放
播放已经发布到点播系统中的视频，在小视频列表页面上下滑动可快速切换上/下一个视频。

**相关代码：**

| 类名                      | 描述           |
| ------------------------- | -------------- |
| TCVodPlayerActivity.java | 短视频播放界面 |

## ugckit[](id:ugckit)
<img src="https://qcloudimg.tencent-cloud.cn/raw/be809606cec3c56ed629a05736c292aa.png" width=500>

此模块主要是对短视频 SDK 的高级封装（包含了 UI），方便快速接入。
### 目录介绍

| 文件/目录                    | 说明                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| base                         | 通用接口                                                     |
| component                    | 页面上使用的组件                                             |
| module                       | 裁剪、编辑、特效、合成、多屏合拍、录制、上传、视频选择 等模块封装，方便对应view使用 |
| utils                        | 工具类模块                                                   |
| PermissionIntroductionDialog | 权限对话框                                                   |
| UGCKit                       | ugc初始化类                                                  |
| UGCKitConstants              | 常量配置信息                                                 |
| UGCKitPicturePicker          | 图片选择模块View                                             |
| UGCKitVideoCut               | 短视频裁剪模块View                                           |
| UGCKitVideoEdit              | 短视频编辑模块View                                           |
| UGCKitVideoEffect            | 短视频特效设置模块View                                       |
| UGCKitVideoJoin              | 短视频合成模块View                                           |
| UGCKitVideoMixRecord         | 多屏录制模块View                                             |
| UGCKitVideoPicker            | 视频选择模块View                                             |
| UGCKitVideoPublish           | 上传视频模块View                                             |
| UGCKitVideoRecord            | 短视频录制模块View                                           |

## xmagickit[](id:xmagickit)
<img src="https://qcloudimg.tencent-cloud.cn/raw/5142c8534c29f9af2b43a8d2aa68d12a.png" width=500>

此模块用于快速接入腾讯特效，主要是对腾讯特效的封装，方便快速接入。

| 文件/目录  | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| config     | demo工程中的动效资源是动态下载的，用于解析动效资源的配置信息 |
| download   | 动效资源的下载模块                                           |
| module     | 腾讯特效美颜属性的创建和封装类                               |
| panel      | 美颜面板模块                                                 |
| utils      | 工具类                                                       |
| widget     | 自定义view                                                   |
| XMagicImpl | 对美颜对象的初级封装，方便使用                               |

## beautysettingkit[](id:beautysettingkit)

<img src="https://qcloudimg.tencent-cloud.cn/raw/7b3306355b0354522f0ae11f432b2184.png" width=500>

此模块是短视频中的基础美颜模块，如果客户选择使用基础美颜，则可以使用此模块进行快速集成。

| 文件/目录    | 说明               |
| ------------ | ------------------ |
| adapter      | 美颜面板UI Adapter |
| constant     | 美颜常量定义       |
| download     | 美颜下载模块       |
| model        | 美颜属性封装模块   |
| utils        | 工具类             |
| view         | 美颜面板           |
| BeautyImpl   | 使用美颜的封装类   |
| BeautyParams | 美颜参数封装类     |

