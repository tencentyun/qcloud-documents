## 场景说明
在远程教育、秀场直播、视频会议、远程定损、金融双录、在线医疗等应用场景中，考虑取证、质检、审核、存档和回放等需求，常需要将整个视频通话或互动直播过程录制和存储下来的情况。

>? 下文将针对实时音视频最新推出的云端录制能力进行使用说明，如果您当前的 TRTC 应用（sdkappid）使用的是旧版云端录制，详情请参见 [旧版云端录制](https://cloud.tencent.com/document/product/647/16823)。判断当前应用的云端录制的类型和旧版云端录制能力切换为新版的方式，详情请参见 [控制台>云端录制说明](https://cloud.tencent.com/document/product/647/50768#.E4.BA.91.E7.AB.AF.E5.BD.95.E5.88.B6.E9.85.8D.E7.BD.AE)。

## 功能说明
通过 TRTC 的云端录制功能，您可以将房间中的每一个用户的音视频流都录制成独立的文件（单流录制），或者把同一个房间的音视频媒体流合流录制成一个文件（合流录制）。
- **订阅流**： 我们支持通过制定订阅用户的黑白名单的方式来指定您需要订阅的用户媒体流**（仅支持 API 录制）**。
- **转码参数**：合流的场景下，我们支持通过设置编解码的参数来指定录制的视频文件的质量。
- **合流参数**：合流的场景下，我们支持多种灵活可变的自动多画面布局模板和自定义布局模板。
- **文件存储**：支持存储到云点播主应用或者子应用账号体系下，目前只支持腾讯云点播。
- **回调通知**：我们支持回调通知的能力，通过配置您的回调域名，云端录制的事件状态会通知到您的回调服务器。

### 单流录制和合流录制说明
#### 单流录制
如下图所示为单流录制的场景，房间1234里面主播1和主播2都上行了音视频流，假设您订阅了主播1和主播2的音视频流，并设置录制模式为单流录制，录制后台会分别拉取主播1和主播2的音视频流，并把他们录制成独立的媒体文件包含：
- 主播1的一个音视频 MP4 录制文件。
- 主播2的一个音视频 MP4 录制文件。

录制后台会把这些文件上传到您指定的 [云点播](https://console.cloud.tencent.com/vod)。具体录制流程如下：
![](https://qcloudimg.tencent-cloud.cn/raw/cdbc605589bc736c489349f38b490035.png)

#### 合流录制
如下图所示为合流录制的场景，房间1234里面有主播1和主播2都上行了音视频流，假设您订阅了主播1和主播2的音视频流，设置录制模式为合流录制，录制后台会分别拉取主播1和主播2的音视频流，并把他们的视频流按照您配置多画面模板进行合流，音频流进行混音，最后把媒体流混合成一路媒体文件。包含：合流后的的一个音视频 MP4 录制文件。

录制后台会把这些文件上传到您指定的云点播，您需要通过回调保存对应录制文件的存于云点播的 [媒资信息](https://cloud.tencent.com/document/product/266/36451)。
![](https://qcloudimg.tencent-cloud.cn/raw/d8b0f3d0e5ecea18b448843324268a10.png)

[](id:mp4_file)
### 录制 MP4 文件说明
录制 MP4 文件切分的条件：
- 录制时长超过24小时。
- 单个 MP4 文件大小达到 2GB。

[](id:upload_vod)
### 录制上传点播说明
录制后台会在录制结束后将录制的 MP4 文件通过您指定的方式上传到点播平台，并通过回调的形式把播放地址发送给您。如果录制模式为单流录制模式，每一个订阅的主播都会有一个对应的播放地址；如果录制模式为合流录制模式，只有一个合流后媒体的播放地址。
1. 通过 API 发起录制：存储参数中必须指定 CloudVod 参数。
2. 上传点播任务的过程中使用 DescribeCloudRecording 只能查询到录制任务进行状态，不会携带录制文件的信息。

[](id:limit)
### API 接口和录制并发限制
- 录制接口的调用频率限制为20qps（如需提高 QPS 请 [提交工单](https://console.cloud.tencent.com/workorder/category)）。
- 单个接口超时时间为6秒。
- 默认并发录制支持100路，如果需要更多路数，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。
- 单次录制任务最大支持同时订阅的房间内主播数为25个，主播只上行音频也会单独占据一路。

[](id:record)
## 录制控制方案
TRTC 提供了两种云端录制方案，分别是 API 调用录制和全局自动录制，这两种方案并不冲突，可以同时使用两种录制方案。API录制相比全局自动录制的优点是录制灵活、功能完备，客户可以指定录制订阅房间内的主播，自定义合流布局，录制中途更新布局和订阅等。全局自动录制的优点是录制不需客户启动和停止，由 TRTC 后台管理录制任务。

[](id:API_record)
### 方案一：API 录制
[](id:action)
#### 启动录制
通过您的后台服务调用 REST API （[CreateCloudRecording](https://cloud.tencent.com/document/api/647/73786)）来启动云端的录制，需要重点关注参数— **任务 ID（TaskId）**；这个参数是本次录制任务的唯一标识，您需要保存下这个任务 ID 作为后续针对这个录制任务接口操作的输入参数。

[](id:RecordMode)
#### 录制的模式（[RecordMode](https://cloud.tencent.com/document/api/647/44055#RecordParams)）
- 单流录制，实时录制房间内每个主播的音频视频 HLS 文件，转码后上传每个用户的 MP4 录制文件到云点播。
- 合流录制，将房间内您所订阅所有主播的音视频流混录成一个 HLS 音视频文件, 转码后上传合流录制 MP4 文件到云点播。

[](id:SubscribeStreamUserIds)
#### 录制用户的黑白名单（[SubscribeStreamUserIds](https://cloud.tencent.com/document/api/647/44055#RecordParams)）
默认情况下，云端录制会订阅房间内所有的媒体流（最多25路）超过25个用户，默认录制最先进房的25位主播。您也可以通过该参数指定订阅的主播用户的黑白名单信息，当然我们也支持在录制的过程中进行更新操作。单流录制场景，如果房间内主播超过25人，可以通过设置订阅名单发起多次录制任务实现。

[](id:rude)
#### 录制文件名命名规则
- **单流录制** MP4 文件名规则：`<SdkAppId>_<RoomId>_UserId_s_<UserId>_UserId_e_<MediaId>_<Index>.mp4`
- **合流录制** MP4 文件名规则：`<SdkAppId>_<RoomId>_<Index>.mp4`
- **字段含义说明**：
<table>
<thead><tr><th>字段</th><th>含义</th></tr></thead>
<tbody><tr>
<td>&lt;SdkAppId&gt;</td>
<td>录制任务的 SdkAppId</td>
</tr>
<tr>
<td>&lt;RoomId&gt;</td>
<td>录制的房间号</td>
</tr>
<tr>
<td>&lt;UserId&gt;</td>
<td>特殊的 base64 处理后的录制流的用户 ID<ul style="margin:0">
    <li>如果这里 &lt;RoomId&gt; 如果是字符串房间 ID，我们会对房间 ID 先做 base64 操作，再把 base64 后的字符串中符号“/”替换成“-” (中划线)，符号“=”替换成“.” </li>
    <li>录制流的 &lt;UserId&gt; 会先做 base64 操作，再把 base64 后的字符串中符号“/”替换成“-” (中划线)，符号“=”替换成“.” </li>
</ul></td>
</tr>
<tr>
<td>&lt;MediaId&gt;</td>
<td>主辅流标识，main 或者 aux</td>
</tr>
<tr>
<td>&lt;Index&gt;</td>
<td>如果没有触发 MP4 切片逻辑（大小超过2GB或时长超过24小时）则无该字段，否则为切片的索引号，从1开始递增</td>
</tr>
</tbody></table>

[](id:time)
#### **录制开始的时间的获取**
通过订阅回调，监听录制回调事件。在事件类型311中的 BeginTimeStamp 字段您可以获取到录制文件对应的录制起始时间戳，EndTimeStamp 字段可以获取到对应的录制结束时间戳。
````json
{
    "EventGroupId": 3,
    "EventType": 311,
    "CallbackTs": 1622186289148,
    "EventInfo": {
        "RoomId": "xx",
        "EventTs": "1622186289",
        "UserId": "xx",
        "TaskId": "xx",
        "Payload": {
            "UserId": "anchor1",
            "TrackType": "video",
            "MediaId": "main",
            "FileId": "xxxxx",
            "VideoUrl": "http://xxxxx",
            "CacheFile": "xxxxxx",
            "BeginTimeStamp": 1622186279,
            "EndTimeStamp": 1622186811
        }
    }
}
```

[](id:MixLayoutMode)
#### 合流录制的布局模式参数（[MixLayoutMode](https://cloud.tencent.com/document/api/647/44055#MixLayoutParams)）
支持 [悬浮布局](#float)、[屏幕分享布局](#share)、[九宫格布局（默认）](#nine) 和 [自定义布局](#customize) 四种布局：

- **悬浮布局**：[](id:float)
默认第一个进入房间的主播（也可以指定一个主播）的视频画面会铺满整个屏幕。其他主播的视频画面从左下角开始依次按照进房顺序水平排列，显示为小画面，小画面悬浮于大画面之上。当画面数量小于等于17个时，每行4个（4 × 4排列）。当画面数量大于17个时，重新布局小画面为每行5个（5 × 5）排列。最多支持25个画面，如果用户只发送音频，仍然会占用画面位置。
悬浮布局随着订阅的子画面增加按照下图进行变化：
<table>
<tr>
    <th>子画面小于等于17个时</th>
    <td width=40%><ul>
        <li>每个小画面的宽和高分别为整个画布宽和高的 0.235</li>
        <li>相邻小画面的左右和上下间距分别为整个画布宽和高的 0.012</li>
        <li>小画面距离画布的水平和垂直边距也分别为整个画布宽和高的 0.012</li>
    </ul></td>
    <td width=40%><img src="https://qcloudimg.tencent-cloud.cn/raw/31047fcd48526ab0876199c7b3a6832f.jpg"></td>
</tr><tr>
    <th>子画面大于17个时</th>
    <td><ul>
        <li>每个小画面的宽和高分别为整个画布宽和高的 0.188</li>
        <li>相邻小画面的左右和上下间距分别为整个画布宽和高的 0.01</li>
        <li>小画面距离画布的水平和垂直边距也分别为整个画布宽和高的 0.01</li>
    </ul></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/19ff366a2e23294a9ee3237a7319b83b.jpg"></td>
</tr>
</table>

- **屏幕分享布局**：[](id:share)
指定一个主播在屏幕左侧的大画面位置（如果不指定，那么大画面位置为背景色），其他主播自上而下依次垂直排列于右侧。当画面数量少于17个的时候，右侧每列最多8人，最多占据两列。当画面数量多于17个的时候，超过17个画面的主播从左下角开始依次水平排列。最多支持24个画面，如果主播只发送音频，仍然会占用画面位置。
屏幕分享布局随着订阅的子画面增加按照下图进行变化：
<table>
<tr>
    <th width=10%>子画面小于等于5个时</th>
    <td width=40%><ul>
        <li>右侧小画面的宽为整个画布宽的1/5，右侧小画面的高为整个画布高的1/4</li>
        <li>左侧大画面的宽为整个画布宽的4/5，左侧大画面的高为整个画布高</li>
    </ul></td>
    <td width=40%><img src="https://qcloudimg.tencent-cloud.cn/raw/2b062b86b3ce46390382a984cdb69c2e.jpeg"></td>
</tr>   <tr>
    <th>子画面大于5且小于等于7个时</th>
    <td><ul>
        <li>右侧小画面的宽为整个画布宽的1/7，右侧小画面的高为整个画布高的1/6</li>
        <li>左侧大画面的宽为整个画布宽的6/7，左侧大画面的高为整个画布高</li>
    </ul></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/15b6afda68597b07f3057730e2cb8114.jpeg"></td>
</tr><tr>
    <th>子画面大于7且小于等于9个时</th>
    <td><ul>
        <li>右侧小画面的宽为整个画布宽的1/9，右侧小画面的高为整个画布高的1/8</li>
        <li>左侧大画面的宽为整个画布宽的8/9，左侧大画面的高为整个画布高</li>
    </ul></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/a1fde386c34877d6a6bcf9bbaaabcb09.jpeg"></td>
</tr><tr>
    <th>子画面大于9小于等于17个时</th>
    <td><ul>
        <li>右侧小画面的宽为整个画布宽的1/10，右侧小画面的高为整个画布高的1/8</li>
        <li>左侧大画面的宽为整个画布宽的4/5，左侧大画面的高为整个画布高</li>
    </ul></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/2a7532383f74794c9e899c84db9a7002.jpeg"></td>
</tr><tr>
    <th>子画面大于17个时</th>
    <td><ul>
        <li>右（下）侧小画面的宽为整个画布宽的1/10，右（下）侧小画面的高为整个画布高的1/8</li>
        <li>左侧大画面的宽为整个画布宽的4/5，左侧大画面的高为整个画布高的7/8</li>
    </ul></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/8fb008d4cab860eb1362368a397435b9.jpeg"></td>
</table>

- **九宫格布局**：[](id:nine)
根据主播的数量自动调整每个画面的大小，每个主播的画面大小一致，最多支持25个画面。
 九宫格布局随着订阅的子画面增加按照下图进行变化：
<table>
<tr>
    <th width=10%>子画面为1个时</th>
    <td width=40%>每个小画面的宽和高分别为整个画布宽和高</td>
    <td width=40%><img src="https://qcloudimg.tencent-cloud.cn/raw/a6c425c039a85d07a726777ddd3d029f.jpg"></td>
</tr><tr>
    <th>子画面为2个时</th>
    <td><ul style="margin:0">
        <li>每个小画面的宽为整个画布宽的1/2</li>
        <li>每个小画面的高为整个画布高</li>
    </ul></td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/1636c5ec6626372aaba378338cd07e31.jpg"></td>
</tr><tr>
    <th>子画面小于等于4个时</th>
    <td>每个小画面的宽和高分别为整个画布宽和高的 1/2</td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/20821cd34b62a72b70570abcbac3902b.jpeg"></td>
</tr><tr>
    <th>子画面小于等于9个时</th>
    <td>每个小画面的宽和高分别为整个画布宽和高的 1/3</td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/2910f0d051b3bd981bcc7beda8f2971a.jpeg"></td>
</tr><tr>
    <th>子画面小于等于16个时</th>
    <td>每个小画面的宽和高分别为整个画布宽和高的 1/4</td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/110df6cbb92792c9f8f1a07fc245c595.jpeg"></td>
</tr><tr>
    <th>子画面大于16个时</th>
    <td>每个小画面的宽和高分别为整个画布宽和高的1/5</td>
    <td><img src="https://qcloudimg.tencent-cloud.cn/raw/2cfa342c0bdb266b11165fb11f82ac98.jpeg"></td>
</tr></table>

- **自定义布局**：[](id:customize)
根据您的业务需要在 [MixLayoutList](https://cloud.tencent.com/document/api/647/44055#MixLayoutParams) 内自己定制每个主播画面的布局信息。

[](id:MixWatermark)
#### 合流录制的水印参数 (MixWatermark)
我们支持在合流录制中添加图片水印，最大支持个数为25个，可以在画布任意位置添加水印。

| 字段名 | 解释                     |
| ------ | ------------------------ |
| Top    | 水印相对左上角的垂直位移 |
| Left   | 水印相对左上角的水平位移 |
| Width  | 水印显示的宽度           |
| Height | 水印显示的高度           |
| url    | 水印文件的存储 URL        |

[](id:DescribeCloudRecording)
#### 查询录制（[DescribeCloudRecording](https://cloud.tencent.com/document/api/647/44055#StorageFile)）
如果需要，您可以调用该接口查询录制服务的状态。
>! 
>- 只有录制任务存在的时候才能查询到信息，如果录制任务已经结束会返回错误。
>- 如果是上传云点播任务，该接口返回的 StorageFile 为空。

[](id:ModifyCloudRecording)
#### 更新录制（[ModifyCloudRecording](https://cloud.tencent.com/document/api/647/44055#SubscribeStreamUserIds)）
如果需要，您可以调用该接口修改录制服务的参数，如订阅黑白名单 SubscribeStreamUserIds（单流和合流录制有效），录制的模板参数 MixLayoutParams（合流录制有效）。
>! 更新操作是全量覆盖的操作，并不是增量更新的操作，您每次更新都需要携带全量的信息，包括模板参数 MixLayoutParams 和黑白名单 SubscribeStreamUserIds，因此您需要保存之前的启动录制的参数或者重新计算完整的录制相关参数。

[](id:DeleteCloudRecording)
#### 停止录制（[DeleteCloudRecording](https://cloud.tencent.com/document/api/647/73785)）
在录制结束之后需要调用停止录制（DeleteCloudRecording）的接口来结束录制任务，否则录制任务会等待到达预设的超时时间 MaxIdleTime 后自动结束。
>! MaxIdleTime 的定义是房间内持续没有主播的状态超过 MaxIdleTime 的时长，这里如果房间是存在有主播，但是主播没有上行数据是不会进入超时的计时状态的，此时后台录制会持续工作。建议业务在录制结束的时候调用此接口结束录制任务。

[](id:autoRecord)
### 方案二：全局自动录制
要使用该种录制方案，请在 [实时音视频控制台 > 应用管理](https://console.cloud.tencent.com/trtc/app) 中开启云端录制功能，并且选择全局自动录制。
![](https://qcloudimg.tencent-cloud.cn/raw/468ebc6601ac4e52ce2ea7b7094018f9.png)
TRTC 房间中的主播上行音视频后将触发启动录制任务，房间内主播都退房后超过设置的 MaxIdleTime（空闲等待时间，默认5s）将触发停止录制任务。

全局自动录制支持 [单流模式](#single) 和 [合流模式](#mix) 两种录制模式，可以同时选中单流和合流模式进行录制，开启后只对新创建的房间有效，对开启自动录制功能之前已经创建的房间不生效。控制台配置好规则到生效预计需要5min时间。

[](id:single)
#### 全局单流录制
录制格式支持音视频录制、纯音频录制和纯视频录制，纯视频录制请选择音视频录制后勾选移除音频。录制文件支持 MP4 格式，录制 MP4 文件切片策略请参见 [录制 MP4 文件说明](#mp4_file)。
>!
>- 单流录制最多录制一个房间内的25个主播，如果超过25个主播将会按照进房时间由先到后排序，录制前25位主播（如需单流录制超过25位主播，请参见 [API 录制](#API_record)）。
>- 续录等待时间默认为5s, 房间内无主播的时间超过设置的续录时间，将会分成多个录制任务，对应的录制文件也是独立的，房间内无主播的时间未超过续录时间，那么录制任务保持，录制文件不切分。

![](https://qcloudimg.tencent-cloud.cn/raw/e5d0a9648e340ae98954374130f0bcd8.png)

[](id:mix)
#### 全局合流录制
合流录制模式与文件与单流录制一致，您可以通过设置视频转码参数和音频转码参数来控制录制文件输出规格。
全局合流录制支持设置预制的布局模板，具体如下：

- **九宫格模板**：所有用户的视频画面大小一致，平分整个屏幕，人数越多，每个画面的尺寸越小。最多支持8个画面
- **屏幕分享模板**：适合视频会议和在线教育场景的布局，屏幕分享（或者主讲的摄像头）始终占据屏幕左侧的大画面位置，其他用户依次垂直排列于右侧，最多支持1个大画面和7个小画面。
- **悬浮模板**：第一个进入房间的用户的视频画面会铺满整个屏幕，其他用户的视频画面从左下角依次水平排列，显示为小画面，最多4行，每行4个，小画面悬浮于大画面之上。最多支持1个大画面和7个小画面。

其中屏幕分享模板和悬浮模板需要指定大画面用户规则（房间内需要布局成大画面的主播用户 ID 的前缀）：
- 如果房间内主播 ID 未按照前缀匹配到，对应大画面会空出预留布局。
- 如果房间内主播 ID 匹配到多个，按照进房时间最早的主播布局。

![](https://qcloudimg.tencent-cloud.cn/raw/959738437cdfcc4ecd0e14b58f329f25.png)

[](id:interface)
## 回调接口
您可以提供一个接收回调的 HTTP / HTTPS 服务网关来订阅回调消息。当相关事件发生时，云录制系统会回调事件通知到您的消息接收服务器。具体操作请参见 [设置录制回调](https://cloud.tencent.com/document/product/647/52428)。

### 事件回调消息格式
事件回调消息以 HTTP/HTTPS POST 请求发送给您的服务器，其中：
- **字符编码格式**：UTF-8。
- **请求**：body 格式为 JSON。
- **应答**：HTTP STATUS CODE = 200，服务端忽略应答包具体内容，为了协议友好，建议客户应答内容携带 JSON： {"code":0}。

### 参数说明
#### 事件回调消息的 header 中包含以下字段

| 字段名       | 值                 |
| ------------ | ------------------ |
| Content-Type | application/json   |
| Sign         | 签名值             |
| SdkAppId     | sdk application id |

#### 事件回调消息的 body 中包含以下字段：

| 字段名       | 类型        | 含义                                                         |
| ------------ | ----------- | ------------------------------------------------------------ |
| EventGroupId | Number      | 事件组 ID， 云端录制固定为3                                  |
| EventType    | Number      | 回调通知的事件类型                                           |
| CallbackTs   | Number      | 事件回调服务器向您的服务器发出回调请求的 Unix 时间戳，单位为毫秒 |
| EventInfo    | JSON Object | 事件信息                                                     |

#### 事件类型说明

| 字段名                                          | 类型        | 含义                                                   |
| ----------------------------------------------- | ----------- | ------------------------------------------------------ |
| EVENT_TYPE_CLOUD_RECORDING_RECORDER_START       | [301](#301) | 云端录制录制模块启动                                   |
| EVENT_TYPE_CLOUD_RECORDING_RECORDER_STOP        | [302](#302) | 云端录制录制模块退出                                   |
| EVENT_TYPE_CLOUD_RECORDING_FAILOVER             | [306](#306) | 云端录制发生迁移，原有的录制任务被迁移到新负载上时触发 |
| EVENT_TYPE_CLOUD_RECORDING_DOWNLOAD_IMAGE_ERROR | [309](#309) | 云端录制下载解码图片文件发生错误                       |
| EVENT_TYPE_CLOUD_RECORDING_VOD_COMMIT           | [311](#311) | 云端录制 VOD 录制任务上传媒体资源完成                  |
| EVENT_TYPE_CLOUD_RECORDING_VOD_STOP             | [312](#312) | 云端录制 VOD 录制任务结束                              |

>! 录制后台是实时录制 HLS(m3u8+ts) 文件后转码成 MP4 后上传至点播平台的，301-309区间的回调状态为实时录制的中间状态，可以更加清晰的知晓录制任务的进行过程并记录状态，实际录制文件上传到点播成功会回调311事件，整体任务结束回调312事件。

#### 事件信息说明

| 字段名  | 类型          | 含义                                 |
| ------- | ------------- | ------------------------------------ |
| RoomId  | String/Number | 房间名（类型与客户端房间号类型一致） |
| EventTs | Number        | 时间发生的 Unix 时间戳，单位为秒     |
| UserId  | String        | 录制机器人的用户 ID                  |
| TaskId  | String        | 录制ID，一次云端录制任务唯一的 ID    |
| Payload | JsonObject    | 根据不同事件类型定义不同             |

- **事件类型为301**（EVENT_TYPE_CLOUD_RECORDING_RECORDER_START）时 Payload 的定义：[](id:301)
<table>
<thead><tr><th>字段名</th><th>类型</th><th>含义</th></tr></thead>
<tbody><tr>
<td>Status</td>
<td>Number</td>
<td>0：代表录制模块启动成功，1：代表录制模块启动失败。</td>
</tr>
</tbody></table>
```json
{
    "EventGroupId": 3,
    "EventType": 301,
    "CallbackTs": 1622186275913,
    "EventInfo": {
        "RoomId": "xx",
        "EventTs": "1622186275",
        "UserId": "xx",
        "TaskId": "xx",
        "Payload": {
            "Status": 0
        }
    }
}
```
- **事件类型为302**（EVENT_TYPE_CLOUD_RECORDING_RECORDER_STOP）时 Payload 的定义：[](id:302)
<table>
<thead>
<tr>
<th>字段名</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>LeaveCode</td>
<td>Number</td>
<td>0：代表录制模块正常调用停止录制退出
  <br>1：录制机器人被客户踢出房间
  <br>2：客户解散房间
  <br>3：服务器将录制机器人踢出
  <br>4：服务器解散房间
  <br>99：代表房间内除了录制机器人没有其他用户流，超过指定时间退出
  <br>100：房间超时退出
  <br>101：同一用户重复进入相同房间导致机器人退出
</td>
</tr>
</tbody></table>
```json
{
  "EventGroupId": 3,
  "EventType": 302,
  "CallbackTs": 1622186354806,
  "EventInfo": {
    "RoomId": "xx",
    "EventTs": "1622186354",
    "UserId": "xx",
    "TaskId": "xx",
    "Payload": {
      "LeaveCode": 0
    }
  }
}
```
- **事件类型为306**（EVENT_TYPE_CLOUD_RECORDING_FAILOVER）时 Payload 的定义：[](id:306)
<table>
<thead>
<tr>
<th>字段名</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>Status</td>
<td>Number</td>
<td>0：代表此次迁移已经完成</td>
</tr>
</tbody></table>
```json
{
  "EventGroupId": 3,
  "EventType": 306,
  "CallbackTs": 1622191989674,
  "EventInfo": {
    "RoomId": "20015",
    "EventTs": 1622191989,
    "UserId": "xx",
    "TaskId": "xx",
    "Payload": {
      "Status": 0
    }
  }
}
```
- **事件类型为309**（EVENT_TYPE_CLOUD_RECORDING_DOWNLOAD_IMAGE_ERROR）时 Payload 的定义：[](id:309)
<table>
<thead>
<tr>
<th>字段名</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>Url</td>
<td>String</td>
<td>下载失败的 URL</td>
</tr>
</tbody></table>
```json
{
  "EventGroupId": 3,
  "EventType": 309,
  "CallbackTs": 1622191989674,
  "EventInfo": {
    "RoomId": "20015",
    "EventTs": 1622191989,
    "UserId": "xx",
    "TaskId": "xx",
    "Payload": {
      "Url": "http://xx",
    }
  }
}
```
- **事件类型为311**（EVENT_TYPE_CLOUD_RECORDING_VOD_COMMIT）时 Payload 的定义：[](id:311)
<table>
<thead>
<tr>
<th>字段名</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>Status</td>
<td>Number</td>
<td>0：代表本录制文件正常上传至点播平台<br>1：代表本录制文件滞留在服务器或者备份存储上<br>2：代表本录制文件上传点播任务异常</td>
</tr>
<tr>
<td>UserId</td>
<td>String</td>
<td>本录制文件对应的用户 ID（当录制模式为合流模式时，此字段为空）</td>
</tr>
<tr>
<td>TrackType</td>
<td>String</td>
<td>audio/video/audio_video</td>
</tr>
<tr>
<td>MediaId</td>
<td>String</td>
<td>main/aux（main 代表主流，aux 代表辅流）</td>
</tr>
<tr>
<td>FileId</td>
<td>String</td>
<td>本录制文件在点播平台的唯一id</td>
</tr>
<tr>
<td>VideoUrl</td>
<td>String</td>
<td>本录制文件在点播平台的播放地址</td>
</tr>
<tr>
<td>CacheFile</td>
<td>String</td>
<td>本录制文件对应的 MP4 文件名</td>
</tr>
<tr>
<td>StartTimeStamp</td>
<td>Number</td>
<td>本录制文件开始的 UNIX 时间戳（毫秒)</td>
</tr>
<tr>
<td>EndTimeStamp</td>
<td>Number</td>
<td>本录制文件结束的 UNIX 时间戳（毫秒)</td>
</tr>
<tr>
<td>Errmsg</td>
<td>String</td>
<td>statue 不为0时，对应的错误信息</td>
</tr>
</tbody></table>
上传成功的回调：
```json
{
  "EventGroupId": 3,
  "EventType": 311,
  "CallbackTs": 1622191965320,
  "EventInfo": {
    "RoomId": "20015",
    "EventTs": 1622191965,
    "UserId": "xx",
    "TaskId": "xx",
    "Payload": {
      "Status": 0,
      "TencentVod": {
        "UserId": "xx",
        "TrackType": "audio_video",
        "MediaId": "main",
        "FileId": "xxxx",
        "VideoUrl": "http://xxxx",
        "CacheFile": "xxxx.mp4",
        "StartTimeStamp": xxxx,
        "EndTimeStamp": xxxx
      }
    }
  }
}
```
上传失败的回调：
```json
{
  "EventGroupId": 3,
  "EventType": 311,
  "CallbackTs": 1622191965320,
  "EventInfo": {
    "RoomId": "20015",
    "EventTs": 1622191965,
    "UserId": "xx",
    "TaskId": "xx",
    "Payload": {
      "Status": 1,
      "Errmsg": "xxx",
      "TencentVod": {
        "UserId": "123",
        "TrackType": "audio_video",
        "CacheFile": "xxx.mp4"
      }
    }
  }
}
```
- **事件类型为312**（EVENT_TYPE_CLOUD_RECORDING_VOD_STOP）时 Payload 的定义：[](id:312)
<table>
<thead>
<tr>
<th>字段名</th>
<th>类型</th>
<th>含义</th>
</tr>
</thead>
<tbody><tr>
<td>Status</td>
<td>Number</td>
<td>0：代表本次上传 VOD 任务已经正常退出<br>1：代表本次上传 VOD 任务异常退出</td>
</tr>
</tbody></table>
```json
{
  "EventGroupId": 3,
  "EventType": 312,
  "CallbackTs": 1622191965320,
  "EventInfo": {
    "RoomId": "20015",
    "EventTs": 1622191965,
    "UserId": "xx",
    "TaskId": "xx",
    "Payload": {
      "Status": 0
    }
  }
}
```

## 最佳实践
为了保障录制的高可用，建议客户在集成 REST ful API 的同时注意以下几点。
- 调用 CreateCloudRecording 请求后，请关注 HTTP response，如果请求失败，那么需要根据具体的状态码采取相应的重试策略。错误码是由“一级错误码”和“二级错误码”组合而成，例如：`InvalidParameter.SdkAppId`。
   - 如果返回的 Code 是 `InValidParameter.xxxxx`，说明输入的参数有误，请根据提示检查参数。
   - 如果返回的 Code 是 `InternalError.xxxxx`，说明遇到了服务端错误，可以使用相同的参数重试多次，直到返回正常，拿到 taskid 为止。建议使用退避重试策略，如第一次3s重试，第二次6s重试，第三次12s重试，以此类推。
   - 如果返回的 Code 是 `FailedOperation.RestrictedConcurrency`，说明客户的并发录制任务数，超过了后台预留的资源（默认是100路），请联系腾讯云技术支持来调整最高并发路数限制。

- 如果您有订阅录制回调，当收到 EVENT_TYPE_CLOUD_RECORDING_RECORDER_STOP 回调事件，LeaveCode 为100时，说明录制与主播数据长时间断开连接，请再次发起录制任务保证录制的可用性。

- 调用 CreateCloudRecording 接口时，指定的 UserId/UserSig 是录制作为单独的机器人用户加入房间的 ID，请不要和 TRTC 房间内的其他用户重复。同时，TRTC 客户端加入的房间类型必须和录制接口指定的房间类型保持一致，比如 SDK 创建房间用的是字符串房间号，那么云端录制的房间类型也需要相应设置成字符串房间号。

- 录制状态查询，客户可以通过以下几种方式来得到录制相应的文件信息：
   - 成功发起 CreateCloudRecording 任务后15s左右，调用 DescribeCloudRecording 接口查询录制文件对应的信息，如果查询到状态为 idle 说明录制没有拉到上行的音视频流，请检查房间内是否有主播上行。
   - 成功发起 CreateCloudRecording 后，在确保房间有上行音视频的情况下，可以按照录制文件名的生成规则来拼接录制文件名称。具体文件名规则请参见 [录制文件名命名规则](#rude)。
   - 录制文件的状态会通过回调发送到客户的服务器，如果订阅了相关回调，将会收到录制文件的状态信息。具体回调信息请参见 [回调接口](#interface)。

- 录制用户（userid）的 UserSig 过期时间应该设置成比录制任务生命周期更长的时间，防止录制任务机器断网，在内部高可用生效的时候，恢复录制因为 UserSig 过期而失败。

