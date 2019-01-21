### [1.6.6] 2019-01-14
#### 新增
1. 白板增加 Apple Pencil 模式开关接口，可开启或关闭 Apple Pencil 模式。

```objc
/**
 打开/关闭 apple pencil 模式，apple pencil 模式下只能响应 apple pencil 触发的操作
 
 @param isEnable YES:打开 NO:关闭
 */
- (void)enableApplePencilMode:(BOOL)isEnable NS_AVAILABLE_IOS(9_1);
```


### [1.6.5] 2019-01-03
#### 优化
1. 修复橡皮擦不能擦除文字的问题。

#### 新增
1. 画笔增加 Apple Pencil 模式 `TXBoardBrushModelApplePencil`。
2. TICSDK 增加带回调的初始化方法。

```objc
/**
 @brief 初始化SDK，带回调接口
 
 @param SDKAppID    腾讯云控制台注册的应用ID
 @param onFinish    完成回调，resultCode：0代表成功，其他代表失败(6012 请求超时)
 */
- (void)initSDK:(NSString *)SDKAppID onFinish:(void(^)(int resultCode))onFinish;
```

### [1.6.4] 2018-12-25
#### 优化
1. 优化文档 URL 加载功能，增加预加载逻辑。
1. 修复收到 roomDisconnect 回调后，群组被解散问题。
2. 修复 enableMic 接口无权限还能调用成功问题。

### [1.6.3] 2018-12-17
#### 新增
1. 增加多端同步缩放功能。

#### 优化
1. 下载文件接口 bug 修复。
2. 修复了其他一些 bug。

### [1.6.2] 2018-11-26
#### 优化
1. 修复了一些 bug。

### [1.6.1] 2018-11-16
#### 优化
1. 拉取历史数据文档信息去重。
2. 修复黑白颜色显示不对问题。
3. 修复其他一些 bug。

### [1.6.0] 2018-11-09
#### 新增
1. `TXBoardSDK`新增文字输入功能：

```objc
[self.boardView setBrushModel:TXBoardBrushModelText];
```
2. 自己被老师踢出课堂会在以下回调抛出（此时`members`中`identifier`为自己）：

```
/**
 *  @brief 有人退出（或者被踢出）课堂时的通知回调
 *
 *  @param members 退出成员的identifier（NSString*）列表
 */
-(void)onMemberQuit:(NSArray*)members;
```

#### 优化
1. 修复了一些 bug。

### [1.5.6] 2018-10-25
#### 优化
1. 修复了一些 bug。

### [1.5.4] 2018-10-19
#### 优化
1. 修复了一些 bug。

#### 新增
1. 新增录制相关接口。

### [1.5.3] 2018-10-08
#### 变更
1. SDK 主动退出音视频房间时（`onRoomDisconnect:`回调），不销毁 IM 群组。

#### 优化
1. 修复了一些 bug。

### [1.5.2] 2018-09-11
#### 变更
1. `TXFileManager` 初始化 COS 接口去掉`SDKAPPID`参数： 

```objc
- (int)initCosWithConfig:(TXCosConfig *)config;
```

#### 优化
1. 修复了一些 bug。


### [1.5.1] 2018-09-07
#### 变更
1. TXBoardSDK 文档接口重构，整合 COS 文件上传，接口更加易用。

#### 新增
1. TXBoardSDK 新增清空指定课堂历史数据接口：

```objc
/**
 清空【指定课堂】的历史数据（该方法为类方法，白板对象销毁后也能调用）
 
 @param roomID 课堂ID
 */
+ (void)clearHistoryDataWithRoomID:(int)roomID;
```

### [1.5.0] 2018-09-03
#### 变更
1.去除`TXBoardViewDelegate`中的`getBoardDataConfig`方法：

```objc
/**
 获取白板所需外部参数，包含uid、userSig、roomID（这些值发送改变时需要重新设置）
 */
- (TXBoardDataConfig *)getBoardDataConfig;
```

2.去掉`TICManger`初始化方法中的`accountType`参数：

```objc
- (int)initSDK:(NSString *)SDKAppID;
```

3.`TICManger`中的 IM 消息收/发方法由原来的 4 个合并为 2 个。

#### 新增
1.`TXBoardSDK`新增白板 SDK 初始化方法：

