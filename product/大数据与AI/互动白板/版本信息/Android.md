### 2.6.0.94 @ 2021.05.08
-  [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.6.0.94.zip)
- 重要特性：
    1. 支持最新的转码方案，具体请看[新文档转码](../开发指南/新文档转码/快速接入.md)
- 新增接口：
   1. 增加[设置单次擦除图层数量(setEraseLayerLimit)]
   2. 增加[限制橡皮擦可擦除的数据类型(setEraseLayerType)]
- 优化:  
   1. 涂鸦绘制性能优化  
   2. 激光笔移动性能优化  
   3. 激光笔多端同步效果优化  
   4. PPT、图片元素加载  
   5. 涂鸦超出白板区域时框选范围错误  
   6. 优化白板渲染时的重排、重绘操作  
- bug 修复：
   1. 截图时文本元素被 iframe 元素遮挡  
   2. 直线碰撞检测计算错误  
   3. 其他若干已知问题  

### 2.5.7.86 @ 2021.02.04
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.7.86.zip)
- 新增接口：
   1. 增加移动白板接口(setScaleAnchor)
   2. 增加是否在画线过程中显示远端画笔接口(setRemoteCursorVisible)
   3. 音频元素-设置音量大小(setAudioVolume)
   4. 音频元素-获取音量大小(getAudioVolume)
   5. 增加设置缩放工具的缩放比例(setScaleToolRatio)
   6. 增加添加资源主备域名映射(addBackupDomain)
   7. 增加删除资源主备域名映射(removeBackupDomain)  
- 新增事件:
删除元素事件  
- 新增初始化参数： 
增加初始化参数，关闭移动工具的缩放功能 enableScaleTool  
- 优化：
  1. 添加 H5 PPT, 图片元素(imageElement)/图片文件(imagesFile)，背景图片，视频等资源支持指定主备 Url，需要配合增加备用域名接口使用。
  2. 静态 PPT 翻页交互效果优化
  3. 整点选框样式
  4. 激光笔功能性能优化 Bug 修复   
- bug 修复：
  1. 图片旋转后缩放比例不对的问题
  2. Chrome 88版本纵向滚动条缺失
  3. 滚动条触发异常滚动问题
  4. 添加自定义元素时点选框范围错误
  5. 文本工具相关问题
  6. 其他若干已知问题

### 2.5.6.85 @ 2020.12.14
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.6.85.zip)
- 新增接口：
    - 增加是否启用原生系统光标接口 setSystemCursorEnable
        - 开启该功能后画笔图标和激光笔图标将使用系统的光标样式来实现，画笔图标和激光笔图标在本地会有一丢丢的流畅度提升。
        - 开启该功能后会出现画笔图标和涂鸦有一点延迟现象，属于正常现象。
        - 开启该功能 Mac 端在一些情况下会导致光标变成默认的鼠标指针，如消息弹窗等行为，属于正常现象。
    - 增加设置画笔和激光笔工具的提示语接口 setToolTypeTitle
    - 支持音频元素
        - 新增音频 addElement
        - 播放音频 playAudio
        - 暂停音频 pauseAudio
        - 跳转进度 seekAudio
        - 是否启用音频控制面板 enableAudioControl
- 新增特性：
    - 点选和框选工具合并
    - 激光笔和画笔支持多人
- 体验优化：
    - 选择工具，橡皮擦选中精度优化。

### 2.5.5.83 @ 2020.12.03 
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.5.83.zip)
- Bug 修复   
  - 修复 WebView 远程调试漏洞
  - 替换日志模块，防止内存泄漏

### 2.5.5.71 @ 2020.11.09
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.5.71.zip)
- 新增特性：
    - 新增文字工具预设文本内容 setNextTextInput
    - 优化白板缩放工具，支持鼠标滚轮缩放，焦点缩放，按 shift 键缩小交互方式
    - TEduBoardToolType 新增自定义图形工具
    - 新增 addElement 接口，支持添加自定义图形的元素
    - 新增 onTEBAddElement 回调
    - 新增白板放大后显示滚动条
- Bug 修复
    - 修复偶现画笔不消失的 bug
    
