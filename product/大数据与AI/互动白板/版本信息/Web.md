### 2.6.7 @ 2021.10.26
* 链接地址：https://res.qcloudtiw.com/board/2.6.7/TEduBoard.min.js
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
- Bug 修复
  1. 若干已知问题修复

### 2.6.6 @ 2021.09.28
* 链接地址：https://res.qcloudtiw.com/board/2.6.6/TEduBoard.min.js
- 新增接口
	1. 设置白板滚动条是否可见(setScrollBarVisible)
- 调整接口
	1. 获取白板中指定文件的文件信息(getFileInfo)
	2. 获取白板中上传的所有文件的文件信息列表(getFileInfoList)
	3. 添加 H5 页面(addH5File)
	4. 批量导入图片到白板(addImagesFile)
	5. 添加视频文件(addVideoFile)
- 调整全局变量
	1. 白板文件类型(TEduBoardFileType)
- 功能优化
	1. 涂鸦过多导致渲染卡顿
	2. 优化日志上报逻辑
	3. 增加网络探测能力
	4. 优化SDK体积
	5. Window端SDK升级CEF内核
- Bug 修复
	1. 若干已知问题修复
### 2.6.5 @ 2021.08.24
* 链接地址：https://res.qcloudtiw.com/board/2.6.5/TEduBoard.min.js
- 新增接口
	1. 设置输出日志级别(setLogLevel)
- 调整全局变量
	1. 几何元素类型(TEduBoardMathGraphType)
	2. 日志级别(TEduBoardLogLevel)
- 废弃的接口与事件
	1. SDK接口：发起文件转码请求(applyFileTranscode)
	2. 回调事件：转码进度回调(TEB_TRANSCODEPROGRESS)
	3. 全局常量：文件转码状态(TEduBoardTranscodeFileStatus)
- 功能优化
	1. 几何画板新增多种几何图形支持
- Bug 修复
	1. 若干已知问题修复

### 2.6.4 @ 2021.08.16
* 链接地址：https://res.qcloudtiw.com/board/2.6.4/TEduBoard.min.js
- 新增分组模式
  1. 添加白板到分组  addBoardToClassGroup
  2. 添加用户到分组 addUserToClassGroup
  3. 获取所有分组id getAllClassGroupIds
  4. 获取分组模式状态 getClassGroupEnable
  5. 获取用户所在的分组 getClassGroupIdByUserId
  6. 获取分组信息 getClassGroupInfoByGroupId
  7. 分组内跳转 gotoClassGroupBoard
  8. 从分组中移除白板 removeBoardInClassGroup
  9. 删除分组 removeClassGroup
  10. 从分组中移除用户 removeUserInClassGroup
  11. 重置所有分组 resetClassGroup
  12. 设置分组 setClassGroup
  13. 开启分组模式 setClassGroupEnable
  14. 设置分组标题 setClassGroupTitle

### 2.6.4 @ 2021.08.06
* 链接地址：https://res.qcloudtiw.com/board/2.6.4/TEduBoard.min.js
- 新增接口
  1. 设置几何图形类型 setMathGraphType，可用于几何画板绘制几何图形
  2. 鼠标模式下的操作权限 setMouseToolBehavior
  3. 设置白板备注信息 setBoardRemark
  4. 获取白板备注信息 getBoardRemark

- 新增初始化参数
  1. 鼠标模式下的操作权限
  2. 开启公式元素支持

- 新增元素类型
  1. 公式元素 TEDU_BOARD_ELEMENT_FORMULA，此功能需要设置开启公式元素支持 formulaEnable 为`true`。添加方式详见 添加白板元素中的 `示例8：添加一个公式元素`

- 新增全局变量
  1. 几何元素类型

- 功能优化
  1. 支持涂鸦点擦
  2. 几何画板新增多种几何图形支持
  3. 新增公式元素的支持
  4. 优化视频加载播放逻辑
  5. 图形涂鸦绘制实时同步显示
  6. 优化 ppt 资源加载重试逻辑

