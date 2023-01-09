

##  so 库调用方法

### 用户回调

#### 媒体流数据接收回调

- 接口描述
  接收设备媒体流数据回调。用于裸流方式观看直播时，SDK 回调该接口向用户传输接收的设备端媒体流数据。
<dx-codeblock>
:::  Java
typedef void (*av_recv_handle_t)(const char *id, uint8_t* recv_buf, size_t recv_len);
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">recv_buf</td>
<td align="left">uint8_t *</td>
<td align="left">接收到的媒体流数据</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">recv_len</td>
<td align="left">size_t</td>
<td align="left">接收到的媒体流数据长度</td>
<td align="left">输出</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

#### [控制类消息通知回调](id:test21)

- 接口描述
  接收控制类消息回调。用于向设备请求非媒体流数据时，SDK 回调该接口向用户传输接收的设备端消息，也用于通知用户 P2P 连接、数据传输等状态改变。
<dx-codeblock>
:::  Java
enum XP2PType {
    XP2PTypeClose   = 1000, //数据传输完成
    XP2PTypeLog     = 1001, //日志输出
    XP2PTypeCmd     = 1002, //command json
    XP2PTypeDisconnect  = 1003, //p2p链路断开
    XP2PTypeDetectReady  = 1004, //p2p链路初始化成功,该事件回调触发后才能进行后续操作(直播、语音对讲、信令等)
    XP2PTypeDetectError  = 1005, //p2p链路初始化失败
    XP2PTypeSaveFileOn  = 8000, //获取保存音视频流开关状态
    XP2PTypeSaveFileUrl = 8001 //获取音视频流保存路径
};

typedef enum {
    XP2PVoiceServiceClose   = 2000, //语音对讲服务关闭
    XP2PStreamServiceClose  = 2001, //音视频流接收服务关闭
} XP2PCloseSubType;

typedef const char* (*msg_handle_t)(const char *id, XP2PType type, const char* msg);
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">type</td>
<td align="left">XP2PType</td>
<td align="left">通知类型</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">msg</td>
<td align="left">const char *</td>
<td align="left">接收到的消息，json 格式：<code>{“errormsg”：“$msg”，“errorcode”：$XP2PCloseSubType}</code>，具体用法请参见 <a href="#test211">设置用户回调</a></td>
<td align="left">输出</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">char *</td>
<td align="left">根据 type 不同有不同返回值</td>
</tr>
</tbody></table>

### [设置用户回调](id:test211)

- 接口描述
  设置用户回调函数。媒体流数据和控制类消息通过设置的回调函数返回。
<dx-codeblock>
:::  Java
void setUserCallbackToXp2p(av_recv_handle_t recv_handle, msg_handle_t msg_handle);
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">recv_handle</td>
<td align="left">av_recv_handle_t</td>
<td align="left">媒体流数据回调</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">msg_handle</td>
<td align="left">msg_handle_t</td>
<td align="left">控制类消息回调</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* av_recv_handle_t回调 */
void _av_data_recv(const char *id, uint8_t *data, size_t len)
{
	printf("this is _av_data_recv\n");
}

