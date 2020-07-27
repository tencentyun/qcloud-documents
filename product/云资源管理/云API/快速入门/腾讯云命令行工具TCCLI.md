欢迎使用腾讯云命令行工具 TCCLI，TCCLI 是管理腾讯云资源的统一工具。通过腾讯云命令行工具，您可以快速轻松的调用腾讯云 API 来管理您的腾讯云资源。您还可以基于腾讯云的命令行工具来做自动化和脚本处理，能够以更多样的方式进行组合和重用。 



## 安装 TCCLI
1. 安装 Python 环境和 pip 工具，安装命令行工具前请确保您的系统已经安装了 Python 环境和 pip 工具。详情请参见 [Python SDK](https://cloud.tencent.com/document/sdk/Python) 文档。
>!
>- Python 版本必须为2.7及以上版本，更多内容请参考 [Python](https://www.python.org/) 和 [pip](https://pypi.org/project/pip/) 官网文档。 
>- TCCLI 依赖于 TencentCloudApi Python SDK，如果 TencentCloudApi Python SDK 的版本号小于要安装 TCCLI 版本号，在安装 TCCLI 时会自动升级 TencentCloudApi Python SDK。
>
2. 按 **Win+R** 打开运行窗口输入 cmd 并单击【确定】。
3. 在命令行窗口中，执行以下命令进行 TCCLI 安装。
```
pip install tccli
```
4. 执行以下命令，查看 TCCLI 是否安装成功。
```
tccli version
```
返回类似如下结果，则说明已成功安装 TCCLI。如下图所示：
![](https://main.qcloudimg.com/raw/a1523cb81e8f38b315147a4e13bcb0be.png)

## 配置 TCCLI
1. 在命令行中执行以下命令，进入交互模式快配置。
```bash
tccli configure
```
返回结果如下，请参考以下信息进行配置：
```bash
 TencentCloud API secretId [*afcQ]:
 TencentCloud API secretKey [*ArFd]:
 region: 
 output[json]:
```
 * **secretId**：云 API 密钥 SecretId，前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取（一个主账号最多可以申请两个云 API 密钥）。
 * **secretKey**：云 API 密钥 SecretKey，前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
 * **region**： 云产品地域，请前往对应云产品的 [API 文档](https://cloud.tencent.com/document/api) 获取可用的 region。例如云服务器的 [地域列表](https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
 * **output**： 可选参数，请求回包输出格式，支持 JSON、table 及 text 三种格式，默认为 JSON。
     更多信息请执行 `tccli configure help` 命令查看。
2. 您可执行以下命令进入命令行模式，通过命令行模式您可以在自动化脚本中配置您的信息。 
```bash
 # set子命令可以设置某一配置，也可同时配置多个。
 tccli configure set secretId AKIDwLw1234xxxxxxxxxxxnR2OTI787aBCDP
 tccli configure set region ap-guangzhou  output json
 # get子命令用于获取配置信息。
 tccli configure get secretKey
 secretKey = OxXj7khcV1234xxxxxxxxxdCc1LiArFd
 # list子命令打印所有配置信息。
 tccli configure list
 credential:
 secretId =  AKIDwLw1234xxxxxxxxxxnR2OTI787aBCDP
 secretKey =  OxXj7khcV1234xxxxxxxxxdCc1LiArFd
 configure:
 region =  ap-guangzhou
 output =  json
```
更多信息请执行 `tccli configure [list、get 或 set] help` 查看，例如 `tccli configure list help`。 
3. 您可执行以下命令配置多账户支持，方便您在多种配置同时使用。 
```bash
 # 在交互模式中指定账户名 test。
 $ tccli configure --profile test
 TencentCloud API secretId [*BCDP]:AKIDwLw1234xxxxxxexxxxR2OTI787aBCDP
 TencentCloud API secretKey [*ArFd]:OxXj7khcV1234xxxxxxxxxdCc1LiArFd
 region: ap-guangzhou
 output[json]:
 # set/get/list子命令指定账户名 test。此命令与上条命令作用相同
 $ tccli configure set region ap-guangzhou  output json secretId AKIDwLw1234xxxxxxexxxxR2OTI787aBCDP secretKey OxXj7khcV1234xxxxxxxxxdCc1LiArFd --profile test
 # 已可以修改单独一个，例如修改地域：
 $ tccli configure set region ap-beijing
 # 查看test用户密钥key或查看配置, 使用命令如下：
 $ tccli configure get secretKey --profile test
 $ tccli configure list --profile test
 # 在调用接口时指定账户（以 cvm DescribeZones 接口为例）。
 $ tccli cvm DescribeZones --profile test
```

## 使用 TCCLI

您可通过以下示例开始使用 TCCLI，执行以下命令，创建一台 CVM：
>!请注意 demo 中非简单类型的参数必须为标准 JSON 格式。 
>
```bash
$ tccli cvm RunInstances --InstanceChargeType POSTPAID_BY_HOUR --InstanceChargePrepaid '{"Period":1,"RenewFlag":"DISABLE_NOTIFY_AND_MANUAL_RENEW"}' --Placement '{"Zone":"ap-guangzhou-2"}' --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}' --InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' --InstanceCount 1 --InstanceName TCCLI-TEST --LoginSettings '{"Password":"isd@cloud"}' --SecurityGroupIds '["sg-0rszg2vb"]' --HostName TCCLI-HOST-NAME1
```
您还可通过以下命令，进一步使用 TCCLI：
- 执行 `tccli help` 命令，查看支持的产品。
- 以 CVM 为例，执行 `tccli cvm help` 命令，查看产品支持的接口。
- 以 CBS 的 DescribeDisks 接口为例，执行 `tccli cbs DescribeDisks help` 命令，查看接口支持的参数。


## 使用高级功能
该步骤以 CVM 为例，详细介绍了如何使用 TCCLI 高级功能，包括多版本接口访问、指定最近的接入点和返回结果过滤。

### 多版本接口访问

某些产品可能存在多个版本的接口，TCCLI 默认访问最新版本的接口。如果您想访问特定旧版本的接口，可以通过以下方式实现。
```bash
# 设置 cvm 产品默认使用版本:2017-03-12
tccli configure set cvm.version 2017-03-12

# 在实时使用时指定版本号。
tccli cvm help --version 2017-03-12
tccli cvm DescribeZones help --version 2017-03-12
tccli cvm DescribeZones --version 2017-03-12
```

### 指定最近的接入点（Endpoint）

TCCLI 默认会请求就近的接口点访问服务，您也可以针对某一产品指定自己的 Endpoint。
```bash
# 设置cvm产品默认 endpoint
tccli configure set cvm.endpoint cvm.ap-guangzhou.tencentcloudapi.com

# 调用时实时指定。
tccli cvm DescribeZones --endpoint cvm.ap-guangzhou.tencentcloudapi.com
```


### 返回结果过滤
- 以 CVM DescribeZones 接口的返回为例，不加任何过滤时的输出。
```bash
   [root@VM_180_248_centos ~]# tccli cvm DescribeZones
   {
    "TotalCount": 4,
    "ZoneSet": [
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100001",
            "Zone": "ap-guangzhou-1",
            "ZoneName": "广州一区"
        },
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100002",
            "Zone": "ap-guangzhou-2",
            "ZoneName": "广州二区"
        },
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100003",
            "Zone": "ap-guangzhou-3",
            "ZoneName": "广州三区"
        },
        {
            "ZoneState": "AVAILABLE",
            "ZoneId": "100004",
            "Zone": "ap-guangzhou-4",
            "ZoneName": "广州四区"
        }
    ],
    "RequestId": "4fd313a6-155f-4c7a-bf86-898c02fcae02"
   }
```
2. 只看某个字段。
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter TotalCount
4
```
3. 指定某个数组类型对象的第 N 个子对象的信息。
```bash
 [root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter ZoneSet[0]
 {
	"ZoneState": "AVAILABLE",
	"ZoneId": "100001",
	"Zone": "ap-guangzhou-1",
	"ZoneName": "广州一区"
 }
```
4. 指定数组类型对象下所有某个名称的子对象的某个字段。
```bash
   [root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter ZoneSet[*].ZoneName
   [
    "广州一区",
    "广州二区",
    "广州三区",
    "广州四区"
   ]
```
5. 过滤数组里的子对象，同时还以新的名称展示。 
>!需要将说明过滤行为的内容用单引号包裹起来。
>
```bash
   [root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter 'ZoneSet[*].{name:ZoneName, id:ZoneId}'
    [
            {
                    "name": "广州一区",
                    "id": "100001"
            },
            {
                    "name": "广州二区",
                    "id": "100002"
            },
            {
                    "name": "广州三区",
                    "id": "100003"
            },
            {
                    "name": "广州四区",
                    "id": "100004"
            }
    ]
```

## 相关问题

#### 如何购买命令行工具？

本服务免费。当您遇到问题时，请 [联系我们](https://cloud.tencent.com/act/event/connect-service) 寻求相应的帮助。

#### 如何实现接口鉴权？
在 API 支持的每个产品文档目录下，可选择【调用方法】>【接口鉴权】，结合产品的“接口鉴权”文档进行实现。例如，可前往 [CVM 接口鉴权](https://cloud.tencent.com/document/api/213/15693) 进行查看。

