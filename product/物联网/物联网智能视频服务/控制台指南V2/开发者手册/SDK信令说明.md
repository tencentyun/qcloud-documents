

## 音视频传输

### 直播标清、高清、超清对应参数（ipc 参数 channel 为0，nvr 参数 channel 为查询 nvr 子设备返回的结果）

```
ipc.flv?action=live&channel=xxx&quality=standard

ipc.flv?action=live&channel=xxx&quality=high

ipc.flv?action=live&channel=xxx&quality=super
```

### 点播参数

```
ipc.flv?action=playback&channel=xxx&start_time=xxx&end_time=yyy
```

参数说明：start_time 和 end_time 秒为单位，差值不得小于5s，UNIX 时间戳

## 对向音频

```
voice?channel=xxx
```

### 文件下载

```
ipc.flv?action=download&channel=0&file_name=xxx&offset=yyy
```

| 参数      | 含义                     | 等级 |
| --------- | ------------------------ | ---- |
| file_name | 需要下载的文件名，字符串 | 必选 |
| offset    | 下载的文件起始偏移，整型 | 必选 |

## 内部信令

### 查询 nvr 设备子设备：（返回 channel+devicename）

```
action=inner_define&cmd=get_nvr_list
```

返回的 json 结构：

```
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

### 获取 ipc/nvr 设备状态，是否可以推流（type 参数区分直播和对讲）

#### 获取 ipc 设备状态

判断是否可以请求视频流(type 区分直播(live)和对讲(voice)):

```
action=inner_define&channel=0&cmd=get_device_st&type=(voice/live)&quality=standard
```

参数说明：appConnectNum 表示：已连接到设备的 APP 数量。

返回的 json 结构：

```
[{"status":"code"，"appConnectNum":"2"}]
```

| 取值 | 含义                        |
| ---- | --------------------------- |
| 0    | 接收请求                    |
| 1    | 拒绝请求                    |
| 404  | 错误请求                    |
| 405  | 连接 APP 数量超过最大连接数 |
| 406  | 信令不支持                  |

app_connect_num：已连接到设备的 APP 数量；



### 拉取本地录像列表

#### 按时间查询

```
action=inner_define&channel=xxx&cmd=get_record_index&start_time=000&end_time=111&type=0

```

参数说明：start_time 和 end_time 秒为单位，差值不得小于5s，UNIX时间戳，type表示录像的类型，是一个整数，由用户自己定义具体含义

设备返回值：

```
{	"video_list":	[{
			"type":xx,
			"start_time":	"<unix时间戳>",
			"end_time":	"<unix时间戳>"
}, {
			"type":xx,
			"start_time":	"<unix时间戳>",
			"end_time":	"<unix时间戳>"
		}]
}

```

说明："file_name"字段用途不明晰，可以暂不处理

#### 按月查询

```
action=inner_define&channel=xxx&cmd=get_month_record&time=yyyymm

```

参数说明:yyyymm中前四位是年份，后两位是月份；

设备返回值：

```
{"video_list"："xxxx"}

```

xxxx：表示32位的数字，从低位到高位每一比特代表月份的第几天是否有录像；例如：8320（0010000010000000）表示8号和14号有录像；

#### 暂停回放

```
action=inner_define&channel=xxx&cmd=playback_pause

```

设备返回值：

返回的 json 结构：

```
 {"status":"code"}

```

#### 继续回放

```
action=inner_define&channel=xxx&cmd=playback_resume

```

设备返回值：

返回的 json 结构：

```
{"status":"code"}

```

#### 录像进度条滑动

```
action=inner_define&channel=xxx&cmd=playback_seek&progress=ms
```

参数说明:ms 是当前文件相对时间戳,单位ms；

设备返回值：

返回的 json 结构：

```
{"status":"code"}
```

#### 获取播放进度

```
action=inner_define&channel=xxx&cmd=playback_progress
```

参数说明:相对当前录像开始的时间，单位毫秒，可由帧数*帧率计算；

设备返回值：

返回的 json 结构：

```
 {"status":"code","progress":”<相对时间>“}
```



## 外部信令

### 云台控制信令格式

```
action=user_define&channel=xxx&cmd=ptz_left

action=user_define&channel=xxx&cmd=ptz_right

action=user_define&channel=xxx&cmd=ptz_up

action=user_define&channel=xxx&cmd=ptz_down
```
