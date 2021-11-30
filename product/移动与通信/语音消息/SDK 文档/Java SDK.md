SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [语音消息 API](https://cloud.tencent.com/document/product/1128/51569)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送语音验证码
>只需提供验证码数字，如需自定义内容，可以 [发送语音通知](#指定模板发送语音通知)。例如，当 msg=“5678” 时，您收到的语音通知为`您的语音验证码是五六七八。`。
>- 发送语音通知
>数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。例如，当 msg=`您的语音验证码是5678。` 时，您收到的语音通知为`您的语音验证码是五千六百七十八。`，当 msg=`您的语音验证码是5,6,7,8。`时，您收到的语音通知为`您的语音验证码是五六七八。`。



## 前提条件

- 已开通语音消息服务，具体操作请参见 [快速入门](https://cloud.tencent.com/document/product/1128/37343)。
- 已准备依赖环境：JDK 7 版本及以上。
- 已在访问管理控制台 >**[API密钥管理](https://console.cloud.tencent.com/cam/capi)**页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 语音消息的调用地址为`vms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/1128/51569)。
- 下载 SDK 源码请访问 [Java SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-java)。

## 安装 SDK

### 通过 Maven 安装（推荐）

[Maven](https://maven.apache.org) 是 Java 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。

1. 访问 [Maven 官网](https://maven.apache.org/) 下载对应系统 Maven 安装包进行安装。
2. 添加 Maven 依赖项，只需在 Maven pom.xml 添加以下依赖项即可：

 >!版本号仅为示例，请在 [Maven 仓库](https://search.maven.org/search?q=tencentcloud-sdk-java) 获取最新的版本号并替换。

<pre><code class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-name">dependency</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">groupId</span>&gt;</span>com.tencentcloudapi<span class="hljs-tag">&lt;/<span class="hljs-name">groupId</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">artifactId</span>&gt;</span>tencentcloud-sdk-java<span class="hljs-tag">&lt;/<span class="hljs-name">artifactId</span>&gt;</span>
        <span class="hljs-tag">&lt;<span class="hljs-name">version</span>&gt;</span>3.1.188<span class="hljs-tag">&lt;/<span class="hljs-name">version</span>&gt;</span><span class="hljs-comment">&lt;!-- 注：这里只是示例版本号，请获取并替换为 <a href="https://mvnrepository.com/artifact/com.tencentcloudapi/tencentcloud-sdk-java">最新的版本号</a> --&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-name">dependency</span>&gt;</span></code></pre>

3. 引用方法可参考 [示例代码](#example)。

### 通过源码包安装

1. [下载](https://github.com/tencentcloud/tencentcloud-sdk-java) 源码压缩包。
2. 解压源码包到您项目中合适的位置。
3. 将 vendor 目录下的 jar 包放在 Java 可找到的路径中。
4. 引用方法可参考 [示例代码](#example)。


## 示例代码[](id:example)

>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=vms&Version=2020-09-02&Action=SendCodeVoice) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。示例代码如下所示。

### 发送语音验证码

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;

// 导入可选配置类
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;

// 导入对应VMS模块的client
import com.tencentcloudapi.vms.v20200902.VmsClient;

// 导入要请求接口对应的request response类
import com.tencentcloudapi.vms.v20200902.models.SendCodeVoiceRequest;
import com.tencentcloudapi.vms.v20200902.models.SendCodeVoiceResponse;

/**
 * Tencent Cloud Vms SendCodeVoice
 * https://cloud.tencent.com/document/product/1128/51559
 *
 */

public class SendCodeVoice
{
    public static void main(String[] args)
    {
        try {
            /* 必要步骤：
             * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId，secretKey。
             * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
             * 您也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
             * 以免泄露密钥对危及您的财产安全。
             * CAM密匙查询: https://console.cloud.tencent.com/cam/capi*/
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化一个http选项，可选，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            // 设置代理
            // httpProfile.setProxyHost("host");
            // httpProfile.setProxyPort(port);
            /* SDK默认使用POST方法。
             * 如果您一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
            httpProfile.setReqMethod("POST");
            /* SDK有默认的超时时间，非必要请不要进行调整
             * 如有需要请在代码中查阅以获取最新的默认值 */
            httpProfile.setConnTimeout(60);
            /* SDK会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务
             * 则必须手动指定域名，例如vms的上海金融区域名： vms.ap-shanghai-fsi.tencentcloudapi.com */
            httpProfile.setEndpoint("vms.tencentcloudapi.com");

            /* 非必要步骤:
             * 实例化一个客户端配置对象，可以指定超时时间等配置 */
            ClientProfile clientProfile = new ClientProfile();
            /* SDK默认用TC3-HMAC-SHA256进行签名
             * 非必要请不要修改这个字段 */
            clientProfile.setSignMethod("TC3-HMAC-SHA256");
            clientProfile.setHttpProfile(httpProfile);
            /* 实例化要请求产品(以vms为例)的client对象
             * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
            VmsClient client = new VmsClient(cred, "ap-guangzhou", clientProfile);
            /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
             * 您可以直接查询SDK源码确定接口有哪些属性可以设置
             * 属性可能是基本类型，也可能引用了另一个数据结构
             * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
            SendCodeVoiceRequest req = new SendCodeVoiceRequest();

            /* 填充请求参数,这里request对象的成员变量即对应接口的入参
             * 您可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义
             * 基本类型的设置:
             * 帮助链接：
             * 语音消息控制台：https://console.cloud.tencent.com/vms
             * vms helper：https://cloud.tencent.com/document/product/1128/37720 */

            // 验证码，仅支持填写数字，实际播报语音时，会自动在数字前补充语音文本"您的验证码是"
            String codeMessage = "1234";
            req.setCodeMessage(codeMessage);

            /* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
             * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号 */
            String calledNumber = "+8613711112222";
            req.setCalledNumber(calledNumber);

            // 在 [语音控制台] 添加应用后生成的实际SdkAppid，示例如1400006666
            String voiceSdkAppid = "1400006666";
            req.setVoiceSdkAppid(voiceSdkAppid);

            // 播放次数，可选，最多3次，默认2次
            Long playTimes = 2L;
            req.setPlayTimes(playTimes);

            // 用户的 session 内容，腾讯 server 回包中会原样返回
            String sessionContext = "xxxx";
            req.setSessionContext(sessionContext);

            /* 通过 client 对象调用 SendCodeVoice 方法发起请求。注意请求方法名与请求对象是对应的
             * 返回的 res 是一个 SendCodeVoiceResponse 类的实例，与请求对象对应 */
            SendCodeVoiceResponse res = client.SendCodeVoice(req);

            // 输出json格式的字符串回包
            System.out.println(SendCodeVoiceResponse.toJsonString(res));

            // 也可以取出单个值，您可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
            System.out.println(res.getRequestId());

        } catch (TencentCloudSDKException e) {
            e.printStackTrace();
        }
    }
}
```

### 指定模版发送语音通知[](id:SendTtsVoice)

```
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;

// 导入可选配置类
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;

// 导入对应VMS模块的client
import com.tencentcloudapi.vms.v20200902.VmsClient;

// 导入要请求接口对应的request response类
import com.tencentcloudapi.vms.v20200902.models.SendTtsVoiceRequest;
import com.tencentcloudapi.vms.v20200902.models.SendTtsVoiceResponse;

/**
 * Tencent Cloud Vms SendTtsVoice
 * https://cloud.tencent.com/document/product/1128/51558
 *
 */

public class SendTtsVoice
{
    public static void main(String[] args)
    {
        try {
            /* 必要步骤：
             * 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey。
             * 这里采用的是从环境变量读取的方式，需要在环境变量中先设置这两个值。
             * 您也可以直接在代码中写死密钥对，但是小心不要将代码复制、上传或者分享给他人，
             * 以免泄露密钥对危及您的财产安全。
             * CAM密匙查询: https://console.cloud.tencent.com/cam/capi*/
            Credential cred = new Credential("secretId", "secretKey");

            // 实例化一个http选项，可选，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            // 设置代理
            // httpProfile.setProxyHost("host");
            // httpProfile.setProxyPort(port);
            /* SDK默认使用POST方法。
             * 如果您一定要使用GET方法，可以在这里设置。GET方法无法处理一些较大的请求 */
            httpProfile.setReqMethod("POST");
            /* SDK有默认的超时时间，非必要请不要进行调整
             * 如有需要请在代码中查阅以获取最新的默认值 */
            httpProfile.setConnTimeout(60);
            /* SDK会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务
             * 则必须手动指定域名，例如vms的上海金融区域名： vms.ap-shanghai-fsi.tencentcloudapi.com */
            httpProfile.setEndpoint("vms.tencentcloudapi.com");

            /* 非必要步骤:
             * 实例化一个客户端配置对象，可以指定超时时间等配置 */
            ClientProfile clientProfile = new ClientProfile();
            /* SDK默认用TC3-HMAC-SHA256进行签名
             * 非必要请不要修改这个字段 */
            clientProfile.setSignMethod("TC3-HMAC-SHA256");
            clientProfile.setHttpProfile(httpProfile);
            /* 实例化要请求产品(以vms为例)的client对象
             * 第二个参数是地域信息，可以直接填写字符串ap-guangzhou，或者引用预设的常量 */
            VmsClient client = new VmsClient(cred, "ap-guangzhou", clientProfile);
            /* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
             * 您可以直接查询SDK源码确定接口有哪些属性可以设置
             * 属性可能是基本类型，也可能引用了另一个数据结构
             * 推荐使用IDE进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明 */
            SendTtsVoiceRequest req = new SendTtsVoiceRequest();

            /* 填充请求参数,这里request对象的成员变量即对应接口的入参
             * 您可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义
             * 基本类型的设置:
             * 帮助链接：
             * 语音消息控制台：https://console.cloud.tencent.com/vms
             * vms helper：https://cloud.tencent.com/document/product/1128/37720 */

            // 模板 ID，必须填写在控制台审核通过的模板 ID，可登录 [语音消息控制台] 查看模板 ID
            String templateId = "4356";
            req.setTemplateId(templateId);

            // 模板参数，若模板没有参数，请提供为空数组
            String[] templateParamSet = {"7652"};
            req.setTemplateParamSet(templateParamSet);

            /* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
             * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号 */
            String calledNumber = "+8613711112222";
            req.setCalledNumber(calledNumber);

            // 在 [语音控制台] 添加应用后生成的实际SdkAppid，示例如1400006666
            String voiceSdkAppid = "1400006666";
            req.setVoiceSdkAppid(voiceSdkAppid);

            // 播放次数，可选，最多3次，默认2次
            Long playTimes = 2L;
            req.setPlayTimes(playTimes);

            // 用户的 session 内容，腾讯 server 回包中会原样返回
            String sessionContext = "xxxx";
            req.setSessionContext(sessionContext);

            /* 通过 client 对象调用 SendTtsVoice 方法发起请求。注意请求方法名与请求对象是对应的
             * 返回的 res 是一个 SendTtsVoiceResponse 类的实例，与请求对象对应 */
            SendTtsVoiceResponse res = client.SendTtsVoice(req);

            // 输出json格式的字符串回包
            System.out.println(SendTtsVoiceResponse.toJsonString(res));

            // 也可以取出单个值，您可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义
            System.out.println(res.getRequestId());

        } catch (TencentCloudSDKException e) {
            e.printStackTrace();
        }
    }
}
```
