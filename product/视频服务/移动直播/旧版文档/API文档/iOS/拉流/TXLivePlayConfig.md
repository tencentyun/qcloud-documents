

__功能__
 
腾讯云直播播放器的参数配置模块。 

__介绍__ 

主要负责 [TXLivePlayer](https://cloud.tencent.com/document/product/454/34762) 对应的参数设置，其中绝大多数设置项在播放开始之后再设置是无效的。




__属性列表__

| 属性 | 类型 | 字段含义 | 推荐取值 | 特别说明 |
|-----|-----|-----|-----|-----|
| cacheTime | float | 播放器缓存时间，单位秒，取值需要大于0，默认值：5。 | - | - |
| bAutoAdjustCacheTime | BOOL | 是否自动调整播放器缓存时间，默认值：YES YES：启用自动调整，自动调整的最大值和最小值可以分别通过修改 maxCacheTime 和 minCacheTime 来设置 NO：关闭自动调整，采用默认的指定缓存时间（1s），可以通过修改 cacheTime 来调整缓存时间。 | - | - |
| maxAutoAdjustCacheTime | float | 播放器缓存自动调整的最大时间，单位秒，取值需要大于0，默认值：5。 | - | - |
| minAutoAdjustCacheTime | float | 播放器缓存自动调整的最小时间，单位秒，取值需要大于0，默认值为1。 | - | - |
| videoBlockThreshold | int | 播放器视频卡顿报警阈值，单位毫秒。 | 800 | 只有渲染间隔超过这个阈值的卡顿才会有 PLAY_WARNING_VIDEO_PLAY_LAG 通知。 |
| connectRetryCount | int | 播放器遭遇网络连接断开时 SDK 默认重试的次数，取值范围1 - 10，默认值：3。 | - | - |
| connectRetryInterval | int | 网络重连的时间间隔，单位秒，取值范围3 - 30，默认值：3。 | - | - |
| enableAEC | BOOL | 是否开启回声消除， 默认值为 NO。 | - | - |
| enableMessage | BOOL | 是否开启消息通道， 默认值为 NO。 | - | - |
| playerPixelFormatType | OSType | 视频渲染对象回调的视频格式，默认值：kCVPixelFormatType_420YpCbCr8Planar。 | - | 支持：kCVPixelFormatType_420YpCbCr8Planar 和 kCVPixelFormatType_420YpCbCr8BiPlanarFullRange。 |
| enableNearestIP | BOOL | 是否开启就近选路，待废弃，默认值：YES。 | - | - |
| rtmpChannelType | int | RTMP 传输通道的类型，待废弃，默认值为：RTMP_CHANNEL_TYPE_AUTO。 | - | - |
| cacheFolderPath | NSString * | 视频缓存目录，点播 MP4、HLS 有效。 | - | - |
| maxCacheItems | int | 最多缓存文件个数，默认值：0。 | - | - |
| headers | NSDictionary * | 自定义 HTTP Headers。 | - | - |



