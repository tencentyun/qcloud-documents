欢迎使用腾讯云命令行工具 TCCLI，TCCLI 是管理腾讯云资源的统一工具。通过腾讯云命令行工具，您可以快速轻松的调用腾讯云 API 来管理您的腾讯云资源。您还可以基于腾讯云的命令行工具来做自动化和脚本处理，能够以更多样的方式进行组合和重用。 

## 产品功能

### 多产品集成

命令行工具集成了腾讯云所有支持云 API 的产品，可以在命令行下完成对腾讯云产品的配置和管理。包括使用 CLI 创建云服务器，操作云服务器，通过 CLI 创建 CBS 盘、查看 CBS 盘使用情况，通过 CLI 创建 VPC 网络、往 VPC 网络中添加资源等等，所有在控制台页面能完成的操作，均能在命令行工具上执行命令实现。

通过腾讯云命令行工具，可以进行无图形页面操作腾讯云资源。

### 多账户支持

命令行工具支持设置多个账号，可完成账号间快速切换。

### 多平台支持

支持在 Windows、Mac OS、Linux/Unix 等操作系统上安装和使用，满足不同开发者的要求。Linux/Unix 环境下支持命令自动补齐。
在 Windows，MacOS，Linux/Unix 操作系统上安装 Python 环境后，即可通过 pip 命令执行安装腾讯云命令行工具。在Linux 下使用熟练后，切换到 Windows 上同样可以执行相应操作，各个平台对应功能的执行命令均相同，无差异化的指令。

### 多种输出格式

命令行工具支持多种输出格式，可以自由选择 text、json、table 等作为输出格式。

* text 是以文本的形式输出，每个返回一行为一条记录，用空格隔开，适合获取资源列表保存成文本或自行转换成表格。
* json 是以 json 形式返回，适合二次开发编码，通过解析 json 返回获取想要的信息。
* table 是以表格形式返回，可视化较好，适合单纯使用命令行工具操作云资源。

## 操作指南

### 步骤一. 安装TCCLI

#### 前提条件

安装 Python 环境和 pip 工具，安装命令行工具前请确保您的系统已经安装了 Python 环境和 pip 工具。安装步骤可参考：Python SDK 文档。

