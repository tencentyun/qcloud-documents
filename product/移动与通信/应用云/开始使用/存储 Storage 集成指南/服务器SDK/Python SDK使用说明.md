### 获取 SDK

[Python SDK]()

### 配置您的信息

解压下载的压缩包，打开 `sts.py` 文件，在头部找到 `Config` 类，请在对应的部分填入你的信息：

```
class Config:

    COMMON_POLICY = r'''{"statement": [{"action": ["name/cos:*"],"effect": "allow","resource":"*"}],"version": "2.0"}'''
    # 昵称，任意即可
    NAME = "你的昵称"
    # 策略，一般情况下使用默认策略即可
    POLICY = COMMON_POLICY
    # 临时密钥有效期，单位是秒，此处为30分钟
    DURATION_SECOND = 1800
    # secret id
    SECRET_ID = '你的secret id'
    # secret key
    SECRET_KEY = '你的secret key'
```

### 获取临时密钥

您可以将 `sts.py` 文件集成到您的 Python 工程中，然后调用以下代码：

```
import sts

response = sts.sign()
content = response.content
```

成功的话，可以拿到包含密钥的 JSON 文本：

```
{"code":0,"message":"","codeDesc":"Success","data":{"credentials":{"sessionToken":"2a0c0ead3e6b8eed9608899eb74f2458812208ab30001","tmpSecretId":"AKIDBSrMaeFD0ZAECKuBzohnjAhJ53XNCE2F","tmpSecretKey":"UC7YjMrIlcuFgoWGwnrHwsMBrQrpUwYI"},"expiredTime":1526288317}}
```


