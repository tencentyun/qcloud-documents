
## 音视频传输
### 直播标清、高清、超清对应参数
**ipc 参数 channel 为0，nvr 参数 channel 为查询nvr 子设备返回的结果**
- ipc.flv?action=live&channel=xxx&quality=standard
- ipc.flv?action=live&channel=xxx&quality=high
- ipc.flv?action=live&channel=xxx&quality=super

### 点播参数
- ipc.flv?action=playback&channel=xxx&start_time=xxx&end_time=yyy
- 参数说明：start_time 和 end_time 秒为单位，差值不得小于5s，UNIX 时间戳。

### 对向音频
- voice?channel=xxx

## 内部信令
### 查询nvr设备 子设备
**返回 channel+devicename**
- action=inner_define&cmd=get_nvr_list

返回的 json 结构：
```json
[
    {"DeviceName":"name1",
    "Channel":"1",
    "Online":"0"
},
  {"DeviceName":"name2",
    "Channel":"2",
    "Online":"1"
}
]
```

### 获取 ipc/nvr 设备状态，是否可以推流
**type 参数区分直播和对讲**
- 	action=inner_define&channel=xxx&cmd=get_device_st&type=(voice/live)&quality=standard
返回的json结构：

```json
[ {"status":"code"，
    "appConnectNum":"2"
}]
```

code 的取值：

|取值	|含义|
|--|--|
|0|	接收请求|
|1	|拒绝请求|
|404	|错误请求|
|405	|连接 APP 数量超过最大连接数|
|406	|信令不支持|

app_connect_num：已连接到设备的 APP 数量；

### 测试信令
**是否保留**
-	action=user_define&channel=xxx&cmd=custom_cmd

### 拉取本地录像列表
#### 按时间查询
-	action=inner_define&channel=xxx&cmd=get_record_index&start_time=000&end_time=111
-	参数说明：start_time 和 end_time 秒为单位，差值不得小于5s，UNIX时间戳。

设备返回值：
```json
{ "video_list": [{
			"start_time":	"<unix时间戳>",
			"end_time":	"<unix时间戳>"
		}, {
			"start_time":	"<unix时间戳>",
			"end_time":	"<unix时间戳>"
		}]
}
```

>? "file_name" 字段用途不明晰，可以暂不处理。
>
#### 按月查询
-	action=inner_define&channel=xxx&cmd=get_month_record&time=yyyymm
-	参数说明:yyyymm 中前四位是年份，后两位是月份；
设备返回值：
```JSON
{"video_list"："xxxx"}
```

xxxx：表示32位的数字，从低位到高位每一比特代表月份的第几天是否有录像；例如：8320（0010000010000000）表示8号和14号有录像；

#### 暂停回放
-	action=inner_define&channel=xxx&cmd=playback_pause
设备返回值：
返回的 json 结构：
```JSON
 {"status":"code"}
```

#### 继续回放
-	action=inner_define&channel=xxx&cmd=playback_resume
设备返回值：
返回的 json 结构：
```JSON
{"status":"code"}
```

#### 录像进度条滑动
-	action=inner_define&channel=xxx&cmd=playback_seek&time=ssss
-	参数说明:ssss 是 UNIX 时间戳,单位s；
设备返回值：
返回的 json 结构：
```JSON
{"status":"code"}
```

#### 设置快进速度（是否支持待定)
-	action=inner_define&channel=xxx&cmd=playback_ff&speed=value
-	参数说明:value 是大于0的整数，代表快进速度，即跳帧的间隔，1表示只发送I帧，2表示两个I帧中取一个发送。
设备返回值：
返回的 json 结构：
```JSON
{"status":"code"}
```

#### 设置快放or慢放速度（是否支持待定）
-	action=inner_define&channel=xxx&cmd=playback_speed&speed=value
-	参数说明:value 是一个正整数，单位毫秒，代表 PTS 的间隔，当 value 大于正常 pts 是慢放，否则是快放；
设备返回值：
返回的 json 结构：
```JSON
{"status":"code"}
```

#### 设置设置快退（是否支持待定）
-	action=inner_define&channel=xxx&cmd=playback_rewind&start_time=000&end_time=111
-	参数说明:start_time 表示快退的截止时间，end_time 表示快退的开始时间；
设备返回值：
返回的 json 结构：
```JSON
{"status":"code"}
```

## 外部信令

### 云台控制信令格式
-	action=user_define&channel=xxx&cmd=ptz_left
-	action=user_define&channel=xxx&cmd=ptz_right
-	action=user_define&channel=xxx&cmd=ptz_up
-	action=user_define&channel=xxx&cmd=ptz_down





