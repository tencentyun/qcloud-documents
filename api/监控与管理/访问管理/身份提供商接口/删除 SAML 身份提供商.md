### 接口描述

本接口（DeleteSAMLProvider）用于删除 SAML 身份提供商。
请求域名：cam.api.qcloud.com

### 输入参数

以下请求参数列表仅列出了接口请求参数，其余公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/213/15692)。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| name | 是 | String | SAML 身份提供商名称|

### 输出参数

暂无。


### 示例

删除一个名称为 IdP 的 SAML 身份提供商.

##### 输入示例：

``` 
https://cam.api.qcloud.com/v2/index.php?Action=DeleteSAMLProvider
&name=idp
&<公共请求参数>
``` 

##### 输出示例：

``` 
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}
``` 

### 错误码

以下仅列出了接口业务逻辑相关的错误码，其他错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。

| 错误码 | 描述 |
|---------|---------|
| InvalidParameter.ProviderNotExist | 身份提供商不已存在|
