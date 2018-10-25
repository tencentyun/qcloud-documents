本文将指导您的客户端如何将房间中的视频通过旁路直播分享给别人，如何将房间中视频录制成视频文件。

## 相关概念

* [旁路直播](/document/product/647/16826)

## 手动开启推流和录制
直接在房间模块中添加手动推流接口：
```Java
    private void startPush(boolean bRecord){
        ILivePushOption.RecordFileType recordFileType = bRecord ?
                ILivePushOption.RecordFileType.RECORD_HLS_FLV_MP4 : ILivePushOption.RecordFileType.NONE
        ILivePushOption option = new ILivePushOption()
                .encode(ILivePushOption.Encode.HLS_AND_RTMP)         // 旁路直播协议类型
                .setRecordFileType(recordFileType)      // 录制文件格式
                //手动推流自动录制时，如果需要后台识别特定的录制文件，用户可以通过这个字段做区分。
                // (使用这个字段时，控制台的“自动旁路直播”开关必须关闭)
                .setRecordId(123456);
        ILiveRoomManager.getInstance().startPushStream(option, new ILiveCallBack<ILivePushRes>() {
            @Override
            public void onSuccess(ILivePushRes data) {
                if (null != data.getUrls()){
                    // 遍历推流类型及地址
                    for (ILivePushUrl url : data.getUrls()){
                        // 处理播放地址
                    }
                }
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                // 处理推流失败
            }
        });
    }
```
>**注意：**
这个接口可以同时开启旁路直播和录制（录制无法单独开启）。
此处的 encode 用于配置旁路的视频流类型，目前支持RTMP、HLS 和 FLV。
setRecordFileType 设置录制的视频文件格式，目前支持 HLS、FLV 和 MP4，纯音频可以录制为MP3格式。

## 停止手动推流和录制

```Java
    private void stopPush(){
        ILiveRoomManager.getInstance().stopPushStream(0, // 直播码模式下填0即可
                new ILiveCallBack() {
            @Override
            public void onSuccess(Object data) {
                // 停止成功
            }

            @Override
            public void onError(String module, int errCode, String errMsg) {
                // 停止失败
            }
        });
    }
```
