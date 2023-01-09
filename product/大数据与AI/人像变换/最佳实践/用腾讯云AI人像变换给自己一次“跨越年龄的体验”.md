互联网时代，日新月异的技术更迭让大众的娱乐方式变得更加多元化。越来越多线上娱乐体验成为新潮流，不少公司各出奇招，推出了 AI 人像特效、VR 游景点、可交互影视剧、元宇宙等；人们花在线上娱乐体验的时间越来越多，也越来越愿意为泛娱乐体验相关的产品服务买单。

以 AI 人像特效为例，现实情况是，大部分新颖的玩法背后都面临困境，或是创意公司缺乏开发能力，或者中小企业缺乏高易用性、高性价比的 AI 产品服务。那么，是否有更智能、简化的方式赋能企业、开发者打造泛娱乐产品服务呢？

通过调研市场上现有的能力，发现腾讯云 AI 推出的人像变换非常有趣，可以选择 API、SDK 等多种接入方式；里面包含年龄变换、性别转换、人像渐变、动漫化等能力，每个基础能力既可单独使用，也能组合使用。

接下来我将尝试用年龄变换和人像渐变能力制作一种“年龄渐变”的视觉感受，此类玩法可以用在一些老少皆宜的宣传广告，或者个人成长的特效体验上。

先看一段视频效果。
<img src="https://qcloudimg.tencent-cloud.cn/raw/380ebd09ac2783bbcc4b555e3b5c271d.gif" width="50%">

## 1. 准备工作
在试用云服务前，应该有一些准备工作要做，例如了解这个产品的效果能否令人满意、费用是否实惠、服务需不需要开通等。

