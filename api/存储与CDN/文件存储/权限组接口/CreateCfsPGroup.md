## 接口描述
本接口（CreateCfsPGroup）用于创建权限组。
接口请求域名：`cfs.api.cloud.tencent.com`
## 输入参数
|       参数      | 必填 |  类型  |                               描述                           |
|-----------------|------|--------|--------------------------------------------------------------|
| Name            |  是   | string | 权限组名字                      | 
| DescInfo        |  否   | string | 权限组描述信息 |

## 输出参数
| 参数名称 |  类型 | 描述 |
|----------|----- | ---- |
|PGroupId   |  string |权限组 ID|
|Name      |  string |权限组名字|
|DescInfo  |  string |权限组描述信息|
|BindCfsNum|  int    |权限组关联文件系统个数|
|CDate     |  string |权限组创建时间|

## 示例 

### 输入

<pre>
https://cfs.test.api.cloud.tencent.com/v2/index.php?Action=CreateCfsPGroup&SecretId=1
&Uin=277000000
&AppId=1250000000
&Name=helloworld1112
&DescInfo=justfortest11
&<<a href="https://www.cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>


### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "PGroupId": "pgroup-bla6gpb3",
        "Name": "helloworld1112",
        "DescInfo": "justfortest11",
        "BindCfsNum": 0,
        "CDate": "2017-12-20 10:25:33"
    }
}

```

