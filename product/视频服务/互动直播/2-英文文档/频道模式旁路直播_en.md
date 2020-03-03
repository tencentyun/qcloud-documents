## Non-interactive Broadcasting
Non-interactive broadcasting feature can transcode the uplink ILVB data to a general format for pushing and distributing, to help users watch videos through Web or streaming media players.<br/><br/>
**You can use the non-interactive broadcasting feature only after the Tencent Cloud LVB service is activated in the console**.

### 1 Client SDK APIs
#### Android
##### Starting Non-interactive Broadcasting
###### 1. Configure Push Parameters
```
ILivePushOption option = new ILivePushOption();
option.channelName("New FreeShow push");
option.encode(TIMAvManager.StreamEncode.RTMP);
```

* Push parameter: ILivePushOption

Field Name | Field Type | Default Value | Description
:--:|:--:|:--:|:--:
channelName | String | Optional | Configure channel name
channelDesc | String | Optional | Configure channel description
channelPassword | String | Optional | Configure channel playback password
record | boolean | NO | Whether to enable recording at the same time
waterMark | boolean | NO | Whether to enable watermark
waterMarkId | long | Optional | Watermark ID
sdkType | TIMAvManager.SDKType | Optional | Configure the current SDK type
rateType | TIMAvManager.RateType | Original bitrate | Supported bitrate
encode | TIMAvManager.StreamEncode | RTMP | Configure push encoding type

###### 2. Start Non-interactive Push

```
ILiveRoomManager.getInstance().startPushStream(option, new ILiveCallBack<TIMAvManager.StreamRes>() {
        @Override
        public void onSuccess(TIMAvManager.StreamRes data) {
            //Non-interactive push is successful
            List<TIMAvManager.LiveUrl> liveUrls = data.getUrls();
            streamChannelID = data.getChnlId();
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //Non-interactive push failed
        }
});
```


##### Stopping Non-interactive Broadcasting

```
ILiveRoomManager.getInstance().stopPushStream(streamChannelIDs, new ILiveCallBack() {
        @Override
        public void onSuccess(Object data) {
            //Non-interactive push stopped successfully
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //Failed to stop non-interactive push
        }
});
```

Parameter | Parameter Type | Description
:--:|:--:|:--:
ids | List<Long> | Array of IDs of channels that need to stop push

For more information on how to implement non-interactive broadcasting on Android, please see [New FreeShow](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos)

#### iOS
##### Starting Non-interactive Broadcasting
###### 1. Configure Push Parameters
```
ILivePushOption *option = [[ILivePushOption alloc] init];
ChannelInfo *info = [[ChannelInfo alloc] init];
info.channelName = @"New FreeShow push";
info.channelDesc = @"New FreeShow push description test text";
option.channelInfo = info;
option.encodeType = encodeType;
option.sdkType = sdkType;
```
* Push parameter: ILivePushOption

Field Name | Field Type | Default Value | Description
:--:|:--:|:--:|:--:
channelInfo | ChannelInfo | Required | Channel information of non-interactive broadcasting
record | BOOL | NO | Whether to enable recording at the same time
waterMark | BOOL | NO | Whether to enable watermark
waterMarkId | uint32_t | Optional | Watermark ID
sdkType | AVSDKType | Optional | SDK business type
rateType | AVRateType | Original bitrate | Supported bitrate
encodeType | AVEncodeType | Required | Encoding type


* Channel parameter: ChannelInfo

Field Name | Field Type | Default Value | Description
:--:|:--:|:--:|:--:
channelName | NSString | Required | Name of LVB channel
channelDesc | NSString | Optional | Description of LVB channel
channelPassword | NSString | Optional | Password configured for the receiver's player

###### 2. Start Non-interactive Push

```
[[ILiveRoomManager getInstance] startPushStream:option succ:^(id selfPtr) {
        AVStreamerResp *resp = (AVStreamerResp *)selfPtr;
        NSLog(@"Channel's ID=%d, AVLiveUrl list=%@",resp.channelID,resp.urls);
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"Push failed");
    }];
```

* Callback result: AVStreamerResp

