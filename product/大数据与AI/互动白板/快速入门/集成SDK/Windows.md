## 集成 SDK

本文主要介绍如何快速的将腾讯云互动白板 SDK 集成到您的项目中。

## 开发环境要求

- Windows 7 及以上版本 Windows 操作系统
- Microsoft Visual Studio 2015 及以上版本，推荐使用 Microsoft Visual Studio 2015
- Windows SDK 8.0 及以上版本，推荐使用 Windows SDK 8.1  

## 集成 互动白板 SDK

#### 步骤1：下载  Windows SDK

[下载 SDK](https://demo.qcloudtiw.com/win/exe/tic_demo.zip)，解压并打开文件，包含以下部分：

|              目录/文件名              |           说明          |
|---------------------------------------|-------------------------|
| Demo                                  | C++ Demo 源码           |
| SDK/TEduBoard/include/TEduBoard.h     | 互动白板 SDK 头文件     |
| SDK/TEduBoard/lib/TEduBoard.lib       | 互动白板 SDK 导入库     |
| SDK/TEduBoard/lib/TEduBoard.dll       | 互动白板 SDK 动态链接库 |
| SDK/TEduBoard/lib/TEduBoardRender.exe | 互动白板 SDK 渲染程序   |
| SDK/TEduBoard/lib/其他文件            | CEF 框架及其依赖文件    |
| SDK/其他目录                          | Demo依赖的其他SDK       |

本文示例中，您只需要使用 SDK/TEduBoard 目录下的 互动白板 SDK 文件即可。


#### 步骤2：导入 SDK 到项目

在 Visual Studio 开发环境下，按如下步骤导入 SDK：

1. 从菜单中依次选择【视图】>【解决方案资源管理器】。
2. 在【解决方案资源管理器】中，右键单击要导入 SDK 的项目名称。
3. 在弹出菜单内单击【属性】选项，弹出项目属性对话框。
4. 从左侧配置属性列表中，选择【VC++目录】项。
5. 将 SDK 头文件所在目录路径添加到右侧【包含目录】中。
6. 将 SDK 导入库所在目录路径添加到右侧【库目录】中。
7. 在需要使用 SDK 的源码文件内添加如下代码导入 SDK。

```cpp
// 引入 SDK 头文件
#include "TEduBoard.h"

// 链接 SDK
#pragma comment(lib, "TEduBoard.lib")
```


#### 步骤3：白板创建及销毁

#### 白板控制器创建及初始化

使用如下代码创建并初始化白板控制器：
```cpp
// 创建白板控制器
TEduBoardController *boardCtrl = CreateTEduBoardController();

// 添加回调
boardCtrl->AddCallback(myCallback); // myCallback 为实例化 TEduBoardCallback 接口的回调接收器

// 初始化授权参数结构体
TEduBoardAuthParam authParam;
authParam.sdkAppId = SDK_APP_ID;    // 填写您的 SDKAppID
authParam.userId = USER_ID;         // 填写用户 ID
authParam.userSig = USER_SIG;       // 填写用户签名

// 初始化白板控制器（配合腾讯云 IMSDK 4.0 以上版本使用时，initParam 参数可以不填）
boardCtrl->Init(authParam, ROOM_ID);
```

#### 监听白板关键事件

白板事件回调接口 `TEduBoardCallback`的`onTEBError`和`onTEBWarning` 回调方法内监听白板事件 

- [onTEBError 错误详情](https://cloud.tencent.com/document/product/1137/39985#onteberror)
- [onTEBWarning 警告详情](https://cloud.tencent.com/document/product/1137/39985#ontebwarning)

```cpp
/**
* 白板错误回调
* 
* @param code 错误码，参见TEduBoardErrorCode定义
* @param msg  错误信息，编码格式为 UTF8
*/
virtual void onTEBError(TEduBoardErrorCode code,const char* msg)		

/**
* 白板警告回调
*
* @param code 警告码，参见TEduBoardWarningCode定义
* @param msg  警告信息，编码格式为 UTF8
*/
virtual void onTEBWarning(TEduBoardWarningCode code,const char* msg)	
```

#### 白板窗口获取及显示

在 onTEBInit 回调方法内，使用如下代码获取并显示白板窗口：
```cpp
// SDK所有回调都在主线程内执行，因此我们可以在回调里直接执行 UI 操作

// 获取白板窗口句柄
HWND boardHwnd = boardCtrl->GetBoardRenderView();

// 获取并计算父窗口客户区大小
RECT parentRect;
::GetClientRect(PARENT_HWND, &parentRect); // PARENT_HWND 为要将白板窗口嵌入其中显示的容器窗口句柄
int cx =  parentRect.right - parentRect.left;
int cy =  parentRect.bottom - parentRect.top;

// 设置白板为子窗口
::SetParent(boardHwnd, PARENT_HWND);

// 更改白板大小和位置
boardCtrl->SetBoardRenderViewPos(0, 0, cx, cy);

// 显示白板窗口
::ShowWindow(boardHwnd, SW_SHOW);
```

####  WM_SIZE 事件处理

在父窗口的 WM_SIZE 事件处理函数内，使用如下代码调整白板窗口大小与父窗口适配：
```cpp
// 获取白板窗口句柄
HWND boardHwnd = boardCtrl->GetBoardRenderView();

// 获取并计算父窗口客户区大小
RECT parentRect;
::GetClientRect(PARENT_HWND, &parentRect);
int cx =  parentRect.right - parentRect.left;
int cy =  parentRect.bottom - parentRect.top;

// 更改白板大小
boardCtrl->SetBoardRenderViewPos(0, 0, cx, cy);
```

#### 白板窗口关闭

需要关闭白板窗口时，使用如下代码关闭：
```cpp
// 销毁白板控制器
DestroyTEduBoardController(&boardCtrl);
```


#### 步骤4：白板数据同步

白板在使用过程中，需要在不同的用户之间进行数据同步（涂鸦数据等），SDK 默认使用 IMSDK 作为信令通道，您需要自行实现 IMSDK 的初始化、登录、加入群组操作，确保白板初始化时，IMSDK 已处于所指定的群组内。