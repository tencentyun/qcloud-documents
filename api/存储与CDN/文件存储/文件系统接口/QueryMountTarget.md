## 接口描述
### 功能描述
本接口（QueryMountTarget）用于查询文件系统挂载点信息。

### 接口域名
文件存储请求域名：`cfs.api.qcloud.com`

## 请求参数
以下请求参数为本接口的请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/product/582/13227) 页面。

|    参数   | 必填 |  类型 |                       描述                         |
|------------|-----|--------|------------------------------------------------|
| Region     |    是   | string |园区，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表 |
| FileSystemId | 是  |string| 文件系统 ID                                       |


## 响应参数

|     参数名称     |             类型  |          描述                        |
|------------------|--------|-----------------------------------|
| FileSystemId     | string | 文件系统 ID                                                  |
| IpAddress        |  string |挂载点 IP                                          |
| FSID             |  string |挂载点 ID                                                   |
| LifeCycleState   | string | 文件系统状态 creating（创建中） available（可用）create_failed（创建失败） deleting（删除中） delete_failed（删除失败） |
| NetworkInterface | String | 网络类型，可选参数 vpc （私有网络），basic（基础网络）                                          |
| VpcId            |int    | 私有网络 ID                                 |
| VpcName          | string | 私有网络名称               |
| SubnetId         |  int    |子网 ID                       |
| SubnetName       | string |子网名称                                     |
| ZoneId           | int    |可用区 ID，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表                       |



## 实际示例 

### 请求示例

```shell
https://cfs.api.qcloud.com/v2/index.php?Action=QueryMountTarget
&Region=bj
&FileSystemId=cfs-h97kuqvr
&<公共请求参数>
```

### 响应示例

```shell
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "MountTargets": [
            {
                "FileSystemId": "cfs-h97kuqvr",
                "IpAddress": "10.0.2.15",
                "FSID": "0322wz9j",
                "LifeCycleState": "available",
                "MountTargetId": "mount-q9wejp86",
                "ClientNetwork": "CVM",
                "NetworkInterface": "vpc",
                "VpcId": "229392421",
                "VpcName": "vpc-4h0fngoa",
                "SubnetId": "12904934",
                "SubnetName": "subnet-pdloiv75",
                "ZoneId": 800001
            }
        ]
    }
}
```
