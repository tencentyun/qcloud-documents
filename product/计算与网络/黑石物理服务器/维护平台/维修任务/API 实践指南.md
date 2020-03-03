## 概述
[维修任务](https://console.cloud.tencent.com/cpm/repairTask) 是用于管理物理机故障维修的基础功能，并同时提供了了控制台功能与[ API 功能](https://cloud.tencent.com/document/product/386/32920)。

>! 建议先阅读官网文档，了解维修过程中，各状态的设定含义。

状态生命周期图
![](https://main.qcloudimg.com/raw/633bbc27051fee577535b6718dc8e471.png)

## 维修操作流程图
![](https://main.qcloudimg.com/raw/9cb048decfd3514c456cc6e4922c4dbd.png)

>! 
> - 云监控告警回调功能，请参考 [回调接口](https://cloud.tencent.com/document/product/248/9066)。
> - 云监控告警回调功能，可在 [告警策略](https://console.cloud.tencent.com/monitor/policylist) 中单击“策略名称”进入“管理告警策略”页面底部可进行配置。
> 

![](https://main.qcloudimg.com/raw/0ec1e345a75fa62bd40eaaf33a24e05c.png)

## 代码编写辅助工具
[API Explore](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度，推荐使用此工具辅助 API 相关功能接入，相关信息可参考 [说明文档](https://cloud.tencent.com/document/sdk/PHP)。


## 代码编写集合与示例
### 1.发现故障
使用接口：[维修任务信息获取](https://cloud.tencent.com/document/product/386/32919)   

#### 生成代码
![](https://main.qcloudimg.com/raw/cf95eb9d1a9ed551a7ca599658bf97c1.png)

#### 返回结果
![](https://main.qcloudimg.com/raw/309a74ec807e4428dd88f08b4f4519ff.png)

### 2.授权维修
使用接口：[维修任务管理](https://cloud.tencent.com/document/product/386/32916)

#### 代码生成
![](https://main.qcloudimg.com/raw/3e68dfa06831dd93ab45180831600c26.png)

>! 通过指定 TaskId，对指定任务进行授权。
>

### 3.查询状态
使用接口：[维修任务信息获取](https://cloud.tencent.com/document/product/386/32919)
请参考“发现故障”中的“DescribeTaskInfo”接口，查询任务状态。

### 4.确认恢复
使用接口：[维修任务管理](https://cloud.tencent.com/document/product/386/32916)
请参考“授权维修”中的“RepairTaskControl”接口，确认服务器已恢复。

#### 操作类别
- 服务器恢复正常：入参“Operate”指定为“ConfirmRecovered”，提交。
- 服务器存在异常：入参“Operate”指定为“ConfirmUnRecovered”，提交，并联系售后，说明异常现象，由腾讯云侧进行协查。






		

