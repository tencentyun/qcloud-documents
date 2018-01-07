## 1.接口描述
本接口（UpdateCfsFileSystemSizeLimit）用于更新文件系统空间限制。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      | 必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
|FsLimit    |   是  | int | 文件系统容量限制大小，输入范围1-1073741824, 单位为GB |
|OrderId       |   是  | string | 文件系统订单ID|
|Region         |  是   | string | 园区, 请参考概览园区信息 |

## 3.输出参数
| 参数名称 | 子参数 |  子参数 | 类型 | 描述 |
|----------|------  |-------- |----- | ---- |


## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsFileSystemSizeLimit
  &Region=gz
  &Uin=2770000000
  &AppId=1250000000
  &OrderId=cfs-ci0kagcd
  &FsLimit=1000
  &<<a href="https://www.cloud.tencent.com/doc/api/229/6976"> 公共请求参数 </a>>
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

