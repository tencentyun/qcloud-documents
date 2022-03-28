## 功能描述

确认上传企业 Logo。

#### 接口说明

权限要求：超级管理员或系统管理员。

## 请求

#### 请求示例

POST /user/v1/file/organization-logo/`{OrganizationId}`/`{FilePath}`?user_token=`{UserToken}`

请求参数：
- OrganizationId: 组织 ID，必选参数。
- UserToken: 用户令牌，必选参数。
- FilePath: 企业 logo 文件 path，即获取企业 logo 简单上传文件参数中的响应字段 path，必选参数。

#### 请求体

该请求无请求体。

## 响应

#### 响应码

更改成功，返回 HTTP 200 OK。

#### 响应体

application/json

- 响应体示例：
```json
{
  "logo": "//tdrive.file.com/xxx.png"
}
```
- 响应体字段说明：
  logo: 字符串，企业 logo 图片链接。
