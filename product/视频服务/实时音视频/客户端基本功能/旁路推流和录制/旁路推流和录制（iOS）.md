本文将指导您如何将房间中的视频通过旁路直播分享给别人，以及如何将房间中视频录制成视频文件。

## 相关概念

* [旁路直播](/document/product/647/16826)

## 推流录制的 4 种方式

旁路直播开启方式  | 旁路直播录制方式  | 多录制格式|  录制回调 | 开发便利程度 | 可靠性| 资源消耗
:-----: | :-----: | :-----: |:-----: |:-----: | :-----:| :-----:
自动|自动 |FLV/HLS/MP4|✔️|※※※※|※※※※|※
手动|自动 |FLV/HLS/MP4|✔️|※※※|※※※|※※
自动|手动 |MP4|❌|※※|※※|※※※
手动|手动 |MP4|❌|※|※|※※※※

>自动旁路推流和自动旁路直播录制是最简单的方式，也是目前我们推荐的方式。

## 手动旁路直播和录制

在某些情况下，用户可能不想要所有视频都进行录制，可以通过 iLiveSDK 手动控制旁路直播和录制。

## 手动开启推流和录制
 手动推流接口如下：
* 开始旁路直播
 ```objc
    // 创建推流配置对象
    ILiveChannelInfo *info = [[ILiveChannelInfo alloc] init];
    info.channelName = [NSString stringWithFormat:@"前缀_%@",[[ILiveLoginManager getInstance] getLoginId]];
    info.channelDesc = [NSString stringWithFormat:@"推流描述字符串"];

    ILivePushOption *option = [[ILivePushOption alloc] init];
    option.channelInfo = info;
    option.encodeType = ILive_ENCODE_RTMP; //使用RTMP协议旁路直播
    option.recrodFileType = ILive_RECORD_FILE_TYPE_MP4; //旁路直播时，如果需要自动录制，则填写自动录制时生成文件的格式，如果不需要自动录制，则不需要处理本字段    
    // 调用开始推流接口开始推流
    [[ILiveRoomManager getInstance] startPushStream:option succ:^(id selfPtr) {
    //旁路推流成功，返回的为`AVStreamerResp`类型的对象，其中包含了旁路直播成功的url信息;
    } failed:^(NSString *module, int errId, NSString *errMsg) {
    //旁路推流失败
    }];
 ```

## 停止手动推流和录制

 ```objc
    // 调用停止旁路推流接口，参数为要停止推流的频道ID数组，channelId在开启推流成功的回调中会返回
    [[ILiveRoomManager getInstance] stopPushStreams:@[channelId] succ:^{
        //停止旁路直播成功;
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        //停止旁路直播失败;
    }];
 ```

* 补充说明：
    如果开了自动旁路直播，打开摄像头就已经开始自动旁路直播了，调用此接口，只是获取旁路直播地址而已；结束推流接口会无效。
