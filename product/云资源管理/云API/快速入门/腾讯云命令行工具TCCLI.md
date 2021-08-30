欢迎使用腾讯云命令行工具 TCCLI，TCCLI 是管理腾讯云资源的统一工具。通过腾讯云命令行工具，您可以快速轻松的调用腾讯云 API 来管理您的腾讯云资源。您还可以基于腾讯云的命令行工具来做自动化和脚本处理，能够以更多样的方式进行组合和重用。 

腾讯云 TCCLI 包含基础功能和高级功能，请参见下表：
<table>
<tr>
<th>功能</th><th>描述</th>
</tr>
<tr>
<td><a href="#primaryfunction">基础功能</a></td>
<td>
<ul style="margin:0px">
<li>配置 TCCLI</li>
<li>helper 信息支持中文信息</li>
<li>支持 JSON、table 及 text 输出格式</li>
</ul>
</td>
</tr>
<tr>
<td><a href="#sophisticatedfunctions">高级功能</a></td>
<td>
<ul style="margin:0px">
<li>多版本接口访问</li>
<li>指定最近的接入点（Endpoint）</li>
<li>返回结果过滤</li>
<li>支持输出入参数据结构到 JSON 文件</li>
<li>支持从 JSON 文件读取参数调用</li>
<li>复杂类型点（.）连接展开方式调用</li>
<li>结果轮询</li>
</ul>
</td>
</tr>
</table>

