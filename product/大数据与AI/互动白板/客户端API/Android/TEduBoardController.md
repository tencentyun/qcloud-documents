## TEduBoardController
白板控制器 

## 创建销毁实例

### TEduBoardController
创建白板控制类实例 
``` Java
TEduBoardController(Context context)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| context | Context | 应用程序的上下文环境  |



## 设置 TEduBoardCallback 回调

### addCallback
设置事件回调监听 
``` Java
void addCallback(TEduBoardCallback callback)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| callback | TEduBoardCallback | 事件回调监听  |

#### 警告
建议在Init之前调用该方法以支持错误处理 


### removeCallback
删除事件回调监听 
``` Java
void removeCallback(TEduBoardCallback callback)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| callback | TEduBoardCallback | 事件回调监听  |



## 基本流程接口

### init
初始化白板 
``` Java
void init(TEduBoardAuthParam authParam, int roomId, final TEduBoardInitParam initParam)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| authParam | TEduBoardAuthParam | 授权参数  |
| roomId | int | 课堂ID  |
| initParam | final TEduBoardInitParam | 可选参数，指定用于初始化白板的一系列属性值  |

#### 警告
使用腾讯云IMSDK进行实时数据同步时，只支持一个白板实例，创建多个白板实例可能导致涂鸦状态异常

#### 介绍
可用 initParam.timSync 指定是否使用腾讯云IMSDK进行实时数据同步 initParam.timSync == true 时，会尝试反射调用腾讯云IMSDK作为信令通道进行实时数据收发（只实现消息收发，初始化、进房等操作需要用户自行实现），目前仅支持IMSDK 4.3.118及以上版本 


### getBoardRenderView
获取白板渲染View 
``` Java
View getBoardRenderView()
```
#### 返回
白板渲染View 

#### 警告
收到onTEBBoardInit回调之前调用该接口无效

#### 介绍
在调用此接口获取View后，加入到视图树中后，在结束时需要removeView 


### refresh
对白板刷新 
``` Java
void refresh()
```
#### 返回
毫秒级时间戳 


### addSyncData
添加白板同步数据 
``` Java
void addSyncData(String data)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | String | 接收到的房间内其他人发送的同步数据 |

#### 介绍
该接口用于多个白板间的数据同步，使用内置IM作为信令通道时，不需要调用该接口 


### setDataSyncEnable
设置白板是否开启数据同步 
``` Java
void setDataSyncEnable(boolean enable)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | boolean | 是否开启 |

#### 介绍
白板创建后默认开启数据同步，关闭数据同步，本地的所有白板操作不会同步到远端和服务器 


### isDataSyncEnable
获取白板是否开启数据同步 
``` Java
boolean isDataSyncEnable()
```
#### 返回
是否开启数据同步，true 表示开启，false 表示关闭 


### reset
重置白板 
``` Java
void reset()
```
#### 介绍
调用该接口后将会删除所有的白板页和文件 


### getSyncTime
获取同步时间戳 
``` Java
long getSyncTime()
```
#### 返回
毫秒级同步时间戳 


### syncRemoteTime
同步远端时间戳 
``` Java
void syncRemoteTime(String userId, long timestamp)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| userId | String | 远端用户ID  |
| timestamp | long | 远端用户毫秒级同步时间戳  |


### getVersion
获取SDK版本号 
``` Java
static String getVersion()
```
#### 返回
SDK版本号 



## 涂鸦相关接口

### setDrawEnable
设置白板是否允许涂鸦 
``` Java
void setDrawEnable(boolean enable)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | boolean | 是否允许涂鸦，true 表示白板可以涂鸦，false 表示白板不能涂鸦 |

#### 介绍
白板创建后默认为允许涂鸦状态 


### isDrawEnable
获取白板是否允许涂鸦 
``` Java
boolean isDrawEnable()
```
#### 返回
是否允许涂鸦，true 表示白板可以涂鸦，false 表示白板不能涂鸦 


