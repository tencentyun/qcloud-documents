## 1. 接口描述

本接口（EmrCreateCluster）用于创建一个EMR集群

接口请求域名：<font style="color:red">emr.api.qcloud.com</font>

1）用户可以选择安装需要的大数据处理组件。
2）用户可以选择创建高可用集群和非高可用集群。安装的软件设置会因为是否集群高可用有所不同。
3) 高可用集群最小节点数为master节点2个，core节点3个，同时有3个默认的common节点用于部署zookeeper。非高可用集群最小节点数为1个master节点和2个core节点。
4）创建集群时可以设置是否集成COS（腾讯云对象存储服务）。集成cos可以通过hadoop-hdfs接口读写cos的数据文件。同时我们也将定时把安装的组件日常生成的日志文件归档存储到cos上。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为EmrCreateCluster。

| 参数名称 | 是否必选 | 类型 | 描述 |
| --------|---------|------|------|
| ProductId | 是 | uint | EMR版本ID|
| ZoneId | 是 | uint | 所在地域可用区ID |
| VpcId | 是 | string | 创建EMR集群所在的私有网络vpcId, vpc-xxxxx格式 |
| SubnetId | 是 | string | 创建EMR集群的所在的私有网络subnetId, subnet-xxxx格式 |
| SoftInfo.n | 是 | array string | 需要安装的软件包 |
| MasterNodes | 是 | uint | master节点个数 | 
| CoreNodes | 是 | uint | core节点个数 |
| TaskNodes | 否 | uint | task节点个数 |
| MasterSpec | 是 | string | master节点机器规格，参见[cvm实例配置](https://www.qcloud.com/document/product/213/2177)|
| MasterStorageType| 否 | uint | master节点存储类型，1：本地盘，2：云盘，3：SSD本地盘，默认1 |
| MasterRootSize | 否 | uint | 单位GB，master节点系统盘容量，默认20G |
| MasterMemory | 是 | uint | 单位MB, master节点内存容量 |
| MasterCpuCores | 是 | uint | master节点cpu核数 |
| MasterVolume | 是 | uint | 单位GB,master节点数据盘容量 |
| CoreSpec | 是 | string | core节点机器规格，参见[cvm实例配置](https://www.qcloud.com/document/product/213/2177)|
| CoreStorageType| 否 | uint | core节点存储类型，1：本地盘，2：云盘，3：SSD本地盘，默认1 |
| CoreRootSize | 否 | uint | 单位GB，core节点系统盘容量，默认20G |
| CoreMemory | 是 | uint | 单位MB, core节点内存容量 |
| CoreCpuCores | 是 | uint | core节点cpu核数 |
| CoreVolume | 是 | uint | 单位GB,core节点数据盘容量 |
| TaskSpec | 否 | string | 若TaskNodes不为0，该字段有效。task节点机器规格，参见[cvm实例配置](https://www.qcloud.com/document/product/213/2177)|
| TaskStorageType| 否 | uint | 若TaskNodes不为0，该字段有效。task节点存储类型，1：本地盘，2：云盘，3：SSD本地盘，默认1 |
| TaskRootSize | 否 | uint | 若TaskNodes不为0，该字段有效。单位GB，task节点系统盘容量，默认20G |
| TaskMemory | 否 | uint | 若TaskNodes不为0，该字段有效。单位MB, task节点内存容量 |
| TaskCpuCores | 否 | uint | 若TaskNodes不为0，该字段有效。task节点cpu核数 |
| TaskVolume | 否 | uint | 若TaskNodes不为0，该字段有效。单位GB,task节点数据盘容量 |
| Password | 是 | string | 初始密码，用于cvm,cdb的初始root密码 |
| VisitCos | 是 | uint | 是否集成cos。0：不集成,非0：集成 |
| LogOnCosPath | 否 | string | 集成cos后，存储软件运行日志的cos路径地址|
| CosSecretId | 否 | string | 访问cos的SecretId,参见[COS基本概念-SecretId/SecretKey](https://www.qcloud.com/document/product/436/6225) |
| CosSecretKey | 否 | string | 访问cos的SecretKey,参见[COS基本概念-SecretId/SecretKey](https://www.qcloud.com/document/product/436/6225) |
| SupportHA | 是 | uint | 是否支持高可用 |

## 3.输出参数

| 参数名称 | 类型 | 描述 |

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data.clusterId | string | 集群ID，emr-xxxx格式 |

## 4.示例

在广州二区创建一个非高可用的集群,1一个master节点，2个core节点，master节点S1型4核16G，50G数据盘，core节点I1型4核16G，50G数据盘，task节点I1型4核16G，数据盘为空，emr版本1,安装hadoop-2.7.3,不集成cos

<pre>
  https://emr.api.qcloud.com/index.php?Action=EmrCreateCluster
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
  &ZoneId=100002
  &SoftInfo.0=hadoop-2.7.3
  &VpcId=vpc-lgfidqdd
  &SubnetId=subnet-i5xrg93s
  &ProductId=1
  &MasterNodes=1
  &CoreNodes=2
  &TaskNodes=0
  &MasterSpec=CVM.S1
  &MasterMemory=16384
  &MasterCpuCores=4
  &MasterVolume=50
  &CoreSpec=CVM.I1
  &CoreStorageType=3
  &CoreRootSize=20
  &CoreMemory=16384
  &CoreCpuCores=4
  &CoreVolume=50
  &TaskSpec=CVM.I1
  &TaskMemory=16384
  &TaskCpuCores=4
  &TaskVolume=0
  &VisitCos=0
  &Password=emrpassword
  &SupportHA=0
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "clusterId": "emr-rowyenms"
    }
}
```
