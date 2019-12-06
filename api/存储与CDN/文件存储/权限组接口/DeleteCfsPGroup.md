## 接口描述
本接口（DeleteCfsPGroup）用于删除权限组。
接口请求域名：`cfs.api.qcloud.com`

## 输入参数

|       参数      | 必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
| PGroupId        | 是   | string | 权限组 ID|


## 输出参数

| 参数名称 |  类型 | 描述 |
|----------|----- | ---- |
|AppId     | int    |用户 ID   |
|PGroupId   | string |权限组 ID |


## 示例 

#### 输入


<pre>
https://cfs.test.api.qcloud.com/v2/index.php?Action=DeleteCfsPGroup
&Uin=27790000000
&AppId=1250000000
&PGroupId=pgroup-qa948g7z
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


#### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "PGroupId": "pgroup-qa948g7z",
        "AppId": 1250000000
    }
}

```


