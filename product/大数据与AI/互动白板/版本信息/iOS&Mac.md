### 2.6.8.87 @ 2021-12-10
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.8.87.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.8.87.zip)

- 新增接口
    1.跳转到指定动画步数(gotoStep)
    2.获取白板滚动位置(getBoardScroll) 
    3.设置分段擦除模式是否开启(setPiecewiseErasureEnable)
    4.获取分段擦除模式开启状态(isPiecewiseErasureEnable)
    5.设置橡皮擦大小(setEraserSize)
    6.获取橡皮擦大小(getEraserSize)
    7.设置全局背景图(setGlobalBackgroundPic)
    8.获取全局背景图(getGlobalBackgroundPic)
  
- 调整接口
    1. 添加白板元素(addTextElement) 支持添加文本元素

- 新增事件
    1. 白板移动回调(onTEBBoardScrollChanged)

- 调整事件
    1. 框选工具选中元素回调(onTEBSelectedElements) 新增元素位置、宽高、包围盒大小等返回字段

- 新增初始化参数
    1. 全局背景图(globalBackgroundPic)

- 功能优化
    1. 优化图片资源加载逻辑
    2. 添加图片元素在低版本上进行旋转校正
    3. 添加图片元素支持自定义大小
    4. 支持画线涂鸦分段擦除

- Bug 修复
    1. 在不同缩放比下添加白板元素大小显示不一致
    2. 若干已知问题修复

### 2.6.7.84 @ 2021-11-04
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.7.84.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.7.84.zip)

- Bug 修复
  1.Mac SDK 在低版本系统中加载白板自定义协议出现的询问弹窗

### 2.6.7.82 @ 2021-10-29
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.7.82.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.7.82.zip)

- 新增接口
  1.设置自定义字体(setTextFontFamily)
  2.添加自定义字体(addTextFontFamily) 
  3.获取当前使用字体(getTextFontFamily)
    
- 调整初始化参数
  1.画笔模式下远端画笔是否显示(remoteCursorVisible) 
    
- 调整接口
  1.设置远端画笔在本地是否可见(setRemoteCursorVisible)
    
- 调整全局变量
  1.白板警告码(TEduBoardWarningCode)，新增静态ppt重复的告警码
    
- 功能优化
  1.弱网环境下涂鸦同步
  2.优化涂鸦显示效果

- Bug 修复
  1.若干已知问题修复

### 2.6.6.78 @ 2021-10-12
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.6.78.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.6.78.zip)

- 新增接口  
  1. 设置白板滚动条是否可见(setScrollBarVisible)    
- 接口调整  
  1. addImagesFile(urls, title, needSwitch) 支持title,needSwitch
  2. addH5File(url, title, needSwitch) 支持title,needSwitch
  3. addVideoFile(url, title, needSwitch) 支持title,needSwitch
- 实体类调整  
  1. TEduBoardFileInfo，新增fileType字段

### 2.6.5.75 @ 2021-09-01
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.5.75.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.5.75.zip)

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
- Bug 修复  
  1. 若干已知问题修复  

### 2.6.4.69 @ 2021-08-25
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.4.66.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.4.66.zip)

Bug 修复
解决互动白板加载 h5 课件加载异常的问题

### 2.6.4.61 @ 2021-08-16
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.4.61.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.4.61.zip)

- 新增接口
    1. 增加白板(addBoard)，可选择不跳转到新增的白板
    2. 分组模式功能
        1. 开启分组模式(setClassGroupEnable)
        2. 设置分组(setClassGroup)
        3. 设置分组标题(setClassGroupTitle)
        4. 重置所有分组(resetClassGroup)
        5. 获取所有分组ID(getAllClassGroupIds)
        6. 获取分组模式状态(getClassGroupEnable)
        7. 获取用户所在的分组(getClassGroupIdByUserId)
        8. 获取分组信息(getClassGroupInfoByGroupId)
        9. 从分组中移除白板(removeBoardInClassGroup)
        10. 从分组中移除用户(removeUserInClassGroup)
        11. 删除分组(removeClassGroup)
        12. 添加白板到分组(addBoardToClassGroup)
        13. 添加用户到分组(addUserToClassGroup)
        14. 分组内跳转(gotoClassGroupBoard)

