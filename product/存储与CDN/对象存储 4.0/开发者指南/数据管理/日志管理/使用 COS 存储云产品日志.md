## 简介

使用腾讯云产品时会产生大量日志，这些日志记录了您的业务情况，有助于您分析业务情况，为您的业务发展和决策提供辅助。您可以利用 COS 的存储能力持久化存储云产品日志，同时您可以通过 API、SDK 或者工具等方式，方便快捷地从 COS 上获取日志并进行分析。

使用 COS 存储云产品日志，可以帮您解决以下问题：

- **持久存储**：COS 提供稳定持久的存储服务，您可以以极低的成本将您的日志存放到 COS 实现持久化存储。当您的业务需要基于日志进行分析或者决策时，您可以通过 COS 随时随地获取任意时间段的日志。
- **数据检索**：COS 提供 Select 功能，您可以使用该功能对存储在 COS 上的日志进行简单的检索和抽取工作。您能够结合日志的字段，帮助您检索所需的信息，减少数据下载流量。
- **数据分析**：您可以使用 Sparkling 产品对存储在 COS 上的日志进行分析，您可以选择一个或者多个日志文件，利用 Sparkling 分析日志，根据分析结果进行决策。

## 日志投递方式

您可以通过两种方式将腾讯云产品的日志存储在 COS 上：

- 使用云产品自带的日志投递功能：例如对象存储 COS、云审计 CA 等产品，可直接将日志投递到 COS。
- 使用日志服务 CLS 的投递功能：将投递到 CLS 的云产品日志，通过 CLS 投递到 COS 上进行持久化存储。

目前腾讯云产品对这两种方式的支持情况如下：

