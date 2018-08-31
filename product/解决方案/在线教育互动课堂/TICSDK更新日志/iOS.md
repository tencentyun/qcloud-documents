## [1.2.1] - 2018-08-23
### 变更
1. TICSDK 接口整理，将TICSDK.h中的接口移动到 TICManger.h 中
2. TXBoardView.framework 更改为 TXBoardSDK.framework，增加TXBoardSDK.h 头文件
3. TICSDK 文档上传下载功能 (TXFileManager) 移动到 TXBoardSDK 内部
4. TXBoardSDK 移除了图片上传下载代理方法，移动到SDK内部实现，减少SDK接入工作量

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

### 新增
1. SDK 提供公共 COS 账户，无需客户自行申请配置 COS 账号
2. 白板增加缩放拖拽功能（本地操作）

```objc
> TXBoardCommon.h

/** 白板工具类型 */
typedef NS_ENUM(NSInteger, TXBoardBrushModel)
{
    ...
    TXBoardBrushModelTransform      // 缩放(双指)/移动(单指)
};

```

### 优化
1. 优化涂鸦画线策略，使涂鸦更加平滑

## [1.2.0] - 2018-08-03
### 新增
1. TICSDK 增加文档上传转码功能；
2. TICSDK 增加退出课堂不退出群组方法；
3. 白板 SDK 增加文档功能相关接口。

### 优化
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


## [1.1.3] - 2018-07-24
### 优化
1. TICSDK 优化进房逻辑，增加原始消息类型收发方法；
1. 白板 SDK 内部逻辑优化，性能提升；
2. 白板 SDK 优化数据上报格式，增加上报开关。

## [1.1.0] - 2018-07-11
### 优化
1. 使用实时音视频 SDK 升级版（云上环境，线路优化）；
2. 修复白板若干 bug，完善白板 SDK 体验。

> **注意：**
> 1.1.0 版本以上的音视频 SDK（IliveSDK）和之前的版本默认不互通（可手动切换环境来互通），建议客户统一升级到该版本以上。

## [1.0.3] - 2018-07-06
### 优化
1. 退出房间时，兼容房间不存在情况；
2. 白板 SDK 课堂数据拉取优化。

## [1.0.1] - 2018-06-29
### 优化
1. 成员加入课堂和退出课堂事件回调优化，退出课堂事件包含成员被踢情况；
2. 图片下载优化。

## [1.0.0] - 2018-06-13
### 新增
1.0.0 版本发布，包含以下功能：

1. 账号登录；
2. 创建、加入、退出课堂；
3. 在线课堂线上音视频互动；
4. 数字白板功能；
5. 课堂 IM 消息互动。





