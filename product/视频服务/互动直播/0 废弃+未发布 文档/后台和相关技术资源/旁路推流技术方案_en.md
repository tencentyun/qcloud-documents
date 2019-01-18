By connecting Tencent Cloud storage VOD and LVB services, Tencent Cloud ILVB service provides a full set of strong capabilities, such as audio/video interaction, non-interactive broadcasting and recording & replay, covering many scenarios including online education, live show/game ILVB, real-time audio/video chat, etc. Its architecture and data flow are shown in the figure below. It is classified into **`audio/video backend service`**, **`non-interactive push service`** and **`recording and storage service`** (with different colors) by feature. Note:

+ **`Audio/video backend service`** is mainly responsible for the forwarding of audio/video data, management of users/rooms and control of network quality. For more information about DC/OC access module in the figure, please see "Data Center (DC) and Outer Center (OC) of ILVB".
+ **`Non-interactive push service`** is mainly responsible for transcoding the uplink QAVSDK audio/video data for pushing and distributing, so that users can watch files through [Web or streaming media player](http://cloud.tencent.com/product/LVB.html). It is used primarily for LVB sharing (send palyback URL to users to play through Web), monitoring (whether VJ behaves exceptionally) and online education.
+ **`Recording and storage service`** is responsible for recording the uplink audio/video data collected by QAVSDK as MP4 file, and storing it into Tencent Cloud storage for users to [replay using VOD service](http://cloud.tencent.com/product/vod.html).

![Overall architecture](//mccdn.qcloud.com/img56cdcee729316.png)

## 1. About Non-interactive Push

Since ILVB uses Tencent Cloud LVB service, you need to apply for activation of Tencent Cloud LVB service before using non-interactive push feature. Upon approval, you can directly perform operations such as management of LVB channels, statistical analysis and configuration in the [Console](http://console.cloud.tencent.com/live). In addition to manual operations, you can also directly manage the LVB at business backend using the capacity provided by [LVB API](http://cloud.tencent.com/wiki/直播API).

### 1.1 Overview of Non-interactive Push

1.1.1 App that is responsible for uplink audio/video data calls QAVSDK API (`RequestMultiVideoStreamStart`) to start push, and obtain the playback URL.
1.1.2 App sends the playback URL obtained in the previous step to all users who watch non-interactive broadcasting (RTMP/HLS). Hotlink protection feature can be enabled for "optional" businesses, to generate a dedicated playback link using uplink URL and viewer's information, thus preventing resources from being stolen.
1.1.3 You can watch non-interactive broadcasting through H5 page, Web plug-in, streaming media player.
1.1.4 App that is responsible for uplink audio/video data calls QAVSDK API (`equestMultiVideoStreamStop`) to stop push. Please note that this step is very important. If this API is not called, the exception handling logic is enabled at the backend when the same user restarts the push. This logic is mainly used to handle the push restart at the client end after the LVB is interrupted because network or client crashes. If this logic is enabled in normal process, problems may occur (for more information, please see "Development Guide for ILVB Non-interactive Broadcasting").

### 1.2 Non-interactive Push API and Usage

For more information, please see [Non-interactive broadcasting Development Guide](/doc/product/268/3219)

### 1.3 Overview of Development of Non-interactive Push Player

#### 1.3.1 Tencent Cloud Web Player

Tencent Cloud Web Player is developed by Tencent Video Cloud, and supports both RTMP and HLS. Demo address is <http://live.qcloud.com/dy/test.html>. Enter the playback URL generated after push starts into the text box to watch the video. For more information, please see [official documentation](http://video.qcloud.com/download/docs/QLIVE_Player_Web_SDK_Developer_Guide.pdf) Example of simple code is as follows:

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

#### 1.3.2 Open-source Web Player (jwplayer)

JW Media Player is an open-source web media player. Demo address is <http://live.qcloud.com/dy/jwplayer.html>. Example of simple code is as follows:

```javascript
<div id="id_video_container" style="width:100%;height:1px;"></div>
<script src="http://qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>
<script>
	(function(){
		var player = new qcVideo.Player(
			" id_video_container ",//Place the element ID of playback position in the page
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

#### 1.3.3 Client SDK Player (ffmpeg)

ffmpeg is an open-source audio/video processing tool used to provide cross-platform solutions. The latest version of ffmpeg comes with rtmp. The download address of ffmpeg is <http://www.ffmpeg.org> (note: ffmpeg uses LGPL or GPL license depending on the component you selected. If any one is used, please abide by the rules of the license). Its simple development steps are as follows:

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

Now, we get the original audio/video data. Play, render, and use a dependency solution. For example, use SDL2, then call SDL_CreateWindow, SDL_CreateRenderer, SDL_CreateTexture in sequence, and copy data to display:

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

### 1.4 Non-interactive Push Q&A

#### 1.4.1 How to watch LVB that uses non-interactive push?

Tencent Cloud CDN supports two streaming media protocols: RTMP (Real Time Messaging Protocol) and HLS (HTTP Live Streaming). However, currently, an LVB stream only supports one output protocol. 2016H1 that supports two push streams is coming soon.

RTMP protocol, a streaming media transmission protocol led by Adobe company, is featured with a low delay (which can be reduced to around 3 seconds) and high compatibility with PC (thanks to the high penetration of Flash plug-in in PC, RTMP stream can be directly played in PC browsers). However, due to problems such as vulnerabilities of FLASH and high battery consumption, the penetration of Flash plug-in is extremely low in mobile devices (it is even not supported in iOS system). So on mobile devices, you need to play RTMP stream using dedicated players. For routine test, you can use **`ffplay`** (a component in ffmpeg) or **`vlc`** to check whether the push is successful:

* Play stream with **`ffplay`**: ffplay -fflags nobuffer -i "rtmp playback address", in which nobuffer is used to restrict player from performing buffering for the better observation of latency
* Play stream with **`vlc`**: (Menu) **Media** -> **Open network stream** -> **Enter RTMP playback URL** -> **Play**

HLS, a streaming media protocol led by Adobe company, is featured with simpleness, high versatility and bitrate adaption. It is supported by iOS system and most Android systems. You can watch videos directly through H5 page. However, to ensure fluency, at least 3 fragments (with each lasting about 5 seconds) should be cached before playback. So the latency for the playback of HLS is generally more than 10 seconds.

#### 1.4.2 Can I combine multiple streams of one audio/video room (including mixing)?

Currently, non-interactive push of a QAVSDK instance only supports the push of one audio channel and one video channel (video is required). Even though an ILVB room can bypass 4 unparallel video streams, they are independent from each other, and cannot be overlaid or mixed. For 2016H1 which is coming soon, the non-interactive push of ILVB supports the mixing (i.e. merge videos, and mix audio in the video at the backend) of audio/video data of the same audio/video room and then outputting these data to CDN for distribution.

#### 1.4.3 Common Error Codes, Descriptions and Handling Methods of Non-interactive Push

+ **`40000415`** The user is already in push process (if LVB has already started, this error code is returned if the same user initiates push repeatedly). If push is normal at viewer end, this exception can be ignored by uplink player.
+ **`20101`** The number of channels exceed the limit. Contact us to expand capacity based on your actual needs.
+ **`20318`** LVB identity verification has not been completed. Activate Tencent Cloud LVB service first.
+ **`20406`** LVB account overdraft. Purchase package in LVB console or top up.
+ **`1002`** Account does not exist. Check whether the user data entered in API parameters is correct.
+ **`6012`** Push timeout. Check the uplink network condition. The retry mechanism should also be introduced on the App level as needed. It is recommended to retry every 30 seconds. If the problem remains unsolved, contact us for troubleshooting.

#### 1.4.4 What is the impact of running App at the backend to non-interactive push?

+ For **`Windows`**, running App at the backend is the same with running at the frontend.
+ For **`iOS`**, running App at the backend may be suspended by the system and cause interruption of push. For more information, please see relevant technical documents of Apple.
+ For **`Android`**, if App is running at the backend, in theory, the system can not kill the process automatically. However, the behaviors of various highly-customized Android systems are different, depending on the specific conditions. In addition, Android system's protection mechanism can end the process automatically in some cases (such as insufficient resource).

#### 1.4.5 What is the impact to non-interactive push if I receive system call during LVB? How to resume from interruption?

+ **The impact of system call to the network connection of network terminal**

	The impact of system call to terminal network is closely linked to the ISP networking type and the audio solution in mobile devices. Currently, 3G network of China Mobile is automatically changed to 2G when the call is connected. So the system call makes the original 4G network disconnected, leading to network interruption. Since 4G network of China Unicom is automatically changed to WCDMA when the call is connected, the network is not interrupted during voice call, nor the call is connected on 4G. It is more complicated for China Telecom. For more information, please see relevant technical documentation.
	
+ **How to resume from interruption of QAVSDK system call**

	Considering the user privacy (the voice of JV calling is not captured) and the stability, QAVSDK calls are interrupted. However, the automatically resuming from interruption is not supported for 1.7 or any other old versions. Users can resume from the interruption of system calls by exiting (perceive interruption) and rejoining (perceive resuming) the room. The feature of automatically resuming from the interruption of system calls is integrated in 1.8 version of QAVSDK (coming soon). Notifications are sent only when the call is interrupted and resumed, to further simplify the processing procedure.

#### 1.4.6 What is the impact of interrupted uplink network to non-interactive push during LVB? How to resume push?

If the network of uplink video player (QAVSDK) is interrupted:

+ For a user who watch videos using QAVSDK, if the audio/video stream is interrupted, a notification of cancellation of video status is sent to the user after 15 seconds, and another notification of exiting the room due to timeout is sent after 90 seconds.
+ If users who watch LVB through RTMP join the room after 7 seconds upon network interruption, they are prompted that LVB has ended.
+ For users who watch LVB through HLS, the LVB is interrupted after the playback of the fragment cached at the backend is completed.

When the uplink network of video is disconnected after timeout, the channel is retained for an hour at the push backend, during which the **_playback URL returned after the push is restarted remains unchanged_**. If the push has not been restarted within an hour, the channel is reclaimed, that is, the palyback URL returned after the push is restarted can be **_re-generated_**.

#### 1.4.7 How to handle the cross-domain issues occurred when you play the HLS stream pushed by non-interactive broadcasting using Flash player?
Because of the native support for Flash, no cross-domain issues occur when you play FLV/MP4/RTMP videos. However, since native HLS is not supported for Flash, the player code is required for the conversion of container and the permission of reading request data is also needed, so the cross-domain permission is restricted. Two solutions are provided currently:

+ Use our player;
+ Place the third-party playback SWF file on our CDN, and use the URL we provided to bypass the restriction. If the third-party player file is required, you can provide the code, and then we put a new code version on CDN.

#### 1.4.8 Is the number of LVB channels related to App or Tencent Cloud account?

The maximum number of LVB channels are bound to Tencent Cloud account. Channel resources are shared among multiple Apps under an account. For example, if the number of channels for an account is limited to 50, App A under the account uses 30, and the rest Apps can only use 20 channels.

## 2 Recording and VOD Q&A

### 2.1 How to partition the audio/video data file recorded at the backend?

To avoid generation of large audio/video file due to long recording length, the file is partitioned every 90 minutes at the backend, and each fragment is saved as a MP4 file with the format of **`file name_start time_end time`**. The **`file name`** is the parameter specified by the API for starting recording. When you play files using VOD service, the list of files in the whole recording process is pulled at business end by calling the API `v2/DescribeVodPlayInfo`** for obtaining video playback information.

### 2.2 Is voice-only recording supported?

Currently, voice-only recording is not supported for non-interactive push of ILVB. The recorded media stream must contain video data. The adjustment of backend logic and introduction of new QAVSDK API are required for voice-only recording, which is under development stage.
