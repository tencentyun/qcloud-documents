## 开发准备
### 相关环境
实时语音识别 [C++ SDK下载地址>>](https://main.qcloudimg.com/raw/8557047f930c0f1198795cba7fa286c3/RASRsdk.zip)

### 环境依赖
C++ 编译器，找相关开源软件下载即可。

### 安装 SDK
**源码安装**
根据下载地址下载源码，解压获得的压缩包得到如下图的文件和文件夹。
![](https://main.qcloudimg.com/raw/79dac714b3bb7b7eb0f9ca725626251d.png)
本 SDK 源码放在 src 文件夹中：QCloudRASRApi.cpp，编译生成的静态库文件在 lib 文件夹中 libRASRsdk.a。用户可将 lib 文件夹中的 libRASRsdk.a 静态库文件和 include 文件夹中的 QCloudRASRApi.h 放在项目中即可使用本 SDK。
若想使用本 SDK 直接测试，可使用 RASRtestdemo 文件夹中的文件进行测试，进入 RASRtestdemo 文件夹，可以看到如下文件与文件夹：
![](https://main.qcloudimg.com/raw/ba0a1c3f373ec35887adaea157061f13.png)
Lib 文件夹中存放实时语音识别 SDK 的静态库文件，用户可以直接修改 src 文件夹中的 TestRASR.cpp，然后重新 make 得到新的 RASRtest可 执行程序。
### 卸载 SDK
卸载方式即删除相关 cpp 文件与静态库文件即可。
## 快速入门
```
//引用 SDK 头文件
#include "QCloudRASRApi.h"
#include"iostream"
using namespace std;

int main(int argc, const char * argv[]) {
　　//用户需修改为自己的Appid，SecretId，SecretKey
    string Appid ="1255628450";
    string SecretId ="AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8";
    string SecretKey ="kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP" ;

    //语音编码方式，可选，默认值为4,1.wav，4，sp，6.skil
    string VoiceFormat="1";

    //模板名称，填写为空字符串即可
    string TemplateName="";

    //音频识别引擎 8k_0 ,16k_0
    string EngineModelType="8k_0";

    //随包返回结果  0：是 1：否
    string ResType="0";

    //识别结果文本编码方式  0：UTF-8,1:GBK2312,2:GBK,3:BIG5
    string ResTextFormat="0";

    //超时时间
    string Timeout="20";
    QCloudRASRApi *rasrdemo=new QCloudRASRApi();
    bool configres=rasrdemo->SetQcloudConfig(Appid,SecretId,SecretKey,VoiceFormat,EngineModelType,ResType,ResTextFormat,TemplateName,Timeout);
    if(configres==false){
    	cout<<"the params are wrong ,please check out.";
        return -1;
     }
    string pResponse;
　　string fileURI="test.wav";

    //切片时间要小于200000
    int cutlength=8000;
    int res=rasrdemo->SendVoiceData(fileURI,pResponse,cutlength);
    if(res!=0){
    	cout<<"send voice data may have some wrong.";
        return -2;
    }
    //cout<<pResponse<<endl;
     delete rasrdemo;
     return 0;
}
```
