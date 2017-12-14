
## 接口描述
### 功能描述
本接口（DeleteCfsFileSystem）用于删除文件系统。

### 接口域名
文件存储请求域名：`cfs.api.qcloud.com`

## 请求参数
以下请求参数为本接口的请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/product/582/13227) 页面。

|    参数    |                    描述                      | 类型  |   必填 |  
|------------|------|--------|------------------------------------------------|
| Region     |   园区，请参考 [概览](https://cloud.tencent.com/document/product/582/13225) 文档中的园区与可用区列表 |String |是   | 
| CfsOrderId |   CFS 实例 ID                                      | String |是   |



## 响应参数

| 参数名称 |  描述 |类型 |
|----------|------|------|
|    code      | 公共错误码。0 表示成功，其他值表示失败。     |  Int   | 
|    codeDesc   |  业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因     | String   | 
|    message      |  模块错误信息描述，与接口相关。详见 [错误返回结果](https://cloud.tencent.com/document/product/582/13234)     | Int   | 


## 实际示例 

### 请求示例

```
  https://cfs.api.qcloud.com/v2/index.php?Action=DeleteCfsFileSystem
  &Region=bj
  &CfsOrderId=cfs-h97kuqvr
  &ActMode=auto
  &<公共请求参数>
```

### 响应示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

```




