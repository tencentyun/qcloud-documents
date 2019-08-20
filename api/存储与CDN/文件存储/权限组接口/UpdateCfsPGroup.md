## 接口描述
本接口（UpdateCfsPGroup）更新权限组信息。
接口请求域名：`cfs.api.qcloud.com`



## 输入参数
|       参数      | 必填 |  类型  |                               描述                           |
|-----------------|-----|--------|--------------------------------------------------------------|
| Name   |  否  | string | 权限组名称 |
| PGroupId   |是   | string | 权限组 ID                                |                                   
| DescInfo  | 否   | string | 描述信息                   |

## 输出参数

| 参数名称 | 类型 | 描述 |
|----------|----- | ---- |
|PGroupId|   string |权限组 ID|
|Name |   string    |权限组名称|
|DescInfo  |  string |描述信息|

## 示例 

#### 输入



<pre>
https://cfs.test.api.qcloud.com/v2/index.php?Action=UpdateCfsPGroup
&Uin=2770000000
&AppId=1250000000
&PGroupId=pgroup-3hfob9vf
&Name=updated-test02
&DescInfo=xxxxxx
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


#### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "PGroupId": "pgroup-3hfob9vf",
        "Name": "updated-test02",
        "DescInfo": "xxxxxx"
    }
}
```


