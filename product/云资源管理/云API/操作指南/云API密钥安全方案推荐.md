代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。建议不要在代码中使用持久 SecretId 和 SecretKey，推荐以下几种方案来提高密钥安全性：

## 方案1：通过环境变量读取 SecretId 和 SecretKey
将 SecretId 和 SecretKey 预先配置到环境变量中，在代码运行时从环境变量中读取 SecretId 和 SecretKey 的值，代码示例如下：
```python
import os
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

try:
    # 硬编码密钥到代码中有可能随代码泄露而暴露，有安全隐患，不推荐
    # 为保护密钥安全，建议将密钥设置在环境变量中
    # cred = credential.Credential("secretId", "secretKey")
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    req = models.DescribeInstancesRequest()
    resp = client.DescribeInstances(req)

    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
```

## 方案2：使用临时密钥
不在代码中使用持久 SecretId 和 SecretKey，而是使用通过 [GetFederationToken](https://cloud.tencent.com/document/product/1312/48195) 接口换取的用户临时密钥，同时根据权限最小化原则赋予相关权限。代码示例如下：
```python
# 换取临时秘钥的 SDK 示例
import json
import os
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sts.v20180813 import sts_client, models

try:
# 实例化一个认证对象，入参需要传入腾讯云账户的secretId和secretKey，为了保护密钥安全，建议结合方案一，将密钥设置在环境变量中
    cred = credential.Credential(
    os.environ.get("TENCENTCLOUD_SECRET_ID"),
    os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "sts.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = sts_client.StsClient(cred, "", clientProfile)
    req = models.GetFederationTokenRequest()
    params = {
    }
    req.from_json_string(json.dumps(params))
    resp = client.GetFederationToken(req)
    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)
``` 
 
## 方案3：使用 KMS 白盒密钥保护 SecretKey
操作指导请参见 [密钥管理系统-使用 KMS 白盒密钥保护 SecretKey 最佳实践](https://cloud.tencent.com/document/product/573/54236)。

