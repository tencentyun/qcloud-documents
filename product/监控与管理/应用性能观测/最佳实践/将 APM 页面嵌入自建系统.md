APM 满足不需要登录腾讯云控制台即可查询分析 APM 数据的诉求。通过内嵌应用性能观测控制台页面，可以给用户带来以下方便：
- 在外部系统服务中（例如公司内部运维或运营系统）快速集成 APM 数据的查询分析能力。
- 无需管理众多腾讯云子账号，方便将 APM 数据分享给他人进行查看。
![](https://qcloudimg.tencent-cloud.cn/raw/26c5416d6362ff652dee8d1427a08c12.png)  

## 创建用户身份

企业用户（运维或开发人员）根据业务需求申请对应的权限，用户身份对应腾讯云账号角色，可以通过 [控制台](https://console.cloud.tencent.com/cam/role) 或 [创建角色API](https://cloud.tencent.com/document/product/598/36225) 创建对应的角色：

### 通过控制台创建 CAM 角色

1. 登录 [访问管理 CAM 控制台](https://console.cloud.tencent.com/cam)。
2. 单击左侧菜单栏中的**角色**，进入角色页面。
3. 选择**新建角色 > 腾讯云账户**，开始新建自定义角色。
4. 选择**当前主账号**并勾选**允许当前角色服务控制台**，单击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/79f8f1d2b176f2fd136e62ff33d0cdca.png)
5. 为角色设置访问策略，例如只读策略权限 QcloudAPMReadOnlyFullAccess，单击**下一步**。
  ![](https://qcloudimg.tencent-cloud.cn/raw/ea9dfe93baefe0a8a45ca33b4972e74d.png)  
6. 输入角色名，完成创建。
![](https://qcloudimg.tencent-cloud.cn/raw/0505f9fadb3340eed6ac9e115f9d43e3.png)  

### 通过 API 创建 CAM 角色

1. 获取当前用户的访问密钥，可参见 [主账号访问密钥管理](https://cloud.tencent.com/document/product/598/40488) 。
2. 创建角色，详情请参见[ 创建角色 API](https://cloud.tencent.com/document/product/598/36225) ，其中 ConsoleLogin 需要填入1，允许角色登录控制台。
3. 绑定 QcloudAPMReadOnlyFullAccess 的权限策略到角色，详情参见[ 绑定权限策略到角色](https://cloud.tencent.com/document/product/598/36226) 。


## 获取用户身份访问密钥

根据角色名访问腾讯云 STS 服务，调用 [AssumeRole](https://cloud.tencent.com/document/product/1312/48197) 接口，申请角色 CompanyOpsRole 的临时密钥。

## 生成 APM 访问链接

### 生成签名串

1. 拼接参数。对要求签名的参数按照字母表或数字表递增顺序的排序，先考虑第一个字母，在相同的情况下考虑第二个字母，依此类推。
<table>
<thead>
<tr>
<th>参数名称</th>
<th>必选</th>
<th>类型</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>action</td>
<td>是</td>
<td>String</td>
<td>操作动作，固定为 roleLogin</td>
</tr>
<tr>
<td>timestamp</td>
<td>是</td>
<td>Int</td>
<td>当前时间戳</td>
</tr>
<tr>
<td>nonce</td>
<td>是</td>
<td>Int</td>
<td>随机整数，取值10000-100000000</td>
</tr>
<tr>
<td>secretId</td>
<td>是</td>
<td>String</td>
<td>STS 返回的临时 AK</td>
</tr>
</tbody></table>

 **拼凑参数示例：**
`action=roleLogin&nonce=67439&secretId=AKI***PLE&timestamp=1484793352`

2. 拼接签名串。按请求方法 + 请求主机 +请求路径 + ? + 请求字符串的规则拼接签名串。
<table>
<thead>
<tr>
<th>参数</th>
<th>必选</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td>请求主机和路径</td>
<td>是</td>
<td>固定为 cloud.tencent.com/login/roleAccessCallback</td>
</tr>
<tr>
<td>请求方法</td>
<td>是</td>
<td>支持 GET 或 POST</td>
</tr>
</tbody></table>

 **拼接签名串示例：**
`GETcloud.tencent.com/login/roleAccessCallback?action=roleLogin&nonce=67439&secretId=AKI***PLE&timestamp=1484793352`

3. 生成签名串。使用 HMAC-SHA1 算法对字符串签名，目前支持 HMAC-SHA1 和 HMAC-SHA256，以Python 语言为例：
```
sts_secret_id = "AKI***PLE"
sts_secret_key = "IF***Wn3"
sig_str = 'GETcloud.tencent.com/login/roleAccessCallback?action=roleLogin&nonce=' + str(nonce) + '&secretId=' + sts_secret_id + '&timestamp=' + str(timestamp)
sign_str = base64.b64encode(hmac.new(bytes(sts_secret_key, encoding='utf-8'), bytes(sig_str, encoding='utf-8'), hashlib.sha1).digest())
```


### 拼凑最终访问链接
1. 获取 APM 控制台页面。
`https://console.cloud.tencent.com/apm?rid=8&hideWidget=true&hideTopNav=true`

URL 参数说明：

| 参数名称    | 必选 | 类型    | 描述                                                      |
| ----------- | ---- | ------- | --------------------------------------------------------- |
| hideWidget  | 否   | Boolean | 是否隐藏智能客服图标：默认不隐藏，true 表示隐藏           |
| hideTopNav  | 否   | Boolean | 是否隐藏腾讯云控制台顶部导航栏：默认不隐藏，true 表示隐藏 |
| hideLeftNav | 否   | Boolean | 是否隐藏腾讯云控制台左侧导航栏：默认不隐藏，true 表示隐藏 |

2. 拼接完整登录信息以及目的页地址进行登录，参数值需要 urlencode 编码。
```
https://cloud.tencent.com/login/roleAccessCallback
?algorithm=<签名时加密算法，目前只支持 sha1 和 sha256 ，不填默认 sha1
&secretId=<签名时 secretId>
&token=<临时密钥 token>
&nonce=<签名时 nonce>
&timestamp=<签名时 timestamp>
&signature=<签名串>
&s_url=<登录后目的 URL>
```
3. 使用生成的最终链接，访问腾讯云 APM 控制台页面。
```
https://cloud.tencent.com/login/roleAccessCallback?algorithm=sha1&secretId=AK***Lb&token=yXJYBcXqi***qPos_52PCpauvYykeiSpVZ7w5g2qOvV1Azs&nonce=67439&timestamp=1484793352&signature=AJ***3D&s_url=https%3A//console.cloud.tencent.com/apm%3FhideWidget%3Dtrue%26hideTopNav%3Dtrue
```

## 完整实例代码

python 语言完整实例代码：

```
import json
import random
import time
import base64
import hmac
import hashlib
from urllib.parse import quote
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cam.v20190116 import cam_client, models as cam_models
from tencentcloud.sts.v20180813 import sts_client, models as sts_models

try:
    role = "CompanyOpsRole"
    uin = 100020507208

    # 步骤一：创建角色
    secret_id = "AK***NO"
    secret_key = "lG***Zx"
    cred = credential.Credential(secret_id, secret_key)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "cam.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cam_client.CamClient(cred, "", clientProfile)

    # 步骤二：创建 CAM 角色
    req = cam_models.CreateRoleRequest()
    params = {
        "RoleName": role,
        "PolicyDocument": "{\"version\":\"2.0\",\"statement\":[{\"action\":\"name/sts:AssumeRole\",\"effect\":\"allow\",\"principal\":{\"qcs\":[\"qcs::cam::uin/" + str(
            uin) + ":root\"]}}]}",
        "ConsoleLogin": 1
    }
    req.from_json_string(json.dumps(params))
    client.CreateRole(req)

    # 步骤三：绑定权限策略到角色
    req = cam_models.AttachRolePolicyRequest()
    params = {
        "AttachRoleName": role,
        "PolicyName": "QcloudAPMReadOnlyFullAccess"
    }
    req.from_json_string(json.dumps(params))
    client.AttachRolePolicy(req)

    # 步骤四：请求 AssumeRole
    client = sts_client.StsClient(cred, "ap-shanghai")
    req = sts_models.AssumeRoleRequest()
    req.RoleArn = "qcs::cam::uin/" + str(uin) + ":roleName/" + role
    req.RoleSessionName = "test"
    resp = client.AssumeRole(req)

    # 步骤五：生成签名串
    sts_secret_id = resp.Credentials.TmpSecretId
    sts_secret_key = resp.Credentials.TmpSecretKey
    token = resp.Credentials.Token
    nonce = random.randint(10000, 100000000)
    timestamp = int(time.time())

    sig_str = 'GETcloud.tencent.com/login/roleAccessCallback?action=roleLogin&nonce=' + str(
        nonce) + '&secretId=' + sts_secret_id + '&timestamp=' + str(timestamp)
    sign_str = base64.b64encode(
        hmac.new(bytes(sts_secret_key, encoding='utf-8'), bytes(sig_str, encoding='utf-8'), hashlib.sha1).digest())

    # 步骤六：拼凑最终访问链接
    result = 'https://cloud.tencent.com/login/roleAccessCallback?algorithm=sha1&secretId=' + \
             quote(sts_secret_id) + '&token=' + quote(token) + '&nonce=' + str(nonce) + '&timestamp=' + str(
        timestamp) + '&signature=' + quote(sign_str) + \
             '&s_url=' + quote('https://console.cloud.tencent.com/apm?hideWidget=true&hideTopNav=true')
    print(result)
except TencentCloudSDKException as err:
    print(err)
```
