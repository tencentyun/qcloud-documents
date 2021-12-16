## 支持环境
- Python 2.7，3.6至3.9版本。
- 调用地址：`vm.tencentcloudapi.com`。
>!API 支持就近地域接入，本产品就近地域接入的域名为 vm.tencentcloudapi.com，也支持指定地域域名访问，例如：广州地域的域名为 vm.ap-guangzhou.tencentcloudapi.com。详细请参考 [视频内容安全-请求结构](https://cloud.tencent.com/document/product/1265/51883)。
>

## 安装 SDK
### 方式1：通过 Pip 安装（推荐）
可通过 pip 安装方式将腾讯云 Python SDK 安装至您的项目中，在命令行中执行以下命令，安装 Python SDK。
```
pip install --upgrade tencentcloud-sdk-python
```
>?
>- 若您的项目环境未安装 pip，请前往 [pip 官网](https://pip.pypa.io/en/stable/installation/) 完成安装。
>- 若同时具备 Python2 及 Python3 环境，则需使用 pip3 命令进行安装。中国大陆地区的用户可以使用国内镜像源提高下载速度，例如：`pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python`。
>- 如果只想使用某个具体产品的包，例如云服务器 CVM，可以单独安装，但是注意不能和总包同时工作。
>- 更多 SDK 支持的云产品，请参见 [云产品名列表](https://cloud.tencent.com/document/product/494/42698#.E6.94.AF.E6.8C.81-sdk-3.0.E7.89.88.E6.9C.AC.E7.9A.84.E4.BA.91.E4.BA.A7.E5.93.81.E5.88.97.E8.A1.A8)。

### 方式2：通过源码包安装
前往[ Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-python) 下载源码压缩包，解压后输入以下命令：
```
$ cd tencentcloud-sdk-python
$ python setup.py install
```

## 使用 SDK
引用方法可参考示例，以下为 ImageModeration 接口的 demo 示例，其中 region 配置为广州，实际请按需配置。
```
import json from tencentcloud.common
import credential from tencentcloud.common.profile.client_profile
import ClientProfile from tencentcloud.common.profile.http_profile
import HttpProfile from tencentcloud.common.exception.tencent_cloud_sdk_exception
import TencentCloudSDKException from tencentcloud.vm.v20201229
import vm_client, models
try: cred = credential.Credential("SecretId", "SecretKey") httpProfile = HttpProfile() httpProfile.endpoint = "vm.tencentcloudapi.com"
clientProfile = ClientProfile() clientProfile.httpProfile = httpProfile client = vm_client.VmClient(cred, "ap-guangzhou", clientProfile) req = models.TextModerationRequest() params = {}
req.from_json_string(json.dumps(params)) resp = client.TextModeration(req) print(resp.to_json_string()) except TencentCloudSDKException as err: print(err)
```
