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


## 2. 接口概述

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
    TXBoardBrushModelText,          // 文字输入
    TXBoardBrushModelApplePencil,   // Apple Pencil，iOS 9.1 及以上系统使用
};
```

接口 | 说明
---|---
-setBrushModel: | 设置白板工具类型

### 2.4 白板基本操作接口
接口 | 说明
---|---
- setBrushColor: | 设置画线、添加标准图形时线条的颜色
- getBrushColor | 获取当前画笔颜色
- setBrushWidth: | 设置画线、添加标准图形时线条的宽度
- getBrushWidth | 获取当前画笔宽度
- setEraserRadius: | 设置擦除效果的范围半径
- getEraserRadius: | 获取擦除效果的范围半径
- setBackgroundColor: | 设置当前白板背景颜色
- setGlobalBackgroundColor: | 设置全局白板背景颜色
- undo | 撤销上一步操作
- canUndo | 获取是否可以进行撤回操作
- redo | 重做上一步被撤回的操作
- canRedo | 获取是否可以进行重做操作
- clear: | 清空当前白板所有数据，包含背景图片
- clearDraws: | 清空当前白板涂鸦数据，不包含背景图片、PPT
- clearFileDraws: | 清空指定文件的涂鸦（不包括背景图片）
+ clearHistoryDataWithRoomID: | 清空指定课堂的历史数据（该方法为类方法，白板对象销毁后也能调用）

### 2.5 文字输入相关接口
接口 | 说明
---|---
- setTextColor: | 设置文字颜色
- getTextColor | 获取当前文字颜色
- setTextSize: | 设置文字大小

### 2.6 图片操作接口

接口 | 说明
---|---
- updateBgImageWithPath:mode:succ:failed: | 设置背景图片（本地图片路径）
- updateBgImageWithURL:mode:succ:failed: | 设置背景图片（网络图片 URL）
- updateCurrentImageMode | 设置当前背景图片显示模式
- getBGImageURL: | 获取BoardId对应白板当前显示的背景图片
- saveToAlbumWithFinish: | 将白板当前内容截图，保存到本地相册

### 2.7 多白板接口

接口 | 说明
---|---
- currentBoardId | 获取当前白板的 ID
- createSubBoard | 创建一个白板
- switchToSubBoard: |  切换到指定白板
- deleteSubBoard:stayBoard: | 删除白板并切换到指定白板
- boardList | 获取当前所有的白板

## 3. 文档展示功能介绍

### 必备知识点：

* 白板SDK实现文档的原理为多白板（白板组）。
* 
* 每个白板展示一页文档，即每个文档会对应一组白板。
* 
* 每个文档有一个 fid (文件唯一标识)。
* 
* 每个白板有一个 boardID。
* 
* 非文档白板的白板全部合成一个白板组，叫做普通白板，该白板组的 fid 为 #DEFAULT。
* 
### 添加文档（以 PPT 为例）

接口 | 说明
---|---
addFile:onProgress:onFinish: |  添加本地文档

调用`addFile`接口，传入本地文件路径即可，添加文档完成会在回调中通知，如果完成回调中的errror参数为空，则代表添加成功，添加成功后会自动跳转到文档的第一页。

* 代码实例：

```objc
[self.boardView addFile:filePath onProgress:^(int64_t bytesSent, int64_t totalBytesSent, int64_t totalBytesExpectedToSend) {
        // 计算上传进度
        CGFloat percent = totalBytesSent*1.0/totalBytesExpectedToSend*100;
        NSString *percentStr = [NSString stringWithFormat:@"%.2f%%", percent];
        NSLog(@"%@", percentStr);
    } onFinish:^(NSString *fid, NSError *error) {
        if (error) {
            // 添加文档失败
            return;
        }
        // 界面展示
        ...
    }];
```


### 获取课堂内文档信息

接口 | 说明
---|---
getAllFileInfo | 获取所有文档信息(包括普通白板组，fid 为 #DEFAULT)

调用`getAllFileInfo`方法即可获得当前课堂内所有的文件信息，返回的数据是一个 `TXBoardFileInfo` 数组：

```objc
/** 文件信息模型 */
@interface TXBoardFileInfo : NSObject

@property (nonatomic, copy) NSString *fid;                  //!< 文件标识
@property (nonatomic, copy) NSString *title;                //!< 文件名称
@property (nonatomic, copy) NSString *downloadURL;          //!< 文件下载地址
@property (nonatomic, strong) NSNumber *pageCount;          //!< 页数
@property (nonatomic, strong) NSNumber *currentPageIndex;   //!< 当前页数

@end
```

接口 | 说明
---|---
getCurrentFid |  获取当前展示的文件 fid

`getCurrentFid` 可以获取当前正在展示文件的 fid。

### 翻页/切换
接口 | 说明
---|---
prePage |  切换到当前文件的前一页
nextPage |  切换到当前文件的后一页

SDK 提供了便捷的翻页接口，调用以上两个方法即可轻松实现向前翻页，向后翻页。


接口 | 说明
---|---
switchPage: |  切换到当前文件的指定页（页码从0开始）

如果想跳页翻页，可以调用 `switchPage:` 该方法接收一个页码参数，可以跳转到当前文件的对应页面。

接口 | 说明
---|---
switchFile: |  切换到 fid 对应文件

调用 `switchFile:` 可实现切换文件，该方法接收文件的 fid 作为参数。切换文件会跳转到对应文件最近展示的页面。

### 删除文档
接口 | 说明
---|---
deleteFiles:stay: |  删除文档，支持一次删除多个

最后，如果要删除某个文档，只需调用 `deleteFiles`方法，传入要删除文件的 fid 即可。

