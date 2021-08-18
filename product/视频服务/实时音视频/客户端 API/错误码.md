## 错误码表
### 基础错误码

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_NULL|0|无错误|

### 进房相关错误码

TRTCCloud.enterRoom() 在进房失败时会触发此类错误码，您可以通过回调函数 TRTCCloudDelegate.onEnterRoom() 和 TRTCCloudDelegate.OnError() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_ROOM_ENTER_FAIL|-3301|进入房间失败|
|ERR_ENTER_ROOM_PARAM_NULL|-3316|进房参数为空，请检查 TRTCCloud.enterRoom(): 接口调用是否传入有效的 param|
|ERR_SDK_APPID_INVALID|-3317|进房参数 sdkAppId 错误|
|ERR_ROOM_ID_INVALID|-3318|进房参数 roomId 错误|
|ERR_USER_ID_INVALID|-3319|进房参数 userID 不正确|
|ERR_USER_SIG_INVALID|-3320|进房参数 userSig 不正确|
|ERR_ROOM_REQUEST_ENTER_ROOM_TIMEOUT|-3308|请求进房超时，请检查网络|
|ERR_SERVER_INFO_SERVICE_SUSPENDED|-100013|服务不可用。请检查：套餐包剩余分钟数是否大于0，腾讯云账号是否欠费|


### 退房相关错误码

TRTCCloud.exitRoom() 在退房失败时会触发此类错误码，您可以通过回调函数 TRTCCloudDelegate.OnError() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_ROOM_REQUEST_QUIT_ROOM_TIMEOUT|-3325|请求退房超时|


### 设备（摄像头、麦克风、扬声器）相关错误码

您可以通过回调函数 TRTCCloudDelegate.OnError() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_CAMERA_START_FAIL|-1301|打开摄像头失败，例如在 Windows 或 Mac 设备，摄像头的配置程序（驱动程序）异常，禁用后重新启用设备，或者重启机器，或者更新配置程序|
|ERR_CAMERA_NOT_AUTHORIZED|-1314|摄像头设备未授权，通常在移动设备出现，可能是权限被用户拒绝了|
|ERR_CAMERA_SET_PARAM_FAIL|-1315|摄像头参数设置出错（参数不支持或其它）|
|ERR_CAMERA_OCCUPY|-1316|摄像头正在被占用中，可尝试打开其他摄像头|
|ERR_MIC_START_FAIL|-1302|打开麦克风失败，例如在 Windows 或 Mac 设备，麦克风的配置程序（驱动程序）异常，禁用后重新启用设备，或者重启机器，或者更新配置程序|
|ERR_MIC_NOT_AUTHORIZED|-1317|麦克风设备未授权，通常在移动设备出现，可能是权限被用户拒绝了|
|ERR_MIC_SET_PARAM_FAIL|-1318|麦克风设置参数失败|
|ERR_MIC_OCCUPY|-1319|麦克风正在被占用中，例如移动设备正在通话时，打开麦克风会失败|
|ERR_MIC_STOP_FAIL|-1320|停止麦克风失败|
|ERR_SPEAKER_START_FAIL|-1321|打开扬声器失败，例如在 Windows 或 Mac 设备，扬声器的配置程序（驱动程序）异常，禁用后重新启用设备，或者重启机器，或者更新配置程序|
|ERR_SPEAKER_SET_PARAM_FAIL|-1322|扬声器设置参数失败|
|ERR_SPEAKER_STOP_FAIL|-1323|停止扬声器失败|


### 屏幕分享相关错误码

您可以通过回调函数 TRTCCloudDelegate.OnError() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_SCREEN_CAPTURE_START_FAIL|-1308|开始录屏失败，如果在移动设备出现，可能是权限被用户拒绝了，如果在 Windows 或 Mac 系统的设备出现，请检查录屏接口的参数是否符合要求|
|ERR_SCREEN_CAPTURE_UNSURPORT|-1309|录屏失败，在 Android 平台，需要5.0以上的系统，在 iOS 平台，需要11.0以上的系统|
|ERR_SERVER_CENTER_NO_PRIVILEDGE_PUSH_SUB_VIDEO|-102015|没有权限上行辅路|
|ERR_SERVER_CENTER_ANOTHER_USER_PUSH_SUB_VIDEO|-102016|其他用户正在上行辅路|
|ERR_SCREEN_CAPTURE_STOPPED|-7001|录屏被系统中止|


### 编解码相关错误码

您可以通过回调函数 TRTCCloudDelegate.OnError() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_VIDEO_ENCODE_FAIL|-1303|视频帧编码失败，例如 iOS 设备切换到其他应用时，硬编码器可能被系统释放，再切换回来时，硬编码器重启前，可能会抛出|
|ERR_UNSUPPORTED_RESOLUTION|-1305|不支持的视频分辨率|
|ERR_AUDIO_ENCODE_FAIL|-1304|音频帧编码失败，例如传入自定义音频数据，SDK 无法处理|
|ERR_UNSUPPORTED_SAMPLERATE|-1306|不支持的音频采样率|