/* msg_handle_t回调 */
const char* _msg_notify(const char *id, XP2PType type, const char* msg)
{
    if (type == XP2PTypeClose) {  //av recv close callback
        int errorcode = getJsonValueInt(msg, "errorcode");  //获取'errorcode'值
        //判断是哪个服务的close
        if (errorcode == XP2PStreamServiceClose) {
            printf("this is stream service close callback\n");
        } else if (errorcode == XP2PVoiceServiceClose) {
            printf("this is voice service close callback\n");
        }
    } else if (type == XP2PTypeCmd) {  //command request callback
        printf("this is command callback\n");
    } else if (type == XP2PTypeSaveFileOn) {//是否将音视频流保存成文件
       printf("this is file save callback\n");
       printf("return "1" if write data to file, else return "0"\n");

       return "0";
    } else if (type == XP2PTypeSaveFileUrl) { //文件存储路径
        printf("this is file save callback\n");
        printf("return file path for type XP2PTypeSaveFileOn\n");

        return "/storage/emulated/0/raw_video.data";
    } else if (type == XP2PTypeLog) {
        //save or print(do not used LOG*) log message
        printf("this is log save callback\n");
        printf("id:%s, msg:%s\n", id, msg);

    } else if (type == XP2PTypeDisconnect) { //p2p链路断开
        printf("this is disconnect callback\n");
    } else if (type == XP2PTypeDetectError) { //p2p探测失败
        printf("this is p2p event callback\n");
    } else if (type == XP2PTypeDetectReady) { //p2p探测成功
        printf("this is p2p event callback\n");
        //该回调触发后才能进行p2p服务请求
    }
    return "";
}

setUserCallbackToXp2p(_av_data_recv, _msg_notify);
:::
</dx-codeblock>


### P2P 通道初始化

- 接口描述
  初始化 XP2P 服务。
<dx-codeblock>
:::  Java
int startServiceWithXp2pInfo(const char* id, const char *product_id, const char *device_name, const char* xp2p_info);
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">product_id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 产品信息</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">device_name</td>
<td align="left">const char *</td>
<td align="left">目标 camera 设备名称</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">xp2p_info</td>
<td align="left">const char *</td>
<td align="left">XP2P 信息</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">XP2PERRNONE</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">XP2PERR*</td>
<td align="left">失败，对应 <a href="https://cloud.tencent.com/document/product/1131/57611"> 错误码</a></td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 伪代码：从自建后台获取xp2p info */
const char* xp2p_info = getXP2PInfo(...);
/* 设置回调函数 */
setUserCallbackToXp2p(_av_data_recv, _msg_notify);
/* 初始化p2p */
startServiceWithXp2pInfo($id, $product_id, $device_name, xp2p_info);
:::
</dx-codeblock>


### P2P 通道传输音视频裸流

#### 启动裸流接收服务

- 接口描述
  向 camera 设备请求媒体流，异步回调方式。
<dx-codeblock>
:::  Java
void *startAvRecvService(const char *id, const char *params, bool crypto);
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">params</td>
<td align="left">const char *</td>
<td align="left">直播（action=live）或回放（action=playback）参数</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">crypto</td>
<td align="left">bool</td>
<td align="left">是否开启传输层加密</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">服务句柄</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">NULL</td>
<td align="left">失败</td>
</tr>
</tbody></table>

#### 停止接收服务

- 接口描述
  停止裸流接收，并关闭接收服务。
<dx-codeblock>
:::  Java
int stopAvRecvService(const char *id, void *req);
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">req</td>
<td align="left">void *</td>
<td align="left">服务句柄</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">XP2PERRNONE</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">XP2PERR*</td>
<td align="left">失败，对应 <a href="https://cloud.tencent.com/document/product/1131/57611"> 错误码</a></td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 设置回调函数 */
setUserCallbackToXp2p(_av_data_recv, _msg_notify);
/* 开始请求数据 */
void *req = startAvRecvService($id, "action=live", true);
/* 接收到数据后回调被触发 */
void _av_data_recv(const char *id, uint8_t *data, size_t len)
{
	//具体数据处理
	//回调中应避免耗时操作
	//多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
}
/* 停止接收 */
stopAvRecvService($id, req);
:::
</dx-codeblock>


### 接收 FLV 音视频流并使用 ijkplayer 播放

- 接口描述
 获取本地代理 url。用于播放器直接通过 url 获取数据进行播放。
```
const char *delegateHttpFlv(const char *id);
```
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">本地代理 url</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">NULL</td>
<td align="left">失败</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
char url[128] = { 0 };
/* 组合请求url */
snprintf(url, sizeof(url), "%s%s", delegateHttpFlv($id), "ipc.flv?action=live");
/* 设置url到播放器 */
setUrl2Player(url);
:::
</dx-codeblock>


