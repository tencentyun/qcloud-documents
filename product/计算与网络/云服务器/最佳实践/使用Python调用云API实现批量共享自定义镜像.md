## 操作步骤
本文介绍如何通过 Python SDK 调用 API 接口，通过子用户批量共享云服务器自定义镜像。若您具备类似需求，或想了解如何使用 SDK，可参考本文进行操作。


## 前提条件[](id:preconditions)
- 已创建子用户，并已具备云服务器及云 API 所有权限。
 - 创建子用户请参见 [新建子用户](https://cloud.tencent.com/document/product/598/13674)。
 - 为子用户授予权限请参见 [子用户权限设置](https://cloud.tencent.com/document/product/598/36256)，本文为子用户授予 `QcloudCVMFullAccess` 及 `QcloudAPIFullAccess` 预设策略。
 - 为子用户创建 SecretId 与 SecretKey，操作步骤请参见 [子账号访问密钥管理](https://cloud.tencent.com/document/product/598/37140)。请记录并妥善保管。
- 已具备待共享自定义镜像。如需创建，请参见 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942)。


## 操作步骤

### 安装 Python
1. 执行以下命令查看当前云服务器是否已经安装 Python 3.6+版本，若已安装，则可以跳过安装步骤。
```shellsession
python --version
```
2. 若您的云服务器没有安装 Python。
 - CentOS 操作系统的云服务器可以执行以下命令安装。
```shellsession
yum install python3
```
 - Ubuntu/Debian 操作系统的云服务器可以执行以下命令安装。
```shellsession
sudo apt install python3
```
 - 其他操作系统您可以前往 [Python 官网](https://www.python.org/doc/)，下载 Python 3.6+版本并上传至 Linux 服务器中，解压并安装 Python。
3. 安装完成后，请执行以下命令核实 Python 版本。
```shellsession
python --version
```

### 创建代码
1. 在调用机器上新建 `test.py` 文件，并输入以下代码。
```python
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

# 默认读取环境变量 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY 获取 secretId 和 secretKey
# 更多凭证管理方式，请参考：https://github.com/TencentCloud/tencentcloud-sdk-python#%E5%87%AD%E8%AF%81%E7%AE%A1%E7%90%86
cred = credential.EnvironmentVariableCredential().get_credential()
httpProfile = HttpProfile()
httpProfile.endpoint = "cvm.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile

# 举例为南京 请按实际情况进行修改 例如上海请修改为ap-shanghai
aria = 'ap-nanjing'
client = cvm_client.CvmClient(cred,aria, clientProfile)
def img_share(img_id,img_name,accountids):
    try:
        req1 = models.ModifyImageSharePermissionRequest()
        params1 = {
            "ImageId": img_id,
            "AccountIds": accountids,
            "Permission": "SHARE"
        }
        req1.from_json_string(json.dumps(params1))

        resp1 = client.ModifyImageSharePermission(req1)
        response1 = json.loads(resp1.to_json_string())
        print(img_name,'共享成功！',response1)
    except TencentCloudSDKException as err:
        print(img_name,'共享失败!',err)
try:
    req = models.DescribeImagesRequest()
    params = {
        "Filters": [
            {
                "Name": "image-type",
                "Values": ["PRIVATE_IMAGE"]
            }
        ],
        "Limit": 100
    }
    req.from_json_string(json.dumps(params))
    resp = client.DescribeImages(req)
    response = json.loads(resp.to_json_string())
    img_num = response["TotalCount"]
    print('正在获取镜像列表....')
    share_config = input('1.共享所有镜像\n\n2.让我决定每一个镜像\n\n输入1或2并按回车 默认为2：') or '2'
    accountids = input('请输入被共享人uin 多个以英文逗号隔开：').split(",")
    for i in range(img_num):
        basic = response['ImageSet'][i]
        img_id = basic['ImageId']
        img_name = basic['ImageName']
        if share_config == '1':
            img_share(img_id,img_name,accountids)
        elif share_config == '2':
            print('镜像id：',img_id,'镜像名称：',img_name)
            share_choice = input('是否共享此镜像 y/n:') or 'y'
            if share_choice == 'y':
                img_share(img_id,img_name,accountids)
            elif share_choice == 'n':
                continue
            else:
                print('请输入正确的选项！！')
        else:
            print('请输入正确的选项！！')

except TencentCloudSDKException as err:
    print(err)
```
 - **SecretId 与 SecretKey**：请替换为已在 [前提条件](#preconditions) 中创建的子用户 SecretId 与 SecretKey。
 - **aria**：请替换为待共享自定义镜像实际所在地域。地域列表可参见 [地域列表](https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
2. 在调用机器的命令行中执行以下命令，运行代码。
```shellesession
python test.py
```
根据屏幕提示输入1或2，同时共享所有镜像或依次选择共享镜像，并输入对端账号 ID。您可通知对方前往 [账号信息](https://console.cloud.tencent.com/developer) 页面获取。
共享成功后，将返回对应数量的 RequestID。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/724301d2dd4c1c612e6649e2b765ee09.png)

## 相关接口文档
本文代码调用接口为 [查看镜像列表](https://cloud.tencent.com/document/product/213/15715) 及 [修改镜像分享信息](https://cloud.tencent.com/document/api/213/15710)。

