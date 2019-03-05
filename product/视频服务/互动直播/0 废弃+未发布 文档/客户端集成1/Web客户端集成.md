**1 Login**

登录IM通讯云。在进行音视频会话前，应用先要先进行登录。

```
Login(sdk_app_id, account_type, app_id_at3rd, identifier, user_sig);
```

**参数**

```
sdk_app_id 应用标识。
account_type 账号类型。
app_id_at3rd 第三方应用的appid。
identifier 用户账号。
user_sig 用户身份鉴权信息。
```

**返回值**
无

>备注
应用在进行音视频会话前需要先调用Login接口完成IM通讯的登录操作，并等待Login回调通知，只有Login执行成功后才能进行音视频会话功能。

**2 StartContext**

启动SDK，创建上下文。

```
StartContext(sdk_app_id, account_type, app_id_at3rd, identifier, user_sig);
```

**参数**

```
sdk_app_id 应用标识。
account_type 账号类型。
app_id_at3rd 第三方应用的appid。
identifier 用户账号。
user_sig 用户身份鉴权信息。
```

**返回值**
无

>备注
只有在收到Login成功回调通知时，才能调用StartContext，并等待StartContext回调通知，只有StartContext执行成功后才能进行其它接口调用。

**3 StopContext**

停止SDK，释放上下文。

```
StopContext()
```

**返回值**

S_OK 接口调用成功。 
无

>备注
退出音视频会话时调用StopContext，释放上下文资源。

**4 EnterRoom**

进入房间。

```
EnterRoom(room_type, relation_type, relation_id, mode, auther);
```

**参数**

```
room_type 房间类型， 固定填2，表示多人房间。
relation_type 关系类型，固定填6。
relation_id 关系Id（房间号）。
mode 音视频通话模式，固定值为1，表示视频通话。
auther 音视频权限bitmap，暂时没有用到，固定填0。
```

**返回值**

无

>备注
只有在启动sdk成功之后，才可以加入房间，如果EnterRoom进入的房间号relation_id不存在，将创建一个新的房间。EnterRoom的执行结果将通过回调接口通知应用层。

**5 ExitRoom**

退出房间。

```
ExitRoom();
```

**返回值**

无

>备注
ExitRoom的执行结果将通过回调接口通知应用层。

**6 GetEndpointAVMode**

获取房间成员音频、视频状态

```
GetEndpointAVMode(identifier);
```

**参数**

identifier 房间成员ID。

**返回值**

用户的音频、视频状态。1：具有视频（打开了摄像头）；2：具有音频（打开了麦克风）；3：同时具有音频和视频（同时打开了摄像头和麦克风）

**7 SetVideoWinPos**

设置其他成员视频显示窗口的大小和位置

```
SetVideoWinPos(identifier, ulPosx, ulPosy, ulWidth, ulHeight)
```

**参数**

```
identifier房间成员ID
ulPosX 视频窗口显示位置，x坐标
ulPosy 视频窗口显示位置，y坐标
ulWidth 视频窗口宽度
ulHeight 视频窗口高度
```

**返回值**

无

**8 MuteAudio**

打开或关闭房间成员声音。

```
MuteAudio(identifier, is_mute);
```

**参数**

```
identifier 房间成员ID。
is_mute：是否设置静音，1：是，0：否。
```

**返回值**

无

**9 RequestViewList**

请求多位房间成员视频画面


```
RequestViewList(identifier_list);
```

**参数**

```
Identifier_list 房间成员ID数组。
```

**返回值**

无

>备注 
RequestViewList的执行结果将通过回调接口通知应用层。

**10 CancelAllView**

取消所有成员视频画面

```
CancelAllView();
```

**参数**

无

**返回值**

无

>备注 
CancelAllView的执行结果将通过回调接口通知应用层。

**11 GetCameraList**

获取摄像头列表。

```
GetCameraList(list);
```

**参数**

list摄像头列表。

**返回值**

获取成功，传入的参数list就是摄像头列表

**12 GetSelectedCameraId**

获取选中的摄像头ID。

```
GetSelectedMicId();
```

**返回值**

返回选中的摄像头ID

**13 SetSelectedCameraIndex**

设置应用使用的摄像头设备索引。

```
SetSelectedCameraIndex(index);
```

**参数**