## 安装 TCCLI
1. 安装 Python 环境和 pip 工具，安装命令行工具前请确保您的系统已经安装了 Python 环境和 pip 工具。详情请参见 [Python SDK](https://cloud.tencent.com/document/sdk/Python) 文档。
>!
>- Python 版本必须为2.7及以上版本，更多内容请参考 [Python](https://www.python.org/) 和 [pip](https://pypi.org/project/pip/) 官网文档。 
>- TCCLI 依赖于 TencentCloudApi Python SDK，如果 TencentCloudApi Python SDK 的版本号小于要安装 TCCLI 版本号，在安装 TCCLI 时会自动升级 TencentCloudApi Python SDK。
>
2. Windows 系统按 **Win+R** 打开运行窗口输入 cmd 并单击**确定**，本文以 Linux 为例。
3. 在命令行窗口中，执行以下命令进行 TCCLI 安装。
```
pip install tccli
```
>! 3.0.252.3以下版本升级需要执行以下代码：
```
sudo pip uninstall tccli jmespath
sudo pip install tccli
```
>
4. 执行以下命令，查看 TCCLI 是否安装成功。
```
tccli --version
```
返回类似如下结果，则说明已成功安装 TCCLI。
```bash
[root@VM_180_248_centos ~]# tccli --version
3.0.250.1
```
5. 在 Linux 环境中，执行以下命令启动自动补全功能，支持大小写自动纠错：
```bash
complete -C 'tccli_completer' tccli
```
以下代码片段展示自动补全过程：
```bash
[root@VM_33_50_centos ~]# tccli c
cam          cbs          cdn          chdfs        ckafka       cloudhsm     cms          cr           cynosdb 
captcha      ccc          cds          cim          clb          cme          configure    cvm          
cat          cdb          cfs          cis          cloudaudit   cmq          cpdp         cws          
[root@VM_33_50_centos ~]# tccli cvm R
RebootInstances                      ResetInstance                        ResetInstancesType 
RenewHosts                           ResetInstancesInternetMaxBandwidth   ResizeInstanceDisks 
RenewInstances                       ResetInstancesPassword               RunInstances 
[root@VM_33_50_centos ~]# tccli cvm RunInstances --
--ActionTimer               --generate-cli-skeleton     --InstanceType              --SecurityGroupIds 
--ClientToken               --HostName                  --InternetAccessible        --SystemDisk 
--cli-input-json            --HpcClusterId              --LoginSettings             --TagSpecification 
--DataDisks                 --ImageId                   --output                    --timeout 
--DisasterRecoverGroupIds   --InstanceChargePrepaid     --Placement                 --UserData 
--DryRun                    --InstanceChargeType        --profile                   --version 
--endpoint                  --InstanceCount             --region                    --VirtualPrivateCloud 
--EnhancedService           --InstanceMarketOptions     --secretId                  
--filter                    --InstanceName              --secretKey                 
[root@VM_33_50_centos ~]# tccli cvm RunInstances --Placement 
```
>?您也可以将该命令加入环境变量（`/etc/profile`）中，使自动补全功能一直有效。

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
 * **secretId**：云 API 密钥 SecretId，请前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取（一个主账号最多可以申请两个云 API 密钥）。
 * **secretKey**：云 API 密钥 SecretKey，请前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
 * **region**： 云产品地域，请前往对应云产品的 [API 文档](https://cloud.tencent.com/document/api) 获取可用的 region。例如云服务器的 [地域列表](https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
 * **output**： 可选参数，请求回包输出格式，支持 JSON、table 及 text 三种格式，默认为 JSON。
2. 您可执行以下命令进入命令行模式，通过命令行模式您可以在自动化脚本中配置您的信息。 
```bash
 # set子命令可以设置某一配置，也可同时配置多个。
 tccli configure set secretId AKIDwLw1234***********nR2OTI787aBCDP
 tccli configure set region ap-guangzhou  output json
 # get子命令用于获取配置信息。
 tccli configure get secretKey
 secretKey = OxXj7khcV1234*********dCc1LiArFd
 # list子命令打印所有配置信息。
 tccli configure list
 credential:
 secretId =  AKIDwLw1234**********nR2OTI787aBCDP
 secretKey =  OxXj7khcV1234*********dCc1LiArFd
 configure:
 region =  ap-guangzhou
 output =  json
``` 
3. 您可执行以下命令配置多账户支持，方便您在多种配置同时使用。 
```bash
 # 在交互模式中指定账户名 test。
 $ tccli configure --profile test
 TencentCloud API secretId [*BCDP]:AKIDwLw1234***********R2OTI787aBCDP
 TencentCloud API secretKey [*ArFd]:OxXj7khcV1234*********dCc1LiArFd
 region: ap-guangzhou
 output[json]:
 # set/get/list子命令指定账户名 test。此命令与上条命令作用相同
 $ tccli configure set region ap-guangzhou  output json secretId AKIDwLw1234***********R2OTI787aBCDP secretKey OxXj7khcV1234*********dCc1LiArFd --profile test
 # 已可以修改单独一个，例如修改地域：
 $ tccli configure set region ap-beijing
 # 查看test用户密钥key或查看配置, 使用命令如下：
 $ tccli configure get secretKey --profile test
 $ tccli configure list --profile test
 # 在调用接口时指定账户（以 cvm DescribeZones 接口为例）。
 $ tccli cvm DescribeZones --profile test
```
4.您可以通过以下两种方式配置 HTTPS 代理，使 TCCLI 通过代理调用 API。
 - 在环境变量中配置 HTTPS 代理：
```bash
# 在Linux/Unix和macOS中执行如下类似命令配置环境变量
export https_proxy=https://192.168.1.1:1111
export https_proxy=https://myproxy.com:1111
# 在Windows的终端中执行如下类似命令配置环境变量
setx http_proxy=https://192.168.1.1:1111
set  http_proxy=https://myproxy.com:1111
# setx表示设置永久环境变量，设置后重启终端生效
```
 - 在命令行中使用 `--https-proxy` 选项设置 HTTPS 代理：
```bash
# 例如
tccli cvm DescribeRegions --https-proxy https://192.168.1.1:1111
```

## 使用 TCCLI

### [基础功能](id:primaryfunction)
TCCLI 支持自主配置，helper 信息支持中文信息且支持 JSON、table 及 text 输出格式。
>! 请注意示例中非简单类型的参数必须为标准 JSON 格式。 
>
TCCLI 目前支持以下三种调用方式：
* JSON 字符串入参调用
* JSON 文件入参调用 --cli-input-json
* 复杂类型点（.）连接展开形式入参调用 --cli-unfold-argument

#### JSON 字符串入参调用示例
- 执行以下命令，创建一台 CVM。
```bash
$ tccli cvm RunInstances --InstanceChargeType POSTPAID_BY_HOUR --InstanceChargePrepaid '{"Period":1,"RenewFlag":"DISABLE_NOTIFY_AND_MANUAL_RENEW"}' --Placement '{"Zone":"ap-guangzhou-2"}' --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}' --InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' --InstanceCount 1 --InstanceName TCCLI-TEST --LoginSettings '{"Password":"isd@cloud"}' --SecurityGroupIds '["sg-0rszg2vb"]' --HostName TCCLI-HOST-NAME1
```
- 执行以下命令，获取 CVM 的监控数据。
```bash
[root@VM_33_50_centos ~]# tccli monitor GetMonitorData --Namespace "QCE/CVM" --Period 300 --MetricName "CPUUsage" --Instances '[{"Dimensions":[{"Name":"InstanceId","Value":"ins-cac6a4w8"}]}]'
```

#### JSON 文件入参调用（--cli-input-json）示例
1. 执行以下命令，输出入参数据结构到 JSON 文件。
```bash
[root@VM_33_50_centos ~]# tccli cvm RunInstances  --generate-cli-skeleton > /tmp/RunInstances.json
```
2. 将文件中参数值替换为实际使用值，并使用该 JSON 文件作为入参，格式为 `--cli-input-json` 后接 `file://+文件路径`。示例如下：
```bash
[root@VM_33_50_centos ~]# tccli cvm RunInstances --cli-input-json file:///tmp/RunInstances.json
{
        "RequestId": "20e2b42d-3260-4750-9293-79116208330e", 
        "InstanceIdSet": null
}
```

#### 复杂类型点（.）连接展开形式入参调用（--cli-unfold-argument）示例
复杂类型点连接展开调用是将复杂类型按用点连接的形式展开，此方式可充分利用命令行自动补全机制来解决入参较复杂时的命令行输入困难，且易出错问题。展开方式如下：
复杂类型 `{"a":{"b": "c"}}` 展开为 `--a.b c`。复杂类型数组使用`.0`，` .1`表示数组的第一个、第二个元素。基本类型数组不需要使用`.0`，`.1`，直接将数组多个元素用空格隔开依次输入，例如 `--Integer 10 20`，`--String str1 str2`。

执行以下命令，创建一台 CVM。
```bash
[root@VM_33_50_centos ~]# tccli cvm RunInstances --cli-unfold-argument --InstanceChargeType POSTPAID_BY_HOUR --InstanceChargePrepaid.Period 1 --InstanceChargePrepaid.RenewFlag DISABLE_NOTIFY_AND_MANUAL_RENEW --Placement.Zone ap-guangzhou-2 --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk.DiskType CLOUD_BASIC --SystemDisk.DiskSize 50 --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR --InternetAccessible.InternetMaxBandwidthOut 10 --InternetAccessible.PublicIpAssigned True --InstanceCount 1 --InstanceName TCCLI-TEST --LoginSettings.Password isd@cloud --SecurityGroupIds sg-0rszg2vb --HostName TCCLI-HOST-NAME1
```


#### 更多使用示例
您还可通过以下命令，进一步使用 TCCLI。
- 执行 `tccli help` 命令，查看支持的产品，支持中文。
```bash
[root@VM_33_50_centos ~]# tccli help
NAME
    tccli
DESCRIPTION
    tccli (Tencent Cloud Command Line Interface) is a tool to manage your Tencent Cloud services.
CONFIGURE
    Before using tccli, you should use the command(tccli configure) to configure your profile as the default For more in
    formation, please enter tccli configure help
USEAGE
    tccli [options] <service> [options] <action> [options] [options and parameters]
OPTIONS
    help
    show the tccli help info
    --version
    show the version of tccli
AVAILABLE SERVICES
    af
    介绍如何使用API对借贷反欺诈进行操作，包括借贷反欺诈等。
    afc
    介绍如何使用API对定制建模进行操作，包括定制建模等。
    ame
    介绍如何使用API对正版曲库直通车进行操作，包括素材获取、数据上报等。
    ......
```
- 本文以 CVM 为例，执行 `tccli cvm help` 命令，查看产品支持的接口。
```bash
[root@VM_33_50_centos ~]# tccli cvm help
NAME
    cvm
AVAILABLE VERSIONS
    2017-03-12
    默认只展示最新版本信息，查看其它版本帮助信息加 --version xxxx-xx-xx
DESCRIPTION
    cvm-2017-03-12
    介绍如何使用API对云服务器进行操作，包括使用并管理实例、镜像、密钥等资源。
USEAGE
    tccli cvm <action> [--param...]
OPTIONS
    help
    show the tccli cvm help info
AVAILABLE ACTIONS
    AllocateHosts
    创建CDH实例
    AssociateInstancesKeyPairs
    绑定密钥对
    AssociateSecurityGroups
    绑定安全组
    ......
```
- 本文以 CBS 的 DescribeDisks 接口为例，执行 `tccli cbs DescribeDisks help` 命令，查看接口支持的参数。
```bash
[root@VM_33_50_centos ~]# tccli cbs DescribeDisks help
NAME
    DescribeDisks
DESCRIPTION
    cbs-2017-03-12-DescribeDisks
    本接口（DescribeDisks）用于查询云硬盘列表。
    * 可以根据云硬盘ID、云硬盘类型或者云硬盘状态等信息来查询云硬盘的详细信息，不同条件之间为与(AND)的关系，过滤信息详细请
    见过滤器`Filter`。
    * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的云硬盘列表。
USEAGE
    tccli cbs DescribeDisks [--param...]
OPTIONS
    help
    show the tccli cbs DescribeDisks help info
    --region
    identify the region to which the instance you want to work with belongs.
    --timeout
    specify a request timeout
    --secretKey
    specify a SecretKey
    ......  
AVAILABLE PARAMS
    --Limit (Integer | Optional)
    返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
    --OrderField (String | Optional)
    云盘列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据云盘的创建时间排序<br><li>DEADLINE：依据云盘的到期时间排序
    <br>默认按云盘创建时间排序。
    --Offset (Integer | Optional)
    偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
    ......
```
- 输出格式支持 JSON、table 及 text 格式。
  - **JSON 格式**：
```bash
[root@VM_33_50_centos ~]# tccli cvm DescribeRegions 
{
    "TotalCount": 20, 
    "RegionSet": [
        {
            "RegionState": "AVAILABLE", 
            "Region": "ap-beijing", 
            "RegionName": "华北地区(北京)"
        }, 
        {
            "RegionState": "AVAILABLE", 
            "Region": "ap-chengdu", 
            "RegionName": "西南地区(成都)"
        },
        {
            "RegionState": "AVAILABLE", 
            "Region": "ap-guangzhou", 
            "RegionName": "华南地区(广州)"
        }, 
        {
            "RegionState": "AVAILABLE", 
            "Region": "ap-hongkong", 
            "RegionName": "港澳台地区(中国香港)"
        },  
        {
            "RegionState": "AVAILABLE", 
            "Region": "ap-singapore", 
            "RegionName": "东南亚地区(新加坡)"
        }, 
        {
            "RegionState": "AVAILABLE", 
            "Region": "ap-tokyo", 
            "RegionName": "亚太地区(东京)"
        }, 
        {
            "RegionState": "AVAILABLE", 
            "Region": "eu-frankfurt", 
            "RegionName": "欧洲地区(法兰克福)"
        }, 
        ......
    ], 
    "RequestId": "e5125cf1-****-****-****-316f18eed021"
}
```
 - **table 格式**：
```bash
[root@VM_33_50_centos ~]# tccli cvm DescribeRegions --output table
--
|                        action                        |
+---------------------------------------+--------------+
|               RequestId               | TotalCount   |
+---------------------------------------+--------------+
|  1af5f2a0-****-****-****-462f0271a69f |  20          |
+---------------------------------------+--------------+
||                      RegionSet                     ||
|+-------------------+----------------+---------------+|
||      Region       |  RegionName    |  RegionState  ||
|+-------------------+----------------+---------------+|
||  ap-bangkok       |  亚太地区(曼谷)      |  AVAILABLE    ||
||  ap-beijing       |  华北地区(北京)      |  AVAILABLE    ||
||  ap-chengdu       |  西南地区(成都)      |  AVAILABLE    ||
||  ap-chongqing     |  西南地区(重庆)      |  AVAILABLE    ||
||  ap-guangzhou     |  华南地区(广州)      |  AVAILABLE    ||
||  ap-guangzhou-open|  华南地区(广州Open)  |  AVAILABLE    ||
||  ap-hongkong      |  港澳台地区(中国香港)   |  AVAILABLE    ||
||  ap-mumbai        |  亚太地区(孟买)      |  AVAILABLE    ||
||  ap-nanjing       |  华东地区(南京)      |  AVAILABLE    ||
||  ap-seoul         |  亚太地区(首尔)      |  AVAILABLE    ||
||  ap-shanghai      |  华东地区(上海)      |  AVAILABLE    ||
||  ap-shanghai-fsi  |  华东地区(上海金融)    |  AVAILABLE    ||
||  ap-shenzhen-fsi  |  华南地区(深圳金融)    |  AVAILABLE    ||
||  ap-singapore     |  东南亚地区(新加坡)    |  AVAILABLE    ||
||  ap-tokyo         |  亚太地区(东京)      |  AVAILABLE    ||
||  eu-frankfurt     |  欧洲地区(法兰克福)    |  AVAILABLE    ||
||  eu-moscow        |  欧洲地区(莫斯科)     |  AVAILABLE    ||
||  na-ashburn       |  美国东部(弗吉尼亚)    |  AVAILABLE    ||
||  na-siliconvalley |  美国西部(硅谷)      |  AVAILABLE    ||
||  na-toronto       |  北美地区(多伦多)     |  AVAILABLE    ||
|+-------------------+----------------+---------------+|
```
 - **text 格式**：
```bash
[root@VM_33_50_centos ~]# tccli cvm DescribeRegions --output text
70bbd02f-****-****-****-afc5c34018ae    20
REGIONSET       ap-bangkok      亚太地区(曼谷)  AVAILABLE
REGIONSET       ap-beijing      华北地区(北京)  AVAILABLE
REGIONSET       ap-chengdu      西南地区(成都)  AVAILABLE
REGIONSET       ap-chongqing    西南地区(重庆)  AVAILABLE
REGIONSET       ap-guangzhou    华南地区(广州)  AVAILABLE
REGIONSET       ap-guangzhou-open       华南地区(广州Open)      AVAILABLE
REGIONSET       ap-hongkong     港澳台地区(中国香港)    AVAILABLE
REGIONSET       ap-mumbai       亚太地区(孟买)  AVAILABLE
REGIONSET       ap-nanjing      华东地区(南京)  AVAILABLE
REGIONSET       ap-seoul        亚太地区(首尔)  AVAILABLE
REGIONSET       ap-shanghai     华东地区(上海)  AVAILABLE
REGIONSET       ap-shanghai-fsi 华东地区(上海金融)      AVAILABLE
REGIONSET       ap-shenzhen-fsi 华南地区(深圳金融)      AVAILABLE
REGIONSET       ap-singapore    东南亚地区(新加坡)      AVAILABLE
REGIONSET       ap-tokyo        亚太地区(东京)  AVAILABLE
REGIONSET       eu-frankfurt    欧洲地区(法兰克福)      AVAILABLE
REGIONSET       eu-moscow       欧洲地区(莫斯科)        AVAILABLE
REGIONSET       na-ashburn      美国东部(弗吉尼亚)      AVAILABLE
REGIONSET       na-siliconvalley        美国西部(硅谷)  AVAILABLE
REGIONSET       na-toronto      北美地区(多伦多)        AVAILABLE
```

### [高级功能](id:sophisticatedfunctions)
该步骤以 CVM 为例，详细介绍了如何使用 TCCLI 高级功能，包括多版本接口访问、指定最近的接入点、返回结果过滤、输出入参数据结构到 JSON 文件以及从 JSON 文件读取参数等。

#### 多版本接口访问
某些产品可能存在多个版本的接口，TCCLI 默认访问最新版本的接口。如果您想访问特定旧版本的接口，可以通过以下方式实现：
- 方式1：设置 CVM 产品默认使用版本为 2017-03-12。
```bash
tccli configure set cvm.version 2017-03-12
```
- 方式2：在实时使用时指定版本号。
```
tccli cvm help --version 2017-03-12
tccli cvm DescribeZones help --version 2017-03-12
tccli cvm DescribeZones --version 2017-03-12
```

#### 指定最近的接入点（Endpoint）
TCCLI 默认会请求就近的接口点访问服务，您也可以针对某一产品指定自己的 Endpoint。
- 设置 CVM 产品默认 Endpoint 为 ap-guangzhou。
```bash
tccli configure set cvm.endpoint cvm.ap-guangzhou.tencentcloudapi.com
```
- 调用时实时指定
```
tccli cvm DescribeZones --endpoint cvm.ap-guangzhou.tencentcloudapi.com
```

#### 返回结果过滤
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
    "RequestId": "4fd313a6-****-****-****-898c02fcae02"
   }
```
- 仅查看某个字段。
```bash
[root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter TotalCount
4
```
- 指定某个数组类型对象的第 N 个子对象的信息。
```bash
 [root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter ZoneSet[0]
 {
	"ZoneState": "AVAILABLE",
	"ZoneId": "100001",
	"Zone": "ap-guangzhou-1",
	"ZoneName": "广州一区"
 }
```
- 指定数组类型对象下所有某个名称的子对象的某个字段。
```bash
   [root@VM_180_248_centos ~]# tccli cvm DescribeZones  --filter ZoneSet[*].ZoneName
   [
    "广州一区",
    "广州二区",
    "广州三区",
    "广州四区"
   ]
```
- 过滤数组里的子对象，同时还以新的名称展示。 
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

#### 结果轮询
在使用产品的过程中，有些操作并不能即时完成，您可以使用结果轮询功能来不断查询操作是否完成。例如，在开启一台实例后，实例并不能立即进入 `RUNNING` 状态，则可使用结果轮询功能对实例状态轮询，直到出现 `RUNNING` 状态为止。
- 执行以下命令，程序将按照一定时间间隔对实例的状态进行轮询，直到实例的状态为 `RUNNING` 或者超时为止。
```bash
tccli cvm DescribeInstancesStatus --region ap-hongkong --waiter "{'expr':'InstanceStatusSet[0].InstanceState','to':'RUNNING'}"
```
- 您可自定义超时时间和睡眠时间，执行以下命令，设定超时时间为180秒，睡眠时间为5秒。
```bash
tccli cvm DescribeInstancesStatus --region ap-hongkong --waiter "{'expr':'InstanceStatusSet[0].InstanceState','to':'RUNNING','timeout':180,'interval':5}"
```
- 您可在配置文件中设置可选子参数的值。在 `default.configure` 文件中添加如下参数，设置系统超时时间为180s，睡眠时间为5s。
```
"waiter": {
		"interval": 5,
		"timeout": 180
	},
```
参数说明如下：
 - **--region**：需替换为您实例所在的地域。
 - **--waiter**：后的参数需使用双引号包裹，且参数需为 JSON 格式。其中必选及可选参数如下表：
 <table>
 <tr>
 <th>参数</th> <th>是否必选</th> <th>说明</th>
 </tr>
 <tr>
	<td>expr</td>
	<td>是</td>
	<td>指定被查询的字段，请使用 <a href="http://jmespath.org/">jmespath</a> 查找被指定的字段的值。</td>
 </tr>
 <tr>
	<td>to</td>
	<td>是</td>
	<td>被轮询的字段的目标值。</td>
 </tr>
 <tr>
	<td>timeout</td>
	<td>否</td>
	<td>轮询的超时时间，单位：秒。</td>
 </tr>
 <tr>
	<td>inaterval</td>
	<td>否</td>
	<td>进程睡眠的时间，单位：秒。</td>
 </tr>
 </table>


## 相关问题

#### 如何购买命令行工具？

本服务免费。当您遇到问题时，请 [联系我们](https://cloud.tencent.com/act/event/connect-service) 寻求相应的帮助。

#### 如何实现接口鉴权？
在 API 支持的每个产品文档目录下，可选择**调用方法** > **接口鉴权**，结合产品的“接口鉴权”文档进行实现。例如，可前往 [CVM 接口鉴权](https://cloud.tencent.com/document/api/213/15693) 进行查看。

