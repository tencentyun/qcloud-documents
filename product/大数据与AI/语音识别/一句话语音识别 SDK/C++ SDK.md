## 接入准备

### SDK 获取
一句话识别 C++ SDK 以及 Demo 的下载地址：[C++ SDK](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/c%2B%2B_sentence_sdk.tar.gz )。

### 接入须知
开发者在调用前请先查看一句话语音识别的[ 接口说明]()，了解接口的**使用要求**和**使用步骤**。


### 开发环境
**编译 Demo**，如失败需确认以下环境：

```
//下载sdk
tar -xzf c++_sentence_asr_sdk.tar.gz
cd c++_sentence_asr_sdk
cmake ./
make
//如果编译并未报错则跳过以下环境检测，否则可根据错误类型去校验库
``` 

**安装 gcc g++** 

```
1.RedHat 系列系统:
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

客户需自行安装版本大于7.44.0的 **curl**。下载 [curl 文件](https://curl.haxx.se/download.html)，解压并进入源码目录执行如下命令：  

```
sudo ./configure
sudo cmake ./
sudo make
sudo make install
```

**openssl**  
本 SDK 提供，目录为：c++_realtime\_asr\_sdk/lib。如果不适合客户系统，请客户自行安装方法，版本1.0.2f，下载 [wget 源码]( http://www.openssl.org/source/openssl-1.0.2f.tar.gz)并执行以下命令：

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

## 快速接入

### <span id="开发流程">开发流程介绍</span>
**配置用户信息**

+ 进入[ API 密钥管理页面 ](https://console.cloud.tencent.com/cam/capi)获取 AppID、SecretId、SecretKey 信息，并按如下步骤配置用户信息和请求 URL 参数。
	
```
//需要配置成用户账号信息 c++_sentence_asr_sdk/src/TCloudSASR.h
//请求的用户信息配置
struct TCloudSASRConfig{
	string SecretId; //对应用户的SecretId
	string SecretKey;//对应用户的SecretKey
	...
};
```

**初始化请求参数** 

+ 定义请求参数，具体参数参考请求参数说明。
+ 请参考 [ 接口说明]()

**设置用户密钥**  

+ 赋值用户的SecretId和SecretKey
+ 请参考 [ 开发流程介绍](#开发流程)

**初始化请求**

+ 调用 TCloudSASR::SetTCloudConfig 接口初始化请求
+ 请参考 [主要接口方法说明](#方法说明)

**发送请求并获取结果**

+ 调用 TCloudSASR::SendVoiceData 接口获取结果  
+ 请参考 [主要接口方法说明](#方法说明)

**SDK 已提供各个接口源码，用户可根据自身需要进行更改。**

### <span id="方法说明">主要接口方法说明</span>  
**TCloudSASR::SetTCloudConfig**

```
/*
*设置相关参数
*params：
*	  SecretId，SecretKey：官网获得的SecretId，SecretKey
*	  EngSerViceTyp：引擎类型引擎模型类型。8k:8k通用，16k:16k通用。
*	  SourceType：语音数据来源。0：语音 URL；1：语音数据（post body）
*	 VoiceFormat：识别音频的音频格式（mp3,wav）
*/
bool SetTCloudConfig(const string &SecretId, const string &SecretKey,const string &EngSerViceType="16k",const string &SourceType="0",const string &VoiceFormat="wav");
```

**TCloudSASR::SendVoiceData**

```
/*
* 发型音频数据
* params：
* fileURI：本地音频文件或者远程音频文件地址
* pResponse：识别结果
*
* */
int SendVoiceData(const string fileURI,string &pResponse);
```

**请求 demo**

```
//在sdk的根目录下执行
cd demo
make
./SASRtest
```

### 快速入门示例
```
//引用 SDK 头文件
#include "TCloudSASR.h"
#include"iostream"
using namespace std;

int main(int argc, const char * argv[]) {
	//重要：<Your SecretId>、<Your SecretKey>需要替换成客户自己的账号信息
   //请参考接口说明中的使用步骤1进行获取。 
	string SecretId="Your SecretId";
	string SecretKey="Your SecretKey";
	//8k or 16k
	string EngSerViceType="16k";
	//1 or 0
	//填1的时候URL可以设置为空
	string SourceType="0";
	//wav or mp3
	string VoiceFormat="wav";
	string fileURI="https://ruskin-1256085166.cos.ap-guangzhou.myqcloud.com/test.wav";
	//string fileURI="test.wav";
	TCloudSASR *sasrdemo=new TCloudSASR();

	//设置请求参数以及校验参数
	bool configres=sasrdemo->SetTCloudConfig(SecretId,SecretKey,EngSerViceType,SourceType,VoiceFormat);
	if(configres==false){
		cout<<"the params are wrong ,please check out.";
		return -1;
	}
	string pResponse;
	//发送请求并获取回包
	int res=sasrdemo->SendVoiceData(fileURI,pResponse);
	if(res!=0){
		cout<<"send voice data may have some wrong.";
		return -2;
	}
	cout<<pResponse<<endl;
	delete sasrdemo;
	return 0;
}
```