### 2.6.4.57 @ 2021-08-06
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.4.57.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.4.57.zip)


- 新增接口
    1.设置几何图形类型(setMathGraphType)，可用于几何画板绘制几何图形
    2.鼠标模式下的操作权限(setMouseToolBehavior)
    3.设置白板备注信息(setBoardRemark)
    4.获取白板备注信息(getBoardRemark)
    
- 新增初始化参数
    1.鼠标模式下的操作权限(mouseToolBehavior)
    2.开启公式元素支持(formulaEnable)
    
- 新增元素类型
    1.公式元素(TEDU_BOARD_ELEMENT_FORMULA)，此功能需要设置开启公式元素支持(formulaEnable)为true。

- 新增全局变量
    1.几何元素类型(TEduBoardMathGraphType)
    
- 功能优化
    1.几何画板新增多种几何图形支持
    2.新增公式元素的支持
    3.优化视频加载播放逻辑
    4.图形涂鸦绘制实时同步显示
    5.优化 ppt 资源加载重试逻辑
    6.添加本地缓存，提高资源加载速度
    
- Bug 修复
    1.互动白板宽高变化时滚动条抖动
    2.删除文件时远端 ppt 动画步数重置
    3.自定义图形高度为0时远端图形显示错误
    4.若干已知问题修复

### 2.6.3.42 @ 2021-07-05
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.3.42.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.3.42.zip)

- 新增接口：
    1.设置画笔自动拟合模式(setPenAutoFittingMode)
    2.设置白板父容器的背景色(setBoardContainerColor)
    3.在后台生成当前白板的板书内容(addSnapshotMark)
    
- 调整接口：
    1.添加白板(addBoard)，支持新增白板直接设置背景H5

- 新增初始化参数：
    1.白板离线告警时间间隔(offlineWarningTimeout)
    
- 新增事件：
    1.白板离线告警(onTEBOfflineWarning)

- 调整事件：
    1.增加元素回调(onTEBAddElement)，返回值新增元素类型type

- 优化：
    1.魔法笔功能
    2.支持直接创建H5背景白板
    3.支持白板离线检测
    4.支持生成板书
    
### 2.6.2.41 @ 2021-06-30
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.2.41.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.2.41.zip)

- 调整接口
    1.设置工具的提示语(setToolTypeTitle)
    2.设置允许操作哪些用户绘制的图形(setAccessibleUsers)
    3.设置用户信息(setUserInfo)
    4.添加白板元素(addElement)
    
- 废除接口
    1.废除添加图片元素(addImageElement)，请使用添加白板元素(addElement)
    
- 调整初始化参数：
    1.优化初始化参数结构
    2.初始化权限参数 mathGraphEnable，预加载数学函数图像库
    3.初始化配置参数 scaleRange，白板缩放范围
    
- 新增事件：
    1.文本组件状态回调(onTEBTextElementStatusChanged)
    2.图片元素加载状态(onTEBImageElementStatusChanged)
    3.白板文字工具异常警告(onTEBTextElemenWarning)
    4.框选工具选中元素回调(onTEBSelectedElements)，原有的回调事件(onTEBRectSelected)弃用
    5.数学函数图像工具事件回调(onTEBMathGraphEvent)
    6.远端白板缩放移动状态回调(onTEBZoomDragStatus)
    
- 优化：
    1.涂鸦支持缩放旋转
    2.文本支持等比例缩放
    3.优化用户权限控制
    4.支持显示远端操作元素
    5.支持显示白板元素操作者或创造者信息
    6.支持自动隐藏静止的远端画笔
    7.优化低版本背景图显示
    8.支持数学函数图像显示
    9.支持H5元素移动、缩放、旋转
    10.添加元素支持自定义位置，目前支持图片元素，H5元素，数学函数图像
    11.移动端支持在任意工具下双指缩放白板
    
- Bug 修复
    若干已知问题


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
    
### 2.6.0.37 @ 2021-05-07
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.6.0.37.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.6.0.37.zip)

