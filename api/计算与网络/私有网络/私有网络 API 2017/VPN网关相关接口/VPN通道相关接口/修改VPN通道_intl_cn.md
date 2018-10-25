## 1. 接口描述

本接口(ModifyVpnConnEx)用于修改VPN通道。
接口请求域名：<font style="color:red">vpc.api.qcloud.com</font>
 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为ModifyVpnConnEx。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | string | 私有网络ID，可使用vpcId或unVpcId，建议使用unVpcId，例如：vpc-03vihbk9,可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询。 | 
| vpnGwId | 是 | String | 系统分配的VPN网关ID，可使用vpnGwId或unVpnGwId，建议unVpnGwId，例如：vpngw-dystbrkv。可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2VPN%E7%BD%91%E5%85%B3%E5%88%97%E8%A1%A8" title="DescribeVpnGw">DescribeVpnGw</a>接口查询。 |
| vpnConnId | 是 | String | 系统分配的VPN通道ID，可使用vpnConnId或unVpnConnId，建议使用unVpnConnId，例如：vpnx-ol6bcqp0。可通过<a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn">DescribeVpnConn</a>接口查询。 | 
| vpnConnName | 否 | String | 通道名称，可任意命名，但不得超过60个字符。 |
| preSharedKey | 否 | String | 预共享密钥。 |
| userGwCidrBlock.n | 否 | Array | 对端网段CIDR地址，可写多个，指定vpc可以和哪些IDC网段通信，后面升级为spdAcl（粒度更细），userGwCidrBlock和spdAcl必须填一项。 |
| spdAcl.n | 否 | Array | SPD策略组，用户指定VPC内哪些网段可以和您IDC中哪些网段通信，由userGwCidrBlock升级而来，userGwCidrBlock和spdAcl必须填一项，更多详见产品说明文档。 |
| IKESet.n | 否 | Array | IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自保护机制，用户配置网络安全协议，详见<a href="https://cloud.tencent.com/doc/product/215/VPN%e8%bf%9e%e6%8e%a5#4.3-ike.E9.85.8D.E7.BD.AE" title="VPN连接-IKE配置">VPN连接-IKE配置</a>。 |
| IPsecSet.n | 否 | Array | IPSec配置，腾讯云提供IPSec安全会话设置，详见<a href="https://cloud.tencent.com/document/product/215/4956#ipsec-.E4.BF.A1.E6.81.AF" title="VPN连接-IPSec配置">VPN连接-IPSec配置</a>。|

IKE配置详情

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| IKESet.propoEncryAlgorithm | 否 | String | IKE配置，加密算法，可选值：'3des-cbc','aes-cbc-128','aes-cbc-192','aes-cbc-256','des-cbc'，默认为3des-cbc，更多详见产品说明文档。 |
| IKESet.propoAuthenAlgorithm | 否 | String | IKE配置，认证算法：可选值：'md5','sha'，默认为md5，更多详见产品说明文档。 |
| IKESet.exchangeMode | 否 | String | IKE配置，协商模式：可选值：'aggressive','main'，默认为main，更多详见产品说明文档。 |
| IKESet.localIdentity | 否 | String | IKE配置，本端标识类型：可选值：'address','fqdn'，默认为address，更多详见产品说明文档。 |
| IKESet.remoteIdentity | 否 | String | IKE配置，对端标识类型：可选值：'address','fqdn'，默认为address，更多详见产品说明文档。 |
| IKESet.localAddress | 否 | String | IKE配置，本端标识，当localIdentity选为address时，localAddress必填。localAddress默认为vpn网关公网IP，更多详见产品说明文档。 |
| IKESet.remoteAddress | 否 | String | IKE配置，对端标识，当remoteIdentity选为address时，remoteAddress必填，更多详见产品说明文档。 |
| IKESet.localFqdnName | 否 | String | IKE配置，本端标识，当localIdentity选为fqdn时，localFqdnName必填，更多详见产品说明文档。 |
| IKESet.remoteFqdnName | 否 | String | IKE配置，对端标识，当remoteIdentity选为fqdn时，remoteFqdnName必填，更多详见产品说明文档。 |
| IKESet.dhGroupName | 否 | String | IKE配置，DH group，指定IKE交换密钥时使用的DH组，可选值：'group1','group2','group5','group14','group24'，更多详见产品说明文档。 |
| IKESet.ikeSaLifetimeSeconds | 否 | Int | IKE配置，IKE SA Lifetime，单位：秒，设置IKE SA的生存周期，取值范围：60-604800，更多详见产品说明文档。 |
| IKESet.encryptAlgorithm | 否 | String | IPsec配置，加密算法，取值：'3des-cbc','aes-cbc-128','aes-cbc-192','aes-cbc-256','des-cbc','null'，默认为3des-cbc，更多详见产品说明文档。 |


