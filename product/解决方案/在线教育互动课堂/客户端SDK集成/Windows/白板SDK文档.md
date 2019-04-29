## 1. SDK 文件结构
白板 SDK 内包含文件说明如下表:

|文件名称|说明|
|---|---|
|BoardSDK.dll|SDK 动态链接库|
|BoardSDK.lib|SDK 导入库|
|BoardSDK.h|SDK 头文件|
|BoardMgr.h|SDK 头文件|

## 2. SDK 快速集成
### 2.1 导入 SDK 到项目
在 Visual Studio 开发环境下，按如下步骤导入 SDK：

1. 从菜单中依次选择`视图`>`解决方案资源管理器`；
2. 在`解决方案资源管理器`中，右键单击要导入 SDK 的项目名称；
3. 在弹出菜单内单击`属性`选项，弹出`项目属性`对话框；
4. 从左侧`配置属性`列表中，选择`VC++目录`项；
5. 将 SDK 所在目录路径依次添加到右侧`包含目录`及`库目录`中；
6. 在任意一个`*.c`或`*.cpp`文件内添加如下代码导入 SDK 接口。

```C++
#pragma comment(lib, "BoardSDK.lib")
```
### 2.2 初始化白板
初始化白板前，首先使用如下代码引入 SDK 头文件：
```C++
#include "BoardMgr.h"
```
然后调用如下代码进行白板初始化：

```C++
boardMgr = BoardMgr::GetSDKInstance();
boardMgr->init(userID, userSig, sdkappId);
```
退出时销毁白板直接删除指针即可：
```C++
delete boardMgr；
```

### 2.3 创建普通白板窗口
使用如下代码创建白板实例，并获得白板指针：

```C++
boardMgr->initBoardSDK(roomId, hwnd);
BoardSDK* boardSDk = boardMgr->getBoardSDK();
```
使用 TICSDK 推荐 TICSDK 的方法`initWhiteBoard`

>!白板长宽比推荐固定为16:9。

其中第一个参数`roomId`指定当前房间 ID，第二个参数`hWnd`用于指定父窗口；`hWnd`参数为可选参数，留空表示白板窗口没有父窗口，此时创建出来的白板窗口为独立窗口。
白板窗口创建完后，可通过如下代码获取白板窗口句柄，方便对白板窗口进行操作：

```C++
HWND boardHWnd = boardSDk->getRenderWindow();
```

之后调用：

```C++
ShowWindow(hWnd, SW_SHOW);
```
将白板显示出来或者使用其他代码将白板插入父窗口。


### 2.4 指定绘制工具及属性
完成白板窗口创建后，可使用如下代码设置要使用的白板工具及其属性：

```C++
boardSDk->useTool(BoardTool::Rectangle);//使用矩形工具
boardSDk->setLineWidth(2);//设置画笔宽度
boardSDk->setBrushColor(255，0，255，255);//设置画笔颜色，按照red，green，blue和alpha通道值顺序
boardSDk->setFill(true);//填充图形
boardSDk->setRadius(10);//设置圆角半径
boardSDk->setFontSize(20);//设置文字大小
boardSDk->setScale(200); //设置缩放系数
```

可选的工具定义如下：

|工具|定义|可用属性|
|---|---|---|
|不使用|BoardTool::None|无|
|铅笔|BoardTool::Pen|宽度、颜色|
|橡皮擦|BoardTool::Eraser|宽度（直径）|
|激光点|BoardTool::Laser|宽度（直径）|
|直线|BoardTool::Line|宽度、颜色|
|椭圆|BoardTool::Ellipse|宽度、颜色、是否填充|
|矩形|BoardTool::Rectangle|宽度、颜色、是否填充、圆角半径|
|文字|BoardTool::Text|颜色、大小|
|选区|BoardTool::Select|无|
|移动|BoardTool::Shift|无|

### 2.5 页面操作、背景设置及页面清除
白板 SDK 支持多页面操作，可通过 BoardMgr 如下接口来进行页面操作：

```C++
	/**
	* \brief 获取当前页码
	* \return 当前页码
	*/
	virtual uint32_t getPageIndex() = 0;

	/**
	* \brief 获取总页数
	* \return 总页数
	*/
	virtual uint32_t getPageCount() = 0;

	/**
	* \brief 刷新页码
	*/
	virtual void refreshPageInfo() = 0;

	/**
	* \brief 页码跳转
	* \param pageIndex  跳转的页码
	*/
	virtual void gotoPage(uint32_t pageIndex) = 0;

	/**
	* \brief 跳转上一页
	*/
	virtual void gotoLastPage() = 0;

	/**
	* \brief 跳转下一页
	*/
	virtual void gotoNextPage() = 0;

	/**
	* \brief 插入新的一页
	*/
	virtual void insertPage() = 0;

	/**
	* \brief 删除当前页
	*/
	virtual void deletePage() = 0;
```
在任何时候，可以通过如下代码设置页面背景图片：
```C++
boardSDk->setBackgroundImage("http://www.image.com/img", "page1");
```

以上代码设置 ID 为 page1 的页面背景图片为 URL`[http://www.image.com/img]()`，当第一个参数指定为 URL 时，白板 SDK 会自动联网下载图片，当该参数以字符串`file://`开头时，SDK 将尝试在本地查找该文件路径。第二个参数用于指定要设置背景的页面 ID，留空表示设置当前页面的背景，当其所指向的页面不存在时，将会自动创建页面。