- 重要特性：
    1. 支持最新的转码方案，具体请看 [新文档转码](https://cloud.tencent.com/document/product/1137/55888)

- 新增接口
    1. 新增限制橡皮擦单次擦除图层数量接口(setEraseLayerLimit)
    2. 新增限制橡皮擦可擦除的数据类型接口(setEraseLayerType)
    3. 新增删除元素接口(removeElement)
  
- 新增初始化参数
    1. syncFps：信令同步频率

- 优化：
    1. 涂鸦绘制性能优化
    2. 涂鸦旋转移动性能优化
    3. 激光笔移动性能优化
    4. 激光笔多端同步效果优化
    5. PPT、图片元素加载
    6. 涂鸦超出白板区域时框选范围错误
    7. 优化白板渲染时的重排、重绘操作
- Bug 修复
    1. 截图时文本元素被iframe元素遮挡
    2. 直线碰撞检测计算错误
    3. 其他若干已知问题
    
### 2.5.7.34 @ 2021.02.02
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.5.7.34.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.5.7.34.zip)
- 新增接口：
    1. 增加移动白板接口(setScaleAnchor)
    2. 增加是否在画线过程中显示远端画笔接口(setRemoteCursorVisible)
    3. 音频元素-设置音量大小(setAudioVolume)
    4. 音频元素-获取音量大小(getAudioVolume)
    5. 增加设置缩放工具的缩放比例(setScaleToolRatio)
    6. 增加添加资源主备域名映射(addBackupDomain)
    7. 增加删除资源主备域名映射(removeBackupDomain)
- 新增事件：
    1. 删除元素事件 onTEBRemoveElement
    1. 增加元素事件 onTEBAddElement
- 新增初始化参数：
    1. 增加初始化参数，关闭移动工具的缩放功能 enableScaleTool
- 优化：
    1. 添加 H5PPT，图片元素(imageElement)/图片文件(imagesFile)，背景图片，视频等资源支持指定主备 URL，需要配合增加备用域名接口使用。
    2. 静态 PPT 翻页交互效果优化
    3. 调整点选框样式
    4. 激光笔功能性能优化
- Bug 修复
    1. 图片旋转后缩放比例不对的问题
    2. Chrome 88版本纵向滚动条缺失
    3. 滚动条触发异常滚动问题
    4. 添加自定义元素时点选框范围错误
    5. 文本工具相关问题
    6. 其他若干已知问题
    7. 修复 setToolTypeTitle 设置衍射不生效问题
    
### 2.5.6.27 @ 2020.12.14
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.5.6.27.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.5.6.27.zip)

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

### 2.5.4.21 @ 2020.10.15
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.5.4.21.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.5.4.21.zip)

- 新增工具类型
    - 新增正圆，正方形工具类，同时支持椭圆工具和矩形工具按 shift 键画正圆和正方形
- 优化
    - 优化橡皮擦擦除箭头工具不精确的问题
- Bug 修复
    - 修复多端同时移动图片元素不同步的问题
    - 修复其他已知问题
    
### 2.5.3.20 @ 2020.08.31
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.5.3.20.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.5.3.20.zip)

- 新增回调
    - 新增视频状态回调 TEDU_BOARD_VIDEO_STATUS_WAITING 和 TEDU_BOARD_VIDEO_STATUS_PLAYING
- Bug 修复
    - 修复激光笔各端显示比例不一致问题
    - 修复白板操作在移动端偶现延迟问题
    - 修复涂鸦到白板外笔迹微变问题
- 优化
    - 桌面端画笔使用时持续展示
    - 视频多次播放失败后回调 ERROR 状态
    - 日志上报优
    
### 2.5.2.10 @ 2020.08.07
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.5.2.10.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.5.2.10.zip)

- 新增回调
    - 新增 H5PPT 状态回调 onTEBH5PPTStatusChanged


### 2.5.1.9 @ 2020.07.23
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.5.1.9.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.5.1.9.zip)

- 功能支持
    - 图片元素支持任意角度旋转和八个方向的缩放
- 接口优化
    - 调用 deleteFile 接口删除非当前文件，则不跳转至默认文件 #DEFAULT
- bug fix
    - 修复文字工具在某些输入法下输入过程中，看不见已输入的文字问题
    - 修复移动端文字工具在白板边界位置点击，键盘会闪一下的问题
