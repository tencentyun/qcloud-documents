### 接口描述
本接口（GetSAMLProvider）用于查询特定的 SAML 身份提供商信息详情。
请求域名：cam.api.qcloud.com

### 输入参数
以下请求参数列表仅列出了接口请求参数，其余公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/213/15692)。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| name | 是 | String | SAML 身份提供商名称 |

### 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| ownerUin | Integer | 腾讯云账号 ID |
| name |String |身份提供商名称|
| desc |String |身份提供商描述|
| createTime| Date | 身份提供商创建时间|
| modifyTime | Date | 身份提供商上次修改时间 |
| SAMLMetadata | String | SAML 身份提供商元数据文档 |

### 示例

查询名称为 IdP 的 SAML 身份提供商详情。

##### 输入示例：

``` 
https://cam.api.qcloud.com/v2/index.php?Action=GetSAMLProvider
&name=idp
&<公共请求参数>
``` 
##### 输出示例：

``` 
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "ownerUin": 798950673,
        "name": "idp",
        "desc": "SAML 身份提供商",
        "createTime": "2018-10-30 14:43:37",
        "modifyTime": "2018-10-30 14:50:38",
        "SAMLMetadata": "U0FNTE1ldGFkYXRh"
    }
}
``` 

### 错误码

该接口暂无业务逻辑相关的错误码，其他错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。


