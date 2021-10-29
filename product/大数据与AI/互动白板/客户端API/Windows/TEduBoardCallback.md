## TEduBoardCallback
白板事件回调接口，请参考 [回调定义文档](https://doc.qcloudtiw.com/win32/latest/struct_t_edu_board_callback.html)

## 通用事件回调

### onTEBError
白板错误回调 
``` C++
virtual void onTEBError(TEduBoardErrorCode code, const char *msg)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| code | TEduBoardErrorCode | 错误码，参见 TEduBoardErrorCode 定义  |
| msg | const char * | 错误信息，编码格式为 UTF8  |


### onTEBWarning
白板警告回调 
``` C++
virtual void onTEBWarning(TEduBoardWarningCode code, const char *msg)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| code | TEduBoardWarningCode | 错误码，参见 TEduBoardWarningCode 定义  |
| msg | const char * | 错误信息，编码格式为 UTF8  |



## 基本流程回调

### onTEBInit
白板初始化完成回调 
``` C++
virtual void onTEBInit()=0
```
#### 介绍
收到该回调后表示白板已处于可正常工作状态（此时白板为空白白板，历史数据尚未拉取到） 


### onTEBHistroyDataSyncCompleted
白板历史数据同步完成回调 
``` C++
virtual void onTEBHistroyDataSyncCompleted()
```

### onTEBSyncData
白板同步数据回调 
``` C++
virtual void onTEBSyncData(const char *data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | const char * | 白板同步数据（JSON 格式字符串） |

#### 介绍
收到该回调时需要将回调数据通过信令通道发送给房间内其他人，接受者收到后调用 AddSyncData 接口将数据添加到白板以实现数据同步，该回调用于多个白板间的数据同步，使用腾讯云 IMSDK 进行实时数据同步时，不会收到该回调。 


### onTEBUndoStatusChanged
白板可撤销状态改变回调 
``` C++
virtual void onTEBUndoStatusChanged(bool canUndo)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| canUndo | bool | 白板当前是否还能执行 Undo 操作  |


### onTEBRedoStatusChanged
白板可重做状态改变回调 
``` C++
virtual void onTEBRedoStatusChanged(bool canRedo)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| canRedo | bool | 白板当前是否还能执行 Redo 操作  |


### onTEBRectSelected
框选工具选中回调 只有框选中涂鸦或图片元素后触发回调 
``` C++
virtual void onTEBRectSelected()
```

### onTEBRefresh
刷新白板回调 
``` C++
virtual void onTEBRefresh()
```

### onTEBOffscreenPaint
白板离屏渲染回调 
``` C++
virtual void onTEBOffscreenPaint(const void *buffer, uint32_t width, uint32_t height, const TEduBoardRect *dirtyRects, uint32_t dirtyRectCount)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| buffer | const void * | 白板数据  |
| width | uint32_t | 白板像素数据的宽度  |
| height | uint32_t | 白板像素数据的高度  |
| dirtyRects | const TEduBoardRect * | 需要重绘的矩形区域数组（有一定概率有多个）  |
| dirtyRectCount | uint32_t | 需要重绘的矩形区域数组个数  |

#### 警告
该回调不会从统一回调线程触发，可能来自不同线程调用

#### 介绍
该回调只有在启用离屏渲染时才会被触发 当width != 0 || height != 0时，buffer 指向白板像素数据，大小为 width * height * 4，像素以白板左上方为原点从左到右从上到下按 BGRA 排列 


### onTEBAudioCallbackStarted
白板音频开始回调 
``` C++
virtual void onTEBAudioCallbackStarted(uint32_t channels, uint32_t channelSize, uint32_t sampleRate)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| channels | uint32_t | 回调的音频声道数  |
| channelSize | uint32_t | 回调的每个声道的采样点个数  |
| sampleRate | uint32_t | 回调的音频采样率  |

#### 警告
该回调不会从统一回调线程触发，可能来自不同线程调用 


### onTEBAudioCallbackPacket
白板音频包回调 
``` C++
virtual void onTEBAudioCallbackPacket(const float **buffer, int64_t pts)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| buffer | const float ** | 音频数据数组，格式为 buffer[channels][channelSize]  |
| pts | int64_t | 音频包时间戳  |

#### 警告
该回调不会从统一回调线程触发，可能来自不同线程调用 


### onTEBAudioCallbackStopped
白板音频停止回调 
``` C++
virtual void onTEBAudioCallbackStopped()
```
#### 警告
该回调不会从统一回调线程触发，可能来自不同线程调用 



## 涂鸦功能回调

### onTEBImageStatusChanged
白板图片状态改变回调 
``` C++
virtual void onTEBImageStatusChanged(const char *boardId, const char *url, TEduBoardImageStatus status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 白板 ID  |
| url | const char * | 白板图片 URL  |
| status | TEduBoardImageStatus | 新的白板图片状态  |


### onTEBSetBackgroundImage
设置白板背景图片回调 
``` C++
virtual void onTEBSetBackgroundImage(const char *url)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 调用 SetBackgroundImage 时传入的 URL |

#### 介绍
只有本地调用 SetBackgroundImage 时会收到该回调 收到该回调表示背景图片已经上传或下载成功，并且显示出来 


### onTEBAddImageElement
添加白板图片元素回调 
``` C++
virtual void onTEBAddImageElement(const char *url)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 调用 AddImageElement 时传入的 URL  |

#### 警告
该回调已废弃，请使用 AddElement 接口及 onTEBAddElement 回调代替

#### 介绍
只有本地调用 AddImageElement 时会收到该回调 收到该回调表示图片已经上传或下载成功，并且显示出来 


### onTEBAddElement
添加白板元素回调 
``` C++
virtual void onTEBAddElement(const char *elementId, const char *url, const TEduBoardElementType type)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 调用 AddElement 时返回的元素 ID  |
| url | const char * | 调用 AddElement 时传入的 URL  |
| type | const TEduBoardElementType | 元素类型 TEduBoardElementType 只有本地调用 AddElement 时会收到该回调 收到该回调表示元素已经显示出来  |


### onTEBRemoveElement
删除白板元素回调 
``` C++
virtual void onTEBRemoveElement(const TEduBoardStringList *elementIds)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementIds | const TEduBoardStringList * | 被删除的元素 ID（使用后不需要自行调用 Release 方法释放，SDK 内部自动释放）  |


### onTEBBackgroundH5StatusChanged
设置白板背景 H5 状态改变回调 
``` C++
virtual void onTEBBackgroundH5StatusChanged(const char *boardId, const char *url, TEduBoardBackgroundH5Status status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 白板 ID  |
| url | const char * | 白板图片 URL  |
| status | TEduBoardBackgroundH5Status | 新的白板图片状态  |



## 白板页操作回调

### onTEBAddBoard
增加白板页回调 
``` C++
virtual void onTEBAddBoard(const TEduBoardStringList *boardList, const char *fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardList | const TEduBoardStringList * | 增加的白板页 ID 列表（使用后不需要自行调用 Release 方法释放，SDK 内部自动释放）  |
| fileId | const char * | 增加的白板页所属的文件 ID（目前版本只可能为::DEFAULT）  |


### onTEBDeleteBoard
删除白板页回调 
``` C++
virtual void onTEBDeleteBoard(const TEduBoardStringList *boardList, const char *fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardList | const TEduBoardStringList * | 删除的白板页 ID（使用后不需要自行调用 Release 方法释放，SDK 内部自动释放）  |
| fileId | const char * | 删除的白板页所属的文件 ID（目前版本只可能为::DEFAULT）  |


### onTEBGotoBoard
跳转白板页回调 
``` C++
virtual void onTEBGotoBoard(const char *boardId, const char *fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 跳转到的白板页 ID  |
| fileId | const char * | 跳转到的白板页所属的文件 ID  |


### onTEBGotoStep
白板页动画步数回调 
``` C++
virtual void onTEBGotoStep(uint32_t currentStep, uint32_t totalStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| currentStep | uint32_t | 当前白板页动画步数，取值范围 [0, totalStep)  |
| totalStep | uint32_t | 当前白板页动画总步数  |


### onTEBSnapshot
白板快照 
``` C++
virtual void onTEBSnapshot(const char *path)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | const char * | 快照本地路径，编码格式为 UTF8  |



## 文件操作回调

### onTEBAddTranscodeFile
增加转码文件回调 
``` C++
virtual void onTEBAddTranscodeFile(const char *fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 增加的文件 ID |

#### 介绍
文件加载完成后才会触发该回调 


### onTEBAddImagesFile
增加批量图片文件回调 
``` C++
virtual void onTEBAddImagesFile(const char *fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 增加的文件 ID |

#### 介绍
文件加载完成后才会触发该回调 


### onTEBVideoStatusChanged
视频文件状态回调 
``` C++
virtual void onTEBVideoStatusChanged(const char *fileId, TEduBoardVideoStatus status, double progress, double duration)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件 ID  |
| status | TEduBoardVideoStatus | 文件状态  |
| progress | double | 当前进度（秒）（仅支持 mp4 格式）  |
| duration | double | 总时长（秒）（仅支持 mp4 格式）  |


### onTEBAudioStatusChanged
音频文件状态回调 
``` C++
virtual void onTEBAudioStatusChanged(const char *elementId, TEduBoardAudioStatus status, double progress, double duration)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 元素 ID  |
| status | TEduBoardAudioStatus | 文件状态  |
| progress | double | 当前进度（秒）  |
| duration | double | 总时长（秒）  |


### onTEBH5FileStatusChanged
H5文件状态回调 
``` C++
virtual void onTEBH5FileStatusChanged(const char *fileId, TEduBoardH5FileStatus status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件 ID  |
| status | TEduBoardH5FileStatus | 文件状态  |


### onTEBH5PPTStatusChanged
H5PPT文件状态改变回调 
``` C++
virtual void onTEBH5PPTStatusChanged(const char *fileId, TEduBoardH5PPTStatus status, const char *message)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件 ID  |
| status | TEduBoardH5PPTStatus | 文件状态  |
| message | const char * | 状态消息  |


### onTEBDeleteFile
删除文件回调 
``` C++
virtual void onTEBDeleteFile(const char *fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 删除的文件 ID  |


### onTEBSwitchFile
切换文件回调 
``` C++
virtual void onTEBSwitchFile(const char *fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 切换到的文件 ID  |


### onTEBFileUploadProgress
文件上传进度回调 
``` C++
virtual void onTEBFileUploadProgress(const char *path, int currentBytes, int totalBytes, int uploadSpeed, double percent)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | const char * | 正在上传的文件路径  |
| currentBytes | int | 当前已上传大小，单位 bytes  |
| totalBytes | int | 文件总大小，单位 bytes  |
| uploadSpeed | int | 文件上传速度，单位 bytes  |
| percent | double | 文件上传进度，取值范围 [0,1]  |


### onTEBFileUploadStatus
文件上传状态回调 
``` C++
virtual void onTEBFileUploadStatus(const char *path, TEduBoardUploadStatus status, int errorCode, const char *errorMsg)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | const char * | 正在上传的文件路径  |
| status | TEduBoardUploadStatus | 文件上传状态  |
| errorCode | int | 文件上传错误码  |
| errorMsg | const char * | 文件上传错误信息  |


### onTEBOfflineWarning
白板离线告警 
``` C++
virtual void onTEBOfflineWarning(int count)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| count | int | 告警次数  |


### onTEBTextElementStatusChanged
文本组件状态回调 
``` C++
virtual void onTEBTextElementStatusChanged(const char *status, const char *id, const char *value, int left, int top)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| status | const char * | 文本组件状态（focus：获得焦点，blur：失去焦点）  |
| id | const char * | 文本组件 ID  |
| value | const char * | 文本内容  |
| left | int | 文本组件水平偏移  |
| top | int | 文本组件垂直偏移  |


### onTEBImageElementStatusChanged
白板图片状态改变回调 
``` C++
virtual void onTEBImageElementStatusChanged(const char *boardId, const char *url, const char *elementId, TEduBoardImageStatus status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 白板 ID  |
| url | const char * | 白板图片 URL  |
| elementId | const char * | 当前元素 ID  |
| status | TEduBoardImageStatus | 新的白板图片状态  |


### onTEBTextElementWarning
白板图片状态改变回调 
``` C++
virtual void onTEBTextElementWarning(const char *message, TEduBoardTextComponentStatus code)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| message | const char * | 异常信息  |
| code | TEduBoardTextComponentStatus | 白板文字工具异常状态码  |


### onTEBSelectedElements
框选工具选中元素回调 
``` C++
virtual void onTEBSelectedElements(const TEduBoardSelectedElementInfoList &selElementList)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| selElementList | const TEduBoardSelectedElementInfoList & | 选中的元素列表 ID  |


### onTEBMathGraphEvent
框选工具选中元素回调 
``` C++
virtual void onTEBMathGraphEvent(const char *boardId, const char *graphId, const char *message, TEduBoardMathGraphCode code)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 函数画板 ID  |
| graphId | const char * | 函数图像 ID  |
| message | const char * | 异常信息  |
| code | TEduBoardMathGraphCode | 数学函数图像工具状态码(TEduBoardMathGraphCode)  |


### onTEBZoomDragStatus
远端白板缩放移动状态回调 
``` C++
virtual void onTEBZoomDragStatus(const char *fid, int32_t scale, int32_t xOffset, int32_t yOffset)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fid | const char * | 文件 ID  |
| scale | int32_t | 文件缩放比  |
| xOffset | int32_t | 当前可视区域距左上角的横向偏移量  |
| yOffset | int32_t | 当前可视区域距左上角的纵向偏移量  |


### onTEBGroupStatusChanged
分组讨论状态变更 
``` C++
virtual void onTEBGroupStatusChanged(bool enable, const char *classGroupId, TEduBoardClassGroupOperationType operationType, const char *messgae)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 分组模式状态  |
| classGroupId | const char * | 发生变化的分组 ID  |
| operationType | TEduBoardClassGroupOperationType | 触发状态变更的操作  |
| messgae | const char * | 操作信息  |