- 接口变更
    - addTranscodeFile 增加参数 needSwitch，表示添加文件后是否切换到该文件
    
### 2.5.0.8 @ 2020.07.2
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.5.0.8.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.5.0.8.zip)

- 功能变更
    - addVideoFile/addTranscodeFile/addImagesFile 添加已存在文件，返回该文件 ID
    - 统一各个平台视频播放控制栏的界面
- 功能支持
    - 支持 PPT 超链接点击同步功能
- bug fix
    - 修复涂鸦过程中擦除涂鸦导致涂鸦不同步问题
    - 修复视频文件在特定场景下新增多余白板问题
    - 修复 iOS8 播放视频失败问题
- 性能优化

### 2.4.9.7 @ 2020.06.10
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.9.7.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.9.7.zip)

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
    - iOS/Mac 修复断网情况初始化白板没有回调问题


### 2.4.8.5 @ 2020.05.21
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.8.5.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.8.5.zip)

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
    
### 2.4.7.2 @ 2020.05.08
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.7.2.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.7.2.zip)

- 体验优化
    - 接收端涂鸦流畅性优化
- BUG 修复
    - 修复重置数据导致初始状态不正确的问题

### 2.4.6.1 @ 2020.04.02
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.6.1.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.6.1.zip)

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
    - 修复 addTranscodeFIle 接口 title 转义错误导致添加失败问题
    

### 2.4.4.2 @ 2020.03.14
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.4.2.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.4.2.zip)

- BUG 修复
    - 白板中播放视频时，学生端自动播放的问题
    - 批量导入图片组时，对 URL 字符串长度进行限制(总长7K)，超长时同步返回空串，同时回调错误 TEDU_BOARD_ERROR_DATA_TOO_LARGE
    - 去掉 onGotoBoard 多余回调，在一页 PPT 内有多个步时，只在最后一步/最前一步时才回调

### 2.4.4.1 @ 2020.03.09
* [单击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.4.1.zip)
* [单击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.4.1.zip)

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

### 2.4.1.2 @ 2020.02.19
* [点击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.1.2.zip)
* [点击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.1.2.zip)

- 内部日志优化
    
