## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0是云 API 3.0平台的配套工具。目前已经支持 CVM、VPC、CBS 等产品，后续所有的云服务产品都会陆续接入。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
本文主要介绍适用于 C++ 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 C++ 开发者快速掌握如何调试和接入腾讯云产品 API。

## 支持3.0版本的云产品列表

SDK 3.0支持全部 API 3.0下的云产品，本列表可能滞后于实际代码，如有疑问请咨询具体的云产品。

<table>
  <tr>
<td><a href="https://cloud.tencent.com/document/api/213/15689">云服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/386/18637">黑石物理服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/362/15634">云硬盘</a></td>
<td><a href="https://cloud.tencent.com/document/api/457/31853">容器服务</a></td>
<td><a href="https://cloud.tencent.com/document/api/858/17761">容器实例服务</a></td>
</tr>
<tr>
 <td><a href="https://cloud.tencent.com/document/api/377/20423">弹性伸缩</a></td>
  <td><a href="https://cloud.tencent.com/document/api/583/17235">云函数</a></td>
  <td><a href="https://cloud.tencent.com/document/api/599/15880">批量计算</a></td>
  <td><a href="https://cloud.tencent.com/document/api/214/30667">负载均衡</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15755">私有网络</a></td>
  </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/216/18404">专线接入</a></td>
  <td><a href="https://cloud.tencent.com/document/api/571/18122">数据传输服务 DTS</a></td>
 <td><a href="https://cloud.tencent.com/document/api/236/15830">云数据库 MySQL</a></td>
 <td><a href="https://cloud.tencent.com/document/api/239/20002">云数据库 Redis</a></td>
 <td><a href="https://cloud.tencent.com/document/api/240/31797">云数据库 MongoDB</a></td>
 </tr>
  <tr>
    <td><a href="https://cloud.tencent.com/document/api/237/16144">云数据库 MariaDB</a></td>
<td><a href="https://cloud.tencent.com/document/api/557/16124">分布式数据库 TDSQL</a></td>
 <td><a href="https://cloud.tencent.com/document/api/238/19927">云数据库 SQL Server</a></td>
  <td><a href="https://cloud.tencent.com/document/api/409/16761">云数据库 PostgreSQL</a></td>
   <td><a href="https://cloud.tencent.com/document/product/1130/39547">数据库智能管家 DBbrain</a></td>
   </tr>
   <tr>     
   <td><a href="https://cloud.tencent.com/document/product/596/39648">游戏数据库 TcaplusDB</a></td>
  <td><a href="https://cloud.tencent.com/document/api/692/16733">漏洞扫描服务</a></td>
   <td><a href="https://cloud.tencent.com/document/api/283/17742">移动应用安全</a></td>
   <td><a href="https://cloud.tencent.com/document/api/266/31753">云点播</a></td>
     <td><a href="https://cloud.tencent.com/document/api/267/20456">云直播</a></td>
   </tr>
   <tr>
<td><a href="https://cloud.tencent.com/document/api/1073/37986">语音合成</a></td>
<td><a href="https://cloud.tencent.com/document/api/1093/35637">语音识别</a></td>
 <td><a href="https://cloud.tencent.com/document/api/551/15612">机器翻译</a></td>
<td><a href="https://cloud.tencent.com/document/api/656/18281">催收机器人</a></td>
<td><a href="https://cloud.tencent.com/document/api/884/19310">智聆口语评测</a></td>
 </tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/1122/40639">企业收付平台</a></td>
  <td><a href="https://cloud.tencent.com/document/api/845/30620">Elasticsearch Service</a></td>
<td><a href="https://cloud.tencent.com/document/api/382/38764">短信</a></td>
<td><a href="https://cloud.tencent.com/document/api/634/19469">物联网通信</a></td>
<td><a href="https://cloud.tencent.com/document/api/663/19455">TBaaS</a></td>
 </tr>
 <tr>
<td><a href="https://cloud.tencent.com/document/api/248/30343">云监控</a></td>
 <td><a href="https://cloud.tencent.com/document/api/659/18591">迁移服务平台</a></td>
<td><a href="https://cloud.tencent.com/document/api/869/17778">电子合同服务</a></td>
 <td><a href="https://cloud.tencent.com/document/api/555/19170">计费相关</a></td>
 <td><a href="https://cloud.tencent.com/document/api/563/16034">渠道合作伙伴</a></td>
  </tr>
  <tr>
  <td><a href="https://cloud.tencent.com/document/api/1007/31320">人脸核身-云智慧眼</a></td>
   <td><a href="https://cloud.tencent.com/document/api/1013/31737">威胁情报云查</a></td>
 <td><a href="https://cloud.tencent.com/document/api/647/37078">实时音视频</a></td>
   <td><a href="https://cloud.tencent.com/document/api/670/31052">人脸融合</a></td>
    <td><a href="https://cloud.tencent.com/document/api/867/32770">人脸识别</a></td>
   </tr>
  <tr>
  <td><a href="https://cloud.tencent.com/document/api/1004/30607">数学作业批改</a></td>
   <td><a href="https://cloud.tencent.com/document/api/1000/30698">数字版权管理</a></td>
   <td><a href="https://cloud.tencent.com/document/api/866/33515">文字识别</a></td>
   <td><a href="https://cloud.tencent.com/document/api/649/36037">腾讯微服务平台 TSF</a></td>
   <td><a href="https://cloud.tencent.com/document/api/597/40823">消息队列 CKafka</a></td>
   </tr>
  <tr>   
   <td><a href="https://cloud.tencent.com/document/api/228/30974">内容分发网络</a></td>
