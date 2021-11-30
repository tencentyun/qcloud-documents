SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [短信 API](https://cloud.tencent.com/document/product/382/52077)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送短信相关接口
>一次群发请求最多支持200个号码。
>- 签名、正文模板相关接口
>个人认证用户不支持使用签名、正文模板相关接口，只能通过短信控制台 [管理短信签名](https://cloud.tencent.com/document/product/382/37794) 和 [管理短信正文模板](https://cloud.tencent.com/document/product/382/37795)。如需使用该类接口，请将 “个人认证” 变更为 “企业认证”，具体操作请参见 [实名认证变更指引](https://cloud.tencent.com/document/product/378/34075)。



## 前提条件

- 已开通短信服务，具体操作请参见 [国内短信快速入门](https://cloud.tencent.com/document/product/382/37745)。
- 如需发送国内短信，需要先 [购买国内短信套餐包](https://cloud.tencent.com/document/product/382/18060)。
- 已准备依赖环境：.NET Framework 4.5+ 和 .NET Core 2.1。
- 已在访问管理控制台 >**[API密钥管理](https://console.cloud.tencent.com/cam/capi)**页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 短信的调用地址为`sms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/382/52077)。
- 下载 SDK 源码请访问 [C# SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)。

## 安装 SDK
### 通过 nuget 安装（推荐）

1. 执行以下安装命令。
```
dotnet add package TencentCloudSDK
```
 其他信息请通过 [nuget](https://www.nuget.org/packages/TencentCloudSDK/) 获取。
2. 通过 Visual Studio 添加包。

### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-dotnet) 或 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-dotnet/tencentcloud-sdk-dotnet.zip) 下载最新代码。
2. 解压后安装到工作目录下。
3. 使用 Visual Studio 2017 打开编译。


## 示例代码
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。本文仅列举几个常用功能的示例代码，如下所示。

### 发送短信

```
using System;
using System.Threading.Tasks;
using TencentCloud.Common;
using TencentCloud.Common.Profile;
using TencentCloud.Sms.V20210111;
using TencentCloud.Sms.V20210111.Models;

namespace TencentCloudExamples
{
    class SendSms
    {
        static void Main1(string[] args)
        {
            try
            {
                /* 必要步骤：
                 * 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
                 * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
                 * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
                 * 以免泄露密钥对危及你的财产安全。
                 * CAM密匙查询: https://console.cloud.tencent.com/cam/capi*/
                Credential cred = new Credential {
                    SecretId = "xxx",
                    SecretKey = "xxx"
                };
                /*
                Credential cred = new Credential {
                    SecretId = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_ID"),
                    SecretKey = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_KEY")
                };*/

                /* 非必要步骤:
                 * 实例化一个客户端配置对象，可以指定超时时间等配置 */
                ClientProfile clientProfile = new ClientProfile();
                /* SDK默认用TC3-HMAC-SHA256进行签名
                 * 非必要请不要修改这个字段 */
                clientProfile.SignMethod = ClientProfile.SIGN_TC3SHA256;
                /* 非必要步骤
                 * 实例化一个客户端配置对象，可以指定超时时间等配置 */
                HttpProfile httpProfile = new HttpProfile();
                /* SDK默认使用POST方法。
                 * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
                httpProfile.ReqMethod = "GET";
                /* SDK有默认的超时时间，非必要请不要进行调整
                 * 如有需要请在代码中查阅以获取最新的默认值 */
                httpProfile.Timeout = 10; // 请求连接超时时间，单位为秒(默认60秒)
                /* SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
                 * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com */
                httpProfile.Endpoint = "sms.tencentcloudapi.com";
                // 代理服务器，当你的环境下有代理服务器时设定
                // httpProfile.WebProxy = Environment.GetEnvironmentVariable("HTTPS_PROXY");

                clientProfile.HttpProfile = httpProfile;
                /* 实例化要请求产品(以sms为例)的client对象
                 * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
                SmsClient client = new SmsClient(cred, "ap-guangzhou", clientProfile);

                /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
                 * 你可以直接查询SDK源码确定SendSmsRequest有哪些属性可以设置
                 * 属性可能是基本类型，也可能引用了另一个数据结构
                 * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
                SendSmsRequest req = new SendSmsRequest();

                /* 基本类型的设置:
                 * SDK采用的是指针风格指定参数，即使对于基本类型你也需要用指针来对参数赋值。
                 * SDK提供对基本类型的指针引用封装函数
                 * 帮助链接：
                 * 短信控制台: https://console.cloud.tencent.com/smsv2
                 * sms helper: https://cloud.tencent.com/document/product/382/3773 */

                req.SmsSdkAppId = "1400787878";
                /* 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看 */
                req.SignName = "xxx";
                /* 短信码号扩展号: 默认未开通，如需开通请联系 [sms helper] */
                req.ExtendCode = "";
                /* 国际/港澳台短信 senderid: 国内短信填空，默认未开通，如需开通请联系 [sms helper] */
                req.SenderId = "";
                /* 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回 */
                req.SessionContext = "";
                /* 下发手机号码，采用 E.164 标准，+[国家或地区码][手机号]
                 * 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号*/
                req.PhoneNumberSet = new String[] {"+8613711112222"};
                /* 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看 */
                req.TemplateId = "449739";
                /* 模板参数: 若无模板参数，则设置为空*/
                req.TemplateParamSet = new String[] {"666"};


                // 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的
                // 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应
                SendSmsResponse resp = client.SendSmsSync(req);

                // 输出json格式的字符串回包
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



### 拉取回执状态

```
using System;
using System.Threading.Tasks;
using TencentCloud.Common;
using TencentCloud.Common.Profile;
using TencentCloud.Sms.V20210111;
using TencentCloud.Sms.V20210111.Models;
namespace TencentCloudExamples
{
  class PullSmsSendStatus
  {
      static void Main(string[] args)
      {
          try
          {
              /* 必要步骤：
               * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
               * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
               * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
               * CAM 密匙查询：https://console.cloud.tencent.com/cam/capi
               */
              Credential cred = new Credential {
                  SecretId = "xxx",
                  SecretKey = "xxx"
              };
              /*
              Credential cred = new Credential {
                  SecretId = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_ID"),
                  SecretKey = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_KEY")
              };*/
               /* 非必要步骤:
               * 实例化一个客户端配置对象，可以指定超时时间等配置 */
              ClientProfile clientProfile = new ClientProfile();
              /* SDK 默认用 TC3-HMAC-SHA256 进行签名
               * 非必要请不要修改该字段 */
              clientProfile.SignMethod = ClientProfile.SIGN_TC3SHA256;
              /* 非必要步骤
               * 实例化一个客户端配置对象，可以指定超时时间等配置 */
              HttpProfile httpProfile = new HttpProfile();
              /* SDK 默认使用 POST 方法
               * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
              httpProfile.ReqMethod = "POST";
              /* SDK 有默认的超时时间，非必要请不要进行调整
               * 如有需要请在代码中查阅以获取最新的默认值 */
              httpProfile.Timeout = 10; // 请求连接超时时间，单位为秒(默认60秒)
              /* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
               * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
              httpProfile.Endpoint = "sms.tencentcloudapi.com";
              // 代理服务器，当您的环境下有代理服务器时设定
              // httpProfile.WebProxy = Environment.GetEnvironmentVariable("HTTPS_PROXY");
              clientProfile.HttpProfile = httpProfile;
              /* 实例化 SMS 的 client 对象
               * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
              SmsClient client = new SmsClient(cred, "ap-guangzhou", clientProfile);
              /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
               * 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
               * 属性可能是基本类型，也可能引用了另一个数据结构
               * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
              PullSmsSendStatusRequest req = new PullSmsSendStatusRequest();

              /* 基本类型的设置:
               * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值
               * SDK 提供对基本类型的指针引用封装函数
               * 帮助链接：
               * 短信控制台：https://console.cloud.tencent.com/smsv2
               * sms helper：https://cloud.tencent.com/document/product/382/3773 */

              // 设置拉取最大条数，最多100条
              req.Limit = 100;
              /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SdkAppId，例如1400006666 */
              req.SmsSdkAppId = "1400009099";
              // 通过 client 对象调用 PullSmsSendStatus 方法发起请求，注意请求方法名与请求对象是对应的
              // 返回的 resp 是一个 PullSmsSendStatusResponse 类的实例，与请求对象对应
              PullSmsSendStatusResponse resp = client.PullSmsSendStatusSync(req);
              // 输出 JSON 格式的字符串回包
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

### 统计短信发送数据

```
using System;
using System.Threading.Tasks;
using TencentCloud.Common;
using TencentCloud.Common.Profile;
using TencentCloud.Sms.V20210111;
using TencentCloud.Sms.V20210111.Models;
namespace TencentCloudExamples
{
   class SendStatusStatistics
   {
       static void Main(string[] args)
       {
           try
           {
               /* 必要步骤：
                * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
                * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
                * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
                * CAM 密匙查询：https://console.cloud.tencent.com/cam/capi
                */
               Credential cred = new Credential {
                   SecretId = "xxx",
                   SecretKey = "xxx"
               };
               /*
               Credential cred = new Credential {
                   SecretId = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_ID"),
                   SecretKey = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_KEY")
               };*/
               /* 非必要步骤:
                * 实例化一个客户端配置对象，可以指定超时时间等配置 */
               ClientProfile clientProfile = new ClientProfile();
               /* SDK 默认用 TC3-HMAC-SHA256 进行签名
                * 非必要请不要修改该字段 */
               clientProfile.SignMethod = ClientProfile.SIGN_TC3SHA256;
               /* 非必要步骤
                * 实例化一个客户端配置对象，可以指定超时时间等配置 */
               HttpProfile httpProfile = new HttpProfile();
               /* SDK 默认使用 POST 方法
                * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
               httpProfile.ReqMethod = "POST";
               /* SDK 有默认的超时时间，非必要请不要进行调整
                * 如有需要请在代码中查阅以获取最新的默认值 */
               httpProfile.Timeout = 10; // 请求连接超时时间，单位为秒(默认60秒)
               /* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
                * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
               httpProfile.Endpoint = "sms.tencentcloudapi.com";
               // 代理服务器，当您的环境下有代理服务器时设定
               // httpProfile.WebProxy = Environment.GetEnvironmentVariable("HTTPS_PROXY");
               clientProfile.HttpProfile = httpProfile;
               /* 实例化 SMS 的 client 对象
                * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
               SmsClient client = new SmsClient(cred, "ap-guangzhou", clientProfile);
               /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
                * 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
                * 属性可能是基本类型，也可能引用了另一个数据结构
                * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
               SendStatusStatisticsRequest req = new SendStatusStatisticsRequest();

               /* 基本类型的设置:
                * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值
                * SDK 提供对基本类型的指针引用封装函数
                * 帮助链接：
                * 短信控制台：https://console.cloud.tencent.com/smsv2
                * sms helper：https://cloud.tencent.com/document/product/382/3773
                */

               /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SdkAppId，例如1400006666 */
               req.SmsSdkAppId = "1400009099";
               // 设置拉取最大条数，最多100条
               req.Limit = 5L;
               /* 偏移量，目前固定设置为0 */
               req.Offset = 0L;
               /* 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时 */
               req.BeginTime = "2019071100";
               /* 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
                * 注：EndTime 必须大于 BeginTime */
               req.EndTime = "2019071123";
               // 通过 client 对象调用 SendStatusStatistics 方法发起请求，注意请求方法名与请求对象是对应的
               // 返回的 resp 是一个 SendStatusStatisticsResponse 类的实例，与请求对象对应
               SendStatusStatisticsResponse resp = client.SendStatusStatisticsSync(req);
               // 输出 JSON 格式的字符串回包
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

### 申请短信模板

```
using System;
using System.Threading.Tasks;
using TencentCloud.Common;
using TencentCloud.Common.Profile;
using TencentCloud.Sms.V20210111;
using TencentCloud.Sms.V20210111.Models;
namespace TencentCloudExamples
{
  class AddSmsTemplate
  {
      static void Main(string[] args)
      {
          try
          {
              /* 必要步骤：
               * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
               * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
               * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
               * CAM 密匙查询：https://console.cloud.tencent.com/cam/capi
               */
              Credential cred = new Credential {
                  SecretId = "xxx",
                  SecretKey = "xxx"
              };
              /*
              Credential cred = new Credential {
                  SecretId = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_ID"),
                  SecretKey = Environment.GetEnvironmentVariable("TENCENTCLOUD_SECRET_KEY")
              };*/
              /* 非必要步骤:
               * 实例化一个客户端配置对象，可以指定超时时间等配置 */
              ClientProfile clientProfile = new ClientProfile();
              /* SDK 默认用 TC3-HMAC-SHA256 进行签名
               * 非必要请不要修改该字段 */
              clientProfile.SignMethod = ClientProfile.SIGN_TC3SHA256;
              /* 非必要步骤
               * 实例化一个客户端配置对象，可以指定超时时间等配置 */
              HttpProfile httpProfile = new HttpProfile();
              /* SDK 默认使用 POST 方法
               * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
              httpProfile.ReqMethod = "GET";
              /* SDK 有默认的超时时间，非必要请不要进行调整
               * 如有需要请在代码中查阅以获取最新的默认值 */
              httpProfile.Timeout = 10; // 请求连接超时时间，单位为秒(默认60秒)
              /* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
               * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
              httpProfile.Endpoint = "sms.tencentcloudapi.com";
              // 代理服务器，当您的环境下有代理服务器时设定
              // httpProfile.WebProxy = Environment.GetEnvironmentVariable("HTTPS_PROXY");
              clientProfile.HttpProfile = httpProfile;
              /* 实例化 SMS 的 client 对象
               * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
              SmsClient client = new SmsClient(cred, "ap-guangzhou", clientProfile);
              /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
               * 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
               * 属性可能是基本类型，也可能引用了另一个数据结构
               * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
              AddSmsTemplateRequest req = new AddSmsTemplateRequest();

              /* 基本类型的设置:
               * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值
               * SDK 提供对基本类型的指针引用封装函数
               * 帮助链接：
               * 短信控制台：https://console.cloud.tencent.com/smsv2
               * sms helper：https://cloud.tencent.com/document/product/382/3773
               */

              /* 模板名称 */
              req.TemplateName = "腾讯云";
              /* 模板内容 */
              req.TemplateContent = "{1}为您的登录验证码，请于{2}分钟内填写，如非本人操作，请忽略本短信。";
              /* 短信类型：0表示普通短信, 1表示营销短信 */
              req.SmsType = 0;
              /* 是否国际/港澳台短信：
               * 0：表示国内短信
               * 1：表示国际/港澳台短信 */
              req.International = 0;
              /* 模板备注：例如申请原因，使用场景等 */
              req.Remark = "xxx";

              // 通过 client 对象调用 AddSmsTemplate 方法发起请求，注意请求方法名与请求对象是对应的
              // 返回的 resp 是一个 AddSmsTemplateResponse 类的实例，与请求对象对应
              AddSmsTemplateResponse resp = client.AddSmsTemplateSync(req);
              // 输出 JSON 格式的字符串回包
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

## 常见问题
<dx-accordion>
::: 代理设置
若在代理的环境下使用 SDK 进行接口调用，则需设置系统环境变量`https_proxy`（已在示例代码中体现），否则可能出现无法正常调用、抛出连接超时异常的现象。
:::
::: 同步调用与异步调用
新版本 SDK 中同时提供了异步接口和同步接口，同步接口统一在异步接口之后添加了`Sync`后缀，在上述代码中已有样例。


>!在示例中由于是控制台应用程序，因此可以使用同步方式调用异步接口，即`ConfigureAwait(false).GetAwaiter().GetResult()`。在开发 ASP 应用程序，或者 Windows Forms 应用程序时，UI 控件的响应方法中，不能使用同步方式调用异步接口，否则会造成界面停止响应。
>解决办法：将 UI 控件的响应方法改为异步，同时要注意同步上下文。另外，由于异步调用立即返回控制权给用户，很容易造成用户多次点击，或者用户进行了一些不期望的操作，程序中应注意此类问题。源码可以参考项目中的 WindowsFormsDemo 项目。

源码可以参考：[腾讯云社区专栏文章](https://cloud.tencent.com/developer/article/1395819)
:::
::: 依赖版本
SDK 依赖的 FluentClient 使用的是3.2版本，但这个包目前发布了4.0版本且不兼容低版本，在 nuget 中升级此包到4.0版本会导致无法调用或调用失败等问题。
:::
</dx-accordion>