Field Name | Field Type | Description
:--:|:--:|:--:
channelID | UInt64 | ID of created channel
urls | NSArray | AVLiveUrl list
recordTaskId | uint32_t | Recording task ID


* URL parameter: AVLiveUrl

Field Name | Field Type | Description
:--:|:--:|:--:
type | AVEncodeType | Encoding type
playUrl | NSString | Playback URL
rateType | AVRateType | Bitrate


##### Stopping Non-interactive Broadcasting

```
[[ILiveRoomManager getInstance] stopPushStreams:@[@(_channelId)] succ:^{
        NSLog(@"Push stopped");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"Failed to stop push");
    }];
```
Parameter | Parameter Type | Description
:--:|:--:|:--:
channelIds | NSArray | Array of IDs of channels that need to stop push

For more information on how to implement non-interactive broadcasting on iOS, please see [New FreeShow](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos)


### 2. Solutions for Watching Videos

#### 2.1 Tencent Cloud Web Player

Tencent Cloud Web Player is developed by Tencent Video Cloud, and supports both RTMP and HLS. The demo URL is <http://live.qcloud.com/dy/test.html>. Enter the playback URL generated after push starts into the text box to watch the video. For more information, please see [Official Documentation](http://video.qcloud.com/download/docs/QLIVE_Player_Web_SDK_Developer_Guide.pdf). Example of simple code is as follows:

```javascript
<div id="id_video_container" style="width:100%;height:1px;"></div>
<script src="http://qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>
<script>
	(function(){
		var player = new qcVideo.Player(
			"element_id",//Place the element ID of playback position in the page
			{
				"width": 640, //Height of player (in pixel) (Required)
				"height": 480, //Width of player (in pixel) (Required)
				"live_url": "rtmp://http://xxx.liveplay.qcloud.com/live/xxx",//LVB URL. HLS, RTMP and FLV are supported (Required)
				"live_url2": "http://http://xxx.liveplay.qcloud.com/live/xxx.m3u8"//LVB URL (Ditto) (Optional)
			}
		);
	})();
</script>
```

#### 2.2 Tencent Video Cloud TcPlayer

TcPlayer is developed by Tencent Video Cloud, and supports RTMP, FLV, and HLS. The demo URL is http://imgcache.qq.com/open/qcloud/video/vcplayer/demo/tcplayer.html. For more information, please see [Official Documentation](https://cloud.tencent.com/document/product/267/7479).

```javascript
<div id="id_test_video" style="width:100%; height:auto;"></div>
<script src="//restcplayer.qcloud.com/sdk/tcplayer-web-1.0.1.js" charset="utf-8"></script>
<script>
    (function(){
        var player = new TcPlayer('id_test_video', {
            "rtmp": "rtmp://http://xxx.liveplay.qcloud.com/live/xxx", //Replace the address with a functional playback address.
            "flv": "http://http://xxx.liveplay.qcloud.com/live/xxx.flv", //Replace the address with a functional playback address.
            "m3u8": "http://http://xxx.liveplay.qcloud.com/live/xxx.m3u8", //Replace the address with a functional playback address.
            "live": true,
            "coverpic" : "http://www.test.com/myimage.jpg",
            "width" :  '480',//Video display width. Use the video definition width if possible.
            "height" : '320'//Video display height. Use the video definition height if possible.
        });
    })();
</script> 

```

If the advertisement feature needs to be used, introduce Google IMA SDK on the page. 
```javascript
<script type="text/javascript" src="//imasdk.googleapis.com/js/sdkloader/ima3.js"></script>

```

You can use the advertisement feature using adTagUrl and auth parameters. Visit https://tcplayer.qcloud.com to apply for an account and license information, or send an email to tcplayer@tencent.com for consultation.
```javascript
var player = new TcPlayer('id_test_video', {
  /* Advertisement-related parameter */
  "adTagUrl": "http://ad_tag_url",	//Tags of VAST, VMAP and VAPID video ads
  "auth": {
    "user_id": "your_user_id",		//Ad account ID 
    "app_id": "your_app_id",		//Application ID 
    "license": "your_license"		//Application license
  }
});

```




