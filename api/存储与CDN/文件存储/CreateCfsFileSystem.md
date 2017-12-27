## 接口描述
### 功能描述
本接口（CreateCfsFileSystem）用于添加新文件系统。
### 接口域名
文件存储请求域名：`cfs.api.qcloud.com`

## 请求参数
以下请求参数为本接口的请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/product/582/13227) 页面。

<<<<<<< Updated upstream
|       参数      |                                   描述                              |类型  |必填 |
|-----------------|------|--------|-----------------------------------------------------------------|
| ZoneId          |   可用区 ID，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表              |Int    | 是   |
| NetInterface    | 网络类型，值为 vpc，basic。 其中 vpc为私有网络，basic 为基础网络                      |String |是   |
| CreationToken   | 用户自定义文件系统名称                                                  |String | 是   |
| PgroupOrderId   |  权限组 ID，目前仅支持 pgroupbasic                                |  String |       是   |                      
| Region          |  园区，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表                   | String |是   |
| VpcId           |    VPC ID，如使用基础网络，请传 0                                 |Int    |是   |
| SubnetId        |  子网 ID， 如使用基础网络，请传 0                                | Int    |是   |
=======
|       参数      | 子参数 | 必填 |  类型  |                               描述                              |
|-----------------|--------|------|--------|-----------------------------------------------------------------|
| ZoneId          |        | 是   | int    | 可用区ID，请参考"概览"文档中的园区与可用区列表              |
| NetInterface    |        | 是   | string | 网络类型，值为 vpc, basic。 其中 vpc为私有网络，basic为基础网络                      |
| CreationToken   |        | 是   | string | 用户自定义文件系统名称                                                  |
| PgroupOrderId   |        | 是   | string | 权限组ID，目前仅支持 pgroupbasic                                |                                   
| Region          |        | 是   | string | 园区，请参考"概览"文档中的园区与可用区列表                   |
| ClientNetwork          |        | 是   | string | 来访客户类型，可选CVM或CPM ， CVM为云服务器、CPM为黑石服务器                  |
| VpcId           |        | 是   | int    | VPC ID，如使用基础网络，请传0。若ClientNetwork为CPM，则仅支持VPC网络。                                 |
| SubnetId        |        | 是   | int    | 子网ID， 如使用基础网络，请传0。若ClientNetwork为CPM，则仅支持VPC网络。                                |
>>>>>>> Stashed changes


## 响应参数

|    参数名称    |                                                          描述                                                          |类型  |   
|----------------|--------|--------------------------------------------------------|
| CreationTime   |创建时间                                                                                                                | String | 
| CreationToken  | 用户自定义文件系统名称                                                          |String | 
| FileSystemId   | 文件系统 ID                                                           |String | 
| LifeCycleState | 文件系统状态 creating（创建中） available（可用）create_failed（创建失败） deleting（删除中） delete_failed（删除失败） | String |
| SizeInBytes    | 文件系统用量信息                                                                                                        |Array  | 
| ZoneId         | 可用区 ID                                                                                                                | Int    |


## 实际示例 

### 请求示例 


```
  https://cfs.api.qcloud.com/v2/index.php?Action=CreateCfsFileSystem
  &Region=bj
  &ZoneId=800001
  &NetInterface=vpc
  &CreationToken=test
  &PgroupOrderId=pgroupbasic
  &ClientNetwork=CVM
  &VpcId=3034
  &SubnetId=17884
<<<<<<< Updated upstream
  &ActMode=auto
  &<公共请求参数>
=======
  &<<a href="https://www.qcloud.com/doc/api/229/6976"> 公共请求参数 </a>>
</pre>
>>>>>>> Stashed changes
```

### 响应示例 

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




