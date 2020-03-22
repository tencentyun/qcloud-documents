### 接口描述

本接口（ListSAMLProviders）用于获取 SAML 身份提供商列表。
请求域名：cam.api.qcloud.com

### 输入参数
以下请求参数列表仅列出了接口请求参数，其余公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/213/15692)。

| 参数名称 | 必选 | 类型 | 描述|
|---------|---------|---------|---------|
|page | 是 | Integer | 页码 |
|rp | 是 |Integer | 页面大小 |

### 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| total | Integer | 身份提供商总数 |
| list | Array Of SAMLProvider | SAML 身份提供商列表 |

SAMLProvider 字段展示如下：

| 名称 | 类型 | 描述 |
|---------|---------|---------|
| name | String | 身份提供商名称 |
| desc | String | 身份提供商描述|
| createTime | Date | 身份提供商创建时间 |
| modifyTime | Date| 身份提供商更新时间 |


###  示例

查询 SAMl 身份提供商列表。

##### 输入示例：

``` 
https://cam.api.qcloud.com/v2/index.php?Action=ListSAMLProviders
&page=1
&rp=5
&<公共请求参数>
``` 

##### 输出示例：

``` 
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "total": 9,
        "list": [
            {
                "name": "api-test-v2",
                "desc": "API测试12121",
                "createTime": "2018-10-30 14:43:36",
                "modifyTime": "2018-10-30 14:57:35"
            },
            {
                "name": "api-test",
                "desc": "API测试",
                "createTime": "2018-10-30 11:40:19",
                "modifyTime": "2018-10-30 11:40:19"
            },
            {
                "name": "aaaaaaaaaaa",
                "desc": "测试",
                "createTime": "2018-10-17 17:16:17",
                "modifyTime": "2018-10-17 17:16:17"
            },
            {
                "name": "test1112222",
                "desc": "111111",
                "createTime": "2018-10-15 21:30:08",
                "modifyTime": "2018-10-15 21:30:08"
            },
            {
                "name": "test111",
                "desc": "111111",
                "createTime": "2018-10-12 18:09:19",
                "modifyTime": "2018-10-12 18:09:19"
            }
        ]
    }
}
``` 

###  错误码
该接口暂无业务逻辑相关的错误码，其他错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。