### 发送语音对讲数据

#### 启动语音发送服务
- 接口描述
  启动向 camera 设备发送语音或自定义数据服务。异步非阻塞方式。
```
void *runSendService(const char *id, const char *params, bool crypto);
```
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">params</td>
<td align="left">const char *</td>
<td align="left">请求参数采用 <code>key1=value&amp;key2=value2</code> 格式，key 不允许以下划线_开头，且 key 和 value 中间不能包含 <code>&amp;/+=</code> 特殊字符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">crypto</td>
<td align="left">bool</td>
<td align="left">否开启传输层加密</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">服务句柄</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">NULL</td>
<td align="left">失败</td>
</tr>
</tbody></table>

#### 发送数据

- 接口描述
  向 camera 设备发送语音或自定义数据。
```
int dataSend(const char *id, uint8_t *data, size_t len);
```
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">data</td>
<td align="left">uint8_t *</td>
<td align="left">要发送的数据内容</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">len</td>
<td align="left">size_t</td>
<td align="left">要发送的数据长度</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">XP2PERRNONE</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">XP2PERR*</td>
<td align="left">失败，对应 <a href="https://cloud.tencent.com/document/product/1131/57611"> 错误码</a></td>
</tr>
</tbody></table>

#### 关闭语音发送服务

- 接口描述
  停止发送语音，并关闭发送服务。
```
int stopSendService(const char *id, void *req);
```
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">req</td>
<td align="left">void *</td>
<td align="left">服务句柄，可传入 NULL</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">XP2PERRNONE</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">XP2PERR*</td>
<td align="left">失败，对应 <a href="https://cloud.tencent.com/document/product/1131/57611"> 错误码</a></td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 启动语音发送服务 */
void *req = runSendService($id, NULL, true);
/* 循环发送 */
while (1) {
	dataSend($id, audio_data, data_len);
	usleep(100 * 1000);
}
/* 停止发送服务 */
stopSendService(id, req);
:::
</dx-codeblock>


### P2P 通道传输自定义数据

#### 同步方式发送自定义数据

- 接口描述
  发送信令消息给 camera 设备并等待回复。同步阻塞方式。
```
int postCommandRequestSync(const char *id, const unsigned char *command, size_t cmd_len, unsigned char **recv_buf, size_t *recv_len, uint64_t timeout_us);
```
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">command</td>
<td align="left">const unsigned char *</td>
<td align="left">可以为任意格式字符或二进制数据</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">cmd_len</td>
<td align="left">size_t</td>
<td align="left">command 参数长度</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">recv_buf</td>
<td align="left">unsigned char **</td>
<td align="left">用于存放 camera 回复的数据</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">recv_len</td>
<td align="left">size_t *</td>
<td align="left">camera 回复的数据长度</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">timeout_us</td>
<td align="left">uint64_t</td>
<td align="left">命令超时时间，单位为微秒，值为0时采用默认超时（7500ms左右）</td>
<td align="left">输出</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">XP2PERRNONE</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">XP2PERR*</td>
<td align="left">失败，对应 <a href="https://cloud.tencent.com/document/product/1131/57611"> 错误码</a></td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
unsigned char *buf = NULL;
size_t len = 0;
/* 接收的数据填充在buf中，buf内存由SDK内部申请外部释放 */
int rc = postCommandRequestSync($id, "action=user_define&cmd=xxx",
sizeof(action=user_define&cmd=custom_cmd), &buf, &len, 2*1000*1000);
if (rc != 0) {
  printf("post command request with async failed:%d\n", rc);
}
/* 释放内存 */
delete buf;
:::
</dx-codeblock>

#### 异步方式发送自定义数据

- 接口描述
  发送信令消息给 camera 设备，不用等待回复。异步非阻塞方式。
