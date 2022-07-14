腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。腾讯 TTS 技术可以应用到很多场景，例如，移动 App 语音播报新闻；智能设备语音提醒；支持车载导航语音合成的个性化语音播报。本接口内测期间免费使用。  

流式语音合成 C++ SDK [下载地址](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/tts/c%2B%2B_stream_tts_sdk.zip)。
>! 此 SDK 目前仅支持在 Linux 平台上使用。 
>
接口请求域名：`tts.cloud.tencent.com/stream`   

## 开发环境
### 编译静态库
先编译静态库，如果报错，再检查后续依赖库。
```
//下载后解压
tar -xzf c++_stream_tts_sdk.zip
cd c++_stream_tts_sdk
cmake ./
//编译静态库和测试demo可执行文件
//demo可执行文件在bin目录下，可直接运行测试demo
//生成的库文件在lib目录下
make
//链接所有依赖静态库生成tts sdk，之后开发直接链接此库即可
cd lib
./build
```

### 基础编译环境
安装 gcc g++。
```
yum install -y gcc gcc-c++ make automake
//安装 gcc 等必备程序包（已安装则略过此步）
yum install -y wget
```

### 安装 CMake 工具
```
// cmake 版本要大于3.5
wget https://cmake.org/files/v3.5/cmake-3.5.2.tar.gz
tar -zxvf cmake-3.5.2.tar.gz
cd cmake-3.5.2
./bootstrap --prefix=/usr
gmake
gmake install
```

