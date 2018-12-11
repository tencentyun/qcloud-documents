<div id="trtc-doc">

## TRTCLocalStatistics
### `width`
`@property (assign) uint32_t width;`

视频宽度 
### `height`
`@property (assign) uint32_t height;`

视频高度 
### `frameRate`
`@property (assign) uint32_t frameRate;`

帧率（fps） 
### `videoBitrate`
`@property (assign) uint32_t videoBitrate;`

视频发送码率（Kbps） 
### `audioSampleRate`
`@property (assign) uint32_t audioSampleRate;`

音频采样率（Hz） 
### `audioBitrate`
`@property (assign) uint32_t audioBitrate;`

音频发送码率（Kbps） 
### `streamType`
`@property (assign) TRTCVideoStreamType streamType;`

流类型（大画面 | 小画面 | 辅路画面） 

## TRTCRemoteStatistics
### `userId`
`@property (retain) NSString * userId;`

用户ID，指定是哪个用户的视频流 
### `finalLoss`
`@property (assign) uint32_t finalLoss;`

该线路的总丢包率(%)

这个值越小越好，比如： 0% 的丢包率代表网络很好 这个丢包率是该线路的 userid 从上行到服务器再到下行的总丢包率 如果 downLoss 为 0%, 但是 finalLoss 不为 0，说明该 userId 在上行就出现了无法恢复的丢包 
### `width`
`@property (assign) uint32_t width;`

视频宽度 
### `height`
`@property (assign) uint32_t height;`

视频高度 
### `frameRate`
`@property (assign) uint32_t frameRate;`

接收帧率（fps） 
### `videoBitrate`
`@property (assign) uint32_t videoBitrate;`

视频码率（Kbps） 
### `audioSampleRate`
`@property (assign) uint32_t audioSampleRate;`

音频采样率（Hz） 
### `audioBitrate`
`@property (assign) uint32_t audioBitrate;`

音频码率（Kbps） 
### `streamType`
`@property (assign) TRTCVideoStreamType streamType;`

流类型（大画面 | 小画面 | 辅路画面） 

## TRTCStatistics
### `upLoss`
`@property (assign) uint32_t upLoss;`

C -> S 上行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着 SDK 向服务器发送的每 10 个数据包中就会有 3 个会在上行传输中丢失 
### `downLoss`
`@property (assign) uint32_t downLoss;`

S -> C 下行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着服务器向 SDK 发送的每 10 个数据包中就会有 3 个会在下行传输中丢失 
### `appCpu`
`@property (assign) uint32_t appCpu;`

当前 App 的 CPU 使用率 (%) 
### `systemCpu`
`@property (assign) uint32_t systemCpu;`

当前系统的 CPU 使用率 (%) 
### `rtt`
`@property (assign) uint32_t rtt;`

延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好 一般低于 50ms 的 rtt 是比较理想的情况，而高于 100ms 的 rtt 会引入较大的通话延时 由于数据上下行共享一条网络连接，所以 local 和 remote 的 rtt 相同 
### `receivedBytes`
`@property (assign) uint64_t receivedBytes;`

总接收字节数(包含信令及音视频) 
### `sentBytes`
`@property (assign) uint64_t sentBytes;`

总发送字节数(包含信令及音视频) 
### `localStatistics`
`@property (strong) NSArray< TRTCLocalStatistics * > * localStatistics;`

自己本地的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组 
### `remoteStatistics`
`@property (strong) NSArray< TRTCRemoteStatistics * > * remoteStatistics;`

远端成员的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组 


</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>
