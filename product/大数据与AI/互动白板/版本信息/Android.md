### 2.4.6.20 @ 2020.04.02
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
1. 白板
    - 支持大房间1000人以上、低延迟视频；

### 2.3.2.125 @ 2019.08.07
1. 白板
    - 直线工具支持虚线和箭头样式；
    - 椭圆工具支持按固定起始或圆心点进行绘制；
    - 增加 addTranscodeFile 接口，用于转码文件的显示；
    - 去掉设置字体的接口
    
### 2.3.1.118 @ 2019.08.01
1. 白板
    - 修复文本框选不精确问题；
    - 增加内置字体，保证各端文本输入功能采用字体一致；
    - 增加各个工具鼠标样式；
    - 激光笔交互优化；
    - 增加加载完历史数据前，禁止调用操作白板接口的保护逻辑；

### 2.3.0.109 @ 2019.07.18
1. 白板
    - 首屏渲染优化;
    - 支持画出白板再画入；
    - 增加 ppt 加载 css，js 失败重试逻辑

### 2.2.2.99 @ 2019.06.30
1. 白板
    - AddFile 接口同步返回 FileID;
    - onTEBFileUploadProgress 回调接口返回 FileID 和进度百分比；
    - onTEBFileUploadStatus 回调接口返回 FileID 和错误码

### 2.2.0 @ 2019.06.20
1. 白板
    - 支持白板上下页跳转是否重置步数
    - 支持获取指定文件 id 的文件信息
    - TEduBoardErrorCode 增加错误码
    - TEDU_BOARD_ERROR_TIM_HISTORYDATA 同步历史数据失败
    - TEDU_BOARD_ERROR_RUNTIME 白板运行错误

### 2.1.0 @ 2019.05.29
1. 白板
    - 支持图片预加载功能；
    - 支持是否将涂鸭数据同步给其他端功能；
    - 优化涂鸭笔迹去锯齿，让线条变得更平滑；
    - 优化橡皮擦工具，支持滑动擦除;
    - 优化 H5ppt 错误提示，在 H5ppt 文件已经存在的情况下抛出警告;
    - 优化文档展示，支持独立设置白板宽高比，支持滑动缩放;；

### 2.0.0.2 @ 2019.05.22
1. 白板
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