#### 2.3 Client SDK Player (ffmpeg)

ffmpeg is an open-source audio/video processing tool used to provide cross-platform solutions. The latest version of ffmpeg comes with rtmp. You can download ffmpeg at <http://www.ffmpeg.org> Note: ffmpeg uses LGPL or GPL license depending on the component you selected. If any is used, follow the license rules. For more information on codes, please see ffplay.c. If the codes need to be compiled, install the SDL. The development steps are briefed as follows:

```c++
//Initialize
av_register_all();
avformat_network_init();

//Open and enter
AVFormatContext *ifmt_ctx = avformat_alloc_context();
avformat_open_input(&ifmt_ctx, in_filename, 0, 0));

//Locate video and audio streams
int videoindex = -1, audioindex = -1, i;
for (i = 0; i<ifmt_ctx->nb_streams; i++) {
	if (ifmt_ctx->streams[i]->codec->codec_type == AVMEDIA_TYPE_VIDEO){
		videoindex = i;
	}
	if (ifmt_ctx->streams[i]->codec->codec_type == AVMEDIA_TYPE_AUDIO){
		audioindex = i;
	}
}

//Initialize audio/video encoder/decoder
AVCodecContext *pVideoCodecCtx = ifmt_ctx->streams[videoindex]->codec;
AVCodec *pVideoCodec = avcodec_find_decoder(pVideoCodecCtx->codec_id);
AVCodecContext *pAudioCodecCtx = ifmt_ctx->streams[audioindex]->codec;
AVCodec *pAudioCodec = avcodec_find_decoder(pAudioCodecCtx->codec_id);

Read and decode data
int got_picture, got_frame;
AVPacket *pkt = av_packet_alloc();
AVFrame * pVideoFrame = av_frame_alloc();
AVFrame * pAudioFrame = av_frame_alloc();

av_read_frame(ifmt_ctx, pkt);
avcodec_decode_video2(pVideoCodecCtx, pVideoFrame, &got_picture, pkt); 
avcodec_decode_audio4(pAudioCodecCtx, pAudioFrame, &got_frame, pkt);
```

Now, you have obtained the original audio/video data. Choose a solution to play and render it. For example, use SDL2 to call SDL_CreateWindow, SDL_CreateRenderer, SDL_CreateTexture in sequence, and then copy the data to display:

```c++
SDL_Texture *txt;
//Omit SDL_CreateTexture initialization txt

//Note: Check whether pVideoFrame->pCodecCtx->pix_fmt is AV_PIX_FMT_YUV420P before calling
//If not, you can use sws_scale to transcode
SDL_UpdateYUVTexture(txt, NULL,
	pVideoFrame ->data[0], pVideoFrame ->linesize[0],
	pVideoFrame ->data[1], pVideoFrame ->linesize[1],
	pVideoFrame ->data[2], pVideoFrame ->linesize[2]);
```

Or, for example, use opencv which only supports RBG data format, so you need to transcode first and then display the data

```c++
//Transcode
AVFrame * pFrameRBG = av_frame_alloc();
int size = av_image_get_buffer_size(AV_PIX_FMT_BGR24, 
	pVideoCodecCtx->width, pVideoCodecCtx->height, 1);
uint8_t *out_bufferRGB = new uint8_t[size];
av_image_fill_arrays(pFrameRBG->data, pFrameRBG->linesize, 
	out_bufferRGB, AV_PIX_FMT_BGR24, 
	pVideoCodecCtx->width, pVideoCodecCtx->height, 8);
struct SwsContext *img_convert_ctx = sws_getContext(
	pVideoCodecCtx->width, pVideoCodecCtx->height, 
	pVideoCodecCtx->pix_fmt,
	pVideoCodecCtx->width, pVideoCodecCtx->height, AV_PIX_FMT_BGR24, 
	SWS_BICUBIC, NULL, NULL, NULL);
sws_scale(img_convert_ctx,
 	 (const uint8_t* const*)pVideoFrame->data, pVideoFrame->linesize, 
	0, pVideoCodecCtx->height,
	pFrameRBG->data, pFrameRBG->linesize);

//Copy data
Mat frame;
if (frame.empty()){
	frame.create(cv::Size(pVideoCodecCtx->width, 
		pVideoCodecCtx->height), CV_8UC3);
}
memcpy(frame.data, out_bufferRGB, size);

//Display
imshow("title", frame);
```

