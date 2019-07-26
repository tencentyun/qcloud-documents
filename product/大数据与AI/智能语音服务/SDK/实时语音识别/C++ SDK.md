实时语音识别 C++ SDK [下载地址](https://main.qcloudimg.com/raw/8635c3a453298b5a3fa47cb291c01e9d/c++_realtime_asr_sdk_v1.0.tar.gz )。

## 功能简介
语音识别（ASR）可以把音频数据转换为文本，需要持续对音频进行识别的场景，推荐使用实时语音识别，例如视频录制时候的实时字幕，语音对话机器人等。  
  
- 语言和方言：语音识别服务目前主语言仅支持中文普通话，可以识别有一定方言口音的普通话，支持在普通话中掺杂少量英文字母和单词。  
- 采样率和位深度：支持16bit、8k或者16k采样率的单声道或双声道的中文音频识别。
- 我们建议每300或者500毫秒发送一次音频，对此，客户端需要做一些必要的缓存逻辑。
- VAD（Voice Activity Detection）指对语音进行分段的技术，是算法通过对语音之间的停顿进行检测，判断用户说话间的的分句。
- voice_id 用于识别单次对话请求。如果用户持续说话一段时间，包含了很多句话，可以采用一个 voice_id 发送一系列的语音数据，seq 字段表示序号，从0开始。voice_id 不能重复，重复会导致识别错误。

例如，用户说：“今天天气好。”，大概2到3秒的时间。假设1秒发3个请求，则共计会发送8个左右的请求。服务器会返回相应个回包。类似于：
```
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":0,"text":"今"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":1,"text":"今天"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":2,"text":"今天"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":3,"text":"今天天气"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":4,"text":"今天天气好"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":5,"text":"今天天气好。"}
```

## 开发环境
首先编译 Demo，失败再去确认以下环境：
```
//下载sdk
tar -xzf c++_realtime_asr_sdk.tar.gz
cd c++_realtime_asr_sdk
make clean
make
//如果编译并未报错则跳过以下环境检测，否则可根据错误类型去校验库
```
**基本编译环境**
安装 gcc g++   

```
1.RedHat系列系统:
yum install -y gcc gcc-c++ make automake
//安装 gcc 等必备程序包（已安装则略过此步）
yum install -y wget

2.Debian系列系统：
apt-get install gcc g++
```
**安装 CMake 工具**
```
// cmake 版本要大于3.5
wget https://cmake.org/files/v3.5/cmake-3.5.2.tar.gz
tar -zxvf cmake-3.5.2.tar.gz
cd cmake-3.5.2
sudo ./bootstrap --prefix=/usr
sudo make
sudo make install
```
**依赖库安装及编译**
**curl**
客户需自行安装版本大于7.44.0：
下载 [curl 文件](https://curl.haxx.se/download.html) 解压进入源码目录
```
sudo ./configure
sudo cmake ./
sudo make
sudo make install
```
**openssl**
本 SDK 提供，目录为：c++_realtime_asr_sdk/lib
如果不适合客户系统，自行安装方法，版本1.0.2f:

下载 [wget 源码]( http://www.openssl.org/source/openssl-1.0.2f.tar.gz)。

```
1. 更新 zlib
RedHat系列:yum install -y zlib
Debian系列:sudo apt-get install zlib1g zlib1g.dev
2. 安装
tar zxf openssl-1.0.2f.tar.gz
cd openssl-1.0.2f
sudo ./config shared zlib
sudo make
sudo make install
自行替换 c++_realtime_asr_sdk/lib 下面的库文件
```

**speex**
本 SDK 提供，目录为：c++_realtime_asr_sdk/lib
如果不适合客户系统，自行安装方法：
下载 [speex 源码](https://speex.org/downloads/)。
解压进入源码目录
```
sudo ./configure
sudo make
sudo make install
自行替换 c++_realtime_asr_sdk/lib 下面的库文件
```
## <span id="result">获取用户信息</span>
**获取用户鉴权信息及申请使用**
- 使用本接口之前需要先 [注册](https://cloud.tencent.com/register) 腾讯云账号，获得 AppID，SecretID 及 SecretKey。  
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。
-  具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。
- 在 [语音识别](https://cloud.tencent.com/product/asr) 页面单击【立即使用】。这一步相当于注册，否则无法使用。

**配置用户信息**
**将 AppID、SecretId、SecretKey 配置到 SDK 中。**

```
#需要配置成用户账号信息 c++_realtime_asr_sdk/config/TCloudRealtimeASRConfig.ini
[tcloud_config]
#用户Appid
appid=1256******* 
#用户SecretId
secretid=AKID****************************
#用户SecretKey，此处若担心存在密钥泄露风险，可在调用接口中传入，参考接口文档
secretkey=670m***************************
```


## 开发相关
**请求参数** 

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| appid |  是 | Int | 用户在腾讯云注册账号的 AppID，具体可以参考  [获取用户信息](#result)。 |
| secretid | 是 | String | 用户在腾讯云注册账号 AppID 对应的 SecretId，获取方法同上。 |
| sub\_service\_type | 否 | Int | 子服务类型。1：实时流式识别。|
| engine\_model\_type | 否 | String | 引擎类型引擎模型类型。8k_0:8k 通用，16k_0:16k 通用，16k_en：16k英文。|
| result\_text\_format | 否 | Int | 识别结果文本编码方式。0：UTF-8；1：GB2312；2：GBK；3：BIG5|
| res_type | 否 | Int | 结果返回方式。1：同步返回；0：尾包返回。|
| voice_format | 否 | Int | 语音编码方式，可选，默认值为 4。1：wav（pcm）；4：speex（sp）；6：silk；8：mp3（仅16k_0模型支持）。|
| needvad | 否 | Int | 0为后台不做 vad 分段，1为后台做自动 vad 分段。 |
| seq | 是 | Int | 	语音分片的序号从0开始。|
| end | 是 | Int | 是否为最后一片，最后一片语音片为1，其余为0。 |
| source | 是 | Int | 设置为0 |
| voice_id | 是 | String | 16位 String 串作为每个音频的唯一标识，用户自己生成。|
| timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK会自动赋值当前时间戳。|
| expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK默认设置1小时。|
| timeout | 是 | Int | 设置超时时间单位为毫秒。|
| nonce | 是 | Int | 随机正整数。用户需自行生成，最长10位。|

**返回参数**

| 参数名称 |  描述 |  
| --- | --- |
| code |  0：正常，其他，发生错误。 |
| message | 如果是0就是 success，不是0就是错误的原因信息。 |
| voice_id | 表示这通音频的标记，同一个音频流这个标记一样。 |
| seq | 语音分片的信号。<br> 如果请求参数 needvad为0的话，表示不需要后台做 vad，这里的 seq 就是发送过来的 seq 的序号。<br>如果请求参数 needvad 为1，则表示需要后台做 vad，因后台做 vad ，vad 会重新分片，送入识别的 seq 会和发送过来的 seq 不一样，这里返回的 seq 就为0 。|
| text |  如果请求参数 needvad 为0的，表示不需要后台做 vad，text 的值是分片的识别结果。<br>如果请求参数 needvad 为1的话，表示需要后台做 vad，因为后台做 vad 的话，vad 会重新分片，送入识别的 seq 会和发送过来的 seq 不一样，text 为"" 。|
| result_number | 请求参数needvad=1， 此字段有效<br>result_number表示后面的 result_list 里面有几段结果，如果是0表示没有结果，可能是遇到中间是静音了。<br>如果是1表示 result\_list 有一个结果， 在发给服务器分片很大的情况下可能会出现多个结果，正常情况下都是1个结果。 |
| result_list | 请求参数needvad=1， 此字段有效 <br>slice\_type: 返回分片类型标记， 0表示一小段话开始，1表示在小段话的进行中，2表示小段话的结束<br>index 表示第几段话<br>start\_time  当前分片所在小段的开始时间（相对整个音频流）。<br>end\_time 当前分片在整个音频流中的结束时间。<br>voice\_text_str 识别结果。 |
| final | 0 表示还在整个音频流的中间部分。<br>1 表示是整个音频流的最后一个包。<br>例如在电信电话场景中，是否是客户端发送的最后一个包的识别结果。 |

**请求 url 参数示例**

```
http://asr.cloud.tencent.com/asr/v1/125000001?
end=0&
engine_model_type=16k_0&
expired=1558016577&
nonce=434303218&
res_type=0&
result_text_format=0&
secretid=XXXXXXXXXXXXXXXXXXXXXXX&
needvad=1&
seq=0&
source=0&
sub_service_type=1&
timeout=5000&
timestamp=1558010577&
voice_format=1&
voice_id=82510017d7deb33e
```
其中v1表示 API 的版本，v1.0，后面125000001是 AppID，各个参数的说明参考上表。

**接口说明**
**TCloudRealtimeASR::Init**
```
/* 
** 初始化公共请求参数，此类参数较稳定不变
** config 公共请求参数结构体
** Output int 返回结果
*/
int Init(TCloudRealtimeASRConfig config);
```
**TCloudRealtimeASR::SetSecretKey**
```
/* 
** 设置用户密钥
** strSecretKey 用户密钥
** Output int 返回结果
*/
int SetSecretKey(string strSecretKey);
```
** TCloudRealtimeASR::BuildRequest**
```
/* 
** 构造一个完整的请求
** Output int 返回结果
*/
int BuildRequest();
```
**TCloudRealtimeASR::SetData**
```
/* 
** 传入语音数据
** pPCMData pcm格式语音数据
** length 音频长度，字节
** voiceID 音频对应的voice_id
** seq 音频序号，含义参考参数
** bEnd 是否是最后一片
** Output TCloudRealtimeASRResponse 返回结果
*/
TCloudRealtimeASRResponse SetData(char* pPCMData, int length, string voiceID, int seq, bool bEnd);
```
**TSpeexEncoder::Encode**
```
/* 
** pcm格式音频speex压缩
** inputBuffer 需压缩音频数据
** inputSize 需压缩音频长度 字节
** strRsp 压缩完成的音频串
** Output bool 返回结果
*/
bool Encode(const char* inputBuffer, int inputSize, string& strRsp);
```
**请求 demo**
```
//首先确认./bin/test.wav是否存在
make
./run.sh 
```

**简单开发流程介绍**

**初始化请求参数** 
调用 Init 接口初始化请求参数  
请参考接口2.1
**设置用户密钥**  
调用 SetSecretKey 接口设置密钥  
请参考接口2.2
**(可选）Speex 压缩**
调用 TSpeexEncoder::Encode 接口对 pcm 格式音频压缩  
建议选择压缩，减少带宽
**传入音频数据**
调用 SetData 接口获取结果  
**SDK 已提供各个接口源码，用户可根据自身需要进行更改。**
## C++ 快速入门示例
参考 c++_realtime_asr_sdk/src/demo.cpp  
此例子为 speex 压缩请求，建议使用 speex 压缩方式，减少带宽。

```
int RunRealtimeASR()
{
	TCloudRealtimeASR realtimeASR;
	int ret = realtimeASR.Init("./config/TCloudRealtimeASRConfig.ini");
	if(ret != 0)
	{
		printf("Realtime ASR Init Error, Code:%d\n", ret);
		return ret;
	}

	FILE* fp = fopen("bin/test.wav", "rb");
	if (fp == NULL)
	{
		printf("file open failed\n");
	}

	char* buffer = new char[FILE_BUFFER_LEN];
	int seq = 0;
	string voiceID = GetVoiceID();
	TSpeexEncoder encoder;
	encoder.Init();
	string strSpeex = "";
	while(!feof(fp))
	{
		memset(buffer, 0, FILE_BUFFER_LEN);
		int readLength = fread(buffer, 1, FILE_BUFFER_LEN, fp);
		if(realtimeASR.GetVoiceFormat() == "4"){
			if(seq == 0){
				encoder.Encode(buffer + 44, readLength - 44, strSpeex);
			}else{
				encoder.Encode(buffer, readLength, strSpeex);
			}
		}
		TCloudRealtimeASRResponse response = realtimeASR.SetData((char*)strSpeex.c_str(), strSpeex.size(), voiceID, seq, readLength != FILE_BUFFER_LEN);
		seq++;
	}

	delete[] buffer;
	buffer = NULL;
	fclose(fp);
	return 0;
}
```
