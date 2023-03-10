
企业经营活动中，资质证书是证明企业生产能力的必要证件，也是企业入驻各类平台、组织项目申报等必须提交的，这里面包括营业执照、税务登记证、生产许可证、高新技术企业认定证书等等。在日常工作中，以平台类企业入驻为例，要求企业上传对应的资质证书然后进行审核，但由于企业资质证书种类繁多，各行各业的资质证书都有差异，没有统一的板式，通过人工审核工作量巨大且很容易出错。




那么，有没有更智能化的方式让资质审核流程更加快捷和高效呢？搜索了国内外的文字识别产品，**发现腾讯云 AI 文字识别新推出了智能结构化识别能力，能够识别并提取各类证照、票据、表单、合同等结构化场景的字段信息。**深入了解后，发现这个接口能力刚好和我们要解决的企业资质自动化审核问题完美契合。



接下来，将详细讲述我是如何使用智能结构化识别能力，完成资质证书标题、企业名称、许可证编号、注册地址、企业负责人等信息的自动获取。


## 准备工作
为了使用腾讯云智能结构化识别能力，首先需要进行一些准备工作。
1. 腾讯云AI文字识别提供了功能体验服务（[功能体验页面](https://cloud.tencent.com/act/event/ocrdemo)），我们首先对智能结构化能力进行了体验，可以看到识别的效果很不错，让我们更有信心使用这个接口能力了。
![](https://qcloudimg.tencent-cloud.cn/raw/6126c22f283d6bf348778c504c370b20.jpg)
2. 在使用腾讯云 AI 文字识别之前需要开通文字识别服务。打开腾讯云 [OCR 控制台](https://console.cloud.tencent.com/ocr/v2/overview) 页面，我们成功开通了文字识别服务。
![](https://qcloudimg.tencent-cloud.cn/raw/54d0164f1b5210cf9ed594eb1a087ad7.png)
3.服务开通成功后，腾讯云 AI 文字识别赠送了免费的资源包，其中智能结构化有1000次的免费额度，可以在 [资源包管理页面](https://console.cloud.tencent.com/ocr/packagemanage) 查看资源包使用情况。
![](https://qcloudimg.tencent-cloud.cn/raw/c1d9ef505513aa8a9bc67eaeb183c821.png)
当免费资源包用尽后，我们先根据使用情况购买了部分预付费资源包，后来又开通了后付费，保证业务可以持续正常调用接口。
	- 我们首先评估了业务的请求量级，于是在文字识别 [购买页](https://buy.cloud.tencent.com/iai_ocr) 购买了智能结构化识别100万次的资源包，资源包购买的越多优惠越大。可以在 [资源包管理页面](https://console.cloud.tencent.com/ocr/packagemanage) 中查看资源包的具体使用情况。
![](https://qcloudimg.tencent-cloud.cn/raw/1f8662823381b2c77332b165b46eb65f.png)
	- 然后在 [用量统计页面](https://console.cloud.tencent.com/ocr/stats) 可以看到接口的调用量。
![](https://qcloudimg.tencent-cloud.cn/raw/f499bbebab37466466e80976041faa32.png)
	- 最后我们在 [设置页面](https://console.cloud.tencent.com/ocr/settings) 开通了后付费服务，这样就不用担心资源包耗尽导致调用接口失败了。需要注意后付费设置每月只能变更一次。
![](https://qcloudimg.tencent-cloud.cn/raw/6a5c4147b92b190fd6d1d1285218228b.png)



## 开发流程
通过下面几个步骤就可以正式使用智能结构化能力了。
- 获取个人密钥
- 智能结构化 API 文档
- 体验在线调用
- 使用集成腾讯云 OCR 的 SDK
- 查询调用量

### 获取个人密钥
首先，我们需要获取个人 API 密钥，用于接口的调用。打开腾讯云访问管理的 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，可以创建个人密钥。
![](https://qcloudimg.tencent-cloud.cn/raw/a401f2812627264212c4e165d567e98f.png)


### 智能结构化识别 API 文档
查看接口具体的使用说明，在文字识别的 [API 文档](https://cloud.tencent.com/document/product/866/60877?from=10680) 中可以查看智能结构化识别的输入参数、输出参数、错误码、示例等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/a89c9e6be345094c17a972cf0d895e9c.png)

### 在线调试
腾讯云 AI 文字识别提供了在线调用 [API Explorer 工具](http://test.api.explorer.woa.com/apiexplorer/?Product=ocr&Version=2018-11-19&Action=RecognizeTravelCardOCR&SignVersion=)，方便我们可视化调用，并生成调用代码，可以直观的看到请求参数和返回参数。
![](https://qcloudimg.tencent-cloud.cn/raw/5f44b55a2a166602d66ee8a67ded7815.png)

### 使用 SDK 调用
接下来可以正式接入接口使用了，在智能结构和文档的最下方，提供了多个语言的开发工具集（SDK），SDK 的使用方法十分简单方便，我们可以根据自己需要的语言选择接入。
![](https://qcloudimg.tencent-cloud.cn/raw/8bef0e716db7cd658a3fb5cba41c2151.png)
我们使用的开发语言是 GoLang。

1. 安装公共基础包
```
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common
```
2. 安装文字识别对应的产品包
```
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ocr
```
3. 实现调用逻辑**（仅为主要逻辑，非完整代码）**
```
package main

import (
	"fmt"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/regions"
	ocr "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ocr/v20181119"
)

func main() {
	credential := common.NewCredential("secretId", "secretKey")
	client, _ := ocr.NewClient(credential, regions.Guangzhou, profile.NewClientProfile())

	request := ocr.NewSmartStructuralOCRRequest()
	request.ImageUrl = common.StringPtr("xxxxx")
	response, err := client.SmartStructuralOCR(request)

	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", response.ToJsonString())
}
```
4. 智能结构化特定参数使用
我们的业务场景针对医疗资质的审核往往比较看重其中特定字段，例如类别、编号，地址、姓名，有效期等，在使用智能结构化接口识别医疗资质证书时，我们需要智能结构化接口返回这些特定字段，方便我们进一步的审核。
![](https://qcloudimg.tencent-cloud.cn/raw/688682851a3a456d9887e5638602ce4c.jpg)
查阅了智能结构化识别接口文档后，我们发现可以自定义结构化功能需返回的字段名称，在请求时候传入对应的参数即可。
![](https://qcloudimg.tencent-cloud.cn/raw/bac025db2306885581cdec1b52bca052.png)

传入自定义参数，让智能结构化接口返回特定字段，包括：类别、编号，地址、姓名，有效期，调用逻辑如下（**仅为主要逻辑，非完整代码**）
```
package main

import (
	"fmt"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/regions"
	ocr "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ocr/v20181119"
)

func main() {
	credential := common.NewCredential("secretId", "secretKey")
	client, _ := ocr.NewClient(credential, regions.Guangzhou, profile.NewClientProfile())

	request := ocr.SmartStructuralOCRRequest{
		ImageUrl: common.StringPtr("xxx") ,
		ItemNames: common.StringPtrs([]string{"类别","编号","地址","姓名","有效期"}),
	}
	response, err := client.SmartStructuralOCR(request)

	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", response.ToJsonString())
}
```
5. 查询调用量
接口调用成功后，我们可以在 [腾讯云文字识别控制台](https://console.cloud.tencent.com/ocr/stats) 查看接口的调用明细，包括调用量、成功量、失败量、错误码等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/055d1875f20195947c20bd4295d08ca0.png)
>! 主账号登录后可以查看所有账号的调用量明细，子账号只能查询自己的调用量明细。
>
如果想要让子账号也有权限查看所有账号的调用明细，可以在 [用量查询权限管理页面](https://console.cloud.tencent.com/ocr/permission) 给子账号赋权，这样子账号也可以查询到所有账号的调用量。
![](https://qcloudimg.tencent-cloud.cn/raw/9198cce1498172616675377eae5f6b32.png)




