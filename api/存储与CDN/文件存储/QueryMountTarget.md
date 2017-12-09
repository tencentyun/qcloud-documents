
## 1.接口描述
本接口（QueryMountTarget）用于查询文件系统挂载点信息。
接口请求域名：**cfs.api.qcloud.com**

## 2.输入参数

|    参数    | 子参数 | 必填 |  类型  |                      描述                      |
|------------|--------|------|--------|------------------------------------------------|
| Region     |        | 是   | string | 园区，请参考"概览"文档中的园区与可用区列表 |
| CfsOrderId |        | 是   | string | CFS实例ID                                      |


## 3.输出参数

|     参数名称     |  类型  |                                                           描述                                                          |
|------------------|--------|-------------------------------------------------------------------------------------------------------------------------|
| FileSystemId     | string | 文件系统ID                                                                                                              |
| IpAddress        | string | 挂载点IP                                                                                                                |
| FSID             | string | 挂载点ID                                                                                                                |
| LifeCycleState   | string | 文件系统状态 creating（创建中） available（可用）create_failed（创建失败） deleting（删除中） delete_failed（删除失败） |
| NetworkInterface | string | 网络类型 vpc（私有网络） basic（基础网络）                                                                              |
| VpcId            | int    | 私有网络ID                                                                                                              |
| VpcName          | string | 私有网络名称                                                                                                            |
| SubnetId         | int    | 子网Id                                                                                                                  |
| SubnetName       | string | 子网名称                                                                                                                |
| ZoneId           | int    | 可用区ID，请参考"概览"文档中的园区与可用区列表                                                                      |


## 4.示例 

###输入

```
<pre>
  https://cfs.api.qcloud.com/v2/index.php?Action=QueryMountTarget
  &Region=bj
  &CfsOrderId=cfs-h97kuqvr
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
</pre>
```

###输出

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




