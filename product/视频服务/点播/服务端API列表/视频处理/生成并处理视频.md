## 接口名称
RunProcedure

## 功能说明
该接口依照指定的流程参数对视频文件进行处理，可以指定的处理流程主要有：转码、创建雪碧图、截图等。目前，具体流程参数需要与腾讯云点播商定。
待处理的视频既可以直接指定，也可以依据一定的流程来生成，比如对多个文件通过剪辑、拼接生成或者是转拉视频文件。
该接口为异步接口，即：调用该接口只是发起一系列视频处理任务。任务流中的任务状态变更（包括结束）可以通过[事件通知](#.E4.BA.8B.E4.BB.B6.E9.80.9A.E7.9F.A5)机制感知。

任务执行完毕之后，每项异步任务的执行结果（例如转码输出文件URL）可以通过[GetVideoInfo](/document/product/266/8586)接口获得。
*本接口只支持点播4.0*

## 事件通知

任务流状态变更（或者处理完成）会触发[事件通知-任务流状态变更通知](/document/product/266/9636)。APP后台可据此监听任务流的执行状态。

更多参见[服务端事件通知简介](/document/product/266/7829)。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| inputType | 是 | String | 输入视频的方式，SingleFile：直接指定要处理的文件ID，MultiFile：指定文件列表和剪辑参数生成操作的文件ID，Stream：指定流ID和剪辑参数生成操作的文件ID,PullFile:指定要拉取的视频文件url|
| file | 否 | Object | 处理的视频文件信息，inputType为SingleFile时有效 |
| file.id | 否 | String | 处理的视频文件的ID |
| file.startTimeOffset | 否 | Integer | 剪辑的文件内起始偏移 |
| file.endTimeOffset | 否 | Integer | 剪辑的文件内结束偏移 |
| fileList | 否 | Array | 处理的视频文件列表，inputType为MultiFile时有效 |
| fileList.n.id | 否 | String | 处理的视频文件的ID |
| fileList.n.startTimeOffset | 否 | Integer | 剪辑的文件内起始偏移 |
| fileList.n.endTimeOffset | 否 | Integer | 剪辑的文件内结束偏移 |
| stream | 否 | Object | 处理的流ID信息，inputType为Stream时有效 |
| stream.streamId | 是 | String | 录制的流ID |
| stream.startTimeStamp | 是 | Integer | 剪辑的录制开始时间 |
| stream.endTimeStamp | 是 | Integer | 剪辑的录制结束时间 |
| pull | 否 | Object | 拉取视频的信息，inputType为PullFile时有效 |
| pull.url | 是 | String | 需要拉取的视频文件的url，inputType为PullFile时必须提供该参数 |
| pull.fileName | 是 | String | 视频文件的名称，inputType为PullFile时必须提供该参数 |
| pull.fileMd5 | 否 | String | 视频文件的MD5，inputType为PullFile时有效 |
| pull.classId | 否 | Integer | 视频的分类ID，inputType为PullFile时有效 |
| procedure | 是 | String | 流程参数 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例

#### 指定单个fileId请求示例
以下示例的含义是：
对指定fileId的文件剪辑后发起任务流

```
https://vod.api.qcloud.com/v2/index.php?Action=RunProcedure
&inputType=SingleFile
&file.id=12345
&file.startTimeOffset=10
&file.endTimeOffset=25
&procedure=SomeProcedure
&COMMON_PARAMS
```

#### 通过指定剪辑文件ID列表请求示例
以下示例的含义是：
1.把fileId为12345的文件按视频内区间（30，100）剪辑，fileId为67899的文件按视频内区间（300，400）剪辑
2.然后再把剪辑的结果拼接成目标文件，格式是mp4
3.最后对目标文件发起任务流。

```
https://vod.api.qcloud.com/v2/index.php?Action=RunProcedure
&inputType=MultiFile
&fileList.0.id=12345
&fileList.0.startTimeOffset=30
&fileList.0.endTime=100
&fileList.1.id=67899
&fileList.1.startTimeOffset=300
&fileList.1.endTime=400
&procedure=SomeProcedure
&COMMON_PARAMS
```

#### 通过录制流信息请求示例
以下示例的含义是：
1.把streamId为12345的所有fileId按录制时间区间（15020876538，15020876638）剪辑
2.然后再把剪辑的结果拼接成目标文件，格式是mp4
3.最后对目标文件发起任务流。

```
https://vod.api.qcloud.com/v2/index.php?Action=RunProcedure
&inputType=Stream
&stream.streamId=12345
&stream.startTimeStamp=15020876538
&stream.endTimeStamp=1502087638
&procedure=SomeProcedure
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| vodTaskId | String | 任务id |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1 | 内部错误  |
| 1000 | 无效参数  |
| 1001 | 内部错误  |
| 1003 | 内部错误  |
| 2000 | 内部错误  |
| 10008 | 文件不存在  |
| 10022 | 内部错误 |
| 50005 | Procedure重复任务已存在 |
| 50006 | Procedure任务创建失败 |
| 50007 | Procedure参数无效 |

### 应答示例
```javascript
{
    "code": 0,
    "message": "",
    "vodTaskId": "procedure-7a2229a8f1957bfce08ba733fbfd4a3c",
}
```
如果开启了回调通知，每个任务完成后会单独回调，参见[服务端事件通知简介](/document/product/266/7829)。
