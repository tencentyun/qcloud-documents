本文将指导您如何将房间中的视频通过旁路直播分享给别人，以及如何将房间中视频录制成视频文件。

## 相关概念

* [旁路直播](/document/product/647/16826)

## 手动旁路直播和录制

在某些情况下，用户可能不想要所有视频都进行录制，可以通过 iLiveSDK 手动控制旁路直播和录制。

## 手动开启推流和录制
 手动录制的开始和结束分别调用 SDK 的 startPushStream() 和 stopPushStream() 接口，实例代码如下：
* 开始旁路直播
  ```c++
    PushStreamOption pushOpt;
    pushOpt.pushDataType = E_PushCamera; //旁路直播数据类型
    pushOpt.encode = HLS_AND_RTMP; //旁路直播所用协议
    pushOpt.recordFileType = RecordFile_HLS_FLV_MP4; //旁路直播时，录制视频文件格式
    GetILive()->startPushStream( pushOpt, [](PushStreamRsp &value, void *data){
        //旁路直播成功,在value参数中包含了旁路直播成功的url信息;
    }, [](int code, const char * desc, void* data){
        //旁路直播失败
    }, NULL );
  ```

## 停止手动推流和录制
 ```c++
    E_PushDataType pushDataType = E_PushCamera;
    GetILive()->stopPushStream(0, pushDataType, [](void* data){
        //停止旁路直播成功;
    }, [](int code, const char *desc, void* data){
        //停止旁路直播失败;
    }, NULL); //第一个参数(channelId)是为了兼容老版本的频道模式的，现在此模式已废弃，直接填0即可;
  ```

* 补充说明：
    如果开了自动旁路直播，打开摄像头就已经开始自动旁路直播了，调用此接口，只是获取旁路直播地址而已；结束推流接口会无效。
