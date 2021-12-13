SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [短信 API](https://cloud.tencent.com/document/product/382/52077)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。

>!
>
>- 发送短信相关接口
>  一次群发请求最多支持200个号码。
>- 签名、正文模板相关接口
>  个人认证用户不支持使用签名、正文模板相关接口，只能通过短信控制台 [管理短信签名](https://cloud.tencent.com/document/product/382/37794) 和 [管理短信正文模板](https://cloud.tencent.com/document/product/382/37795)。如需使用该类接口，请将 “个人认证” 变更为 “企业认证”，具体操作请参见 [实名认证变更指引](https://cloud.tencent.com/document/product/378/34075)。



## 前提条件

- 已开通短信服务，具体操作请参见 [国内短信快速入门](https://cloud.tencent.com/document/product/382/37745)。
- 如需发送国内短信，需要先 [购买国内短信套餐包](https://cloud.tencent.com/document/product/382/18060)。
- 已准备依赖环境：JDK 7 及以上版本。
- 已在访问管理控制台 >**[API密钥管理](https://console.cloud.tencent.com/cam/capi)**页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 短信的调用地址为`sms.tencentcloudapi.com`。

## 相关资料

- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/382/52077)。
- 下载 SDK 源码请访问 [Java SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-java)。


## 安装 SDK

### 通过 Maven 安装（推荐）

[Maven](https://maven.apache.org) 是 Java 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。

1. 访问 [Maven 官网](https://maven.apache.org/) 下载对应系统 Maven 安装包进行安装。
2. 添加 Maven 依赖项，只需在 Maven pom.xml 添加以下依赖项即可：
>!
>- 版本号仅为示例，请在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 获取最新的版本号并替换。
>- Maven 仓库中显示的 4.0.11 是废弃版本，由于 Maven 索引更新问题尚未完全删除。
<pre><code class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">dependency</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">groupId</span>&gt;</span>com.tencentcloudapi<span class="hljs-tag">&lt;/<span class="hljs-name">groupId</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">artifactId</span>&gt;</span>tencentcloud-sdk-java<span class="hljs-tag">&lt;/<span class="hljs-name">artifactId</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">version</span>&gt;</span>3.1.270<span class="hljs-tag">&lt;/<span class="hljs-name">version</span>&gt;</span><span class="hljs-comment">&lt;!-- 注：这里只是示例版本号（可直接使用），可获取并替换为 <a href="https://mvnrepository.com/artifact/com.tencentcloudapi/tencentcloud-sdk-java">最新的版本号</a>，注意不要使用4.0.x版本（非最新版本） --&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-name">dependency</span>&gt;</span></code></pre>
3. 引用方法可参考 [示例代码](#example)。

### 通过源码包安装

1. [下载](https://github.com/tencentcloud/tencentcloud-sdk-java) 源码压缩包。
2. 解压源码包到您项目中合适的位置。
3. 将 vendor 目录下的 jar 包放在 Java 可找到的路径中。
4. 引用方法可参考 [示例代码](#example)。

## 示例代码[](id:example)

>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。本文仅列举几个常用功能的示例代码，如下所示。

### 发送短信

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;

//导入可选配置类
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;

// 导入对应SMS模块的client
import com.tencentcloudapi.sms.v20210111.SmsClient;

// 导入要请求接口对应的request response类
import com.tencentcloudapi.sms.v20210111.models.SendSmsRequest;
import com.tencentcloudapi.sms.v20210111.models.SendSmsResponse;

/**
 * Tencent Cloud Sms Sendsms
 *
 */
public class SendSms
{
    public static void main(String[] args)
    {
        try {
            /* 必要步骤：
             * 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
             * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
             * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
             * 以免泄露密钥对危及你的财产安全。
             * CAM密匙查询: https://console.cloud.tencent.com/cam/capi*/
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化一个http选项，可选，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            // 设置代理
            // httpProfile.setProxyHost("真实代理ip");
            // httpProfile.setProxyPort(真实代理端口);
            /* SDK默认使用POST方法。
             * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
            httpProfile.setReqMethod("POST");
            /* SDK有默认的超时时间，非必要请不要进行调整
             * 如有需要请在代码中查阅以获取最新的默认值 */
            httpProfile.setConnTimeout(60);
            /* SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
             * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com */
            httpProfile.setEndpoint("sms.tencentcloudapi.com");

            /* 非必要步骤:
             * 实例化一个客户端配置对象，可以指定超时时间等配置 */
            ClientProfile clientProfile = new ClientProfile();
            /* SDK默认用TC3-HMAC-SHA256进行签名
             * 非必要请不要修改这个字段 */
            clientProfile.setSignMethod("HmacSHA256");
            clientProfile.setHttpProfile(httpProfile);
            /* 实例化要请求产品(以sms为例)的client对象
             * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
            SmsClient client = new SmsClient(cred, "ap-guangzhou",clientProfile);
            /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
             * 你可以直接查询SDK源码确定接口有哪些属性可以设置
             * 属性可能是基本类型，也可能引用了另一个数据结构
             * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
            SendSmsRequest req = new SendSmsRequest();

            /* 填充请求参数,这里request对象的成员变量即对应接口的入参
             * 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义
             * 基本类型的设置:
             * 帮助链接：
             * 短信控制台: https://console.cloud.tencent.com/smsv2
             * sms helper: https://cloud.tencent.com/document/product/382/3773 */

            /* 短信应用ID: 短信SdkAppId在 [短信控制台] 添加应用后生成的实际SdkAppId，示例如1400006666 */
            String sdkAppId = "1400009099";
            req.setSmsSdkAppId(sdkAppId);

            /* 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看 */
            String signName = "签名内容";
            req.setSignName(signName);

            /* 国际/港澳台短信 SenderId: 国内短信填空，默认未开通，如需开通请联系 [sms helper] */
            String senderid = "";
            req.setSenderId(senderid);

            /* 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回 */
            String sessionContext = "xxx";
            req.setSessionContext(sessionContext);

            /* 短信号码扩展号: 默认未开通，如需开通请联系 [sms helper] */
            String extendCode = "";
            req.setExtendCode(extendCode);

            /* 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看 */
            String templateId = "400000";
            req.setTemplateId(templateId);

            /* 下发手机号码，采用 E.164 标准，+[国家或地区码][手机号]
             * 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号 */
            String[] phoneNumberSet = {"+8621212313123", "+8612345678902", "+8612345678903"};
            req.setPhoneNumberSet(phoneNumberSet);

            /* 模板参数: 若无模板参数，则设置为空 */
            String[] templateParamSet = {"5678"};
            req.setTemplateParamSet(templateParamSet);

            /* 通过 client 对象调用 SendSms 方法发起请求。注意请求方法名与请求对象是对应的
             * 返回的 res 是一个 SendSmsResponse 类的实例，与请求对象对应 */
            SendSmsResponse res = client.SendSms(req);

            // 输出json格式的字符串回包
            System.out.println(SendSmsResponse.toJsonString(res));

            // 也可以取出单个值，你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
            System.out.println(res.getRequestId());

        } catch (TencentCloudSDKException e) {
            e.printStackTrace();
        }
    }
}
```



### 拉取回执状态

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;

//导入可选配置类
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;

// 导入对应SMS模块的client
import com.tencentcloudapi.sms.v20210111.SmsClient;

// 导入要请求接口对应的request response类
import com.tencentcloudapi.sms.v20210111.models.PullSmsReplyStatusRequest;
import com.tencentcloudapi.sms.v20210111.models.PullSmsReplyStatusResponse;

/**
 * Tencent Cloud Sms PullSmsSendStatus
 *
 */
public class PullSmsSendStatus {
    public static void main(String[] args) {
        try {
            /* 必要步骤：
             * 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
             * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
             * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
             * 以免泄露密钥对危及你的财产安全。
             * CAM密匙查询: https://console.cloud.tencent.com/cam/capi*/
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化一个http选项，可选，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            // 设置代理
            // httpProfile.setProxyHost("真实代理ip");
            // httpProfile.setProxyPort(真实代理端口);
            /* SDK默认使用POST方法。
             * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
            httpProfile.setReqMethod("POST");
            /* SDK有默认的超时时间，非必要请不要进行调整
             * 如有需要请在代码中查阅以获取最新的默认值 */
            httpProfile.setConnTimeout(60);
            /* SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
             * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com */
            httpProfile.setEndpoint("sms.tencentcloudapi.com");

            /* 非必要步骤:
             * 实例化一个客户端配置对象，可以指定超时时间等配置 */
            ClientProfile clientProfile = new ClientProfile();
            /* SDK默认用TC3-HMAC-SHA256进行签名
             * 非必要请不要修改这个字段 */
            clientProfile.setSignMethod("HmacSHA256");
            clientProfile.setHttpProfile(httpProfile);

            /* 实例化要请求产品(以sms为例)的client对象
             * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
            SmsClient client = new SmsClient(cred, "ap-guangzhou", clientProfile);

            /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
             * 你可以直接查询SDK源码确定接口有哪些属性可以设置
             * 属性可能是基本类型，也可能引用了另一个数据结构
             * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
            PullSmsSendStatusRequest req = new PullSmsSendStatusRequest();

            /* 填充请求参数,这里request对象的成员变量即对应接口的入参
             * 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义
             * 基本类型的设置:
             * 帮助链接：
             * 短信控制台: https://console.cloud.tencent.com/smsv2
             * sms helper: https://cloud.tencent.com/document/product/382/3773 */

            /* 短信应用ID: 短信SdkAppId在 [短信控制台] 添加应用后生成的实际SdkAppId，示例如1400006666 */
            String sdkAppId = "1400009099";
            req.setSmsSdkAppId(sdkAppId);

            // 设置拉取最大条数，最多100条
            Long limit = 5L;
            req.setLimit(limit);

            /* 通过 client 对象调用 PullSmsSendStatus 方法发起请求。注意请求方法名与请求对象是对应的
             * 返回的 res 是一个 PullSmsSendStatusResponse 类的实例，与请求对象对应 */
            PullSmsSendStatusResponse res = client.PullSmsSendStatus(req);

            // 输出json格式的字符串回包
            System.out.println(PullSmsSendStatusResponse.toJsonString(res));

        } catch (TencentCloudSDKException e) {
            e.printStackTrace();
        }
    }
}
```


### 统计短信发送数据

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;

//导入可选配置类
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;

// 导入对应SMS模块的client
import com.tencentcloudapi.sms.v20210111.SmsClient;

// 导入要请求接口对应的request response类
import com.tencentcloudapi.sms.v20210111.models.SendStatusStatisticsRequest;
import com.tencentcloudapi.sms.v20210111.models.SendStatusStatisticsResponse;

/**
 * Tencent Cloud Sms SendStatusStatistics
 *
 */
public class SendStatusStatistics {
    public static void main(String[] args) {
        try {
            /* 必要步骤：
             * 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
             * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
             * 你也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
             * 以免泄露密钥对危及你的财产安全。
             * CAM密匙查询: https://console.cloud.tencent.com/cam/capi*/
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化一个http选项，可选，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            // 设置代理
            // httpProfile.setProxyHost("真实代理ip");
            // httpProfile.setProxyPort(真实代理端口);
            /* SDK默认使用POST方法。
             * 如果你一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
            httpProfile.setReqMethod("POST");
            /* SDK有默认的超时时间，非必要请不要进行调整
             * 如有需要请在代码中查阅以获取最新的默认值 */
            httpProfile.setConnTimeout(60);
            /* SDK会自动指定域名。通常是不需要特地指定域名的，但是如果你访问的是金融区的服务
             * 则必须手动指定域名，例如sms的上海金融区域名： sms.ap-shanghai-fsi.tencentcloudapi.com */
            httpProfile.setEndpoint("sms.tencentcloudapi.com");

            /* 非必要步骤:
             * 实例化一个客户端配置对象，可以指定超时时间等配置 */
            ClientProfile clientProfile = new ClientProfile();
            /* SDK默认用TC3-HMAC-SHA256进行签名
             * 非必要请不要修改这个字段 */
            clientProfile.setSignMethod("HmacSHA256");
            clientProfile.setHttpProfile(httpProfile);

            /* 实例化要请求产品(以sms为例)的client对象
             * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
            SmsClient client = new SmsClient(cred, "ap-guangzhou",clientProfile);

            /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
             * 你可以直接查询SDK源码确定接口有哪些属性可以设置
             * 属性可能是基本类型，也可能引用了另一个数据结构
             * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
            SendStatusStatisticsRequest req = new SendStatusStatisticsRequest();

            /* 填充请求参数,这里request对象的成员变量即对应接口的入参
             * 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义
             * 基本类型的设置:
             * 帮助链接：
             * 短信控制台: https://console.cloud.tencent.com/smsv2
             * sms helper: https://cloud.tencent.com/document/product/382/3773 */

            /* 短信应用ID: 短信SdkAppId在 [短信控制台] 添加应用后生成的实际SdkAppId，示例如1400006666 */
            String sdkAppId = "1400009099";
            req.setSmsSdkAppId(sdkAppId);

            // 设置拉取最大条数，最多100条
            Long limit = 5L;
            req.setLimit(limit);
            /* 偏移量 注：目前固定设置为0 */
            Long offset = 0L;
            req.setOffset(offset);
            /* 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时 */
            String beginTime = "2019071100";
            req.setBeginTime(beginTime);
            /* 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
             * 注：EndTime 必须大于 beginTime */
            String endTime = "2019071123";
            req.setEndTime(endTime);

            /* 通过 client 对象调用 SendStatusStatistics 方法发起请求。注意请求方法名与请求对象是对应的
             * 返回的 res 是一个 SendStatusStatisticsResponse 类的实例，与请求对象对应 */
            SendStatusStatisticsResponse res = client.SendStatusStatistics(req);

            // 输出json格式的字符串回包
            System.out.println(SendStatusStatisticsResponse.toJsonString(res));

        } catch (TencentCloudSDKException e) {
            e.printStackTrace();
        }
    }
}
```

### 申请短信模板

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
//导入可选配置类
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
// 导入 SMS 模块的 client
import com.tencentcloudapi.sms.v20210111.SmsClient;
// 导入要请求接口对应的 request response 类
import com.tencentcloudapi.sms.v20210111.models.AddSmsTemplateRequest;
import com.tencentcloudapi.sms.v20210111.models.AddSmsTemplateResponse;
/**
* Tencent Cloud Sms AddSmsTemplate
*
*/
public class AddSmsTemplate
{
  public static void main( String[] args )
  {
      try {
          /* 必要步骤：
           * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
           * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
           * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
           * CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
           */
          Credential cred = new Credential("secretId", "secretKey");
           // 实例化一个 http 选项，可选，无特殊需求时可以跳过
          HttpProfile httpProfile = new HttpProfile();
          // 设置代理
          // httpProfile.setProxyHost("真实代理ip");
          // httpProfile.setProxyPort(真实代理端口);
          /* SDK 默认使用 POST 方法
           * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
          httpProfile.setReqMethod("POST");
          /* SDK 有默认的超时时间，非必要请不要进行调整
           * 如有需要请在代码中查阅以获取最新的默认值 */
          httpProfile.setConnTimeout(60);
          /* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
           * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
          httpProfile.setEndpoint("sms.tencentcloudapi.com");
           /* 非必要步骤:
           * 实例化一个客户端配置对象，可以指定超时时间等配置 */
          ClientProfile clientProfile = new ClientProfile();
          /* SDK 默认使用 TC3-HMAC-SHA256 进行签名
           * 非必要请不要修改该字段 */
          clientProfile.setSignMethod("HmacSHA256");
          clientProfile.setHttpProfile(httpProfile);
          /* 实例化 SMS 的 client 对象
           * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
          SmsClient client = new SmsClient(cred, "ap-guangzhou", clientProfile);
          /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
           * 您可以直接查询 SDK 源码确定接口有哪些属性可以设置
           * 属性可能是基本类型，也可能引用了另一个数据结构
           * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
          AddSmsTemplateRequest req = new AddSmsTemplateRequest();
           /* 填充请求参数，这里 request 对象的成员变量即对应接口的入参
           * 您可以通过官网接口文档或跳转到 request 对象的定义处查看请求参数的定义
           * 基本类型的设置:
           * 帮助链接：
           * 短信控制台：https://console.cloud.tencent.com/smsv2
           * sms helper：https://cloud.tencent.com/document/product/382/3773 */
           /* 模板名称*/
          String templatename = "腾讯云";
          req.setTemplateName(templatename);
           /* 模板内容 */
          String templatecontent = "{1}为您的登录验证码，请于{2}分钟内填写，如非本人操作，请忽略本短信。";
          req.setTemplateContent(templatecontent);
           /* 短信类型：0表示普通短信, 1表示营销短信 */
          long smstype = 0;
          req.setSmsType(smstype);
           /* 是否国际/港澳台短信：0：表示国内短信，1：表示国际/港澳台短信。 */
          long international = 0;
          req.setInternational(international);
           /* 模板备注：例如申请原因，使用场景等 */
          String remark = "xxx";
          req.setRemark(remark);
           /* 通过 client 对象调用 AddSmsTemplate 方法发起请求。注意请求方法名与请求对象是对应的
           * 返回的 res 是一个 AddSmsTemplateResponse 类的实例，与请求对象对应 */
          AddSmsTemplateResponse res = client.AddSmsTemplate(req);
           // 输出 JSON 格式的字符串回包
          System.out.println(AddSmsTemplateResponse.toJsonString(res));
           // 可以取出单个值，您可以通过官网接口文档或跳转到 response 对象的定义处查看返回字段的定义
          System.out.println(res.getRequestId());
       } catch (TencentCloudSDKException e) {
          e.printStackTrace();
      }
  }
}
```

## 常见问题
<dx-accordion>
::: 更新仓库\spom.xml\s文件里面的依赖失败
可能是因为本机配置了代理，而工具在更新时未进行代理的配置导致，按照上文在命令端更新依赖，如果还是失败，这时候需要看是否因为网络不通还是防火墙拦截。
:::
::: 运行示例失败
`[TencentCloudSDKException]message:java.net.ConnectException-Connection timed out: connect requestId:`这里需要排查：是否本机配置了代理，而未在代码中加入代理，代理的加入可参考：
```
HttpProfile httpProfile = new HttpProfile();
httpProfile.setProxyHost("真实代理ip");
httpProfile.setProxyPort(真实代理端口);
```
:::
::: 版本升级
请注意，从3.0.x版本升级到3.1.x版本有兼容性问题，对于 Integer 字段的使用修改为了 Long 类型，需要重新编译项目。
:::
::: 依赖冲突
目前，SDK 依赖 okhttp 2.5.0，如果和其他依赖 okhttp3 的包混用时，有可能会报错：如`Exception in thread "main" java.lang.NoSuchMethodError: okio.BufferedSource.rangeEquals(JLokio/ByteString;)Z`。

原因是 okhttp3 依赖 okio 1.12.0，而 okhttp 依赖 okio 1.6.0，maven 在解析依赖时的规则是路径最短优先和顺序优先，所以如果 SDK 在 pom.xml 依赖中先被声明，则 okio 1.6.0 会被使用，从而报错。

在 SDK 没有升级到 okhttp3 前的解决办法：
1. 在 pom.xml 中明确指定依赖 okio 1.12.0 版本（注意可能有其他包需要用到更高的版本，变通下取最高版本即可）。
2. 将 SDK 放在依赖的最后（注意如果此前已经编译过，则需要先删除掉 maven 缓存的 okhttp 包），以同时使用依赖 okhttp3 的 CMQ SDK 为例，形如（注意变通版本号）： 
```xml
    <dependency>
      <groupId>com.qcloud</groupId>
      <artifactId>cmq-http-client</artifactId>
      <version>1.0.7</version>
    </dependency>
    <dependency>
      <groupId>com.tencentcloudapi</groupId>
      <artifactId>tencentcloud-sdk-java</artifactId>
      <version>3.1.59</version>
    </dependency>
```
:::
::: 证书问题
证书问题通常是客户端环境配置错误导致的。SDK 没有对证书进行操作，依赖的是 Java 运行环境本身的处理。出现证书问题后，可以使用`-Djavax.net.debug=ssl`开启详细日志辅助判断。

有用户报告使用 IBM JDK 1.8 出现证书报错：`javax.net.ssl.SSLHandshakeException: Received fatal alert: handshake_failure`，使用 Oracle JDK 后问题消失。

:::
</dx-accordion>
