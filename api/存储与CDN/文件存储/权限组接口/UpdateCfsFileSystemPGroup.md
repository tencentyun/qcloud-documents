## 1.接口描述
本接口（UpdateCfsFileSystemPGroup）用于更新文件系统所属权限组。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      | 子参数 | 必填 |  类型  |                               描述                           |
|-----------------|--------|------|--------|--------------------------------------------------------------|
|PGroupOrderId    |        |  是  | string | 权限组ID |
|CfsOrderId       |        |  是  | string | 文件系统订单ID|

## 3.输出参数
| 参数名称 | 子参数 |  子参数 | 类型 | 描述 |
|----------|------  |-------- |----- | ---- |
|PGroupOrderId    |        |    | string | 权限组ID |
|CfsOrderId       |        |    | string | 文件系统订单ID|
|AppId            |         |   | int    | 用户ID|


## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsFileSystemPGroup
  &Uin=2779643970
  &AppId=1251668577
  &PGroupOrderId=pgroupbasic
  &CfsOrderId=cfs-ci0kagcd
  &<<a href="https://www.cloud.tencent.com/doc/api/229/6976"> 公共请求参数 </a>>
</pre>
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "cfs_order_id": "cfs-ci0kagcd",
        "pgroup_order_id": "pgroupbasic",
        "app_id": 1251668577
    }
}

```