### 2.4.1.1 @ 2020.01.08
* [点击下载 SDK（iOS）](https://sdk.qcloudtiw.com/ios/TEduBoard_2.4.1.1.zip)
* [点击下载 SDK（macOS）](https://sdk.qcloudtiw.com/mac/TEduBoard_Mac_2.4.1.1.zip)

- 回调变更
    - onTEBFileUploadProgress 回调参数 fileId 变更为 path
    - onTEBFileUploadStatus 回调参数 fileId 变更为 path
- 接口变更
    - addImageElement 支持添加本地图片
- 增加接口
    - 增加添加图片元素回调 onTEBAddImageElement

### 2.4.0 @ 2019.12.06

**注意：2.4.0或以下版本必须使用 IM 4.5.11或以下版本，否则导致白板无法同步消息。**

- 增加接口支持视频播放功能
    - 添加视频文件 - (NSString *)addVideoFile:(NSString *)url;
    - 显示或隐藏视频控制栏- (void)showVideoControl:(BOOL)show;
    - 播放视频 - (void)playVideo;
    - 暂停视频 - (void)pauseVideo;
    - 跳转 - (void)seekVideo:(CGFloat)time;
    - 是否同步本地视频操作到远端 - (void)setSyncVideoStatusEnable:(BOOL)enable;
    - 定时同步视频状态到远端 - (void)startSyncVideoStatus:(NSInteger)interval;
    - 停止同步视频状态 - (void)stopSyncVideoStatus;
- 增加接口支持 H5 页面展示功能
    - 添加 H5 页面 - (NSString *)addH5File:(NSString *)url;
- 增加接口支持图片元素功能
    - 添加图片资源 - (void)addImageElement:(NSString *)url;

### 2.3.7 @ 2019.11.21

- 增加接口
    - setAccessibleUsers 设置允许操作特定用户绘制的图形
    - clearBackground:andSelected 删除选中涂鸦
    - setCursorIcon:cursorIcon 自定义鼠标样式

### 2.3.6 @ 2019.11.18

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


### 2.3.5 @ 2019.10.30

- 新增接口 getThumbnailImages 获取文件缩略图
- 新增步数回调 onTEBGotoStep
- 修复白板放大到一定比例，涂鸦失效问题
- 修复白板放大后精度丢失各端画面不对齐的问题

### 2.3.4 @ 2019.09.25

- 涂鸦屏蔽多指触摸
- ppt 点击事件透传
- 移动端 ppt 翻页交互支持左右滑动翻页

### 2.3.3 @ 2019.08.19

- 增加接口
    - (uint64_t)getSyncTime 支持大房间方案获取对时时间戳
    - (void)syncRemoteTime:(NSString *)userId timestamp:(uint64_t)timestamp 设置远程时间戳
    
- bug 修复
    - 修复 getFileInfo 返回错误的问题

### 2.3.2 @ 2019.08.07

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

### 2.3.1 @ 2019.08.01
- 激光笔优化
- 修复 iOS8 背景图片白板涂鸦闪屏问题
- 修复 iOS8 背景图片和H5背景切换放大问题
- 增加 html 资源加载重试逻辑

### 2.3.0 @ 2019.07.18
性能优化
- 首屏渲染优化

### 2.2.2 @ 2019.07.04
接口修改
- addFile/addH5PPTFile 返回文件 Id
- onTEBFileUploadProgress/onTEBFileUploadStatus 回调接口修改
功能更新
- 支持画出白板再画入

### 2.2.1 @ 2019.06.21
回调接口修改
- onTEBAddBoard 回调 boardId 数组
- onTEBDeleteBoard 回调 boardId 数组

### 2.2.0 @ 2019.06.20
新增接口
- 支持白板上下页跳转是否重置步数
- 支持获取指定文件 id 的文件信息
- TEduBoardErrorCode 增加错误码
    - TEDU_BOARD_ERROR_TIM_HISTORYDATA  同步历史数据失败
    - TEDU_BOARD_ERROR_RUNTIME  白板运行错误

### 2.1.0 @ 2019.05.29
新增功能
- 支持静态 PPT 页面预加载
- 笔迹优化（铅笔工具曲线平滑）
- 支持禁止数据同步（不将本地数据同步到远端）
- 橡皮擦工具支持滑动擦除
- 添加的 H5PPT 已存在时抛出警告
- 支持独立设置每个白板宽高比
- 支持白板缩放及拖动查看

修复 bug
- 修复 macOS 文本工具兼容性问题
- 修复 iOS ES6 兼容性问题
- 修复 iOS H5PPT 兼容性问题

### 2.0.0.5 @ 2019.05.24

修复 bug
- 替换 web board为2.0.0.2版本修复 iOS h5ppt 显示兼容问题


### 2.0.0.4 @ 2019.05.22

修复 bug
- 修复 iOS8.4白板创建没有`onTEBInit`回调的问题
- 修复 iOS9.3/8.4白板创建返回 Javascript 错误的问题
- 修复 macOS 文本工具不可用问题

### 2.0.0.2 @ 2019.05.17

修复 bug
- 修复 iOS12.1白板创建没有`onTEBInit`回调的问题
- 调整`TEduBoardErrorCode`错误码`TEDU_BOARD_ERROR_LOAD`和`TEDU_BOARD_ERROR_AUTH`顺序


### 2.0.0.1 @ 2019.05.15

 新增功能
- 新增鼠标工具类型`TEDU_BOARD_TOOL_TYPE_MOUSE`
- 支持设置 H5 背景
- 白板支持并发文件上传

 bug 修复
- 修复 RC3 版本白板数据同步失败问题




### 2.0.0_RC3 @ 2019.05.10

新增功能
- 支持设置文本样式及字体属性
- 初始化接口支持传入所有属性初始值
- 初始化支持设置白板宽高比
- `AddFile` 接口支持传入 COS 转码 URL


### 2.0.0_RC2 @ 2019.05.08

新增功能
- macOS 平台支持
- PPT 动画展示

修复 bug
- 拼写错误修正：TIC 的`getTRTCClound`接口改名为`getTRTCCloud`


### 2.0.0_RC1 @ 2019.04.26

新增功能
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
