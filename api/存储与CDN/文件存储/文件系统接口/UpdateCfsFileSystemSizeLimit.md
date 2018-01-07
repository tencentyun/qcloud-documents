## 1.接口描述
本接口（UpdateCfsFileSystemSizeLimit）用于更新文件系统空间限制。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      | 子参数 | 必填 |  类型  |                               描述                           |
|-----------------|--------|------|--------|--------------------------------------------------------------|
|FsLimit    |        |  是  | int | GB为单位大小 |
|OrderId       |        |  是  | string | 文件系统订单ID|
|Region         |       | 是   | string | 园区 |

## 3.输出参数
| 参数名称 | 子参数 |  子参数 | 类型 | 描述 |
|----------|------  |-------- |----- | ---- |


## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsFileSystemSizeLimit
  &Region=gz
  &Uin=2779643970
  &AppId=1251668577
  &OrderId=cfs-ci0kagcd
  &FsLimit=1000
  &<<a href="https://www.qcloud.com/doc/api/229/6976"> 公共请求参数 </a>>
</pre>
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

```