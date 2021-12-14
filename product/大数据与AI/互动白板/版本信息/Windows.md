### 2.6.7.233 @ 2021-10-27
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.7.233.zip)

- 新增接口
    1. 设置自定义字体(setTextFontFamily)
    2. 添加自定义字体(addTextFontFamily)
    3. 获取当前使用字体(getTextFontFamily)
    
- 调整初始化参数
    1. 画笔模式下远端画笔是否显示(remoteCursorVisible)
    
- 调整接口
    1. 设置远端画笔在本地是否可见(setRemoteCursorVisible)
    
- 调整全局变量
    1. 白板警告码(TEduBoardWarningCode)，新增静态ppt重复的告警码
    
- 功能优化
    1. 弱网环境下涂鸦同步
    2. 优化涂鸦显示效果
    3. 渲染进程残留进程处理

- Bug 修复
    若干已知问题修复
### 2.6.6.232 @ 2021-10-12
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.6.232.zip)

- 新增接口
    1. setScrollBarVisible 设置白板滚动条是否可见
    
- 调整接口
    1. getFileInfo 获取白板中指定文件的文件信息 返回fileType字段
    2. getFileInfoList 获取白板中上传的所有文件的文件信息列表 返回fileType字段
    3. addH5File 添加H5页面 支持title,needSwitch
    4. addImagesFile 批量导入图片到白板 支持title,needSwitch
    5. addVideoFile 添加视频文件 支持title,needSwitch
    
- 调整全局变量
    1. TEduBoardFileType 白板文件类型 
    
- 功能优化
    1. 涂鸦过多导致渲染卡顿
    2. 优化日志上报逻辑
    3. 增加网络探测能力
    4. 优化SDK体积
    5. Window端SDK升级CEF内核(93版本)
   
- Bug 修复
    1. 若干已知问题修复
   
### 2.6.5.224 @ 2021-09-17
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.5.224.zip)

- 新增接口
    1. 设置输出日志级别(setLogLevel)
    
- 调整全局变量
    1. 几何元素类型(TEduBoardMathGraphType)
    2. 日志级别(TEduBoardLogLevel)
 
- 当前版本废弃的接口与事件
    1. SDK接口：发起文件转码请求(applyFileTranscode)
    2. 回调事件：转码进度回调(TEB_TRANSCODEPROGRESS)
    3. 全局常量：文件转码状态(TEduBoardTranscodeFileStatus)
    
- 功能优化
    1. 几何画板新增多种几何图形支持
    
- Bug修复
    1. 若干已知问题修复
    
### 2.6.5.219 @ 2021-09-01
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.5.219.zip)


- 新增接口
    1、设置输出日志级别(setLogLevel)
    
- 调整全局变量
    1、几何元素类型(TEduBoardMathGraphType)
    2、日志级别(TEduBoardLogLevel)
 
- 当前版本废弃的接口与事件
    1、SDK接口：发起文件转码请求(applyFileTranscode)
    2、回调事件：转码进度回调(TEB_TRANSCODEPROGRESS)
    3、全局常量：文件转码状态(TEduBoardTranscodeFileStatus)
    
- 功能优化
    1、几何画板新增多种几何图形支持
    
- Bug修复
    1、若干已知问题修复

### 2.6.5.218 @ 2021-09-01
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.5.218.zip)

- 新增接口
    1、设置输出日志级别(setLogLevel)
    
- 调整全局变量
    1、几何元素类型(TEduBoardMathGraphType)
    2、日志级别(TEduBoardLogLevel)
 
- 当前版本废弃的接口与事件
    1、SDK接口：发起文件转码请求(applyFileTranscode)
    2、回调事件：转码进度回调(TEB_TRANSCODEPROGRESS)
    3、全局常量：文件转码状态(TEduBoardTranscodeFileStatus)
    
- 功能优化
    1、几何画板新增多种几何图形支持
    
- Bug修复
    1、若干已知问题修复
    
### 2.6.4.216 @ 2021-08-17
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.4.216.zip)