You can play audio using DirectShow, which is not discussed here. Note: The above is an example of simplified calling steps. In practice, you need to develop independently, and pay attention to more details, for example, using jitterbuf for anti-shake, audio/video synchronization, etc.

### 3. FAQs
#### 3.1 Can I combine (or mix) multiple streams in one audio/video room?

Non-interactive push of a QAVSDK instance only supports the push of one audio channel and one video channel (video is required). Even though an ILVB room can bypass 4 unparallel video streams, they are independent from each other, and cannot be overlaid or mixed.

#### 3.2 What is the impact of running App at the backend to non-interactive push?
+ For **`Windows`**, running App at the backend is the same with running at the frontend.
+ For **`iOS`**, running App at the backend may be suspended by the system and cause interruption of push. For more information, please see relevant technical documents of Apple.
+ For **`Android`**, if App is running at the backend, the system cannot kill the process automatically in theory. However, the behaviors of various highly-customized Android systems are different, depending on the specific conditions. In addition, Android system's protection mechanism can end the process automatically in some cases (such as insufficient resource).


#### 3.3 What is the impact of interrupted uplink network to non-interactive push during LVB? How to resume push?

When the uplink network is interrupted:

+ If users who watch LVB through RTMP join the room after 7 seconds upon network interruption, they are prompted that LVB has ended.
+ For users who watch LVB through HLS, the LVB is interrupted after the playback of the fragment cached at the backend is completed.

When the uplink network of video is disconnected after timeout, the channel is retained for an hour at the push backend, during which the **_playback URL returned after the push is restarted remains unchanged_**. If the push has not been restarted within an hour, the channel is reclaimed, that is, the playback URL returned after the push is restarted can be **_re-generated_**.


#### 3.4 Is the number of LVB channels related to App or Tencent Cloud account?

The maximum number of LVB channels is bound to Tencent Cloud account. Channel resources are shared among multiple Apps under an account. For example, if the number of channels for an account is limited to 50, App A under the account uses 30, and the rest Apps can only use 20 channels.



### 4. Error Codes