### 自定义采集相关错误码

您可以通过回调函数 TRTCCloudDelegate.OnError() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_PIXEL_FORMAT_UNSUPPORTED|-1327|设置的 pixel format 不支持|
|ERR_BUFFER_TYPE_UNSUPPORTED|-1328|设置的 buffer type 不支持|


### CDN 绑定和混流相关错误码

您可以通过回调函数 TRTCCloudDelegate.onStartPublishing() 和 TRTCCloudDelegate.onSetMixTranscodingConfig() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_PUBLISH_CDN_STREAM_REQUEST_TIME_OUT|-3321|旁路转推请求超时|
|ERR_CLOUD_MIX_TRANSCODING_REQUEST_TIME_OUT|-3322|云端混流请求超时|
|ERR_PUBLISH_CDN_STREAM_SERVER_FAILED|-3323|旁路转推回包异常|
|ERR_CLOUD_MIX_TRANSCODING_SERVER_FAILED|-3324|云端混流回包异常|
|ERR_ROOM_REQUEST_START_PUBLISHING_TIMEOUT|-3333|开始向腾讯云的直播 CDN 推流信令超时|
|ERR_ROOM_REQUEST_START_PUBLISHING_ERROR|-3334|开始向腾讯云的直播 CDN 推流信令异常|
|ERR_ROOM_REQUEST_STOP_PUBLISHING_TIMEOUT|-3335|停止向腾讯云的直播 CDN 推流信令超时|
|ERR_ROOM_REQUEST_STOP_PUBLISHING_ERROR|-3336|停止向腾讯云的直播 CDN 推流信令异常|


### 跨房连麦相关错误码

TRTCCloud.ConnectOtherRoom() 在跨房失败时会触发此类错误码，您可以通过回调函数 TRTCCloudDelegate.onConnectOtherRoom() 捕获相关通知。

| 符号 | 值 | 含义 |
|---|---|---|
|ERR_ROOM_REQUEST_CONN_ROOM_TIMEOUT|-3326|请求连麦超时|
|ERR_ROOM_REQUEST_DISCONN_ROOM_TIMEOUT|-3327|请求退出连麦超时|
|ERR_ROOM_REQUEST_CONN_ROOM_INVALID_PARAM|-3328|无效参数|
|ERR_CONNECT_OTHER_ROOM_AS_AUDIENCE|-3330|当前是观众角色，不能请求或断开跨房连麦，需要先 switchRole() 到主播|
|ERR_SERVER_CENTER_CONN_ROOM_NOT_SUPPORT|-102031|不支持跨房间连麦|
|ERR_SERVER_CENTER_CONN_ROOM_REACH_MAX_NUM|-102032|达到跨房间连麦上限|
|ERR_SERVER_CENTER_CONN_ROOM_REACH_MAX_RETRY_TIMES|-102033|跨房间连麦重试次数耗尽|
|ERR_SERVER_CENTER_CONN_ROOM_REQ_TIMEOUT|-102034|跨房间连麦请求超时|
|ERR_SERVER_CENTER_CONN_ROOM_REQ|-102035|跨房间连麦请求格式错误|
|ERR_SERVER_CENTER_CONN_ROOM_NO_SIG|-102036|跨房间连麦无签名|
|ERR_SERVER_CENTER_CONN_ROOM_DECRYPT_SIG|-102037|跨房间连麦签名解密失败|
|ERR_SERVER_CENTER_CONN_ROOM_NO_KEY|-102038|未找到跨房间连麦签名解密密钥|
|ERR_SERVER_CENTER_CONN_ROOM_PARSE_SIG|-102039|跨房间连麦签名解析错误|
|ERR_SERVER_CENTER_CONN_ROOM_INVALID_SIG_TIME|-102040|跨房间连麦签名时间戳错误|
|ERR_SERVER_CENTER_CONN_ROOM_SIG_GROUPID|-102041|跨房间连麦签名不匹配|
|ERR_SERVER_CENTER_CONN_ROOM_NOT_CONNED|-102042|本房间无连麦|
|ERR_SERVER_CENTER_CONN_ROOM_USER_NOT_CONNED|-102043|本用户未发起连麦|
|ERR_SERVER_CENTER_CONN_ROOM_FAILED|-102044|跨房间连麦失败|
|ERR_SERVER_CENTER_CONN_ROOM_CANCEL_FAILED|-102045|取消跨房间连麦失败|
|ERR_SERVER_CENTER_CONN_ROOM_CONNED_ROOM_NOT_EXIST|-102046|被连麦房间不存在|
|ERR_SERVER_CENTER_CONN_ROOM_CONNED_REACH_MAX_ROOM|-102047|被连麦房间达到连麦上限|
|ERR_SERVER_CENTER_CONN_ROOM_CONNED_USER_NOT_EXIST|-102048|被连麦用户不存在|
|ERR_SERVER_CENTER_CONN_ROOM_CONNED_USER_DELETED|-102049|被连麦用户已被删除|
|ERR_SERVER_CENTER_CONN_ROOM_CONNED_USER_FULL|-102050|被连麦用户达到资源上限|
|ERR_SERVER_CENTER_CONN_ROOM_INVALID_SEQ|-102051|连麦请求序号错乱|