### 2.5.4.67 @ 2020.10.15
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.4.67.zip)
- 新增工具类型
    - 新增正圆，正方形工具类，同时支持椭圆工具和矩形工具按 shift 键画正圆和正方形
- 优化
    - 优化橡皮擦擦除箭头工具不精确的问题
- Bug 修复
    - 修复多端同时移动图片元素不同步的问题
    - 修复其他已知问题

### 2.5.3.61 @ 2020.08.31
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.3.61.zip)
- 新增回调
    - 新增视频状态回调 TEDU_BOARD_VIDEO_STATUS_WAITING 和 TEDU_BOARD_VIDEO_STATUS_PLAYING
- Bug 修复
    - 修复激光笔各端显示比例不一致问题
    - 修复白板操作在移动端偶现延迟问题
    - 修复涂鸦到白板外笔迹微变问题
- 优化
    - 桌面端画笔使用时持续展示
    - 视频多次播放失败后回调 ERROR 状态
    - 日志上报相关优化
    
### 2.5.2.49 @ 2020.08.18
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.2.49.zip)
- WebView 版本更新
    -Android 10及以上版本强制使用系统 WebView

### 2.5.2.48 @ 2020.08.07
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.2.48.zip)
- 新增回调
    - 新增 H5 PPT 状态回调 onTEBH5PPTStatusChanged
    
### 2.5.1.47 @ 2020.07.23
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.1.47.zip)
- 功能支持
    - 图片元素支持任意角度旋转和八个方向的缩放
- 接口优化
    - 调用 deleteFile 接口删除非当前文件，则不跳转至默认文件 #DEFAULT
- bug fix
    - 修复文字工具在某些输入法下输入过程中，看不见已输入的文字问题
    - 修复移动端文字工具在白板边界位置点击，键盘会闪一下的问题
- 接口变更
    - addTranscodeFile 增加参数 needSwitch，表示添加文件后是否切换到该文件
    
### 2.5.0.46 @ 2020.07.2
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.5.0.46.zip)
- 功能变更
    - addVideoFile/addTranscodeFile/addImagesFile 添加已存在文件，返回该文件 ID
    - 统一各个平台视频播放控制栏的界面
- 功能支持
    - 支持 PPT 超链接点击同步功能
- bug fix
    - 修复在部分 Android 手机点击点播视频无法显示视频控制栏问题
    - 修复涂鸦过程中擦除涂鸦导致涂鸦不同步问题
    - 修复视频文件在特定场景下新增多余白板问题
- 性能优化

### 2.4.9.32 @ 2020.06.10
 [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.4.9.32.zip)

- 新增接口
    - 新增白板同步和刷新接口 syncAndReload
    - 新增白板快照接口 snapshot
- 新增回调
    - 新增 onTEBSnapshot 回调
- 新增错误码
    - TEDU_BOARD_ERROR_PATH_INVALID  路径非法
    - TEDU_BOARD_ERROR_WRITE_ERROR 文件写入错误
- BUG 修复
    - 修复视频频繁操作导致权限错乱问题
    - 解决文字工具在底部点击输入无效问题
    - 修复清空偶现残留问题


### 2.4.8.31 @ 2020.05.21
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.4.8.31.zip)
- 新增接口
    - 新增 refresh 接口刷新当前白板
- 新增回调
    - TEduBoardImageStatus 新增 TEDU_BOARD_IMAGE_STATUS_READ_ERROR
    - 新增刷新回调 onTEBRefresh
- 功能优化
    - 视频文件 url 支持携带签名信息
    - 优化选框功能，框内点击即可移动
- BUG修复
    - 修复视频切换进度错误问题
    - 修复激光笔闪烁问题
    - 修复激光笔跳变问题
    
    
### 2.4.7.25 @ 2020.04.30
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.4.7.25.zip)
- 体验优化
    - 接收端涂鸦流畅性优化
- BUG 修复
    - 修复重置数据导致初始状态不正确的问题

