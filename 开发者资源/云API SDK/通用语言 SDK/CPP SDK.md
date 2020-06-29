本文主要介绍适用于 C++ 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 C++ 开发者快速掌握如何调试和接入腾讯云产品 API。
支持 SDK 3.0 版本的云产品列表请参见 [SDK 简介](https://cloud.tencent.com/document/product/494/42698)。


## 环境依赖

### 开通云产品并获取密钥

- 登录 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应云产品。
- 在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 获取调用地址（endpoint），endpoint 一般格式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。


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
本文以 CVM 的 DescribeInstances 接口为例，更多示例请参考 [example 目录](https://github.com/TencentCloud/tencentcloud-sdk-cpp/tree/master/example)。

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

## 单元测试
1. 依赖库 gtest。
```
git clone https://github.com/google/googletest
cd googletest
cmake CMakeLists.txt
make
```
将生成的 libgtest.a libgtest_main.a 静态库，以及 gtest 的头文件，拷贝到系统目录下。
2.配置环境变量：
 - ENV_SecretId：密钥 ID
 - ENV_SecretKey：密钥 Key
3. 执行以下命令测试。
```
sh function_test.sh
```




