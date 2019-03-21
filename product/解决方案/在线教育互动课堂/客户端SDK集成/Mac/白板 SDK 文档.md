## 1. TXBoardSDK 

`TXBoardSDK.framework`即白板 SDK，提供画笔、橡皮擦、背景图设置、标准图形、框选等基本功能，同时还支持文档展示和多端互动。

>! TICSDK 包含白板 SDK，用户只需创建白板对象，并调用白板对象的相应接口来操作白板即可。

#### 头文件

类名 | 主要功能
--------- | ---------
TXBoardSDK.h | SDK 的全局管理类。
TXBoardView.h | 白板视图类，白板SDK的主要操作类，包含了所有白板相关的接口和展示逻辑。
TXBoardCommon.h | 白板定义类，定义了一些与白板视图相关的枚举，类和代理方法。
TXFileManager.h | 文件管理类，内部封装了腾讯云对象云存储 COS SDK，负责文件（PPT、wrod、Excel、pdf、图片等）的上传、下载、在线转码预览等（一般无需使用该类接口，添加文件接口已封装在 TXBoardView.h 中）。


## 2. SDK 接口

### 2.1 初始化 SDK
接口 | 说明
---|---
-initSDK:uid:userSig:succ:failed: | 初始化白板 TXBoardSDK

使用`TXBoardSDK`前需先执行初始化，初始化方法请参见`TXBoardSDK.h`。
>?使用 TICSDK 时无需单独调用该接口，TICSDK 内部已将`TXBoardSDK`初始化。


### 2.2 创建白板
接口 | 说明
---|---
-initWithRoomID: | 初始化 TXBoardView

展示涂鸦和课件，需先创建一块白板，`TXBoardView`为唯一指定的初始化接口，需传入一个房间 ID 作为参数（即 TIC 中创建房间填入的 roomID），示例代码如下：

```objc
TXBoardView *boardView = [[TXBoardView alloc] initWithRoomID:_classID];
boardView.frame = ...;
```

>!为保证数据展示的准确性，各端白板视图的长宽比需保持一致，demo 中为16：9。

### 2.3 选择白板工具
白板支持各种工具，定义为一个枚举，用户可根据实际场景设置白板。

接口 | 说明
---|---
-setBrushModel: | 设置白板工具类型

```objc

/** 白板工具类型 */
typedef NS_ENUM(NSInteger, TXBoardBrushModel)
{
    TXBoardBrushModelNone = 0,      //无效果(触摸无响应，相当于禁用画笔)
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
    TXBoardBrushModelLaserPen,      // 激光笔
};
```



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
- getBGImageURL: | 获取 BoardId 对应白板当前显示的背景图片

### 2.7 多白板接口

接口 | 说明
---|---
- currentBoardId | 获取当前白板的 ID
- createSubBoard | 创建一个白板
- switchToSubBoard: |  切换到指定白板
- deleteSubBoard:stayBoard: | 删除白板并切换到指定白板
- boardList | 获取当前所有的白板

## 3. 文档展示功能介绍

* 白板 SDK 实现文档的原理为多白板（白板组）。 
* 每个白板展示一页文档，即每个文档会对应一组白板。
* 每个文档有一个 fid（文件唯一标识）。
* 每个白板有一个 boardID。
* 非文档白板的白板全部合成一个白板组，为普通白板，该白板组的 fid 为 #DEFAULT。

### 3.1 添加文档（以 PPT 为例）

接口 | 说明
---|---
addFile:onProgress:onFinish: |  添加本地文档

调用`addFile`接口，传入本地文件路径，添加文档完成后会在回调中通知，如果完成回调中的errror参数为空，表示添加成功，添加成功后会自动跳转到文档的第一页。

代码示例：

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


### 3.2 获取课堂内文档信息

接口 | 说明
---|---
getAllFileInfo | 获取所有文档信息（包括普通白板组，fid 为 #DEFAULT）

调用`getAllFileInfo`可获得当前课堂内所有的文件信息，返回数据是一个 `TXBoardFileInfo` 数组。
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

调用`getCurrentFid` 接口可以获取当前正在展示文件的 fid。

### 3.3 翻页/切换
接口 | 说明
---|---
prePage |  切换到当前文件的前一页
nextPage |  切换到当前文件的后一页

调用以上两个接口可实现向前翻页和向后翻页。

接口 | 说明
---|---
switchPage: |  切换到当前文件的指定页（页码从0开始）

调用 `switchPage:` 接口可跳页翻页，接收一个页码参数，会跳转到当前文件的对应页面。

接口 | 说明
---|---
switchFile: |  切换到 fid 对应文件

调用 `switchFile:` 接口可切换文件，接收文件的 fid 作为参数，切换文件会跳转到对应文件最近展示的页面。

### 3.4 删除文档
接口 | 说明
---|---
deleteFiles:stay: |  删除文档，支持一次删除多个

调用 `deleteFiles`接口，传入要删除文件的 fid 即可删除文档。

