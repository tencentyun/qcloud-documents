SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [语音消息 API](https://cloud.tencent.com/document/product/1128/51569)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送语音验证码
>只需提供验证码数字，如需自定义内容，可以 [发送语音通知](#指定模板发送语音通知)。例如，当 msg=“5678” 时，您收到的语音通知为`您的语音验证码是五六七八。`。
>- 发送语音通知
>数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。例如，当 msg=`您的语音验证码是5678。` 时，您收到的语音通知为`您的语音验证码是五千六百七十八。`，当 msg=`您的语音验证码是5,6,7,8。`时，您收到的语音通知为`您的语音验证码是五六七八。`。



## 前提条件

- 已开通语音消息服务，具体操作请参见 [快速入门](https://cloud.tencent.com/document/product/1128/37343)。
- 已准备依赖环境：Go 1.9 版本及以上。
- 已在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 语音消息的调用地址为`vms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/1128/51569)。
- 下载 SDK 源码请访问 [Go SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-go)。

## 安装 SDK
### 通过 go get 安装（推荐）
推荐使用语言自带的工具安装 SDK：
```
 go get -u github.com/tencentcloud/tencentcloud-sdk-go
```

### 通过源码安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-go) 或 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-go/tencentcloud-sdk-go.zip) 下载最新代码。
2. 解压后安装到`$GOPATH/src/github.com/tencentcloud`目录下。

## 示例代码[](id:example)

>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=vms&Version=2020-09-02&Action=SendCodeVoice) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。示例代码如下所示。

### 发送语音验证码

```
package main

import (
	"encoding/json"
	"fmt"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	vms "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/vms/v20200902" // 引入 vms
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
		"secretId",
		"secretKey",
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
	 * 例如 VMS 的上海金融区域名为 vms.ap-shanghai-fsi.tencentcloudapi.com */
	cpf.HttpProfile.Endpoint = "vms.tencentcloudapi.com"

	/* SDK 默认用 TC3-HMAC-SHA256 进行签名，非必要请不要修改该字段 */
	cpf.SignMethod = "TC3-HMAC-SHA256"

	/* 实例化 VMS 的 client 对象
	 * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
	client, _ := vms.NewClient(credential, "ap-guangzhou", cpf)

	/* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	   * 您可以直接查询 SDK 源码确定接口有哪些属性可以设置
	    * 属性可能是基本类型，也可能引用了另一个数据结构
	    * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
	request := vms.NewSendCodeVoiceRequest()

	/* 基本类型的设置:
	 * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值。
	 * SDK 提供对基本类型的指针引用封装函数
	 * 帮助链接：
	 * 语音消息控制台：https://console.cloud.tencent.com/vms
	 * vms helper：https://cloud.tencent.com/document/product/1128/37720
	 */

	// 验证码，仅支持填写数字，实际播报语音时，会自动在数字前补充语音文本"您的验证码是"
	request.CodeMessage = common.StringPtr("1234")
	/* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
	 * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号
	 */
	request.CalledNumber = common.StringPtr("+8613711112222")
	// 在语音控制台添加应用后生成的实际SdkAppid，示例如1400006666
	request.VoiceSdkAppid = common.StringPtr("1400006666")
	// 播放次数，可选，最多3次，默认2次
	request.PlayTimes = common.Uint64Ptr(2)
	// 用户的 session 内容，腾讯 server 回包中会原样返回
	request.SessionContext = common.StringPtr("xxxx")

	// 通过 client 对象调用想要访问的接口，需要传入请求对象
	response, err := client.SendCodeVoice(request)
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


### 指定模版发送语音通知[](id:SendTtsVoice)

```
package main

import (
	"encoding/json"
	"fmt"

	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	vms "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/vms/v20200902" // 引入 vms
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
		"secretId",
		"secretKey",
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
	 * 例如 VMS 的上海金融区域名为 vms.ap-shanghai-fsi.tencentcloudapi.com */
	cpf.HttpProfile.Endpoint = "vms.tencentcloudapi.com"

	/* SDK 默认用 TC3-HMAC-SHA256 进行签名，非必要请不要修改该字段 */
	cpf.SignMethod = "TC3-HMAC-SHA256"

	/* 实例化 VMS 的 client 对象
	 * 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量 */
	client, _ := vms.NewClient(credential, "ap-guangzhou", cpf)

	/* 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
	   * 您可以直接查询 SDK 源码确定接口有哪些属性可以设置
	    * 属性可能是基本类型，也可能引用了另一个数据结构
	    * 推荐使用 IDE 进行开发，可以方便地跳转查阅各个接口和数据结构的文档说明 */
	request := vms.NewSendTtsVoiceRequest()

	/* 基本类型的设置:
	 * SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值。
	 * SDK 提供对基本类型的指针引用封装函数
	 * 帮助链接：
	 * 语音消息控制台：https://console.cloud.tencent.com/vms
	 * vms helper：https://cloud.tencent.com/document/product/1128/37720
	 */

	// 模板 ID，必须填写在控制台审核通过的模板 ID，可登录 [语音消息控制台] 查看模板 ID
	request.TemplateId = common.StringPtr("4356")
	// 模板参数，若模板没有参数，请提供为空数组
	request.TemplateParamSet = common.StringPtrs([]string{"7652"})
	/* 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]
	 * 例如：+8613711112222，其中前面有一个+号，86为国家码，13711112222为手机号
	 */
	request.CalledNumber = common.StringPtr("+8613711112222")
	// 在语音控制台添加应用后生成的实际SdkAppid，示例如1400006666
	request.VoiceSdkAppid = common.StringPtr("1400006666")
	// 播放次数，可选，最多3次，默认2次
	request.PlayTimes = common.Uint64Ptr(2)
	// 用户的 session 内容，腾讯 server 回包中会原样返回
	request.SessionContext = common.StringPtr("xxxx")

	// 通过 client 对象调用想要访问的接口，需要传入请求对象
	response, err := client.SendTtsVoice(request)
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
