SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [短信 API](https://cloud.tencent.com/document/product/382/52077)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送短信相关接口：
>一次群发请求最多支持200个号码。
>- 签名、正文模板相关接口：
>个人认证用户不支持使用签名、正文模板相关接口，只能通过短信控制台 [管理短信签名](https://cloud.tencent.com/document/product/382/37794) 和 [管理短信正文模板](https://cloud.tencent.com/document/product/382/37795)。如需使用该类接口，请将 “个人认证” 变更为 “企业认证”，具体操作请参见 [实名认证变更指引](https://cloud.tencent.com/document/product/378/34075)。



## 前提条件

- 已开通短信服务，创建签名和模板并通过审核，具体操作请参见 [国内短信快速入门](https://cloud.tencent.com/document/product/382/37745)。
- 如需发送国内短信，需要先 [购买国内短信套餐包](https://cloud.tencent.com/document/product/382/18060)。
- 已在访问管理控制台 > [**API密钥管理**](https://console.cloud.tencent.com/cam/capi) 页面获取 SecretID 和 SecretKey。
  - SecretID 用于标识 API 调用者的身份。
  - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 短信的调用地址为`sms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/382/52077)。
- 下载 SDK 源码请访问 [C++ SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-cpp)。

## 安装 SDK
### 环境依赖
参见 [环境依赖](https://github.com/TencentCloud/tencentcloud-sdk-cpp#%E7%8E%AF%E5%A2%83%E4%BE%9D%E8%B5%96)。

### 从源代码构建 SDK
参见 [从源代码构建 SDK](https://github.com/TencentCloud/tencentcloud-sdk-cpp#%E4%BB%8E%E6%BA%90%E4%BB%A3%E7%A0%81%E6%9E%84%E5%BB%BA-sdk)。


## 示例代码
>?所有示例代码仅作参见，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。本文仅列举几个常用功能的示例代码，如下所示。

### 发送短信

```
#include <tencentcloud/core/TencentCloud.h>
#include <tencentcloud/core/profile/HttpProfile.h>
#include <tencentcloud/core/profile/ClientProfile.h>
#include <tencentcloud/core/Credential.h>
#include <tencentcloud/core/NetworkProxy.h>
#include <tencentcloud/core/AsyncCallerContext.h>
#include <tencentcloud/sms/v20210111/SmsClient.h>
#include <tencentcloud/sms/v20210111/model/SendSmsRequest.h>
#include <tencentcloud/sms/v20210111/model/SendSmsResponse.h>

#include <iostream>
#include <string>

using namespace TencentCloud;
using namespace TencentCloud::Sms::V20210111;
using namespace TencentCloud::Sms::V20210111::Model;
using namespace std;

int main()
{
    TencentCloud::InitAPI();

    // use the sdk
    // 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey, 切勿将密钥泄露给他人
    // 前往 https://console.cloud.tencent.com/cam/capi 获取 API 密钥 SecretId SecretKey
    string secretId = "<your secret id>";
    string secretKey = "<your secret key>";
    Credential cred = Credential(secretId, secretKey);
    
    // 实例化一个http选项，可选的，没有特殊需求可以跳过。
    HttpProfile httpProfile = HttpProfile();
    httpProfile.SetKeepAlive(true);  // 状态保持，默认是False
    httpProfile.SetEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)
    httpProfile.SetReqTimeout(30);  // 请求超时时间，单位为秒(默认60秒)
    httpProfile.SetConnectTimeout(30); // 响应超时时间，单位是秒(默认是60秒)

    ClientProfile clientProfile = ClientProfile(httpProfile);

    SendSmsRequest req = SendSmsRequest();
    
    /* 帮助链接：
     * 短信控制台: https://console.cloud.tencent.com/smsv2
     * 腾讯云短信小助手: https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81 */
    /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SdkAppId，例如1400006666 */
    // 应用 ID 可前往 [短信控制台](https://console.cloud.tencent.com/smsv2/app-manage) 查看
    req.SetSmsSdkAppId("1400787878");

    /* 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名 */
    // 签名信息可前往 [国内短信](https://console.cloud.tencent.com/smsv2/csms-sign) 或 [国际/港澳台短信](https://console.cloud.tencent.com/smsv2/isms-sign) 的签名管理查看
    req.SetSignName("腾讯云");

    /* 模板 ID: 必须填写已审核通过的模板 ID */
    // 模板 ID 可前往 [国内短信](https://console.cloud.tencent.com/smsv2/csms-template) 或 [国际/港澳台短信](https://console.cloud.tencent.com/smsv2/isms-template) 的正文模板管理查看
    req.SetTemplateId("449739");

    /* 模板参数: 模板参数的个数需要与 TemplateId 对应模板的变量个数保持一致，若无模板参数，则设置为空 */
    req.SetTemplateParamSet(std::vector<std::string>{"1234"});

    /* 下发手机号码，采用 E.164 标准，+[国家或地区码][手机号]
     * 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号 */
    req.SetPhoneNumberSet(std::vector<std::string>{"+8613711112222"});

    /* 用户的 session 内容（无需要可忽略）: 可以携带用户侧 ID 等上下文信息，server 会原样返回 */
    req.SetSessionContext("");

    /* 短信码号扩展号（无需要可忽略）: 默认未开通，如需开通请联系 [腾讯云短信小助手] */
    req.SetExtendCode("");

    /* 国际/港澳台短信 senderid（无需要可忽略）: 国内短信填空，默认未开通，如需开通请联系 [腾讯云短信小助手] */
    req.SetSenderId("");

    /* 实例化要请求产品(以sms为例)的client对象
     * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，支持的地域列表参考 https://cloud.tencent.com/document/api/382/52071#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8 */
    SmsClient sms_client = SmsClient(cred, "ap-guangzhou", clientProfile);

    // 设置代理（无需要直接忽略）
    // NetworkProxy proxy = NetworkProxy(NetworkProxy::Type::HTTP, "localhost.proxy.com", 8080);
    // sms_client.SetNetworkProxy(proxy);

    auto outcome = sms_client.SendSms(req);
    if (!outcome.IsSuccess())
    {
        cout << outcome.GetError().PrintAll() << endl;
        TencentCloud::ShutdownAPI();
        return -1;
    }
    SendSmsResponse rsp = outcome.GetResult();
    cout<<"RequestId="<<rsp.GetRequestId()<<endl;
    cout<<"SendSmsResponse="<<rsp.ToJsonString()<<endl;
    
    TencentCloud::ShutdownAPI();

    /* 当出现以下错误码时，快速解决方案参考
     * [FailedOperation.SignatureIncorrectOrUnapproved](https://cloud.tencent.com/document/product/382/9558#.E7.9F.AD.E4.BF.A1.E5.8F.91.E9.80.81.E6.8F.90.E7.A4.BA.EF.BC.9Afailedoperation.signatureincorrectorunapproved-.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F)
     * [FailedOperation.TemplateIncorrectOrUnapproved](https://cloud.tencent.com/document/product/382/9558#.E7.9F.AD.E4.BF.A1.E5.8F.91.E9.80.81.E6.8F.90.E7.A4.BA.EF.BC.9Afailedoperation.templateincorrectorunapproved-.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F)
     * [UnauthorizedOperation.SmsSdkAppIdVerifyFail](https://cloud.tencent.com/document/product/382/9558#.E7.9F.AD.E4.BF.A1.E5.8F.91.E9.80.81.E6.8F.90.E7.A4.BA.EF.BC.9Aunauthorizedoperation.smssdkappidverifyfail-.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F)
     * [UnsupportedOperation.ContainDomesticAndInternationalPhoneNumber](https://cloud.tencent.com/document/product/382/9558#.E7.9F.AD.E4.BF.A1.E5.8F.91.E9.80.81.E6.8F.90.E7.A4.BA.EF.BC.9Aunsupportedoperation.containdomesticandinternationalphonenumber-.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F)
     * 更多错误，可咨询[腾讯云助手](https://tccc.qcloud.com/web/im/index.html#/chat?webAppId=8fa15978f85cb41f7e2ea36920cb3ae1&title=Sms)
     */

    return 0;
}
```



### 拉取回执状态

```
#include <tencentcloud/core/TencentCloud.h>
#include <tencentcloud/core/profile/HttpProfile.h>
#include <tencentcloud/core/profile/ClientProfile.h>
#include <tencentcloud/core/Credential.h>
#include <tencentcloud/core/NetworkProxy.h>
#include <tencentcloud/core/AsyncCallerContext.h>
#include <tencentcloud/sms/v20210111/SmsClient.h>
#include <tencentcloud/sms/v20210111/model/PullSmsSendStatusRequest.h>
#include <tencentcloud/sms/v20210111/model/PullSmsSendStatusResponse.h>

#include <iostream>
#include <string>

using namespace TencentCloud;
using namespace TencentCloud::Sms::V20210111;
using namespace TencentCloud::Sms::V20210111::Model;
using namespace std;

int main()
{
    TencentCloud::InitAPI();

    // use the sdk
    // 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey, 切勿将密钥泄露给他人
    // 前往 https://console.cloud.tencent.com/cam/capi 获取 API 密钥 SecretId SecretKey
    string secretId = "<your secret id>";
    string secretKey = "<your secret key>";
    Credential cred = Credential(secretId, secretKey);
    
    // 实例化一个http选项，可选的，没有特殊需求可以跳过。
    HttpProfile httpProfile = HttpProfile();
    httpProfile.SetKeepAlive(true);  // 状态保持，默认是False
    httpProfile.SetEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)
    httpProfile.SetReqTimeout(30);  // 请求超时时间，单位为秒(默认60秒)
    httpProfile.SetConnectTimeout(30); // 响应超时时间，单位是秒(默认是60秒)

    ClientProfile clientProfile = ClientProfile(httpProfile);

    PullSmsSendStatusRequest req = PullSmsSendStatusRequest();
    
    /* 帮助链接：
     * 短信控制台: https://console.cloud.tencent.com/smsv2
     * 腾讯云短信小助手: https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81 */
    /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SdkAppId，例如1400006666 */
    req.SetSmsSdkAppId("1400787878");
    // 设置拉取最大条数，最多100条
    req.SetLimit(100);

    SmsClient sms_client = SmsClient(cred, "ap-guangzhou", clientProfile);

    // set proxy
    // NetworkProxy proxy = NetworkProxy(NetworkProxy::Type::HTTP, "localhost.proxy.com", 8080);
    // cvm_client.SetNetworkProxy(proxy);

    auto outcome = sms_client.PullSmsSendStatus(req);
    if (!outcome.IsSuccess())
    {
        cout << outcome.GetError().PrintAll() << endl;
        TencentCloud::ShutdownAPI();
        return -1;
    }
    PullSmsSendStatusResponse rsp = outcome.GetResult();
    cout<<"RequestId="<<rsp.GetRequestId()<<endl;
    cout<<"PullSmsSendStatusResponse="<<rsp.ToJsonString()<<endl;
    
    TencentCloud::ShutdownAPI();

    return 0;
}
```

### 统计短信发送数据

```
#include <tencentcloud/core/TencentCloud.h>
#include <tencentcloud/core/profile/HttpProfile.h>
#include <tencentcloud/core/profile/ClientProfile.h>
#include <tencentcloud/core/Credential.h>
#include <tencentcloud/core/NetworkProxy.h>
#include <tencentcloud/core/AsyncCallerContext.h>
#include <tencentcloud/sms/v20210111/SmsClient.h>
#include <tencentcloud/sms/v20210111/model/SendStatusStatisticsRequest.h>
#include <tencentcloud/sms/v20210111/model/SendStatusStatisticsResponse.h>

#include <iostream>
#include <string>

using namespace TencentCloud;
using namespace TencentCloud::Sms::V20210111;
using namespace TencentCloud::Sms::V20210111::Model;
using namespace std;

int main()
{
    TencentCloud::InitAPI();

    // use the sdk
    // 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey, 切勿将密钥泄露给他人
    // 前往 https://console.cloud.tencent.com/cam/capi 获取 API 密钥 SecretId SecretKey
    string secretId = "<your secret id>";
    string secretKey = "<your secret key>";
    Credential cred = Credential(secretId, secretKey);
    
    // 实例化一个http选项，可选的，没有特殊需求可以跳过。
    HttpProfile httpProfile = HttpProfile();
    httpProfile.SetKeepAlive(true);  // 状态保持，默认是False
    httpProfile.SetEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)
    httpProfile.SetReqTimeout(30);  // 请求超时时间，单位为秒(默认60秒)
    httpProfile.SetConnectTimeout(30); // 响应超时时间，单位是秒(默认是60秒)

    ClientProfile clientProfile = ClientProfile(httpProfile);

    SendStatusStatisticsRequest req = SendStatusStatisticsRequest();
    
    /* 帮助链接：
     * 短信控制台: https://console.cloud.tencent.com/smsv2
     * 腾讯云短信小助手: https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81 */
    /* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SdkAppId，例如1400006666 */
    req.SetSmsSdkAppId("1400787878");
    // 最大上限，目前固定设置为0
    req.SetLimit(0);
    /* 偏移量，目前固定设置为0 */
    req.SetOffset(0);
    /* 设置起始时间，格式为yyyymmddhh，精确到小时，例如2021050113，表示2021年5月1号13时。 */
    req.SetBeginTime("2019071100");
    /* 设置结束时间，格式为yyyymmddhh，精确到小时，例如2021050118，表示2021年5月1号18时。
        注：EndTime 必须大于 BeginTime。 */
    req.SetEndTime("2019071123");

    SmsClient sms_client = SmsClient(cred, "ap-guangzhou", clientProfile);

    // set proxy
    // NetworkProxy proxy = NetworkProxy(NetworkProxy::Type::HTTP, "localhost.proxy.com", 8080);
    // cvm_client.SetNetworkProxy(proxy);

    auto outcome = sms_client.SendStatusStatistics(req);
    if (!outcome.IsSuccess())
    {
        cout << outcome.GetError().PrintAll() << endl;
        TencentCloud::ShutdownAPI();
        return -1;
    }
    SendStatusStatisticsResponse rsp = outcome.GetResult();
    cout<<"RequestId="<<rsp.GetRequestId()<<endl;
    cout<<"SendStatusStatisticsResponse="<<rsp.ToJsonString()<<endl;
    
    TencentCloud::ShutdownAPI();

    return 0;
}
```

### 申请短信模板

```
#include <tencentcloud/core/TencentCloud.h>
#include <tencentcloud/core/profile/HttpProfile.h>
#include <tencentcloud/core/profile/ClientProfile.h>
#include <tencentcloud/core/Credential.h>
#include <tencentcloud/core/NetworkProxy.h>
#include <tencentcloud/core/AsyncCallerContext.h>
#include <tencentcloud/sms/v20210111/SmsClient.h>
#include <tencentcloud/sms/v20210111/model/AddSmsTemplateRequest.h>
#include <tencentcloud/sms/v20210111/model/AddSmsTemplateResponse.h>

#include <iostream>
#include <string>

using namespace TencentCloud;
using namespace TencentCloud::Sms::V20210111;
using namespace TencentCloud::Sms::V20210111::Model;
using namespace std;

int main()
{
    TencentCloud::InitAPI();

    // use the sdk
    // 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey, 切勿将密钥泄露给他人
    // 前往 https://console.cloud.tencent.com/cam/capi 获取 API 密钥 SecretId SecretKey
    string secretId = "<your secret id>";
    string secretKey = "<your secret key>";
    Credential cred = Credential(secretId, secretKey);
    
    // 实例化一个http选项，可选的，没有特殊需求可以跳过。
    HttpProfile httpProfile = HttpProfile();
    httpProfile.SetKeepAlive(true);  // 状态保持，默认是False
    httpProfile.SetEndpoint("sms.tencentcloudapi.com");  // 指定接入地域域名(默认就近接入)
    httpProfile.SetReqTimeout(30);  // 请求超时时间，单位为秒(默认60秒)
    httpProfile.SetConnectTimeout(30); // 响应超时时间，单位是秒(默认是60秒)

    ClientProfile clientProfile = ClientProfile(httpProfile);

    AddSmsTemplateRequest req = AddSmsTemplateRequest();
    
    /* 帮助链接：
     * 短信控制台: https://console.cloud.tencent.com/smsv2
     * 腾讯云短信小助手: https://cloud.tencent.com/document/product/382/3773#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81 */
    /* 模板名称 */
    req.SetTemplateName("腾讯云");
    /* 模板内容 */
    req.SetTemplateContent("{1}为您的登录验证码，请于{2}分钟内填写，如非本人操作，请忽略本短信。");
    /* 短信类型：0表示普通短信, 1表示营销短信 */
    req.SetSmsType(0);
    /* 是否国际/港澳台短信：
    * 0：表示国内短信
    * 1：表示国际/港澳台短信 */
    req.SetInternational(0);
    /* 模板备注：例如申请原因，使用场景等 */
    req.SetRemark("xxx");

    SmsClient sms_client = SmsClient(cred, "ap-guangzhou", clientProfile);

    // set proxy
    // NetworkProxy proxy = NetworkProxy(NetworkProxy::Type::HTTP, "localhost.proxy.com", 8080);
    // cvm_client.SetNetworkProxy(proxy);

    auto outcome = sms_client.AddSmsTemplate(req);
    if (!outcome.IsSuccess())
    {
        cout << outcome.GetError().PrintAll() << endl;
        TencentCloud::ShutdownAPI();
        return -1;
    }
    AddSmsTemplateResponse rsp = outcome.GetResult();
    cout<<"RequestId="<<rsp.GetRequestId()<<endl;
    cout<<"AddSmsTemplateResponse="<<rsp.ToJsonString()<<endl;
    
    TencentCloud::ShutdownAPI();

    return 0;
}
```
