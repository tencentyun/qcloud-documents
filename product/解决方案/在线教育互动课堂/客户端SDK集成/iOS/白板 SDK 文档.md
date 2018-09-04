## 1. TXBoardSDK 简介

`TXBoardSDK.framework`即白板 SDK，提供了包括画笔、橡皮擦、背景图设置、标准图形、框选等基本功能，同时还支持文档展示和多端互动。

> 注意: TICSDK 中已经包含了白板 SDK，开发者无需单独集成，也不需要关心代理设置，协议方法等逻辑，这些功能已经在 TICSDK 内部实现，开发者只需要创建白板对象，并调用白板对象的相应接口来操作白板即可。

#### 头文件概览

先总体说明下 SDK 中暴露的公开头文件的主要功能：

类名 | 主要功能
--------- | ---------
TXBoardSDK.h | SDK 的全局管理类
TXBoardView.h | 白板视图类，白板操作类，包含了所有白板相关的操作接口
TXBoardCommon.h | 白板定义类，定义了一些与白板视图相关的枚举，类和代理方法
TXFileManager.h | 文件管理类，内部封装了腾讯云对象云存储 COSSDK，负责文件（PPT、wrod、Excel、pdf、图片等）的上传、下载、在线转码预览等


## 2. 使用方法

### 2.1 初始化
接口 | 说明
---|---
-initSDK:uid:userSig:succ:failed: | 初始化白板 TXBoardSDK

使用`TXBoardSDK`必须先初始化（使用 TICSDK 无需单独调用该接口，TICSDK 内部已将`TXBoardSDK`初始化）


### 2.2 创建一块白板
接口 | 说明
---|---
-initWithRoomID: | 初始化 TXBoardView



`TXBoardView`的指定初始化方法（其他方法已经废弃），需传入一个房间 ID（即 TIC 中创建房间填入的 roomID）, 实例代码如下：

```objc
TXBoardView *boardView = [[TXBoardView alloc] initWithRoomID:_classID];
boardView.frame = ...;
```

> 注意：为了保证数据的准确展示，各端白板视图的长宽比需保持一致，demo 中为 16：9。

### 2.3 选择白板工具
白板工具定义为一个枚举，开发者可以根据业务场景自行设置：

```objc

/** 白板工具类型 */
typedef NS_ENUM(NSInteger, TXBoardBrushModel)
{
    TXBoardBrushModelNone = 0,
    TXBoardBrushModelLine = 1,      //线条（默认）
    TXBoardBrushModelEraser,        //橡皮擦（点选删除某段涂鸦）
    TXBoardBrushModelTapSel,        //单击选择涂鸦
    TXBoardBrushModelRectSel,       //框选涂鸦
    TXBoardBrushModelSegment,       //直线线段
    TXBoardBrushModelOval,          //椭圆
    TXBoardBrushModelOvalFill,      //实心椭圆
    TXBoardBrushModelRound,         //正圆
    TXBoardBrushModelRoundFill,     //实心正圆
    TXBoardBrushModelRectangle,     //矩形
    TXBoardBrushModelRectangleFill, //实心矩形
    TXBoardBrushModelTransform,     // 缩放(双指)/移动(单指)
};
```

接口 | 说明
---|---
-setBrushModel: | 设置白板工具类型

### 2.4 白板基本操作接口
接口 | 说明
---|---
setBrushColor: | 设置画线、添加标准图形时线条的颜色
getBrushColor | 获取当前画笔颜色
setBrushWidth: | 设置画线、添加标准图形时线条的宽度
getBrushWidth | 获取当前画笔宽度
setEraserRadius: | 设置擦除效果的范围半径
getEraserRadius: | 获取擦除效果的范围半径
setBackgroundColor: | 设置当前白板背景颜色
setGlobalBackgroundColor: | 设置全局白板背景颜色
undo | 撤销上一步操作
canUndo | 获取是否可以进行撤回操作
redo | 重做上一步被撤回的操作
canRedo | 获取是否可以进行重做操作
clear: | 清空当前白板所有数据，包含背景图片
clearDraws: | 清空当前白板涂鸦数据，不包含背景图片、PPT
clearFileDraws: | 清空指定文件的涂鸦（不包括背景图片）

### 2.5 图片操作接口

接口 | 说明
---|---
updateBgImageWithPath:mode:succ:failed: | 设置背景图片（本地图片路径）
updateBgImageWithURL:mode:succ:failed: | 设置背景图片（网络图片 URL）
getBGImageURL: | 获取BoardId对应白板当前显示的背景图片
saveToAlbumWithFinish: | 将白板当前内容截图，保存到本地相册

### 2.6 多白板接口

接口 | 说明
---|---
currentBoardId | 获取当前白板的 ID
createSubBoard | 创建一个白板
switchToSubBoard: |  切换到指定白板
deleteSubBoard:stayBoard: | 删除白板并切换到指定白板
boardList | 获取当前所有的白板

