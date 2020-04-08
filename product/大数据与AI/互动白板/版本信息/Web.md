### 2.4.6 @ 2020.04.02

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

- 接口变更
    - addImageElement 支持添加本地图片
- 增加接口
    - 增加添加图片元素回调 onTEBAddImageElement

### 2.4.0 @ 2019.12.06

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
        - PPT动画展示