<td><a href="https://cloud.tencent.com/document/api/296/19825">主机安全</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
     </tr>
  </table>

## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度。

## 环境依赖

### 开通云产品并获取密钥

- 登录 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应云产品。
- 获取 SecretID、SecretKey 以及调用地址（endpoint）。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
 - endpoint 一般形式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。


### 编译器

- 安装可支持 C++ 11 及以上版本的编译器：GCC 4.8 及以上版本。
- 目前仅支持 Linux 环境，不支持 Windows 环境。

### 编译工具
安装 [cmake](https://cmake.org/) 3.0 及以上版本，例如：
```
ubuntu
sudo apt-get install cmake
centos
yum install cmake3 
```



### 依赖库


- [libcurl](https://curl.haxx.se/libcurl/)
>!建议安装最新版本的 libcurl 库，否则可能存在 libcurl 库内存泄露 bug 问题。
>
安装示例：
```
ubuntu
sudo apt-get install libcurl4-openssl-dev
centos
yum install libcurl-devel 
```
- [openssl](https://www.openssl.org/)
安装示例：
```
ubuntu
sudo apt-get install libssl-dev
centos
yum install openssl-devel 
```
- libuuid
安装示例：
```
ubuntu
sudo apt-get install uuid-dev
centos
yum install libuuid-devel 
```

## 获取安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-cpp) 下载最新代码。
2. 解压源码包到项目中的合适位置。
3. 进入 SDK 创建生成必要的构建文件。
```
cd <path/to/tencentcloud-sdk-cpp>
mkdir sdk_build
cd sdk_build
cmake ..
make
sudo make install 
```

## 示例
本文以 CVM 的 DescribeInstances 接口为例，开发者可以在 GitHub 仓库 [example 目录](https://github.com/TencentCloud/tencentcloud-sdk-cpp/tree/master/example) 下查看更多更详细的示例。

源码如下：
```
#include <iostream>
#include <tencentcloud/core/TencentCloud.h>
#include <tencentcloud/core/Credential.h>
#include <tencentcloud/cvm/v20170312/CvmClient.h>
#include <tencentcloud/cvm/v20170312/model/DescribeInstancesRequest.h>
#include <tencentcloud/cvm/v20170312/model/DescribeInstancesResponse.h>
#include <tencentcloud/cvm/v20170312/model/Instance.h>
#include <string>
#include <vector>
using namespace TencentCloud;
using namespace TencentCloud::Cvm::V20170312;
using namespace TencentCloud::Cvm::V20170312::Model;
using namespace std;
int main()
{
    // 必须调用初始化函数
    TencentCloud::InitAPI();
    // use the sdk
    string secretId = "<Your-secretId>";
    string secretKey = "<Your-secertKey>";
    Credential cred = Credential(secretId, secretKey);
    DescribeInstancesRequest req = DescribeInstancesRequest();
    req.SetOffset(0);
    req.SetLimit(5);
    CvmClient cvm_client = CvmClient(cred, "ap-guangzhou");
    auto outcome = cvm_client.DescribeInstances(req);
    if (!outcome.IsSuccess())
    {
        cout << outcome.GetError().PrintAll() << endl;
        TencentCloud::ShutdownAPI();
        return -1;
    }
    DescribeInstancesResponse rsp = outcome.GetResult();
    cout<<"RequestId="<<rsp.GetRequestId()<<endl;
    cout<<"TotalCount="<<rsp.GetTotalCount()<<endl;
    vector<Instance> instanceSet = rsp.GetInstanceSet();
    for (auto itr=instanceSet.begin(); itr!=instanceSet.end(); ++itr)
    {
        cout<<(*itr).GetPlacement().GetZone()<<endl;
    }
    TencentCloud::ShutdownAPI();
    return 0;
} 
```

Demo 用例依次编译执行以下命令：
```
cd example/cvm/v20170312
mkdir build
cd build
cmake ..
make
./DescribeInstances 
```


如果无法自动找到报错动态库，可指定动态库路径。例如，`libtencentcloud-sdk-cpp-core.so`安装在`/usr/local/lib`路径下：
```
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
./DescribeInstances 
```
