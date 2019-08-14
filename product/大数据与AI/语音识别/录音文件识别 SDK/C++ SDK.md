## 1. 接入准备
### 1.1 SDK 获取
录音文件识别 C++ SDK 以及 Demo 的下载地址：[C++ SDK](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/c%2B%2B_record_asr_sdk.tar.gz)。

### 1.2 接入须知
开发者在调用前请先查看录音文件识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/35721) ，了解接口的**使用要求**和**使用步骤**。
### 1.3 开发环境
+ **编译 Demo**，如失败需确认以下环境：
```
//下载sdk
tar -xzf c++_record_asr_sdk.tar.gz
cd c++_record_asr_sdk
make clean
make
//如果编译并未报错则跳过以下环境检测，否则可根据错误类型去校验库
```
+ **安装 gcc、g++**   
```
1.RedHat系列系统:
yum install -y gcc gcc-c++ make automake
//安装 gcc 等必备程序包（已安装则略过此步）
yum install -y wget
	
2.Debian系列系统：
apt-get install gcc g++
```
+ **安装 CMake 工具**
```
// cmake 版本要大于3.5
wget https://cmake.org/files/v3.5/cmake-3.5.2.tar.gz
tar -zxvf cmake-3.5.2.tar.gz
cd cmake-3.5.2
sudo ./bootstrap --prefix=/usr
sudo make
sudo make install
```
+ **依赖库安装及编译**
客户需自行安装版本大于7.44.0的**curl**。下载 [curl 文件](https://curl.haxx.se/download.html)，解压并进入源码目录执行如下命令：
	
```
sudo ./configure
sudo cmake ./
sudo make
sudo make install
```
+ **openssl**
本 SDK 会提供，目录为：c++\_record\_asr\_sdk/lib。如果不适合客户系统，请客户自行安装方法，版本1.0.2f，下载地址: [wget 源码](http://www.openssl.org/source/openssl-1.0.2f.tar.gz) 。
	
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

## 2. 快速接入
### 2.1 开发流程介绍
**配置用户信息**
+ 进入[ API 密钥管理页面 ](https://console.cloud.tencent.com/cam/capi)获取 AppID、SecretId、SecretKey 信息，并按如下步骤配置用户信息和请求 URL 参数。
	
	```
	#需要配置成用户账号信息 c++_realtime_asr_sdk/config/TCloudRealtimeASRConfig.ini
	[tcloud_config]
	#用户Appid
	appid=1256******* 
	#用户SecretId
	secretid=AKID****************************
	#用户SecretKey，此处若担心存在密钥泄露风险，可在调用接口中传入，参考下面的“设置用户密钥”
	secretkey=670m***************************
	#需要配置成用户实际的参数，参见接口说明中的请求 URL 参数说明
	[tcloud_asr]
	projectid=0
	sub_service_type=0
	engine_model_type=16k_0
	callback_url=http://www.qq.com
	source_type=0
	channel_num=1
	res_text_format=0
	res_type=0
	```

**初始化请求参数**  
+ 调用 Init 接口初始化请求参数。  
+ 参考接口 [TCloudRecordASR::Init](#init)。

**设置用户密钥**    
+ 调用 SetSecretKey 接口设置密钥。  
+ 参考接口 [TCloudRecordASR::SetSecretKey](#SetSecretKey)。

**传入音频获取结果**  
+ **方法一：传入音频 URL(建议使用)**  
调用 SetUrl 接口获取结果，对应参数设置为 url 模式。
参考接口 [TCloudRecordASR::SetUrl](#setdata)。   
+ **方法二：传入音频数据**  
调用 SetData 或者 SetFile 接口获取结果，对应配置参数为 post 音频。  
参考接口 [TCloudRecordASR::SetData](#seturl) 与 [TCloudRecordASR::SetFile](#setfile)。

**SDK 已提供各个接口源码，用户可根据自身需要进行更改。**

### 2.2 主要接口方法说明
 
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
### 2.3 入门示例
参考 c++\_record\_asr\_sdk/src/demo.cpp  
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

	/* 本地文件
	FILE* fp = fopen("bin/test.wav", "rb");
	if (fp == NULL)
	{
		printf("file open failed\n");
	}

	char* buffer = new char[FILE_BUFFER_LEN];
	int seq = 0;
	
	memset(buffer, 0, FILE_BUFFER_LEN);
	int readLength = fread(buffer, 1, FILE_BUFFER_LEN, fp);
	
	recordASR.SetData(buffer, readLength);
	
	TCloudRecordASRResponse response = recordASR.Run();
	*/
	return 0;
}
```
