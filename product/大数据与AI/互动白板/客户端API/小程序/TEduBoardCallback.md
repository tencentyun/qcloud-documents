## TEduBoardCallback
白板事件回调接口 

## 通用事件回调

### TEB_ERROR
白板错误回调 
``` C++
function TEB_ERROR(TEduBoardErrorCode code, String msg)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| code | TEduBoardErrorCode | 错误码，参见 [TEduBoardErrorCode](https://cloud.tencent.com/document/product/1137/40008#teduboarderrorcode) 定义  |
| msg | String | 错误信息，编码格式为 UTF8  |


### TEB_WARNING
白板警告回调 
``` C++
function TEB_WARNING(TEduBoardWarningCode code, String msg)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| code | TEduBoardWarningCode | 错误码，参见 [TEduBoardWarningCode](https://cloud.tencent.com/document/product/1137/40008#teduboardwarningcode) 定义  |
| msg | String | 错误信息，编码格式为 UTF8  |



## 基本流程回调

### TEB_INIT
白板初始化完成回调 
``` C++
function TEB_INIT()
```
#### 介绍
收到该回调后表示白板已处于可正常工作状态（此时白板为空白白板，历史数据尚未拉取到） 


### TEB_HISTROYDATA_SYNCCOMPLETED
白板历史数据同步完成回调  
``` C++
function TEB_HISTROYDATA_SYNCCOMPLETED()
```

### TEB_SYNCDATA
白板同步数据回调 
``` C++
function TEB_SYNCDATA(Object data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | Object | 白板同步数据 |

#### 介绍
收到该回调时需要将回调数据通过信令通道发送给房间内其他人，接受者收到后调用 AddSyncData 接口将数据添加到白板以实现数据同步，该回调用于多个白板间的数据同步，使用腾讯云 IMSDK 进行实时数据同步时，不会收到该回调。


### TEB_OPERATE_CANUNDO_STATUS_CHANGED
白板可撤销状态改变回调 
``` C++
function TEB_OPERATE_CANUNDO_STATUS_CHANGED(Boolean canUndo)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| canUndo | Boolean | 白板当前是否还能执行 Undo 操作  |


### TEB_OPERATE_CANREDO_STATUS_CHANGED
白板可重做状态改变回调 
``` C++
function TEB_OPERATE_CANREDO_STATUS_CHANGED(Boolean canRedo)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| canRedo | Boolean | 白板当前是否还能执行 Redo 操作  |



## 涂鸦功能回调

### TEB_IMAGE_STATUS_CHANGED
白板图片状态改变回调 
``` C++
function TEB_IMAGE_STATUS_CHANGED(TEduBoardImageStatus status, Object data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| status | TEduBoardImageStatus | 新的白板图片状态  |
| data | Object | 当前图片相关信息 |

#### 介绍
data 参数格式如下： 
``` 
{
     currentBoardId: "xxx",          //当前的白板 ID
     imgUrl: "http://xxxx",          //要加载的图片 url
     currentImgUrl: "http://xxxxx",  //当前 img 标签上的图片 url
}
```
 


### TEB_SETBACKGROUNDIMAGE
设置白板背景图片回调 
``` C++
function TEB_SETBACKGROUNDIMAGE(String fileName, String fileUrl, String userData)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileName | String | 文件名  |
| fileUrl | String | 文件的下载地址  |
| userData | String | 透传上传接口的 userData |

#### 介绍
只有本地调用 setBackgroundImage 时会收到该回调 收到该回调表示背景图片已经上传或下载成功，并且显示出来。


### TEB_H5BACKGROUND_STATUS_CHANGED
设置白板背景H5状态改变回调 
``` C++
function TEB_H5BACKGROUND_STATUS_CHANGED(TEduBoardBackgroundH5Status status, Object data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| status | TEduBoardBackgroundH5Status | 新的白板图片状态  |
| data | Object | 当前白板背景数据 |

#### 介绍
data参数格式如下： 
``` 
{
     currentBoardId: "xxx",          //当前的白板 ID
     url: "http://xxxx",             //当前白板的 H5 背景 url
}
```
 



## 白板页操作回调

### TEB_ADDBOARD
增加白板页回调 
``` C++
function TEB_ADDBOARD(Array boardList, String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardList | Array | 增加的白板页 ID 列表（使用后不需要自行调用 Release 方法释放，SDK 内部自动释放）  |
| fileId | String | 增加的白板页所属的文件 ID（目前版本只可能为::DEFAULT）  |


### TEB_DELETEBOARD
删除白板页回调 
``` C++
function TEB_DELETEBOARD(Array boardList, String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardList | Array | 删除的白板页 ID（使用后不需要自行调用 Release 方法释放，SDK 内部自动释放）  |
| fileId | String | 删除的白板页所属的文件 ID（目前版本只可能为::DEFAULT）  |


### TEB_GOTOBOARD
跳转白板页回调 
``` C++
function TEB_GOTOBOARD(String boardId, String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | String | 跳转到的白板页 ID  |
| fileId | String | 跳转到的白板页所属的文件 ID  |


### TEB_GOTOSTEP
白板页动画步数回调 
``` C++
function TEB_GOTOSTEP(Number currentStep, Number totalStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| currentStep | Number | 当前白板页动画步数，取值范围 [0, totalStep)  |
| totalStep | Number | 当前白板页动画总步数  |



## 文件操作回调

### TEB_TRANSCODEPROGRESS
文件转码进度回调 
``` C++
function TEB_TRANSCODEPROGRESS(TEduBoardTranscodeFileResult result)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| result | TEduBoardTranscodeFileResult | 文件转码结果  |


### TEB_ADDTRANSCODEFILE
增加转码文件回调 
``` C++
function TEB_ADDTRANSCODEFILE(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 增加的文件 ID |

#### 介绍
文件加载完成后才会触发该回调 


### TEB_DELETEFILE
删除文件回调 
``` C++
function TEB_DELETEFILE(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 删除的文件 ID  |


### TEB_SWITCHFILE
切换文件回调 
``` C++
function TEB_SWITCHFILE(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 切换到的文件 ID  |


### TEB_FILEUPLOADPROGRESS
文件上传进度回调 
``` C++
function TEB_FILEUPLOADPROGRESS(Object data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | Object | 进度相关信息 |

#### 介绍
data参数格式如下： 
``` 
{
     loaded: 50,     //已经上传的文件部分大小，以字节（bytes）为单位
     total: 100,     //整个文件的大小，以字节（bytes）为单位
     speed: 10,      //文件的上传速度，以字节/秒（bytes/s）为单位
     percent: 0.5,   //文件的上传百分比，以小数形式呈现，例如：下载50%即为0.5
     userData: "xx", //透传上传接口的 userData
     fid: "xxx"      //文件 ID
}
```
 


### TEB_FILEUPLOADSTATUS
文件上传状态回调 
``` C++
function TEB_FILEUPLOADSTATUS(TEduBoardUploadStatus status, Object data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| status | TEduBoardUploadStatus | 文件上传状态  |
| data | Object | 正在上传的文件 ID |

#### 介绍
data参数格式如下： 
``` 
{
     code: 0,                    //错误码，0：成功
     errorMsg: "xx",             //错误描述信息
     fid: "xxx"                  //文件 ID
     fileName: "xx",             //文件名
     fileUrl: "http://xxx",      //文件的下载地址
     picUrls: ["xx", "xx"],      //文件的转码后每一页预览地址
     userData: "xx",             //透传上传接口的 userData
}
```
 



