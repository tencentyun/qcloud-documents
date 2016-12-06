## 旁路直播
旁路直播功能可以把互动直播上行的数据转码成通用格式进行推流分发，以方便用户通过Web或流媒体播放器观看。<br/><br/>
**使用旁路直播功能前，请先在控制台开通腾讯云直播服务，否则将无法使用**。

### 1 客户端SDK接口
#### Android
##### 开始旁路直播
######1. 设置推流参数
```
ILivePushOption option = new ILivePushOption();
option.channelName("新随心播推流");
option.encode(TIMAvManager.StreamEncode.RTMP);
```

* 推流参数：ILivePushOption

字段名|字段类型|默认值|说明
:--:|:--:|:--:|:--:
channelName|String|可选|设置频道名称
channelDesc|String|可选|设置频道描述
channelPassword|String|可选|设置频道播放密码
record|boolean|NO|是否同时开启录制
waterMark|boolean|NO|是否开启水印
waterMarkId|long|可选|水印id
sdkType|TIMAvManager.SDKType|可选|设置当前sdk类型
rateType|TIMAvManager.RateType|原始码率|支持的码率
encode|TIMAvManager.StreamEncode|RTMP|设置推流编码类型

######2. 开始旁路推流

```
ILiveRoomManager.getInstance().startPushStream(option, new ILiveCallBack<TIMAvManager.StreamRes>() {
        @Override
        public void onSuccess(TIMAvManager.StreamRes data) {
            //旁路推流成功
            List<TIMAvManager.LiveUrl> liveUrls = data.getUrls();
            streamChannelID = data.getChnlId();
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //旁路推流失败
        }
});
```


##### 结束旁路直播

```
ILiveRoomManager.getInstance().stopPushStream(streamChannelIDs, new ILiveCallBack() {
        @Override
        public void onSuccess(Object data) {
            //停止旁路推流成功
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //停止旁路推流失败
        }
});
```

参数名|参数类型|说明
:--:|:--:|:--:
ids|List<Long>|要停止推流的频道ID数组

Android旁路直播功能的详细实现见[新随心播](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos)

#### ios
##### 开始旁路直播
######1. 设置推流参数
```
ILivePushOption *option = [[ILivePushOption alloc] init];
ChannelInfo *info = [[ChannelInfo alloc] init];
info.channelName = @"新随心播推流";
info.channelDesc = @"新随心播推流描述测试文本";
option.channelInfo = info;
option.encodeType = encodeType;
option.sdkType = sdkType;
```
* 推流参数：ILivePushOption

字段名|字段类型|默认值|说明
:--:|:--:|:--:|:--:
channelInfo|ChannelInfo|必填|旁路直播频道信息
record|BOOL|NO|是否同时开启录制
waterMark|BOOL|NO|是否开启水印
waterMarkId|uint32_t|可选|水印id
sdkType|AVSDKType|可选|SDK业务类型
rateType|AVRateType|原始码率|支持的码率
encodeType|AVEncodeType|必填|编码格式


* 频道参数：ChannelInfo

字段名|字段类型|默认值|说明
:--:|:--:|:--:|:--:
channelName|NSString|必填|直播频道的名称
channelDesc|NSString|可选|直播频道的描述
channelPassword|NSString|可选|为接收方播放器设置的密码

######2. 开始旁路推流

```
[[ILiveRoomManager getInstance] startPushStream:option succ:^(id selfPtr) {
        AVStreamerResp *resp = (AVStreamerResp *)selfPtr;
        NSLog(@"频道的ID=%d,AVLiveUrl列表=%@",resp.channelID,resp.urls);
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"推流失败");
    }];
```

* 回调结果：AVStreamerResp

字段名|字段类型|说明
:--:|:--:|:--:
channelID|UInt64|创建频道的ID
urls|NSArray|AVLiveUrl列表
recordTaskId|uint32_t|录制任务id


* URL参数：AVLiveUrl

字段名|字段类型|说明
:--:|:--:|:--:
type|AVEncodeType|编码格式
playUrl|NSString|播放url
rateType|AVRateType|码率


##### 结束旁路直播