### 1.1 体验效果
为了决定是否使用这个服务的能力，我想体验下这个效果。看了下产品首页有 demo 体验功能，还挺详细的，支持各种参数调节，且拖拽式的实时效果展示，单击进行可 [体验效果](https://cloud.tencent.com/product/ft)。
![](https://qcloudimg.tencent-cloud.cn/raw/8e7cd4e2cd46697dbf9f5f9f54a04c9a.png)

### 1.2 了解计费方式
在正式试用之前，我也想了解下他的计费规则。万一收费很贵那试用就要慎重了，但是好在官网页面上有明确的 [购买计费方式](https://cloud.tencent.com/document/product/1202/45860)，且有 [免费额度](https://cloud.tencent.com/document/product/1202/45861) 的说明，看上去可以放心使用了。
![](https://qcloudimg.tencent-cloud.cn/raw/b2e9cd124ec1d75678b201cfadcfd551.png)
这里的计费模式我也研究了下，大体的意思是说：
1. 人像变换下的所有产品每个月会有**1000次免费调用额度**。
2. 预付费调用方式，提前买好不同量级的资源包，调用时会进行抵扣。偶尔会有优惠活动，且资源包一年有效，这个月用不完下个月用。
3. 后付费调用方式，没有买资源包或资源包消耗完会根据后付费规则计费。
4. 扣减顺序为**免费资源包** > **预付费资源包** > **后付费**。

### 1.3 开通人像变换服务
正式使用人像变换服务好像要开通下现有服务，和腾讯云其他产品比较像。单击下开通即可。
![](https://qcloudimg.tencent-cloud.cn/raw/ccb3ce62cdbf981697bfc21279cae2c1.png)

### 1.4 获取 API 调用密钥
在 [访问管理](https://console.cloud.tencent.com/cam/capi) 里可以获取到当前账号的 SecretId 和 SecretKey，以便于后面调用云服务的前面验证。这个一定要保管好，泄露出去有被人盗刷的风险。已废弃或者有暴露风险的 Secret 也可以禁用，最大程度降低风险。
![](https://qcloudimg.tencent-cloud.cn/raw/924b2af9b8e701ca4f5e5d0ddaa9e3c9.png)


## 2. API 调用

### 2.1 查看接口文档
在 [API 文档](https://cloud.tencent.com/document/product/1202/41959) 选项栏里可以看到各个接口的参数说明，以下以人脸年龄变换和人像变换举例。

#### 2.1.1 人脸年龄变换
人脸年龄变换的 [接口文档](https://cloud.tencent.com/document/product/1202/41968) 里有输入参数和输出参数两部分，输入参数就是我们要传进去的内容，一般是图片。输出参数就是接口的返回，一般是结果图片。

输入参数里还包含公共参数，这部分一般是用于签名的，请求包体里一般不用带上。
![](https://qcloudimg.tencent-cloud.cn/raw/06aa61f6044793d141fcd4f0a09586da.png)
![](https://qcloudimg.tencent-cloud.cn/raw/fa8c972e05ee24f72ebf5d284cc640fd.png)
这里的 RequestId 要记得日志打印，后面有服务相关的问题可以提供这个信息来定位。

#### 2.1.2 人像渐变
人像渐变的接口和变年龄等同步接口有所不同，是一种异步处理的方式。
- [人像渐变](https://cloud.tencent.com/document/product/1202/47937)：创建一个人像渐变的处理任务，其中可以指定处理参数之类的。
- [查询人像渐变任务](https://cloud.tencent.com/document/product/1202/47936)：查询任务处理的结果，用于后面轮询查结果看看有没处理完。
- [撤销人像渐变任务](https://cloud.tencent.com/document/product/1202/47938)：取消任务。
![](https://qcloudimg.tencent-cloud.cn/raw/11d44ca58adf94624a27dcc3052c1ed0.png)
JobId 是标识任务状态的关键，整个程序 pipeline 里这个变量要记录好。

### 2.2 自动生成代码
腾讯云接口大部分都支持一个叫 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=ft&Version=2020-03-04&Action=ChangeAgePic&SignVersion=) 的工具，可以在上面自动生成代码，同时也配备有签名调试工具。
![](https://qcloudimg.tencent-cloud.cn/raw/4eda98d4521e732a9fc600bf924c8e47.png)
- 代码生成：不同语言的 SDK 调用代码，比较实用，基本上贴过来改改就可以用了。
- 在线调用：模拟一次真实调用，可以指定所有参数，测试一些 demo 页不支持的参数也行。
- 签名串生成：如果打算自己拼接 API 签名来调用，可以把自己的签名结果和这里的对比下，但是 API 签名整体比较复杂不太推荐用这种方式。

### 2.3 调试验证
以 Python 语言为例，把上面的代码拷下来基本就可以跑了。下面以在线 SDK 调用为例。

#### 2.3.1 下载 SDK
从 [官网文档](https://cloud.tencent.com/document/product/1202/41968) 上可以看到有多种不同语言版本的 SDK，我这里选了 Python 来开发体验效果。
![](https://qcloudimg.tencent-cloud.cn/raw/e53354e3761dcfb89d59f241430e9963.png)
点开的 git 项目 README，有对应语言更详细的安装方法。
![](https://qcloudimg.tencent-cloud.cn/raw/9f4960296de697f23cdab3c83047482c.png)

#### 2.3.2 粘贴生成的代码稍作修改
```
import json
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ft.v20200304 import ft_client, models

# 读一个本地测试文件转换为base64编码
f = open('./test.png', 'rb')
base64_data = base64.b64encode(f.read())

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
    # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
    cred = credential.Credential("YourSecretId", "YourSecretKey")	# 传入自己的密钥
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ft.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = ft_client.FtClient(cred, "ap-guangzhou", clientProfile)

    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.ChangeAgePicRequest()
    params = {
        "Image": base64_data.decode("utf-8"),   # Python里的bytes类型要转成string才可使用
        "AgeInfos": [
            {
                "Age": 40	# 可以测试不同的年龄看效果
            }
        ],
        "RspImgType": "url"
    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个ChangeAgePicResponse的实例，与请求对象对应
    resp = client.ChangeAgePic(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
```

可以看到效果还是不错的
![](https://qcloudimg.tencent-cloud.cn/raw/9f217780d1d30b6b061694f63095dd15.png)


## 3. 玩法升级

### 3.1 组合变年龄与渐变
了解了下，人像变换产品下还有很多其他有意思的能力，我在想这些能力如果可以组合一下，应该会很有意思。例如人脸年龄变换+人像渐变，应该可以做成年龄渐变的效果。

#### 3.1.1 将云服务接口调用包在函数里
因为 Python 是脚本语言，先将服务改为函数的形式，便于后面组合调用。
```
# 变年龄
def change_age(client, img, age):
    req = models.ChangeAgePicRequest()
    params = {
        "Image": img.decode("utf-8"),   # Python里的bytes类型要转成string才可使用
        "AgeInfos": [
            {
                "Age": int(age)
            }
        ],
        "RspImgType": "base64"
    }
    req.from_json_string(json.dumps(params))
    resp = client.ChangeAgePic(req)
    return resp
```
同理，可以把其他功能也包一下。

#### 3.1.2 异步类接口的使用
因为人像渐变是一种异步类接口，即调用时不能立即返回结果，一般是通过某些标识 ID 来区分每次调用。当后面我们要查结果时可以用这个标识 ID 来跟踪结果。常采用轮询的方式，即我们在获取到整体流程的 JobId 后隔一段固定的时间，例如2s，再调用查询结果接口，看看结果已经处理完了就收取，没有处理完就继续循环。
![](https://qcloudimg.tencent-cloud.cn/raw/ab99601c823ba43b31de8a06893da54a.png)

#### 3.1.3 最终代码
将人像渐变和年龄变换的调用组合起来。
```
import json
import sys
import time
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ft.v20200304 import ft_client, models

# 读一个本地测试文件转换为base64编码
def read_file(filename):
    f = open(filename, 'rb')
    base64_data = base64.b64encode(f.read())
    return base64_data

# 变年龄
def change_age(client, img, age):
    req = models.ChangeAgePicRequest()
    params = {
        "Image": img.decode("utf-8"),   # Python里的bytes类型要转成string才可使用
        "AgeInfos": [
            {
                "Age": int(age)
            }
        ],
        "RspImgType": "base64"
    }
    req.from_json_string(json.dumps(params))
    resp = client.ChangeAgePic(req)
    return resp

# 人像渐变
def morph_face(client, imgs):
    req = models.MorphFaceRequest()
    params = {
        "Images": imgs,
        # 更多细节可通过参数调节
        # "GradientInfos": [
        #     {
        #         "Tempo": 1,
        #         "MorphTime": 1
        #     }
        # ],
        "Fps": 25
    }
    req.from_json_string(json.dumps(params))
    resp = client.MorphFace(req)
    print(resp.to_json_string())
    return resp

# 查询人像渐变结果
def query_morph_face(client, job_id):
    req = models.QueryFaceMorphJobRequest()
    params = {
        "JobId": job_id
    }
    req.from_json_string(json.dumps(params))
    resp = client.QueryFaceMorphJob(req)
    print(resp.to_json_string())
    return resp


try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
    # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
    cred = credential.Credential("YourSecretId", "YourSecretKey")
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ft.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = ft_client.FtClient(cred, "ap-guangzhou", clientProfile)

    # 读取图片
    data = read_file(sys.argv[1])

    ages = [20, 30, 40, 50, 60]

    # 批量变年龄
    imgs = []
    for age in ages:
        resp=change_age(client, data, age)
        imgs.append(resp.ResultImage)

	# 将图片集合起来调人像渐变
    resp = morph_face(client, imgs)
    job_id = resp.JobId

    # 轮询查结果
    resp=query_morph_face(client, job_id)
    while resp.JobStatusCode != 7:
        resp=query_morph_face(client, job_id)
        time.sleep(2)
   

except TencentCloudSDKException as err:
    print(err)
```

### 3.2 调参优化效果
变年龄和渐变都支持一定程度的算法效果调整，我也是在尝试不同的效果后选一个最佳组合。
![](https://qcloudimg.tencent-cloud.cn/raw/0cfb415dbc49596ecc9a09752b5c197a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ff6e306dff3ca4cd20d8331db1a82a7b.png)

## 4. 查看调用情况
### 4.1 查接口调用量

在 [控制台页面](https://console.cloud.tencent.com/ft/change-age-pic) 可以看到对应的调用情况，这个调用量是包含预付费资源包和后付费在内的所有调用量
![](https://qcloudimg.tencent-cloud.cn/raw/b4d58c0c2fbee6841b913b8f288cd879.png)

### 4.2 查资源包扣减情况
在资源包管理页面可以看到预付费资源包扣减的情况。
![](https://qcloudimg.tencent-cloud.cn/raw/6788a60dc45078523f74d4ca190ed84c.png)


了解更多详见 [腾讯云 AI 人像变化能力](https://cloud.tencent.com/product/ft)。 

