
## 功能介绍
一条直播流的状态变化、一个新录制文件的生成、一张新截图文件的生成，这类事件都在腾讯云内部管理，但您的后台服务器可能也同样有获知的需求，这时您可以使用腾讯云的事件通知服务获知这些事件。

您可以在控制台注册一个来自您后台服务器的回调URL给腾讯云，当有事件发生时，腾讯云会通过HTTP POST的方式将新的事件投递给您的服务器，事件内容以 JSON 格式组织。

## 配置URL
在[直播控制台>>直播码接入>>接入配置](https://console.cloud.tencent.com/live/livecodemanage) 开启直播码模式时，可以指定一个接收腾讯云通知的URL，如下图：

![](//mc.qcloudimg.com/static/img/b1df74884171a920e37940a17d2edac2/image.png)

## 消息组织格式
通知信息是以 JSON 格式进行组织的，然后放在 HTTP POST 协议体中，注意这里的 POST 格式的 ContentType 是 application/json，而不是 multipart/form-data，所以<font color='red'>不要使用 PHP 或者 Java 里读取表单字段的函数</font>来读取信息。

## 公共的头信息
如下的字段是每种类型的通知消息都一定会携带的：

| 字段名称 | 类型 | 含义 | 备注 | 
|------------|-------------|---------|---------|
| t           | string      | 有效时间  |UNIX时间戳(十进制) |
| sign      | string     | 安全签名  | MD5(KEY+t) |
| event_type | int     | 事件类型   | 目前可能值为： 0、1、100、200  |
| stream_id | string     | 直播码   |  标示事件源于哪一条直播流  |
| channel_id | string     | 直播码  | 同stream_id   |

- **stream_id | channel_id（直播码）**
 在直播码模式下，stream_id 和 channel_id 两个字段都是同一个值，有两个不同的名字主要是历史原因所致。

- **t（过期时间）**
  来自腾讯云的消息通知的默认过期时间是10分钟，如果一条通知消息中的 t 值所指定的时间已经过期，则可以判定这条通知无效，进而可以防止网络重放攻击。t 的格式为十进制UNIX时间戳，即从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。

- **sign（安全签名）**
  <font color='blue'>sign = MD5(key + t) </font>：腾讯云把加密key 和 t 进行字符串拼接后，通过MD5计算得出sign值，并将其放在通知消息里，您的后台服务器在收到通知消息后可以根据同样的算法确认sign是否正确，进而确认消息是否确实来自腾讯云后台。
	
	这里的加密key即CGI调用key，您在腾讯云直播管理控制台开通直播码服务时可以指定，如下图所示：
![](//mc.qcloudimg.com/static/img/28a16dbab36fc3867301d2311204b8e4/image.png)

- **event_type（通知类型）**
  目前腾讯云支持三种消息类型的通知：0 — 断流； 1 — 推流；100 — 新的录制文件已生成；200 — 新的截图文件已生成。
	
## 各类型消息体
### (1)推流 (0)断流
**event_type = 0** 代表断流，**event_type = 1** 代表推流，同时消息体会额外包含如下信息： 

| 字段名称  |含义 |   类型        | 备注    |是否必须|
|-------------|-------------|--------------|-------------|--------------|
| appname | 推流路径   | string  ||Y|
| app         | 推流域名   | string  ||Y|
|update_time|消息产生的时间|int|单位s|Y|
|sequence|消息序列号，标识一次推流活动，一次推流活动会产生相同序列号的推流和断流消息|string||Y|
|node	|Upload接入点的ip	|String||	Y|
|user_ip	|用户推流ip|	String	|Client_ip	|Y|
|errcode	|断流错误码	|Int	|	|N|
|errmsg	|断流错误信息	|String	|	|N|
|stream_param	|推流url参数|	String	|	|Y|
|push_duration|	推流时长|	String	|单位ms	|N|


示例：腾讯云通知直播流（1234_15919131751）发生断流（event_type=0）事件。

```json
{
    "app": "3954.livepush.myqcloud.com", 
    "appname": "live",
    "channel_id": "16093425727656502238",
    "event_type": 0,
    "sign": "ab86d22870427e3f25bb1d9446b8f924", 
    "stream_id": "3954_ea88f7495ba711e6a2cba4dcbef5e35a", 
    "t": 1471256100,
    "event_time": 1471256200,
    "sequence": "5911795891871911817",
    "node":"123.10.1.1",
    "user_ip":"127.0.0.1",
    "errcode":0,
    "errmsg":"OK",
    "stream_param":""
}
```

#### 推流断流错误码
| 错误码 | 错误描述 | 错误原因 |
|---------|---------|---------|
|1|	recv rtmp deleteStream|	主播端主动断流|
|2|	recv rtmp closeStream	|主播端主动断流|
|3|	recv() return 0	|主播端主动断开TCP连接|
|4	|recv() return error	|主播端TCP连接异常|
|7|	rtmp message large than 1M |	收到流数据异常|
|18	|push url maybe invalid	|推流鉴权失败，服务端禁止推流
|19	|3rdparty auth failed	|第三方鉴权失败，服务端禁止推流|
|其他错误码|直播服务内部异常| 如需处理请联系腾讯商务人员或者提交工单，联系电话：4009-100-100 |


### (100)新录制文件
**event_type = 100** 代表有新的录制文件生成，同时消息体会额外包含如下信息：

| 字段名称  | 含义        |   类型      |备注|是否必须|
|------------  |-------------|-------------|-------------|-------------|
| video_id  |vid | string      | 点播用vid，在点播平台可以唯一定位一个点播视频文件  |Y|
| video_url  |下载地址| string      | 点播视频的下载地址  | Y|
| file_size  |文件大小 | string       |  | Y|
| start_time |分片开始时间戳 | int      | 开始时间（unix时间戳，由于I帧干扰，暂时不能精确到秒级）  |Y|
| end_time |分片结束时间戳 | int       | 结束时间（unix时间戳，由于I帧干扰，暂时不能精确到秒级）  |Y|
|file_id|file_id	|string||	Y|
|file_format	|文件格式	|string|	flv, hls, mp4	|Y|
|vod2Flag	|是否开启点播2.0	|Int	|0表示未开启，1表示开启|	N|
|record_file_id	|录制文件id|	String|	点播2.0开启时，才会有这个字段|	N|
|duration	|推流时长	|Int	|	|Y|
|stream_param|	推流url参数|	string|		|Y|

示例：一个id为9192487266581821586的新的flv录制分片已经生成，播放地址为：'http://200025724.vod.myqcloud.com/200025724_ac92b781a22c4a3e937c9e61c2624af7.f0.flv'。
```json
{
    "channel_id": "3891_@v_tls#3pfnm5fw35qt", 
    "end_time": 1471256054, 
    "event_type": 100, 
    "file_format": "flv", 
    "file_id": "16093425727657168197", 
    "file_size": 130938971, 
    "sign": "5c5e614ab58efc5a7ed6894dae22f471", 
    "start_time": 1471254513, 
    "stream_id": "3891_@v_tls#3pfnm5fw35qt", 
    "t": 1471256688, 
    "video_id": "200024424_a62017f6489748df9ee439360a8cc32c", 
    "video_url": "http://200024424.vod.myqcloud.com/200024424_a62017f6489748df9ee439360a8cc32c.f0.flv"
}
```

### (200)新截图文件 
**event_type = 200** 代表有新的截图图片生成，同时消息体会额外包含如下信息：

| 字段名称  | 含义        |   类型      |备注|是否必须|
|-------------------|-------------|---------|-------------|-------------|
| pic_url        |图片地址   | string      | 不带域名的路径 |Y|
| create_time  |截图时间戳 | int           |截图时间戳（unix时间戳，由于I帧干扰，暂时不能精确到秒级） |Y|
|pic_full_url|	截图全路径|	String|	需要带上域名	|Y|

示例：直播流“2016090090936”在腾讯云生成了一张新的截图图片：

```json
{
    "channel_id": "2016090090936", 
    "create_time": 1473645788, 
    "event_type": 200, 
    "pic_url": "/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg", //文件路径名
    "sign": "8704a0297ab7fdd0d8d94f8cc285cbb7", 
    "stream_id": "2016090090936", 
    "t": 1473646392
}
```

>**图片下载地址**
>
> 1.由于历史原因，以前开启截图功能需要您自己申请cos服务，我们给您返回的pic_url 不是真正的图片下载地址只是下载路径，真正的下载地址是需要拼接的，拼接方法是：
> - 下载前缀：`http://(cos_bucketname)-(cos_appid).file.myqcloud.com/`
> - 下载路径：`/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg`
> - 完整URL：`http://(cos_bucketname)-(cos_appid).file.myqcloud.com/2016-09-12/2016090090936-screenshot-10-03-08-1280x720.jpg`
> 
> **其中 cos_appid 和 cos_bucketname 是您在腾讯云开通[对象存储服务](https://console.cloud.tencent.com/cos)。以前您需要自己开通cos服务并将其绑定到直播截图服务后才能使用截图功能。当前该方式已经不适用了，现在无需您自己申请cos服务。目前开通截图功能的方式有两种：1.控制台上开启截图功能；2.联系我们配置相关信息后再调用接>口开启截图功能。**
>
> 2.现在您无需自己开通cos服务，我们能够将完整的截图URL地址回调给您。
>  回调新增一个完整图片URL字段：pic_full_url，以便您直接得到完整的图片URL。为了不影响原有业务，原有回调信息字段均无变化（即pic_url字段依旧存在）。
 
## 通知可靠性
很多客户会担心消息丢了怎么办，比如客户的服务器宕机了一下会儿，消息会不会丢失呢？
腾讯云后台目前的消息可靠性保证机制是基于**简单重传**实现的，即：<font color='blue'>如果一条通知消息没有成功发送到您指定的回调URL，腾讯云会反复重试3次。每次重试的时间间隔是 3 秒。</font> 

那怎么确认消息是已经送达您的服务器了呢？这里是需要您的协助的：<font color='red'>当您的服务器成功收到一条http事件通知消息时，请回复：</font> 

```json
// 在收到消息通知的http请求里返回错误码 0 以代表您已经成功收到了消息，从而避免腾讯云反复重复通知
{ "code":0 }
```

代表：“嗯，我（客户服务器）已经你的通知了，请（腾讯云）不要再不断地发消息给我”。