- 新增接口
    增加白板(addBoard)，可选择不跳转到新增的白板
    分组模式功能
        开启分组模式(setClassGroupEnable)
        设置分组(setClassGroup)
        设置分组标题(setClassGroupTitle)
        重置所有分组(resetClassGroup)
        获取所有分组id(getAllClassGroupIds)
        获取分组模式状态(getClassGroupEnable)
        获取用户所在的分组(getClassGroupIdByUserId)
        获取分组信息(getClassGroupInfoByGroupId)
        从分组中移除白板(removeBoardInClassGroup)
        从分组中移除用户(removeUserInClassGroup)
        删除分组(removeClassGroup)
        添加白板到分组(addBoardToClassGroup)
        添加用户到分组(addUserToClassGroup)
        分组内跳转(gotoClassGroupBoard)
- 其他
    功能优化
    已知问题处理
    
### 2.6.4.214 @ 2021-08-06
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.4.214.zip)


- 新增接口
    设置几何图形类型(setMathGraphType)，可用于几何画板绘制几何图形
    鼠标模式下的操作权限(setMouseToolBehavior)
    设置白板备注信息(setBoardRemark)
    获取白板备注信息(getBoardRemark)
    
- 新增初始化参数
    鼠标模式下的操作权限(mouseToolBehavior)
    开启公式元素支持(formulaEnable)
    
- 新增元素类型
    公式元素(TEDU_BOARD_ELEMENT_FORMULA)，此功能需要设置开启公式元素支持(formulaEnable)为true。

- 新增全局变量
    几何元素类型(TEduBoardMathGraphType)
    
- 功能优化
    支持涂鸦点擦
    几何画板新增多种几何图形支持
    新增公式元素的支持
    优化视频加载播放逻辑
    图形涂鸦绘制实时同步显示
    优化ppt资源加载重试逻辑
    添加本地缓存，提高资源加载速度
    
- Bug修复
    互动白板宽高变化时滚动条抖动
    删除文件时远端ppt动画步数重置
    自定义图形高度为0时远端图形显示错误
    若干已知问题修复

### 2.6.3.213 @ 2021-07-23
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.3.213.zip)

- 新增接口：
    设置鼠标工具行为(setMouseToolBehavior)
 
- 优化：
    其他已知问题及优化
    
### 2.6.3.211 @ 2021-07-05
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.3.211.zip)

- 新增接口：
    设置画笔自动拟合模式(setPenAutoFittingMode)
    
- 调整接口：
    添加白板(addBoard)
    支持新增白板直接设置背景H5

- 新增初始化参数：
    白板离线告警时间间隔(offlineWarningTimeout)
    
- 新增事件：
    白板离线告警(TEB_OFFLINE_WARNING)

- 调整事件：
    增加元素回调(TEB_ADDELEMENT)
    增加元素回调返回值新增元素类型type

- 优化：
    魔法笔功能
    支持直接创建H5背景白板
    支持白板离线检测

### 2.6.2.209 @ 2021-06-30
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.2.209.zip)


- 调整接口
   添加白板元素(addElement)
  
- 调整初始化参数：
   初始化权限参数 mathGraphEnable，预加载数学函数图像库
   初始化配置参数 scaleRange，白板缩放范围
  
- 新增事件：
   框选工具选中元素回调(TEB_SELECTED_ELEMENTS)，原有的回调事件(TEB_RECTSELECTED)弃用
   数学函数图像工具事件回调(TEB_MATH_GRAPH_EVENT)
   远端白板缩放移动状态回调(TEB_ZOOM_DRAG_STATUS)
   
- 废除接口
   废除添加图片元素(addImageElement)，请使用添加白板元素(addElement)
   
- 优化：
   支持数学函数图像显示
   支持H5元素移动、缩放、旋转
   添加元素支持自定义位置，目前支持图片元素，H5元素，数学函数图像
   移动端支持在任意工具下双指缩放白板
    
### 2.6.0. @ 2021-06-17
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.6.0..zip)

- 新增接口
    1. 新增设置代理服务器接口(SetProxyServer)
    2. 新增限制橡皮擦单次擦除图层数量接口(SetEraseLayerLimit)
    3. 新增限制橡皮擦可擦除的数据类型接口(SetEraseLayerType)
  
