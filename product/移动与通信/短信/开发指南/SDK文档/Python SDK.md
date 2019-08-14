## SDK 功能简介
目前腾讯云短信为客户提供**国内短信、语音短信**和**国际/港澳台短信**服务，腾讯云短信 SDK 支持以下操作：

| 国内短信             | 语音短信               | 国际/港澳台短信                 |
| ------------------ | ---------------------- | ---------------- |
| <li>[单发短信](#单发短信)<li>[指定模板单发短信](#指定模板单发短信)<li>[群发短信](#群发短信)<li>[指定模板群发短信](#指定模板群发短信)<li>[拉取短信回执和短信回复状态](#拉取短信回执) | <li>[发送语音验证码](#发送语音验证码)<li>[发送语音通知](#发送语音通知)<li>[指定模板发送语音通知](#指定模板发送语音通知) | <li>[单发短信](#单发短信)<li>[指定模板单发短信](#指定模板单发短信)<li>[群发短信](#群发短信)<li>[指定模板群发短信](#指定模板群发短信)<li>[拉取短信回执](#拉取短信回执) |

>?
>- 群发短信
>一次群发请求最多支持200个号码，如对号码数量有特殊需求请联系腾讯云短信技术支持（QQ：[3012203387](https://main.qcloudimg.com/raw/e674a37df984126f53ab9cbf4b9a168a.html)）。
>- 拉取短信回执
>该功能默认关闭。您可以根据实际需求联系腾讯云短信技术支持（QQ：[3012203387](https://main.qcloudimg.com/raw/e674a37df984126f53ab9cbf4b9a168a.html)）开通，实现批量拉取短信回执。
>- 发送语音验证码
>只需提供验证码数字，如需自定义内容，可以 [发送语音通知](#发送语音通知)。例如，当 msg=“5678” 时，您收到的语音通知为`您的语音验证码是五六七八。`。
>- 发送语音通知
>数字默认按照个十百千万进行播报，可通过在数字前添加英文逗号（,）改变播报方式。例如，当 msg=`您的语音验证码是5678。` 时，您收到的语音通知为`您的语音验证码是五千六百七十八。`，当 msg=`您的语音验证码是5,6,7,8。`时，您收到的语音通知为`您的语音验证码是五六七八。`。

## SDK 使用指南
### 相关资料
各个接口及其参数的详情介绍请参见 [API 指南](https://cloud.tencent.com/document/product/382/13297) 、[SDK 文档](https://github.com/qcloudsms/qcloudsms_py) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。

### 前提条件
在使用 SDK 前，您需要准备以下信息：
- **获取 SDKAppID 和 AppKey**
云短信应用 **SDKAppID** 和 **AppKey** 可在 [短信控制台](https://console.cloud.tencent.com/sms) 的应用信息里获取。如您尚未添加应用，请登录 [短信控制台](https://console.cloud.tencent.com/sms) 添加应用。
- **申请签名并确认审核通过**
一个完整的短信由短信**签名**和**短信正文内容**两部分组成，短信**签名**需申请和审核，**签名**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建签名](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。发送国际/港澳台短信时，允许不携带签名。
- **申请模板并确认审核通过**
短信或语音正文内容**模板**需申请和审核，**模板**可在 [短信控制台](https://console.cloud.tencent.com/sms) 的相应服务模块【内容配置】中进行申请，详细申请操作请参见 [创建正文模板](https://cloud.tencent.com/document/product/382/18061#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E6.9D.BF)。


### 配置 SDK

- **pip 配置：**
qcloudsms_py 采用 pip 进行安装，要使用 qcloudsms 功能, 只需要执行：
```shell
pip install qcloudsms_py
```
- **手动配置：**
 1.手动下载或 clone 最新版本 qcloudsms_py 代码。
 2.在 qcloudsms_py 目录运行 `python setup.py install`或直接把 qcloudsms_py 所在目录加入`sys.path`。
 >?Python 2/Python 3都支持。

### 示例代码
>?所有示例代码仅作参考，无法直接编译和运行，需根据实际情况进行修改。

- **准备必要参数**
```python
# 短信应用 SDK AppID
appid = 1400009099  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad"
# 需要发送短信的手机号码
phone_numbers = ["21212313123", "12345678902", "12345678903"]
# 短信模板ID，需要在短信控制台中申请
template_id = 7839  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "腾讯云"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请
```

<a id="单发短信" ></a>
- **单发短信**
```python
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
ssender = SmsSingleSender(appid, appkey)
try:
    result = ssender.send(sms_type, 86, phone_numbers[0],
        "【腾讯云】您的验证码是: 5678", extend="", ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```

<a id="指定模板单发短信" ></a>
- **指定模板 ID 单发短信**
```python
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
ssender = SmsSingleSender(appid, appkey)
params = ["5678"]  # 当模板没有参数时，`params = []`
try:
    result = ssender.send_with_param(86, phone_numbers[0],
        template_id, params, sign=sms_sign, extend="", ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```

<a id="群发短信" ></a>
- **群发短信**
```python
from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError
sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
msender = SmsMultiSender(appid, appkey)
try:
    result = msender.send(sms_type, "86", phone_numbers,
        "【腾讯云】您的验证码是: 5678", extend="", ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```

<a id="指定模板群发短信" ></a>
- **指定模板 ID 群发短信**
```python
from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError
msender = SmsMultiSender(appid, appkey)
params = ["5678"]
try:
    result = msender.send_with_param(86, phone_numbers,
        template_id, params, sign=sms_sign, extend="", ext="")   # 签名参数未提供或者为空时，会使用默认签名发送短信
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```


<a id="拉取短信回执" ></a>
- **拉取短信回执以及回复**
```python
from qcloudsms_py import SmsStatusPuller
from qcloudsms_py.httpclient import HTTPError
max_num = 10  # 单次拉取最大量
spuller = SmsStatusPuller(appid, appkey)
try:
    # 拉取短信回执
    callback_result = spuller.pull_callback(max_num)
    # 拉取回复，国际/港澳台短信不支持回复功能
    reply_result = spuller.pull_reply(max_num)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(callback_result)
print(reply_result)
```


- **拉取单个手机短信状态**
```python
from qcloudsms_py import SmsMobileStatusPuller
from qcloudsms_py.httpclient import HTTPError
begin_time = 1511125600  # 开始时间（UNIX timestamp）
end_time = 1511841600    # 结束时间（UNIX timestamp）
max_num = 10             # 单次拉取最大量
mspuller = SmsMobileStatusPuller(appid, appkey)
try:
    # 拉取短信回执
    callback_result = mspuller.pull_callback("86", phone_numbers[0],
        begin_time, end_time, max_num)
    # 拉取回复，国际/港澳台短信不支持回复功能
    reply_result = mspuller.pull_reply("86", phone_numbers[0],
        begin_time, end_time, max_num)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(callback_result)
print(reply_result)
```

<a id="发送语音验证码" ></a>
- **发送语音验证码**
```python
from qcloudsms_py import SmsVoiceVerifyCodeSender
from qcloudsms_py.httpclient import HTTPError
vvcsender = SmsVoiceVerifyCodeSender(appid, appkey)
try:
    result = vvcsender.send("86", phone_numbers[0], "5678",
        playtimes=2, ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```

<a id="发送语音通知" ></a>
- **发送语音通知**
```python
from qcloudsms_py import SmsVoicePromptSender
from qcloudsms_py.httpclient import HTTPError
vpsender = SmsVoicePromptSender(appid, appkey)
try:
    result = vpsender.send("86", phone_numbers[0], 2, "5678",
        playtimes=2, ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```
<a id="指定模板发送语音通知" ></a>
- **指定模版发送语音通知**
```python
from qcloudsms_py import TtsVoiceSender
from qcloudsms_py.httpclient import HTTPError
template_id = 12345
params = ["5678"]
tvsender = TtsVoiceSender(appid, appkey)
Try:
    result = tvsender.send(template_id, params, phone_numbers[0],
        nationcode="86", playtimes=2, ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```

- **发送国际/港澳台短信**
发送国际/港澳台短信与发送国内短信类似，只需替换相应的国家码或地区码。详细示例请参考：
 - [单发短信](#单发短信)
 - [指定模板单发短信](#指定模板单发短信)
 - [群发短信](#群发短信)
 - [指定模板群发短信](#指定模板群发短信)
 - [拉取短信回执](#拉取短信回执)

- **使用代理**
有的环境需要使用代理才能上网，可以指定 HTTPSimpleClient 的 proxy 参数来实现, 示例如下:
```python
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPSimpleClient, HTTPError
httpclient = HTTPSimpleClient(proxy="www.proxysever.com:8080")
ssender = SmsSingleSender(appid, appkey, httpclient=httpclient)
template_id = 7839
params = ["5678"]
try:
    result = ssender.send_with_param(86, phone_numbers[0],
        template_id, params, sign=sms_sign, extend="", ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
print(result)
```

- **统一创建对象**
短信和语音各类的对象可以通过 qcloudsms_py.QcloudSms 统一创建，这种方式可以避免创建对象时多次传入参数 appid 和 appkey， 示例如下：
```python
from qcloudsms_py import QcloudSms
# 创建 QcloudSms 对象
qcloudsms = QcloudSms(appid, appkey)
# 创建单发短信 SmsSingleSender 对象
ssender = qcloudsms.SmsSingleSender()
# 创建上传语音文件 VoiceFileUploader 对象
uploader = qcloudsms.VoiceFileUploader()
```
