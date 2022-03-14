本篇教程向大家介绍如何完成合唱的基础功能。
## 版本支持
本页文档所描述功能，在腾讯云视立方中支持情况如下：

| 版本名称 | 基础直播 Smart | 互动直播 Live | 短视频 UGSV | 音视频通话 TRTC | 播放器 Player | 全功能 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 支持情况 | -  | -  | &#10003;  | -  | -  | &#10003;  |
| SDK 下载 <div style="width: 90px"/> | [下载](https://vcube.cloud.tencent.com/home.html?sdk=basicLive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=interactivelive) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=shortVideo) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=video) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=player) | [下载](https://vcube.cloud.tencent.com/home.html?sdk=allPart) |

不同版本 SDK 包含的更多能力，具体请参见 [SDK 下载](https://cloud.tencent.com/document/product/1449/56978)。


## 过程简介

1. 在界面上放两个 View, 一个用来播放，一个用来录制。
2. 再放一个按钮和进度条来开始录制和显示进度。
3. 录制与源视频相同的时长后停止。
4. 把录好的视频与源视频左右合成。
5. 预览合成好的视频。

## 界面搭建

在录制界面 TCVideoRecordActivity 的 `activity_video_record.xml` 中创建两个 view，左半边是录制界面，右半边是播放界面。
![](https://main.qcloudimg.com/raw/db388cf497615ac5f1ab58238a765e93.png)

## 代码部分

对于合唱功能主要使用三大块功能：播放、录制、以及录制后和原视频进行合成，这三个功能对应到 SDK 的类为： TXVideoEditer、TXUGCRecord、TXVideoJoiner，其中播放也可以换成 TXVodPlayer 去播放。

1. 从小视频主页的视频列表中，选择一个视频进入播放界面 TCVodPlayerActivity，单击右下角的“合拍”按钮。
首先会下载该视频到本地 sdcard 中，并获取该视频的音频采样率以及 FPS 等信息后进入录制界面。
2. 进入录制界面 TCVideoRecordActivity 进行合唱。需要注意以下几点：
 - 录制进度条以跟拍视频的进度为最大长度。
 - 保证录制视频的帧率和合唱视频的帧率一致，否则可能出现音画不同步的现象。
 - 保证录制视频的音频采样率和合唱视频的音频采样率一致，否则可能出现音画不同步的现象。
 - 录制设置渲染模式为自适应模式，在9:16的宽高比时能等比例缩放。
 - Android 的录制需要设置静音，否则会造成与跟拍视频的“二重唱”。
<dx-codeblock>
::: android 
// 录制的界面
mVideoView = mVideoViewFollowShotRecord;
// 播放的视频
mFollowShotVideoPath = intent.getStringExtra(TCConstants.VIDEO_EDITER_PATH);
mFollowShotVideoDuration = (int)(intent.getFloatExtra(TCConstants.VIDEO_RECORD_DURATION, 0) * 1000);
initPlayer();
// 录制进度条以跟拍视频的进度为最大长度，fps 以跟拍视频的 fps 为准
mMaxDuration = (int)mFollowShotVideoDuration;
mFollowShotVideoFps = intent.getIntExtra(TCConstants.RECORD_CONFIG_FPS, 20);
mFollowShotAudioSampleRateType = intent.getIntExtra(TCConstants.VIDEO_RECORD_AUDIO_SAMPLE_RATE_TYPE, TXRecordCommon.AUDIO_SAMPLERATE_48000);
// 初始化合拍的接口
mTXVideoJoiner = new TXVideoJoiner(this);
mTXVideoJoiner.setVideoJoinerListener(this);
:::
</dx-codeblock>
<dx-codeblock>
::: android 
// 播放器初始化，这里使用 TXVideoEditer，也可以使用 TXVodPlayer
mTXVideoEditer = new TXVideoEditer(this);
mTXVideoEditer.setVideoPath(mFollowShotVideoPath);
TXVideoEditConstants.TXPreviewParam param = new TXVideoEditConstants.TXPreviewParam();
param.videoView = mVideoViewPlay;
param.renderMode = TXVideoEditConstants.PREVIEW_RENDER_MODE_FILL_EDGE;
mTXVideoEditer.initWithPreview(param);
:::
</dx-codeblock>
<dx-codeblock>
::: android 
customConfig.videoFps = mFollowShotVideoFps;
customConfig.audioSampleRate = mFollowShotAudioSampleRateType; // 录制的视频的音频采样率必须与跟拍的音频采样率相同
customConfig.needEdit = false;
mTXCameraRecord.setVideoRenderMode(TXRecordCommon.VIDEO_RENDER_MODE_ADJUST_RESOLUTION); // 设置渲染模式为自适应模式
mTXCameraRecord.setMute(true); // 跟拍不从喇叭录制声音，因为跟拍的视频声音也会从喇叭发出来被麦克风录制进去，造成跟原视频声音的"二重唱"。
:::
</dx-codeblock>
3. 接下来就可以开始录制了，在录制到最大长度后，会回调 onRecordComplete，继续完成拼接部分，这里需要指定两个视频在结果中的位置。
<dx-codeblock>
::: android 
private void prepareToJoiner(){
    List<String> videoSourceList = new ArrayList<>();
    videoSourceList.add(mRecordVideoPath);
    videoSourceList.add(mFollowShotVideoPath);
    mTXVideoJoiner.setVideoPathList(videoSourceList);
    mFollowShotVideoOutputPath = getCustomVideoOutputPath("Follow_Shot_");
    // 以左边录制的视频宽高为基准，右边视频等比例缩放
    int followVideoWidth;
    int followVideoHeight;
    if ((float) followVideoInfo.width / followVideoInfo.height >= (float)recordVideoInfo.width / recordVideoInfo.height) {
        followVideoWidth = recordVideoInfo.width;
        followVideoHeight = (int) ((float)recordVideoInfo.width * followVideoInfo.height / followVideoInfo.width);
    } else {
        followVideoWidth = (int) ((float)recordVideoInfo.height * followVideoInfo.width / followVideoInfo.height);
        followVideoHeight = recordVideoInfo.height;
    }

    TXVideoEditConstants.TXAbsoluteRect rect1 = new TXVideoEditConstants.TXAbsoluteRect();
    rect1.x = 0;                     //第一个视频的左上角位置
    rect1.y = 0;
    rect1.width = recordVideoInfo.width;   //第一个视频的宽高
    rect1.height = recordVideoInfo.height;

    TXVideoEditConstants.TXAbsoluteRect rect2 = new TXVideoEditConstants.TXAbsoluteRect();
    rect2.x = rect1.x + rect1.width; //第2个视频的左上角位置
    rect2.y = (recordVideoInfo.height - followVideoHeight) / 2;
    rect2.width = followVideoWidth;  //第2个视频的宽高
    rect2.height = followVideoHeight;

    List<TXVideoEditConstants.TXAbsoluteRect> list = new ArrayList<>();
    list.add(rect1);
    list.add(rect2);
    mTXVideoJoiner.setSplitScreenList(list, recordVideoInfo.width + followVideoWidth, recordVideoInfo.height); //第2、3个 param：两个视频合成画布的宽高
    mTXVideoJoiner.splitJoinVideo(TXVideoEditConstants.VIDEO_COMPRESSED_540P, mFollowShotVideoOutputPath);
}
:::
</dx-codeblock>
4. 监听合成的回调，在 onJoinComplete 后跳转到预览界面播放。
<dx-codeblock>
::: android 
@Override
public void onJoinComplete(TXVideoEditConstants.TXJoinerResult result) {
    mCompleteProgressDialog.dismiss();
    if(result.retCode == TXVideoEditConstants.JOIN_RESULT_OK){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                isReadyJoin = true;
                startEditerPreview(mFollowShotVideoOutputPath);
                if(mTXVideoEditer != null){
                    mTXVideoEditer.release();
                    mTXVideoEditer = null;
                }
            }
        });
    }else{
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Toast.makeText(TCVideoRecordActivity.this, "合成失败", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
:::
</dx-codeblock>

至此就完成了全部合唱的基础功能，完整代码请参见 [小视频源码](https://cloud.tencent.com/document/product/1449/56977#video_app)。
