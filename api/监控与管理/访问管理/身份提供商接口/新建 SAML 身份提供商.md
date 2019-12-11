### 接口描述

本接口（CreateSAMLProvider）用于创建 SAML 身份提供商。
请求域名：cam.api.qcloud.com
请求方式：HTTP POST

### 输入参数

以下请求参数列表仅列出了接口请求参数，其余公共参数列表见 [公共请求参数](https://cloud.tencent.com/document/api/213/15692)。

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| name | 是 | String | SAML 身份提供商名称 |
| desc | 是 | String | 身份提供商描述 |
| SAMLMetadataDocument | 是 | String | SAML 身份提供商元数据文档。需要以 Base64 编码，支持最大数据为 64KB |

备注：若IdP元数据文档超过最大限制，可删除元数据XML文档中除IDPSSODescriptor外的其他XML节点。例如：

``` 
<?xml version="1.0" encoding="utf-8"?>
<EntityDescriptor>
	<IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
		......
	</IDPSSODescriptor>
</EntityDescriptor>
``` 

### 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| name | String | SAML 身份提供商名称 |
| SAMLProviderArn | String | SAML 身体提供商访问描述名称 |

### 示例

创建一个名称为 IdP 的 SAML 身份提供商。

##### 输入示例：

``` 
POST /v2/index.php HTTP/1.1
Host: cam.api.qcloud.com
Accept: */*
Content-Length: 3927
Content-Type: application/x-www-form-urlencoded

Action=CreateSAMLProvider&name=idp&SAMLMetadataDocument=U0FNTE1ldGFkYXRhRG9jdW1lbnQ&desc=descriptor&<公共请求参数>
``` 
##### 输出示例：

``` 
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "name": "idp",
        "SAMLProviderArn": "qcs::cam::uin/798950673:saml-provider/idp"
    }
}

``` 

### 错误码
以下仅列出了接口业务逻辑相关的错误码，其他错误码详见 [公共错误码](https://cloud.tencent.com/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。

| 错误码 | 描述 |
|---------|---------|
| InvalidParameter.ProviderAlreadyExist | 身份提供商已存在 |
| InvalidParameter. SAMLMetadataDocument | SAML 身份提供商元数据文档错误 |
| InvalidParameter.ProviderMaxLimit | 身份提供商达到上限 |
