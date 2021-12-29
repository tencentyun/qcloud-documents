SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [短信 API](https://cloud.tencent.com/document/product/382/38764)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送短信相关接口
>一次群发请求最多支持200个号码。
>- 签名、正文模板相关接口
>个人认证用户不支持使用签名、正文模板相关接口，只能通过短信控制台 [管理短信签名](https://cloud.tencent.com/document/product/382/37794) 和 [管理短信正文模板](https://cloud.tencent.com/document/product/382/37795)。如需使用该类接口，请将 “个人认证” 变更为 “企业认证”，具体操作请参见 [实名认证变更指引](https://cloud.tencent.com/document/product/378/34075)。


## 前提条件

- 已开通短信服务，具体操作请参见 [国内短信快速入门](https://cloud.tencent.com/document/product/382/37745)。
- 如需发送国内短信，需要先 [购买国内短信套餐包](https://cloud.tencent.com/document/product/382/18060)。
- 已准备依赖环境：Go 1.9版本及以上。
- 已在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 短信的调用地址为`sms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/382/38764)。
- 下载 SDK 源码请访问 [Golang SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-go)。

## 安装 SDK
### 通过 go get 安装（推荐）
推荐使用语言自带的工具安装 SDK：
```
 go get -u github.com/tencentcloud/tencentcloud-sdk-go
```

### 通过源码安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-go) 或 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-go/tencentcloud-sdk-go.zip) 下载最新代码。
2. 解压后安装到`$GOPATH/src/github.com/tencentcloud`目录下。

## 示例代码
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2019-07-11&Action=SendSms) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。本文仅列举几个常用功能的示例代码，如下所示。
### 申请短信模板
```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	sms "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sms/v20190711"//引入sms
)

func main() {
	/* 必要步骤：
     * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
     * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
     * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
     * CAM 密匙查询: https://console.cloud.tencent.com/cam/capi
     */
	credential := common.NewCredential(
		// os.Getenv("TENCENTCLOUD_SECRET_ID"),
		// os.Getenv("TENCENTCLOUD_SECRET_KEY"),
		"xxx",
		"xxx",
	)
	/* 非必要步骤:
	 * 实例化一个客户端配置对象，可以指定超时时间等配置 */
	cpf := profile.NewClientProfile()

	/* SDK 默认使用 POST 方法
	 * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
	cpf.HttpProfile.ReqMethod = "POST"

	/* SDK 有默认的超时时间，非必要请不要进行调整
	 * 如有需要请在代码中查阅以获取最新的默认值 */
	//cpf.HttpProfile.ReqTimeout = 5

	/* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
     * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
	cpf.HttpProfile.Endpoint = "sms.tencentcloudapi.com"

	/* SDK 默认用 TC3-HMAC-SHA256 进行签名，非必要请不要修改该字段 */
	cpf.SignMethod = "HmacSHA1"

	/* 实例化 SMS 的 client 对象
     * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
	client, _ := sms.NewClient(credential, "ap-guangzhou", cpf)

	/* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	* 您可以直接查询 SDK 源码确定接口有哪些属性可以设置
	 * 属性可能是基本类型，也可能引用了另一个数据结构
	 * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
	request := sms.NewAddSmsTemplateRequest()

	/* 基本类型的设置:
	 * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值。
	 * SDK 提供对基本类型的指针引用封装函数
	 * 帮助链接：
	 * 短信控制台：https://console.cloud.tencent.com/smsv2
	 * sms helper：https://cloud.tencent.com/document/product/382/3773
	 */

	/* 模板名称 */
	request.TemplateName = common.StringPtr("腾讯云")
	/* 模板内容 */
	request.TemplateContent = common.StringPtr("{1}为您的登录验证码，请于{2}分钟内填写，如非本人操作，请忽略本短信。")
	/* 短信类型：0表示普通短信, 1表示营销短信 */
	request.SmsType = common.Uint64Ptr(0)
	/* 是否国际/港澳台短信：
	   0：表示国内短信
	   1：表示国际/港澳台短信 */
	request.International = common.Uint64Ptr(0)
	/* 模板备注：例如申请原因，使用场景等 */
	request.Remark = common.StringPtr("xxx")

	// 通过 client 对象调用想要访问的接口，需要传入请求对象
	response, err := client.AddSmsTemplate(request)
	// 处理异常
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	// 非 SDK 异常，直接失败。实际代码中可以加入其他的处理
	if err != nil {
		panic(err)
	}
	b, _ := json.Marshal(response.Response)
	// 打印返回的 JSON 字符串
	fmt.Printf("%s", b)
}
```

### 发送短信

```
package main

import (
	"encoding/json"
	"fmt"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	sms "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sms/v20190711"//引入sms
)

func main() {
	/* 必要步骤：
     * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
     * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
     * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
     * CAM 密匙查询: https://console.cloud.tencent.com/cam/capi
     */
	credential := common.NewCredential(
		// os.Getenv("TENCENTCLOUD_SECRET_ID"),
		// os.Getenv("TENCENTCLOUD_SECRET_KEY"),
		"xxx",
		"xxx",
	)
	/* 非必要步骤:
	 * 实例化一个客户端配置对象，可以指定超时时间等配置 */
	cpf := profile.NewClientProfile()

	/* SDK 默认使用 POST 方法
	 * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
	cpf.HttpProfile.ReqMethod = "POST"

	/* SDK 有默认的超时时间，非必要请不要进行调整
	 * 如有需要请在代码中查阅以获取最新的默认值 */
	//cpf.HttpProfile.ReqTimeout = 5

	/* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
     * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
	cpf.HttpProfile.Endpoint = "sms.tencentcloudapi.com"

	/* SDK 默认用 TC3-HMAC-SHA256 进行签名，非必要请不要修改该字段 */
	cpf.SignMethod = "HmacSHA1"

	/* 实例化 SMS 的 client 对象
     * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
	client, _ := sms.NewClient(credential, "ap-guangzhou", cpf)

	/* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	* 您可以直接查询 SDK 源码确定接口有哪些属性可以设置
	 * 属性可能是基本类型，也可能引用了另一个数据结构
	 * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
	request := sms.NewSendSmsRequest()

	/* 基本类型的设置:
	 * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值。
	 * SDK 提供对基本类型的指针引用封装函数
	 * 帮助链接：
	 * 短信控制台：https://console.cloud.tencent.com/smsv2
	 * sms helper：https://cloud.tencent.com/document/product/382/3773
	 */

	/* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666 */
	request.SmsSdkAppid = common.StringPtr("1400787878")
	/* 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，可登录 [短信控制台] 查看签名信息 */
	request.Sign = common.StringPtr("xxx")
	/* 国际/港澳台短信 senderid: 国内短信填空，默认未开通，如需开通请联系 [sms helper] */
	request.SenderId = common.StringPtr("")
	/* 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回 */
	request.SessionContext = common.StringPtr("xxx")
	/* 短信码号扩展号: 默认未开通，如需开通请联系 [sms helper] */
	request.ExtendCode = common.StringPtr("")
	/* 模板参数: 若无模板参数，则设置为空*/
	request.TemplateParamSet = common.StringPtrs([]string{"0"})
	/* 模板 ID: 必须填写已审核通过的模板 ID，可登录 [短信控制台] 查看模板 ID */
	request.TemplateID = common.StringPtr("449739")
	/* 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号]
	 * 例如+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号*/
	request.PhoneNumberSet = common.StringPtrs([]string{"+8613711112222", "+8613711333222", "+8613711144422"})


	// 通过 client 对象调用想要访问的接口，需要传入请求对象
	response, err := client.SendSms(request)
	// 处理异常
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	// 非 SDK 异常，直接失败。实际代码中可以加入其他的处理
	if err != nil {
		panic(err)
	}
	b, _ := json.Marshal(response.Response)
	// 打印返回的 JSON 字符串
	fmt.Printf("%s", b)
}
```

### 拉取回执状态

```
package main

import (
	"encoding/json"
	"fmt"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	sms "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sms/v20190711"//引入sms
)

func main() {
	/* 必要步骤：
     * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
     * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
     * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
     * CAM 密匙查询: https://console.cloud.tencent.com/cam/capi
     */
	credential := common.NewCredential(
		// os.Getenv("TENCENTCLOUD_SECRET_ID"),
		// os.Getenv("TENCENTCLOUD_SECRET_KEY"),
		"xxx",
		"xxx",
	)
	/* 非必要步骤:
	 * 实例化一个客户端配置对象，可以指定超时时间等配置 */
	cpf := profile.NewClientProfile()

	/* SDK 默认使用 POST 方法
	 * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
	cpf.HttpProfile.ReqMethod = "POST"

	/* SDK 有默认的超时时间，非必要请不要进行调整
	 * 如有需要请在代码中查阅以获取最新的默认值 */
	//cpf.HttpProfile.ReqTimeout = 5

	/* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
     * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
	cpf.HttpProfile.Endpoint = "sms.tencentcloudapi.com"

	/* SDK 默认用 TC3-HMAC-SHA256 进行签名
	 * 非必要请不要修改该字段 */
	cpf.SignMethod = "HmacSHA1"

	/* 实例化 SMS 的 client 对象
     * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
	client, _ := sms.NewClient(credential, "ap-guangzhou", cpf)

	/* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	 * 您可以直接查询 SDK 源码确定接口有哪些属性可以设置
	 * 属性可能是基本类型，也可能引用了另一个数据结构
	 * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
	request := sms.NewPullSmsSendStatusRequest()

	/* 基本类型的设置:
	 * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值。
	 * SDK 提供对基本类型的指针引用封装函数
	 * 帮助链接：
	 * 短信控制台：https://console.cloud.tencent.com/smsv2
	 * sms helper：https://cloud.tencent.com/document/product/382/3773
	 */

	/* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666 */
	request.SmsSdkAppid = common.StringPtr("1400787878")
	/* 拉取最大条数，最多100条 */
	request.Limit = common.Uint64Ptr(10)

	// 通过 client 对象调用想要访问的接口，需要传入请求对象
	response, err := client.PullSmsSendStatus(request)
	// 处理异常
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	// 非 SDK 异常，直接失败。实际代码中可以加入其他的处理
	if err != nil {
		panic(err)
	}
	b, _ := json.Marshal(response.Response)
	// 打印返回的 JSON 字符串
	fmt.Printf("%s", b)
}
```

### 统计短信发送数据

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	sms "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/sms/v20190711" //引入sms
)

func main() {
	/* 必要步骤：
     * 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
     * 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
     * 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
     * CAM 密匙查询: https://console.cloud.tencent.com/cam/capi
     */
	credential := common.NewCredential(
		// os.Getenv("TENCENTCLOUD_SECRET_ID"),
		// os.Getenv("TENCENTCLOUD_SECRET_KEY"),
		"xxx",
		"xxx",
	)
	/* 非必要步骤:
	 * 实例化一个客户端配置对象，可以指定超时时间等配置 */
	cpf := profile.NewClientProfile()

	/* SDK 默认使用 POST 方法
	 * 如需使用 GET 方法，可以在此处设置，但 GET 方法无法处理较大的请求 */
	cpf.HttpProfile.ReqMethod = "POST"

	/* SDK 有默认的超时时间，非必要请不要进行调整
	 * 如有需要请在代码中查阅以获取最新的默认值 */
	//cpf.HttpProfile.ReqTimeout = 5

	/* SDK 会自动指定域名，通常无需指定域名，但访问金融区的服务时必须手动指定域名
     * 例如 SMS 的上海金融区域名为 sms.ap-shanghai-fsi.tencentcloudapi.com */
	cpf.HttpProfile.Endpoint = "sms.tencentcloudapi.com"

	/* SDK 默认用 TC3-HMAC-SHA256 进行签名
	 * 非必要请不要修改该字段 */
	cpf.SignMethod = "HmacSHA1"

	/* 实例化 SMS 的 client 对象
     * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
	client, _ := sms.NewClient(credential, "ap-guangzhou", cpf)

	/* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	 * 您可以直接查询 SDK 源码确定接口有哪些属性可以设置
	 * 属性可能是基本类型，也可能引用了另一个数据结构
	 * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
	request := sms.NewSendStatusStatisticsRequest()

	/* 基本类型的设置:
	 * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值。
	 * SDK 提供对基本类型的指针引用封装函数
	 * 帮助链接：
	 * 短信控制台：https://console.cloud.tencent.com/smsv2
	 * sms helper：https://cloud.tencent.com/document/product/382/3773
	 */

	/* 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666 */
	request.SmsSdkAppid = common.StringPtr("1400787878")
	/* 拉取最大条数，最多100条 */
	request.Limit = common.Uint64Ptr(0)
	/* 偏移量，目前固定设置为0 */
	request.Offset = common.Uint64Ptr(0)
	/* 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时 */
	request.StartDateTime = common.Uint64Ptr(2019122400)
	/* 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
	 * 注：EndDataTime 必须大于 StartDateTime */
	request.EndDataTime = common.Uint64Ptr(2019122523)

	// 通过 client 对象调用想要访问的接口，需要传入请求对象
	response, err := client.SendStatusStatistics(request)
	// 处理异常
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	// 非 SDK 异常，直接失败。实际代码中可以加入其他的处理
	if err != nil {
		panic(err)
	}
	b, _ := json.Marshal(response.Response)
	// 打印返回的 JSON 字符串
	fmt.Printf("%s", b)
}
```

## 常见问题
<dx-accordion>
::: 代理设置
如有代理的环境下，需要设置系统环境变量 `https_proxy` ，否则可能无法正常调用，抛出连接超时的异常现象。
:::
::: 开启\sDNS\s缓存
当前 GO SDK 总是会去请求 DNS 服务器，而没有使用到 nscd 的缓存，可以通过导出环境变量`GODEBUG=netdns=cgo`，或者`go build`编译时指定参数`-tags 'netcgo'`控制读取 nscd 缓存。
:::
::: 忽略服务器证书校验
虽然使用 SDK 调用公有云服务时，必须校验服务器证书，以识别他人伪装的服务器，确保请求的安全。但某些极端情况下，例如测试时，您可能会需要忽略自签名的服务器证书。以下是其中一种可能的方法：

```
import "crypto/tls"
...
    client, _ := cvm.NewClient(credential, regions.Guangzhou, cpf)
    tr := &http.Transport{
        TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
    }
    client.WithHttpTransport(tr)
...
```

>!除非您知道自己在进行何种操作，并明白由此带来的风险，否则不要尝试关闭服务器证书校验。
:::
::: import\s导包失败
例如报错：`imported and not used: "os"`，说明“ os ”这个包并未在代码中使用到，去掉即可。
:::
</dx-accordion>