- 新增初始化参数
    1. proxyServer：配置代理服务器
    2. syncFps：信令同步频率

### 2.5.7.195 @ 2021-04-07
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.5.7.195.zip)

- 枚举值调整
    1. 调整 TEDU_BOARD_ERROR_PATH_INVALID 枚举值
    2. 调整 TEDU_BOARD_ERROR_WRITE_ERROR 枚举值
    3. 调整 TEDU_BOARD_WARNING_TRTC_INVALID 枚举值
    4. 新增 TEDU_BOARD_WARNING_GRAFFITI_LOST 枚举值
    5. 新增 TEDU_BOARD_WARNING_CUSTOM_GRAPH_URL_NON_EXISTS 枚举值

### 2.5.7.193 @ 2021-04-02
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.5.7.193.zip)

- 新增接口
    1. 新增设置文件缩放接口(SetFileScale)
    2. 新增获取文件缩放接口(GetFileScale)
    3. 新增限制橡皮擦单次点击擦除图层数量接口(SetEraseLayerLimit)

### 2.5.7.191 @ 2021-02-25
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.5.7.191.zip)

- Bug 修复
    1. 白板每次创建时重新注册IM消息回调，避免IM重新初始化导致收不到白板消息

### 2.5.7.187 @ 2021-02-22
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.5.7.187.zip)

- 新增接口
    1. 增加清理白板SDK环境接口(ClearTEduBoardSDKEnv)

### 2.5.7.185 @ 2021-02-02
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.5.7.185.zip)

- 新增接口
    1. 增加移动白板接口(SetScaleAnchor)
    2. 增加是否在画线过程中显示远端画笔接口(SetRemoteCursorVisible)
    3. 音频元素-设置音量大小(SetAudioVolume)
    4. 音频元素-获取音量大小(GetAudioVolume)
    5. 增加设置缩放工具的缩放比例(SetScaleToolRatio)
    6. 增加添加资源主备域名映射(AddBackupDomain)
    7. 增加删除资源主备域名映射(RemoveBackupDomain)
- 新增事件
    1. 删除元素事件(onTEBRemoveElement)
- 新增初始化参数：
    1. 增加初始化参数，关闭移动工具的缩放功能(enableScaleTool)
- 优化
    1. 添加H5PPT, 图片元素(imageElement)/图片文件(imagesFile)，背景图片，视频等资源支持指定主备Url，需要配合增加备用域名接口使用
    2. 静态PPT翻页交互效果优化
    3. 调整点选框样式
    4. 激光笔功能性能优化
- Bug 修复
    1. 图片旋转后缩放比例不对的问题
    2. chrome 88版本纵向滚动条缺失
    3. 滚动条触发异常滚动问题
    4. 添加自定义元素时点选框范围错误
    5. 文本工具相关问题
    6. 其他若干已知问题

### 2.5.6.183 @ 2021-01-27
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.5.6.183.zip)

- Bug 修复
    - 修复偶现丢失收到的笔画问题

### 2.5.6.177 @ 2020-12-16
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/sdk_bin_2.5.6.177.zip)

- 新增接口：
    1. 增加是否启用原生系统光标接口 SetSystemCursorEnable
        - 开启该功能后画笔图标和激光笔图标将使用系统的光标样式来实现，画笔图标和激光笔图标在本地会有一丢丢的流畅度提升。
        - 开启该功能后会出现画笔图标和涂鸦有一点延迟现象，属于正常现象。
        - 开启该功能 Mac 端在一些情况下会导致光标变成默认的鼠标指针，如消息弹窗等行为，属于正常现象。
    2. 增加设置画笔和激光笔工具的提示语接口 SetToolTypeTitle
    3. 支持音频元素
        - 新增音频 AddElement
        - 播放音频 PlayAudio
        - 暂停音频 PauseAudio
        - 跳转进度 SeekAudio
        - 是否启用音频控制面板 EnableAudioControl
- 新增特性：
    1. 点选和框选工具合并
    2. 激光笔和画笔支持多人
    3. 集成新的日志模块，支持日志上报，优化日志格式
