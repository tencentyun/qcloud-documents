## 基于信令进行双向交互

### 信令使用场景

应用端需要向 ipc 设备发送控制(镜头移动等)、查询(录像列表等)、查询设备状态是否可响应直播、获取 ip 设备信息 等需求可以使用信令来完成



#### ipc 设备
**点播参数**
`ipc.flv?action=playback&channel=xxx&start_time=xxx&end_time=yyy`
参数说明：start_time 和 end_time 秒为单位，差值不得小于5s，UNIX 时间戳

##### 设备查询

channel 固定为0

##### 查询设备本地录像列表

###### 按时间查询 

`action=inner_define&channel=0&cmd=get_record_index&start_time=000&end_time=111`
参数说明：start_time 和 end_time 秒为单位，差值不得小于5s，UNIX 时间戳。

设备返回的 json 结构：
```
	{
	    "video_list":[
		{
		    "start_time":"&lt;unix时间戳&gt;",
		    "end_time":"&lt;unix时间戳&gt;"
		},
		{
		    "start_time":"&lt;unix时间戳&gt;",
		    "end_time":"&lt;unix时间戳&gt;"
		}
	    ]
	}
```

###### 按月查询 

`action=inner_define&channel=0&cmd=get_month_record&time=yyyymm`
参数说明：
- yyyymm中前四位是年份，后两位是月份；
- xxxx：表示32位的数字，从低位到高位每一比特代表月份的第几天是否有录像；例如：8320（0010000010000000）表示8号和14号有录像；

设备返回的 json 结构：
```
	{"video_list"："xxxx"}
```

##### 暂停回放

`action=inner_define&channel=xxx&cmd=playback_pause`

设备返回的 json 结构：
```
	{"status":"code"}
```

##### 继续回放 

`action=inner_define&channel=xxx&cmd=playback_resume`

设备返回的 json 结构：
```
	{"status":"code"}
```

##### 录像进度条滑动 

`action=inner_define&channel=xxx&cmd=playback_seek&time=ssss`
 参数说明：ssss 是 UNIX 时间戳,单位s。
	
设备返回的json结构：
```
	{"status":"code"}
```

##### 获取 ipc 设备状态

判断是否可以请求视频流(type 区分直播(live)和对讲(voice)):`action=inner_define&channel=0&cmd=get_device_st&type=(voice/live)&quality=standard`
参数说明：app_connect_num 表示：已连接到设备的 APP 数量。    
	
返回的 json 结构：
```
[{"status":"code"，"appConnectNum":"2"}]
```
    
| 取值 | 含义 |
|:-|:-|
| 0 | 接收请求 |
| 1 | 拒绝请求 |
| 404 | 错误请求 |
| 405 | 连接 APP 数量超过最大连接数 |
| 406 | 信令不支持 |


##### 云台控制信令

channel 固定为0


- 控制 ipc 左移:`action=user_define&channel=0&cmd=ptz_left`
- 控制 ipc 右移:`action=user_define&channel=0&cmd=ptz_right`
- 控制 ipc 上移:`action=user_define&channel=0&cmd=ptz_up`
- 控制 ipc 下移:`action=user_define&channel=0&cmd=ptz_down`


#### nvr 设备

##### 设备查询:

返回`channel`和`devicename`

```
查询nvr设备子设备:`action=inner_define&cmd=get_nvr_list&nvr=$nvrname
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

##### 查询设备本地录像列表:

`action=inner_define&channel=xxx&cmd=get_record_index&start_time=000&end_time=111`

##### 获取 ipc 设备状态

判断是否可以请求视频流(type 区分直播(live)和对讲(voice)):

`action=inner_define&channel=xxx&cmd=get_device_st&type=(voice/live)&quality=standard`

##### 云台控制信令

channel 通过查询指令获取
- 控制ipc左移:`action=user_define&channel=xxx&cmd=ptz_left`
- 控制ipc右移:`action=user_define&channel=xxx&cmd=ptz_right`
- 控制ipc上移:`action=user_define&channel=xxx&cmd=ptz_up`
- 控制ipc下移:`action=user_define&channel=xxx&cmd=ptz_down`


