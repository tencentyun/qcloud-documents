## 接口描述

本接口（EmrCreateCluster）用于创建一个 EMR 集群。

接口请求域名：`emr.api.qcloud.com`

- 用户可以选择安装需要的大数据处理组件。
- 用户可以选择创建高可用集群和非高可用集群。安装的软件设置会因为是否集群高可用有所不同。
- 高可用集群最小节点数为 Master 节点2个，Core 节点3个，同时有3个默认的 Common 节点用于部署 zookeeper。非高可用集群最小节点数为1个 Master 节点和2个 Core 节点。
- 创建集群时可以设置是否集成 COS（腾讯云对象存储服务）。集成 COS 可以通过 hadoop-hdfs 接口读写 COS 的数据文件。同时我们也将定时把安装的组件日常生成的日志文件归档存储到 COS 上。

## 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的 Action 字段为 EmrCreateCluster。

| 参数名称 | 是否必选 | 类型 | 描述 |
| --------|---------|------|------|
| ProductId | 是 | Uint | EMR 版本 ID|
| ZoneId | 是 | Uint | 所在地域可用区 ID |
| VpcId | 是 | String | 创建 EMR 集群所在的私有网络 vpcId，vpc-xxxxx 格式 |
| SubnetId | 是 | String | 创建 EMR 集群的所在的私有网络 subnetId，subnet-xxxx 格式 |
| SoftInfo.n | 是 | Array String | 需要安装的软件包，至少包含 hadoop 和 zookeeper 组件 |
| MasterNodes | 是 | Uint |  Master 节点个数 | 
| CoreNodes | 是 | Uint | Core 节点个数 |
| TaskNodes | 否 | Uint | Task 节点个数 |
| MasterSpec | 是 | String |  Master 节点机器规格，参见 [CVM 实例配置](https://cloud.tencent.com/document/product/213/11518)|
| MasterStorageType| 否 | Uint |  Master 节点存储类型，1：本地盘，2：云盘，3：SSD 本地盘，默认1 |
| MasterRootSize | 否 | Uint | 单位 GB，Master 节点系统盘容量，默认20G |
| MasterMemory | 是 | Uint | 单位 MB，Master 节点内存容量 |
| MasterCpuCores | 是 | Uint |  Master 节点 CPU 核数 |
| MasterVolume | 是 | Uint | 单位 GB，Master 节点数据盘容量 |
| CoreSpec | 是 | String | Core 节点机器规格，参见 CVM 实例配置|
| CoreStorageType| 否 | Uint | Core 节点存储类型，1：本地盘，2：云盘，3：SSD本地盘，默认1 |
| CoreRootSize | 否 | Uint | 单位 GB，Core 节点系统盘容量，默认20G |
| CoreMemory | 是 | Uint | 单位 MB，Core 节点内存容量 |
| CoreCpuCores | 是 | Uint | Core 节点 CPU 核数 |
| CoreVolume | 是 | Uint | 单位 GB，Core 节点数据盘容量 |
| TaskSpec | 否 | String | 若 TaskNodes 不为0，该字段有效。Task 节点机器规格，参见 CVM 实例配置|
| TaskStorageType| 否 | Uint | 若 TaskNodes 不为0，该字段有效。Task 节点存储类型，1：本地盘，2：云盘，3：SSD本地盘，默认1 |
| TaskRootSize | 否 | Uint | 若 TaskNodes 不为0，该字段有效。单位 GB，Task 节点系统盘容量，默认20G |
| TaskMemory | 否 | Uint | 若 TaskNodes 不为0，该字段有效。单位 MB，Task 节点内存容量 |
| TaskCpuCores | 否 | Uint | 若 TaskNodes 不为0，该字段有效。Task 节点 CPU 核数 |
| TaskVolume | 否 | Uint | 若 TaskNodes 不为0，该字段有效。单位 GB，Task 节点数据盘容量 |
| Password | 是 | String | 初始密码，用于 CVM，TencentDB 的初始 root 密码。要求8 - 16个字符，且必须同时包含大写字母、小写字母、数字和特殊字符 !@#%^\* 中两种 |
| VisitCos | 是 | Uint | 是否集成 COS。0：不集成，非0：集成 |
| LogOnCosPath | 否 | String | 集成 COS 后，存储软件运行日志的 COS 路径地址|
| CosSecretId | 否 | String | 访问 COS 的 SecretId，参见 [COS 基本概念-SecretId/SecretKey](https://cloud.tencent.com/document/product/436/18507) |
| CosSecretKey | 否 | String | 访问 COS 的 SecretKey，参见 [COS 基本概念-SecretId/SecretKey](https://cloud.tencent.com/document/product/436/18507) |
| SupportHA | 是 | Uint | 是否支持高可用 |
| CvmCharge | 是 | Int | CVM 计费模式，0：按量计费，1：包年包月。如有 hive 等组件会自动申请 TencentDB，则 TencentDB 的计费方式和 CVM 一致。 |
| SgId | 否 | String | 外网 IP 的 CVM，安全组 ID，如果填写了安全组则使用已有安全组。如未填，则会新建一个安全组。不管使用已有还是新建安全组，入站规则仅会开放22和3001端口，如需更改可在 CVM 安全组修改，参见 [安全组](https://cloud.tencent.com/document/product/213/12452) |
| ProjectId | 否 | Uint | 项目 ID 可以在账户信息，项目管理中查看，不填则使用0（默认项目）|

## 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
| data.clusterId | String | 集群 ID，emr-xxxx 格式 |

## 示例

在广州二区创建一个非高可用的集群，1个 Master 节点，2个 Core 节点，Master 节点 S1 型4核16G，50G数据盘，Core 节点 I1 型4核16G，50G数据盘，Task 节点 I1 型4核16G，数据盘为空，EMR 版本1，安装 hadoop-2.7.3，不集成 COS。

输入：
<pre>
  https://emr.api.qcloud.com/index.php?Action=EmrCreateCluster
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &ZoneId=100002
  &SoftInfo.0=hadoop-2.7.3
  &SoftInfo.1=zookeeper-3.4.9
  &VpcId=vpc-lgfidqdd
  &SubnetId=subnet-i5xrg93s
  &ProductId=1
  &MasterNodes=1
  &CoreNodes=2
  &TaskNodes=0
  &MasterSpec=CVM.S2
  &MasterMemory=16384
  &MasterCpuCores=4
  &MasterVolume=50
  &CoreSpec=CVM.I2
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
  &Password=emrpassword@123
  &SupportHA=0
  &CvmCharge=0
</pre>

输出：
```
{
    "code": 0,
    "message": "",
    "data": {
        "clusterId": "emr-rowyenms"
    }
}
```
