## TEduBoardCallback
白板事件回调接口 

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
| dirtyRects | const TEduBoardRect * | 需要重绘的矩形区域数组（可能有多个）  |
| dirtyRectCount | uint32_t | 需要重绘的矩形区域数组个数  |

#### 警告
该回调不会从统一回调线程触发，可能来自不同线程调用

#### 介绍
该回调只有在启用离屏渲染时才会被触发 当width != 0 || height != 0时，buffer指向白板像素数据，大小为 width * height * 4，像素以白板左上方为原点从左到右从上到下按 BGRA 排列 


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
| url | const char * | 调用 AddImageElement 时传入的 URL |

#### 介绍
只有本地调用 AddImageElement 时会收到该回调 收到该回调表示图片已经上传或下载成功，并且显示出来 


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



## 文件操作回调

### onTEBFileTranscodeProgress
文件转码进度回调 
``` C++
virtual void onTEBFileTranscodeProgress(const char *path, const char *errorCode, const char *errorMsg, const TEduBoardTranscodeFileResult &result)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | const char * | 正在转码的本地文件路径  |
| errorCode | const char * | 文件转码错误码，无异常时为空字符串 ""  |
| errorMsg | const char * | 文件转码错误信息，无异常时为空字符串 ""  |
| result | const TEduBoardTranscodeFileResult & | 文件转码结果  |


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


### onTEBH5FileStatusChanged
H5 文件状态回调 
``` C++
virtual void onTEBH5FileStatusChanged(const char *fileId, TEduBoardH5FileStatus status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件 ID  |
| status | TEduBoardH5FileStatus | 文件状态  |


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
| percent | double | 文件上传进度，取值范围 [0, 1]  |


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



