
## 接口描述
本接口（DeleteCfsFileSystem）用于删除文件系统。
接口请求域名：`cfs.api.qcloud.com`

## 输入参数

|    参数    |  必填 |  类型  |                      描述                      |
|------------|------|--------|------------------------------------------------|
| Region     |   是   | string | 园区，请参见 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中园区与可用区列表 |
| FileSystemId  | 是 |string| 文件系统 ID                                      |



## 输出参数

| 参数名称 | 类型 | 描述 |
|----------|------|------|
|    code      |   int   | 公共错误码。0 表示成功，其他值表示失败     |
|    codeDesc   |   string   | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因     |
|    message      |   int   | 模块错误信息描述，与接口相关。详见 错误返回结果     |


## 示例 

#### 输入


<pre>
https://cfs.api.qcloud.com/v2/index.php?Action=DeleteCfsFileSystem
&Region=bj
&FileSystemId=cfs-h97kuqvr
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




