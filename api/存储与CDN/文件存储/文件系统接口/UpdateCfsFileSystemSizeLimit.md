## 接口描述
本接口（UpdateCfsFileSystemSizeLimit）用于更新文件系统空间限制。
接口请求域名：`cfs.api.qcloud.com`

## 输入参数

|       参数      | 必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
|FsLimit    |   是  | int | 文件系统容量限制大小，输入范围 1-1073741824, 单位为 GB |
|FileSystemId       |   是  | string | 文件系统 ID|
|Region         |  是   | string | 园区，请参考概览园区信息 |

## 输出参数

| 参数名称 | 类型 | 描述 |
|----------|------|------|
|    code      |   int   | 公共错误码。0表示成功，其他值表示失败     |
|    codeDesc   |   string   | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因     |
|    message      |   int   | 模块错误信息描述，与接口相关     |


## 示例 

#### 输入


<pre>
https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsFileSystemSizeLimit
&Region=gz
&Uin=2770000000
&AppId=1250000000
&FileSystemId=cfs-ci0kagcd
&FsLimit=1000
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


#### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}
```