### 安装及编译依赖库
- **curl** 需要客户需自行安装，版本大于7.44.0。
下载 [curl 文件](https://curl.haxx.se/download.html) 解压进入源码目录。
```
sudo ./configure
sudo cmake ./
sudo make
sudo make install
```
- **openssl** 由本文 SDK 提供，目录为 `c++_tts_sdk/lib`。若在您的系统不适合，可自行安装，版本 openssl-1.0.2f，下载 [wget 源码](http://www.openssl.org/source/openssl-1.0.2f.tar.gz)。
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
自行替换 c++_tts_sdk/extern/openssl_1.0.2f/lib下面的库文件
```
- **jsoncpp** 由本文 SDK 提供，目录为 `extern/json/lib`。存在64位版本和32位版本，客户可自行根据自身操作系统更换链接。
- **opus** 由本文 SDK 提供，目录为 `extern/opus`。若在您的系统不适合，可自行安装，下载 [opus 源码](https://www.opus-codec.org/downloads/) 解压进入源码目录。
```
sudo ./configure --prefix=/usr
sudo make
sudo make install
自行替换 c++_tts_sdk/extern/opus/lib下面的库文件
```

[](id:result)
## 获取用户信息
### 获取 AppID、SecretId 和 SecretKey
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 和 SecretKey。 
- 登录您的 [腾讯云控制台](https://console.cloud.tencent.com/) 账号，鼠标悬停到右上角账号名称处，选择【访问管理】>【访问密钥】>【API 密钥管理】，即可查看 AppID、SecretId 和 SecretKey。

### 更改用户信息配置文件
将查询到的用户信息更改到 `conf/tcloud_auth.ini` 配置文件中。
```
用户需要替换成自己账号信息
AppId=1259*********
SecretId=AKIDo***************************
SecretKey=kFpw***************************
```

## 开发相关
### 请求参数

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| Action |  是 | String | 本接口取值：TextToStreamAudio，不可更改。 |
| AppId  |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| SecretId | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| Text | 是 | String | 合成语音的源文本。中文最大支持600个汉字（全角标点符号算一个汉字），英文最大支持1800个字母（半角标点符号算一个字母）。包含空格等字符时，需要 URL encode 再传输。|
| SessionId | 是 | String | 一次请求对应一个 SessionId，会原样返回，建议传入类似于 uuid 的字符串防止重复。|
| ModelType | 否 | Int | 模型类型，1：默认模型，此字段只需设置为1即可。|
| Volume | 否 | Float | 音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。没有静音选项。<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| Speed | 否 | Int | 语速，范围：[-2，2]，分别对应不同语速：<br>-2代表0.6倍 <br>-1代表0.8倍<br>0代表1.0倍（默认）<br>1代表1.2倍<br>2代表1.5倍<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| VoiceType | 否 | Int | 详见 [语音合成 API 文档中的 VoiceType 参数](https://cloud.tencent.com/document/product/1073/37995)。|
| PrimaryLanguage | 否 | Int | 主语言类型：<br>1：中文（默认）<br>2：英文 |
| SampleRate | 否 | Int | 音频采样率：<br>16000：16k（默认）<br>8000：8k |
| Codec | 否 | String | 返回音频格式：<br>opus：返回多段含 opus 压缩分片音频，数据量小，建议使用（默认）。<br>pcm：返回二进制 pcm 音频，使用简单，但数据量大。|
| ProjectId | 否 | Int | 项目 ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置，请填写默认项目 ID:0。 |
| Timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK 会自动赋值当前时间戳。|
| Expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK 默认设置1小时。|

**具体参数配置可以参考：conf/request_parameter.ini 的默认配置。**

### 请求接口
[](id:Param)
#### TCloudTTS::InitCommonParam
此接口用来初始化请求的公共请求参数，参数参考配置文件说明。路径为 `conf/request_parameter.ini`。
```
/* 初始化公共请求参数，此类参数较稳定不变
** configPath 参数文件路径
** time 鉴权的有效时间
** Output int 返回结果
*/
int InitCommonParam(string configPath);
```

[](id:InitAuth)
#### TCloudTTS::InitAuth
此接口用来初始化用户信息，参数参考配置文件说明。信息获取参考 [获取用户信息](#result)。路径为 `conf/tcloud_auth.ini`。
```
通过配置文件初始化，建议选择此接口
/* 初始化用户信息
** configPath 参数文件路径
** time 鉴权的有效时间
** Output int 返回结果
*/
int InitAuth(string configPath, int time = 60 * 60);

通过结构体初始化
/* 初始化用户信息
** stAuth 用户信息结构体
** time 鉴权的有效时间，默认为 1h
** Output int 返回结果
*/
int InitAuth(TCloudTTSAuth stAuth, int time = 60 * 60);
```

#### TCloudTTS::CreateRequest
此接口用来创建一个完整的请求信息。 
```
初始化公共参数后不需要更改则只需要通过text来创建请求，建议使用此接口：
/* 创建请求
** text 请求文本，不改变其他请求参数
** Output int 返回结果
*/
int CreateRequest(string text);

通过完整的请求参数信息来创建请求：
/* 创建请求
** stReq 完整的请求结构体信息
** Output int 返回结果
*/
int CreateRequest(TCloudTTSReq stReq);
```
 

#### TCloudTTS::RequestToJson
此接口将请求转换成 json body，在 post 时作 body 传到服务端。
```
/* 请求转换成 json
** stReq 请求结构体
** Output string json结果
*/
string RequestToJson(TCloudTTSReq stReq);
```


#### TCloudTTS::Process
此接口将执行一次请求。
```
/* 执行请求
** strRsp 请求的json body
** Output int 返回结果
*/
int Process(string &strRsp);
```

[](id:Split)
#### SplitString（可选功能）
此接口提供对文本进行标点切割功能。用户可选择使用，建议参考 demo 的思路。
```
/* 将文本根据标点符号切割
** strText 需要切割的原始文本
** model为标点符合的集合 例如：".,;!?"
** Out put 为切割完成的文本片
*/
vector<string> SplitString(string strText, string model);
```


### 请求 DEMO
前提已经更改用户正确的 AppId 信息。
```
cd bin
./tts_demo
```

以下存在多种方法的建议，选择方法一较优，其他方法供接入用户多选。

#### 创建请求 TCloudTTS ttsReq

1. 初始化用户信息  
 - 方法一（推荐此方法）：调用 InitAuth 通过配置文件初始化，默认路径 `conf/tcloud_auth.ini`。
 - 方法二：调用 InitAuth 通过 TCloudTTSAuth 结构体初始化。参考 [TCloudTTS::InitAuth](#InitAuth) 接口。
2. 初始化请求参数  
公共请求参数大多只需要设置一次，除了 Text、SessionId 参数。
 - 方法一（推荐此方法）：调用 InitCommonParam 通过配置文件 `conf/request_parameter.ini`。调用 CreateRequest 传入 Text。  
 - 方法二：通过完整的请求结构体来初始化请求。调用 InitCommonParam 通过 TCloudTTSReq 请求体来初始化。参考 [TCloudTTS::InitCommonParam](#Param) 接口。

#### 分片（可选功能）
>?初次接入不建议选择。

本 sdk 提供根据标点符号将整个文本进行分片的方法，通过调用 SplitString（Text）获取整个文本分片的结果，每片单独调用获取音频再合并。详见 [SplitString](#Split) 接口。

#### 执行任务
SDK 已提供各个接口源码，用户可根据自身需要进行更改。
```
调用 Process 函数获取音频结果，结果为 pcm 格式的音频串。  
结果存储在 TCloudTTS::m_strRsp;
```

## C++ 快速入门示例
参考 Demo/demo.cpp。
```
int main(){
    TCloudTTS tts;
    //初始化请求参数
    tts.InitCommonParam("./conf/request_parameter.ini");
    //初始化用户信息
    tts.InitAuth("./conf/tcloud_auth.ini");
    //文本过长可以自行切片，将返回strRsp合并即为完整音频
    //Text限制800字符以内
    string strRsp;
    int ret = 0;
    string strText = "尊敬的旅客您好，很抱歉的通知您：您在去哪网购买的2018年7月11日首尔到大连OZ301航班发生变动，最新的飞行计划为2018年7月11日9时35分的OZ301航班，从仁川国际机场起飞，2018年7月11日9时50分到达大连周水子国际机场，起降时间均为当地时间，我们已将详情发送至您的手机和邮箱，如需协助请拨打去哪网热线电话95117，谢谢。";
    
    //创建具体文本请求
    tts.CreateRequest(strText);
    ret = tts.Process(strRsp);
    
    //将 pcm 音频保存为 wave 格式
    FILE *f = fopen("./test.wav", "wb");
    unsigned char *wav_buffer = (unsigned char *) malloc(4 * 1024 * 1024);
    //添加 wave 头
    pcm16le_to_wave_buf((const int16_t *)strRsp.c_str(), strRsp.size(), 1, 16000, wav_buffer);
    fwrite(wav_buffer, sizeof(char), strRsp.size() + 44, f);
    fclose(f);
    free(wav_buffer);
    
    return 0
}
```