```
[[ILiveRoomManager getInstance] stopPushStreams:@[@(_channelId)] succ:^{
        NSLog(@"已停止推流");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"停止推流失败");
    }];
```
参数名|参数类型|说明
:--:|:--:|:--:
channelIds|NSArray|要停止推流的频道ID数组

IOS旁路直播功能的详细实现见[新随心播](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos)


### 2 观看方案

#### 2.1 腾讯云Web播放器

视频云Web播放器是由腾讯视频云自主开发的一款播放器，同时支持RTMP和HLS。演示地址为<http://live.qcloud.com/dy/test.html>，将启动推流后得到的观看地址输入文本框即可播放。更多详情请参阅[官方文档](http://video.qcloud.com/download/docs/QLIVE_Player_Web_SDK_Developer_Guide.pdf)。简单代码示例如下所示：

```javascript
<div id="id_video_container" style="width:100%;height:1px;"></div>
<script src="http://qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>
<script>
	(function(){
		var player = new qcVideo.Player(
			"element_id",//页面放置播放位置的元素 ID
			{
				"width": 640, //播放器宽度，单位像素(必选参数)
				"height": 480, //播放器高度，单位像素(必选参数)
				"live_url": "rtmp://http://xxx.liveplay.qcloud.com/live/xxx",//直播地址，支持 hls 和 rtmp 、flv 三种格式(必选参数)
				"live_url2": "http://http://xxx.liveplay.qcloud.com/live/xxx.m3u8"//直播地址，同上，（可选参数）
			}
		);
	})();
</script>
```

#### 2.2 开源Web播放器jwplayer

JW Media Player是一个开源的网页媒体播放器。演示地址为<http://live.qcloud.com/dy/jwplayer.html>，示例代码如下所示：

```javascript
<div id="id_video_container" style="width:100%;height:1px;"></div>
<script src="http://qzonestyle.gtimg.cn/open/qcloud/video/live/h5/live_connect.js" charset="utf-8"></script>
<script>
	(function(){
		var player = new qcVideo.Player(
			" id_video_container ",//页面放置播放位置的元素 ID
			{
				"width": 640, //播放器宽度，单位像素(必选参数)
				"height": 480, //播放器高度，单位像素(必选参数)
				"live_url": "rtmp://http://xxx.liveplay.qcloud.com/live/xxx",//直播地址，支持 hls 和 rtmp 、flv 三种格式(必选参数)
				"live_url2": "http://http://xxx.liveplay.qcloud.com/live/xxx.m3u8"//直播地址，同上，（可选参数）
			}
		);
	})();
</script>
```

#### 2.3 客户端SDK播放器(ffmpeg)

ffmpeg是提供跨平台解决方案的开源音视频处理工具，最新ffmpeg已自带rtmp。ffmpeg下载地址为<http://www.ffmpeg.org>（注：ffmpeg采用LGPL或GPL许可证(依据你选择的组件)，如使用，请遵循许可证的规则）代码可以参考ffplay.c(如需编译ffplay，需安装SDL)，其简单开发步骤如下所示：

```c++
//初始化
av_register_all();
avformat_network_init();

//打开输入
AVFormatContext *ifmt_ctx = avformat_alloc_context();
avformat_open_input(&ifmt_ctx, in_filename, 0, 0));

//找到视频流和音频流
int videoindex = -1, audioindex = -1, i;
for (i = 0; i<ifmt_ctx->nb_streams; i++) {
	if (ifmt_ctx->streams[i]->codec->codec_type == AVMEDIA_TYPE_VIDEO){
		videoindex = i;
	}
	if (ifmt_ctx->streams[i]->codec->codec_type == AVMEDIA_TYPE_AUDIO){
		audioindex = i;
	}
}

//初始化音视频编解码器
AVCodecContext *pVideoCodecCtx = ifmt_ctx->streams[videoindex]->codec;
AVCodec *pVideoCodec = avcodec_find_decoder(pVideoCodecCtx->codec_id);
AVCodecContext *pAudioCodecCtx = ifmt_ctx->streams[audioindex]->codec;
AVCodec *pAudioCodec = avcodec_find_decoder(pAudioCodecCtx->codec_id);

开始读取数据并解码
int got_picture, got_frame;
AVPacket *pkt = av_packet_alloc();
AVFrame * pVideoFrame = av_frame_alloc();
AVFrame * pAudioFrame = av_frame_alloc();

av_read_frame(ifmt_ctx, pkt);
avcodec_decode_video2(pVideoCodecCtx, pVideoFrame, &got_picture, pkt); 
avcodec_decode_audio4(pAudioCodecCtx, pAudioFrame, &got_frame, pkt);
```

