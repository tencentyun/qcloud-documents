## 视频上传
|功能名称|API 名称|描述|
|-|-|-|
|发起上传| [ApplyUpload](https://cloud.tencent.com/document/product/266/9756)|发起视频文件的上传，获取文件上传到腾讯云对象存储 COS 的元信息。|
|上传文件|-|将视频（和封面）文件上传。|
|确认上传| [CommitUpload](https://cloud.tencent.com/document/product/266/9757)|确认视频文件（和视频封面文件）的上传，获取文件的播放地址和文件 ID。|
|URL 拉取视频上传| [MultiPullVodFile](https://cloud.tencent.com/document/product/266/7817)|通过用户传递的 URL，从已有的资源库批量拉取视频文件到腾讯云。|

## 视频处理
|功能名称|API 名称|描述|
|-|-|-|
|使用任务流处理视频|	[RunProcedure](https://cloud.tencent.com/document/product/266/11030)|依照指定的流程参数对视频文件进行处理。目前，具体流程参数需要与云点播商定。|
|对视频文件进行处理|	[ProcessFile](https://cloud.tencent.com/document/product/266/9642)|开发者可以通过该接口对单个视频发起多种处理任务。|
|视频转码|	[ConvertVodFile](https://cloud.tencent.com/document/product/266/7822)|依照控制台中的转码配置，对视频文件进行转码。|
|视频剪辑|	[ClipVideo](https://cloud.tencent.com/document/product/266/10156)|将源视频文件按指定偏移时间进行剪切。|
|视频拼接|	[ConcatVideo](https://cloud.tencent.com/document/product/266/7821)|将多个视频拼接成新视频文件，并添加到云点播系统。|
|指定时间点截图|	[CreateSnapshotByTimeOffset](https://cloud.tencent.com/document/product/266/8102)|获取视频文件在一组时间点的截图。|
|截取雪碧图|	[CreateImageSprite](https://cloud.tencent.com/document/product/266/8101)|对视频文件进行截图，生成雪碧图。|

## 媒资管理
|功能名称|API 名称|描述|
|-|-|-|
|获取视频信息|	[GetVideoInfo](https://cloud.tencent.com/document/product/266/8586)|可以获取单个视频的多种信息，也可以指定回包只返回部分信息。|
|依照视频名称前缀获取视频信息|	[DescribeVodPlayInfo](https://cloud.tencent.com/document/product/266/7825)|根据视频名称前缀搜索视频，并返回其播放信息列表。|
|依照 VID 查询视频信息|	[DescribeRecordPlayInfo](https://cloud.tencent.com/document/product/266/8227)|云直播、互动直播录制文件会进入云点播系统，每个录制文件会有唯一的 video_id（简称 vid）。|
|增加视频标签|	[CreateVodTags](https://cloud.tencent.com/document/product/266/7826)|为视频增加标签。|
|删除视频标签|	[DeleteVodTags](https://cloud.tencent.com/document/product/266/7827)|删除视频的标签。|
|删除视频|	[DeleteVodFile](https://cloud.tencent.com/document/product/266/7838)|删除视频文件。|
|修改视频属性|	[ModifyVodInfo](https://cloud.tencent.com/document/product/266/7828)|修改视频文件的描述信息（包括分类、名称、描述和过期时间等）。|
|增加打点信息|	[AddKeyFrameDesc](https://cloud.tencent.com/document/product/266/14190)|为视频增加打点信息，每个文件最多支持100个打点信息。|
|删除打点信息|	[DeleteKeyFrameDesc](https://cloud.tencent.com/document/product/266/13442)|删除视频的打点信息；支持一次删除单个视频的多个打点信息。|

## 视频分类管理
|功能名称|API 名称|描述|
|-|-|-|
|创建视频分类|	[CreateClass](https://cloud.tencent.com/document/product/266/7812)|用于管理视频文件，增加分类。|
|获取视频分类层次信息|	[DescribeAllClass](https://cloud.tencent.com/document/product/266/7813)|获得当前用户所有的分类层级关系。|
|获取视频分类信息|	[DescribeClass](https://cloud.tencent.com/document/product/266/7814)|获取全局分类列表，以及每个分类的具体信息。|
|修改视频分类|	[ModifyClass](https://cloud.tencent.com/document/product/266/7815)|修改视频分类的属性（包括名称）。|
|删除视频分类|	[DeleteClass](https://cloud.tencent.com/document/product/266/7816)|删除视频分类。|

## 事件通知与任务管理
|功能名称|API 名称|描述|
|-|-|-|
|拉取事件通知|	[PullEvent](https://cloud.tencent.com/document/product/266/7818)|用于从云点播服务端获取事件通知。|
|确认事件通知|	[ConfirmEvent](https://cloud.tencent.com/document/product/266/7819)|开发者调用拉取事件通知，获取到事件之后，必须调用该接口来确认消息已经收到。|
|查询任务列表|	[GetTaskList](https://cloud.tencent.com/document/product/266/11722)|查询任务列表，能查询到三天（72小时）内的任务。|
|查询任务信息|	[GetTaskInfo](https://cloud.tencent.com/document/product/266/11724)|用于获取任务的执行情况，只能查询到三天（72小时）内的任务。|
|重试任务|	[RedoTask](https://cloud.tencent.com/document/product/266/11725)|只能重试已结束三天（72小时）内的任务，执行之后任务 ID 不会改变，重试成功后会覆盖之前的数据。|

## 参数模板管理
|功能名称|API 名称|描述|
|-|-|-|
|创建转码模板|	[CreateTranscodeTemplate](https://cloud.tencent.com/document/product/266/9910)|创建新的转码模板。|
|查询转码模板列表|	[QueryTranscodeTemplateList](https://cloud.tencent.com/document/product/266/9913)|查询转码模板列表。|
|查询转码模板|	[QueryTranscodeTemplate](https://cloud.tencent.com/document/product/266/9912)|查询转码模板详细信息。|
|更新转码模板|	[UpdateTranscodeTemplate](https://cloud.tencent.com/document/product/266/9911)|更新转码模板。|
|删除转码模板|	[DeleteTranscodeTemplate](https://cloud.tencent.com/document/product/266/9914)|删除转码模板。|

## 水印模板管理
|功能名称|API 名称|描述|
|-|-|-|
|申请上传水印文件|	[ApplyUploadWatermark](https://cloud.tencent.com/document/product/266/11607)|在创建水印模板时，通过该接口获取水印文件的上传 URL。|
|创建水印模板|	[CreateWatermarkTemplate](https://cloud.tencent.com/document/product/266/11599)|创建新的水印模板。|
|查询水印模板列表|	[QueryWatermarkTemplateList](https://cloud.tencent.com/document/product/266/11608)|查询水印模板列表。|
|查询水印模板|  [QueryWatermarkTemplate](https://cloud.tencent.com/document/product/266/11606)|根据水印模板 ID，查询水印模板详细信息。|
|更新水印模板|	[UpdateWatermarkTemplate](https://cloud.tencent.com/document/product/266/11605)|更新水印模板。|
|删除水印模板|	[DeleteWatermarkTemplate](https://cloud.tencent.com/document/product/266/11604)|删除水印截图模板。|

## 密钥管理
|功能名称|API 名称|描述|
|-|-|-|
|获取视频解密密钥|	[DescribeDrmDataKey](https://cloud.tencent.com/document/product/266/9643)|用户在视频加密任务处理成功后调用该接口获取视频加密的数据密钥，用户需要自己保存该数据密钥。|

## 数据统计
|功能名称|API 名称|描述|
|-|-|-|
|获取播放统计数据文件下载地址|	[GetPlayStatLogList](https://cloud.tencent.com/document/product/266/12624)|查询每天的播放统计文件下载地址。|
|查询汇总的 CDN 统计数据|	[DescribeCdnStat](https://cloud.tencent.com/document/product/266/15290)|查询指定域名在指定时间段累计的 CDN 统计数据（流量、带宽、请求数和请求命中率）。|
|查询按地区及运营商分布的 CDN 统计数据|	[DescribeCdnRegionIspDetailStat](https://cloud.tencent.com/document/product/266/15329)|查询指定域名指定日期按地区、运营商统计的国内 CDN 节点数据（流量、带宽和请求数）。|
|查询详细的 CDN 统计数据|	[DescribeCdnDetailStat](https://cloud.tencent.com/document/product/266/15330)|查询指定域名在指定时间段的 CDN 统计数据明细（流量、带宽、请求数和请求命中率）。|
|查询域名列表|	[DescribeVodHosts](https://cloud.tencent.com/document/product/266/15331)|查询云点播域名的信息。|
|查询存储统计数据|	[DescribeStorage](https://cloud.tencent.com/document/product/266/15332)|查询使用的云点播存储空间。|
|查询每日 Top100 的视频播放统计数据|	[DescribePlayStatTopFiles](https://cloud.tencent.com/document/product/266/15333)|查询指定日期播放次数 Top100 的视频文件播放统计数据。|
|获取 CDN 日志下载链接|	[GetCdnLogList](https://cloud.tencent.com/document/product/266/15334)|获取指定时间段内云点播 CDN 的日志下载链接。|
|查询转码统计数据|	[DescribeTranscodeStat](https://cloud.tencent.com/document/product/266/15339)|查询指定时间段内每天的转码统计数据，包括编码格式、时长和次数。|


## 附录
以下接口是已废弃的服务端 API 接口，具体废弃原因请参见对应文档。

|功能名称|API 名称|描述|
|-|-|-|
|获取视频信息|	[DescribeVodPlayUrls](https://cloud.tencent.com/document/product/266/7824)|获取当前视频的播放信息（包括播放地址、格式、码率、高度和宽度信息）。|
|批量获取视频信息|	[DescribeVodInfo](https://cloud.tencent.com/document/product/266/7823)|根据 FileID 获取视频属性信息（包括名称、标签和创建时间等）。|
|依照指定流程处理视频|	[ProcessFileByProcedure](https://cloud.tencent.com/document/product/266/9045)|依照指定的流程参数对视频文件进行处理，可以指定的处理流程主要有：转码、创建雪碧图截图等。目前，具体流程参数需要与云点播商定。|
|HLS 视频简单剪切|	[SimpleClipHls](https://cloud.tencent.com/document/product/266/8859)|将源视频文件按指定偏移时间进行剪切，新生成的视频文件（目标文件）将拥有新的 FileID。|
|截图地址设为视频封面|	[DescribeVodCover](https://cloud.tencent.com/document/product/266/8814)|-|