- Bug 修复
  1. 互动白板宽高变化时滚动条抖动
  2. 删除文件时远端 ppt 动画步数重置
  3. 自定义图形高度为0时远端图形显示错误
  4. 若干已知问题修复

### 2.6.3 @ 2021.06.28
* 链接地址：https://res.qcloudtiw.com/board/2.6.3/TEduBoard.min.js
- 新增接口：
    1. 设置画笔自动拟合模式 setPenAutoFittingMode
    2. 生成板书图片 addSnapshotMark
- 调整接口：
    1. 添加白板 addBoard（支持新增白板直接设置背景 H5）
- 新增初始化参数：
    1. 白板离线告警时间间隔 offlineWarningTimeout
- 新增事件：
    1. 白板离线告警 TEB_OFFLINE_WARNING
- 调整事件：
    1. 增加元素回调 TEB_ADDELEMENT（增加元素回调返回值新增元素类型 type）
- 优化：
    1. 魔法笔功能
    2. 支持直接创建 H5 背景白板
    3. 支持白板离线检测
    4. 支持生成板书
- Bug 修复
    1. 若干已知问题

### 2.6.2 @ 2021.06.09
* 链接地址：https://res.qcloudtiw.com/board/2.6.2/TEduBoard.min.js
- 调整接口：
    1. 添加白板元素 addElement
- 调整初始化参数：
    1. 初始化权限参数 mathGraphEnable，预加载数学函数图像库
    2. 初始化配置参数 scaleRange，白板缩放范围
- 新增事件：
    1. 框选工具选中元素回调 TEB_SELECTED_ELEMENTS，原有的回调事件 TEB_RECTSELECTED 弃用
    2. 数学函数图像工具事件回调 TEB_MATH_GRAPH_EVENT
    2. 远端白板缩放移动状态回调 TEB_ZOOM_DRAG_STATUS
- 废除接口
    1. 废除添加图片元素 addImageElement，请使用添加白板元素 addElement
- 优化：
    1. 支持数学函数图像显示
    2. 支持 H5 元素移动、缩放、旋转
    3. 添加元素支持自定义位置，目前支持图片元素，H5 元素，数学函数图像
    4. 移动端支持在任意工具下双指缩放白板
- Bug 修复
    1. 若干已知问题

### 2.6.1 @ 2021.06.01
* 链接地址：https://res.qcloudtiw.com/board/2.6.1/TEduBoard.min.js
- 调整接口：
    1. 设置工具的提示语 setToolTypeTitle
    2. 设置允许操作哪些用户绘制的图形 setAccessibleUsers
    2. 设置用户信息 setUserInfo
- 调整初始化参数：
    1. 优化初始化参数结构
- 新增事件：
    1. 文本组件状态回调 TEB_TEXT_ELEMENT_STATUS_CHANGED
    2. 图片元素加载状态 TEB_IMAGE_ELEMENT_STATUS_CHANGED
    3. 白板文字工具异常警告 TEB_TEXT_ELEMENT_WARNING
- 优化：
    1. 涂鸦支持缩放旋转
    2. 文本支持等比例缩放
    3. 优化用户权限控制
    4. 支持显示远端操作元素
    5. 支持显示白板元素操作者或创造者信息
    6. 支持自动隐藏静止的远端画笔
    7. 优化低版本背景图显示
- Bug 修复
    1. 若干已知问题