| 云产品名称          | 是否支持直接投递到 COS | 是否支持投递到 CLS     |
| ------------------- | ---------------------- | ---------------------- |
| 云审计 CA           | 是                     | 否                     |
| 负载均衡 CLB        | 否                     | 是                     |
| 消息队列 CKafka     | 是                     | 否                     |
| API 网关 APIGateway | 否                     | 是                     |
| 云函数 SCF      | 否                     | 是                     |
| 容器服务 TKE        | 否                     | 是                     |
| 云直播 CSS          | 否                     | 是                     |
| 云开发 TCB          | 否                     | 是，但不支持通过 CLS 投递到 COS |
| 对象存储 COS        | 是                     |  支持申请开通白名单，请您加入 [技术支持微信群](https://cloud.tencent.com/document/product/436/37708#.E6.8A.80.E6.9C.AF.E6.94.AF.E6.8C.81) 联系我们开通白名单       |

### 直接投递日志到 COS

以下腾讯云产品拥有直接投递日志到 COS 的能力，您可以按照对应的产品文档指引，配置日志投递规则，将日志投递到 COS 。

| 云产品名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      | 日志投递文档                                                 | 日志投递间隔&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        | 日志投递路径                                                 |
| --------------- | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ |
|云审计 CA |[点此查阅](https://cloud.tencent.com/document/product/629/11985) | 10-15分钟 |  cloudaudit/customprefix/timestamp|
| 消息队列 CKafka | [点此查阅](https://cloud.tencent.com/document/product/597/17273) | 5分钟 - 60分钟<br>可指定投递间隔 | instance id/topic id/timestamp                           |
| 对象存储 COS    | [点此查阅](https://cloud.tencent.com/document/product/436/17040) | 5分钟                | 路径前缀可自行指定，推荐设置可识别的路径，例如 cos_bucketname_access_log/timestamp |

>?消息队列支持投递该产品上产生的消息数据，如果您需要获取创建 CKafka 实例等行为日志，可以选择投递云审计产品的日志。

### 通过日志服务（CLS）投递日志到 COS

以下腾讯云产品支持投递日志到日志服务 CLS 中，以便用户进行检索分析。日志服务同时提供了投递到 COS 的产品能力，方便用户持久化存储日志。对于支持投递日志到 CLS 的产品，您也可以通过在 CLS 处开启投递日志到 COS 的方式，将数据持久化存储以降低您的存储成本，方便进一步离线分析。当前支持直接投递日志到 CLS 的产品如下：

| 云产品名称           | 日志投递文档                                                 |
| -------------------- | ------------------------------------------------------------ |
| API 网关 API Gateway | [点此查阅](https://cloud.tencent.com/document/product/628/19552) |                               
| 容器服务 TKE         | [点此查阅](https://cloud.tencent.com/document/product/457/13659) |
| 云直播 LVB           | [点此查阅](https://cloud.tencent.com/document/product/267/33996) |

CLS 投递到 COS 支持如下三种方式投递：

- 通过分隔符格式投递：可以将数据按照分隔符格式投递到 COS，详情请参见 [分隔符格式投递](https://cloud.tencent.com/document/product/614/33814)。
- 通过 JSON 格式投递：可以将数据按照 JSON 格式投递到 COS，详情请参见 [JSON 格式投递](https://cloud.tencent.com/document/product/614/33815)。
- 通过原文格式投递：可以将数据按照原文格式进行投递，支持单行全文、多行全文投递，部分支持 CSV 格式投递，详情请参见 [原文格式投递](https://cloud.tencent.com/document/product/614/33816)。

通过 CLS 投递日志到 COS，您需要执行的操作如下：

1. 根据您业务需要选择对应的产品，按照上述提供的产品日志投递文档链接指引，配置日志集和日志主题，将您业务产生的数据对接到 CLS 中。
2. 此后，根据您业务需要，选择合适的格式将数据投递到 COS 上。在将日志投递到 COS 时，我们建议您按照产品名称作为路径前缀以作为不同产品日志的区分。例如 TKE 的日志，您可以命名为`TKE_tkeid_log/timestamp`。
3. 配置好投递规则后，您还可以额外在 SCF 产品下配置文件上传的事件通知，当日志数据投递到 COS 后，您可以根据事件通知执行下一步操作，详情请参见 [事件通知](https://cloud.tencent.com/document/product/436/35526)。

## 对日志进行分析

### 下载日志到本地进行离线分析

如果您需要下载日志数据到本地，可以通过控制台、SDK、API 或者工具等多种方式进行下载，以下为各下载方式的使用文档说明，您可以参照下述文档，将代码中涉及到文件路径的部分替换为您日志存储路径，即可下载日志数据到本地：

| 下载方式       | 使用说明                                                     |
| -------------- | ------------------------------------------------------------ |
| 控制台         | [点此查阅](https://cloud.tencent.com/document/product/436/13322) |
| cosbrowser     | [点此查阅](https://cloud.tencent.com/document/product/436/38103#download ) |
| coscmd         | [点此查阅](https://cloud.tencent.com/document/product/436/10976#.E4.B8.8B.E8.BD.BD.E6.96.87.E4.BB.B6.E6.88.96.E6.96.87.E4.BB.B6.E5.A4.B9 ) |
| Android SDK    | [点此查阅](https://cloud.tencent.com/document/product/436/46416) |
| C SDK          | [点此查阅](https://cloud.tencent.com/document/product/436/35558#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| C++ SDK        | [点此查阅](https://cloud.tencent.com/document/product/436/35161#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| .NET SDK       | [点此查阅](https://cloud.tencent.com/document/product/436/32819#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| Go SDK         | [点此查阅](https://cloud.tencent.com/document/product/436/35057#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| iOS SDK        | [点此查阅](https://cloud.tencent.com/document/product/436/46382) |
| Java SDK       | [点此查阅](https://cloud.tencent.com/document/product/436/35215#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| JavaScript SDK | [点此查阅](https://cloud.tencent.com/document/product/436/35649#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| Node.js SDK    | [点此查阅]( https://cloud.tencent.com/document/product/436/36119#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1) |
| PHP SDK        | [点此查阅](https://cloud.tencent.com/document/product/436/34282#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| Python SDK     | [点此查阅](https://cloud.tencent.com/document/product/436/35151 ) |
| 小程序 SDK     | [点此查阅](https://cloud.tencent.com/document/product/436/36160#.E4.B8.8B.E8.BD.BD.E5.AF.B9.E8.B1.A1 ) |
| API            | [点此查阅](https://cloud.tencent.com/document/product/436/7753 ) |

### 使用 COS Select 对日志进行分析

您也可以通过 COS Select 功能直接检索和分析存储在 COS 上的日志文件，前提是日志文件以 CSV 或者 JSON 格式存储。通过 COS Select 功能，您可以筛选出您所需要的日志字段，这将很大程度降低 COS 传输的日志数据量，以减小您的使用成本，同时提高您的数据获取效率。如需详细了解 COS Select 功能，请参见 [Select 概述](https://cloud.tencent.com/document/product/436/37635)。

目前您可以通过控制台或者 API 的方式使用 COS Select 功能：

| 使用方式 | 使用说明                                                     |
| -------- | ------------------------------------------------------------ |
| 控制台   | [点此查阅](https://cloud.tencent.com/document/product/436/37642) |
| API      | [点此查阅](https://cloud.tencent.com/document/product/436/37641) |