在任何时候，可以通过如下代码来清除当前页面内容：

```C++
boardSDk->clear();
```

页面清除操作不可撤销。

### 2.6 选区、复制及删除
使用如下代码将白板工具设置为选区工具后，用户可以在白板上框选已绘制图形：

```C++
boardSDk->useTool(BoardTool::Select);
```

已绘制图形选中以后，用户可以在白板区域中进行拖动操作，同时可以使用如下代码进行复制及删除操作：

```C++
boardSDk->copy();//复制选中图形
boardSDk->remove();//删除选中图形
```
>?复制及删除操作支持撤销重做。


### 2.7 上传文档

用户想使用 PPT，可先上传至腾讯云对象存储 COS。目前白板内部集成了 COSSDK。
开发者可以使用我们维护内置的公共账号（每个客户对应一个存储桶，推荐），也可以自己申请配置 COS 账号并自行维护。

使用如下接口可以将 PPT 上传至 COS：
```C++
boardSDk->uploadFile(filePath);//上传文件
```
这里会将文件上传至公共账号的 COS 路径下，通过回调`onUploadResult`和`onFileUploadResult`通知上传和预览结果。
如果想使用自己申请的 COS 账号存储地址，可以调如下接口设置：
```C++
boardSDk->setCosConfig(appId, bucket, path, region);//设置COS参数
```
对于使用了 V4 旧版的 COS 系统，上传需要先计算签名 sig，再调用以下代码。
```C++
boardSDk->uploadFile(filePath, sig);
```
### 2.8 添加 PPT（以 PPT 为例）

用户首先需要将 PPT 上传到腾讯云对象存储 COS（或者其他存储系统），获取到PPT每一页转码后的图片 URL 链接。
```C++
url = boardMgr->getPreviewUrl(objName, i);
```

* PPT上传管理

将上一步获取到的 URL 数组，和文件名当做参数传入，SDK 内部会根据该文件生成对应的文件唯一标识 **fid** 返回，并生成与 URL 数量对应数量的白板。 
```C++
boardMgr->addFile(_backsUrl, fileName);
```

若要删除 PPT，调用 deleteFile 接口，传入文件对应的 fid 即可。deleteFile 内部会将该文件对应的白板全部删除，同样的用户在外部维护的白板 ID 也应该对应删除。

### 2.9 SDK 回调
白板 SDK 通过回调接口通知用户 SDK 内部状态变化，当需要接收回调时，您需要创建一个类继承自`BoardCallback`类，并实现其中所有纯虚方法，使用如下代码设置 SDK 回调：

```C++
class MyCallback : public BoardCallback{
public:
    void onActionsData(const char *data, uint32_t length) override;
    void onBoardEventData(const char *data, uint32_t length) override;
    void onStatusChanged(bool canUndo, bool canRedo) override;
    uint32_t onGetTime() override;
    void onGetBoardData(bool bResult) override;
    void onReportBoardData(const int code, const char * msg) override;
    void onUploadResult(bool success, int code, const wchar_t* objName, const wchar_t*  fileName, void* data) override;
    void onFileUploadResult(bool success, const wchar_t* objName, const wchar_t* fileName, int pageCount, void* data) override;
    void onUploadProgress(int percent, void* data) override;
};

MyCallback myCallback;
boardSDk->setCallback(&myCallback);
```

其中`onGetTime`接口用于供白板 SDK 获取统一的时间戳，白板 SDK 内部对所有操作的排序都依靠该接口保证先后顺序，您必须在该接口中返回尽可能准确且多端统一的时间戳，精度至少为秒（时间戳多端不统一一般也不会造成太大问题，但极端情况下可能导致多端显示内容存在细微差异）。

### 2.10 撤销及重做
白板 SDK 支持操作的撤销及重做，任何时候可以使用如下代码进行撤销或重做操作：

```C++
boardSDk->undo();//撤销
boardSDk->redo();//重做
```

如果当前已经没有操作可撤销或者重做，则调用无效，不会产生其他负面效果。对于当前是否存在操作可撤销或重做，SDK 将会在用户进行操作后通过回调`onStatusChanged`返回通知，其中`canUndo`参数指示当前是否存在可撤销操作，`canRedo`参数指示当前是否存在可重做操作。

### 2.11 多白板状态同步

课堂中，老师对白板的操作，涂鸦、图片、PPT、撤销、清空等操作需要上报到后台，并进行存储，这样后面中途加入课堂的成员就能拉取之前的白板数据进行展示。

该过程主要分为两步，数据上报和数据拉取：

白板数据上报：
在每次对白板操作后，SDK 会将操作的数据上报到白板后台，目前表白 SDK 已经内部实现了该功能，白板后台服务也是我们在维护，用户无需自行实现。

白板数据拉取（同步）：
数据拉取在白板中提供了一个接口，用户只需要在进房成功之后调用该接口拉取白板数据即可， 方法内部已经实现了数据的解析即填充到白板的功能（包括异常退出重新进入房间时同步数据的场景）。
```C++
boardSDk->getBoardData();
```

## 3. SDK 参考
各接口具体的作用及参数说明，详见 SDK 头文件注释。


