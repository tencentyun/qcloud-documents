## 接入准备
### SDK 获取
录音文件识别 C++ SDK 以及 Demo 的下载地址：[C++ SDK](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/record/c%2B%2B_record_asr_sdk.zip)

### 接入须知
开发者在调用前请先查看录音文件识别的 [接口说明](https://cloud.tencent.com/document/product/1093/37139)，了解接口的**使用要求**和**使用步骤**。

### 开发环境
**需要64位 Linux 系统，如果用户使用的是32位系统，则需自行安装编译 extern 中的依赖库**。  

* 编译 demo，如果失败则参考对应的提示安装依赖工具。

```
//下载 sdk 并解压
unzip c++_record_asr_sdk.zip
cd c++_record_asr_sdk
cmake ./
make clean
make
//如果编译并未报错则跳过以下环境检测，否则可根据错误类型去校验库
```

* 安装 CMake 工具

```
// cmake 版本要大于3.5
wget https://cmake.org/files/v3.5/cmake-3.5.2.tar.gz
tar -zxvf cmake-3.5.2.tar.gz
cd cmake-3.5.2
sudo ./bootstrap --prefix=/usr
sudo make
sudo make install
```

* 安装 gcc g++

```
1.RedHat 系列系统:
yum install -y gcc gcc-c++ make automake
//安装 gcc 等必备程序包（已安装则略过此步）
yum install -y wget

2.Debian 系列系统：
apt-get install gcc g++
```

**编译安装 extern 依赖库（编译 demo 正常则跳过）**

* 安装 curl  [下载地址](https://curl.haxx.se/download.html)

```
解压，并进入目录
sudo ./configure
sudo cmake ./
sudo make
sudo make install
```

* 安装 openssl [下载地址](http://www.openssl.org/source/openssl-1.0.2f.tar.gz)

```
1.更新 zlib
RedHat 系列:yum install -y zlib
Debian 系列:sudo apt-get install zlib1g zlib1g.dev

2.安装
tar zxf openssl-1.0.2f.tar.gz
cd openssl-1.0.2f
sudo ./config shared zlib
sudo make
sudo make install
自行替换 c++_record_asr_sdk/lib 下面的库文件
```


## 快速接入
### 开发流程介绍
* 配置用户信息，进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 获取 AppID、SecretId、SecretKey 信息，并配置用户信息

```
#用户配置信息文件：tcloud_auth.ini
AppId=Your AppId
SecretId=Your SecretId
SecretKey=Your SecretKey
```

* 配置请求参数

```
#用户请求参数配置文件：request_parameter.ini
#引擎类型。
EngineModelType = 16k_zh
#语音声道数。1：单声道；2：双声道（仅在电话 8k 通用模型下支持）。
ChannelNum = 1
#识别结果文本编码方式。0：UTF-8。
ResTextFormat = 0
#语音数据来源。0：语音 URL；1：语音数据（post body）。
SourceType = 1 
#回调 URL，用户自行搭建的用于接收识别结果的服务器地址，长度小于2048字节。
CallbackUrl = http://test.qq.com
```

* 创建和初始化请求

```
//创建一个具体的请求
TCloudRecordASR asrReq;
//初始化请求参数
asrReq.InitCommonParam("./conf/request_parameter.ini");
//初始化用户信息
asrReq.InitAuth("./conf/tcloud_auth.ini");
```

* 传入音频发送请求，有本地音频上传和音频 URL 上传两种方式

```
//本地音频方式
//将sourcetype设置为1
asrReq.SetSourceType(1);
//传入本地音频文件路径
asrReq.CreateRecTask("./test.wav");
```

```
//音频URL方式
//将sourcetype设置为0
asrReq.SetSourceType(0);
//传入本地音频文件路径
asrReq.CreateRecTask("http://***.wav");
```

* 获取请求结果，支持轮询或者回调

```
//获取请求结果
string  taskRsp = asrReq.GetResponse();
//成功请求则返回 taskId,可根据 taskId 查询识别结果
```

* 查询识别结果（轮询方式）

```
//根据 taskId 轮询查询识别结果
string strRsp;
asrReq.DescribeTaskStatus(taskId, strRsp);
```

* 获取识别结果（回调方式）  

```
此方式需要客户自行搭建接收识别结果的服务，并将 服务 URL 传入参数 CallbackUrl
```

### 主要接口说明
**SDK 已提供各个接口源码，用户可根据自身需要进行更改。**  

* TCloudRecordASR::InitCommonParam

```
/* 初始化公共请求参数，此类参数较稳定不变
** configPath 参数文件路径
** time 鉴权的有效时间
** Output int 返回结果
*/
int InitCommonParam(string configPath);
```

* TCloudRecordASR::InitAuth

```
/* 初始化用户信息
** stAuth 用户信息结构体
** time 鉴权的有效时间
** Output int 返回结果
*/
int InitAuth(TCloudRecordASRAuth stAuth);

/* 初始化用户信息
** configPath 参数文件路径
** time 鉴权的有效时间
** Output int 返回结果
*/
int InitAuth(string configPath);
```

* TCloudRecordASR::SetSourceType

```
/* 设置 SourceType
** type 0 音频url， 1本地音频
** Output void
*/
void SetSourceType(int type);
```

* TCloudRecordASR::CreateRecTask

```
/* 创建识别请求
** fileURI 音频的本地地址或者音频的 URL 链接 
** Output int 返回结果
*/
int CreateRecTask(string fileURI);
```

* TCloudRecordASR::GetResponse

```
/* 获取任务结果
** Output string 任务返回 json 包
*/
string GetResponse();
```

* TCloudRecordASR::DescribeTaskStatus

```
/* 轮询查询识别结果
** taskId  任务 Id
** rsp   查询结果
** Output int 返回结果
*/
int DescribeTaskStatus(int taskId, string &rsp);
```

### 接入示例

```
//进入 demo 文件夹
//编译
./compile
//创建任务 参数：sourceType fileURI
./run_create_task 1 test.wav
//查询识别结果 参数：taskId
./run_describe_task 12345678
```
### 参考代码

#### 识别请求 demo
```
#include "TCloudRecordASR.h"
#include <iostream>

using namespace std;
int main(int argc, char ** argv){
    if(argc < 3){
        cout << "use ./run_create_task source_type uri" << endl;
    }
    int sourceType = atoi(argv[1]);
    string uri = string(argv[2]);
    TCloudRecordASR asrReq;
    //初始化请求参数
    asrReq.InitCommonParam("./conf/request_parameter.ini");
    //初始化用户信息
    asrReq.InitAuth("./conf/tcloud_auth.ini");
    asrReq.SetSourceType(sourceType);
    asrReq.CreateRecTask(uri);
    string  taskRsp = asrReq.GetResponse();
    cout << "rsp: " << taskRsp << endl;
    return 0;
}
```

#### 轮询查询结果 demo
```
#include "TCloudRecordASR.h"
#include <iostream>

using namespace std;
int main(int argc, char ** argv){
    if(argc < 2){
        cout << "use ./run_describe_task taskId" << endl;
    }
    int taskId = atoi(argv[1]);
    TCloudRecordASR asrReq;
    //初始化请求参数
    asrReq.InitCommonParam("./conf/request_parameter.ini");
    //初始化用户信息
    asrReq.InitAuth("./conf/tcloud_auth.ini");
    string strRsp;
    asrReq.DescribeTaskStatus(taskId, strRsp);
    cout << "rsp: " << strRsp << endl;
    return 0;
}

```
