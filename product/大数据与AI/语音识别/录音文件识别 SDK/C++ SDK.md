
录音文件识别 C++ SDK [下载地址](https://main.qcloudimg.com/raw/d138ccce115b3821a86dbe3768ac1a85/c++_record_asr_sdk_v1.0.tar.gz)。

## 功能简介
- 录文件识别适用于多种标准语音格式的长段语音文件，通常应用于对识别结果返回时延要求不高的场景。目前支持的采样率为 8K 和 16K，仅支持中文。可以应用于客服语音记录质检、UGC 音频审核、会议语音记录转写和医生就诊录音转写等场景。 
- 语言和方言：语音识别服务目前主语言仅支持中文普通话，可以识别有一定方言口音的普通话，支持在普通话中掺杂少量英文字母和单词。   
- 音频格式支持：支持16bit、8k或者16k采样率的单声道或双声道的中文音频识别；支持音频格式为 wav、pcm、mp3、silk、speex、amr。  
- 音频数据长度支持：若采用直接上传音频数据方式，则音频数据不能大于5M，若采用上传 url 方式，则音频时长不能大于1小时。

>!如超出当天免费策略上限，您可以提交工单 [联系我们](https://cloud.tencent.com/about/connect) 处理。
　　

## 开发环境
首先编译 Demo，失败再去确认以下环境：
```
//下载sdk
tar -xzf c++_record_asr_sdk.tar.gz
cd c++_record_asr_sdk
make clean
make
//如果编译并未报错则跳过以下环境检测，否则可根据错误类型去校验库
```
**基础编译环境**
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
下载 [curl 文件](https://curl.haxx.se/download.html) 解压进入源码目录。
```
sudo ./configure
sudo cmake ./
sudo make
sudo make install
```
**openssl**
本 SDK 提供，目录为：c++_record_asr_sdk/lib
如果不适合客户系统，自行安装方法，版本1.0.2f:
下载 [wget 源码](http://www.openssl.org/source/openssl-1.0.2f.tar.gz) 。
```
1.更新zlib
RedHat系列:yum install -y zlib
Debian系列:sudo apt-get install zlib1g zlib1g.dev
2.安装
tar zxf openssl-1.0.2f.tar.gz
cd openssl-1.0.2f
sudo ./config shared zlib
sudo make
sudo make install
自行替换 c++_record_asr_sdk/lib 下面的库文件
```
## <span id="result">获取用户信息</span>
**获取用户鉴权信息及申请使用**
- 使用本接口之前需要先 [注册腾讯云账号](https://cloud.tencent.com/register) ，获得 AppID，SecretID 及 SecretKey。 并在 [语音识别](https://cloud.tencent.com/product/asr) 页面单击【立即使用】。
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。    
- 具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。

**配置用户信息**
**将 AppID、SecretId、SecretKey 配置到 SDK 中**。

```
#需要配置成用户账号信息 c++_record_asr_sdk/config/TCloudRecordASRConfig.ini
[tcloud_config]
#用户Appid
appid=1256******* 
#用户SecretId
secretid=AKID****************************
#用户SecretKey，此处若担心存在密钥泄露风险，可在调用接口中传入，参考接口文档
secretkey=670m***************************
```


## 开发相关
**参数说明**
**请求参数**

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| appid |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| secretid | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| sub\_service\_type | 否 | Int | 子服务类型。0：离线语音识别。|
| engine\_model\_type | 否 | String | 引擎类型。8k_0：电话 8k 通用模型；16k_0：16k 通用模型；8k_6: 电话场景下单声道话者分离模型。 |
| res\_text\_format | 否 | Int | 识别结果文本编码方式。0：UTF-8；1：GB2312；2：GBK；3：BIG5。|
| res_type | 否 | Int | 结果返回方式。0：同步返回；1：异步返回。目前只支持异步返回。|
| callback_url | 是 | String | 回调 URL，用户接受结果，长度大于0，小于2048。回调服务需用户自己实现。 |
| channel_num | 否 | Int | 语音声道数，仅在电话 8k 通用模型下，支持 1 和 2，其他模型仅支持 1。 |
| source_type | 是 | Int | 语音数据来源。0：语音 URL；1：语音数据（post body）。 |
| url | 否 | String | 语音 URL，公网可下载。当 source_type 值为0时须填写该字段，为1时不填；URL 的长度大于0，小于2048。 |
| timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK 会自动赋值当前时间戳。|
| expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK 默认设置1小时。|
| nonce | 是 | Int | 随机正整数。用户需自行生成，最长10位。|

**请求 url 参数示例**
```
https://aai.qcloud.com/asr/v1/125000001?engine_model_type=0
&expired=1473752807
&nonce=44925
&projectid=0
&res_text_format=0
&res_type=1
&secretid=<secretid>
&source_type=0
&sub_service_type=0
&timestamp=1473752207
&url=<url>
&callback_url=<callback_url>
```
```
headers:
{
"Content-Type":"application/octet-stream",
"Authorization":"UyKZ+Q4xMbdu3gxOmPD7tgnAm1A="
}
```
其中v1表示 API 的版本，v1.0，后面125000001是 AppID，各个参数的说明参考上表。
**返回参数**
离线语音识别的 RESTful API 请求返回结果如下表所示：

| 参数名称 | 类型 | 描述 |  
| --- | --- | --- |
| code |  Int | 服务器错误码，0为成功 |
| message |  String | 服务器返回的信息 |
| requestId |  Int | 如果成功，返回任务 ID |

**结果回调**  
当语音识别系统完成识别后，会将结果通过 HTTP POST 请求的形式通知到用户，用户需要在自身业务服务器上搭建服务接收回调。语音识别系统通过回调接口形式将识别结果回调通知客户，接口 Body 各字段说明如下：

| 字段 | 类型 | 描述 |  
| --- | --- | --- |
| code |  Int | 服务器错误码，0 为成功，其他：失败 |
| message |  String | 成功或者失败原因文字描述 |
| requestId |  Int | 请求 ID，与后台任务 ID 一一对应 |
| appid |  Int | 腾讯云应用 ID |
| projectid |  Int | 腾讯云项目 ID |
| audioUrl |  String | 语音下载 ur。如果语音源非公网可下载 URL，则不包含该字段 |
| text |  String | 识别出的结果文本 |
| audioTime |  Double | 语音总时长 |  

**客户端确认返回**  
用户业务服务器在接收到语音识别系统发起的 HTTP POST 回调请求后，需要按照如下约定，返回结果：

| 参数名称 | 类型 | 描述 |  
| --- | --- | --- |
| code |  Int | 错误码，0 为成功，其他值代表失败 |
| message |  String | 失败原因说明，例如业务服务器过载。 如果业务服务器返回失败，会间隔一段时间重新通知 |

**接口说明**  
**<span id="init"></span>TCloudRecordASR::Init**
```
/* 
** 初始化公共请求参数，此类参数较稳定不变
** config 公共请求参数结构体
** Output int 返回结果
*/
int Init(TCloudRecordASRConfig config);

/* 
** 初始化公共请求参数，此类参数较稳定不变
** strPath 配置文件路径
** Output int 返回结果
*/
int Init(TCloudRecordASRConfig strPath);
```
**<span id="SetSecretKey">TCloudRecordASR::SetSecretKey</span>**
```
/* 
** 设置用户密钥
** strSecretKey 用户密钥
** Output int 返回结果
*/
int SetSecretKey(string strSecretKey);
```
**TCloudRecordASR::BuildRequest**
```
/* 
** 构造一个完整的请求
** Output int 返回结果
*/
int BuildRequest();
```
**<span id="setdata">TCloudRecordASR::SetData</span>**
```
/* 
** 传入语音数据
** pPCMData pcm格式语音数据
** length 音频长度，字节
** Output int 返回结果
*/
int SetData(char* pPCMData, int length);
```
**<span id="seturl">TCloudRecordASR::SetUrl</span>**
```
/* 
** 设置可以获取音频的URL
** strAudioURL 音频url
** Output int 返回结果
*/
int SetUrl(string strAudioURL);
```
**<span id="setfile">TCloudRecordASR::SetFile</span>**
```
/* 
** 添加音频文件
** strFile 音频文件路径
** Output int 返回结果
*/
int SetFile(string strFile);
```
**CServerConf::ParseFile()**
```
/* 
** 初始化配置文件
** szConfigFile 文件路径
** Output int 返回结果
*/
int ParseFile(const char* szConfigFile);
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
make
./run.sh
```

**简单开发流程介绍**
**初始化请求参数**  
调用 Init 接口初始化请求参数。  
参考接口 [TCloudRecordASR::Init](#init)。
**设置用户密钥**
调用 SetSecretKey 接口设置密钥。  
参考接口 [TCloudRecordASR::SetSecretKey](#SetSecretKey)。
**传入音频获取结果**
方法一：传入音频 URL 建议使用  
调用 SetUrl 接口获取结果，对应参数设置为 url 模式。
参考接口 [TCloudRecordASR::SetUrl](#setdata)。
方法二：音频数据  
调用 SetData 或者 SetFile 接口获取结果，对应配置参数为 post 音频。  
参考接口 [TCloudRecordASR::SetData](#seturl) 与 [TCloudRecordASR::SetFile](#setfile)。
**SDK 已提供各个接口源码，用户可根据自身需要进行更改。**

## 错误码
**请求错误码**  

|数值	|返回码 |	说明|
| --- | --- | --- |
|1000	|ERROR\_BAD\_REQ	|请求的参数不符合要求|
|1001	|ERROR\_PARSE\_DATA\_FAILED	|解析请求参数时失败|
|1002	|ERROR\_HAS\_NO\_VALID\_PROJECTID	|没有提供 projectid，或者值不合法|
|1003	|ERROR\_HAS\_NO\_VALID\_RES\_TEXT\_FORMAT |没有提供 res\_text\_format，或者值不合法|
|1004	|ERROR\_HAS\_NO\_VALID\_SUB\_SERVICE\_TYPE |没有提供 sub\_service\_type，或者值不合法|
|1005	|ERROR\_HAS\_NO\_VALID\_ENGINE\_MODEL\_TYPE|没有提供 engine\_model\_type，或者值不合法|
|1006	|ERROR\_HAS\_NO\_VALID\_CALLBACK\_URL	|没有提供 callback\_url，或者值不合法|
|1007	|ERROR\_HAS\_NO\_VALID\_RES\_TYPE	|没有提供 res\_type，或者值不合法|
|1008	|ERROR\_HAS\_NO\_VALID\_SOURCE\_TYPE	|没有提供 source\_type，或者值不合法|
|1009	|ERROR\_HAS\_NO\_VALID\_URL	|没有提供下载语音的 url，或者值不合法|
|1010	|ERROR\_HAS\_NO\_VALID\_SECRET\_ID	|没有提供 SecretId，或者值不合法|
|1011	|ERROR\_HAS\_NO\_VALID\_TIMESTAMP	|没有提供 timestamp，或者值不合法|
|1012	|ERROR\_HAS\_NO\_VALID\_EXPIRED	|没有提供 expired，或者值不合法|
|1013	|ERROR\_HAS\_NO\_VALID\_NONCE	|没有提供 nonce，或者值不合法|
|1014	|ERROR\_HAS\_NO\_VALID\_TEMPLATENAME	|提供的 template\_name 不合法|
|1015	|ERROR\_HAS\_NO\_BUCKET	|没有提供 bucket，或者值不合法|
|1016	|ERROR\_HAS\_NO\_AMOUNT	|没有剩余的免费用量|
|1017	|ERROR\_URL\_TOO\_LONG	|提供的 url 长度大于 2048|
|1018	|ERROR\_FILEID\_TOO\_LONG	|提供的文件名长度大于 2048|
|1019	|ERROR\_APPID\_NOT\_REGISTER	|提供的 APPID 未注册|
|1020	|ERROR\_APPID\_PROJECTID\_TEMPLATENAME\_MISMATCH	|提供的 APPID，ProjectId 与 template\_name 不匹配|
|1021	|ERROR\_PROCESS\_FAILED	|服务端处理出现内部错误|
|1022	|ERROR\_PROXY\_BAD\_AUTH	|签名不符合规则|
|1024	|ERROR\_PROXY\_AUTH\_TOO\_LONG\_EXPIRED	|签名的有效期设置太长|
|1025	|ERROR\_PROXY\_AUTH\_EXPIRED	|签名过期|
|1026	|ERROR\_PROXY\_AUTH\_PROJECTID\_NOEXIST	|签名中的 ProjectId 错误|
|1027	|ERROR\_PROXY\_AUTH\_SECRETID\_NOEXIST	|签名中的 SecretId 错误|
|1028	|ERROR\_PROXY\_AUTH\_PROJECTID\_MISMATCH	|签名中的 ProjectId 不匹配|
|1029	|ERROR\_PROXY\_AUTH\_REPLAY\_ATTACK	|重放攻击|
|1030	|ERROR\_PROXY\_AUTH\_FAILED	|签名验证不通过|
|1032	|ERROR\_AUDIO\_TOO\_LARGE	|发送的语音数据过大（大于 5M）|
|1034	|ERROR\_UNKNOWN	|其他未知错误|

**回调错误码**

| 数值 |  说明 |  
| --- | --- |
| 10000 | 语音非标准格式，转码失败 |
| 10001 | 识别不成功 |
| 10002 | 语音时长过长 |
| 10003 | 语音时长过长 |
| 10004 | 无效的语音文件 |
| 10005 | 其他失败 |
| 10006 | 音轨个数不匹配 |

## C ++ 快速入门示例
参考 c++_record_asr_sdk/src/demo.cpp  
```
int RunReacordASR()
{
	TCloudRecordASR recordASR;
	int ret = recordASR.Init("./config/TCloudRecordASRConfig.ini");
	
	if(ret != 0)
	{
		printf("Record ASR Init Error, Code:%d\n", ret);
		return ret;
	}

	string strURL = "https://test-audio-1256085166.cos.ap-guangzhou.myqcloud.com/123.wav";
	recordASR.SetUrl(strURL);
	TCloudRecordASRResponse response = recordASR.Run();
	return 0;
}
```