```objc
/**
 @brief 初始化SDK，使用白板SDK第一个调用的接口 (使用 TICSDK 无需调用该接口，单独使用TXBoardSDK的开发者，需手动调用该接口初始化，建议在登录IM时调用)
 
 @param SDKAppID    腾讯云控制台注册的应用ID
 @param uid 登录时的用户id
 @param userSig 登录时的用户签名
 @param succ 成功回调，返回的code暂时无用
 @param failed 失败回调
 */
+ (void)initSDK:(NSString *)SDKAppID uid:(NSString *)uid userSig:(NSString *)userSig succ:(void (^)(int code))succ failed:(void (^)(int errCode, NSString *errMsg))failed;
```

2.`TICManager`增加课堂销毁方法，与创建课堂方法对应：

```
/**
 @brief 销毁课堂（老师端调用）
 
 @param roomID 课堂ID，课堂唯一标识（课堂销毁成功后，roomID将会被回收，可再次使用该roomID创建房间）
 */
- (void)destroyClassroom:(int)roomID succ:(TCIVoidBlock)succ failed:(TCIErrorBlock)failed;
```

#### 优化
1. 激光点乱序问题修复。

### [1.2.2] 2018-08-23
#### 变更
1. TICSDK 接口整理，将 TICSDK.h 中的接口移动到 TICManger.h 中。
2. TXBoardView.framework 更改为 TXBoardSDK.framework，增加 TXBoardSDK.h 头文件。
3. TICSDK 文档上传下载功能 (TXFileManager) 移动到 TXBoardSDK 内部。
4. TXBoardSDK 移除了图片上传下载代理方法，移动到 SDK 内部实现，减少 SDK 接入工作量。

```objc
/**
 上传图片
 */
- (void)uploadImage:(NSString *)imagePath succ:(TXSuccBlock)succ failed:(TXFailBlock)failed;

/**
 下载图片
 */
- (void)downloadImage:(NSString *)imageURL succ:(void (^)(UIImage *image))succ failed:(TXFailBlock)failed;
```

#### 新增
1. SDK 提供公共 COS 账户，无需客户自行申请配置 COS 账号。
2. 白板增加缩放拖拽功能（本地操作）。

```objc
> TXBoardCommon.h

/** 白板工具类型 */
typedef NS_ENUM(NSInteger, TXBoardBrushModel)
{
    ...
    TXBoardBrushModelTransform      // 缩放(双指)/移动(单指)
};

```

#### 优化
1. 优化涂鸦画线策略，使涂鸦更加平滑。
2. 修改 FID 生成规则，兼容短时间上传多个文档的场景。
3. 不再显示起点和终点重合的标准图形。

### [1.2.0] 2018-08-03
#### 新增
1. TICSDK 增加文档上传转码功能。
2. TICSDK 增加退出课堂不退出群组方法。
3. 白板 SDK 增加文档功能相关接口。

#### 优化
1. TICSDK addBoardView 接口增加完成回调，用来通知拉取课堂历史消息完成事件。

```objc
/**
 @brief 添加白板到 TICManager【使用白板必调】，并拉取课堂历史数据
 @discussion 方法内部不会对 TXBoardView 对象进行强引用，只是将 boardView 的代理设置为 TICManager，同时只能添加一个，重复添加以后添加的为准
 
 @param boardView 用户创建的白板对象
 @param loadFinish 拉取完成回调（拉取失败会发挥错误码和错误信息，拉取成功则 errCode 为0，errMsg 为 nil）
 */
- (void)addBoardView:(TXBoardView *)boardView andLoadHistoryData:(void (^)(int errCode, NSString *errMsg))loadFinish;
```


### [1.1.3] 2018-07-24
#### 优化
1. TICSDK 优化进房逻辑，增加原始消息类型收发方法。
1. 白板 SDK 内部逻辑优化，性能提升。
2. 白板 SDK 优化数据上报格式，增加上报开关。

### [1.1.0] 2018-07-11
#### 优化
1. 使用实时音视频 SDK 升级版（云上环境，线路优化）。
2. 修复白板若干 bug，完善白板 SDK 体验。

>!1.1.0版本以上的音视频 SDK（IliveSDK）和之前的版本默认不互通（可手动切换环境来互通），建议用户户统一升级到该版本以上。

### [1.0.3] 2018-07-06
#### 优化
1. 退出房间时，兼容房间不存在情况。
2. 白板 SDK 课堂数据拉取优化。

### [1.0.1] 2018-06-29
#### 优化
1. 成员加入课堂和退出课堂事件回调优化，退出课堂事件包含成员被踢情况。
2. 图片下载优化。

### [1.0.0] 2018-06-13
#### 新增
1.0.0版本发布，包含以下功能：

1. 账号登录。
2. 创建、加入、退出课堂。
3. 在线课堂线上音视频互动。
4. 数字白板功能。
5. 课堂 IM 消息互动。









