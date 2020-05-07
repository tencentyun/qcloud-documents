## 接口描述
本接口（UpdateCfsFileSystemPGroup）用于更新文件系统所属权限组。
接口请求域名：`cfs.api.qcloud.com`

## 输入参数

|       参数      | 必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
|PGroupId    |  是  | string | 权限组 ID |
|FileSystemId       |   是  | string | 文件系统 ID|

## 输出参数

| 参数名称 | 类型 | 描述 |
|----------|----- | ---- |
|PGroupId    |   string | 权限组 ID |
|FileSystemId       |   string | 文件系统 ID|
|AppId            |   int    | 用户 ID|


## 示例 

#### 输入



<pre>
https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsFileSystemPGroup
&Uin=2770000000
&AppId=1250000000
&PGroupId=pgroupbasic
&FileSystemId=cfs-ci0kagcd
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


#### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "cfs_order_id": "cfs-ci0kagcd",
        "pgroup_order_id": "pgroupbasic",
        "app_id": 1250000000
    }
}

```


