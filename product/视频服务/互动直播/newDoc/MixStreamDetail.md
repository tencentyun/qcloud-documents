


# 混流

## 什么是混流
所谓混流是指将多路视频流混合成为新的视频流(可以替换原视频流)

![](https://mc.qcloudimg.com/static/img/20dcad307192885fca4fd604b1fafad0/t610.png)

### 如何混流
对于在使用腾讯视频云业务(包括直播、互动直播)的用户，都可以通过[接口](https://www.qcloud.com/document/product/267/8832)实现在云端混流

### 流ID
混流的基础为视频流，对互动直播来说，直播码就是视频流id。

在自动开启旁路直播的情况下，房间内所有视频(主播及上麦观众)都会产生对应的直播视频流。
```
直播码=[BIZID]_MD5(房间号_用户名_数据类型)

摄像头数据类型是main
屏幕分享的数据类型是aux

播放地址=传输协议://BIZID.liveplay.myqcloud.com/live/直播码[.格式]
```
详见[直播码模式下旁路直播](https://www.qcloud.com/document/product/268/8560)

### 混流接口
混流接口实际是一个基于HTTP协议的Post请求

#### 请求地址
```
服务器地址: http://fcgi.video.qcloud.com/common_access
```

#### URL参数

参数|参数含义|类型|备注|是否必填
--:|:--:|:--:|:--:|:--:
appid|客户ID|int|填写直播APPID(不是sdkappid)，用于区分不同客户的身份|Y
interface|接口名称|string|混流接口名称固定填写：Mix_Stream|Y
t|有效时间|int|UNIX时间戳，即从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数；这个字段表示的是请求过期时间，请您在获取当前时间（秒）的基础上加60秒偏移|Y
sign|安全签名|string|sign = MD5(key + t) ，即把加密key 和 t 进行字符串拼接后，计算一下md5值。这里的key是您在腾讯云直播管理控制台中设置的API鉴权key|Y

#### Post内容

Post内部为Json格式的混流参数,详见[接口](https://www.qcloud.com/document/product/267/8832)

其中比较重要参数：

参数|参数含义|类型|备注|是否必填
--:|:--:|:--:|:--:|:--:
output_stream_id|混流输出流ID|string|指定输出流ID|Y
output_stream_type|混流输出流类型|int|指定输出流类型。当输出流为输入流list中的一条时，填写0；当输出流为一条新的流，并非输入流list中的流时，该值为1。不填默认为0。|N
mix_stream_template_id|混流模版|int|输入模版ID。目前两输入源支持10、20、30、40；三输入源支持310、390、391；四输入源支持410；五输入源支持510、590；六输入源支持610。不填默认为0。|N

#### 混流配置示例
##### 将两路视频混合成一路新的视频
新视频的流id为自已指定的直播码，要求是不超过100字节的字符串，且不跟已经分配过直播冲突。

这里为了规范以及避免与其它用户冲突，定义格式如下：
```
[BIZID]_MIX_[底流id]_[混流数量]_[时间戳]
```
说明:
- BIZID: 业务id(可以腾讯云后台[直播管理](https://console.qcloud.com/live/livecodemanage)查看)
- MIX: 固定前缀，表明该流为混流产生
- 底流id: 作为混流底流(背景主流)的流id(如果超过80字节，取前80字节)
- 混流数量: 若该视频流为两路视频流混合产生则为2，以此类推
- 时间戳: 1970年1月1日以来的秒数
```
将A和B混成新一路流C
output_stream_id  C
output_stream_type 1
```
##### 将两路视频混合后替换原视频
```
将A和B混成流替换A
output_stream_id  A
output_stream_type 0
```