### setAccessibleUsers
设置允许操作哪些用户绘制的图形 
``` Java
void setAccessibleUsers(List< String > users)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| users | List< String > | 指定允许操作的用户集，为null表示不加限制 |

#### 介绍
该接口会产生以下影响：
1. ERASER 工具只能擦除users参数列出的用户绘制的涂鸦，无法擦除其他人绘制的涂鸦
2. POINTSELECT、SELECT 工具只能选中users参数列出的用户绘制的涂鸦，无法选中其他人绘制的涂鸦
3. clear 接口只能用于清空选中涂鸦以及users参数列出的用户绘制的涂鸦，无法清空背景及其他人绘制的涂鸦
4. 白板包含的其他功能未在本列表明确列出者都可以确定不受本接口影响 


### setGlobalBackgroundColor
设置所有白板的背景色 
``` Java
void setGlobalBackgroundColor(TEduBoardColor color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | TEduBoardColor | 要设置的全局背景色 |

#### 介绍
调用该接口将导致所有白板的背景色发生改变 新创建白板的默认背景色取全局背景色 


### getGlobalBackgroundColor
获取白板全局背景色 
``` Java
TEduBoardColor getGlobalBackgroundColor()
```
#### 返回
全局背景色 


### setBackgroundColor
设置当前白板页的背景色 
``` Java
void setBackgroundColor(TEduBoardColor color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | TEduBoardColor | 要设置的背景色 |

#### 介绍
白板页创建以后的默认背景色由SetDefaultBackgroundColor接口设定 


### getBackgroundColor
获取当前白板页的背景色 
``` Java
TEduBoardColor getBackgroundColor()
```
#### 返回
当前白板页的背景色 


### setToolType
设置要使用的白板工具 
``` Java
void setToolType(int type)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| type | int | 要设置的白板工具  |


### getToolType
获取正在使用的白板工具 
``` Java
int getToolType()
```
#### 返回
正在使用的白板工具 


### setCursorIcon
自定义白板工具鼠标样式 
``` Java
void setCursorIcon(int type, TEduBoardCursorIcon icon)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| type | int | 要设置鼠标样式的白板工具类型  |
| icon | TEduBoardCursorIcon | 要设置的鼠标样式  |


### setBrushColor
设置画笔颜色 
``` Java
void setBrushColor(TEduBoardColor color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | TEduBoardColor | 要设置的画笔颜色 |

#### 介绍
画笔颜色用于所有涂鸦绘制 


### getBrushColor
获取画笔颜色 
``` Java
TEduBoardColor getBrushColor()
```
#### 返回
画笔颜色 


### setBrushThin
设置画笔粗细 
``` Java
void setBrushThin(int thin)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| thin | int | 要设置的画笔粗细 |

#### 介绍
画笔粗细用于所有涂鸦绘制，实际像素值取值(thin * 白板的高度 / 10000)px，如果结果小于1px，则涂鸦的线条会比较虚 


### getBrushThin
获取画笔粗细 
``` Java
int getBrushThin()
```
#### 返回
画笔粗细 


### setTextColor
设置文本颜色 
``` Java
void setTextColor(TEduBoardColor color)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | TEduBoardColor | 要设置的文本颜色  |


### getTextColor
获取文本颜色 
``` Java
TEduBoardColor getTextColor()
```
#### 返回
文本颜色 


### setTextSize
设置文本大小 
``` Java
void setTextSize(int size)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| size | int | 要设置的文本大小 |

#### 介绍
实际像素值取值(size * 白板的高度 / 10000)px 


### getTextSize
获取文本大小 
``` Java
int getTextSize()
```
#### 返回
文本大小 


### setTextStyle
设置文本样式 
``` Java
void setTextStyle(int style)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| style | int | 要设置的文本样式  |


### getTextStyle
获取文本样式 
``` Java
int getTextStyle()
```
#### 返回
文本样式 


### clear
清空当前白板页涂鸦 
``` Java
void clear(boolean clearBackground)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| clearBackground | boolean | 是否同时清空背景色以及背景图片  |


### clear
清空当前白板页涂鸦 
``` Java
void clear(boolean clearBackground, boolean clearSelectedOnly)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| clearBackground | boolean | 是否同时清空背景色以及背景图片  |
| clearSelectedOnly | boolean | 是否只清除选中部分涂鸦  |

#### 警告
目前不支持清除选中部分的同时清除背景 


### setLineStyle
设置直线样式 
``` Java
void setLineStyle(TEduBoardLineStyle style)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| style | TEduBoardLineStyle | 要设置的直线样式  |


### getLineStyle
获取直线样式 
``` Java
TEduBoardLineStyle getLineStyle()
```
#### 返回
直线样式 


### setOvalDrawMode
设置椭圆绘制模式 
``` Java
void setOvalDrawMode(int drawMode)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| drawMode | int | 要设置的椭圆绘制模式  |


### getOvalDrawMode
获取椭圆绘制模式 
``` Java
int getOvalDrawMode()
```
#### 返回
椭圆绘制模式 


### setBackgroundImage
设置当前白板页的背景图片 
``` Java
void setBackgroundImage(String url, int mode)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | String | 要设置的背景图片URL，编码格式为UTF8  |
| mode | int | 要使用的图片填充对齐模式 |

#### 介绍
当URL是一个有效的本地文件地址时，该文件会被自动上传到COS 


### setBackgroundH5
设置当前白板页的背景H5页面 
``` Java
void setBackgroundH5(String url)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | String | 要设置的背景H5页面URL |

#### 介绍
该接口与SetBackgroundImage接口互斥 


### undo
撤销当前白板页上一次动作 
``` Java
void undo()
```

### redo
重做当前白板页上一次撤销 
``` Java
void redo()
```


## 白板页操作接口

### addBoard
增加一页白板 
``` Java
String addBoard(String url)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | String | 要使用的背景图片URL，编码格式为UTF8，为null表示不指定背景图片  |

#### 返回
白板ID 

#### 警告
白板页会被添加到默认文件（文件ID为::DEFAULT)，自行上传的文件无法添加白板页 


### deleteBoard
删除一页白板 
``` Java
void deleteBoard(String boardId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | String | 要删除的白板ID，为null表示删除当前页  |

#### 警告
只允许删除默认文件（文件ID为::DEFAULT）内的白板页，且默认白板页（白板ID为::DEFAULT）无法删除 


### prevStep
上一步 每个Step对应PPT的一个动画效果，若当前没有已展示的动画效果，则该接口调用会导致向前翻页 
``` Java
void prevStep()
```

### nextStep
下一步 
``` Java
void nextStep()
```
#### 介绍
每个Step对应PPT的一个动画效果，若当前没有未展示的动画效果，则该接口调用会导致向后翻页 


### prevBoard
向前翻页 
``` Java
void prevBoard()
```
#### 介绍
若当前白板页为当前文件的第一页，则该接口调用无效 


### nextBoard
向后翻页 
``` Java
void nextBoard()
```
#### 介绍
若当前白板页为当前文件的最后一页，则该接口调用无效 


### gotoBoard
跳转到指定白板页 
``` Java
void gotoBoard(String boardId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | String | 要跳转到的白板页ID |

#### 介绍
允许跳转到任意文件的白板页 


### prevBoard
向前翻页 
``` Java
void prevBoard(boolean resetStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| resetStep | boolean | 指定翻到指定页以后是否重置PPT动画步数 |

#### 介绍
若当前白板页为当前文件的第一页，则该接口调用无效 


### nextBoard
向后翻页 
``` Java
void nextBoard(boolean resetStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| resetStep | boolean | 指定翻到指定页以后是否重置PPT动画步数 |

#### 介绍
若当前白板页为当前文件的最后一页，则该接口调用无效 


### gotoBoard
跳转到指定白板页 
``` Java
void gotoBoard(String boardId, boolean resetStep)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | String | 要跳转到的白板页ID  |
| resetStep | boolean | 指定翻到指定页以后是否重置PPT动画步数 |

#### 介绍
允许跳转到任意文件的白板页 


### getCurrentBoard
获取当前白板页ID 
``` Java
String getCurrentBoard()
```
#### 返回
当前白板页ID 


### getBoardList
获取所有文件的白板列表 
``` Java
List<String> getBoardList()
```
#### 返回
所有文件的白板列表 


### setBoardRatio
设置当前白板页宽高比 
``` Java
void setBoardRatio(String ratio)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| ratio | String | 要设置的白板宽高比 |

#### 介绍
格式如: "4:3"、"16:9" 


### getBoardRatio
获取当前白板页宽高比 
``` Java
String getBoardRatio()
```
#### 返回
白板宽高比，格式与SetBoardRatio接口参数格式一致 


### setBoardScale
设置当前白板页缩放比例 
``` Java
void setBoardScale(int scale)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| scale | int | 要设置的白板缩放比例 |

#### 介绍
支持范围: [100，300]，实际缩放比为: scale/100 


### getBoardScale
获取当前白板页缩放比例 
``` Java
int getBoardScale()
```
#### 返回
白板缩放比例，格式与SetBoardScale接口参数格式一致 


### setBoardContentFitMode
设置白板内容自适应模式 
``` Java
void setBoardContentFitMode(int mode)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| mode | int | 要设置的白板内容自适应模式 |

#### 介绍
设置自适应模式后会影响所有后续白板内容操作,受影响接口包括：AddTranscodeFile 


### getBoardContentFitMode
获取白板内容自适应模式 
``` Java
int getBoardContentFitMode()
```
#### 返回
白板内容自适应模式 



## 文件操作接口

### applyFileTranscode
发起文件转码请求 
``` Java
void applyFileTranscode(final String path, final TEduBoardTranscodeConfig config)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | final String | 要转码的文件路径，编码格式为UTF8  |
| config | final TEduBoardTranscodeConfig | 转码参数  |

#### 警告
本接口设计用于在接入阶段快速体验转码功能，原则上不建议在生产环境中使用，生产环境中的转码请求建议使用后台服务接口发起 

#### 介绍
支持 PPT、PDF、Word文件转码 PPT文档默认转为H5动画，能够还原PPT原有动画效果，其它文档转码为静态图片 PPT动画转码耗时约1秒/页，所有文档的静态转码耗时约0.5秒/页 转码进度和结果将会通过onTEBFileTranscodeProgress回调返回，详情参见该回调说明文档 


### getFileTranscodeProgress
主动查询文件转码进度 
``` Java
void getFileTranscodeProgress(final String taskId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| taskId | final String | 通过onTEBFileTranscodeProgress回调拿到的转码任务taskId  |

#### 警告
该接口仅用于特殊业务场景下主动查询文件转码进度，调用ApplyFileTranscode后，SDK内部将会自动定期触发onTEBFileTranscodeProgress回调，正常情况下您不需要主动调用此接口 

#### 介绍
转码进度和结果将会通过onTEBFileTranscodeProgress回调返回，详情参见该回调说明文档 


### addTranscodeFile
添加转码文件 
``` Java
String addTranscodeFile(final TEduBoardTranscodeFileResult result)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| result | final TEduBoardTranscodeFileResult | 文件转码结果  |

#### 返回
文件ID 

#### 警告
当传入文件的URL重复时，文件ID返回为空字符串 
在收到对应的onTEBAddTranscodeFile回调前，无法用返回的文件ID查询到文件信息 

#### 介绍
本接口只处理传入参数结构体的title、resolution、url、pages字段 调用该接口后，SDK会在后台进行文件加载，期间用户可正常进行其它操作，加载成功或失败后会触发相应回调 文件加载成功后，将自动切换到该文件 


### deleteFile
删除文件 
``` Java
void deleteFile(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 要删除的文件ID |

#### 介绍
文件ID为nullptr时表示当前文件，默认文件无法删除 


### switchFile
切换文件 
``` Java
void switchFile(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 要切换到的文件ID  |

>? 文件ID为必填项，为null或空字符串将导致文件切换失败 


### switchFile
切换文件 
``` Java
void switchFile(String fileId, String boardId, int stepIndex)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 要切换到的文件ID  |
| boardId | String | 切换文件并跳转到这个白板页  |
| stepIndex | int | 跳转到白板页并切换到这个动画  |

#### 警告
该接口仅可用于文件切换，如果传入的fileId为当前文件ID，SDK会忽略其它参数，不做任何操作 

>? 文件ID为必填项，为null或空字符串将导致文件切换失败 


### getCurrentFile
获取当前文件ID 
``` Java
String getCurrentFile()
```
#### 返回
当前文件ID 


### getFileInfoList
获取白板中上传的所有文件的文件信息列表 
``` Java
List<TEduBoardFileInfo> getFileInfoList()
```
#### 返回
文件信息列表 


### getFileInfo
获取白板中指定文件的文件信息 
``` Java
TEduBoardFileInfo getFileInfo(String fid)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fid | String |  |

#### 返回
文件信息 


### getFileBoardList
获取指定文件的白板ID列表 
``` Java
List<String> getFileBoardList(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 文件ID  |

#### 返回
白板ID列表 


### clearFileDraws
清空指定文件的所有白板涂鸦 
``` Java
void clearFileDraws(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 文件ID  |


### getThumbnailImages
获取指定文件的缩略图，不支持默认文件（fileId=#DEFAULT） 
``` Java
List<String> getThumbnailImages(String fileId)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | String | 文件ID  |

#### 返回
缩略图URL列表 

>? 用户在调用rest api请求转码时，需要带上 "thumbnail_resolution" 参数，开启缩略图功能，否则返回的缩略图url无效 