### 2.6.0 @ 2021.05.07
* 链接地址：https://res.qcloudtiw.com/board/2.6.0/TEduBoard.min.js
- 重要特性：
    1. 支持最新的转码方案，具体请看[新文档转码](https://cloud.tencent.com/document/product/1137/55888)

- 新增接口：
    1. 增加设置代理服务器(setProxyServer)
    2. 增加设置单次擦除图层数量(setEraseLayerLimit)
    3. 增加限制橡皮擦可擦除的数据类型(setEraseLayerType)
- 新增初始化参数：
    1. 增加初始化参数，代理服务器配置 proxyServer
- 优化：
    1. 涂鸦绘制性能优化
    2. 涂鸦旋转移动性能优化
    3. 激光笔移动性能优化
    4. 激光笔多端同步效果优化
    5. PPT、图片元素加载
    6. 涂鸦超出白板区域时框选范围错误
    7. 优化白板渲染时的重排、重绘操作
- Bug 修复
    1. 截图时文本元素被 iframe 元素遮挡
    2. 直线碰撞检测计算错误
    3. 其他若干已知问题

### 2.5.7 @ 2021.02.02
* 链接地址：https://res.qcloudtiw.com/board/2.5.7/TEduBoard.min.js

- 新增接口：
    1. 增加移动白板接口(setScaleAnchor)
    2. 增加是否在画线过程中显示远端画笔接口(setRemoteCursorVisible)
    3. 音频元素-设置音量大小(setAudioVolume)
    4. 音频元素-获取音量大小(getAudioVolume)
    5. 增加设置缩放工具的缩放比例(setScaleToolRatio)
    6. 增加添加资源主备域名映射(addBackupDomain)
    7. 增加删除资源主备域名映射(removeBackupDomain)
    8. 增加是否同步本地音频操作状态到远端(setSyncAudioStatusEnable)
    9. 增加删除白板元素接口(removeElement)
- 新增事件：
    1. 删除元素事件(TEB_REMOVEELEMENT)
- 新增初始化参数：
    1. 增加初始化参数，关闭移动工具的缩放功能 enableScaleTool
- 优化：
    1. 添加H5PPT, 图片元素(imageElement)/图片文件(imagesFile)，背景图片，视频等资源支持指定主备Url，需要配合增加备用域名接口使用。
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

### 2.5.6 @ 2020.12.14
* 链接地址：https://res.qcloudtiw.com/board/2.5.6/TEduBoard.min.js
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

### 2.5.5 @ 2020.11.05
* 链接地址：https://res.qcloudtiw.com/board/2.5.5/TEduBoard.min.js

- 新增特性：
    - 新增文字工具预设文本内容 setNextTextInput
    - 优化白板缩放移动工具，支持鼠标滚轮缩放，焦点缩放，按 shift 键缩小等
    - 新增白板缩放工具图标 setZoomCursorIcon
    - TEduBoardToolType 新增自定义图形工具
    - TEduBoardElementType 新增自定义图形的元素类型
    - 新增白板放大后显示滚动条
- Bug 修复
    - Mac 端鼠标缓慢移除白板左边缘和上边缘，鼠标指针不隐藏的 bug
    - 修复偶现画笔不消失的 bug

- 缩放移动工具使用说明：
    
    ![](https://main.qcloudimg.com/raw/4b467dd838aaac65aa66d26a4c55572f.png)

### 2.5.4 @ 2020.10.15
* 链接地址：https://res.qcloudtiw.com/board/2.5.4/TEduBoard.min.js

- 新增工具类型
    - 新增正圆，正方形工具类，同时支持椭圆工具和矩形工具按 shift 键画正圆和正方形
- 优化
    - 优化橡皮擦擦除箭头工具不精确的问题
- Bug 修复
    - 修复多端同时移动图片元素不同步的问题。
    - 修复已知问题。


### 2.5.3 @ 2020.08.31
* 链接地址：https://res.qcloudtiw.com/board/2.5.3/TEduBoard.min.js

- 新增回调
    - 新增视频状态回调 TEDU_BOARD_VIDEO_STATUS_WAITING 和 TEDU_BOARD_VIDEO_STATUS_PLAYING
- Bug 修复
    - 修复激光笔各端显示比例不一致问题
    - 修复白板操作在移动端偶现延迟问题
    - 修复涂鸦到白板外笔迹微变问题
- 优化
    - 桌面端画笔使用时持续展示
    - 视频多次播放失败后回调 ERROR 状态
    
### 2.5.2 @ 2020.08.07
* 链接地址：https://res.qcloudtiw.com/board/2.5.2/TEduBoard.min.js

- 新增回调
    - 新增 H5PPT 状态回调 TEB_H5PPT_STATUS_CHANGED
    
### 2.5.1 @ 2020.07.23
* 链接地址：https://res.qcloudtiw.com/board/2.5.1/TEduBoard.min.js

- 功能支持
    - 图片元素支持任意角度旋转和八个方向的缩放
- 接口优化
    - 如果 getFileBoardList，getFileInfo 接口 fid 参数缺省，则默认返回当前文件文件的信息
    - 调用 deleteFile 接口删除非当前文件，则不跳转至默认文件#DEFAULT
- bug fix
    - 修复文字工具在某些输入法下输入过程中，看不见已输入的文字问题
    - 修复移动端文字工具在白板边界位置点击，键盘会闪一下的问题


### 2.5.0 @ 2020.07.2
* 链接地址：https://res.qcloudtiw.com/board/2.5.0/TEduBoard.min.js

- 功能变更
    - addVideoFile/addTranscodeFile/addImagesFile 添加已存在文件，返回该文件 ID
    - 统一各个平台视频播放控制栏的界面
- 功能支持
    - 支持 PPT 超链接点击同步功能
- bug fix
    - 修复涂鸦过程中擦除涂鸦导致涂鸦不同步问题
    - 修复视频文件在特定场景下新增多余白板问题
- 性能优化


### 2.4.9 @ 2020.06.10
* 链接地址：https://res.qcloudtiw.com/board/2.4.9/TEduBoard.min.js

- 新增接口
    - 新增白板同步和刷新接口 syncAndReload
    - 新增白板快照接口 snapshot
- 新增回调
    - 新增截图回调
    ```
    teduBoard.on(TEduBoard.EVENT.TEB_SNAPSHOT, ({image, userData}) => {
        //image 为 base64格式图片， userdata 为透传字段
    });
    ```
- BUG 修复
    - 修复视频频繁操作导致权限错乱问题
    - 解决文字工具在底部点击输入无效问题
    - 修复清空偶现残留问题

### 2.4.8 @ 2020.05.21
* 链接地址：https://res.qcloudtiw.com/board/2.4.8/TEduBoard.min.js

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

### 2.4.7 @2020.04.30
* 链接地址：https://res.qcloudtiw.com/board/2.4.7/TEduBoard.min.js

- BUG 修复
    - 修复 IM 信令每次都重复发送一条问题
- 性能优化
    - 优化房间内其他人涂鸦渲染的流程性

### 2.4.6 @ 2020.04.02
* 链接地址：https://res.qcloudtiw.com/board/2.4.6/TEduBoard.min.js

- 新增回调
    - TEduBoardImageStatus 新增两个状态回调
        - TEDU_BOARD_IMAGE_STATUS_LOAD_TIMEOUT 图片加载超时
        - TEDU_BOARD_IMAGE_STATUS_LOAD_CANCEL 图片取消加载
    - onTEBRectSelected 框选工具选中回调
- 新增参数
    - progressBarUrl 自定义加载图标
    - imageTimeout 图片加载超时
- BUG 修复
    - 修复加载相同图片没有回调问题

### 2.4.4 @ 2020.03.14
* 链接地址：https://res.qcloudtiw.com/board/2.4.4/TEduBoard.min.js
- 批量导入图片组时，对 URL 字符串长度进行限制(总长7K)，超长时同步返回空串，同时回调错误 TEDU_BOARD_ERROR_DATA_TOO_LARGE
- 替换内部 mp4 播放器为 videojs
- 新增接口
    - addImagesFile 批量导入图片到白板
    - setHandwritingEnable 开启或关闭笔锋功能
    - isHandwritingEnable 获取白板是否开启笔锋
- 新增回调
    - TEB_ADDIMAGESFILE 增加批量图片文件回调
- 参数变更
   - TEduBoard初始化参数 smoothLevel 默认值变更为0
- 枚举变更
    - TEB_ERROR 新增 TEDU_BOARD_ERROR_AUTH_TIMEOUT 服务鉴权超时，请务必处理此错误
    - TEB_WARNING 新增 TEDU_BOARD_WARNING_IMAGESFILE_ALREADY_EXISTS
    - TEDU_BOARD_VIDEO_STATUS_PLAYING 变更为 TEDU_BOARD_VIDEO_STATUS_TIMEUPDATE
    
### 2.4.1 @ 2020.01.08
* 链接地址：https://res.qcloudtiw.com/board/2.4.1/TEduBoard.min.js
- 接口变更
    - addImageElement 支持添加本地图片
- 增加接口
    - 增加添加图片元素回调 onTEBAddImageElement

### 2.4.0 @ 2019.12.06
* 链接地址：https://res.qcloudtiw.com/board/2.4.0/TEduBoard.min.js
- 增加接口
    - 添加视频文件 addVideoFile
    - 显示或隐藏视频控制栏 showVideoControl
    - 播放视频 playVideo
    - 暂停视频 pauseVideo
    - 跳转 seekVideo
    - 是否同步本地视频操作到远端 setSyncVideoStatusEnable
    - 定时同步视频状态到远端 startSyncVideoStatus
    - 停止同步视频状态 stopSyncVideoStatus
    - 添加 H5 页面 addH5File
    - 添加图片资源 addImageElement

### 2.3.7 @ 2019.11.21

- 增加接口
    - setAccessibleUsers 设置允许操作特定用户绘制的图形
    - clearBackground 删除选中涂鸦
    - setCursorIcon 自定义鼠标样式

### 2.3.6 @ 2019.11.12

- 转码资源全部接入 CDN，请务必升级。
- 废弃 addFile，addH5PPTFile 接口，废弃 TEB_ADDFILE，TEB_ADDH5PPTFILE 事件。
- 新增 applyFileTranscode，getFileTranscodeProgress，新增 TEB_TRANSCODEPROGRESS 事件。
- 切换文件支持切换到指定页和指定步


### 2.3.5 @ 2019.10.30
* 链接地址：https://res.qcloudtiw.com/board/2.3.5/TEduBoard.min.js
- 新增接口 getThumbnailImages 获取文件缩略图
- 新增步数回调 TEB_GOTOSTEP
- 修复白板放大到一定比例，涂鸦失效问题
- 修复白板放大后精度丢失各端画面不对齐的问题

### 2.3.4 @ 2019.09.25

- 涂鸦屏蔽多指触摸
- ppt 点击事件透传
- 移动端 ppt 翻页交互支持左右滑动翻页

### 2.3.3 @ 2019.08.07
1. 白板
    - 增加资源文件失败上报
    - 支持大班课

### 2.3.2 @ 2019.08.07
1. 白板
    - 直线支持设置样式，包括实线，虚线，箭头
    - 圆和椭圆支持固定圆心
    - 新增 addTranscodeFile 接口支持 restapi 转码结果
    - 废弃 setTextFontFamily（设置文字输入字体）和 getTextFontFamily（获取文字输入字体）接口

### 2.3.1 @ 2019.08.01
1. 白板
    - 修复文本框选不精确问题；
    - 增加内置字体，保证各端文本输入功能采用字体一致；
    - 增加各个工具鼠标样式；
    - 激光笔交互优化；
    - 增加加载完历史数据前，禁止调用操作白板接口的保护逻辑；

### 2.3.0 @ 2019.07.18
1. 白板
    - 首屏渲染优化;
    - 支持画出白板再画入；
    - 增加 ppt 加载 css,js 失败重试逻辑
    - 添加文件和 PPT 动画接口同步返回文件 ID

### 2.2.1 @ 2019.06.21

优化
 - 新增白板回调事件和删除白板回调事件，白板 ID 参数修改为数组

### 2.2.0 @ 2019.06.20

优化
 - 翻页接口增加参数，支持是否重置动画步数（prevBoard, nextBoard, gotoBoard）
 - 历史数据及资源加载增加 loading 图标(progressEnable)
 - 白板预加载支持跨文件预加载
 - 动画 PPT 支持直接加载到指定页和指定步
 - 修复已知 bug

新增功能
 - 新增根据文件 ID 获取文件信息接口 getFileInfo
 - 错误事件新增历史数据同步失败和白板内部运行错误事件


### 2.1.0 @ 2019.05.29
新增功能
- 支持预加载，白板初始化增加参数：preloadDepth 用于指定图片预加载深度，默认值为5（表示预加载当前页前后5页的图片）
- 笔迹优化，白板初始化增加参数：smoothLevel 用于指定笔迹平滑级别，默认值0.1，取值[0, 1]
- 支持禁止数据同步，白板初始化增加参数：dataSyncEnable 用于指定是否启用数据同步，同时增加对应的接口 setDataSyncEnable、isDataSyncEnable
- 橡皮擦工具支持滑动擦除，没有接口变更
- TEduBoardWarningCode 新增一个 TEDU_BOARD_WARNING_H5PPT_ALREADY_EXISTS = 3的枚举值，当要添加的 H5PPT 已存在时抛出该警告
- 文档展示优化，支持独立设置白板宽高比，支持滑动缩放


| 新增初始化参数	| 类型	| 必填 | 默认值 |说明
--------- | --------- | ----- | --------- | --------- |
| boardContentFitMode | Number | 否 | 0 | 0 不自动调整白板宽高比，文件等比例缩放居中显示，文件宽高<=白板宽高<br/> 1 自动调整白板宽高比与文件一致，文件铺满白板，白板等比例缩放居中显示，白板宽高<=容器宽高<br/> 2 自动调整白板宽高比与文件一致，文件铺满白板，白板等比例缩放居中显示，白板宽高>=容器宽高 |
| dataSyncEnable | Boolean | 否 | true | 是否数据同步 |
| scale | Number | 否 | 100 | 实际缩放比为scale/100 |
| preloadDepth | Number | 否 | 5 | 预加载深度，预加载前后 preloadDepth 页白板 |
| smoothLevel | Number | 否 | 0.1 | 平滑级别，取值0～1之间的浮点数，0表示不启用平滑 |



| 新增接口          | 说明      |
| ------------------ | ---------------------------------------- |
| setBoardRatio                            |          设置当前的白板比例                           |
| getBoardRatio                            |          获取当前的白板比例                           |
| setBoardScale                                  |          设置当前的白板缩放比                           |
| getBoardScale                            |          获取当前的白板缩放比                           |
| setDataSyncEnable                            |          设置是否同步数据                           |
| isDataSyncEnable                            |          获取是否允许同步数据                           |
| setBoardContentFitMode                            |          设置白板文件的显示方式                           |
| getBoardContentFitMode                            |          获取白板文件的显示方式                           |

### 2.0.0.2 @ 2019.05.22

1. bug 修复
    - 文字输入在 mac 中的兼容性问题
    - 修复PPT动画在 iPhone 显示异常的问题

### 2.0.0.1 @ 2019.05.15

1. 新增功能支持：
    - 白板
        - 新增鼠标工具类型 TEDU_BOARD_TOOL_TYPE_MOUSE
        - 支持设置 H5 背景
        - 白板支持并发文件上传
2. bug 修复
    - 新增白板有边框


### 2.0.0_RC3 @ 2019.05.10

1. 新增功能支持：
    - 白板
        - 支持设置文本样式及字体属性
        - 初始化接口支持传入所有属性初始值
        - 初始化支持设置白板宽高比
        - `AddFile` 接口支持传入 COS 转码 URL


### 2.0.0_RC2 @ 2019.05.08

1. 新增功能支持：
    - 白板
        - 涂鸦（铅笔、橡皮、激光教鞭、直线、空心椭圆、空心矩形、实心椭圆、实心矩形、文本）
        - 背景色、背景图
        - 点选、框选、移动涂鸦、撤销、重做
        - 白板缩放、移动
        - 文件展示（静态：支持PPT、PDF、WORD、EXCEL）、多文件支持
        - PPT 动画展示



