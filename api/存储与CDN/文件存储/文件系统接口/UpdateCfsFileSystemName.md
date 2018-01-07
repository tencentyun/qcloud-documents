## 1.接口描述
本接口（UpdateCfsFileSystemName）用于更新文件系统名。
接口请求域名：**cfs.api.qcloud.com**
## 2.输入参数
|       参数      | 子参数 | 必填 |  类型  |                               描述                           |
|-----------------|--------|------|--------|--------------------------------------------------------------|
| CreationToken   |        | 是   | string | 用户自定义文件系统名称										     |
| CfsId   |        | 是   | string | 文件系统订单ID                                |                                   

## 3.输出参数
| 参数名称 | 子参数 |  子参数 | 类型 | 描述 |
|----------|------  |-------- |----- | ---- |
|CreationToken|               |           |string |用户自定义文件系统名称|
|FileSystemId |               |           |string    |文件系统订单ID|

## 4.示例 

### 输入


```
<pre>
  https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsFileSystemName
  &Uin=2779643970
  &AppId=1251668577
  &CreationToken=hello-world
  &CfsId=cfs-8xbtlopj
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
        "CreationToken": "hello-world",
        "FileSystemId": "cfs-8xbtlopj"
    }
}

```