index 摄像头索引，为GetCameraList返回的摄像头列表中的索引。

**返回值**

无

**14 OpenCamera**

打开摄像头。


```
OpenCamera();
```

**返回值**

无

>备注 
OpenCamera的执行结果将通过回调接口通知应用层。

**15 CloseCamera**

关闭摄像头。

```
CloseCamera();
```

**返回值**
无

>备注 
CloseCamera的执行结果将通过回调接口通知应用层。

**16 GetMicList**

获取系统安装的麦克风设备列表。


```
GetMicList(list);
```

**参数**
List 麦克风列表。

**返回值**

获取成功，传入的参数list就是麦克风列表

**17 SetSelectedMicIndex**

设置使用的麦克风索引。

```
SetSelectedMicIndex(index);
```

**参数**

index 麦克风索引，为GetMicList返回的麦克风列表中的索引号。

**返回值**

无

**18 GetSelectedMicId**

获取选中的麦克风ID。

```
GetSelectedMicId();
```

**参数**

无

**返回值**

返回选中的麦克风ID

**19 OpenMic**

打开麦克风。

```
OpenMic();
```

**返回值**

无

>备注 
OpenMic的执行结果将通过回调接口通知应用层。

**20 CloseMic**

关闭麦克风。

```
CloseMic();
```

**返回值**

无

>备注 
CloseMic的执行结果将通过回调接口通知应用层。

**21 SetMicVolumn**

设置麦克风音量。

```
SetMicVolumn(value);
```

**参数**

value 麦克风音量 ，取值返回0~100。0：最小音量，100：最大音量。

**返回值**

无

**22 GetMicVolumn**

获取麦克风音量。

```
GetMicVolumn();
```

**参数**

无

**返回值**

返回麦克风音量

**23 GetPlayerList **

获取扬声器列表。

```
GetPlayerList(list);
```

**参数**

list扬声器列表。

**返回值**

获取成功，传入的参数list就是扬声器列表

**24 SetSelectedPlayerIndex**

设置应用使用的扬声器索引

```
SetSelectedPlayerIndex(index)
```

**参数**

index扬声器序号，为GetPlayerList返回的扬声器列表里的序号。

**返回值**

无

**25 OpenPlayer**

打开扬声器

```
OpenPlayer(void)
```

**返回值**
无

**备注 **

OpenPlayer的执行结果将通过回调接口通知应用层。

**26 ClosePlayer**

关闭扬声器

```
ClosePlayer();
```

**返回值**

无

>备注 
ClosePlayer的执行结果将通过回调接口通知应用层。

**27 GetPlayerVolumn**

获取扬声器音量。

```
GetPlayerVolumn();
```

**参数**

无

**返回值**

返回扬声器音量

**28 SetPlayerVolumn**

设置扬声器音量。

```
SetPlayerVolumn(value);
```

**参数**

value音量大小，取值0~100。

**返回值**
无

**29 qavsdk_eventcallback**

js回调函数。Html页面上必须定义qavsdk_eventcallback函数，用来接收ActiveX的回调和事件通知。

```
function qavsdk_eventcallback(evt,result,oper,vcnt,vusers)
```

**参数**

```
evt 事件类型，参考后面的事件类型定义
result 结果，0：成功，非0表示失败
oper 操作类型，evt=3155、3156、3158时有效
vcnt 房间成员个数，evt=3150时有效
vusers，房间成员列表，evt=3150时有效
```

**事件类型：**

```
3144 登录，Login接口的执行结果通知。
3146 启动sdk，StartContext的执行结果通知。
3147 停止sdk, StopContext的执行结果通知。
3148 加入房间， EnterRoom的执行结果通知
3149 退出房间， ExitRoom的执行结果通知
3150 房间成员变化通知，收到该回调时，可以获取到当前的房间成员列表
3153 请求多位成员视频画面， RequestViewList的执行结果通知
3154 取消所有成员视频画面， CancelAllView的执行结果通知
3155 打开/关闭麦克风结果通知，
      Oper 1，打开麦克风，2，关闭麦克风
3156 打开/关闭扬声器结果通知
      Oper 1，打开扬声器，2，关闭扬声器
3158 打开/关闭摄像头通知
      Oper 1，打开摄像头，2，关闭摄像头
```

      

