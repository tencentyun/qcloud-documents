
## 1.接口描述
本接口（CreateCfsFileSystem）用于添加新文件系统。
接口请求域名：**cfs.api.qcloud.com**

## 2.输入参数

|       参数      | 子参数 | 必填 |  类型  |                               描述                              |
|-----------------|--------|------|--------|-----------------------------------------------------------------|
| ZoneId          |        | 是   | int    | 可用区ID，请参考"概览"文档中的园区与可用区列表              |
| NetInterface    |        | 是   | string | 网络类型，值为 vpc, basic。 其中 vpc为私有网络，basic为基础网络                      |
| CreationToken   |        | 是   | string | 用户自定义文件系统名称                                                  |
| PgroupOrderId   |        | 是   | string | 权限组ID，目前仅支持 pgroupbasic                                |                                   
| Region          |        | 是   | string | 园区，请参考"概览"文档中的园区与可用区列表                   |
| VpcId           |        | 是   | int    | VPC ID，如使用基础网络，请传0                                 |
| SubnetId        |        | 是   | int    | 子网ID， 如使用基础网络，请传0                                |


## 3.输出参数

|    参数名称    |  类型  |                                                           描述                                                          |
|----------------|--------|-------------------------------------------------------------------------------------------------------------------------|
| CreationTime   | string | 创建时间                                                                                                                |
| CreationToken  | string | 用户自定义文件系统名称                                                                                                          |
| FileSystemId   | string | 文件系统ID                                                                                                              |
| LifeCycleState | string | 文件系统状态 creating（创建中） available（可用）create_failed（创建失败） deleting（删除中） delete_failed（删除失败） |
| SizeInBytes    | array  | 文件系统用量信息                                                                                                        |
| ZoneId         | int    | 可用区ID                                                                                                                |


## 4.示例 

### 输入


```
<pre>
  https://cfs.api.qcloud.com/v2/index.php?Action=CreateCfsFileSystem
  &Region=bj
  &ZoneId=800001
  &NetInterface=vpc
  &CreationToken=test
  &PgroupOrderId=pgroupbasic
  &PerformanceMode=sata
  &VpcId=3034
  &SubnetId=17884
  &ActMode=auto
  &<<a href="https://www.qcloud.com/doc/api/229/6976"> 公共请求参数 </a>>
</pre>
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "CreationTime": "2017-11-23 20:51:34",
        "CreationToken": "test",
        "FileSystemId": "cfs-ocakq8tt",
        "LifeCycleState": "creating",
        "NumberOfMountTargets": 0,
        "PGroup_Order_Id": "pgroupbasic",
        "SizeInBytes": {
            "Timestamp": "1511441494",
            "value": 4000
        },
        "ZoneId": 800001
    }
}

```