```
int postCommandRequestWithAsync(const char *id, const unsigned char *command, size_t cmd_len);
```
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">command</td>
<td align="left">const unsigned char *</td>
<td align="left">可以为任意格式字符或二进制数据</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">cmd_len</td>
<td align="left">size_t</td>
<td align="left">command 参数长度</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">XP2PERRNONE</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">XP2PERR*</td>
<td align="left">失败，对应 <a href="https://cloud.tencent.com/document/product/1131/57611"> 错误码</a></td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 设置消息接收回调 */
setUserCallbackToXp2p(_av_data_recv, _msg_notify);
int rc = postCommandRequestWithAsync($id, "action=user_define&cmd=xxx", sizeof(action=user_define&cmd=custom_cmd));
if (rc != 0) {
  printf("post command request with sync failed:%d\n", rc);
}

/* SDK接收到消息后调用注册的回调 */
char* _msg_notify(const char *id, XP2PType type, const char* msg) {
    if (type == XP2PTypeCmd) {
      //处理返回结果
      //回调中应避免耗时操作
      //多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
    }
}
:::
</dx-codeblock>


### 主动关闭 P2P 通道

- 接口描述
  停止 XP2P 服务。
```
void stopService(const char *id);
```
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">const char *</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
 stopService($id);
:::
</dx-codeblock>


### 控制类消息回调

#### P2P 通道关闭回调

