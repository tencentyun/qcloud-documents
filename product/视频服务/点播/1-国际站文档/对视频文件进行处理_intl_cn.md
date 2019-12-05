## 接口名称
ProcessFile

## 功能说明
该接口是点播任务流相关接口中的一个。开发者可以通过该接口对单个视频发起多种处理任务，包括：
1. 视频转码（包括水印、加密、转封装）；
2. 采样截图；
3. 使用截图设置封面。

该接口为异步接口，即：调用该接口只是发起一系列视频处理任务。任务流中的任务状态变更（包括结束）可以通过[事件通知](#.E4.BA.8B.E4.BB.B6.E9.80.9A.E7.9F.A5)机制感知。

任务执行完毕之后，每项异步任务的执行结果（例如转码输出文件URL）可以通过[GetVideoInfo](/document/product/266/8586)接口获得。

**注意：该接口仅支持点播4.0。**

## 事件通知

任务流状态变更（或者处理完成）会触发[事件通知-任务流状态变更通知](/document/product/266/9636)。APP后台可据此监听任务流的执行状态。

更多参见[服务端事件通知简介](/document/product/266/7829)。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 请求参数说明

| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| fileId | 是 | String | 文件ID |
| transcode | 否 | Object | 参见[转码控制参数](#transcode.EF.BC.88.E8.BD.AC.E7.A0.81.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| sampleSnapshot | 否 | Object | 参见[采样截图控制参数](#samplesnapshot.EF.BC.88.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E5.8F.82.E6.95.B0.EF.BC.89) |
| coverBySnapshot | 否 | Object | 参见[使用截图设置封面控制参数](#coverbysnapshot.EF.BC.88.E4.BD.BF.E7.94.A8.E6.88.AA.E5.9B.BE.E8.AE.BE.E7.BD.AE.E8.A7.86.E9.A2.91.E5.B0.81.E9.9D.A2.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| snapshotByTimeOffset | 否 | Object | 参见[指定时间点截图控制参数](#snapshotbytimeoffset.EF.BC.88.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.8E.A7.E5.88.B6.E5.8F.82.E6.95.B0.EF.BC.89) |
| notifyMode | 否 | String | 任务流状态变更通知模式。Finish：只有当任务流全部执行完毕时，才发起一次事件通知；Change：只要任务流中每个子任务的状态发生变化，都进行事件通知； None：不接受该任务流回调。 默认为Finish。 | 
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

#### transcode（转码控制参数）

| **参数名称** | **必填** | **类型** | **描述** |
|---------|---------|---------|---------|
| definition | 是 | Array | 若HLS转封装MP4，输入格式9；若MP4转封装HLS，输入格式6；转码输出模板号，参见[转码参数模板](/document/product/266/8098)|
| watermark | 否 | Integer | 参见[水印参数模板](/document/product/266/9647)。 目前只能填1，表示默认模板。 不填则不带水印 |
| hlsMasterPlaylist  | 否 | Integer | 若指定的转码输出参数包含多种HLS规格，并且指定了hlsMasterPlaylist=1，那么转码结束后将生成包含HLS Master Playlist的多码率HLS文件，该文件的definition固定为10000。 使用支持HLS标准的播放器播放该文件，将能够实现根据码率自适应选择视频流播放|
| disableHigherBitrate | 否 | Integer | 是否禁止从较低码率转为较高码率。0：不禁止；1：禁止。默认不禁止。（注1） |
| drm | 否 | Object | 视频加密控制参数，参见[视频加密解决方案](/document/product/266/9638)。 | 
| drm.definition | 是 | Integer | 加密方式，参见[视频加密参数模板](/document/product/266/9645)。 |

任务流执行完毕之后，转码结果可以从[GetVideoInfo](https://cloud.tencent.com/document/product/266/8586)接口应答包体中的[transcodeInfo](/document/product/266/8586#transcodeinfo.EF.BC.88.E8.A7.86.E9.A2.91.E8.BD.AC.E7.A0.81.E7.BB.93.E6.9E.9C.E4.BF.A1.E6.81.AF.EF.BC.89)对象获取到。

> 注1：
> 将低码率视频文件转为高码率视频，会导致无谓的带宽浪费。如果启用该选项，则当目标转码模板的码率高于源视频的码率时，该目标模板将被忽略。例如，假设原始视频的码率为800kbps，目标转码输出模板号为10、20、30、40，码率分别为256kbps，512kbps，1024kbps，2500kbps，则30、40两个转码模板将被忽略，只会转出10和20两个模板。

#### sampleSnapshot（采样截图控制参数）

| **参数名称** | **必填** | **类型** | **描述** |
|---------|---------|---------|---------|
| definition | 是 | Integer | 采样截图模板号，参见[采样截图参数模板](/document/product/266/9050)。 |

任务流执行完毕之后，截图URL可以从[GetVideoInfo](/document/product/266/8586)接口应答包体中的sampleSnapshotInfo.imageUrls字段中获取到。

#### snapshotByTimeOffset（指定时间点截图控制参数）

| **参数名称** | **必填** | **类型** | **描述** |
|---------|---------|---------|---------|
| definition | 是 | Integer | 指定时间点截图模板号，参见[截图参数模板](/document/product/266/8097)。 |
| timeOffset | 是 | Array | 整形数组，截图的时间偏移，单位为毫秒。 |

任务流执行完毕之后，时间点截图信息可以从[GetVideoInfo](/document/product/266/8586)接口应答包体中的snapshotByTimeOffsetInfo字段获取。

#### coverBySnapshot（使用截图设置视频封面控制参数）

| **参数名称** | **必填** | **类型** | **描述** |
|---------|---------|---------|---------|
| definition | 是 | Integer | 指定时间点截图模板号，参见[截图参数模板](/document/product/266/8097)。 |
| positionType | 是 | String | 截图方式。Time：依照时间点截图；Percent：依照百分比截图。 |
| position | 是 | Integer | 截图位置。对于依照时间点截图，该值表示指定视频第几秒的截图作为封面；对于依照百分比截图，该值表示使用视频百分之多少的截图作为封面。 |

任务流执行完毕之后，截图URL可以从[GetVideoInfo](/document/product/266/8586)接口应答包体中的basicInfo.coverUrl字段中获取到。

<!--
#### imageSprite（雪碧图控制参数）

| **参数名称** | **必填** | **类型** | **描述** |
|---------|---------|---------|---------|
| definition | 是 | Integer | 雪碧图截图模板号，参见[雪碧图参数模板](/document/product/266/8099)。 |

任务流执行完毕之后，雪碧图结果可以从[GetVideoInfo](/document/product/266/8586)接口应答包体中的[imageSpriteInfo](/document/product/266/8586#imagespriteinfo.EF.BC.88.E8.A7.86.E9.A2.91.E9.9B.AA.E7.A2.A7.E5.9B.BE.E4.BF.A1.E6.81.AF.EF.BC.89)对象获取到。
-->


### 请求示例

#### 通用视频转码示例
以下示例的含义是：
1. 对视频进行转码，转码输出模板为10，20，30，40，要求禁止将低码率视频转为高码率视频；
1. 转码过程需要设置水印，水印模板号为1，即默认模板；
1. 对视频进行采样截图，采样截图的模板号为10；
任务流中每个子任务的状态发生变化，都需要发起事件通知。


```
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFile
&fileId=24961954183381008
&transcode.definition.0=210
&transcode.definition.1=220
&transcode.definition.3=230
&transcode.definition.4=240
&transcode.disableHigherBitrate=1
&transcode.watermark=1
&sampleSnapshot.definition=10
&notifyMode=Change
&COMMON_PARAMS
```

#### 视频加密转码示例

以下示例的含义是：
1. 对视频文件进行转码，目标输出模板为210，220，230，240，要求禁止将低码率视频转为高码率视频；
1. 转码过程需要对视频文件进行加密，使用模板号为10的加密策略进行加密；
1. 当整个任务流执行完毕之后，再发起事件通知。

```
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFile
&fileId=24961954183381008
&transcode.definition.0=210
&transcode.definition.1=220
&transcode.definition.3=230
&transcode.definition.4=240
&transcode.disableHigherBitrate=1
&transcode.drm.definition=10
&notifyMode=Finish
&COMMON_PARAMS
```

#### 视频生成多码率HLS文件示例

以下示例的含义是：
1. 对视频文件进行转码，目标输出模板为210，220，230，240，要求禁止将低码率视频转为高码率视频；
1. 生成包含210，220，230，240这四种码率的HLS文件；
1. 当整个任务流执行完毕之后，再发起事件通知。

```
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFile
&fileId=24961954183381008
&transcode.definition.0=210
&transcode.definition.1=220
&transcode.definition.3=230
&transcode.definition.4=240
&transcode.disableHigherBitrate=1
&transcode.hlsMasterPlaylist=1
&notifyMode=Finish
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功；其他值: 失败 |
| message | String | 错误信息 |
| vodTaskId | String | 任务id |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |


### 应答示例
```javascript
{
    "code": 0,
    "message": "",
    "vodTaskId": "125xx-Procedure-6a651e8d148c512af27f3b5f3d60f43a"
}
```
