腾讯云的云端混流技术，在于将一个或者多个（目前暂时支持到1+3）小主播的视频画面叠加到大主播的视频流上（包括音频混音），基于这种方案，您可以让普通观众在不改造播放器的情况下就能观看连麦直播。


## 使用方法
### 1. 腾讯云混流 API 地址

```
http://fcgi.video.qcloud.com/common_access
```

### 2. 通过 GET 方式传递鉴权参数

```
http://fcgi.video.qcloud.com/common_access?cmd=appid&interface=Mix_StreamV2&t=t&sign=sign
```

- **cmd**：填写直播APPID，用于区分不同客户的身份
- **interface**：固定填写Mix_StreamV2
- **t（过期时间）**：UNIX时间戳，即从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数；这个字段表示的是请求过期时间，请您在获取当前时间（秒）的基础上加60秒偏移
- **sign（安全签名）**： sign = MD5(key + t) ，即把加密key 和 t 进行字符串拼接后，计算一下md5值。这里的key是您在腾讯云直播管理[控制台](https://console.cloud.tencent.com/live/livecodemanage)中设置的API鉴权key

举例说明安全签名**sign**的计算方法 

```
key = "40328529ca4381a80c6ecf2e6aa57438"                    //API鉴权key 
t = 1490858347                                              //t 过期时间
key + t = "40328529ca4381a80c6ecf2e6aa574381490858347"      //key 和 t 进行字符串拼接
sign = MD5（key + t） = "7f29ed83c61b77de1b0d66936fd4fd44"   //对拼接后的字符串计算MD5
```


### 3. 通过POST方式传递混流参数

混流参数是json格式的字符串，用来指定对哪些视频流进行混流操作以及混流的方式，下面举例说明

```
{
    "timestamp":int(time.time()),           # UNIX时间戳，即从1970年1月1日开始所经过的秒数
    "eventId":int(time.time()),             # 混流事件ID，取时间戳即可，后台使用
    "interface":
    {
        "interfaceName":"Mix_StreamV2",	     # 照此填写即可
        "para":
        {
            "app_id": appid,                   # 填写直播APPID
            "interface": "mix_streamv2.start_mix_stream_advanced",  # 照此填写即可
            "mix_stream_session_id" : "8888_denny",                # 填大主播的流ID
            "output_stream_id": "8888_denny",                      # 填大主播的流ID
            "input_stream_list":
            [
                # 大主播：背景画面
                {
                    "input_stream_id":"8888_denny",    # 流ID
                    "layout_params":
                    {   
                        "image_layer": 1                # 图层标识号：大画面填 1, 小画面依次填写2、3、4
                    }   
                },
                # 小主播1
                {
                    "input_stream_id":"8888_rex",    # 流ID
                    "layout_params":
                    {   
                        "image_layer": 2,              # 图层标识号：大画面填 1, 小画面依次填写2、3、4
                        "image_width": 160,            # 小主播画面宽度
                        "image_height": 240,           # 小主播画面高度
                        "location_x": 380,             # x偏移：相对于大主播背景画面左上角的横向偏移
                        "location_y": 630              # y偏移：相对于大主播背景画面左上角的纵向偏移
                    }   
                 },
                # 小主播2
                 {
                     "input_stream_id":"8888_link",
                     "layout_params":
                     {
                         "image_layer": 3,
                         "image_width": 160,
                         "image_height": 240,
                         "location_x": 380,
                         "location_y": 390
                     }
                 },
                # 小主播3
                 {
                     "input_stream_id":"8888_shock",
                     "layout_params":
                     {
                         "image_layer": 4,
                         "image_width": 160,
                         "image_height": 240,
                         "location_x": 380,
                         "location_y": 150
                     }
                 }
            ]
        }
    }
}
```


详细解释一下混流参数：

- 上面混流参数里，以#开始的内容是python格式的注释；

- 字段timestamp和eventId都取当前时间（秒）即可；

- 字段mix_stream_session_id和output_stream_id都填大主播的流ID；

- 字段input_stream_list是一个数组，包含了需要混流的视频流信息；这个数组里必须包含大主播的视频流，但视频流的数目不能超过4路，因为混流后台目前最多支持4路混流；

- 字段layout_params用于设置视频流排布参数；大主播的画面默认铺满整个屏幕，只需要将字段image_layer填写为1，不需要填写其它字段；image_layer是图层标识号，小主播请按照顺序，依次填写2、3或者4；

- 字段image_width、 image_height、 location_x、 location_y用来定义小画面相对于大画面的位置；需要注意的是，小画面的上、下、左、右四个位置都不能超过大画面的范围，即：location_x不能小于0，不能超过大画面的宽度；

- location_y不能小于0，不能超过大画面的高度； location_x + image_width之和不能超过大画面的宽度；location_y + image_height之和不能超过大画面的高度；


### 4. 腾讯云回应调用结果

```
{"code":0, "message":"Success!", "timestamp":1490079362}
```


- **code**: 错误码，0表示成功，其它表示失败
- **message**:错误描述信息
- **timestamp**:时间戳，取值与混流参数里的timestamp相同

## 注意事项
- 混流CGI没有显式区分启动混流和结束混流，“是否需要混流”以及“把几路流混在一起”是由混流参数input_stream_list数组里视频流的数目决定的；如果视频流的数目大于1，就会启动混流；如果只有大主播一条视频流，就会结束混流；

- 鉴权参数建议在您App的后台服务端生成，因为基于保密性的考虑，API鉴权KEY不能放在前端App；混流参数建议您在大主播端生成，因为“有没有连麦（是否需要启动混流）”以及“有哪些小主播加入连麦（要对哪些视频流做混流操作）”，只有大主播最为清楚；混流CGI请求可以在后台服务端发起（需要把混流参数发送给后台，请后台代为发送混流请求），也可以在大主播端发起（需要向后台请求鉴权参数）；

- 启动混流之前必须确认大、小主播都已经推流成功了，也即必须在收到推流成功事件PUSH_EVT_PUSH_BEGIN之后调用混流CGI；否则会失败，CGI回包里code字段非0；

- 如果确认是在收到PUSH_EVT_PUSH_BEGIN事件之后调用的混流CGI，却仍然返回失败；这种情况下，可以采取重试策略，建议每2秒重试一次，最多重试5次；出现这种情况，是因为PUSH_EVT_PUSH_BEGIN事件，只是表示SDK成功地把第一个视频关键帧发送给服务器了，视频云后台流状态同步会有滞后。