### 2.7 文档接口
接口 | 说明
---|---
addFile:fileName: |  添加文档
deleteFile:stayBoardID: |  删除文档
getBoardIDsWithFid: |  获取文档对应的所有 boardID
getAllFileInfo | 获取所有文档信息(包括普通白板组)

## 3. 文档上传下载

文件上传下载方法位于`XFileManager.h`头文件中，如下：

接口 | 说明
---|---
uploadFile:onProgress:onFinish: |  上传文件到 COS 云存储 TXSDK 默认文件夹（/TIC/iOS）
downloadFile:onProgress:onFinish: |  下载 COS 云存储 TXSDK 默认文件夹（/TIC/iOS）中的文件
uploadFile:cosPath:onProgress:onFinish: |  上传文件到 COS 指定路径
downloadFileWithCosPath:onProgress:onFinish: |  下载 COS 指定路径中的文件

> 这里的 **下载接口** 只是为了方便开发者使用，开发者也可以上传文件之后拿到下载链接自行下载。

## 4. 文档展示功能详解
### 相关概念解释
* 默认白板：白板 SDK 初始化后内部会自动生成一个白板，这个白板是第一块白板，作为白板 SDK 展示的默认白板，不允许删除。

* 文件白板：即通过`addFile`接口生成的白板，一块文件白板对应文件的一页（底层实现为普通白板，设置其背景图为文件预览URL）。

* 普通白板：即非文件白板，调用`createSubBoard`方法创建的白板，可涂鸦，可设置/清除白板，默认白板属于普通白板。

* fid：文件唯一标识，由于一个文件对应一组白板，所以 fid 也可以理解为一个白板组的标识。
* boardID：白板 ID，白板唯一标识。

* boardID 生成规则：
    - 默认白板的 boardID 为固定值 #DEFAULT。
    - 其他白板的 boardID 为 xxxxxxx_fid （fid 为该白板所属文件(白板组)的唯一标识）。

* fid生成规则（fid 都以 # 号开头）
    - 普通白板的 fid 为固定值 #DEFAULT。
    - 文件白板的 fid 为 #xxxx。
    
>**注意：**文件在白板中的实现其实就是一组白板（文件的每一页对应一块白板），他们用一个 fid 来标识，这组白板中每个白板的 boardID 都会带上其所属文件（白板组）的 fid 当做后缀。

### 添加文档（以 PPT 为例）
1. 开发者首先调用上一节的文件上传方法将 PPT 文件上传到腾讯云对象存储 COS，获取到 PPT 每一页转码后的图片 URL 链接。

2. 然后调用`addFile`接口，将上一步获取到的 URL 数组，和文件名当做参数传入，SDK 内部会根据 URL 数量生成对应数量的白板，并生成一个该文件对应的文件唯一标识 **fid** 返回。

* 代码实例：

```objc
NSString *fid = [self.boardView addFile:urls fileName:fileName];
```

### 删除文档
1. 调用`deleteFile`接口，传入文件对应的 fid 和删除后要跳转到的白板 ID，deleteFile 内部会将该文件对应的白板全部删除。
> **注意：**普通白板组不能删除。

* 代码实例：

```objc
[self.boardView deleteFile:deleteFid stayBoardID:stayBoardID];
```


### 切换白板
1. 调用`switchToSubBoard`方法，传入 boardID 即可切换到对应白板。

* 代码实例：

```objc
[self.boardView switchToSubBoard:targetBoardID];
```

### 切换 PPT
1. 切换 PPT 其实也是切换白板

> **注意：**用户需要自己维护哪个 PPT 当前显示的是哪一页。

### 获取当前显示的白板
1. 调用`currentBoardId`接口，即可获得当前显示的白板 ID。

* 代码实例：

```objc
NSString *currentBoardId = self.boardView.currentBoardId;
```

### 根据 fid 获取文件对应的所有白板 ID
1. 调用`getBoardIDsWithFid`接口，传入 fid 即可

* 代码实例：

```objc
NSArray *boardIds = [self.boardView getBoardIDsWithFid:fid];
```

### 获取课堂内所有文件信息（PPT）
1. 调用`getAllFileInfo`方法即可获得当前课堂内所有的文件信息（调用 deleteFile 接口删除的文件不会返回）。
2. 该接口返回格式如下，业务层根据该接口返回的信息结合 fid 即可确定白板属于哪个 PPT 和该 PPT 的title：

```json
    [
        {
        "fid" : "",      // 文件唯一标识
        "title" : "",   // 文件名称
        }
        ...
    ]
```

### 推荐实现方案
1. 进房或者调用`addFile`添加文件后，调用`getAllFileInfo`可获得课堂内所有文件列表，用于展示。
2. 翻页时，先调用`currentBoardId`接口获得当前显示的白板 ID，再调用`getBoardIDsWithFid`接口获得当前文件所有白板 ID，即可得出当前显示的是哪一页，然后根据具体的翻页指令，调用`switchToSubBoard`调到对应的白板即可。


