## 1. SDK文件结构
白板SDK内包含文件说明如下表:

|文件名称|说明|
|---|---|
|BoardSDK.dll|SDK动态链接库|
|BoardSDK.lib|SDK导入库|
|BoardSDK.h|SDK头文件|

## 2. SDK快速集成
### 2.1 导入SDK到项目
在Visual Studio开发环境下，按如下步骤导入SDK：

1. 从菜单中依次选择`视图`-`解决方案资源管理器`
2. 在`解决方案资源管理器`中，右键点击要导入SDK的项目名称
3. 在弹出菜单内点击`属性`选项，弹出`项目属性`对话框
4. 从左侧`配置属性`列表中，选择`VC++目录`项
5. 将SDK所在目录路径依次添加到右侧`包含目录`及`库目录`中
6. 在任意一个`*.c`或`*.cpp`文件内添加如下代码导入SDK接口

```C++
#pragma comment(lib, "BoardSDK.lib")
```

### 2.2 创建白板窗口
创建白板前，首先使用如下代码引入SDK头文件：

```C++
#include "BoardSDK.h"
```

之后使用如下代码创建一个白板实例：

```C++
BoardSDK *boardSDk = new BoardSDK("TestUser", hWnd);
```

> 注意：白板长宽比固定为 16 : 9

其中第一个参数`"TestUser"`指定当前用户ID，第二个参数`hWnd`用于指定父窗口；`hWnd`参数为可选参数，留空表示白板窗口没有父窗口，此时创建出来的白板窗口为独立窗口。

想要获得白板离线数据则还要初始化白板上报，添入参数依次为sdkAppID，房间ID，用户签名
```C++
boardSDk->enableDefaultReporter(sdkAppID(), roomID(),  userSig());
```

白板窗口创建完后，可通过如下代码获取白板窗口句柄，方便对白板窗口进行操作：

```C++
HWND boardHWnd = boardSDk->getRenderWindow();
```

之后调用

```C++
ShowWindow(hWnd, SW_SHOW);
```
将白板显示出来或者使用其他代码将白板插入父窗口。


### 2.3 指定绘制工具及属性
完成白板窗口创建后，可使用如下代码设置要使用的白板工具及其属性：

```C++
boardSDk->useTool(BoardTool::Rectangle);//使用矩形工具
boardSDk->setWidth(100);//设置画笔宽度
boardSDk->setColor(0xff0000ff);//设置画笔颜色（颜色字节序从高到低按RGBA存储）
boardSDk->setFill(true);//填充图形
boardSDk->setRadius(30);//设置圆角半径
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
|选区|BoardTool::Select|无|

### 2.4 页面操作、背景设置及页面清除
白板SDK支持多页面操作，可通过如下代码来进行页面操作：

```C++
char *pages[50];
for(int i = 0; i < 50; ++i){
    pages[i] = new char[256];
}
uint32_t pageCount = boardSDk->getPages(pages, 50);
boardSDk->pageOperate("newPage", pages, pageCount);
for(int i = 0; i < 50; ++i){
    delete[] pages[i];
    pages[i] = nullptr;
}
delete[] pages;
```

以上代码实现了删除所有原有页面并跳转到ID为newPage的页面的功能。`getPages`接口用于获取白板页面ID列表，返回值为白板页数；其参数1指定了用于接收页面ID的字符串数组缓冲区，为可选参数，留空表示只查询白板页数，参数2指定了缓冲区数组长度。`pageOperate`接口用于跳转到参数1指定的页面并删除参数2指定的一些页面，其参数2和参数3为可选参数，留空表示不删除任何页面。当参数1所指向的页面不存在时，将会自动创建页面。当参数2所指向的页面不存在时，会自动忽略。

在任何时候，可以通过如下代码设置页面背景图片：

```C++
boardSDk->useBackground("http://www.image.com/img", "page1");
```

以上代码设置ID为page1的页面背景图片为URL“[http://www.image.com/img]()”，当第一个参数指定为URL时，白板SDK会自动联网下载图片，当该参数以字符串“file://” 开头时，SDK将尝试在本地查找该文件路径。第二个参数用于指定要设置背景的页面ID，留空表示设置当前页面的背景，当其所指向的页面不存在时，将会自动创建页面。

在任何时候，可以通过如下代码来清除当前页面内容：

```C++
boardSDk->clear();
```

页面清除操作不可撤销。

### 2.5 选区、复制及删除
使用如下代码将白板工具设置为选区工具后，用户可以在白板上框选已绘制图形：

```C++
boardSDk->useTool(BoardTool::Select);
```

已绘制图形选中以后，用户可以在白板区域中进行拖动操作，同时可以使用如下代码进行复制及删除操作：

```C++
boardSDk->copy();//复制选中图形
boardSDk->remove();//删除选中图形
```

以上复制及删除操作支持撤销重做。

### 2.6 上传文档

用户想使用PPT，可先上传到腾讯云对象存储COS。白板内部集成了COSSDK
开发者可以使用我们维护内置的公共账号（每个客户对应一个存储桶，推荐），也可以自己申请配置COS账号并自行维护。

使用如下接口可以将ppt上传至COS：
```C++
boardSDk->uploadFile(filePath);//上传文件
```
这里会将文件上传至公共账号的COS路径下，通过回调`onUploadResult`和`onFileUploadResult`通知上传和预览结果
如果想使用自己申请的COS账号存储地址，可以调如下接口设置：
```C++
boardSDk->setCosConfig(appId, bucket, path, region);//设置COS参数
```

### 2.7 添加PPT（以PPT为例）

用户首先需要将PPT上传到腾讯云对象存储COS（或者其他存储系统），获取到PPT每一页转码后的图片URL链接。

* 添加PPT作为普通白板

将上一步获取到的URL数组当做参数传入，SDK内部会生成与URL数量对应数量的白板，并将这些白板的boardID通过输出参数返回
用户在外层维护白板数据结构

* 多PPT上传管理

将上一步获取到的URL数组，和文件名当做参数传入，SDK内部会根据该文件生成对应的文件唯一标识**fid**返回，并生成与URL数量对应数量的白板，并将这些白板的boardID通过输出参数返回。 
用户需在外层维护这样一个数据结构：

```json
{

    fid1 : {
        boardID1,
        boardID2,
        boardID3,
        ...
    },
    
    fid2 : {
        boardID1,
        boardID2,
        boardID3,
        ...
    },
    ....
}