IPsec配置详情

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| IPsecSet.integrityAlgorith | 否 | String | IPsec配置，认证算法：可选值：'md5','sha'，默认为md5，更多详见产品说明文档。 |
| IPsecSet.ipsecSaLifetimeSeconds | 否 | Int | IPsec配置，IPsec SA lifetime(s)：单位秒，取值范围：180-604800，更多详见产品说明文档。 |
| IPsecSet.ipsecSaLifetimeTraffic | 否 | Int | IPsec配置，IPsec SA lifetime(KB)：单位KB，取值范围：2560-604800，更多详见产品说明文档。 |
| IPsecSet.pfsDhGroup | 否 | String | IPsec配置，PFS：可选值：'null','dh-group1','dh-group14','dh-group2','dh-group24','dh-group5'，默认为null，更多详见产品说明文档。 |

## 3. 输出参数
 
| 参数名称 | 类型 | 描述|
|---------|---------|---------|
| code| Int | 错误码，0：成功，其他值：失败 |
| message |  String | 错误信息 |
| data.taskId | Int  | 任务ID，操作结果可以用taskId查询，详见<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2%e4%bb%bb%e5%8a%a1%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c%e6%8e%a5%e5%8f%a3">查询任务执行结果接口</a>。 |

 ## 4. 错误码表
 以下错误码表仅列出了该接口的业务逻辑错误码，更多公共错误码详见<a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC错误码">VPC错误码</a>。

| 错误码 | 描述 |
|---------|---------|
| InvalidVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a>接口查询VPC。 |
| InvalidVpnGw.NotFound | 无效的vpn网关。vpn网关资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/doc/api/245/%e6%9f%a5%e8%af%a2VPN%e7%bd%91%e5%85%b3%e5%88%97%e8%a1%a8?viewType=preview" title="DescribeVpnGw">DescribeVpnGw</a>接口查询vpn网关。 |
| InvalidVpnGw.NotFound | 无效的vpn通道。vpn通道资源不存在，请再次核实您输入的资源信息是否正确，可通过<a href="https://cloud.tencent.com/document/product/215/5113" title="DescribeVpnConn">DescribeVpnConn</a>接口查询vpn通道。 |
 

## 5. 示例
 
输入
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=ModifyVpnConnEx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &vpcId=vpc-03vihbk9
  &vpnGwId=vpngw-kfldykuz
  &vpnConnId=vpnx-ol6bcqp0
  &userGwCidrBlock.0=10.100.2.0/24
  &preSharedKey=tencenttest

</pre>

输出
```

{
    "code": 0,
    "message": "",
    "data": {
        "vpnGwId": "vpngw-kfldykuz",
        "vpcConnId": "vpnx-ol6bcqp0",
        "taskId": 12614,
        "vpcConnStatus": 2,
        "preSharedKey": "tencenttest",
        "userGwSubnetList": [
            "10.100.2.0\/24"
        ],
        "userGwId": 315
    }
}

```

