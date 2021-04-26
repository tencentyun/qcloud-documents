本文档介绍了 OpenSDK 游戏语音 C# 接口 SDK 的接入方法，适用于 Unity3D 引擎开发的游戏。
### 1. 下载SDK
SDK 以 unitypackage 的格式提供，双击导入到 Unity 工程中即可。导入后，目录结构如下：
![目录结构](https://mc.qcloudimg.com/static/img/ec0d5e296afdffbb9b376aa74fba8409/image.png)
### 2. 接入代码实例：
```
public class MainScene : MonoBehaviour{
	void onClickStartContextBtn()
	{
		IQAVVoiceEngine engine = IQAVVoiceEngine.GetEngine ();
		//AppID 和 AccountType 在腾讯云上申请
		//OpenID 由 APP 自行生成，保证每个用户 OpenID 不同就行，目前必须是数字
		engine.SetAppInfo("AppID","AccountType","OpenID");
		
		engine.Init(delegate(int result, string error_info){
			if(result == QAVContext.AV_OK){
				int roomID = 0;       //RoomID 由 APP 自行分配，进入同一个 RoomID 中的用户可以互相说话
				string role = "user"; //角色由 APP 开发者在腾讯云中的 Spear 引擎配置页面中自行预设
				engine.JoinRoom(roomID, role);
			}
		});
	}
}
```
### 3. 接口调用流程
#### 3.1 基本 API：无论语音消息功能还是实时语音都需要的基本API。

**接口说明：**获取语音引擎句柄
**函数原型：**`IQAVVoiceEngine GetEngine();`
#### 3.2 实时语音API：实时语音功能调用；
**接口说明：**设置业务信息
**函数原型：**`int SetAppInfo(string appID, string accountType, string openID);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| appID | string | 开通业务页面中的游戏ID，在腾讯云上申请 |
| accountType | string | 在腾讯云上申请 |
| openID | string | 玩家唯一标识，比如从手Q或者微信获得到的OpenID |
| 返回值 | int | 成功时返回QAVError.AV_OK |

**接口说明：**初始化 QAVVoiceEngine，必须在SetAppInfo之后调用
**函数原型：**`int Init(InitCompleteHandler initHandler);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| initHandler | InitCompleteHandler | Callback |
| 返回值 | int | 成功时返回QAVError.AV_OK |

**接口说明：**加入语音房间
**函数原型：**`int JoinRoom(int roomID, String role);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| roomID | int | 加入房间ID，由APP自行分配的，进入同一个ID可以自由说话 |
| role | string | 角色由APP开发者在腾讯云中的spear引擎配置页面中预设的 |

#### 3.3 语音消息API：消息语音功能调用；

**接口说明：**语音转文字 ,为了避免过大的游戏音效影响识别效果，建议游戏业务层在启用录制时关闭背景音效或进行压低的操作，来实现更好的语音识别效果。
**函数原型：**`int SpeechToText(string fileID);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| fileID | string | 需要转文字的语音文件标识 |

**接口说明：**设置最大语音录音时长
**函数原型：**`int SetMaxMessageLength(int msTime);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| msTime | int | 设置语音消息时长，单位s |

**接口说明：**启动录音
**函数原型：**`int StartRecording(string filePath);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| filePath | string | 播放的语音路径，可以为NULL |

**接口说明：**停止录音
**函数原型：**`int StopRecording ();`
**接口说明：**上传语音文件
**函数原型：**`int UploadRecordedFile (string filePath);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| filePath | string | 上传语音的文件路径 |

**接口说明：**下载语音文件 
**函数原型：**`int DownloadRecordedFile (string fileID, string downloadFilePath);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| fileID | string | 需要下载的文件 |
| downloadFilePath | string |文件存储路径，可以为NULL |

**接口说明：**播放语音文件 
**函数原型：**`int PlayRecordedFile (string downloadFilePath);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| downloadFilePath | string | 播放语音的文件路径 |

**接口说明：**停止播放语音文件  
**函数原型：**`int StopPlayFile ();`

#### 3.4 实时语音API：实时语音功能调用；
**接口说明：**设置业务信息
**函数原型：**`int SetAppInfo(string appID, string accountType, string openID);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| appID | string | 开通业务页面中的游戏ID，在腾讯云上申请 |
| accountType | string | 在腾讯云上申请 |
| openID | string | 玩家唯一标识，比如从手Q或者微信获得到的OpenID |
| 返回值 | int | 成功时返回QAVError.AV_OK |

**接口说明：**初始化 QAVVoiceEngine，必须在SetAppInfo之后调用
**函数原型：**`int Init(InitCompleteHandler initHandler);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| initHandler | InitCompleteHandler | Callback |
| 返回值 | int | 成功时返回QAVError.AV_OK |

**接口说明：**加入语音房间 
**函数原型：**`int JoinRoom(int roomID, String role);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| roomID | int | 加入房间ID，由APP自行分配的，进入同一个ID可以自由说话 |
| role | string | 角色由APP开发者在腾讯云中的spear引擎配置页面中预设的 |

**接口说明：**注册音频回调，用于叠加音频回调，用于伴奏场景
**函数原型：**`int RegistAudioDataCallback(int srcType, 
QAVAudioCtrl.QAVAudioDataCallback audioDataCallback);`

| 参数 | 类型 | 意义 |
|---------|---------|---------|
| srcType | int | Callback |
| 返回值 | int | QAVAudioDataSource_MixToSend = 1,<br>///< 发送混音输入用于叠加给远端用户听(比如在房间内部，非自己听到伴奏声音)<br>QAVAudioDataSource_MixToPlay = 3, ///< 扬声器混音输入用于叠加给自己听,用于自己本端听到伴奏声音)  |
| audioDataCallback |  | 音频回调 业务层需要实现这一个回调函数 注册给sdk sdk会通过这个回调拿音频数据 而业务层需要在这个回调里面把伴奏数据塞给SDK |

#### 4. 错误码表

| 错误 | 十进制值 | 意义 |
|---------|---------|---------|
| AV_OK | 0 | Success |
| AV_ERR_FAIL | 1 | 一般错误 |
| AV_ERR_REPETITIVE_OPERATION | 1001 | 重复操作 |
| AV_ERR_EXCLUSIVE_OPERATION | 1002 | 互斥操作 |
| AV_ERR_HAS_IN_THE_STATE | 1003 | 已经处于所要状态，无需再操作 |
| AV_ERR_INVALID_ARGUMENT | 1004 | 错误参数 |
| AV_ERR_TIMEOUT | 1005 | 操作超时 |
| AV_ERR_NOT_IMPLEMENTED | 1006 | 功能未实现 |
| AV_ERR_NOT_IN_MAIN_THREAD | 1007 | 不在主线程中执行操作 |
| AV_ERR_RESOURCE_IS_OCCUPIED | 1008 | 资源被占用 |
| AV_ERR_CONTEXT_NOT_START | 1101 | AVContext没有启动 |
| AV_ERR_CONTEXT_NOT_STOP | 1102 | AVContext未结束 |
| AV_ERR_ROOM_NOT_EXIST | 1201 | 房间不存在 |
| AV_ERR_ROOM_NOT_EXITED | 1202 | 房间未退出 |
| AV_ERR_DEVICE_NOT_EXIST | 1301 | 设备不存在 |
| AV_ERR_ENDPOINT_NOT_EXIST | 1401 | 房间成员不存在 |
| AV_ERR_ENDPOINT_HAS_NOT_VIDEO | 1402 | 该成员没有上视频 |
| AV_ERR_TINYID_TO_OPENID_FAILED | 1501 | tinyid转换至identifier失败 |
| AV_ERR_OPENID_TO_TINYID_FAILED | 1502 | identifier转换至tinyid失败 |
| AV_ERR_NOT_TRY_NEW_ROOM | 2001 | 没有尝试进入新房间，将停留在旧房间 |
| AV_ERR_TRY_NEW_ROOM_FAILED | 2002 | 尝试进入新房间，但失败了，旧房间也将关闭 |
| AV_ERR_SERVER_FAILED | 10001 | 服务器内部错误 |
| AV_ERR_SERVER_NO_PERMISSION | 10003 | 没有权限 |
| AV_ERR_SERVER_REQUEST_ROOM_ADDRESS_FAIL | 10004 | 进房间获取房间地址失败 |
| AV_ERR_SERVER_CONNECT_ROOM_FAIL | 10005 | 进房间连接房间失败 |
| AV_ERR_SERVER_FREE_FLOW_AUTH_FAIL | 10006 | 免流情况下，免流签名校验失败，导致进房获取房间地址失败 |
| AV_ERR_IMSDK_UNKNOWN | 6999 | IMSDK内部错误 |
| AV_ERR_IMSDK_TIMEOUT | 7000 | IMSDK内部错误 |
| AV_ERR_UNKNOWN | 65536 | IMSDK内部错误 |
| AV_ERR_SOUTIL_INTERNAL_MEMORY_NOT_ENOUGH | 10101 | 手机ROM空间不够，建议用户删除部分程序，然后重新启动app |
| AV_ERR_SOUTIL_INTERNAL_ERROR | 10102 | 手机内部出错，建议用户重新安装 |