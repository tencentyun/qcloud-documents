## 1. API Description
 
This API (CreateCluster) is used to create a cluster.

Domain for API request: ccs.api.qcloud.com

* When creating a cluster, you need to specify the number and configuration of nodes (CVMs) in the cluster.
* All the nodes in the cluster are HDD cloud disks.
* Up to 5 clusters can be created per region by default. You can [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=350&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1CCS) to raise your quota.
* Up to 20 nodes are allowed per cluster by default. You can [submit a ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=350&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E5%AE%B9%E5%99%A8%E6%9C%8D%E5%8A%A1CCS) to raise your quota. The quota of nodes is also subject to [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/doc/product/213/CVM%E5%AE%9E%E4%BE%8B%E8%B4%AD%E4%B9%B0%E9%99%90%E5%88%B6).
* **Limitations on the ratio** of CPU to memory can be found [here](https://cloud.tencent.com/doc/product/213/CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE).
* If you need to change the bandwidth, change it using the API [UpdateInstanceBandwidthHour](https://cloud.tencent.com/doc/api/229/1345). The bandwidth of public network is 0 by default if not specified</font>.
* Supported instance types **(the types of CVMs purchased in each availability zone are different)** can be found [here](https://cloud.tencent.com/doc/product/213/CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE):

| CVM Type | Series 1 | Series 2 |
|---------|---------|---------|
| Standard | CVM.S1 | CVM.S2 |
| High IO | CVM.I1 | CVM.I2 |
| Standard | CVM.M1 | CVM.M2 |
| Computational | - | CVM.C2 |

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/457/9463).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| clusterName | Yes | String | Cluster name |
| clusterDesc | No | String | Cluster description |
| clusterCIDR | Yes | String | CIDR used to assign cluster container and service IP. It cannot be in conflict with VPC CIDR nor CIDR of other clusters in the same VPC |
| ignoreClusterCIDRConflict | No | Int | Whether to ignore the clusterCIDR conflict error, 1: Ignore the conflict (and continue with creation); 0: Do not ignore the conflict (and return error). Default is 1 |
| zoneId | Yes | Int | [Availability Zone](https://cloud.tencent.com/document/api/213/1286) ID. |
| goodsNum | Yes | Int | Number of purchased instances. The maximum value is 100 |
| cpu | Yes | Int | The number of CPU cores, see above for specific limits.  |
| mem | Yes | Int | Memory size (GB), see above for specific limits.  |
| osName | Yes | String | System name (centos7.2x86_64 or ubuntu16.04.1 LTSx86_64). The system is used by all the nodes in the cluster, and also used during node scaling automatically. |
| instanceType | No | String | Instance type (e.g. High IO). Default is CVM.S1. For more instance types, see the "Instance types" section above. |
| cvmType | No | String | CVM type. <br>PayByHour: Postpaid (default)<br>PayByMonth: Prepaid<br><br> |
| bandwidthType | Yes | String | Bandwidth type. <br>CVM with Prepaid mode: PayByMonth: Bill-by-bandwidth usage period; PayByTraffic: Bill-by-traffic. <br> CVM with Postpaid mode: PayByHour: Bill-by-bandwidth usage period; PayByTraffic: Bill-by-traffic.<br>The difference between the network billing modes can be found in [Purchase Network Bandwidth](https://cloud.tencent.com/doc/product/213/509). |
| bandwidth | Yes | Int | Internet bandwidth (Mbps), or the peak Internet bandwidth when bandwidth type is "Bill-by-traffic". |
| wanIp | No | Int | Whether to enable the Internet IP. 1: Enable, 0: Not enable. If "bandwidth" is greater than 0, you're free to choose whether to enable the Internet IP ("Enable" by default). If "bandwidth" is 0, the Internet IP will not be assigned. |
| vpcId | Yes | String | VPC ID. Enter the unVpcId (unified VPC ID) field returned via API [Query VPC List](https://cloud.tencent.com/document/api/215/1372). |
| subnetId | Yes | String |  Subnet ID. Enter the unSubnetId (unified subnet ID ) field returned via API [Query Subnet List](https://cloud.tencent.com/document/api/215/1371).  |
| isVpcGateway | Yes | Int | Whether it is [Internet Gateway](https://cloud.tencent.com/doc/product/215/3089#3.-.E5.90.91.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.AD.E6.B7.BB.E5.8A.A0.E5.85.AC.E7.BD.91.E7.BD.91.E5.85.B3.) or not. 0: Non-Internet gateway; 1: Internet gateway. The Internet gateway can be used only when the instance has an Internet IP and is in VPC. |
| rootSize | Yes | Int | System disk size (GB). <br>The adjustment range for Linux system is 20-50 GB, with an increment of 1. The default size is 20 GB. Adjustment is not supported for Windows. The default size is 50 GB. The type of system disk is the same as specified by storageType. |
| storageSize | Yes | Int | Data disk size (GB). The increment is 10. The value of 0 means that no data disk is needed. For the maximum size of different disks, please see API [Overview of Hard Disk Products](https://cloud.tencent.com/doc/product/213/498). |
| password | No | String | Instance password. It will be generated randomly if not set, and be sent via internal message. Linux instance's password should be a combination of 8-16 characters comprised of at least two of the following types: letters [a-z, A-Z], numbers [0-9], and special characters [( ) &#96; ~ ! @ # $ % ^ & * - + = &#124; { } [ ] : ; ' < > , . ? / ]. Windows instance's password should be a combination of 12-16 characters comprised of at least three of the following types: lowercase letters [a-z], uppercase letters [A-Z], numbers [0-9] and special characters [( ) &#96; ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. |
| keyId | No | String | [Key](https://cloud.tencent.com/doc/product/213/503) ID. You can use the key to log in to the instance after the key is associated. "keyId" can be obtained through API [Query Keys](http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%AF%86%E9%92%A5). Key and password cannot both be specified, and specifying key is not supported by Windows operating systems. |

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed. For more information, please see Common Error Codes on Error Codes page. |
| message | String | Module error message description depending on API. For more information, please see Module Error Codes on Error Codes page. |
| requestId | Int | Task ID |
| clusterId | Int | Cluster  ID |



 

## 4. Example
 
Input

```
  https://domain/v2/index.php?Action=CreateCluster
  &imageId=1
  &bandwidth=1
  &cpu=1
  &mem=2
  &storageType=1
  &storageSize=50
  &goodsNum=1
  &zoneId=1
  &vpcId=vpc-8e0ypm3z 
  &subnetId=subnet-3lzrkspo 
  &<Common request parameters>
```
Output

```
  {
      "code" : 0,
      "message" : "ok",
      "data":{
	      "clusterId":"cluster-xxxx",
	      "requestId":11333
      }
      
  }

```
