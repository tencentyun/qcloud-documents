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

## 快速入门

若您对接口存在疑问，可以查阅 [API 文档](https://cloud.tencent.com/document/product/382/13297)。


- **准备必要参数**

```python
appid = 122333333;
appkey = "111111111112132312xx";
phone_numbers = ["21212313123", "12345678902", "12345678903"];
template_id = 7839;
```

- **单发短信**

```python
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

ssender = SmsSingleSender(appid, appkey)
try:
    result = ssender.send(0, 86, phone_numbers[0],
        "测试短信，普通单发，深圳，小明，上学。")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

> `Note`: 发送短信没有指定模板ID时，发送的内容需要与已审核通过的模板内容相匹配，才可能下发成功，否则返回失败。
> `Note`: 如需发送国际短信，同样可以使用此接口，只需将国家码"86"改写成对应国家码号。

- **指定模板ID单发短信**

```python
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

ssender = SmsSingleSender(appid, appkey)
params = ["指定模板单发", "深圳", "小明"]
try:
    result = ssender.send_with_param(86, phone_numbers[0],
        template_id, params)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

> `Note:`无论单发短信还是指定模板ID单发短信都需要从控制台中申请模板并且模板已经审核通过，才可能下发成功，否则返回失败。

- **群发短信**

```python
from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError

msender = SmsMultiSender(appid, appkey)
try:
    result = msender.send(0, "86", phone_numbers,
        "测试短信，普通群发，深圳，小明，上学。")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

- **指定模板ID群发**

```python
from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError

msender = SmsMultiSender(appid, appkey)
params = ["指定模板群发", "深圳", "小明"]
try:
    result = msender.send_with_param(86, phone_numbers[0],
        template_id, params)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

> `Note:`群发一次请求最多支持200个号码，如有对号码数量有特殊需求请联系腾讯云短信技术支持(QQ:3012203387)。

- **发送语音验证码**

```python
from qcloudsms_py import SmsVoiceVerifyCodeSender
from qcloudsms_py.httpclient import HTTPError

vvcsender = SmsVoiceVerifyCodeSender(appid, appkey)
try:
    result = vvcsender.send("86", phone_numbers[0], "1234", 2)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

> `Note`: 语音验证码发送只需提供验证码数字，例如msg内容为“123”时，您收到的语音通知为“您的语音验证码是123，如需自定义内容，可以使用语音通知。

- **发送语音通知**

```python
from qcloudsms_py import SmsVoicePromptSender
from qcloudsms_py.httpclient import HTTPError


vpsender = SmsVoicePromptSender(appid, appkey)
try:
    result = vpsender.send("86", phone_numbers[0], 2, "1234", 2)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
```

- **拉取短信回执以及回复**

```python
from qcloudsms_py import SmsStatusPuller
from qcloudsms_py.httpclient import HTTPError

spuller = SmsStatusPuller(appid, appkey)
try:
    # 拉取短信回执
    callback_result = spuller.pull_callback(10);
    # 拉取回复
    reply_result = spuller.pull_reply(10);
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(callback_result)
print(reply_result)
```

> `Note:` 短信拉取功能需要联系腾讯云短信技术支持(QQ:3012203387)，量大客户可以使用此功能批量拉取，其他客户不建议使用。

- **拉取单个手机短信状态**

```python
from qcloudsms_py import SmsMobileStatusPuller
from qcloudsms_py.httpclient import HTTPError

mspuller = SmsMobileStatusPuller(appid, appkey)
try:
    # 拉取短信回执
    callback_result = mspuller.pull_callback("86", phone_numbers[0],
        1511125600, 1511841600, 10)
    # 拉取回复
    reply_result = mspuller.pull_reply("86", phone_numbers[0],
        1511125600, 1511841600, 10)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(callback_result)
print(reply_result)
```

- **发送海外短信**

海外短信与国内短信发送类似
