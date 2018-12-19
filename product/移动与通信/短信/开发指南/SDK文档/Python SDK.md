## 腾讯短信服务
目前腾讯云短信为客户提供 **国内短信、国内语音** 和 **国际短信** 三大服务，腾讯云短信 SDK 支持以下操作：

### 国内短信
国内短信支持操作： [指定模板单发短信](#指定模板单发短信)、[指定模板群发短信](#指定模板群发短信)、[拉取短信回执和短信回复状态](#拉取短信回执)。

> 短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)开通权限，量大客户可以使用此功能批量拉取，其他客户不建议使用。

### 国际短信
国际短信支持操作： [指定模板单发短信](#指定模板单发短信)、[指定模板群发短信](#指定模板群发短信)、[拉取短信回执和短信回复状态](#拉取短信回执)。

> 国际短信和国内短信使用同一接口，只需替换相应的国家码与手机号码，每次请求群发接口手机号码需全部为国内或者国际手机号码。

### 语音通知
语音通知支持操作：[发送语音验证码](#发送语音验证码)、[发送语音通知](#发送语音通知)、[上传语音文件](#上传语音文件)、[按语音文件 fid 发送语音通知](#按语音文件fid发送语音通知)、[指定模板发送语音通知](#指定模板发送语音通知)。


## 开发准备
### SDK 获取
短信 Python SDK 在 Github 中的下载地址：[短信 Python SDK](https://github.com/qcloudsms/qcloudsms_py)。

### 开发准备
**1. 申请 SDK AppID 以及 App Key：**
在开始本教程之前，您需要先获取 SDK AppID 和 App Key，如您尚未申请，请到 [短信控制台](https://console.cloud.tencent.com/sms) 中添加应用。应用添加成功后您将获得 SDK AppID 以及 App Key。
>**注意：**
> SDK AppID 是以 14xxxxx 开头。

**2. 申请签名：**
下发短信必须携带签名，您可以在短信 [控制台](https://console.cloud.tencent.com/sms) 中申请短信签名，详细申请操作参考 [创建签名](https://cloud.tencent.com/document/product/382/13481#.E5.88.9B.E5.BB.BA.E7.AD.BE.E5.90.8D)。

**3. 申请模板：**
下发短信内容必须经过审核，您可以在短信 [控制台](https://console.cloud.tencent.com/sms) 中申请短信模板，详细申请操作参考 [创建正文模板](https://cloud.tencent.com/document/product/382/13481#.E5.88.9B.E5.BB.BA.E6.AD.A3.E6.96.87.E6.A8.A1.E7.89.88)。

完成以上三项便可开始代码开发。

### SDK 配置

- **pip 配置：**
qcloudsms_py 采用 pip 进行安装，要使用 qcloudsms 功能, 只需要执行：
```shell
pip install qcloudsms_py
```

- **手动配置：**

 1.手动下载或 clone 最新版本 qcloudsms_py 代码。
 2.在 qcloudsms_py 目录运行 `python setup.py install`或直接把 qcloudsms_py 所在目录加入`sys.path`。
 >python2/python3都支持。

 ### 相关资料
 若您对接口存在疑问，可以查阅 [开发指南](https://cloud.tencent.com/document/product/382/13297) 、[API文档](https://qcloudsms.github.io/qcloudsms_java/) 和 [错误码](https://cloud.tencent.com/document/product/382/3771)。


### 示例
- **准备必要参数**

```python
# 短信应用SDK AppID
appid = 1400009099  # SDK AppID是1400开头

# 短信应用SDK AppKey
appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad"

# 需要发送短信的手机号码
phone_numbers = ["21212313123", "12345678902", "12345678903"]

# 短信模板ID，需要在短信应用中申请
template_id = 7839  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
# templateId 7839 对应的内容是"您的验证码是: {1}"
# 签名
sms_sign = "腾讯云"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`
```

<a id="指定模板单发短信" ></a>

- **指定模板ID单发短信**

```python
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

ssender = SmsSingleSender(appid, appkey)
params = ["5678"]  # 当模板没有参数时，`params = []`，数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:5678对应一个变量，参数数组中元素个数也必须是一个
try:
    result = ssender.send_with_param(86, phone_numbers[0],
        template_id, params, sign=sms_sign, extend="", ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

> 无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。


<a id="指定模板群发短信" ></a>

- **指定模板ID群发短信**

```python
from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError

msender = SmsMultiSender(appid, appkey)
params = ["5678"] # 数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:5678对应一个变量，参数数组中元素个数也必须是一个
try:
    result = msender.send_with_param(86, phone_numbers,
        template_id, params, sign=sms_sign, extend="", ext="")   # 签名参数未提供或者为空时，会使用默认签名发送短信
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

> 群发一次请求最多支持 200 个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持(QQ:3012203387)。
>无论单发/群发短信还是指定模板ID单发/群发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

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

> 语音验证码发送只需提供验证码数字，例如当 msg=“5678” 时，您收到的语音通知为“您的语音验证码是5678”，如需自定义内容，可以使用语音通知。


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
    # 拉取回复
    reply_result = spuller.pull_reply(max_num)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(callback_result)
print(reply_result)
```

> 短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)，量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **拉取单个手机短信状态**

```python
from qcloudsms_py import SmsMobileStatusPuller
from qcloudsms_py.httpclient import HTTPError

begin_time = 1511125600  # 开始时间(UNIX timestamp)
end_time = 1511841600    # 结束时间(UNIX timestamp)
max_num = 10             # 单次拉取最大量
mspuller = SmsMobileStatusPuller(appid, appkey)
try:
    # 拉取短信回执
    callback_result = mspuller.pull_callback("86", phone_numbers[0],
        begin_time, end_time, max_num)
    # 拉取回复
    reply_result = mspuller.pull_reply("86", phone_numbers[0],
        begin_time, end_time, max_num)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(callback_result)
print(reply_result)
```
>短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)，量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **发送国际短信**
国际短信与国内短信发送类似, 发送国际短信只需替换相应国家码。

<a id="上传语音文件" ></a>

- **上传语音文件**

```python
from qcloudsms_py import VoiceFileUploader
from qcloudsms_py.httpclient import HTTPError

# Note: 语音文件大小上传限制400K字节
with open("/path/to/example.mp3", "rb") as f:
    content = f.read()
uploader = VoiceFileUploader(appid, appkey)
try:
    result = uploader.upload(content, content_type="mp3")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

# 上传成功后，result里会带有语音文件的fid
print(result)
```
>语音文件上传功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。


<a id="按语音文件fid发送语音通知" ></a>

- **按语音文件 fid 发送语音通知**

```python
from qcloudsms_py import FileVoiceSender
from qcloudsms_py.httpclient import HTTPError

# Note：这里fid来自`上传语音文件`接口返回的响应，要按语音
#   文件fid发送语音通知，需要先上传语音文件获取fid
fid = "c799d10a43ec109f02f2288ca3c85b79e7700c98.mp3"
fvsender = FileVoiceSender(appid, appkey)
try:
    result = fvsender.send(fid, phone_numbers[0],
        nationcode="86", playtimes=2, ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)

```
>按语音文件 fid 发送语音通知功能需要联系腾讯云短信技术支持(QQ:3012203387)才能开通。

<a id="指定模板发送语音通知" ></a>

- **指定模版发送语音通知**

```python
from qcloudsms_py import TtsVoiceSender
from qcloudsms_py.httpclient import HTTPError

template_id = 12345
params = ["5678"]# 数组具体的元素个数和模板中变量个数必须一致，例如事例中templateId:5678对应一个变量，参数数组中元素个数也必须是一个
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

# 创建QcloudSms对象
qcloudsms = QcloudSms(appid, appkey)

# 创建单发短信(SmsSingleSender)对象
ssender = qcloudsms.SmsSingleSender()

# 创建上传语音文件(VoiceFileUploader)对象
uploader = qcloudsms.VoiceFileUploader()
```