至此，音视频原始数据已经获取到，播放和渲染，依赖使用哪种方案。例如，使用SDL2，依次调用SDL_CreateWindow、SDL_CreateRenderer、SDL_CreateTexture然后拷贝数据并显示：

```c++
SDL_Texture *txt;
//省略SDL_CreateTexture初始化txt

//注：调用前先确认pVideoFrame->pCodecCtx->pix_fmt为AV_PIX_FMT_YUV420P
//如不是，可先用sws_scale转格式
SDL_UpdateYUVTexture(txt, NULL,
	pVideoFrame ->data[0], pVideoFrame ->linesize[0],
	pVideoFrame ->data[1], pVideoFrame ->linesize[1],
	pVideoFrame ->data[2], pVideoFrame ->linesize[2]);
```

或者例如使用opencv，opencv只接受RBG数据格式，因此需先转格式，再显示

```c++
//转码
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

//拷贝数据
Mat frame;
if (frame.empty()){
	frame.create(cv::Size(pVideoCodecCtx->width, 
		pVideoCodecCtx->height), CV_8UC3);
}
memcpy(frame.data, out_bufferRGB, size);

//显示
imshow("title", frame);
```

声音播放方式可以用DirectShow，这里就不展开了（注：上面仅为简略调用步骤示意，实际使用需自行开发，并且还需很多细化工作，例如使用jitterbuf来防抖动，音视频同步等）

### 3.常见问题
#### 3.1 同一音视频房间的多路流是否支持合并（包括混音）？

目前，一个QAVSDK实例的旁路推流只支持推一路语音+一路视频（且必须有视频），虽然同一个互动直播房间可以旁路4路不同的音视频流，但是每个流之间各自独立，并不能叠加或混合。

#### 3.2 App退后台对旁路推流有什么影响？
+ **`Windows`**退后台，与前台无异
+ **`iOS`**退后台，可能会被系统挂起导致推流终端，具体详情请参阅Apple公司相关技术文档
+ **`Android`**退后台，理论上系统是不会自动杀进程的。但各家深度定制的安卓系统行为不尽相同，需要具体情况具体分析。此外，安卓系统自身的一些保护机制也会在某些情况下（如资源不足等）自动结束进程


#### 3.3 直播过程中上行方网络中断对旁路推流有什么影响？如何恢复推流？

如果视频上行方网络中断，则：

+ 通过RTMP观看的用户，在网络中断的7秒后进入，会提示直播已结束
+ 通过HLS观看的用户，在后台缓存分片播放完后中断。

视频上行方网络超时断开后，推流后台会将频道保留1小时，这段时间内该用户重新推流所返回的**_观看地址不会改变_**。如果1小时内该用户仍未重新推流，则频道将会回收，即该用户重新推流所获得的观看地址会**_重新生成_**。


#### 3.4 直播频道的数量限制是与应用相关还是与腾讯云账号相关？

直播频道的数量上限是与腾讯云帐号绑定的，一个帐号下多个应用是共用频道资源的。例如，一个账号频道上限50，该账号下的应用A使用了30个，则该账号下的其他应用就只有20个频道可用



### 4 错误码