| Error Code | Description | Solution |
|---------|---------|---------|
| 1001	| Permission error	| It is generally caused by wrong input of sdkappid |
| 1002	| Account does not exist	| Check whether the user data entered in API parameters is correct |
| 6012	| Push timeout	| Check the uplink network condition. The retry mechanism should also be introduced on the App level as needed. It is recommended to retry every 30 seconds. If the problem remains unsolved, contact us for troubleshooting |
| 20101	| The number of channels exceeds the limit 	| The number of push channels is limited. Check and delete unnecessary channels in the push console, or expand the capacity based on actual needs |
| 20318	| LVB identity verification has not been completed	| Please activate Tencent Cloud LVB service first |
| 20406	| Account overdraft	| Check whether the account is in arrears |
| 50002	| Incorrect input parameters | Check whether user ID and sdkappid are entered correctly |
| 50003	| Pull URL is not fetched at the backend	| Report to Tencent customer service |
| 50004	| Push type of push request is incorrect	| Check whether the push type field is entered correctly |
| 50005	| Backend console connection timeout	| It is probably due to network failure. Try again. Send feedback to Tencent Cloud customer service if retry failed |
| 50006	| Backend console connection timeout	| It is probably due to network failure. Try again. Send feedback to Tencent Cloud customer service if retry failed |
| 50007	| The parameter returned from the backend is null	| Report to Tencent Cloud customer service |
| 40000000	| Failed to resolve SDK request	| Check whether the push request fields are complete |
| 40000001	| Failed to resolve SDK request - The push request packet is missing	| Check whether the push request fields are complete |
| 40000002	| Failed to resolve SDK request - The operation field of push request is missing	| Check whether the push request fields are complete |
| 40000003	| Failed to resolve SDK request - The output coding (HLS/RTMP, etc.) of push request is missing	| Check whether the push request fields are complete |
| 40000004	| Failed to resolve SDK request - The video source type is incorrect (camera/desktop, etc.)	| Check whether the push request fields are complete |
| 40000005	| Failed to resolve SDK request - Incorrect request operation (request for push, stop push)	| Check whether the push request fields are complete |
| 40000006	| User ID is incorrect when you send request for push	| Check whether the push request fields are correct |
| 40000007	| Push room ID is 0	| Check whether the push room ID is correct |
| 40000201 | An error occurred while requesting server for internal data packing | Report to Tencent customer service |
| 40000202 | An error occurred while requesting server for internal data packing | Report to Tencent customer service |
| 40000203 | An error occurred while requesting server for internal data packing | Report to Tencent customer service |
| 40000207 | A communication error occurred while requesting pushing server - Failed to fetch the address of pushing server | This may be caused by network problem. Try again. If the problem persists, report to Tencent customer service |
| 40000208 | A communication error occurred while requesting pushing server - Timeout of request for pushing server | This may be caused by network problem. Try again. If the problem persists, report to Tencent customer service |
| 40000301 | An error occurred while resolving the response packet from push server - Failed to resolve the data packet | Report to Tencent customer service |
| 40000302 | An error occurred while resolving the response packet from push server - Failed to resolve the data packet | Report to Tencent customer service |
| 40000303 | An error occurred while resolving the response packet from push server - No IP is returned | Report to Tencent Cloud customer service |
| 40000304 | An error occurred while resolving the response packet from push server - No port is returned | Report to Tencent customer service |
| 40000305 | An error occurred while resolving the response packet from push server - No result is returned | Report to Tencent Cloud customer service |
| 40000306	| An error occurred while resolving the response packet from push server - Overflow of length of returned URL	| Report to Tencent Cloud customer service |
| 40000401 |An error occurred while obtaining the grocery service IP by querying room | This may be caused by network problem. Try again. If the problem persists, report to Tencent customer service |
| 40000402 | An error occurred while fetching grocery data by querying room | This may be caused by network problem. Try again. If the problem persists, report to Tencent customer service |
| 40000403 | grocery does not exist and cannot be fetched by querying room (the room requesting push does not exist) | Check whether the room has been activated successfully, and whether the user ID and groupid are correctly entered |
| 40000404 | Timeout while querying room stream-control server | This may be caused by network problem. Try again. If the problem persists, report to Tencent customer service |
| 40000405 |An error occurred with the response packet while querying room - Failed to resolve the data packet | Report to Tencent customer service |
| 40000406 |An error occurred with the response packet while querying room - Failed to resolve the data packet | Report to Tencent customer service |
| 40000407 |An error occurred with the response packet while querying room - Failed to resolve the data packet | Report to Tencent customer service |
| 40000408 | An error occurred with the response packet while querying room - No result is returned | Report to Tencent customer service |
| 40000409 |An error occurred with the response packet while querying room - Failed to resolve the data packet | Report to Tencent customer service |
| 40000410	| The room requesting the push does not exist	| Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly, or whether the user has quitted the room |
| 40000411	| The user who initiates the push does not exist in the room	| Check whether the room has been activated successfully, and whether the user ID and groupid for the push are entered correctly, or whether the user has quitted the room |
| 40000412	| Request for ending push has been sent more than once and the user has ended push	| This indicates that push has ended. No action is needed for this. |
| 40000413	| Request for ending push has been sent more than once and the user has ended push	| This indicates that push has ended. No action is needed for this. |
| 40000414	| An error occurred with internal server operation type while querying room | This may be caused by network problem. Try again. If the problem persists, report to Tencent customer service |
| 40000415	| Request for starting push has been sent more than once and the user is pushing stream	| This indicates that push is already in progress. No action is needed for this |
| 40000500	| Control the frequency of starting push	| Unexceptional. Error is returned if a user sends a push request repeatedly within 3 seconds. The request should be retried after 3 seconds upon initiation of the last request |