- 体验优化：
    1. 选择工具,橡皮擦选中精度优化。

### 2.5.5.155 @ 2020.11.09
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.5.5.155.zip)

- 新增特性：
    - 新增文字工具预设文本内容
    - 优化白板缩放工具，支持鼠标滚轮缩放，焦点缩放，按shift键缩小交互方式
    - 新增自定义图形工具
    - 新增自定义图形的元素类型
    - 新增白板放大后显示滚动条
- Bug 修复
    - 修复偶现画笔不消失的bug

### 2.5.4.152 @ 2020.10.15
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.5.4.152.zip)

- 新增工具类型
    - 新增正圆，正方形工具类，同时支持椭圆工具和矩形工具按shift键画正圆和正方形
- 优化
    - 优化橡皮擦擦除箭头工具不精确的问题
- Bug 修复
    - 修复多端同时移动图片元素不同步的问题
    - 修复已知问题

### 2.5.3.134 @ 2020.08.31
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.5.3.134.zip)

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

### 2.5.2.132 @2020.08.07
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.5.2.132.zip)

- 新增回调
    - 新增H5PPT状态回调 onTEBH5PPTStatusChanged
    
### 2.5.1.123 @2020.07.27
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.5.1.123.zip)

- 功能支持
    - 图片元素支持任意角度旋转和八个方向的缩放
- 接口优化
    - 调用 deleteFile 接口删除非当前文件，则不跳转至默认文件 #DEFAULT
- bug fix
    - 修复文字工具在某些输入法下输入过程中，看不见已输入的文字问题
- 接口变更
    - addTranscodeFile 增加参数 needSwitch，表示添加文件后是否切换到该文件
- 内核升级
    - 升级CEF版本到83.5.0+gbf03589
    - 升级Chromium内核到83.0.4103.106

### 2.5.0.119 @2020.07.2
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.5.0.119.zip)

- 功能变更
    - addVideoFile/addTranscodeFile/addImagesFile 添加已存在文件，返回该文件 ID
    - 统一各个平台视频播放控制栏的界面
- 功能支持
    - 支持 PPT 超链接点击同步功能
- bug fix
    - 修复涂鸦过程中擦除涂鸦导致涂鸦不同步问题
    - 修复视频文件在特定场景下新增多余白板问题
- 性能优化

### 2.4.9.118 @2020.06.15
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.4.9.118.zip)

- 新增接口
    - 初始化参数新增 windowBackgroundColor 用于设置非白板区域背景色
- BUG 修复
    - AddTranscodeFile 接口超时时间改为2000毫秒缓解添加文件超时问题

### 2.4.9.115 @2020.06.10
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.4.9.115.zip)

- 新增接口
    - 新增白板同步和刷新接口 SyncAndReload
    - 新增白板快照接口 Snapshot
- 新增回调
    - 新增 onTEBSnapshot 回调
- 新增错误码
    - TEDU_BOARD_ERROR_PATH_INVALID  路径非法
    - TEDU_BOARD_ERROR_WRITE_ERROR 文件写入错误
- BUG 修复
    - 修复视频频繁操作导致权限错乱问题
    - 解决文字工具在底部点击输入无效问题
    - 修复清空偶现残留问题
    - 适配IM 4.8.10版本枚举值变化导致消息收发异常问题

### 2.4.8.108 @2020.05.21
* [单击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.4.8.108.zip)

- 新增接口
    - 新增 refresh 接口刷新当前白板
- 新增回调
    - TEduBoardImageStatus 新增 TEDU_BOARD_IMAGE_STATUS_READ_ERROR
    - 新增刷新回调 onTEBRefresh
- 功能优化
    - 视频文件 url 支持携带签名信息
    - 优化选框功能，框内点击即可移动
- BUG 修复
    - 修复视频切换进度错误问题
    - 修复激光笔闪烁问题
    - 修复激光笔跳变问题

