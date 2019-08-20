## 开发准备
### 相关环境
一句话语音识别 [C++ SDK 下载地址>>](https://main.qcloudimg.com/raw/87702dcc907c1e9b9e270e8581181ddc/SASRsdk.zip)

### 环境依赖
C++ 编译器，可找相关开源软件下载即可。

### 安装 SDK
**源码安装**
根据下载地址下载源码，解压获得的压缩包得到如下图的文件和文件夹。
![](https://main.qcloudimg.com/raw/e9b0b58b1394d6ae2dad0aa41980977d.png)
本 SDK 源码放在 src 文件夹中：QCloudSASRApi.cpp，编译生成的静态库文件在lib文件夹中libSASRsdk.a。用户可将lib文件夹中的 libSASRsdk.a 静态库文件和 include 文件夹中的 QCloudSASRApi.h 放在项目中即可使用本 SDK。
如果需要使用本 SDK 直接测试，可使用 SASRtestdemo 文件夹中的文件进行测试，进入 SASRtestdemo 文件夹，可以看到如下文件与文件夹：
![](https://main.qcloudimg.com/raw/18ce86623856ec64aa1117778d242949.png)
Lib 文件夹中存放实时语音识别 SDK 的静态库文件，用户可以直接修改 src 文件夹中的 TestSASR.cpp，然后重新 make 得到新的 SASRtest 可执行程序。

### 卸载 SDK

卸载方式即删除相关 cpp 文件与静态库文件即可。
## 快速入门
```
//引用 SDK 头文件
#include "QCloudSASRApi.h"
#include"iostream"
using namespace std;

int main(int argc, const char * argv[]) {
　　string SecretId="AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5";
    string SecretKey="oaYWFO70LGDmcpfwo8uF1IInayysGtgZ";
    //8k or 16k
    string EngSerViceType="8k";
    //1 or 0
    string SourceType="1";
    //wav or mp3
    string VoiceFormat="wav";
    //string fileURI="http://liqiansunvoice-1255628450.cosgz.myqcloud.com/30s.wav";
    string fileURI="test.wav";
    QCloudSASRApi *sasrdemo=new QCloudSASRApi();
    bool configres=sasrdemo->SetQcloudConfig(SecretId,SecretKey,EngSerViceType,SourceType,VoiceFormat);
    if(configres==false){
    	cout<<"the params are wrong ,please check out.";
         return -1;
    }
    string pResponse;
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