## 警告码表

警告码无需特别关注，您可以按需选择是否对当前用户进行相应的提示。

| 符号 | 值 | 含义 |
|---|---|---|
|WARNING_HW_ENCODER_START_FAIL|1103|硬编码启动出现问题，自动切换到软编码|
|WARNING_VIDEO_ENCODER_SW_TO_HW|1107|当前 CPU 使用率太高，无法满足软件编码需求，自动切换到硬件编码|
|WARNING_INSUFFICIENT_CAPTURE_FPS|1108|摄像头采集帧率不足，部分自带美颜算法的 Android 手机上会出现|
|WARNING_SW_ENCODER_START_FAIL|1109|软编码启动失败|
|WARNING_REDUCE_CAPTURE_RESOLUTION|1110|摄像头采集分辨率被降低，以满足当前帧率和性能最优解。|
|WARNING_CAMERA_DEVICE_EMPTY|1111|没有检测到可用的摄像头设备|
|WARNING_CAMERA_NOT_AUTHORIZED|1112|用户未授权当前应用使用摄像头|
|WARNING_MICROPHONE_DEVICE_EMPTY|1201|没有检测到可用的麦克风设备|
|WARNING_SPEAKER_DEVICE_EMPTY|1202|没有检测到可用的扬声器设备|
|WARNING_MICROPHONE_NOT_AUTHORIZED|1203|用户未授权当前应用使用麦克风|
|WARNING_MICROPHONE_DEVICE_ABNORMAL|1204|音频采集设备不可用（例如被占用）|
|WARNING_SPEAKER_DEVICE_ABNORMAL|1205|音频播放设备不可用（例如被占用）|
|WARNING_VIDEO_FRAME_DECODE_FAIL|2101|当前视频帧解码失败|
|WARNING_AUDIO_FRAME_DECODE_FAIL|2102|当前音频帧解码失败|
|WARNING_VIDEO_PLAY_LAG|2105|当前视频播放出现卡顿|
|WARNING_HW_DECODER_START_FAIL|2106|硬解启动失败，采用软解码|
|WARNING_VIDEO_DECODER_HW_TO_SW|2108|当前流硬解第一个 I 帧失败，SDK 自动切软解|
|WARNING_SW_DECODER_START_FAIL|2109|软解码器启动失败|
|WARNING_VIDEO_RENDER_FAIL|2110|视频渲染失败|
|WARNING_START_CAPTURE_IGNORED|4000|已经在采集，启动采集被忽略|
|WARNING_AUDIO_RECORDING_WRITE_FAIL|7001|音频录制写入文件失败|
|WARNING_ROOM_DISCONNECT|5101|网络断开连接|
|WARNING_IGNORE_UPSTREAM_FOR_AUDIENCE|6001|当前是观众角色，忽略上行音视频数据|
|WARNING_NET_BUSY|1101|网络状况不佳：上行带宽太小，上传数据受阻|
|WARNING_RTMP_SERVER_RECONNECT|1102|直播推流，网络断连, 已启动自动重连（自动重连连续失败超过三次会放弃）|
|WARNING_LIVE_STREAM_SERVER_RECONNECT|2103|直播拉流，网络断连, 已启动自动重连（自动重连连续失败超过三次会放弃）|
|WARNING_RECV_DATA_LAG|2104|网络来包不稳：可能是下行带宽不足，或由于主播端出流不均匀|
|WARNING_RTMP_DNS_FAIL|3001|直播，DNS 解析失败|
|WARNING_RTMP_SEVER_CONN_FAIL|3002|直播，服务器连接失败|
|WARNING_RTMP_SHAKE_FAIL|3003|直播，与 RTMP 服务器握手失败|
|WARNING_RTMP_SERVER_BREAK_CONNECT|3004|直播，服务器主动断开|
|WARNING_RTMP_READ_WRITE_FAIL|3005|直播，RTMP 读/写失败，将会断开连接|
|WARNING_RTMP_WRITE_FAIL|3006|直播，RTMP 写失败（SDK 内部错误码，不会对外抛出）|
|WARNING_RTMP_READ_FAIL|3007|直播，RTMP 读失败（SDK 内部错误码，不会对外抛出）|
|WARNING_RTMP_NO_DATA|3008|直播，超过30s 没有数据发送，主动断开连接|
|WARNING_PLAY_LIVE_STREAM_INFO_CONNECT_FAIL|3009|直播，connect 服务器调用失败（SDK 内部错误码，不会对外抛出）|
|WARNING_NO_STEAM_SOURCE_FAIL|3010|直播，连接失败，该流地址无视频（SDK 内部错误码，不会对外抛出）|
|WARNING_ROOM_RECONNECT|5102|网络断连，已启动自动重连|
|WARNING_ROOM_NET_BUSY|5103|网络状况不佳：上行带宽太小，上传数据受阻|
    
