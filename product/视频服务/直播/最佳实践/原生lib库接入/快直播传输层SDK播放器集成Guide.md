## 简单介绍
快直播传输层 SDK（libLebConnection）提供基于原生 WebRTC 升级版的传输能力，用户仅需对已有播放器进行简单改造，即可接入快直播。在完全兼容标准直播的推流、云端媒体处理能力的基础上，实现高并发低延迟直播，帮助用户实现从现有的标准直播平滑地迁移到快直播上来。也可以帮助用户在现有 RTC 场景中快速实现低成本的大房间低延迟旁路直播。


## 功能介绍

- 音视频拉流，兼具优异的低延迟性能和抗弱网能力
- 视频支持H.264、H.265和 AV1，支持 B 帧，视频输出格式为视频帧裸数据（H.264/H.265为 AnnexB，AV1 为 OBU）
- 音频支持AAC和OPUS，音频输出格式为音频帧裸数据
- 支持 Android、iOS、Windows、Linux 和 Mac 平台


## 接入方式

### 基础接口说明

- 创建快直播连接
```
LEB_EXPORT_API LebConnectionHandle* OpenLebConnection(void* context, LebLogLevel loglevel);
```
- 注册回调函数
```
LEB_EXPORT_API void RegisterLebCallback(LebConnectionHandle* handle, const LebCallback* callback);
```
-  开始连接拉流
```
LEB_EXPORT_API void StartLebConnection(LebConnectionHandle* handle, LebConfig config);
```
- 停止连接
```
LEB_EXPORT_API void StopLebConnection(LebConnectionHandle* handle);
```
- 关闭连接
```
LEB_EXPORT_API void CloseLebConnection(LebConnectionHandle* handle);
```

### 回调接口说明
```
typedef struct LebCallback {
  // 日志回调
  OnLogInfo onLogInfo;
  // 视频信息回调
  OnVideoInfo onVideoInfo;
  // 音频信息回调
  OnAudioInfo onAudioInfo;
  // 视频数据回调
  OnEncodedVideo onEncodedVideo;
  // 音频数据回调
  OnEncodedAudio onEncodedAudio;
  // MetaData回调
  OnMetaData onMetaData;
  // 统计信息回调
  OnStatsInfo onStatsInfo;
  // 错误回调
  OnError onError;
} LebCallback;
```

>! 详细数据结构定义请见头文件 `leb_connection_api.h`。


### 接口调用流程
1. **创建 LEB 连接**：OpenLebConnection()
2. **注册各种回调函数**：RegisterXXXXCallback()
3. **开始连接拉流**：StartLebConnection()
4. **音视频裸数据回调输出**：
  - OnEncodedVideo()
  - OnEncodedAudio()
5. **停止连接**：StopLebConnection()
6. **关闭连接**：CloseLebConnection



