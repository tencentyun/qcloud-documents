## 接口描述
### 功能描述
本接口（CreateCfsFileSystem）用于添加新文件系统。
### 接口域名
文件存储请求域名：`cfs.api.cloud.tencent.com`

## 请求参数
以下请求参数为本接口的请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/product/582/13227) 页面。

|       参数      |必填 |类型  |                                   描述                              |
|-----------------|------|--------|-----------------------------------------------------------------|
| ZoneId          |   是   |int    | 可用区 ID，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表              |
| NetInterface    | 是   |string | 网络类型，值为 vpc，basic。 其中 vpc 为私有网络，basic 为基础网络                      |
| CreationToken   |  是   |string | 用户自定义文件系统名称                                                  |
| PGroupId   |       是   |  string |  权限组 ID                                |
| Region          |  是   |string |园区，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表                   |
| VpcId           |  否   |int   |  VPC ID，如使用基础网络，请传 0                                 |
| UnVpcId           |  是   |string    | 系统分配的 VPC 统一 ID，由 VPCID 升级而来，为了兼容这两种ID系统都支持，推荐使用统一ID，示例：vpc-2ari9m7h。可以到私有网络控制台获取 VPCID。如使用基础网络，请传0。                                 |
| SubnetId        | 否   |int    | 子网 ID， 如使用基础网络，请传 0         |
| UnSubnetId           |  是   |string    | 系统分配的子网统一 ID，由子网 ID 升级而来，为了兼容这两种ID系统都支持，示例：subnet-5gu2jxf4。可以到私有网络控制台获取 UnSubnetID。如使用基础网络，请传0。|
| MountIP        |  否   |int    | 指定 IP 地址 ，仅 VPC 网络支持       | 




## 响应参数

|    参数名称    |类型|                                                          描述                                                            |
|----------------|--------|--------------------------------------------------------|
| CreationTime   |string | 创建时间                                                                                                                |
| CreationToken  |string| 用户自定义文件系统名称                                                           |
| FileSystemId   |string| 文件系统 ID                                                            |
| LifeCycleState | string |文件系统状态：creating（创建中）、available（可用）、create_failed（创建失败） 、deleting（删除中）、 delete_failed（删除失败） |
| SizeInBytes    |Array  | 文件系统用量信息                                                                                                        |
| ZoneId       | int     | 可用区 ID                                                                                                                 |
| ZoneName       | string     | 可用区名称，示例：ap-guangzhou-1                                                                                                                  |
| Protocol          |  string |文件系统协议类型，输入值 NFS，CIFS；不填默认为 NFS  |


## 实际示例 

### 请求示例 



<pre>
https://cfs.api.qcloud.com/v2/index.php?Action=CreateCfsFileSystem
&Region=bj
&ZoneId=800001
&NetInterface=vpc
&CreationToken=test
&PGroupId=pgroupbasic
&ProtocolType=NFS
&UnVpcId=vpc-fifeioa3
&UnSubnetId=sub-rh3i23s
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


### 响应示例 

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "CreationTime": "2017-11-23 20:51:34",
        "CreationToken": "test",
        "FileSystemId": "cfs-ocAK***abcalejrq8tt",
        "LifeCycleState": "creating",
        "NumberOfMountTargets": 0,
        "PGroup_Order_Id": "pgroupbasic",
        "ProtocolType":"NFS",
        "SizeInBytes": {
            "Timestamp": "1511441494",
            "value": 4000
        },
        "ZoneId": 800001
    }
}

```