### 使用示例(以 Android 为例)

- ipc 设备
```shell
/* 通过云台控制ipc左移 */
char ipc_ctl_cmd[] = "action=user_define&channel=0&cmd=ptz_left";
/* 
 * 异步方式
 * 控制结果:设备端将指令执行结果发送到app端，SDK通过事先注册的回调通知到用户
 */
postCommandRequestWithAsync($id, ipc_ctl_cmd, strlen(ipc_ctl_cmd));
```
- nvr设备(nvr设备发送控制信令前需发送查询信令获取channel)
```shell
/* 查询nvr设备子设备 */
char nvr_get_cmd[] = "action=inner_define&cmd=get_nvr_list";
/* 
 * 异步方式
 * 控制结果:设备端将指令执行结果发送到app端，SDK通过事先注册的回调通知到用户
 */
postCommandRequestWithAsync($id, nvr_get_cmd, strlen(nvr_get_cmd));
/* 从回调函数中获取channel */
char *channel = getChannel();
/* 通过云台控制nvr左移 */
char nvr_ctl_cmd[] = "action=user_define&channel=$channel&cmd=ptz_left";
/* 控制nvr设备左移 */
postCommandRequestWithAsync($id, nvr_ctl_cmd, strlen(nvr_ctl_cmd));
```

## 基于请求参数进行单向交互

### 信令使用场景

应用端需要向 ipc 设备发送语音数据或向设备端请求视频数据时需要告诉设备端数据格式(高清、标清等)，可以直接使用请求参数达到目的。

### 接口及命令格式

#### SDK 语音对讲及直播接口

#### ipc 设备

##### 启动语音对讲

```
开始语音对讲:`channel=0`
```

##### 启动直播

(channel 固定为0)


- 直播标准流:`ipc.flv?action=live&channel=0&quality=standard`
- 直播高清流:`ipc.flv?action=live&channel=0&quality=high`
- 直播超清流:`ipc.flv?action=live&channel=0&quality=super`



#### nvr 设备

##### 启动语音对讲

```
开始语音对讲:`channel=xxx`
```

##### 启动直播

(channel 通过查询指令获取)


- 直播标准流:`ipc.flv?action=live&channel=xxx&quality=standard`
- 直播高清流:`ipc.flv?action=live&channel=xxx&quality=high`
- 直播超清流:`ipc.flv?action=live&channel=xxx&quality=super`



- nvr 设备(nvr 设备发送控制信令前需发送查询信令获取 channel)

### 使用示例（以 Android 为例）

```shell
/* 查询nvr设备子设备 */
char nvr_get_cmd[] = "action=inner_define&cmd=get_nvr_list";

/* 
 * 异步方式
 * 控制结果:设备端将指令执行结果发送到app端，SDK通过事先注册的回调通知到用户
 */
postCommandRequestWithAsync($id, nvr_get_cmd, strlen(nvr_get_cmd));

/* 从回调函数中获取channel */
char *channel = getChannel();

/* 查询设备状态 */
char nvr_state_cmd[] = "action=inner_define&channel=$channel&cmd=get_device_st&type=(live)&quality=high";

/* 
 * 异步方式
 * 控制结果:设备端将指令执行结果发送到app端，SDK通过事先注册的回调通知到用户
 */
postCommandRequestWithAsync($id, nvr_state_cmd, strlen(nvr_state_cmd));

/* 高清直播 */
char nvr_live_cmd[] = "ipc.flv?action=live&channel=$channel&quality=high";

/* 
 * 数据流:设备端将数据流发送到app端，SDK通过事先注册的回调通知到用户
 */
startAvRecvService($id, nvr_live_cmd, true);

/* 语音对讲 */
char nvr_voice_cmd[] = "channel=$channel";

/* 
 * 数据流:使用SDK提供的dataSend接口发送数据
 */
runSendService($id, nvr_voice_cmd, true);

```