### 接入示例
本 [示例](https://mp.weixin.qq.com/s/f3ct29ydzAjdJ1fIdOmHmQ) 基于 Android 端使用广泛的具有代表性开源播放器 ijkplayer，介绍接入快直播传输层 SDK 的方法及流程，其他平台可参考进行集成。

### 最新 SDK 下载
快直播传输层 libLebConnection SDK 请参见 [SDK 下载](https://github.com/tencentyun/libLebConnectionSDK/tree/main/libs/v1.0.3.2)。

## 集成常见问题解答

### 开发卡顿统计功能
由于关闭了 buffering，现可以通过统计渲染刷新时间间隔来统计卡顿参数。当视频渲染时间间隔大于一定阈值，记一次卡顿次数，并累计进卡顿时长。
以 ijkplayer 为例，以下内容演示卡顿统计的开发流程。

1. **代码修改**
  1. 在 VideoState、FFPlayer 结构体中添加卡顿统计需要用到的变量。
```diff
diff --git a/ijkmedia/ijkplayer/ff_ffplay_def.h b/ijkmedia/ijkplayer/ff_ffplay_def.h
index 00f19f3c..f38a790c 100755
--- a/ijkmedia/ijkplayer/ff_ffplay_def.h
+++ b/ijkmedia/ijkplayer/ff_ffplay_def.h
@@ -418,6 +418,14 @@ typedef struct VideoState {
     SDL_cond  *audio_accurate_seek_cond;
     volatile int initialized_decoder;
     int seek_buffering;
+
+    int64_t stream_open_time;
+    int64_t first_frame_display_time;
+    int64_t last_display_time;
+    int64_t current_display_time;
+    int64_t frozen_time;
+    int frozen_count;
+    float frozen_rate;
 } VideoState;
 
 /* options specified by the user */
@@ -720,6 +728,14 @@ typedef struct FFPlayer {
     char *mediacodec_default_name;
     int ijkmeta_delay_init;
     int render_wait_start;

     int low_delay_playback;
+    int frozen_interval;
     int high_level_ms;
     int low_level_ms;

     int64_t update_plabyback_rate_time;
     int64_t update_plabyback_rate_time_prev;
 } FFPlayer;
 
 #define fftime_to_milliseconds(ts) (av_rescale(ts, 1000, AV_TIME_BASE))
@@ -844,6 +860,15 @@ inline static void ffp_reset_internal(FFPlayer *ffp)
     ffp->pf_playback_volume             = 1.0f;
     ffp->pf_playback_volume_changed     = 0;
 
     ffp->low_delay_playback             = 0;
 
     ffp->high_level_ms                  = 500;
     ffp->low_level_ms                   = 200;
+    ffp->frozen_interval                = 200;
 
     ffp->update_plabyback_rate_time      = 0;
     ffp->update_plabyback_rate_time_prev = 0;

     av_application_closep(&ffp->app_ctx);
     ijkio_manager_destroyp(&ffp->ijkio_manager_ctx);
```
  2. **添加卡顿统计逻辑**
```diff
diff --git a/ijkmedia/ijkplayer/ff_ffplay.c b/ijkmedia/ijkplayer/ff_ffplay.c
index 714a8c9d..c7368ff5 100755
--- a/ijkmedia/ijkplayer/ff_ffplay.c
+++ b/ijkmedia/ijkplayer/ff_ffplay.c
@@ -874,6 +874,25 @@ static void video_image_display2(FFPlayer *ffp)
     VideoState *is = ffp->is;
     Frame *vp;
     Frame *sp = NULL;
+    int64_t display_interval = 0;
+
+    if (!is->first_frame_display_time){
+        is->first_frame_display_time = SDL_GetTickHR() - is->stream_open_time;
+    }
+    
+    is->last_display_time = is->current_display_time;
+    is->current_display_time = SDL_GetTickHR() - is->stream_open_time;
+    display_interval = is->current_display_time - is->last_display_time;
+    av_log(NULL, AV_LOG_DEBUG, "last_display_time:%"PRId64" current_display_time:%"PRId64" display_interval:%"PRId64"\n", is->last_display_time, is->current_display_time, display_interval);
+
+    if (is->last_display_time > 0) {
+        if (display_interval > ffp->frozen_interval) {
+            is->frozen_count += 1;
+            is->frozen_time += display_interval;
+        }
+    }
+    is->frozen_rate = (float) is->frozen_time / is->current_display_time;
+    av_log(NULL, AV_LOG_DEBUG, "frozen_interval:%d frozen_count:%d frozen_time:%"PRId64" is->current_display_time:%"PRId64" frozen_rate: %f ", ffp->frozen_interval, is->frozen_count, is->frozen_time, is->current_display_time, is->frozen_rate);
 
     vp = frame_queue_peek_last(&is->pictq);
```
>! 本示例中卡顿阈值 frozen_interval 初始化值为`200(ms)`，可根据业务需要进行调整。
2. **卡顿参数统计测试**
使用 QNET 模拟弱网环境进行测试，步骤如下：
  1. 下载 [QNET 网络测试工具](https://wetest.qq.com/product/qnet/)。
  2. 打开QNET，单击**新增** > **模版类型** > **自定义模版**，根据需要配置弱网模版和参数（下图配置为下行网络30%随机丢包）。
  3. 在程序列表中选择测试程序。
  4. 开启弱网进行测试。

>! 为便于测试，可将上述卡顿参数的修改，通过 jni 将数据传递到 Java 层进行显示。



### 解决播放有噪音问题（Android soundtouch 优化）

根据 buffer 水位调整播放速率的修改，会用到 soundtouch 进行音频变速实现。但在网络波动较大、buffer 水位调整频率高需要多次变速处理时，原生 ijkplayer 对于 soundtouch 的调用可能出现噪音问题，可参考如下代码进行优化：

在调用 soundtouch 进行变速处理时，如果是低延时播放模式，则全部 buffer 都是用 soundtouch 进行 translate。

```diff
diff --git a/ijkmedia/ijkplayer/ff_ffplay.c b/ijkmedia/ijkplayer/ff_ffplay.c
index 714a8c9d..c7368ff5 100755
--- a/ijkmedia/ijkplayer/ff_ffplay.c
+++ b/ijkmedia/ijkplayer/ff_ffplay.c
@@ -2579,7 +2652,7 @@ reload:
         int bytes_per_sample = av_get_bytes_per_sample(is->audio_tgt.fmt);
         resampled_data_size = len2 * is->audio_tgt.channels * bytes_per_sample;
 #if defined(__ANDROID__)
-        if (ffp->soundtouch_enable && ffp->pf_playback_rate != 1.0f && !is->abort_request) {
+        if (ffp->soundtouch_enable && (ffp->pf_playback_rate != 1.0f || ffp->low_delay_playback) && !is->abort_request) {
             av_fast_malloc(&is->audio_new_buf, &is->audio_new_buf_size, out_size * translate_time);
             for (int i = 0; i < (resampled_data_size / 2); i++)
             {

```



### 解决打开 MediaCodec 后，H.265不使用 MediaCodec 解码问题
快直播传输层的特色是支持 H.265 格式的视频流，但是原生 ijkplayer 在 **Settings** 中勾选打开 `Using MediaCodec` 后，H.265的视频流不会使用 MediaCodec 进行解码。可参考如下代码进行优化：
```diff
diff --git a/ijkmedia/ijkplayer/ff_ffplay_options.h b/ijkmedia/ijkplayer/ff_ffplay_options.h
index b021c26e..958b3bae 100644
--- a/ijkmedia/ijkplayer/ff_ffplay_options.h
+++ b/ijkmedia/ijkplayer/ff_ffplay_options.h
@@ -178,8 +178,8 @@ static const AVOption ffp_context_options[] = {
         OPTION_OFFSET(vtb_handle_resolution_change),    OPTION_INT(0, 0, 1) },
 
     // Android only options
-    { "mediacodec",                             "MediaCodec: enable H.264 (deprecated by 'mediacodec-avc')",
-        OPTION_OFFSET(mediacodec_avc),          OPTION_INT(0, 0, 1) },
+    { "mediacodec",                             "MediaCodec: enable all_videos (deprecated by 'mediacodec_all_videos')",
+        OPTION_OFFSET(mediacodec_all_videos),   OPTION_INT(0, 0, 1) },
     { "mediacodec-auto-rotate",                 "MediaCodec: auto rotate frame depending on meta",
         OPTION_OFFSET(mediacodec_auto_rotate),  OPTION_INT(0, 0, 1) },
     { "mediacodec-all-videos",                  "MediaCodec: enable all videos",
```

