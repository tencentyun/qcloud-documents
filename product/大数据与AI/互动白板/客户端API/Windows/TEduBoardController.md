## 互动白板控制器

互动白板控制器，请参考 [互动白板控制器](https://doc.qcloudtiw.com/win32/latest/class_t_edu_board_controller.html) 文档

## 创建销毁实例

### CreateTEduBoardController
创建白板控制类实例 
``` C++
EDUSDK_API TEduBoardController* CreateTEduBoardController(bool disableCefInit=false, const char *cefRenderPath=nullptr)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| disableCefInit | bool | 是否禁用 CEF 框架初始化，通常传默认值即可  |
| cefRenderPath | const char * | 使用 SDK 内部的 CEF 初始化时，用于指定自定义 Render 进程可执行程序的路径，UTF8 编码，为空或 nullptr 表示使用 SDK 内置 Render 进程  |

#### 返回
白板控制类实例指针 

#### 警告
该接口必须在主线程调用 

>? 由于 SDK 基于 CEF 框架(BSD-licensed)实现，若您的程序中也使用了 CEF 框架，可能会存在冲突，我们为您提供了冲突解决方案：
> 1. 选用以下两种方法中的一种来启用自己的 Render 进程
> 	- 令 disableCefInit = false，cefRenderPath 指向您自己的 Render 进程
> 	- 令 disableCefInit = true，自行实现 CEF 初始化
> 2. 按下面说明，在您的 Render 进程内调用 SDK 的 RenderProcessHandler
> 	- Render 进程启动后调用接口获取一个 sdkHandler 实例，CefRefPtr&lt; CefRenderProcessHandler&gt; sdkHandler = (CefRenderProcessHandler * )GetTEduBoardRenderProcessHandler();
> 	- 在 Render 进程的 CefApp 中重写 GetRenderProcessHandler 方法，每次都返回以上 sdkHandler
> 	- 若您需要自定义 CefRenderProcessHandler，第二步可返回自定义 Handler，然后在自定义 Handler 的下面几个方法中，调用 sdkHandler 的对应方法
> 		- OnBrowserCreated
> 		- OnBrowserDestroyed
> 		- OnContextCreated 


### DestroyTEduBoardController
销毁白板控制类 
``` C++
EDUSDK_API void DestroyTEduBoardController(TEduBoardController **ppBoardController)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| ppBoardController | TEduBoardController ** | 指向白板控制类指针 |

#### 介绍
ppBoardController 指针会被自动置空 


### ClearTEduBoardSDKEnv
清理白板 SDK 环境，在不使用白板后调用以释放资源 
``` C++
EDUSDK_API void ClearTEduBoardSDKEnv()
```
#### 警告
该接口必须在主线程调用 

>?请在确保不再使用白板功能时才调用该接口（建议在应用程序退出前调用），调用了该接口之后，CreateTEduBoardController 接口不再有效。 



## 日志相关接口

### GetTEduBoardVersion
获取 SDK 版本号 
``` C++
EDUSDK_API const char* GetTEduBoardVersion()
```
#### 返回
SDK 版本号

#### 介绍
返回值内存由 SDK 内部管理，用户不需要自己释放 


### SetTEduBoardLogFileDir
设置白板日志文件存储目录路径 
``` C++
EDUSDK_API bool SetTEduBoardLogFileDir(const char *logDir)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| logDir | const char * | 要设置的白板日志文件存储目录路径，UTF8 编码，为空或 nullptr 表示使用默认路径  |

### SetLogLevel
设置输出日志级别 
``` C++
EDUSDK_API bool SetLogLevel(const uint32_t *level)
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| SetLogLevel | const uint32_t * | 日志级别  |

#### 返回
设置白板日志文件存储目录是否成功 

#### 警告
该接口必须要在第一次调用 CreateTEduBoardController 之前调用才有效，否则将会失败

#### 介绍

- 默认路径，Windows下为："%AppData%/../Local/TEduBoard"
- 默认路径，Linux下为："~/TEduBoard" 



## 高级功能接口

### EnableTEduBoardOffscreenRender
启用白板离屏渲染 
``` C++
EDUSDK_API bool EnableTEduBoardOffscreenRender(uint32_t maxFps=30)
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| maxFps | uint32_t | 离屏渲染的最大帧率，取值[1, 60]  |

#### 返回
启用离屏渲染是否成功 

#### 警告
该接口必须要在第一次调用 CreateTEduBoardController 之前调用才有效，否则将会失败

#### 介绍
启用离屏渲染时，SDK 不再创建白板 VIEW，而是通过 onTEBOffscreenPaint 回调接口将白板离屏渲染的像素数据抛出 


### EnableTEduBoardCrashReport
启用白板 Crash 上报 
``` C++
EDUSDK_API bool EnableTEduBoardCrashReport()
```
#### 返回
启用白板 Crash 上报是否成功 

#### 警告
该接口必须要在第一次调用 CreateTEduBoardController 之前调用才有效，否则将会失败 


### GetTEduBoardRenderProcessHandler
获取 SDK 内部的 CefRenderProcessHandler 
``` C++
EDUSDK_API void* GetTEduBoardRenderProcessHandler()
```
#### 返回
SDK 内部的 CefRenderProcessHandler 

#### 介绍
本接口详细使用方法参见 CreateTEduBoardController 接口说明 



## TEduBoardController
白板控制器 

## 设置 TEduBoardCallback 回调

### AddCallback
设置事件回调监听 
``` C++
virtual void AddCallback(TEduBoardCallback *callback)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| callback | TEduBoardCallback * | 事件回调监听  |

#### 警告
建议在 Init 之前调用该方法以支持错误处理 


### RemoveCallback
删除事件回调监听 
``` C++
virtual void RemoveCallback(TEduBoardCallback *callback)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| callback | TEduBoardCallback * | 事件回调监听  |



## 基本流程接口

### Init
初始化白板 
``` C++
virtual void Init(const TEduBoardInitParam &initParam=TEduBoardInitParam())=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| initParam | const TEduBoardInitParam & | 可选参数，指定用于初始化白板的一系列属性值  |

#### 警告
使用腾讯云 IMSDK 进行实时数据同步时，只支持一个白板实例，创建多个白板实例可能导致涂鸦状态异常

#### 介绍
可用 initParam.timSync 指定是否使用腾讯云 IMSDK 进行实时数据同步 initParam.timSync == true 时，会尝试反射调用腾讯云 IMSDK 作为信令通道进行实时数据收发（只实现消息收发，初始化、进房等操作需要用户自行实现），目前仅支持 IMSDK 4.3.118 及以上版本 


### GetBoardRenderView
获取白板渲染 View 
``` C++
virtual WINDOW_HANDLE GetBoardRenderView()=0
```
#### 返回
白板渲染 View 


### Refresh
刷新当前页白板，触发 onTEBRefresh 回调 
``` C++
virtual void Refresh()=0
```
#### 警告
如果当前白板包含 PPT/H5/图片/视频时，刷新白板将会触发对应的回调 


### SyncAndReload
同步本地发送失败的数据到远端并刷新本地数据 
``` C++
virtual void SyncAndReload()=0
```
#### 警告
Reload 等同于重新加载历史数据，会触发白板初始化时除 onTEBInit 之外的所有回调。 

#### 介绍
- 接口用途：此接口主要用于网络恢复后，同步本地数据到远端，拉取远端数据到本地 
- 调用时机：在网络恢复后调用 
- 使用限制：如果历史数据还没有加载完成，则不允许重复调用，否则回调告警 TEDU_BOARD_WARNING_ILLEGAL_OPERATION 


### AddSyncData
添加白板同步数据 
``` C++
virtual void AddSyncData(const char *data)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| data | const char * | 接收到的房间内其他人发送的同步数据 |

#### 介绍
该接口用于多个白板间的数据同步，使用内置 IM 作为信令通道时，不需要调用该接口 


### SetDataSyncEnable
设置白板是否开启数据同步 
``` C++
virtual void SetDataSyncEnable(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 是否开启 |

#### 介绍
白板创建后默认开启数据同步，关闭数据同步，本地的所有白板操作不会同步到远端和服务器 


### IsDataSyncEnable
获取白板是否开启数据同步 
``` C++
virtual bool IsDataSyncEnable()=0
```
#### 返回
是否开启数据同步，true 表示开启，false 表示关闭 


### Reset
重置白板 
``` C++
virtual void Reset()=0
```
#### 介绍
调用该接口后将会删除所有的白板页和文件 


### SetBoardRenderViewPos
设置白板渲染 View 的位置和大小 
``` C++
virtual void SetBoardRenderViewPos(int32_t x, int32_t y, uint32_t width, uint32_t height)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| x | int32_t | 要设置的白板渲染 View 的位置 X 分量  |
| y | int32_t | 要设置的白板渲染 View 的位置 Y 分量  |
| width | uint32_t | 要设置的白板渲染 View 的宽度  |
| height | uint32_t | 要设置的白板渲染 View 的高度 |

#### 介绍
白板渲染 View 有父窗口时，(x, y) 指定相对其父窗口的位置 


### GetSyncTime
获取同步时间戳 
``` C++
virtual uint64_t GetSyncTime()=0
```
#### 返回
毫秒级同步时间戳 


### SyncRemoteTime
同步远端时间戳 
``` C++
virtual void SyncRemoteTime(const char *userId, uint64_t timestamp)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| userId | const char * | 远端用户 ID  |
| timestamp | uint64_t | 远端用户毫秒级同步时间戳  |


### SetSystemCursorEnable
是否启用原生系统光标 
``` C++
virtual void SetSystemCursorEnable(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 启用或禁用，默认禁用  |


### AddBackupDomain
添加备用域名 
``` C++
virtual void AddBackupDomain(const char *domain, const char *backup, uint32_t priority=0)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| domain | const char * | 要添加备用域名的主域名  |
| backup | const char * | 要添加的备用域名  |
| priority | uint32_t | 备用域名优先级，数字越大优先级越高 |

#### 介绍
主备域名均需要包含协议类型（支持 http/https） 当使用主域名访问资源超时后，按优先级逐个尝试使用备用域名去访问，资源访问超时时间默认为5秒 多次调用此接口，可以为同一个主域名添加多个备用域名，重复添加相同的备用域名会被忽略 


### RemoveBackupDomain
删除备用域名 
``` C++
virtual void RemoveBackupDomain(const char *domain, const char *backup)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| domain | const char * | 要删除备用域名的主域名  |
| backup | const char * | 要删除的备用域名，nullptr 或空字符串表示删除主域名对应的所有备用域名  |


### SetProxyServer
设置服务的代理服务器 
``` C++
virtual void SetProxyServer(const char *settingStr)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| settingStr | const char * | 代理服务器配置字符串，字符串内容为一个 JSON 对象，格式参考如下：介绍 |

#### 介绍
{ '服务类型': '代理服务器地址', ... }


### CallExperimentalAPI
调用白板实验性接口 
``` C++
virtual const char* CallExperimentalAPI(const char *apiExp)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| apiExp | const char * | 要执行的白板相关 JS 代码  |

#### 返回
JS 执行后的返回值转换而来的字符串 



## 离屏渲染输入事件相关接口

### SendKeyEvent
发送键盘事件到白板 
``` C++
virtual void SendKeyEvent(const TEduBoardKeyEvent &event)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| event | const TEduBoardKeyEvent & | 要发送的键盘事件  |


### SendMouseClickEvent
发送鼠标点击事件到白板 
``` C++
virtual void SendMouseClickEvent(const TEduBoardMouseEvent &event, TEduBoardMouseButtonType type, bool mouseUp, int clickCount)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| event | const TEduBoardMouseEvent & | 要发送的鼠标事件  |
| type | TEduBoardMouseButtonType | 鼠标按键类型  |
| mouseUp | bool | 鼠标是否弹起  |
| clickCount | int | 点击次数  |


### SendMouseMoveEvent
发送鼠标移动事件到白板 
``` C++
virtual void SendMouseMoveEvent(const TEduBoardMouseEvent &event, bool mouseLeave)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| event | const TEduBoardMouseEvent & | 要发送的鼠标事件  |
| mouseLeave | bool | 鼠标是否离开白板  |


### SendMouseWheelEvent
发送鼠标滚轮事件到白板 
``` C++
virtual void SendMouseWheelEvent(const TEduBoardMouseEvent &event, int deltaX, int deltaY)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| event | const TEduBoardMouseEvent & | 要发送的鼠标事件  |
| deltaX | int | 滚轮在X方向的移动增量  |
| deltaY | int | 滚轮在Y方向的移动增量  |


### SendTouchEvent
发送触摸事件到白板 
``` C++
virtual void SendTouchEvent(const TEduBoardTouchEvent &event)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| event | const TEduBoardTouchEvent & | 要发送的触摸事件  |



## 涂鸦相关接口

### SetDrawEnable
设置白板是否允许涂鸦 
``` C++
virtual void SetDrawEnable(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 是否允许涂鸦，true 表示白板可以涂鸦，false 表示白板不能涂鸦 |

#### 介绍
白板创建后默认为允许涂鸦状态 


### IsDrawEnable
获取白板是否允许涂鸦 
``` C++
virtual bool IsDrawEnable()=0
```
#### 返回
是否允许涂鸦，true 表示白板可以涂鸦，false 表示白板不能涂鸦 


### SetHandwritingEnable
设置白板是否开启笔锋特性 
``` C++
virtual void SetHandwritingEnable(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 是否开启笔锋，true 表示开启，false 表示关闭 |

#### 介绍
白板创建后默认为关闭 


### IsHandwritingEnable
获取白板是否开启笔锋特性 
``` C++
virtual bool IsHandwritingEnable()=0
```
#### 返回
是否开启笔锋特性 


### SetEraseLayerLimit
设置橡皮擦单次擦除图层数量 
``` C++
virtual void SetEraseLayerLimit(uint32_t limit=0)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| limit | uint32_t | 擦除图层数量，默认为0，即不限制图层数量 |

#### 介绍
单次擦除：鼠标/手指按下 > 鼠标/手指移动 > 鼠标/手指抬起。 


### SetEraseLayerType
限制橡皮擦可擦除的白板元素类型 
``` C++
virtual void SetEraseLayerType(const TEduBoardErasableElementType *typeArr=nullptr, uint32_t typeArrCount=0)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| typeArr | const TEduBoardErasableElementType * | 限制可擦除的白板元素类型数组，默认为 nullptr 则不限制元素类型  |
| typeArrCount | uint32_t | 要限制的可擦除的白板元素类型数量  |


### SetAccessibleUsers
设置允许操作哪些用户绘制的图形 
``` C++
virtual void SetAccessibleUsers(char **users, uint32_t userCount, TEduBoardAccessibleOperation *operatorType, uint32_t typeCount)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| users | char ** | 指定允许操作的用户集，为 nullptr 表示不加限制  |
| userCount | uint32_t | 指定 users 参数包含的用户个数  |
| operatorType | TEduBoardAccessibleOperation * | 用户操作类型  |
| typeCount | uint32_t | 操作类型个数 该接口会产生以下影响：<br>1. ERASER 工具只能擦除 users 参数列出的用户绘制的涂鸦，无法擦除其他人绘制的涂鸦<br>2. POINTSELECT、SELECT 工具只能选中 users 参数列出的用户绘制的涂鸦，无法选中其他人绘制的涂鸦<br>3. clear 接口只能用于清空选中涂鸦以及 users 参数列出的用户绘制的涂鸦，无法清空背景及其他人绘制的涂鸦<br>4. 白板包含的其他功能未在本列表明确列出者都可以确定不受本接口影响  |


### SetGlobalBackgroundColor
设置所有白板的背景色 
``` C++
virtual void SetGlobalBackgroundColor(const TEduBoardColor &color)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | const TEduBoardColor & | 要设置的全局背景色 |

#### 介绍
调用该接口将导致所有白板的背景色发生改变 新创建白板的默认背景色取全局背景色 


### GetGlobalBackgroundColor
获取白板全局背景色 
``` C++
virtual TEduBoardColor GetGlobalBackgroundColor()=0
```

#### 返回
全局背景色 


### SetBackgroundColor
设置当前白板页的背景色 
``` C++
virtual void SetBackgroundColor(const TEduBoardColor &color)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | const TEduBoardColor & | 要设置的背景色 |

#### 介绍
白板页创建以后的默认背景色由 SetDefaultBackgroundColor 接口设定 


### GetBackgroundColor
获取当前白板页的背景色 
``` C++
virtual TEduBoardColor GetBackgroundColor()=0
```

#### 返回
当前白板页的背景色 


### SetToolType
设置要使用的白板工具 
``` C++
virtual void SetToolType(TEduBoardToolType type)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| type | TEduBoardToolType | 要设置的白板工具  |


### GetToolType
获取正在使用的白板工具 
``` C++
virtual TEduBoardToolType GetToolType()=0
```

#### 返回
正在使用的白板工具 


### SetToolTypeTitle
设置画笔和激光笔工具提示语 
``` C++
virtual void SetToolTypeTitle(const char *title, const TEduBoardToolTypeTitleStyle *style, TEduBoardToolType type)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| title | const char * | 提示语  |
| style | const TEduBoardToolTypeTitleStyle * | 提示语样式，如果为 nullptr，则使用默认样式  |
| type | TEduBoardToolType |  |


### SetCursorIcon
自定义白板工具鼠标样式 
``` C++
virtual void SetCursorIcon(TEduBoardToolType type, const TEduBoardCursorIcon &icon)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| type | TEduBoardToolType | 要设置鼠标样式的白板工具类型  |
| icon | const TEduBoardCursorIcon & | 要设置的鼠标样式  |


### SetBrushColor
设置画笔颜色 
``` C++
virtual void SetBrushColor(const TEduBoardColor &color)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | const TEduBoardColor & | 要设置的画笔颜色 |

#### 介绍
画笔颜色用于所有涂鸦绘制 


### GetBrushColor
获取画笔颜色 
``` C++
virtual TEduBoardColor GetBrushColor()=0
```

#### 返回
画笔颜色 


### SetBrushThin
设置画笔粗细 
``` C++
virtual void SetBrushThin(uint32_t thin)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| thin | uint32_t | 要设置的画笔粗细 |

#### 介绍
画笔粗细用于所有涂鸦绘制，实际像素值取值(thin * 白板的高度 / 10000)px，如果结果小于1px，则涂鸦的线条会比较虚 


### GetBrushThin
获取画笔粗细 
``` C++
virtual uint32_t GetBrushThin()=0
```

#### 返回
画笔粗细 


### SetTextColor
设置文本颜色 
``` C++
virtual void SetTextColor(const TEduBoardColor &color)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| color | const TEduBoardColor & | 要设置的文本颜色  |


### GetTextColor
获取文本颜色 
``` C++
virtual TEduBoardColor GetTextColor()=0
```

#### 返回
文本颜色 


### SetTextSize
设置文本大小 
``` C++
virtual void SetTextSize(uint32_t size)=0
```

#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| size | uint32_t | 要设置的文本大小 |

#### 介绍
实际像素值取值(size * 白板的高度 / 10000)px 


### GetTextSize
获取文本大小 
``` C++
virtual uint32_t GetTextSize()=0
```
#### 返回
文本大小 


### SetTextStyle
设置文本样式 
``` C++
virtual void SetTextStyle(TEduBoardTextStyle style)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| style | TEduBoardTextStyle | 要设置的文本样式  |


### GetTextStyle
获取文本样式 
``` C++
virtual TEduBoardTextStyle GetTextStyle()=0
```
#### 返回
文本样式 


### SetLineStyle
设置直线样式 
``` C++
virtual void SetLineStyle(const TEduBoardLineStyle &style)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| style | const TEduBoardLineStyle & | 要设置的直线样式  |


### GetLineStyle
获取直线样式 
``` C++
virtual TEduBoardLineStyle GetLineStyle()=0
```
#### 返回
直线样式 


### SetOvalDrawMode
设置椭圆绘制模式 
``` C++
virtual void SetOvalDrawMode(TEduBoardOvalDrawMode drawMode)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| drawMode | TEduBoardOvalDrawMode | 要设置的椭圆绘制模式  |


### GetOvalDrawMode
获取椭圆绘制模式 
``` C++
virtual TEduBoardOvalDrawMode GetOvalDrawMode()=0
```
#### 返回
椭圆绘制模式 


### Clear
清空当前白板页涂鸦 
``` C++
virtual void Clear(bool clearBackground=false, bool clearSelectedOnly=false)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| clearBackground | bool | 是否同时清空背景色以及背景图片  |
| clearSelectedOnly | bool | 是否只清除选中部分涂鸦  |

#### 警告
目前不支持清除选中部分的同时清除背景 


### SetBackgroundImage
设置当前白板页的背景图片 
``` C++
virtual void SetBackgroundImage(const char *url, TEduBoardImageFitMode mode)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 要设置的背景图片 URL，编码格式为 UTF8  |
| mode | TEduBoardImageFitMode | 要使用的图片填充对齐模式 |

#### 介绍
当 URL 是一个有效的本地文件地址时，该文件会被自动上传到 COS 


### SetBackgroundH5
设置当前白板页的背景 H5 页面 
``` C++
virtual void SetBackgroundH5(const char *url)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 要设置的背景 H5 页面 URL |

#### 介绍
该接口与 SetBackgroundImage 接口互斥 


### Undo
撤销当前白板页上一次动作 
``` C++
virtual void Undo()=0
```

### Redo
重做当前白板页上一次撤销 
``` C++
virtual void Redo()=0
```

### 
重做当前白板页上一次撤销 
``` C++
virtual void Redo()=0
```

### setScrollBarVisible
设置白板滚动条是否可见 
``` C++
virtual void setScrollBarVisible(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | true 显示滚动条 false 不显示滚动条 |


## 白板页操作接口

### AddBoard
增加一页白板 
``` C++
virtual const char* AddBoard(const char *url=nullptr, const TEduBoardImageFitMode mode=TEDU_BOARD_IMAGE_FIT_MODE_CENTER, const TEduBoardBackgroundType type=TEDU_BOARD_BACKGROUND_IMAGE, bool needSwitch=true)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 要使用的背景图片 URL，编码格式为 UTF8，为 nullptr 表示不指定背景图片，只支持 https 协议的图片 URL  |
| mode | const TEduBoardImageFitMode | 要使用的图片填充对齐模式，当设置 URL 时有效 TEduBoardImageFitMode  |
| type | const TEduBoardBackgroundType | 背景类型 TEduBoardBackgroundType  |
| needSwitch | bool | 是否切换到添加的白板页 |

#### 返回
白板 ID 

#### 警告
白板页会被添加到默认文件（文件 ID 为::DEFAULT)，自行上传的文件无法添加白板页 触发 TEduBoard.EVEN.TEB_ADDBOARD 事件 返回值内存由 SDK 内部管理，用户不需要自己释放 


### AddImageElement
添加图片资源 
``` C++
virtual void AddImageElement(const char *url)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 要添加的图片元素 URL 地址，编码格式为 UTF8  |

#### 警告
该接口已废弃，请使用 AddElement 接口代替 


### AddElement
添加白板元素 
``` C++
virtual const char* AddElement(TEduBoardElementType type, TEduAddBoardBase *pTag, const TEduBoardElementOptions &options=TEduBoardElementOptions())=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| type | TEduBoardElementType | 元素类型，当设置 TEDU_BOARD_ELEMENT_IMAGE 时，等价于 addImageElement 方法  |
| pTag | TEduAddBoardBase * | 网页或者图片的 URL，只支持 https 协议的网址或者图片 URL，编码格式为 UTF8，为 nullptr 表示不指定 URL  |
| options | const TEduBoardElementOptions & | 元素参数  |

#### 返回
元素 ID 

#### 警告
（1）当 type = TEDU_BOARD_ELEMENT_IMAGE，支持 png、jpg、gif、svg 格式的本地和网络图片，当 URL 是一个有效的本地文件地址时，该文件会被自动上传到 COS，上传进度回调 onTEBFileUploadStatus 
（2）当 type = TEDU_BOARD_ELEMENT_CUSTOM_GRAPH，仅支持网络 URL，请与自定义图形工具 TEDU_BOARD_TOOL_TYPE_BOARD_CUSTOM_GRAPH 配合使用 
（3）当 type = TEDU_BOARD_ELEMENT_AUDIO 或 TEDU_BOARD_ELEMENT_GLOBAL_AUDIO，仅支持网络 URL 对应类型和子类对象的匹配：TEDU_BOARD_ELEMENT_MATH_GRAPH --> TEduAddBoardElementMathGraph TEDU_BOARD_ELEMENT_MATH_BOARD --> TEduAddBoardElementMathBoard 其他类型暂时对应-> TEduAddBoardElementUrl 


### RemoveElement
删除白板元素 
``` C++
virtual bool RemoveElement(const char *elementId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 元素 ID  |

#### 返回
删除操作是否成功 


### GetBoardElementList
获取白板中所有元素 
``` C++
virtual TEduBoardElementInfoList* GetBoardElementList(const char *boardId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 白板 ID，如果为空则获取当前白板所有元素  |

#### 返回
白板元素列表 


### DeleteBoard
删除一页白板 
``` C++
virtual void DeleteBoard(const char *boardId=nullptr)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 要删除的白板 ID，为 nullptr 表示删除当前页  |

#### 警告
只允许删除默认文件（文件 ID 为::DEFAULT）内的白板页，且默认白板页（白板 ID 为::DEFAULT）无法删除 


### PrevStep
上一步 每个 Step 对应 PPT 的一个动画效果，若当前没有已展示的动画效果，则该接口调用会导致向前翻页 
``` C++
virtual void PrevStep()=0
```

### NextStep
下一步 
``` C++
virtual void NextStep()=0
```
#### 介绍
每个 Step 对应 PPT 的一个动画效果，若当前没有未展示的动画效果，则该接口调用会导致向后翻页 


### PrevBoard
向前翻页 
``` C++
virtual void PrevBoard(bool resetStep=false)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| resetStep | bool | 指定翻到指定页以后是否重置 PPT 动画步数 |

#### 介绍
若当前白板页为当前文件的第一页，则该接口调用无效 


### NextBoard
向后翻页 
``` C++
virtual void NextBoard(bool resetStep=false)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| resetStep | bool | 指定翻到指定页以后是否重置 PPT 动画步数 |

#### 介绍
若当前白板页为当前文件的最后一页，则该接口调用无效 


### GotoBoard
跳转到指定白板页 
``` C++
virtual void GotoBoard(const char *boardId, bool resetStep=false)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 要跳转到的白板页 ID  |
| resetStep | bool | 指定翻到指定页以后是否重置 PPT 动画步数 |

#### 介绍
允许跳转到任意文件的白板页 


### GetCurrentBoard
获取当前白板页 ID 
``` C++
virtual const char* GetCurrentBoard()=0
```
#### 返回
当前白板页 ID

#### 介绍
返回值内存由 SDK 内部管理，用户不需要自己释放 


### GetBoardList
获取所有文件的白板列表 
``` C++
virtual TEduBoardStringList* GetBoardList()=0
```
#### 返回
所有文件的白板列表 

#### 警告
返回值不再使用时不需要自行 delete，但是务必调用其 release 方法以释放内存占用 


### SetBoardRatio
设置当前白板页宽高比 
``` C++
virtual void SetBoardRatio(const char *ratio)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| ratio | const char * | 要设置的白板宽高比 |

#### 介绍
格式如: "4:3"、"16:9" 


### GetBoardRatio
获取当前白板页宽高比 
``` C++
virtual const char* GetBoardRatio()=0
```
#### 返回
白板宽高比，格式与 SetBoardRatio 接口参数格式一致 


### SetBoardScale
设置当前白板页缩放比例 
``` C++
virtual void SetBoardScale(uint32_t scale)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| scale | uint32_t | 要设置的白板缩放比例 |

#### 介绍
支持范围: [100，1600]，实际缩放比为: scale/100 


### GetBoardScale
获取当前白板页缩放比例 
``` C++
virtual uint32_t GetBoardScale()=0
```
#### 返回
白板缩放比例，格式与 SetBoardScale 接口参数格式一致 


### SetFileScale
设置文件缩放比例 
``` C++
virtual void SetFileScale(const char *fileId, uint32_t scale)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件ID  |
| scale | uint32_t | 要设置的文件缩放比例 |

#### 介绍
支持范围: [100，1600]，实际缩放比为: scale/100 


### GetFileScale
获取文件缩放比例 
``` C++
virtual uint32_t GetFileScale(const char *fileId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件ID  |

#### 返回
文件缩放比例，格式与 SetFileScale 接口参数格式一致 


### SetScaleToolRatio
设置白板缩放工具的缩放比例 
``` C++
virtual void SetScaleToolRatio(uint32_t scale)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| scale | uint32_t | 如果设置为50，则每次滚轮滚动（或鼠标点击），缩放会在原来基础上进行50的缩放。 等价于 teduBoard.setBoardScale(teduBoard.getBoardScale() + 50) 或 teduBoard.setBoardScale(teduBoard.getBoardScale() - 50)  |


### SetScaleAnchor
移动当前白板缩放展示位置 
``` C++
virtual void SetScaleAnchor(double xRatio, double yRation)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| xRatio | double | 白板左上角X坐标，取值[0, 1]  |
| yRation | double | 白板左上角Y坐标，取值[0, 1]  |


### SetBoardContentFitMode
设置白板内容自适应模式 
``` C++
virtual void SetBoardContentFitMode(TEduBoardContentFitMode mode)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| mode | TEduBoardContentFitMode | 要设置的白板内容自适应模式 |

#### 介绍
设置自适应模式后会影响所有后续白板内容操作,受影响接口包括：AddTranscodeFile 


### GetBoardContentFitMode
获取白板内容自适应模式 
``` C++
virtual TEduBoardContentFitMode GetBoardContentFitMode()=0
```
#### 返回
白板内容自适应模式 


### Snapshot
白板快照 
``` C++
virtual void Snapshot(const TEduBoardSnapshotInfo &info)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| info | const TEduBoardSnapshotInfo & | 快照信息  |


### SetNextTextInput
预设文本工具内容 
``` C++
virtual void SetNextTextInput(const char *input, bool focus)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| input | const char * | 预设文本内容，取消预设则设置为空  |
| focus | bool | 是否继续保持焦点  |


### SetZoomCursorIcon
设置放大缩小工具的指针图标 
``` C++
virtual void SetZoomCursorIcon(const TEduBoardCursorIcon &zoomIn, const TEduBoardCursorIcon &zoomOut)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| zoomIn | const TEduBoardCursorIcon & | 放大工具图标  |
| zoomOut | const TEduBoardCursorIcon & | 缩小工具图标  |


### SetRemoteCursorVisible
设置远端画笔在本地是否可见 
``` C++
virtual void SetRemoteCursorVisible(bool visible)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| visible | bool | 远端画笔在本地是否可见  |



## 文件操作接口

### ApplyFileTranscode
发起文件转码请求 
``` C++
virtual void ApplyFileTranscode(const char *path, const TEduBoardTranscodeConfig &config=TEduBoardTranscodeConfig())=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| path | const char * | 要转码的文件路径，编码格式为 UTF8  |
| config | const TEduBoardTranscodeConfig & | 转码参数  |

#### 警告
本接口设计用于在接入阶段快速体验转码功能，原则上不建议在生产环境中使用，生产环境中的转码请求建议使用后台服务接口发起 

#### 介绍
支持 PPT、PDF、Word 文件转码 PPT 文档默认转为 H5 动画，能够还原 PPT 原有动画效果，其它文档转码为静态图片 PPT 动画转码耗时约1秒/页，所有文档的静态转码耗时约0.5秒/页 转码进度和结果将会通过 onTEBFileTranscodeProgress 回调返回，详情参见该回调说明文档 


### GetFileTranscodeProgress
主动查询文件转码进度 
``` C++
virtual void GetFileTranscodeProgress(const char *taskId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| taskId | const char * | 通过 onTEBFileTranscodeProgress 回调拿到的转码任务 taskId  |

#### 警告
该接口仅用于特殊业务场景下主动查询文件转码进度，调用 ApplyFileTranscode 后，SDK 内部将会自动定期触发 onTEBFileTranscodeProgress 回调，正常情况下您不需要主动调用此接口 

#### 介绍
转码进度和结果将会通过 onTEBFileTranscodeProgress 回调返回，详情参见该回调说明文档 


### AddTranscodeFile
添加转码文件 
``` C++
virtual const char* AddTranscodeFile(const TEduBoardTranscodeFileResult &result, bool needSwitch=true)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| result | const TEduBoardTranscodeFileResult & | 文件转码结果  |
| needSwitch | bool | 是否需要在文件加载成功后自动切换到该文件  |

#### 返回
文件 ID 

#### 警告
当传入文件的 URL 重复时，返回 URL 对应的 文件 ID 
在收到对应的 onTEBAddTranscodeFile 回调前，无法用返回的文件 ID 查询到文件信息 

#### 介绍
TEduBoardTranscodeFileResult 的字段信息主要来自：
1. 使用客户端 ApplyFileTranscode 转码，直接将转码结果用于调用此接口
2. （推荐）使用服务端 REST API 转码，只需传入转码回调结果的四个字段（title，resolution，url，pages），其服务端->客户端字段的对应关系为 Title->title、Resolution->resolution、ResultUrl->url、Pages->pages [转码文档](https://cloud.tencent.com/document/product/1137/40260)


### AddImagesFile
添加图片文件 
``` C++
virtual const char* AddImagesFile(const char **urls, uint32_t urlCount)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| urls | const char ** | 要使用的图片 URL 列表，编码格式为 UTF8，不允许为 nullptr  |
| urlCount | uint32_t | 图片 URL 个数  |

#### 返回
文件 ID 

#### 警告
当传入文件的 URL 重复时，文件 ID 返回为空字符串 
在收到对应的 onTEBAddImagesFile 回调前，无法用返回的文件 ID 查询到文件信息 

#### 介绍
文件加载成功后，将自动切换到该文件 


### AddVideoFile
添加视频文件 
``` C++
virtual const char* AddVideoFile(const char *url)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 文件播放地址  |

#### 返回
文件 ID

#### 介绍
移动端支持 mp4/m3u8，桌面端支持 mp4/m3u8/flv/rtmp；触发状态改变回调 onTEBVideoStatusChange 


### ShowVideoControl
显示或隐藏视频控制栏 
``` C++
virtual void ShowVideoControl(bool show)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| show | bool | 是否显示  |

#### 警告
全局控制项，对所有视频文件有效 隐藏和显示默认视频控制栏，默认显示系统自带的 video 控制栏，不同平台界面 UI 样式不同 


### PlayVideo
播放视频 
``` C++
virtual void PlayVideo()=0
```
#### 警告
只对当前文件有效

#### 介绍
触发状态改变回调 onTEBVideoStatusChange，一般在使用自定义视频控制栏时使用 


### PauseVideo
暂停视频 
``` C++
virtual void PauseVideo()=0
```
#### 警告
只对当前文件有效

#### 介绍
触发状态改变回调 onTEBVideoStatusChange，一般在使用自定义视频控制栏时使用 


### SeekVideo
跳转（仅支持点播视频） 
``` C++
virtual void SeekVideo(double time)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| time | double | 播放进度，单位秒  |

#### 警告
只对当前文件有效

#### 介绍
触发状态改变回调 onTEBVideoStatusChange，一般在使用自定义视频控制栏时使用 


### SetSyncVideoStatusEnable
是否同步本地视频操作到远端 
``` C++
virtual void SetSyncVideoStatusEnable(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 是否同步  |

#### 警告
全局控制项，对所有视频文件有效

#### 介绍
play/pause/seek 接口以及控制栏事件的触发是否影响远端，默认为 true 一般情况下学生设置为 false，老师设置为 true 


### StartSyncVideoStatus
内部启动定时器，定时同步视频状态到远端（仅限于 mp4） 
``` C++
virtual void StartSyncVideoStatus(uint32_t interval)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| interval | uint32_t | 同步间隔，例如设置5秒  |

#### 警告
只对当前文件有效

#### 介绍
一般在老师端视频加载完成后调用，切换文件后内部自动销毁定时器， 


### StopSyncVideoStatus
停止同步视频状态 
``` C++
virtual void StopSyncVideoStatus()=0
```
#### 警告
只对当前文件有效 


### EnableAudioControl
是否启用音频控制面板 
``` C++
virtual void EnableAudioControl(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 启用或禁止  |

#### 警告
禁止控制面板后，不能通过界面交互方式操作音频元素 


### PlayAudio
播放音频 
``` C++
virtual void PlayAudio(const char *elementId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 调用 addElement 方法返回的元素 ID |

#### 介绍
触发状态改变回调 onTEBAudioStatusChange 


### PauseAudio
暂停音频 
``` C++
virtual void PauseAudio(const char *elementId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 调用 addElement 方法返回的元素 ID |

#### 介绍
触发状态改变回调 onTEBAudioStatusChange 


### SeekAudio
跳转 
``` C++
virtual void SeekAudio(const char *elementId, double time)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 调用 addElement 方法返回的元素 ID  |
| time | double | 播放进度，单位秒 |

#### 介绍
触发状态改变回调 onTEBAudioStatusChange 


### SetAudioVolume
设置音频播放音量 
``` C++
virtual void SetAudioVolume(const char *elementId, double volume)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 调用 addElement 返回的元素 ID  |
| volume | double | 音频音量，取值范围[0-1]  |


### GetAudioVolume
获取音频播放音量 
``` C++
virtual double GetAudioVolume(const char *elementId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| elementId | const char * | 调用 addElement 返回的元素 ID  |

#### 返回
当前音量 


### AddH5File
添加 H5 页面 
``` C++
virtual const char* AddH5File(const char *url)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| url | const char * | 网页地址  |

#### 返回
文件 ID 

>? 只支持展示，不支持互动 


### DeleteFile
删除文件 
``` C++
virtual void DeleteFile(const char *fileId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 要删除的文件 ID |

#### 介绍
文件 ID 为 nullptr 时表示当前文件，默认文件无法删除 


### SwitchFile
切换文件 
``` C++
virtual void SwitchFile(const char *fileId, const char *boardId=nullptr, int32_t stepIndex=-1)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 要切换到的文件 ID  |
| boardId | const char * | 切换文件并跳转到这个白板页  |
| stepIndex | int32_t | 跳转到白板页并切换到这个动画  |

#### 警告
该接口仅可用于文件切换，如果传入的 fileId 为当前文件 ID，SDK 会忽略其它参数，不做任何操作 

>? 文件 ID 为必填项，为 nullptr 或空字符串将导致文件切换失败 


### GetCurrentFile
获取当前文件 ID 
``` C++
virtual const char* GetCurrentFile()=0
```
#### 返回
当前文件 ID 


### GetFileInfo
获取白板中指定文件的文件信息 
``` C++
virtual TEduBoardFileInfo GetFileInfo(const char *fileId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * |  |

#### 返回
文件信息 

#### 警告
每次调用该接口的返回值内容都指向同一块内存，若需要保存返回信息，请在拿到返回值后及时拷贝走 


### GetFileInfoList
获取白板中上传的所有文件的文件信息列表 
``` C++
virtual TEduBoardFileInfoList* GetFileInfoList()=0
```
#### 返回
文件信息列表 

#### 警告
返回值不再使用时不需要自行 delete，但是务必调用其 release 方法以释放内存占用 


### GetFileBoardList
获取指定文件的白板 ID 列表 
``` C++
virtual TEduBoardStringList* GetFileBoardList(const char *fileId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件 ID  |

#### 返回
白板 ID 列表 

#### 警告
返回值不再使用时不需要自行 delete，但是务必调用其 release 方法以释放内存占用 


### GetThumbnailImages
获取指定文件的缩略图，不支持默认文件（fileId=#DEFAULT） 
``` C++
virtual TEduBoardStringList* GetThumbnailImages(const char *fileId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件 ID  |

#### 返回
缩略图 URL 列表 

>? 用户在调用 rest api 请求转码时，需要带上 "thumbnail_resolution" 参数，开启缩略图功能，否则返回的缩略图 URL 无效 


### ClearFileDraws
清空指定文件的所有白板涂鸦 
``` C++
virtual void ClearFileDraws(const char *fileId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| fileId | const char * | 文件 ID  |


### SetUserInfo
设置用户信息 
``` C++
virtual void SetUserInfo(const TEduUserInfo &userInfo)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| userInfo | const TEduUserInfo & | 用户信息  |


### SetPenAutoFittingMode
设置画笔自动拟合模式 
``` C++
virtual void SetPenAutoFittingMode(const TEduBoardPenFittingMode &penMode)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| penMode | const TEduBoardPenFittingMode & | 画笔自动拟合模式 TEduBoardPenFittingMode  |


### AddSnapshotMark
生成板书图片 调用此接口可在后台生成当前白板的板书内容 
``` C++
virtual void AddSnapshotMark()=0
```

### SetMouseToolBehavior
设置鼠标工具行为 调用此接口设置鼠标工具行为 
``` C++
virtual void SetMouseToolBehavior(const TEduMouseToolBehavior &turnPage)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| turnPage | const TEduMouseToolBehavior & |  |


### SetMathGraphType
设置几何画板元素调用此接口设置几何画板元素 
``` C++
virtual void SetMathGraphType(const TEduBoardMathGraphType &graphType, bool setMouseToolopt=true)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| graphType | const TEduBoardMathGraphType & | 几何图形类型  |
| setMouseToolopt | bool | 是否切换到鼠标工具 默认为 true  |


### SetBoardRemark
设置白板备注 为某个白板设置备注, 当前白板可省略 boardId 参数 
``` C++
virtual void SetBoardRemark(const char *boardId, const char *remark)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 白板 ID  |
| remark | const char * | 对应白板备注  |


### GetBoardRemark
获取白板备注 
``` C++
virtual TEduBoardReMarkInfoList* GetBoardRemark(const char *boardId=nullptr)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 为空时，获取所有设置过白板备注  |

#### 返回
返回白板备注列表 


### SetClassGroupEnable
开启分组模式 
``` C++
virtual void SetClassGroupEnable(bool enable)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| enable | bool | 是否启用  |


### GetClassGroupEnable
获取分组模式状态 
``` C++
virtual bool GetClassGroupEnable()=0
```
#### 返回
true: 开启 false: 未开启 


### SetClassGroup
添加分组 
``` C++
virtual void SetClassGroup(const char *groudId, char **boards, uint32_t boardCount, char **users, uint32_t userCount, const char *titleId, const char *currentBoardId=nullptr)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| groudId | const char * | 分组 ID  |
| boards | char ** | 分组白板列表  |
| boardCount | uint32_t | 分组白板个数  |
| users | char ** | 分组用户列表   |
| userCount | uint32_t | 分组用户个数   |
| titleId | const char * | 分组标题  |
| currentBoardId | const char * | 分组初始白板  |


### ResetClassGroup
重置所有分组 
``` C++
virtual void ResetClassGroup()=0
```

### RemoveClassGroup
删除分组 
``` C++
virtual void RemoveClassGroup(const char *groudId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| groudId | const char * | 分组 ID  |


### GetClassGroupInfoByGroupId
获取分组信息 
``` C++
virtual TEduBoardClassGroupInfo GetClassGroupInfoByGroupId(const char *groupId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| groupId | const char * | 分组 ID  |

#### 返回
分组信息 


### GetClassGroupIdByUserId
获取用户所在的分组 
``` C++
virtual TEduBoardStringList* GetClassGroupIdByUserId(const char *userId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| userId | const char * | 用户 ID  |


### RemoveUserInClassGroup
从分组中删除用户 
``` C++
virtual void RemoveUserInClassGroup(const char *group, const char *userId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| group | const char * | 分组 ID  |
| userId | const char * | 用户 ID  |


### RemoveBoardInClassGroup
从分组中删除白板 
``` C++
virtual void RemoveBoardInClassGroup(const char *group, const char *boardId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| group | const char * | 分组 ID  |
| boardId | const char * | 白板 ID  |


### GotoClassGroupBoard
分组内跳转 分组模式下切换白板只能通过此方法进行，必须知道需要跳转的白板 ID 
``` C++
virtual void GotoClassGroupBoard(const char *boardId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| boardId | const char * | 白板id  |


### SetClassGroupTitle
设置分组标题 
``` C++
virtual void SetClassGroupTitle(const char *groupId, const char *title)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| groupId | const char * | 分组 ID  |
| title | const char * | 分组标题  |


### AddBoardToClassGroup
新增白板 ID 
``` C++
virtual void AddBoardToClassGroup(const char *groupId, const char *boardId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| groupId | const char * | 分组 ID  |
| boardId | const char * | 白板 ID  |


### AddUserToClassGroup
添加用户到分组 
``` C++
virtual void AddUserToClassGroup(const char *groupId, const char *userId)=0
```
#### 参数

| 参数 | 类型 | 含义 |
| --- | --- | --- |
| groupId | const char * | 分组 ID  |
| userId | const char * | 用户 ID  |


### GetAllClassGroupIds
获取所有分组 ID 
``` C++
virtual TEduBoardStringList* GetAllClassGroupIds()=0
```
#### 返回
分组列表 