### 2.4.6.20 @ 2020.04.02
- [单击下载 SDK](https://sdk.qcloudtiw.com/android/TEduBoardSdk_2.4.6.20.zip)
- 新增回调
    - TEduBoardImageStatus 新增三个状态回调
        - TEDU_BOARD_IMAGE_STATUS_LOAD_ABORT 图片加载中断
        - TEDU_BOARD_IMAGE_STATUS_LOAD_TIMEOUT 图片加载超时
        - TEDU_BOARD_IMAGE_STATUS_LOAD_CANCEL 图片取消加载
    - onTEBRectSelected 框选工具选中回调
- 新增接口
    - TEduBoardInitParam 新增两个参数
        - progressEnable 启用加载图标
        - progressBarUrl 自定义加载图标
        - imageTimeout 图片加载超时
- BUG修复
    - 修复加载相同图片没有回调问题

### 2.4.4.14 @ 2020.03.14
- BUG 修复
    - 白板中播放视频时，学生端自动播放的问题
    - 批量导入图片组时，对 URL 字符串长度进行限制(总长7K)，超长时同步返回空串，同时回调错误 TEDU_BOARD_ERROR_DATA_TOO_LARGE
    - 去掉 onGotoBoard 多余回调，在一页 PPT 内有多个步时，只在最后一步/最前一步时才回调

### 2.4.4.12 @ 2020.03.09

- 替换内部 mp4 播放器为 videojs
- 新增接口
    - addImagesFile 批量导入图片到白板
    - setHandwritingEnable 开启或关闭笔锋功能
    - isHandwritingEnable 获取白板是否开启笔锋
    - unInit 反初始化白板
- 新增回调
    - onTEBAddImagesFile 增加批量图片文件回调
- 参数变更
   - TEduBoardInitParam 的 smoothLevel 默认值变更为0
- 枚举变更
    - TEduBoardErrorCode 新增 TEDU_BOARD_ERROR_AUTH_TIMEOUT 服务鉴权超时，请务必处理此错误
    - TEduBoardWarningCode 新增 TEDU_BOARD_WARNING_IMAGESFILE_ALREADY_EXISTS
    - TEDU_BOARD_VIDEO_STATUS_PLAYING 变更为 TEDU_BOARD_VIDEO_STATUS_TIMEUPDATE

### 2.4.1.1 @ 2020.01.08

- 回调变更
    - onTEBFileUploadProgress 回调参数 fileId 变更为 path
    - onTEBFileUploadStatus 回调参数 fileId 变更为 path
- 接口变更
    - addImageElement 支持添加本地图片
- 增加接口
    - 增加添加图片元素回调 onTEBAddImageElement
    
### 2.4.0.286 @ 2019.12.26
- 增加接口支持视频播放功能
    - 添加视频文件  String AddVideoFile(String url);
    - 显示或隐藏视频控制栏 void ShowVideoControl(boolean show);
    - 播放视频 void PlayVideo() ;
    - 暂停视频 void PauseVideo() ;
    - 跳转视频 void SeekVideo(double time) ;
    - 是否同步本地视频操作到远端 void SetSyncVideoStatusEnable(boolean enable) ;
    - 定时同步视频状态到远端 void StartSyncVideoStatus(int interval);
    - 停止同步视频状态 void StopSyncVideoStatus() ;
- 增加接口支持 H5 页面展示功能
    - 添加 H5 页面 String AddH5File(String url) ;
- 增加接口支持图片元素功能
    - 添加图片资源 void AddImageElement(String url) ;

### 2.3.7.255 @ 2019.11.21
- 增加 setAccessibleUsers 接口，设置允许操作特定用户绘制的图形
- 增加 clearBackground 接口，删除选中涂鸦
- 增加 setCursorIcon 接口，自定义鼠标样式
    
### 2.3.6.242 @ 2019.11.14
- 增加客户端转码接口(PPT、PDF、Word 文件转码 applyFileTranscode)
- 增加客户端转码回调(onTEBFileTranscodeProgress)
- 删除添加普通和 H5 文件接口(AddFile、AddH5PPTFile); 

### 2.3.5.227 @ 2019.10.30
- 增加跳转白板页步数的回调接口(onTEBGotoStep)
- 增加获取指定文件的缩略图接口(getThumbnailImages)
- 修改白板缩放过程中会产生 Crash 的问题; 
- 修复白板放大后精度丢失各端画面不对齐的问题

### 2.3.4.192 @ 2019.09.25
- 涂鸦屏蔽多指触摸
- ppt 点击事件透传
- 移动端ppt翻页交互支持左右滑动翻页

### 2.3.3.135 @ 2019.08.19
- 白板
    - 支持大房间1000人以上、低延迟视频；

### 2.3.2.125 @ 2019.08.07
- 白板
    - 直线工具支持虚线和箭头样式；
    - 椭圆工具支持按固定起始或圆心点进行绘制；
    - 增加 addTranscodeFile 接口，用于转码文件的显示；
    - 去掉设置字体的接口
    
### 2.3.1.118 @ 2019.08.01
- 白板
    - 修复文本框选不精确问题；
    - 增加内置字体，保证各端文本输入功能采用字体一致；
    - 增加各个工具鼠标样式；
    - 激光笔交互优化；
    - 增加加载完历史数据前，禁止调用操作白板接口的保护逻辑；

### 2.3.0.109 @ 2019.07.18
- 白板
    - 首屏渲染优化;
    - 支持画出白板再画入；
    - 增加 ppt 加载 css，js 失败重试逻辑

### 2.2.2.99 @ 2019.06.30
- 白板
    - AddFile 接口同步返回 FileID;
    - onTEBFileUploadProgress 回调接口返回 FileID 和进度百分比；
    - onTEBFileUploadStatus 回调接口返回 FileID 和错误码

### 2.2.0 @ 2019.06.20
- 白板
    - 支持白板上下页跳转是否重置步数
    - 支持获取指定文件 id 的文件信息
    - TEduBoardErrorCode 增加错误码
    - TEDU_BOARD_ERROR_TIM_HISTORYDATA 同步历史数据失败
    - TEDU_BOARD_ERROR_RUNTIME 白板运行错误

### 2.1.0 @ 2019.05.29
- 白板
    - 支持图片预加载功能；
    - 支持是否将涂鸭数据同步给其他端功能；
    - 优化涂鸭笔迹去锯齿，让线条变得更平滑；
    - 优化橡皮擦工具，支持滑动擦除;
    - 优化 H5ppt 错误提示，在 H5ppt 文件已经存在的情况下抛出警告;
    - 优化文档展示，支持独立设置白板宽高比，支持滑动缩放;；

### 2.0.0.2 @ 2019.05.22
- 白板
    - 修改 BUG；

### 2.0.0.1 @ 2019.05.15

1. 新增功能支持：
    - 白板
        - 新增使用网页作为白板的背景；
        - 新增工具鼠标的功能，可以方便的手势翻页；
2. 问题修复
    - 修正 Demo 中白板的构建方式，移到 TIC SDK 中统一初始和反初始化；

### 2.0.0_RC3 @ 2019.05.10

1. 新增功能支持：
    - 白板
        - 支持设置文本样式及字体属性
        - 初始化接口支持传入所有属性初始值
        - 初始化支持设置白板宽高比
        - `AddFile` 接口支持传入 COS 转码 URL
2. 问题修复
    - Demo 依赖的 IM 版本指定为4.3.81，修复最新版 IM 修改接口导致编译异常问题


### 2.0.0_RC2 @ 2019.05.08

1. 新增功能支持：
    - 白板
        - PPT 动画展示
3. 新增服务：
    - PPT 动画转码服务


### 2.0.0_RC1 @ 2019.04.26

1. 新增功能支持：
    - 音视频通信
        - 实时音视频通信
        - 屏幕分享/播片（可与摄像头画面并存）
    - 即时通信 IM
        - 消息
        - 群组
        - 关系链管理
    - 白板
        - 涂鸦（铅笔、橡皮、激光教鞭、直线、空心椭圆、空心矩形、实心椭圆、实心矩形、文本）
        - 背景色、背景图
        - 点选、框选、移动涂鸦、撤销、重做
        - 白板缩放、移动
        - 文件展示（静态：支持 PPT、PDF、WORD、EXCEL）、多文件支持
