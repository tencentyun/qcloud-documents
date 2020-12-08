SDK 3.0是云 API 3.0平台的配套工具，您可以通过 SDK 使用所有 [短信 API](https://cloud.tencent.com/document/product/382/38764)。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
>!
>- 发送短信相关接口
>一次群发请求最多支持200个号码，如对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：[3012203387](https://main.qcloudimg.com/raw/e674a37df984126f53ab9cbf4b9a168a.html)）。
>- 签名、正文模板相关接口
>个人认证用户不支持使用签名、正文模板相关接口，只能通过短信控制台 [管理短信签名](https://cloud.tencent.com/document/product/382/37794) 和 [管理短信正文模板](https://cloud.tencent.com/document/product/382/37795)。如需使用该类接口，请将 “个人认证” 变更为 “企业认证”，具体操作请参见 [实名认证变更指引](https://cloud.tencent.com/document/product/378/34075)。



## 前提条件

- 已开通短信服务，具体操作请参见 [国内短信快速入门](https://cloud.tencent.com/document/product/382/37745)。
- 如需发送国内短信，需要先 [购买国内短信套餐包](https://cloud.tencent.com/document/product/382/18060)。
- 已准备依赖环境：Python 2.7 - 3.6 版本。
- 已在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 短信的调用地址为`sms.tencentcloudapi.com`。

## 相关资料
- 各个接口及其参数的详细介绍请参见 [API 文档](https://cloud.tencent.com/document/product/382/38764)。
- 下载 SDK 源码请访问 [Python SDK 源码](https://github.com/TencentCloud/tencentcloud-sdk-python)。

## 安装 SDK

### 通过 pip 安装（推荐）
1. 下载并安装 [pip](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o)。
2. 执行以下命令安装 SDK。
```bash
pip install tencentcloud-sdk-python
```

### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-python) 或 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-python/tencentcloud-sdk-python.zip) 下载最新代码。
2. 解压后依次执行以下命令安装 SDK。
```
    $ cd tencentcloud-sdk-python
    $ python setup.py install
```

<span id="example"></span>
## 示例代码
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改，您也可以根据实际需求使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2019-07-11&Action=SendSms) 自动化生成 Demo 代码。

每个接口都有一个对应的 Request 结构和一个 Response 结构。本文仅列举几个常用功能的示例代码，更多示例请参见 [Python SDK 示例](https://github.com/TencentCloud/tencentcloud-sdk-python/tree/master/examples/sms)。

### 申请短信模板

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 SMS 模块的 client models
from tencentcloud.sms.v20190711 import sms_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 必要步骤：
    # 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
    # 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
    # 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
    # CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
		
    cred = credential.Credential("secretId", "secretKey")
    # cred = credential.Credential(
    #     os.environ.get(""),
    #     os.environ.get("")
    # )

    # 实例化一个 http 选项，可选，无特殊需求时可以跳过
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # POST 请求（默认为 POST 请求）
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒（默认60秒）
    httpProfile.endpoint = "sms.tencentcloudapi.com"  # 指定接入地域域名（默认就近接入）

    # 非必要步骤:
    # 实例化一个客户端配置对象，可以指定超时时间等配置
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    # 实例化 SMS 的 client 对象
    # 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量
    client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    # 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
    # 属性可能是基本类型，也可能引用了另一个数据结构
    # 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明
    req = models.AddSmsTemplateRequest()

    # 基本类型的设置:
    # SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值
    # SDK 提供对基本类型的指针引用封装函数
    # 帮助链接：
    # 短信控制台：https://console.cloud.tencent.com/smsv2
    # sms helper：https://cloud.tencent.com/document/product/382/3773

    # 模板名称 
	req.TemplateName = "腾讯云"
	# 模板内容 
	req.TemplateContent = "{1}为您的登录验证码，请于{2}分钟内填写，如非本人操作，请忽略本短信。"
	# 短信类型：0表示普通短信, 1表示营销短信 
	req.SmsType = 0;
	# 是否国际/港澳台短信：
	# 0：表示国内短信
	# 1：表示国际/港澳台短信 
	req.International = 0
	# 模板备注：例如申请原因，使用场景等 
	req.Remark = "xxx"

    # 通过 client 对象调用 AddSmsTemplate 方法发起请求。注意请求方法名与请求对象是对应的
    resp = client.AddSmsTemplate(req)

    # 输出 JSON 格式的字符串回包
    print(resp.to_json_string(indent=2))

except TencentCloudSDKException as err:
    print(err)
```


### 发送短信

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 SMS 模块的client models
from tencentcloud.sms.v20190711 import sms_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 必要步骤：
    # 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
    # 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
    # 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
    # CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
		
    cred = credential.Credential("secretId", "secretKey")
    # cred = credential.Credential(
    #     os.environ.get(""),
    #     os.environ.get("")
    # )

    # 实例化一个 http 选项，可选，无特殊需求时可以跳过
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # POST 请求（默认为 POST 请求）
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒（默认60秒）
    httpProfile.endpoint = "sms.tencentcloudapi.com"  # 指定接入地域域名（默认就近接入）

    # 非必要步骤:
    # 实例化一个客户端配置对象，可以指定超时时间等配置
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    # 实例化 SMS 的 client 对象
    # 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量
    client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    # 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
    # 属性可能是基本类型，也可能引用了另一个数据结构
    # 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明
    req = models.SendSmsRequest()

    # 基本类型的设置:
    # SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值
    # SDK 提供对基本类型的指针引用封装函数
    # 帮助链接：
    # 短信控制台：https://console.cloud.tencent.com/smsv2
    # sms helper：https://cloud.tencent.com/document/product/382/3773

    # 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666
    req.SmsSdkAppid = "1400787878"
    # 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，可登录 [短信控制台] 查看签名信息
    req.Sign = "xxx"
    # 短信码号扩展号: 默认未开通，如需开通请联系 [sms helper]
    req.ExtendCode = ""
    # 用户的 session 内容: 可以携带用户侧 ID 等上下文信息，server 会原样返回
    req.SessionContext = "xxx"
    # 国际/港澳台短信 senderid: 国内短信填空，默认未开通，如需开通请联系 [sms helper]
    req.SenderId = ""
    # 下发手机号码，采用 e.164 标准，+[国家或地区码][手机号]
    # 例如+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号
    req.PhoneNumberSet = ["+8613711112222", "+8613711333222", "+8613711144422"]
    # 模板 ID: 必须填写已审核通过的模板 ID，可登录 [短信控制台] 查看模板 ID
    req.TemplateID = "449739"
    # 模板参数: 若无模板参数，则设置为空
    req.TemplateParamSet = ["666"]


    # 通过 client 对象调用 SendSms 方法发起请求。注意请求方法名与请求对象是对应的
    resp = client.SendSms(req)

    # 输出 JSON 格式的字符串回包
    print(resp.to_json_string(indent=2))

except TencentCloudSDKException as err:
    print(err)
```



### 拉取回执状态

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 SMS 模块的 client models
from tencentcloud.sms.v20190711 import sms_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 必要步骤：
    # 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
    # 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
    # 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
    # CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
		
    cred = credential.Credential("secretId", "secretKey")
    # cred = credential.Credential(
    #     os.environ.get(""),
    #     os.environ.get("")
    # )

    # 实例化一个 http 选项，可选，无特殊需求时可以跳过
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # POST 请求（默认为 POST 请求）
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒（默认60秒）
    httpProfile.endpoint = "sms.tencentcloudapi.com"  # 指定接入地域域名（默认就近接入）

    # 非必要步骤:
    # 实例化一个客户端配置对象，可以指定超时时间等配置
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    # 实例化 SMS 的 client 对象
    # 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量
    client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    # 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
    # 属性可能是基本类型，也可能引用了另一个数据结构
    # 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明
    req = models.PullSmsSendStatusRequest()

    # 基本类型的设置:
    # SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值
    # SDK 提供对基本类型的指针引用封装函数
    # 帮助链接：
    # 短信控制台：https://console.cloud.tencent.com/smsv2
    # sms helper：https://cloud.tencent.com/document/product/382/3773

    # 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666
    req.SmsSdkAppid = "1400787878"
    # 拉取最大条数，最多100条
    req.Limit = 10

    # 通过 client 对象调用 PullSmsSendStatus 方法发起请求。注意请求方法名与请求对象是对应的
    resp = client.PullSmsSendStatus(req)

    # 输出 JSON 格式的字符串回包
    print(resp.to_json_string(indent=2))


except TencentCloudSDKException as err:
    print(err)
```


### 统计短信发送数据

```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 SMS 模块的client models
from tencentcloud.sms.v20190711 import sms_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    # 必要步骤：
    # 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
    # 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
    # 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
    # CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
		
    cred = credential.Credential("secretId", "secretKey")
    # cred = credential.Credential(
    #     os.environ.get(""),
    #     os.environ.get("")
    # )

    # 实例化一个 http 选项，可选，无特殊需求时可以跳过
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # POST 请求（默认为 POST 请求）
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒（默认60秒）
    httpProfile.endpoint = "sms.tencentcloudapi.com"  # 指定接入地域域名（默认就近接入）

    # 非必要步骤:
    # 实例化一个客户端配置对象，可以指定超时时间等配置
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    # 实例化 SMS 的 client 对象
    # 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量
    client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    # 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
    # 属性可能是基本类型，也可能引用了另一个数据结构
    # 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明
    req = models.SendStatusStatisticsRequest()

    # 基本类型的设置:
    # SDK 采用的是指针风格指定参数，即使对于基本类型也需要用指针来对参数赋值
    # SDK 提供对基本类型的指针引用封装函数
    # 帮助链接：
    # 短信控制台：https://console.cloud.tencent.com/smsv2
    # sms helper：https://cloud.tencent.com/document/product/382/3773

    # 短信应用 ID: 在 [短信控制台] 添加应用后生成的实际 SDKAppID，例如1400006666
    req.SmsSdkAppid = "1400787878"
    # 拉取最大条数，最多100条
    req.Limit = 10
    # 偏移量 注：目前固定设置为0
    req.Offset = 0
    # 开始时间，yyyymmddhh 需要拉取的起始时间，精确到小时
    req.StartDateTime = 2019122400
    # 结束时间，yyyymmddhh 需要拉取的截止时间，精确到小时
    # 注：EndDataTime 必须大于 StartDateTime
    req.EndDataTime = 2019122523

    # 通过 client 对象调用 SendStatusStatistics 方法发起请求。注意请求方法名与请求对象是对应的
    resp = client.SendStatusStatistics(req)

    # 输出 JSON 格式的字符串回包
    print(resp.to_json_string(indent=2))

except TencentCloudSDKException as err:
    print(err)
```


