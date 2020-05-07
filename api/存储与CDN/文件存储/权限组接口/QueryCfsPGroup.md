## 接口描述
本接口（QueryCfsPGroup）用于查询权限组列表。
接口请求域名：`cfs.api.qcloud.com`
## 输入参数
|       参数      |  必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
|      Uin       |  是 |   int |                                用户 ID                        |
|    AppId        | 是  |  int  |                          用户 APPID                                |


## 输出参数
| 参数名称 | 子参数 |  类型 | 描述 |
|----------|------  |----- | ---- |
|PGrouplist|    -     |  array  |权限组信息列表 |
|  -        | PGroupId |  string |权限组 ID |
|    -      | Name    |  string |权限组名称 |
|    -      | DescInfo|  string |描述信息 |
|     -     | CDate   |  string |创建时间 |
|     -     | BindCfsNum| int    |关联文件系统个数|

## 示例 

### 输入



<pre>
https://cfs.test.api.qcloud.com/v2/index.php?Action=QueryCfsPGroup
&Uin=2770000000
&AppId=1250000000
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "PGrouplist": [
            {
                "PGroupId": "pgroup-atutdqup",
                "Name": "dd",
                "DescInfo": "2345",
                "BindCfsNum": 0,
                "CDate": "2017-07-05 19:04:18"
            },
            
            {
                "PGroupId": "pgroup-8rf7odn5",
                "Name": "test23",
                "DescInfo": "ddd",
                "BindCfsNum": 0,
                "CDate": "2017-07-06 10:57:29"
            },
            {
                "PGroupId": "pgroup-19l63t3p",
                "Name": "测试",
                "DescInfo": "use for test",
                "BindCfsNum": 1,
                "CDate": "2017-08-03 16:06:38"
            },
            {
                "PGroupId": "pgroupbasic",
                "Name": "默认权限组",
                "DescInfo": "默认权限组",
                "BindCfsNum": 5,
                "CDate": "2017-06-21 17:30:05"
            }
        ]
    }
}

```


