## TEduBoard
白板控制器 

## 创建销毁实例

### TEduBoard
白板构造函数 
``` Javascript  
TEduBoard(TEduBoardInitParam initParams)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| initParams | TEduBoardInitParam | **必填**白板初始化参数  |


### destroy
销毁白板 
``` Javascript
void destroy()
```


## 设置 TEduBoardCallback 回调

### on
启用事件监听 
``` Javascript
void on(String name, Function callback)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| name | String | **必填**要监听的事件  |
| callback | Function | **必填**事件处理回调  |


### off
取消事件监听 
``` Javascript
void off(String name, Function callback)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| name | String | **必填**要取消监听的事件  |
| callback | Function | **必填**事件处理回调  |



## 基本流程接口

### addSyncData
添加白板同步数据 
``` Javascript
void addSyncData(Object data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | Object | **必填**接收到的房间内其他人发送的同步数据 |

#### 介绍
该接口用于多个白板间的数据同步，使用内置 IM 作为信令通道时，不需要调用该接口。 


### getVersion
获取 SDK 版本号 
``` Javascript
String getVersion()
```
#### 返回
SDK 版本号 


### setDataSyncEnable
设置白板是否开启数据同步 
``` Javascript
void setDataSyncEnable(Boolean enable)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | Boolean | **必填**是否开启 |

#### 介绍
白板创建后默认开启数据同步，关闭数据同步，本地的所有白板操作不会同步到远端和服务器。 


### isDataSyncEnable
获取白板是否开启数据同步 
``` Javascript
Boolean isDataSyncEnable()
```
#### 返回
是否开启数据同步，true 表示开启，false 表示关闭 


### reset
重置白板 
``` Javascript
void reset()
```
#### 介绍
调用该接口后将会删除所有的白板页和文件。


### getSyncTime
获取同步时间戳 
``` Javascript
Number getSyncTime()
```
#### 返回
毫秒级同步时间戳 


### syncRemoteTime
同步远端时间戳 
``` Javascript
void syncRemoteTime(String userId, Number timestamp)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| userId | String | **必填**远端用户 ID  |
| timestamp | Number | **必填**远端用户毫秒级同步时间戳  |



## 涂鸦相关接口

### setDrawEnable
设置白板是否允许涂鸦 
``` Javascript
void setDrawEnable(Boolean enable)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | Boolean | **必填**是否允许涂鸦，true 表示白板可以涂鸦，false 表示白板不能涂鸦 |

#### 介绍
白板创建后默认为允许涂鸦状态。 


### isDrawEnable
获取白板是否允许涂鸦 
``` Javascript
Boolean isDrawEnable()
```
#### 返回
是否允许涂鸦，true 表示白板可以涂鸦，false 表示白板不能涂鸦 


### setAccessibleUsers
设置允许操作哪些用户绘制的图形 
``` Javascript
void setAccessibleUsers(Array users)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| users | Array | **必填**指定允许操作的用户集，为[]或 null 表示不加限制 |

#### 介绍
该接口会产生以下影响：
1. ERASER 工具只能擦除 users 参数列出的用户绘制的涂鸦，无法擦除其他人绘制的涂鸦。
2. POINTSELECT、SELECT 工具只能选中 users 参数列出的用户绘制的涂鸦，无法选中其他人绘制的涂鸦。
3. clear 接口只能用于清空选中涂鸦以及 users 参数列出的用户绘制的涂鸦，无法清空背景及其他人绘制的涂鸦。
4. 白板包含的其他功能未在本列表明确列出者都可以确定不受本接口影响。 


### setGlobalBackgroundColor
设置所有白板的背景色 
``` Javascript
void setGlobalBackgroundColor(Color color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | Color | **必填**要设置的全局背景色 |

#### 介绍
调用该接口将导致所有白板的背景色发生改变新创建白板的默认背景色取全局背景色。 


### getGlobalBackgroundColor
获取白板全局背景色 
``` Javascript
Color getGlobalBackgroundColor()
```
#### 返回
全局背景色 


### setBackgroundColor
设置当前白板页的背景色 
``` Javascript
void setBackgroundColor(Color color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | Color | **必填**要设置的背景色 |

#### 介绍
白板页创建以后的默认背景色由 SetDefaultBackgroundColor 接口设定。 


### getBackgroundColor
获取当前白板页的背景色 
``` Javascript
Color getBackgroundColor()
```
#### 返回
当前白板页的背景色 


### setToolType
设置要使用的白板工具 
``` Javascript
void setToolType(TEduBoardToolType type)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| type | TEduBoardToolType | **必填**要设置的白板工具  |


### getToolType
获取正在使用的白板工具 
``` Javascript
TEduBoardToolType getToolType()
```
#### 返回
正在使用的白板工具 


### setCursorIcon
自定义白板工具鼠标样式 
``` Javascript
void setCursorIcon(TEduBoardToolType toolType, TEduBoardCursorIcon cursorIcon)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| toolType | TEduBoardToolType | **必填**要设置鼠标样式的白板工具类型  |
| cursorIcon | TEduBoardCursorIcon | **必填**要设置的鼠标样式  |


### setBrushColor
设置画笔颜色 
``` Javascript
void setBrushColor(Color color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | Color | **必填**要设置的画笔颜色 |

#### 介绍
画笔颜色用于所有涂鸦绘制。 


### getBrushColor
获取画笔颜色 
``` Javascript
Color getBrushColor()
```
#### 返回
画笔颜色 


### setBrushThin
设置画笔粗细 
``` Javascript
void setBrushThin(Number thin)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| thin | Number | **必填**要设置的画笔粗细 |

#### 介绍
画笔粗细用于所有涂鸦绘制，实际像素值取值(thin * 白板的高度 / 10000)px，如果结果小于1px，则涂鸦的线条会比较虚。 


### getBrushThin
获取画笔粗细 
``` Javascript
Number getBrushThin()
```
#### 返回
画笔粗细 


### setTextColor
设置文本颜色 
``` Javascript
void setTextColor(Color color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | Color | **必填**要设置的文本颜色  |


### getTextColor
获取文本颜色 
``` Javascript
Color getTextColor()
```
#### 返回
文本颜色 


### setTextSize
设置文本大小 
``` Javascript
void setTextSize(Number size)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| size | Number | **必填**要设置的文本大小 |

#### 介绍
实际像素值取值(size * 白板的高度 / 10000)px。 


### getTextSize
获取文本大小 
``` Javascript
Number getTextSize()
```
#### 返回
文本大小 


### setTextStyle
设置文本样式 
``` Javascript
void setTextStyle(TEduBoardTextStyle style)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| style | TEduBoardTextStyle | **必填**要设置的文本样式  |


### getTextStyle
获取文本样式 
``` Javascript
TEduBoardTextStyle getTextStyle()
```
#### 返回
文本样式 


### setLineStyle
设置直线样式 
``` Javascript
void setLineStyle(TEduBoardLineStyle style)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| style | TEduBoardLineStyle | **必填**要设置的直线样式  |


### getLineStyle
获取直线样式 
``` Javascript
TEduBoardLineStyle getLineStyle()
```
#### 返回
直线样式 


### setOvalDrawMode
设置椭圆绘制模式 
``` Javascript
void setOvalDrawMode(TEduBoardOvalDrawMode drawMode)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| drawMode | TEduBoardOvalDrawMode | **必填**要设置的椭圆绘制模式  |


### getOvalDrawMode
获取椭圆绘制模式 
``` Javascript
TEduBoardOvalDrawMode getOvalDrawMode()
```
#### 返回
椭圆绘制模式 


### clear
清空当前白板页涂鸦 
``` Javascript
void clear(Boolean clearBackground, Boolean clearSelectedOnly)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| clearBackground | Boolean | **可选**是否同时清空背景色以及背景图片  |
| clearSelectedOnly | Boolean | **可选**是否只清除选中部分涂鸦  |

#### 警告
目前不支持清除选中部分的同时清除背景 


### setBackgroundImage
设置当前白板页的背景图片 
``` Javascript
void setBackgroundImage(String url, TEduBoardImageFitMode mode)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | String | **必填**要设置的背景图片 URL，编码格式为 UTF8  |
| mode | TEduBoardImageFitMode | **可选**要使用的图片填充对齐模式 |

#### 介绍
除了设置一个在线图片为背景外，您也可以选择上传一个本地图片作为背景，此时 url 参数可以传一个 Object 类型，格式如下： 
``` 
{
   data: document.getElementById('uploadFile').files[0], //取自 input 标签的 fileObject 对象
   name: 'xxx.jpg', //文件名
   userData: 'xxx' //透传数据，会在文件上传进度回调中带回
}
```
 


### setBackgroundH5
设置当前白板页的背景 H5 页面 
``` Javascript
void setBackgroundH5(String url)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | String | **必填**要设置的背景 H5 页面 URL |

#### 介绍
该接口与 SetBackgroundImage 接口互斥。 


### undo
撤销当前白板页上一次动作 
``` Javascript
void undo()
```

### redo
重做当前白板页上一次撤销 
``` Javascript
void redo()
```

### resize
重新计算白板大小，并渲染 
``` Javascript
void resize()
```


## 白板页操作接口

### addBoard
增加一页白板 
``` Javascript
String addBoard(String url, TEduBoardImageFitMode mode)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | String | **可选**要使用的背景图片 URL，为 null 表示不指定背景图片  |
| mode | TEduBoardImageFitMode | **可选**要使用的图片填充对齐模式  |

#### 返回
白板 ID 

#### 警告
白板页会被添加到默认文件（文件ID为::DEFAULT)，自行上传的文件无法添加白板页。 


### deleteBoard
删除一页白板 
``` Javascript
void deleteBoard(String boardId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | String | **可选**要删除的白板 ID，为 null 表示删除当前页  |

#### 警告
只允许删除默认文件（文件 ID 为::DEFAULT）内的白板页，且默认白板页（白板 ID 为::DEFAULT）无法删除。 


### prevStep
上一步 每个 Step 对应 PPT 的一个动画效果，若当前没有已展示的动画效果，则该接口调用会导致向前翻页 
``` Javascript
void prevStep()
```

### nextStep
下一步 
``` Javascript
void nextStep()
```
#### 介绍
每个 Step 对应 PPT 的一个动画效果，若当前没有未展示的动画效果，则该接口调用会导致向后翻页。 


### prevBoard
向前翻页 
``` Javascript
void prevBoard(Boolean resetStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| resetStep | Boolean | **可选**指定翻到指定页以后是否重置 PPT 动画步数 |

#### 介绍
若当前白板页为当前文件的第一页，则该接口调用无效。 


### nextBoard
向后翻页 
``` Javascript
void nextBoard(Boolean resetStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| resetStep | Boolean | **可选**指定翻到指定页以后是否重置 PPT 动画步数 |

#### 介绍
若当前白板页为当前文件的最后一页，则该接口调用无效。 


### gotoBoard
跳转到指定白板页 
``` Javascript
void gotoBoard(String boardId, Boolean resetStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | String | **必填**要跳转到的白板页 ID  |
| resetStep | Boolean | **可选**指定翻到指定页以后是否重置 PPT 动画步数 |

#### 介绍
允许跳转到任意文件的白板页。 


### getCurrentBoard
获取当前白板页ID 
``` Javascript
String getCurrentBoard()
```
#### 返回
当前白板页 ID 


### getBoardList
获取所有文件的白板列表 
``` Javascript
Array getBoardList()
```
#### 返回
所有文件的白板列表


### setBoardRatio
设置当前白板页宽高比 
``` Javascript
void setBoardRatio(String ratio)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| ratio | String | **必填**要设置的白板宽高比 |

#### 介绍
格式如: "4:3"、"16:9"。 


### getBoardRatio
获取当前白板页宽高比 
``` Javascript
String getBoardRatio()
```
#### 返回
白板宽高比，格式与 SetBoardRatio 接口参数格式一致 


### setBoardScale
设置当前白板页缩放比例 
``` Javascript
void setBoardScale(Number scale)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| scale | Number | **必填**要设置的白板缩放比例 |

#### 介绍
支持范围: [100，300]，实际缩放比为: scale/100。 


### getBoardScale
获取当前白板页缩放比例 
``` Javascript
Number getBoardScale()
```
#### 返回
白板缩放比例，格式与 SetBoardScale 接口参数格式一致

### setBoardContentFitMode
设置白板内容自适应模式 
``` Javascript
void setBoardContentFitMode(TEduBoardContentFitMode mode)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| mode | TEduBoardContentFitMode | **必填**要设置的白板内容自适应模式 |

#### 介绍
设置自适应模式后会影响所有后续白板内容操作，受影响接口包括：AddTranscodeFile。 


### getBoardContentFitMode
获取白板内容自适应模式 
``` Javascript
TEduBoardContentFitMode getBoardContentFitMode()
```
#### 返回
白板内容自适应模式 



## 文件操作接口

### applyFileTranscode
发起文件转码请求 
``` Javascript
void applyFileTranscode(Object fileObj, TEduBoardTranscodeConfig config)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileObj | Object | **必填**请求转码的文件对象，详细格式见下方介绍  |
| config | TEduBoardTranscodeConfig | **必填**转码参数  |

#### 警告
本接口设计用于在接入阶段快速体验转码功能，原则上不建议在生产环境中使用，生产环境中的转码请求建议使用后台服务接口发起。

#### 介绍
fileObj 参数格式如下： 
``` 
{
   data: document.getElementById('uploadFile').files[0], //取自input标签的fileObject对象
   userData: 'xxx' //透传数据，会在文件转码进度回调中带回
}
```

- 本接口支持支持 PPT、PDF、Word 文件转码。
- PPT 文档默认转为 H5 动画，能够还原 PPT 原有动画效果，其它文档转码为静态图片。
- PPT 动画转码耗时约1秒/页，所有文档的静态转码耗时约0.5秒/页。
- 转码进度和结果将会通过 onTEBFileTranscodeProgress 回调返回，详情参见该回调说明文档。 


### getFileTranscodeProgress
主动查询文件转码进度 
``` Javascript
void getFileTranscodeProgress(Object data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | Object | **必填**文件信息，格式见下方介绍  |

#### 警告
该接口仅用于特殊业务场景下主动查询文件转码进度，调用 applyFileTranscode 后，SDK 内部将会自动定期触发 TEB_TRANSCODEPROGRESS 回调，正常情况下您不需要主动调用此接口。

#### 介绍
data 参数格式如下： 
``` 
{
    taskId: "xxxxx" //从TEB_TRANSCODEPROGRESS回调拿到的taskId
}
```
转码进度和结果将会通过 onTEBFileTranscodeProgress 回调返回，详情参见该回调说明文档。 


### addTranscodeFile
添加转码文件 
``` Javascript
String addTranscodeFile(TEduBoardTranscodeFileResult result)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| result | TEduBoardTranscodeFileResult | **必填**文件转码结果  |

#### 返回
文件ID 

#### 警告
当传入文件的 URL 重复时，文件 ID 返回为空字符串。 
在收到对应的 TEB_TRANSCODEPROGRESS 回调前，无法用返回的文件 ID 查询到文件信息。

#### 介绍
本接口只处理传入参数结构体的 title、resolution、url、pages 字段 调用该接口后，SDK会在后台进行文件加载，期间用户可正常进行其它操作，加载成功或失败后会触发相应回调 文件加载成功后，将自动切换到该文件。 


### deleteFile
删除文件 
``` Javascript
void deleteFile(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | **可选**要删除的文件 ID |

#### 介绍
文件 ID为 null 时表示当前文件，默认文件无法删除。 


### switchFile
切换文件 
``` Javascript
void switchFile(String fileId, String boardId, Number stepIndex)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | **必填**要切换到的文件 ID  |
| boardId | String | **可选**切换文件并跳转到这个白板页  |
| stepIndex | Number | **可选**跳转到白板页并切换到这个动画  |

#### 警告
该接口仅可用于文件切换，如果传入的 fileId 为当前文件 ID，SDK 会忽略其它参数，不做任何操作。 

>? 文件 ID 为必填项，为 null 或空字符串将导致文件切换失败。 


### getCurrentFile
获取当前文件 ID 
``` Javascript
String getCurrentFile()
```
#### 返回
当前文件ID 


### getFileInfo
获取白板中指定文件的文件信息 
``` Javascript
TEduBoardFileInfo getFileInfo(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | **必填**要获取信息的文件 ID  |

#### 返回
文件信息 


### getFileInfoList
获取白板中上传的所有文件的文件信息列表 
``` Javascript
Array getFileInfoList()
```
#### 返回
文件信息列表 


### getFileBoardList
获取指定文件的白板 ID 列表 
``` Javascript
Array getFileBoardList(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | **必填**文件 ID  |

#### 返回
白板 ID列表 


### getThumbnailImages
获取指定文件的缩略图，不支持默认文件（fileId=#DEFAULT） 
``` Javascript
Array getThumbnailImages(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | **必填**文件 ID  |

#### 返回
缩略图 URL 列表 

>?用户在调用 rest api 请求转码时，需要带上 "thumbnail_resolution" 参数，开启缩略图功能，否则返回的缩略图 url 无效。 


### clearFileDraws
清空指定文件的所有白板涂鸦 
``` Javascript
void clearFileDraws(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | **必填**文件 ID  |