| 错误码| 错误说明| 处理建议|
|---------|---------|---------|
|1001	|权限错误	|一般是sdkappid填写错误导致|
|1002	|账户不存在	|请排查接口参数填写的用户数据是否正确|
|6012	|推流超时	|请查看上行方的网络状况，App层面也根据需要引入适当的重试，重试间隔建议为30秒。如果依然有问题可以联系我们协助排查|
|20101	|通道数超过上限	|推流通道数存在上限，在推流控制台检查并删除无用的通道，或根据实际需要进行扩容|
|20318	|未开通直播资质	|请先开通腾讯云直播服务|
|20406	|用户欠费	|检查是否已欠费|
|50002	|输入参数检验错误|检查用户ID是否填写错误，sdkappid是否填写错误|
|50003	|后端没有拉取到拉流的url	|反馈腾讯客服|
|50004	|推流请求的推流类型错误	|检查推流类型字段填写是否正确|
|50005	|连接后端控制台超时	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|50006	|连接后端控制台超时	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|50007	|后端返回参数为空	|反馈腾讯客服|
|40000000	|SDK请求解析失败	|推流请求字段填写是否完整|
|40000001	|SDK请求解析失败-没有推流请求包体	|推流请求字段填写是否完整|
|40000002	|SDK请求解析失败-没有推流请求操作字段	|推流请求字段填写是否完整|
|40000003	|SDK请求解析失败-缺少推流请求的输出编码（HLS/RTMP等）	|推流请求字段填写是否完整|
|40000004	|SDK请求解析失败-视频源类型错误（摄像头/桌面等）	|推流请求字段填写是否完整|
|40000005	|SDK请求解析失败-请求操作错误（请求推流、停止推流）	|推流请求字段填写是否完整|
|40000006	|请求推流的时候检查用户ID不正确	|推流请求字段填写是否正确|
|40000007	|推流房间ID填写成0	|请检查推流的房间ID的填写|
|40000201	|请求服务器内部数据打包错误	|反馈腾讯客服|
|40000202	|请求服务器内部数据打包错误	|反馈腾讯客服|
|40000203	|请求服务器内部数据打包错误	|反馈腾讯客服|
|40000207	|请求推流服务器通讯错误-拉取推流服务器地址失败	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|40000208	|请求推流服务器通讯错误-请求推流服务器超时	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|40000301	|解析推流服务器回包错误-数据包解析失败	|反馈腾讯客服|
|40000302	|解析推流服务器回包错误-数据包解析失败	|反馈腾讯客服|
|40000303	|解析推流服务器回包错误-没有返回IP	|反馈腾讯客服|
|40000304	|解析推流服务器回包错误-没有返回端口	|反馈腾讯客服|
|40000305	|解析推流服务器回包错误-没有返回结果	|反馈腾讯客服|
|40000306	|解析推流服务器回包错误-返回url长度溢出	|反馈腾讯客服|
|40000401	|查询房间获取grocery服务IP错误	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|40000402	|查询房间拉取grocery数据错误	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|40000403	|查询房间拉取grocery不存在（请求推流的房间不存在）	|检查是否成功开房，推流的用户ID，groupid是否填写正确|
|40000404	|查询房间流控服务器超时	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|40000405	|查询房间回包错误-数据包解析失败	|反馈腾讯客服|
|40000406	|查询房间回包错误-数据包解析失败	|反馈腾讯客服|
|40000407	|查询房间回包错误-数据包解析失败	|反馈腾讯客服|
|40000408	|查询房间回包错误-没有返回结果	|反馈腾讯客服|
|40000409	|查询房间回包错误-数据包解析失败	|反馈腾讯客服|
|40000410	|请求推流的房间不存在	|检查是否成功开房，推流的用户ID，groupid是否填写正确,或者用户是否已经退出房间|
|40000411	|发起推流用户不在房间内	|检查是否成功开房，推流的用户ID，groupid是否填写正确,或者用户是否已经退出房间|
|40000412	|停止推流重复发送，用户已经停止推流	|如果是推流停止操作说明已经停止，重复停止操作，无需处理|
|40000413	|停止推流重复发送，用户已经停止推流	|如果是推流停止操作说明已经停止，无需处理|
|40000414	|查询房间-服务器内部操作类型错误	|可能是网络问题，重试处理，重试失败反馈腾讯客服|
|40000415	|启动推流重复发送，用户正在推流	|如果是推流启动操作说明已经是在推流状态，无需处理|
|40000500	|启动推流频率控制	|非异常，同一个用户在3秒内重复请求推流会返回次错误，重试请求需要在上一次请求发起3秒后|





