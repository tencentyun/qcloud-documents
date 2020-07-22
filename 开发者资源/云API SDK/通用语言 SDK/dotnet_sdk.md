## 简介

- 欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0 是云 API 3.0 平台的配套工具。
- SDK 3.0 实现了统一化，各个语言版本的 SDK 具备使用方法相同、接口调用方式相同、错误码和返回包格式相同等优点。本文以 .NET SDK 3.0 为例，介绍如何使用、调试并接入腾讯云产品 API。首次使用 .NET SDK 3.0 的简单示例见下文，您可通过本文快速获取腾讯云 .NET SDK 3.0 并开始进行调用。
- 目前已支持云服务器 CVM、私有网络 VPC 、云硬盘 CBS 等 [腾讯云产品](https://cloud.tencent.com/product)，后续会支持其他云产品接入。





## 步骤1：搭建所需环境

### 配置语言环境

- 依赖环境：.NET Framework 4.5+ 和 .NET Core 2.1。 
- 下面以 .NET Framework 4.7 和 .NET Core 2.1 为例。
- win10 系统自带 .NET Framework 4.7，则可以省去这里的安装。

#### 1. 下载安装 .NET Framework 4.7

查看本机 .net Framework 版本：打开【控制面板】>【程序】>【启用或关闭 Windows 功能】。

<img src="https://main.qcloudimg.com/raw/6bc643910f56ae99c392690893aaf810.png" width="408"><span><span/>
![](https://main.qcloudimg.com/raw/ebda693fbe89d1d98aae855b9ef68c2b.png)

经查看后，**如果没有，则需要在官网下载**：

1. 进入 [官网]( https://dotnet.microsoft.com/download/dotnet-framework ) 下载您所需的版本。
<img src="https://main.qcloudimg.com/raw/84718141b823a60adefbb81341132d61.png" width="700"><span/>
下载完毕，会得到一个`NDP47-DevPack-KB3186612-ENU.exe`可执行文件。
2. 双击打开，安装即可。
<div><img src="https://main.qcloudimg.com/raw/40e1152743e779c0d5d9fece89995e34.png" width="450"></div>

#### 2. 下载安装 Core 2.1

1. 进入 [官网](https://dotnet.microsoft.com/download/dotnet-core) 下载您所需的版本。
![](https://main.qcloudimg.com/raw/ce300f8f12fc64f1944bacf5069c9f2b.png)
![](https://main.qcloudimg.com/raw/1d76e5008ef1323000316bcade963493.png)
下载完毕，会得到一个`dotnet-sdk-2.1.612-win-x64.exe`可执行文件。
2. 双击打开，单击【install】即可。
![](https://main.qcloudimg.com/raw/18f16fd6141062767a5e87b87d14eebb.png)
默认安装地址一般为`C:\Program Files\dotnet`，并且**已经配置好环境变量**。如果需要指定安装位置，可下载右边的对应的 Binaries 文件，会得到一个`dotnet-sdk-2.1.807-win-x64.zip`压缩文件，提取到指定位置，并需要手动配置环境变量，例如解压到这个地址：`F:\saftware\language\dotnet`。
>?配置环境变量：【我的电脑】>【属性】>【高级系统设置】>【环境变量】>【系统变量】。
<img src="https://main.qcloudimg.com/raw/0946c8544324227a4ba405b0fe4a97ee.png" width="600"><span/>
<img src="https://main.qcloudimg.com/raw/d294cc6e233fd91156d952be63537809.png" width="500">
3. 安装完成后，按 **Win+R** 打开运行窗口，输入 cmd 并单击【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/f1206af2dd8361a6a5884ee6af4739a3.png)
在命令行窗口中，执行以下命令查看 Core SDK 版本。
```bash
dotnet --version
```
返回结果如下图所示，即表明已成功安装 Core 2.1.807。
![](https://main.qcloudimg.com/raw/2cc61cc0041774c6760bfa33655865f7.png) 



## 步骤2：安装 SDK

### 通过 nuget 安装（推荐）

- 通过命令行安装（**这里的版本仅作为示例，实际请选择最新版本**）：

   <pre>
    dotnet add package TencentCloudSDK --version 3.0.0
    # 其他信息请到 <a href="https://www.nuget.org/packages/TencentCloudSDK/">nuget</a> 获取
   </pre>
	 >!命令需要在项目的主目录下执行。
- 通过 Visual Studio 添加包：
例如，创建一个 HelloWorld 项目：
```bash
dotnet new console -o HelloWorld
# 进入到 HelloWorld 项目主目录
dotnet run
# 输出为：Hello World!
dotnet add package TencentCloudSDK --version 3.0.0
# 为项目下载 SDK 依赖
```



## 步骤3：使用 SDK

每个接口都有一个对应的 Request 结构和一个 Response 结构。例如，云服务器的查询实例列表接口 DescribeInstances 有对应的请求结构体 DescribeInstancesRequest 和返回结构体 DescribeInstancesResponse。

下面以云服务器查询实例列表接口为例，介绍 SDK 的基础用法。出于演示目的，有一些非必要的内容也在示例中，以尽量展示 SDK 常用的功能，但也显得臃肿，在实际编写代码使用 SDK 的时候，应尽量简化。

>!
>- 因为一个项目主目录下只能有一个主入口，所以这里在项目主目录下创建 DescribeZones.sc 文件时将原有的 Program.sc 文件去掉，之后在命令行输入`dotnet run`运行，即可获得数据。
>- 建议将密钥对加到环境变量中：
 - 变量名：TENCENTCLOUD_SECRET_ID，变量值：`xxxxxxxxxxxxxx`。
 - 变量名：TENCENTCLOUD_SECRET_KEY，变量值：`xxxxxxxxxxxxxx`。

### 示例1：查询可用区

```C#
using System;
using System.Collections.Generic;
using System.Text;
using TencentCloud.Common;
using TencentCloud.Common.Profile;
using TencentCloud.Cvm.V20170312;
using TencentCloud.Cvm.V20170312.Models;

namespace TencentCloudExamples
{
    class DescribeZones
    {
        static void Main(string[] args)
        {
            try
            {
                // 必要步骤：
                // 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId、secretKey。
                // 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
                // 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
                // 以免泄露密钥对危及你的财产安全。
                Credential cred = new Credential
                {
                    SecretId = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_ID"),
                    SecretKey = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_KEY")
                };

                // 实例化一个 client 选项，可选的，没有特殊需求可以跳过
                ClientProfile clientProfile = new ClientProfile();
                // 非必要步骤
                // 实例化一个客户端配置对象，可以指定超时时间等配置
                HttpProfile httpProfile = new HttpProfile();
                // 代理服务器，当你的环境下有代理服务器时设定
                httpProfile.WebProxy = Environment.GetEnvironmentVariable("HTTPS_PROXY");

                clientProfile.HttpProfile = httpProfile;

                // 实例化要请求产品（以 cvm 为例）的 client 对象
                // 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量，clientProfile 是可选的
                CvmClient client = new CvmClient(cred, "ap-guangzhou", clientProfile);

                // 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
                // 你可以直接查询 SDK 源码确定 DescribeZonesRequest 有哪些属性可以设置，
                // 属性可能是基本类型，也可能引用了另一个数据结构。
                // 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明。
                DescribeZonesRequest req = new DescribeZonesRequest();

                // 通过 client 对象调用 DescribeInstances 方法发起请求。注意请求方法名与请求对象是对应的
                // 返回的 resp 是一个 DescribeInstancesResponse 类的实例，与请求对象对应
                DescribeZonesResponse resp = client.DescribeZonesSync(req);

                // 输出 json 格式的字符串回包
                Console.WriteLine(AbstractModel.ToJsonString(resp));
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            Console.Read();
        }
    }
}
```

### 示例2：查询实例列表

```c#
using System;
using System.Threading.Tasks;
using TencentCloud.Common;
using TencentCloud.Common.Profile;
using TencentCloud.Cvm.V20170312;
using TencentCloud.Cvm.V20170312.Models;

namespace TencentCloudExamples
{
    class DescribeInstances
    {
        static void Main(string[] args)
        {
            try
            {
                // 必要步骤：
                // 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId、secretKey。
                // 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
                // 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
                // 以免泄露密钥对危及你的财产安全。
                Credential cred = new Credential {
                    SecretId = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_ID"),
                    SecretKey = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_KEY")
                };               

                // 实例化一个 client 选项，可选的，没有特殊需求可以跳过
                ClientProfile clientProfile = new ClientProfile();
                // 指定签名算法（默认为 HmacSHA256）
                clientProfile.SignMethod = ClientProfile.SIGN_SHA1;
                // 非必要步骤
                // 实例化一个客户端配置对象，可以指定超时时间等配置
                HttpProfile httpProfile = new HttpProfile();
                // SDK 默认使用 POST 方法。
                // 如果你一定要使用 GET 方法，可以在这里设置。GET 方法无法处理一些较大的请求。
                httpProfile.ReqMethod = "POST";
                // SDK 有默认的超时时间，非必要请不要进行调整。
                // 如有需要请在代码中查阅以获取最新的默认值。
                httpProfile.Timeout = 10; // 请求连接超时时间，单位为秒（默认60秒）
                // SDK 会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务，
                // 则必须手动指定域名，例如云服务器的上海金融区域名：cvm.ap-shanghai-fsi.tencentcloudapi.com
                httpProfile.Endpoint = ("cvm.tencentcloudapi.com");
                // 代理服务器，当你的环境下有代理服务器时设定
                httpProfile.WebProxy = Environment.GetEnvironmentVariable("HTTPS_PROXY");

                clientProfile.HttpProfile = httpProfile;

                // 实例化要请求产品（以 cvm 为例）的 client 对象
                // 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量，clientProfile 是可选的
                CvmClient client = new CvmClient(cred, "ap-guangzhou", clientProfile);

                // 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
                // 你可以直接查询 SDK 源码确定 DescribeInstancesRequest 有哪些属性可以设置，
                // 属性可能是基本类型，也可能引用了另一个数据结构。
                // 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明。
                DescribeInstancesRequest req = new DescribeInstancesRequest();
              
                // 基本类型的设置。
                // 此接口允许设置返回的实例数量。此处指定为只返回一个。
                // SDK 采用的是指针风格指定参数，即使对于基本类型你也需要用指针来对参数赋值。
                // SDK 提供对基本类型的指针引用封装函数
                req.Limit = 1;
                // 数组类型的设置。
                // 此接口允许指定实例 ID 进行过滤，但是由于和接下来要演示的 Filter 参数冲突，先注释掉。
                // req.InstanceIds = new string[] { "ins-r8hr2upy" };

                // 复杂对象的设置。
                // 在这个接口中，Filters 是数组，数组的元素是复杂对象 Filter，Filter 的成员 Values 是 string 数组。
                // 填充请求参数,这里 request 对象的成员变量即对应接口的入参
                // 你可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
                Filter respFilter = new Filter(); // 创建 Filter 对象, 以 zone 的维度来查询 cvm 实例
                respFilter.Name = "zone";
                respFilter.Values = new string[] { "ap-guangzhou-1", "ap-guangzhou-2" };
                req.Filters = new Filter[] { respFilter }; // Filters 是成员为 Filter 对象的列表

                //// 这里还支持以标准 json 格式的 string 来赋值请求参数的方式。下面的代码跟上面的参数赋值是等效的
                //string strParams = "{\"Filters\":[{\"Name\":\"zone\",\"Values\":[\"ap-guangzhou-1\",\"ap-guangzhou-2\"]}]}";
                //req = DescribeInstancesRequest.FromJsonString<DescribeInstancesRequest>(strParams);

                // 通过 client 对象调用 DescribeInstances 方法发起请求。注意请求方法名与请求对象是对应的
                // 返回的 resp 是一个 DescribeInstancesResponse 类的实例，与请求对象对应
                DescribeInstancesResponse resp = client.DescribeInstancesSync(req);

                // 使用同步接口调用结果
                // DescribeInstancesResponse resp = client.DescribeInstancesSync(req);

                // 输出 json 格式的字符串回包
                Console.WriteLine(AbstractModel.ToJsonString(resp));

                // 也可以取出单个值。
                // 你可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
                Console.WriteLine(resp.TotalCount);
    
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            Console.Read();
        }
    }
}

```



### 更多示例

更多示例请参见 [github](https://github.com/TencentCloud/tencentcloud-sdk-dotnet) TencentCloudExamples 目录。 

### 同步调用与异步调用

新版本 SDK 中同时提供了异步接口和同步接口，同步接口统一在异步接口之后添加了`Sync`后缀，在上述代码中已有样例。


>!在示例中由于是控制台应用程序，因此可以使用同步方式调用异步接口，即`ConfigureAwait(false).GetAwaiter().GetResult()`。在开发 ASP 应用程序，或者 Windows Forms 应用程序时，UI 控件的响应方法中，不能使用同步方式调用异步接口，否则会造成界面停止响应。
>解决办法：将 UI 控件的响应方法改为异步，同时要注意同步上下文。另外，由于异步调用立即返回控制权给用户，很容易造成用户多次点击，或者用户进行了一些不期望的操作，程序中应注意此类问题。源码可以参考项目中的 WindowsFormsDemo 项目。

源码可以参考：[腾讯云社区专栏文章](https://cloud.tencent.com/developer/article/1395819)



## 相关配置

### 代理

若在代理的环境下使用 SDK 进行接口调用，则需设置系统环境变量`https_proxy`（已在示例代码中体现），否则可能出现无法正常调用、抛出连接超时异常的现象。