### 2.4.7.106 @2020.04.30
* [点击下载 SDK](https://sdk.qcloudtiw.com/win32/binary_2.4.7.106.zip)

- BUG 修复
    - 修复 IM 信令每次都重复发送一条问题
- 性能优化
    - 优化房间内其他人涂鸦渲染的流程性

### 2.4.6.94 @ 2020.04.02
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
- BUG 修复
    - 修复加载相同图片没有回调问题

### 2.4.4.82 @ 2020.03.20
- BUG 修复
    - 修复传入参数含特殊符号时接口调用失败问题（单双引号及反斜杠可引发问题）
    - 修复上传文件导致白板翻页问题

### 2.4.4.78 @ 2020.03.14
- BUG 修复
    - 白板中播放视频时，学生端自动播放的问题
    - 批量导入图片组时，对 URL 字符串长度进行限制(总长7K)，超长时同步返回空串，同时回调错误 TEDU_BOARD_ERROR_DATA_TOO_LARGE
    - 去掉 onGotoBoard 多余回调，在一页 PPT 内有多个步时，只在最后一步/最前一步时才回调

### 2.4.4.73 @ 2020.03.09

- 替换内部 mp4 播放器为 videojs
- 新增接口
    - AddImagesFile 批量导入图片到白板
    - SetHandwritingEnable 开启或关闭笔锋功能
    - IsHandwritingEnable 获取白板是否开启笔锋
- 新增回调
    - onTEBAddImagesFile 增加批量图片文件回调
- 参数变更
   - TEduBoardInitParam 的 smoothLevel 默认值变更为0
- 枚举变更
    - TEduBoardErrorCode 新增 TEDU_BOARD_ERROR_AUTH_TIMEOUT 服务鉴权超时，请务必处理此错误
    - TEduBoardWarningCode 新增 TEDU_BOARD_WARNING_IMAGESFILE_ALREADY_EXISTS
    - TEDU_BOARD_VIDEO_STATUS_PLAYING 变更为 TEDU_BOARD_VIDEO_STATUS_TIMEUPDATE

### 2.4.1.64 @ 2020.01.08

- 回调变更
    - onTEBFileUploadProgress 回调参数 fileId 变更为 path
    - onTEBFileUploadStatus 回调参数 fileId 变更为 path
- 接口变更
    - addImageElement 支持添加本地图片
- 增加接口
    - 增加添加图片元素回调 onTEBAddImageElement
    
### 2.4.0.60 @2019.12.06
- 增加接口支持视频播放功能
    - 添加视频文件 virtual const char *AddVideoFile(const char *url) = 0;
    - 显示或隐藏视频控制栏 virtual void ShowVideoControl(bool show) = 0;
    - 播放视频 virtual void PlayVideo() = 0;
    - 暂停视频 virtual void PauseVideo() = 0;
    - 跳转视频 virtual void SeekVideo(double time) = 0;
    - 是否同步本地视频操作到远端 virtual void SetSyncVideoStatusEnable(bool enable) = 0;
    - 定时同步视频状态到远端 virtual void StartSyncVideoStatus(uint32_t interval) = 0;
    - 停止同步视频状态 virtual void StopSyncVideoStatus() = 0;
- 增加接口支持 H5 页面展示功能
    - 添加 H5 页面 virtual const char *AddH5File(const char *url) = 0;
- 增加接口支持图片元素功能
    - 添加图片资源 virtual void AddImageElement(const char * url) = 0;

### 2.3.5.27 @2019.10.30
- IM 兼容4.5.x版本
- 增加动画步数回调
- 增加获取课件缩略图接口
- 接口改动：
    - class TEduBoardList 改名为 class TEduBoardStringList
    - TEduBoardList::GetBoard 改名为 TEduBoardStringList::GetString

### 2.3.4.18 @2019.09.29
- 修复大文件上传 Crash 问题

### 2.3.3.48 @2019.08.15
- 支持时间戳同步机制（用于配合较大延迟的音视频方案使用）

### 2.3.2.46 @2019.08.13
- 屏蔽文件拖动事件，防止拖入文件导致页面跳转后白板无法使用问题

### 2.3.2.45 @2019.08.07
- 避免各端样式不一致，统一使用白板内置字体，删除字体设置相关接口及初始化参数
- 历史数据加载过程中禁止进行白板操作，增加非法操作枚举值
- 增加添加转码文件接口
- 增加直线样式设置接口及相应枚举值
- 增加椭圆绘制模式设置接口及相应枚举值
- 更新 CEF 及 Chromium 内核版本到76.0.3809.87

### 2.3.0.40 @2019.07.27
- 白板消息优先级调整到最高
- 修复初始化参数实验性字段为空时 crash 问题

### 2.3.0.36 @2019.07.12
- 更新 Windows&Linux 的 Chromium 版本到75.0.3770.100
- Windows&Linux 适配新版 CEF 接口
- Windows&Linux 离屏渲染模式下禁用 JS 弹窗
- Windows&Linux 增加白板 HTML 加载失败自动重试选项
- Windows&Linux 白板 HTML 文件上云

### 2.2.2.34 @2019.07.03
- 修复设置白板背景图接口功能异常

### 2.2.2.33 @2019.06.28
- 监测 Render 进程 Crash 并打印日志
- AddFile 和 AddH5PPTFile 接口同步返回文件 ID
- 文件上传进度回调和文件上传结果回调返回文件 ID 参数
- 修复某些接口参数传 nullptr 会 Crash 的问题
- 修复白板延迟显示会导致文本工具无法切换中文输入法问题

### 2.2.1.29 @2019.06.27
- 修复偶现接口调用返回 nullptr 问题

### 2.2.1.28 @2019.06.24
- 修复收不到白板初始化完成回调问题
- 添加和删除白板回调改为批量回调
- 增加是否启用 SDK 内置 Loading 图标的初始化参数

### 2.2.0.21 @ 2019.06.20
- 支持 mp4 播放
- 支持磁盘 cache 缓存

优化
 - 翻页接口增加参数，支持是否重置动画步数（prevBoard, nextBoard, gotoBoard）
 - 历史数据及资源加载增加 loading 图标
 - 白板预加载支持跨文件预加载
 - 动画 PPT 支持直接加载到指定页和指定步
 - 修复已知 bug

新增功能
 - 新增根据文件 ID 获取文件信息接口 getFileInfo
 - 错误事件新增历史数据同步失败和白板内部运行错误事件

### 2.1.0.16 @ 2019.06.12
- 支持设置日志文件路径

### 2.1.0.15 @ 2019.05.30
- 修复 onTEBFileUploadStatus 回调参数异常问题

### 2.1.0.14 @ 2019.05.29
- 支持静态 PPT 页面预加载
- 笔迹优化（铅笔工具曲线平滑）
- 支持禁止数据同步（不将本地数据同步到远端）
- 橡皮擦工具支持滑动擦除
- 添加的 H5PPT 已存在时抛出警告
- 支持独立设置每个白板宽高比
- 支持白板缩放及拖动查看

### 2.0.0.6 @ 2019.05.17
- 修复中文路径下无法初始化问题

### 2.0.0.1 @ 2019.05.15
- 新增鼠标工具类型 TEDU_BOARD_TOOL_TYPE_MOUSE
- 支持设置 H5 背景
- 白板支持并发文件上传

### 2.0.0_RC3 @ 2019.05.10
- 支持设置文本样式及字体属性
- 初始化接口支持传入所有属性初始值
- 初始化支持设置白板宽高比
- `AddFile` 接口支持传入 COS 转码 URL

### 2.0.0_RC2 @ 2019.05.08
1. 新增功能支持：
    - PPT 动画展示
2. 新增服务：
    - PPT 动画转码服务
3. 问题修复
    - 白板修复禁用 CEF 初始化后收不到回调问题

### 2.0.0_RC1 @ 2019.04.26
- 涂鸦（铅笔、橡皮、激光教鞭、直线、空心椭圆、空心矩形、实心椭圆、实心矩形、文本）
- 背景色、背景图
- 点选、框选、移动涂鸦、撤销、重做
- 白板缩放、移动
- 文件展示（静态：支持PPT、PDF、WORD、EXCEL）、多文件支持

        


