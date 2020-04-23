## TEduBoardCallback
白板事件回调接口 

## 通用事件回调

### onTEBError
白板错误回调 
``` Java
void onTEBError(int code, String msg)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| code | int | 错误码，参见 TEduBoardErrorCode 定义  |
| msg | String | 错误信息，编码格式为 UTF8  |


### onTEBWarning
白板警告回调 
``` Java
void onTEBWarning(int code, String msg)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| code | int | 错误码，参见 TEduBoardWarningCode 定义  |
| msg | String | 错误信息，编码格式为 UTF8  |



## 基本流程回调

### onTEBInit
白板初始化完成回调 
``` Java
void onTEBInit()
```
#### 介绍
收到该回调后表示白板已处于可正常工作状态（此时白板为空白白板，历史数据尚未拉取到） 


### onTEBHistroyDataSyncCompleted
白板历史数据同步完成回调 
``` Java
void onTEBHistroyDataSyncCompleted()
```

### onTEBSyncData
白板同步数据回调 
``` Java
void onTEBSyncData(String data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | String | 白板同步数据（JSON 格式字符串） |

#### 介绍
收到该回调时需要将回调数据通过信令通道发送给房间内其他人，接受者收到后调用 AddSyncData 接口将数据添加到白板以实现数据同步，该回调用于多个白板间的数据同步，使用腾讯云 IMSDK 进行实时数据同步时，不会收到该回调 


### onTEBUndoStatusChanged
白板可撤销状态改变回调 
``` Java
void onTEBUndoStatusChanged(boolean canUndo)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| canUndo | boolean | 白板当前是否还能执行 Undo 操作  |


### onTEBRedoStatusChanged
白板可重做状态改变回调 
``` Java
void onTEBRedoStatusChanged(boolean canRedo)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| canRedo | boolean | 白板当前是否还能执行 Redo 操作  |



## 涂鸦功能回调

### onTEBImageStatusChanged
白板图片状态改变回调 
``` Java
void onTEBImageStatusChanged(final String boardId, final String url, int status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | final String | 白板 ID  |
| url | final String | 白板图片 URL  |
| status | int | 新的白板图片状态  |


### onTEBSetBackgroundImage
设置白板背景图片回调 
``` Java
void onTEBSetBackgroundImage(final String url)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | final String | 调用 SetBackgroundImage 时传入的 URL |

#### 介绍
只有本地调用 SetBackgroundImage 时会收到该回调 收到该回调表示背景图片已经上传或下载成功，并且显示出来 


### onTEBAddImageElement
添加图片元素回调 
``` Java
void onTEBAddImageElement(final String url)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | final String | 调用 SetBackgroundImage 时传入的 URL |

#### 介绍
只有本地调用 addImageElement 时会收到该回调 收到该回调表示背景图片已经上传或下载成功，并且显示出来 


### onTEBBackgroundH5StatusChanged
设置白板背景 H5 状态改变回调 
``` Java
void onTEBBackgroundH5StatusChanged(final String boardId, final String url, final int status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | final String | 白板 ID  |
| url | final String | 白板图片 URL  |
| status | final int | 新的白板图片状态  |



## 白板页操作回调

### onTEBAddBoard
增加白板页回调 
``` Java
void onTEBAddBoard(final List< String > boardList, final String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardList | final List< String > | 增加的白板页 ID 列表（使用后不需要自行调用 Release 方法释放，SDK 内部自动释放）  |
| fileId | final String | 增加的白板页所属的文件 ID（目前版本只可能为::DEFAULT）  |


### onTEBDeleteBoard
删除白板页回调 
``` Java
void onTEBDeleteBoard(final List< String > boardList, final String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardList | final List< String > | 删除的白板页 ID（使用后不需要自行调用 Release 方法释放，SDK 内部自动释放）  |
| fileId | final String | 删除的白板页所属的文件 ID（目前版本只可能为::DEFAULT）  |


### onTEBGotoBoard
跳转白板页回调 
``` Java
void onTEBGotoBoard(final String boardId, final String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | final String | 跳转到的白板页 ID  |
| fileId | final String | 跳转到的白板页所属的文件 ID  |


### onTEBGotoStep
白板页动画步数回调 
``` Java
void onTEBGotoStep(int currentStep, int totalStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| currentStep | int | 当前白板页动画步数，取值范围 [0, totalStep)  |
| totalStep | int | 当前白板页动画总步数  |


### onTEBRectSelected
框选工具选中回调 
``` Java
void onTEBRectSelected()
```
#### 警告
只有框选中涂鸦或图片元素后触发回调 



## 文件操作回调

### onTEBAddTranscodeFile
增加转码文件回调 
``` Java
void onTEBAddTranscodeFile(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 增加的文件 ID |

#### 介绍
文件加载完成后才会触发该回调 


### onTEBDeleteFile
删除文件回调 
``` Java
void onTEBDeleteFile(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 删除的文件 ID  |


### onTEBSwitchFile
切换文件回调 
``` Java
void onTEBSwitchFile(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 切换到的文件 ID  |


### onTEBFileUploadProgress
文件上传进度回调 
``` Java
void onTEBFileUploadProgress(final String path, int currentBytes, int totalBytes, int uploadSpeed, float percent)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | final String | 正在上传的文件路径  |
| currentBytes | int | 当前已上传大小，单位 bytes  |
| totalBytes | int | 文件总大小，单位 bytes  |
| uploadSpeed | int | 文件上传速度，单位 bytes  |
| percent | float | 文件上传进度，取值范围 [0, 1]  |


### onTEBFileUploadStatus
文件上传状态回调 
``` Java
void onTEBFileUploadStatus(final String path, int status, int errorCode, final String errorMsg)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | final String | 正在上传的文件路径  |
| status | int | 文件上传状态  |
| errorCode | int | 文件上传错误码  |
| errorMsg | final String | 文件上传错误信息  |


### onTEBFileTranscodeProgress
文件转码进度回调 
``` Java
void onTEBFileTranscodeProgress(final String file, final String errorCode, final String errorMsg, final TEduBoardTranscodeFileResult result)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| file | final String | 正在转码的本地文件路径  |
| errorCode | final String | 文件转码错误码，无异常时为空字符串 ""  |
| errorMsg | final String | 文件转码错误信息，无异常时为空字符串 ""  |
| result | final TEduBoardTranscodeFileResult | 文件转码结果  |


### onTEBH5FileStatusChanged
H5 文件状态回调 
``` Java
void onTEBH5FileStatusChanged(String fileId, int status)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 文件 ID  |
| status | int | 文件状态  |


### onTEBAddImagesFile
增加批量图片文件回调 
``` Java
void onTEBAddImagesFile(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 增加的文件 ID |

#### 介绍
文件加载完成后才会触发该回调 


### onTEBVideoStatusChanged
视频文件状态回调 
``` Java
void onTEBVideoStatusChanged(String fileId, int status, float progress, float duration)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 文件 ID  |
| status | int | 文件状态  |
| progress | float | 当前进度（秒）（仅支持 mp4 格式）  |
| duration | float | 总时长（秒）（仅支持 mp4 格式）  |