>  **注意**  Python 版本必须为2.7及以上版本，更多内容请参考 [Python](https://www.python.org/) 和 [pip](https://pypi.org/project/pip/) 官网文档。 

#### 相关说明

TCCLI 依赖于 TencentCloudApi Python SDK，如果 TencentCloudApi Python SDK 的版本号小于要安装 TCCLI 版本号，在安装 TCCLI 时会自动升级 TencentCloudApi Python SDK。

#### 操作步骤

1. 安装TCCLI，按 **Win+R** 打开运行窗口输入 cmd 并单击【确定】。如下图所示：

   ![](https://main.qcloudimg.com/raw/f1206af2dd8361a6a5884ee6af4739a3.png)

2. 在命令行窗口中，执行以下命令进行TCCLI的安装：

   ```
   pip install tccli
   ```

3. 安装完成之后，执行以下命令检测是否安装成功。 

   ```
   tccli version
   ```

   返回结果如下图所示，及安装成功。

    ![https://main.qcloudimg.com/raw/e506487db4bc1c4bda2a48b65d61244c.png](https://main.qcloudimg.com/raw/e506487db4bc1c4bda2a48b65d61244c.png) 

### 步骤二. 配置TCCLI

#### 操作步骤

1. 交互模式，您可以通过在命令行输入 `tccli configure` 命令进入交互模式快速配置。 

   ```bash
   $ tccli configure
   TencentCloud API secretId [*afcQ]:AKIDwLw1234xxxxxxxxxxnR2OTI787aBCDP
   TencentCloud API secretKey [*ArFd]:OxXj7khcV1234xxxxxxxxxdCc1LiArFd
   region: ap-guangzhou
   output[json]:
   ```

   ![](https://main.qcloudimg.com/raw/665e5334b0d5db156ef48a19072ba8bd.png)

   * **secretId**：云 API 密钥 SecretId，前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取（一个主账号最多可以申请两对 云 API 密钥）。
   * **secretKey**：云 API 密钥 SecretKey，前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
   * **region**： 云产品地域，请前往对应云产品的 [API 文档](https://cloud.tencent.com/document/api) 获取可用的 region。例如云服务器的 [地域列表](https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
   * **output**： 可选参数，请求回包输出格式，支持 [json table text] 三种格式，默认为 json。
     更多信息请执行 `tccli configure help` 查看。

2. 命令行模式，通过命令行模式您可以在自动化脚本中配置您的信息。 

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

    更多信息请执行 `tccli configure [list get set] help` (列表里三选一)查看：如 `tccli configure list help`。 

3. 多账户支持，TCCLI 支持多账户，方便您多种配置同时使用。 

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

### 步骤三. 使用TCCLI

* 通过`tccli cvm DescribeInstances`命令查看当前账号有哪些云服务器。
* 通过`tccli cbs DescribeDisks`命令查看有 CBS 盘列表。

#### 操作示例

**注意** ： 请注意 demo 中非简单类型的参数必须为标准 json 格式。 

 以创建一台 CVM 为例，执行以下命令。 

```bash
$ tccli cvm RunInstances --InstanceChargeType POSTPAID_BY_HOUR --InstanceChargePrepaid '{"Period":1,"RenewFlag":"DISABLE_NOTIFY_AND_MANUAL_RENEW"}' --Placement '{"Zone":"ap-guangzhou-2"}' --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}' --InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' --InstanceCount 1 --InstanceName TCCLI-TEST --LoginSettings '{"Password":"isd@cloud"}' --SecurityGroupIds '["sg-0rszg2vb"]' --HostName TCCLI-HOST-NAME1
```

**说明：**

>  更多功能，您可以通过`tccli help`查看支持的产品，通过`tccli cvm help`（以 CVM 举例）查看产品支持的接口。通过`tccli cbs DescribeDisks help`（以 CBS 产品的 DescribeDisks 接口为例） 查看接口支持的参数。 

### 使用高级功能

#### 操作场景

> 详细介绍如何使用 TCCLI 高级功能，包括多版本接口访问、指定最近的接入点和返回结果过滤。

#### 操作步骤

##### 多版本接口访问

某些产品可能存在多个版本的接口，TCCLI 默认访问最新版本的接口。如果您想访问特定旧版本的接口，可以通过以下方式实现（以 CVM 举例）。

```bash
# 设置 cvm 产品默认使用版本:2017-03-12
tccli configure set cvm.version 2017-03-12

# 在实时使用时指定版本号。
tccli cvm help --version 2017-03-12
tccli cvm DescribeZones help --version 2017-03-12
tccli cvm DescribeZones --version 2017-03-12
```

##### 指定最近的接入点（Endpoint）

TCCLI 默认会请求就近的接口点访问服务，您也可以针对某一产品指定自己的 Endpoint（以 CVM 为例）。

```bash
# 设置cvm产品默认 endpoint
tccli configure set cvm.endpoint cvm.ap-guangzhou.tencentcloudapi.com

# 调用时实时指定。
tccli cvm DescribeZones --endpoint cvm.ap-guangzhou.tencentcloudapi.com
```

1. 不加任何过滤时的输出（以 CVM DescribeZones 接口的返回为例）。

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

   **注意**：这里需要将说明过滤行为的内容用单引号包裹起来。

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

## 常见问题

### 如何购买命令行工具？

本服务免费。当您遇到问题时，请 [联系我们](https://cloud.tencent.com/act/event/connect-service) 寻求相应的帮助。

### 接口鉴权如何实现？

在 API 的每个产品下，都可以通过单击每个产品下的调用方法下的接口鉴权进行查看，例如云服务器（CVM）可以单击这里查看 [云服务器接口鉴权](https://cloud.tencent.com/document/api/213/15693)。

### 提示如下错误码 10060，如何处理？

```
Socket error 10060 - Connection timed out
```

10060 是 Socket 编程接口给出的错误，表示网络连接超时，遇到这个问题，是由于您的机器和腾讯云云API服务器之间的网络无法连通，可以检查下面几点问题：

* 本地访问外网是否需要设置代理。
* 本地机器防火墙是否有限制外访的规则。
* 路由器是否有限制外访的规则。

### 腾讯云 API 的错误码有哪些？

腾讯云 API 的错误码通常分为公共错误码和非公共错误码。公共错误码一般可以单击每个产品下的调用方式，返回结果查看。非公共错误码可以在具体的接口描述页面查看。单击这里可以查看 [错误码](https://cloud.tencent.com/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)（以 CVM 为例）。
