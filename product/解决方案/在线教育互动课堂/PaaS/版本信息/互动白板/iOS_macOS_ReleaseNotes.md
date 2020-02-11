# Release Notes - iOS & macOS

## 2.3.6 @ 2019.11.18

- 删除接口
    - -(NSString *)addFile:(NSString *)path
    - -(NSString *)addH5PPTFile:(NSString *)url
- 删除回调
    - -(void)onTEBAddFile:(NSString *)fileId
    - -(void)onTEBAddH5PPTFile:(NSString *)fileId
- 增加接口
    - -(void)switchFile:(NSString *)fileId boardId:(NSString *)boardId stepIndex:(NSInteger)stepIndex
    - -(void)applyFileTranscode:(NSString *)path config:(TEduBoardTranscodeConfig *)config
    - -(void)getFileTranscodeProgress:(NSString *)taskId
- 增加回调
    - -(void)onTEBFileTranscodeProgress:(TEduBoardTranscodeFileResult *)result path:(NSString *)path errorCode:(NSString *)errorCode errorMsg:(NSString *)errorMsg


## 2.3.5 @ 2019.10.30

- 新增接口getThumbnailImages获取文件缩略图
- 新增步数回调onTEBGotoStep
- 修复白板放大到一定比例，涂鸦失效问题
- 修复白板放大后精度丢失各端画面不对齐的问题

## 2.3.4 @ 2019.09.25

- 涂鸦屏蔽多指触摸
- ppt点击事件透传
- 移动端ppt翻页交互支持左右滑动翻页

## 2.3.3 @ 2019.08.19

- 增加接口
    - (uint64_t)getSyncTime支持大房间方案获取对时时间戳
    - (void)syncRemoteTime:(NSString *)userId timestamp:(uint64_t)timestamp设置远程时间戳
    
- bug修复
    - 修复getFileInfo返回错误的问题

## 2.3.2 @ 2019.08.07

- 废弃接口
    - addFile
    - addH5PPTFile
    - setTextFamily
    - getTextFamily
    - TEduBoardAuthParam.textFamily
- 废弃回调
    - onTEBAddFile
    - onTEBAddH5PPTFile
- 增加接口
    - addTranscodeFile 添加转码文件
    - setLineStyle 设置直线样式（虚线/箭头）
    - getLineStyle 获取直线样式
    - setOvalDrawMode 设置椭圆绘制模式
    - getOvalDrawMode 获取椭圆绘制模式
- 增加回调
    - onTEBAddTranscodeFile 添加转码文件回调

## 2.3.1 @ 2019.08.01
- 激光笔优化
- 修复iOS8背景图片白板涂鸦闪屏问题
- 修复iOS8背景图片和H5背景切换放大问题
- 增加html资源加载重试逻辑

## 2.3.0 @ 2019.07.18
性能优化
- 首屏渲染优化

## 2.2.2 @ 2019.07.04
接口修改
- addFile/addH5PPTFile返回文件Id
- onTEBFileUploadProgress/onTEBFileUploadStatus回调接口修改
功能更新
- 支持画出白板再画入

## 2.2.1 @ 2019.06.21
回调接口修改
- onTEBAddBoard回调boardId数组
- onTEBDeleteBoard回调boardId数组

## 2.2.0 @ 2019.06.20
新增接口
- 支持白板上下页跳转是否重置步数
- 支持获取指定文件id的文件信息
- TEduBoardErrorCode增加错误码
    - TEDU_BOARD_ERROR_TIM_HISTORYDATA  同步历史数据失败
    - TEDU_BOARD_ERROR_RUNTIME  白板运行错误

## 2.1.0 @ 2019.05.29
新增功能
- 支持静态PPT页面预加载
- 笔迹优化（铅笔工具曲线平滑）
- 支持禁止数据同步（不将本地数据同步到远端）
- 橡皮擦工具支持滑动擦除
- 添加的H5PPT已存在时抛出警告
- 支持独立设置每个白板宽高比
- 支持白板缩放及拖动查看

修复bug
- 修复macOS文本工具兼容性问题
- 修复iOS ES6兼容性问题
- 修复iOS H5PPT兼容性问题

## 2.0.0.5 @ 2019.05.24

修复bug
- 替换web board为2.0.0.2版本修复iOS h5ppt显示兼容问题


## 2.0.0.4 @ 2019.05.22

修复bug
- 修复iOS8.4白板创建没有`onTEBInit`回调的问题
- 修复iOS9.3/8.4白板创建返回Javascript错误的问题
- 修复macOS文本工具不可用问题

## 2.0.0.2 @ 2019.05.17

修复bug
- 修复iOS12.1白板创建没有`onTEBInit`回调的问题
- 调整`TEduBoardErrorCode`错误码`TEDU_BOARD_ERROR_LOAD`和`TEDU_BOARD_ERROR_AUTH`顺序


## 2.0.0.1 @ 2019.05.15

 新增功能
- 新增鼠标工具类型`TEDU_BOARD_TOOL_TYPE_MOUSE`
- 支持设置H5背景
- 白板支持并发文件上传

 bug修复
- 修复RC3版本白板数据同步失败问题




## 2.0.0_RC3 @ 2019.05.10

新增功能
- 支持设置文本样式及字体属性
- 初始化接口支持传入所有属性初始值
- 初始化支持设置白板宽高比
- `AddFile` 接口支持传入COS转码URL


## 2.0.0_RC2 @ 2019.05.08

新增功能
- macOS平台支持
- PPT动画展示

修复bug
- 拼写错误修正：TIC的`getTRTCClound`接口改名为`getTRTCCloud`


## 2.0.0_RC1 @ 2019.04.26

新增功能
- 音视频通信
    - 实时音视频通信
    - 屏幕分享/播片（可与摄像头画面并存）
- 云通信
    - 消息
    - 群组
    - 关系链管理
- 白板
    - 涂鸦（铅笔、橡皮、激光教鞭、直线、空心椭圆、空心矩形、实心椭圆、实心矩形、文本）
    - 背景色、背景图
    - 点选、框选、移动涂鸦、撤销、重做
    - 白板缩放、移动
    - 文件展示（静态：支持PPT、PDF、WORD、EXCEL）、多文件支持
