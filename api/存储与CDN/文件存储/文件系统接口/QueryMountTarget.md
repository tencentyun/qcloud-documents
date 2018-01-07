## 接口描述
### 功能描述
本接口（QueryMountTarget）用于查询文件系统挂载点信息。

### 接口域名
文件存储请求域名：`cfs.api.qcloud.com`

## 请求参数
以下请求参数为本接口的请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/product/582/13227) 页面。

|    参数    |                       描述                      |  类型  | 必填 |
|------------|-----|--------|------------------------------------------------|
| Region     |   园区，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表 | String |  是   |
| CfsOrderId | CFS 实例 ID                                      | String | 是   |


## 响应参数

|     参数名称     |                      描述                        |类型  |  
|------------------|--------|-----------------------------------|
| FileSystemId     | 文件系统 ID                                                  |String | 
| IpAddress        |  挂载点 IP                                          |String |
| FSID             |  挂载点 ID                                                   |String |
| LifeCycleState   |  文件系统状态 creating（创建中） available（可用）create_failed（创建失败） deleting（删除中） delete_failed（删除失败） |String |
| NetworkInterface |  网络类型 vpc（私有网络） basic（基础网络）                                          |String |
| VpcId            |私有网络 ID                                 | Int    | 
| VpcName          | 私有网络名称               |String | 
| SubnetId         |  子网 Id                       |Int    |
| SubnetName       | 子网名称                                     |String | 
| ZoneId           | 可用区 ID，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表                       |Int    | 



## 实际示例 

### 请求示例

```
  https://cfs.api.qcloud.com/v2/index.php?Action=QueryMountTarget
  &Region=bj
  &CfsOrderId=cfs-h97kuqvr
  &<公共请求参数>
```

### 响应示例

```
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
                "VpcId": "vpc-4h0fngoa",
                "VpcName": "222",
                "SubnetId": "subnet-pdloiv75",
                "SubnetName": "sddds",
                "ZoneId": 800001,
            }
        ]
    }
}

```