```

若要删除PPT，调用 deleteFile 接口，传入文件对应的fid即可。deleteFile 内部会将该文件对应的白板全部删除，同样的用户在外部维护的白板ID也应该对应删除

### 2.8 SDK回调
白板SDK通过回调接口通知用户SDK内部状态变化，当需要接收回调时，您需要创建一个类继承自`BoardCallback`类，并实现其中所有纯虚方法，使用如下代码设置SDK回调：

```C++
class MyCallback : public BoardCallback{
public:
    void onActionsData(const char *data, uint32_t length) override;
    void onBoardEventData(const char *data, uint32_t length) override;
    void onStatusChanged(bool canUndo, bool canRedo) override;
    uint32_t onGetTime() override;
    void onGetBoardData(bool bResult) override;
    void onReportBoardData(const int code, const char * msg) override;
    void onUploadResult(bool success, int code, const wchar_t* objName, const wchar_t*  fileName) override;
    void onFileUploadResult(bool success, const wchar_t* objName, const wchar_t* fileName, int pageCount) override;
};

MyCallback myCallback;
boardSDk->setCallback(&myCallback);
```

其中`onGetTime`接口用于供白板SDK获取统一的时间戳，白板SDK内部对所有操作的排序都依靠该接口保证先后顺序，您必须在该接口中返回尽可能准确且多端统一的时间戳，精度至少为秒。（时间戳多端不统一一般也不会造成太大问题，但极端情况下可能导致多端显示内容存在细微差异）

### 2.9 撤销及重做
白板SDK支持操作的撤销及重做，任何时候可以使用如下代码进行撤销或重做操作：

```C++
boardSDk->undo();//撤销
boardSDk->redo();//重做
```

如果当前已经没有操作可撤销或者重做，则调用无效，不会产生其他负面效果。对于当前是否存在操作可撤销或重做，SDK将会在用户进行操作后通过回调`onStatusChanged`返回通知，其中`canUndo`参数指示当前是否存在可撤销操作，`canRedo`参数指示当前是否存在可重做操作。

### 2.10 多白板状态同步

课堂中，老师对白板的操作，涂鸦、图片、PPT、撤销、清空等操作需要上报到后台，并进行存储，这样后面中途加入课堂的成员就能拉取之前的白板数据进行展示。

该过程主要分为两步，数据上报和数据拉取：

白板数据上报：
在每次对白板操作后，SDK会将操作的数据上报到白板后台，目前表白SDK已经内部实现了该功能，白板后台服务也是我们在维护，用户无需自行实现。

白板数据拉取（同步）：
数据拉取在白板中提供了一个接口，用户只需要在进房成功之后调用该接口拉取白板数据即可， 方法内部已经实现了数据的解析即填充到白板的功能。（包括异常退出重新进入房间时同步数据的场景）
```C++
boardSDk->getBoardData();
```

## 3. SDK参考
各接口具体的作用及参数说明，详见SDK头文件注释。


