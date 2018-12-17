<div id="trtc-doc">

## TRTCStatistics
### `appCpu`
`int com.tencent.trtc.TRTCStatistics.appCpu`

当前 App 的 CPU 使用率 (%) 
### `systemCpu`
`int com.tencent.trtc.TRTCStatistics.systemCpu`

当前系统的 CPU 使用率 (%) 
### `rtt`
`int com.tencent.trtc.TRTCStatistics.rtt`

延迟（毫秒）：代表 SDK 跟服务器一来一回之间所消耗的时间，这个值越小越好 一般低于 50ms 的 rtt 是比较理想的情况，而高于 100ms 的 rtt 会引入较大的通话延时 由于数据上下行共享一条网络连接，所以 local 和 remote 的 rtt 相同 
### `upLoss`
`int com.tencent.trtc.TRTCStatistics.upLoss`

C -> S 上行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着 SDK 向服务器发送的每 10 个数据包中就会有 3 个会在上行传输中丢失 
### `downLoss`
`int com.tencent.trtc.TRTCStatistics.downLoss`

S -> C 下行丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 而 30% 的丢包率则意味着服务器向 SDK 发送的每 10 个数据包中就会有 3 个会在下行传输中丢失 
### `sendBytes`
`long com.tencent.trtc.TRTCStatistics.sendBytes`

发送字节总数，注意是字节数（bytes），不是比特数（bits） 
### `receiveBytes`
`long com.tencent.trtc.TRTCStatistics.receiveBytes`

接收字节总数，注意是字节数（bytes），不是比特数（bits） 
### `localArray`
`ArrayList<TRTCLocalStatistics> com.tencent.trtc.TRTCStatistics.localArray`

自己本地的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组 
### `remoteArray`
`ArrayList<TRTCRemoteStatistics> com.tencent.trtc.TRTCStatistics.remoteArray`

远端成员的音视频统计信息，由于可能有大画面、小画面以及辅路画面等多路的情况，所以是一个数组 

## TRTCRemoteStatistics
### `userId`
`String com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.userId`

用户ID，指定是哪个用户的视频流 
### `finalLoss`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.finalLoss`

该线路的总丢包率(%)，这个值越小越好，比如： 0% 的丢包率代表网络很好， 这个丢包率是该线路的 userid 从上行到服务器再到下行的总丢包率 如果 downLoss 为 0%, 但是 finalLoss 不为 0，说明该 userId 在上行就出现了无法恢复的丢包 
### `width`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.width`

视频宽度 
### `height`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.height`

视频高度 
### `frameRate`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.frameRate`

接收帧率（fps） 
### `videoBitrate`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.videoBitrate`

视频码率（Kbps） 
### `audioSampleRate`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.audioSampleRate`

音频采样率（Hz） 
### `audioBitrate`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.audioBitrate`

音频码率（Kbps） 
### `streamType`
`int com.tencent.trtc.TRTCStatistics.TRTCRemoteStatistics.streamType`

流类型（大画面 | 小画面 | 辅路画面） 

## TRTCLocalStatistics
### `width`
`int com.tencent.trtc.TRTCStatistics.TRTCLocalStatistics.width`

视频宽度 
### `height`
`int com.tencent.trtc.TRTCStatistics.TRTCLocalStatistics.height`

视频高度 
### `frameRate`
`int com.tencent.trtc.TRTCStatistics.TRTCLocalStatistics.frameRate`

帧率（fps） 
### `videoBitrate`
`int com.tencent.trtc.TRTCStatistics.TRTCLocalStatistics.videoBitrate`

视频发送码率（Kbps） 
### `audioSampleRate`
`int com.tencent.trtc.TRTCStatistics.TRTCLocalStatistics.audioSampleRate`

音频采样率（Hz） 
### `audioBitrate`
`int com.tencent.trtc.TRTCStatistics.TRTCLocalStatistics.audioBitrate`

音频发送码率（Kbps） 
### `streamType`
`int com.tencent.trtc.TRTCStatistics.TRTCLocalStatistics.streamType`

流类型（大画面 | 小画面 | 辅路画面） 


</div>
<style>
#trtc-doc h2 code, #trtc-doc h3 code, #trtc-doc h4 code { display:block; padding:3px 5px; background: #E3F3FF; color: #333; text-shadow:0px 1px #BCD2E2; }
//#trtc-doc h2{ font-size:28px !important;}
#trtc-doc table td:nth-child(1){font-family: 'Lucida Console', Monaco, monospace; font-size:14px !important; color: #4078c0}
#trtc-doc table tr:nth-child(even){background: #fafafa;}
</style>