详情请参见 [控制类消息通知回调](#test21)。
- 示例代码
<dx-codeblock>
:::  Java
char* _msg_notify(const char *id, XP2PType type, const char* msg) {
    if (type == XP2PTypeDisconnect) {
      //p2p通道错误断开
      //回调中应避免耗时操作
      //多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
    }
}
:::
</dx-codeblock>

#### P2P 通道错误断开回调


详情请参见 [控制类消息通知回调](#test21)。
- 示例代码
<dx-codeblock>
:::  Java
char* _msg_notify(const char *id, XP2PType type, const char* msg) {
    if (type == XP2PTypeDisconnect) {
      //p2p通道错误断开
      //回调中应避免耗时操作
      //多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
    }
}
:::
</dx-codeblock>


#### 日志保存


详情请参见 [控制类消息通知回调](#test21)。
- 示例代码
<dx-codeblock>
:::  Java
char* _msg_notify(const char *id, XP2PType type, const char* msg) {
    if (type == XP2PTypeDisconnect) {
      //p2p通道错误断开
      //回调中应避免耗时操作
      //多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
    }
}
:::
</dx-codeblock>

#### P2P 探测失败


详情请参见 [控制类消息通知回调](#test21)。
- 示例代码
<dx-codeblock>
:::  Java
bool p2pReady = false;
bool p2pError = false;
char* _msg_notify(const char *id, XP2PType type, const char* msg) {
    if (type == XP2PTypeDetectError) {
      //多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
      //该回调触发后需要对p2p服务做重置处理

      p2pError = true;
    }
}

//事务处理
void sample() {
    int wait_cnt = 0;
    int ret = 0;

START:
    ret = startServiceWithXp2pInfo($id, $product_id, $device_name, $xp2p_info);
    if (ret < 0>) {
        printf("p2p start error\n");
        return;
    }

    while (!p2pReady) {
        if (p2pError || wait_cnt >= 20) {
            printf("p2p detect error\n");
            break;
        }
        wait_cnt++;
        usleep(100 * 1000);
        printf("waiting for p2p ready\n");
    }
    if (!p2pReady) {
        stopService($id);
        goto START;
    }

    startAvRecvService($id, $params, true);
    ...
    stopAvRecvService($id, NULL);
    stopService($id);
}
:::
</dx-codeblock>


####  P2P 探测成功


详情请参见 [控制类消息通知回调](#test21)。
- 示例代码
<dx-codeblock>
:::  Java
bool p2pReady = false;
bool p2pError = false;
char* _msg_notify(const char *id, XP2PType type, const char* msg) {
    if (type == XP2PTypeDetectReady) {
      //多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
      //该回调触发后才能进行p2p服务请求

      p2pReady = true;
    }
}

//事务处理
void sample() {
    int wait_cnt = 0;
    int ret = 0;

START:
    ret = startServiceWithXp2pInfo($id, $product_id, $device_name, $xp2p_info);
    if (ret < 0>) {
        printf("p2p start error\n");
        return;
    }

    while (!p2pReady) {
        if (p2pError || wait_cnt >= 20) {
            printf("p2p detect error\n");
            break;
        }
        wait_cnt++;
        usleep(100 * 1000);
        printf("waiting for p2p ready\n");
    }
    if (!p2pReady) {
        stopService($id);
        goto START;
    }

    startAvRecvService($id, $params, true);
    ...
    stopAvRecvService($id, NULL);
    stopService($id);
}
:::
</dx-codeblock>



## aar 库调用方法

接口详细说明请参见 [VideoSDK 接口说明](https://github.com/tencentyun/iot-link-android/blob/master/sdk/video-link-android/doc/VideoSDK接口说明.md)

###  用户回调

#### 媒体流数据接收回调

- 接口描述
  媒体流数据通知。该回调用于返回以裸流方式传输的媒体流数据。
<dx-codeblock>
:::  Java
fun avDataRecvHandle(id: String?, data: ByteArray?, len: Int)
{
	//媒体流数据接收
	//回调中应避免耗时操作
	//多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
}
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">data</td>
<td align="left">ByteArray</td>
<td align="left">接收到的媒体流数据</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">len</td>
<td align="left">Int</td>
<td align="left">接收到的媒体流数据长度</td>
<td align="left">输出</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

####  信令消息通知回调

- 接口描述
  信令消息通知。该回调用于返回以异步方式发送的信令请求结果。
<dx-codeblock>
:::  Java
fun commandRequest(id: String?, msg: String?)
{
	//信令消息通知
	//回调中应避免耗时操作
	//多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
}
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">msg</td>
<td align="left">String</td>
<td align="left">接收到的消息</td>
<td align="left">输出</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

#### P2P 连接异常断开通知回调

- 接口描述
  P2P 通道错误断开。该回调用于通知 P2P 连接异常状况。
<dx-codeblock>
:::  Java
private var isXp2pDisconnect: Boolean = false
private var isXp2pDetectReady: Boolean = false
private var isXp2pDetectError: Boolean = false

fun xp2pEventNotify(id: String?, msg: String?, event: Int)
{
    //p2p通道错误断开
    //回调中应避免耗时操作
    //多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理

    if (event == 1003) {
        isXp2pDisconnect = true
    } else if (event == 1004) {
        isXp2pDetectReady = true
    } else if (event == 1005) {
        isXp2pDetectError = true
    }
}
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">msg</td>
<td align="left">String</td>
<td align="left">附加消息</td>
<td align="left">输出</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

#### P2P 连接正常关闭通知回调

- 接口描述
 P2P 通道正常关闭回调。该回调用于通知媒体流传输完成。
<dx-codeblock>
:::  Java
fun avDataCloseHandle(id: String?, msg: String?, errorCode: Int)
{
	//p2p通道正常关闭
	//回调中应避免耗时操作
	//多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
}
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">msg</td>
<td align="left">String</td>
<td align="left">附加消息</td>
<td align="left">输出</td>
</tr>
<tr>
<td align="left">errorCode</td>
<td align="left">Int</td>
<td align="left">状态码</td>
<td align="left">输出</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

### 设置用户回调

- 接口描述
  设置用户回调函数。媒体流数据和控制类消息通过设置的回调函数返回。	
<dx-codeblock>
:::  Java
public static void setCallback(XP2PCallback cb)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">cb</td>
<td align="left">XP2PCallback</td>
<td align="left">P2P 回调函数类</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
class VideoActivity : XP2PCallback {
	...
	XP2P.setCallback(this)
    ...
}
:::
</dx-codeblock>


### P2P 通道初始化

- 接口描述
  初始化 XP2P 服务。
<dx-codeblock>
:::  Java
public static void startServiceWithXp2pInfo(String id, String product_id, String device_name, String xp2p_info)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">product_id</td>
<td align="left">String</td>
<td align="left">目标 camera 产品信息</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">device_name</td>
<td align="left">String</td>
<td align="left">目标 camera 设备名称</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">xp2p_info</td>
<td align="left">String</td>
<td align="left">XP2P 信息</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 从自建后台获取xp2p info */
String xp2p_info = getXP2PInfo(...)
/* 设置回调 */
XP2P.setCallback(this)
/* 初始化p2p */
XP2P.startServiceWithXp2pInfo($id, $product_id, $device_name, xp2p_info)
:::
</dx-codeblock>


### P2P 通道传输音视频裸流

####  启动裸流接收服务

- 接口描述
  向 camera 设备请求媒体流，异步回调方式。
<dx-codeblock>
:::  Java
public static void startAvRecvService(String id, String params, boolean crypto)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">params</td>
<td align="left">String</td>
<td align="left">直播（action=live）或回放（action=playback）参数</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">crypto</td>
<td align="left">boolean</td>
<td align="left">是否开启传输层加密</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

#### 停止裸流接收服务

- 接口描述
  停止裸流接收，并关闭接收服务。
<dx-codeblock>
:::  Java
public static int stopAvRecvService(String id, byte[] req)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">req</td>
<td align="left">byte[]</td>
<td align="left">服务句柄，当前版本传入 null</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">0</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">其他</td>
<td align="left">失败</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 设置回调函数 */
XP2P.setCallback(this)
/* 开始请求数据 */
XP2P.startAvRecvService($id, "action=live", true)
/* 接收到数据后回调被触发 */
override fun avDataRecvHandle(id: String?, data: ByteArray?, len: Int)
{
	//裸流数据处理
	//回调中应避免耗时操作
	//多路p2p传输场景需根据回传的`id`判断对应的p2p通道,以做相应处理
}
/* 停止接收 */
XP2P.stopAvRecvService($id, null)
:::
</dx-codeblock>


###  接收 FLV 音视频流并使用 ijkplayer 播放

- 接口描述
  获取本地代理 url。用于播放器直接通过 url 获取数据进行播放。
<dx-codeblock>
:::  Java
public static String delegateHttpFlv(String id)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">本地代理 url</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">null</td>
<td align="left">失败</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 加密方式观看直播(action=live)，回放(action=playback) */
val url = XP2P.delegateHttpFlv($id) + "ipc.flv?action=live"
/* 非加密方式观看直播(action=live)，回放(action=playback) */
val url = XP2P.delegateHttpFlv($id) + "ipc.flv?action=live&crypto=false"

mPlayer.dataSource = url
mPlayer.prepareAsync()
mPlayer.start()
:::
</dx-codeblock>

###  发送语音对讲数据

#### 启动语音发送服务

- 接口描述
  启动向 camera 设备发送语音或自定义数据服务。异步非阻塞方式。
<dx-codeblock>
:::  Java
public static void runSendService(String id, String params, boolean crypto)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">params</td>
<td align="left">String</td>
<td align="left">请求参数采用 <code>key1=value&amp;key2=value2</code> 格式，key不允许以下划线_开头，且 key 和 value 中间不能包含 <code>&amp;/+=</code> 特殊字符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">crypto</td>
<td align="left">boolean</td>
<td align="left">否开启传输层加密</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

####  发送数据

- 描述
  向 amera 备发送语音或自定义数据。
<dx-codeblock>
:::  Java
public static int dataSend(String id, byte[] data, int len)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">data</td>
<td align="left">byte[]</td>
<td align="left">要发送的数据内容</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">len</td>
<td align="left">int</td>
<td align="left">要发送的数据长度</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>

####  关闭语音发送服务

- 接口描述
  向 camera 设备发送语音或自定义数据。
<dx-codeblock>
:::  Java
public static int stopSendService(String id, byte[] req)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">req</td>
<td align="left">byte[]</td>
<td align="left">服务句柄，当前版本可传入 null</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">0</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">其他</td>
<td align="left">失败</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 开启语音发送服务 */
XP2P.runSendService($id, "", true)
while(!stop) {
    /* 采集语音数据并发送 */
    byte[] flvData = flvPacker.getFLV(data);
    XP2P.dataSend(deviceId, flvData, flvData.length);
}
/* 发送完成后停止服务 */
XP2P.stopSendService($id, null)
:::
</dx-codeblock>


### P2P 通道传输自定义数据

#### 同步方式发送自定义数据

- 接口描述
  发送信令消息给 camera 设备并等待回复。同步阻塞方式。
<dx-codeblock>
:::  Java
public static String postCommandRequestSync(String id, byte[] command, long cmd_len, long timeout_us)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">command</td>
<td align="left">byte[]</td>
<td align="left">可以为任意格式字符或二进制数据</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">cmd_len</td>
<td align="left">long</td>
<td align="left">command 参数长度</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">timeout_us</td>
<td align="left">long</td>
<td align="left">命令超时时间，单位为微秒，值为0时采用默认超时（7500ms左右）</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">camera 回复的数据</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">空值</td>
<td align="left">失败</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
val cmd = "action=inner_define&amp;cmd=xxx".toByteArray()
val ret = XP2P.postCommandRequestSync($id, cmd, cmd.size.toLong(), 2*1000*1000)
L.e("--------ret:----$ret--\n")
:::
</dx-codeblock>


#### 异步方式发送自定义数据

- 接口描述
  发送信令消息给 camera 设备，不用等待回复。异步非阻塞方式。
<dx-codeblock>
:::  Java
public static int postCommandRequestWithAsync(String id, byte[] command, long cmd_len)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">command</td>
<td align="left">byte[]</td>
<td align="left">可以为任意格式字符或二进制数据</td>
<td align="left">输入</td>
</tr>
<tr>
<td align="left">cmd_len</td>
<td align="left">long</td>
<td align="left">command 参数长度</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">0</td>
<td align="left">成功</td>
</tr>
<tr>
<td align="left">其他</td>
<td align="left">失败</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
/* 设置回调 */
XP2P.setCallback(this)
val cmd = "action=user_define&amp;cmd=xxx".toByteArray()
XP2P.postCommandRequestWithAsync($id, cmd, cmd.size.toLong())
override fun commandRequest(id: String?, msg: String?, len: Int)
{
	//处理回复消息
}
:::
</dx-codeblock>


### 主动关闭 P2P 通道

- 接口描述
  停止 XP2P 服务。	
<dx-codeblock>
:::  Java
public static void stopService(String id)
:::
</dx-codeblock>
- 参数说明
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">类型</th>
<th align="left">描述</th>
<th align="left">输入/输出</th>
</tr>
</thead>
<tbody><tr>
<td align="left">id</td>
<td align="left">String</td>
<td align="left">目标 camera 在 App 端的唯一标识符</td>
<td align="left">输入</td>
</tr>
</tbody></table>
- 返回值
<table>
<thead>
<tr>
<th align="left">返回值</th>
<th align="left">描述</th>
</tr>
</thead>
<tbody><tr>
<td align="left">void</td>
<td align="left">-</td>
</tr>
</tbody></table>
- 示例代码
<dx-codeblock>
:::  Java
override fun onDestroy() {
      super.onDestroy()
      mPlayer.release()
      XP2P.stopService($id)
}
:::
</dx-codeblock>




