## 功能描述

批量导入用户 - 获取 xlsx 文件上传参数。

#### 接口说明

  - PUT 简单上传指使用 HTTP PUT 请求上传一个文件，调用 COS 接口时，请求体即为文件的内容。
  - 调用该接口将返回一系列用于 PUT 简单上传请求和确认上传完成的参数，上传的目标 URL 为 https://`{Domain}``{Path}`，其中 Domain 为响应体中的 domain 字段，Path 为响应体中的 path 字段，例如 `https://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/smhxxx/xxx.mp4`。
  - PUT 简单上传时还需要指定一系列额外的请求头部字段，这些字段的名和值包含在响应体中的 headers 字段中。
  - 在完成实际上传后，上传的目标 URL 将返回 HTTP 200 OK。

## 请求

#### 请求示例

PUT /user/v1/file/allowlist/`{OrganizationId}`?ext=`{FileExt}`&user_token=`{UserToken}`

- 请求参数：
  - OrganizationId：组织 ID，必选参数
  - UserToken：用户令牌，必选参数
  - FileExt：请求上传的文件后缀，当前仅支持 xlsx 文件

xlsx 文件模板如下：

  | Name/姓名     | Phone/手机号       | Personal capacity /是否分配个人空间（单位为GB）| Enterprise Sector/部门（层级以"/"划分） |
      |----------|-------------|-------------------|-------------------|
  | 张三 | 18666666666 | 5                 | 1级             |
  |      李四    |    13100000000         |     0              |    1级/2级/3级               |


#### 请求体

该请求无请求体。

## 响应

#### 响应码

成功响应，返回 HTTP 200 OK。

#### 响应体

application/json

- 响应体示例：
```json
  {
  "domain": "examplebucket-1250000000.cos.ap-beijing.myqcloud.com",
  "path": "/ghjksdhgfhjasdf",
  "headers": {
    "Cache-Control": "max-age=31104000",
    "Content-Type": "xxx",
    "x-cos-acl": "default",
    "x-cos-storage-class": "STANDARD",
    "Authorization": "xxx",
    "x-cos-security-token": "xxx"
  }
}
```
- 响应体字段说明：
  - domain：字符串，实际上传文件时的域名。
  - path：字符串，实际文件上传时的 URL 路径。
  - headers：键值对，实际上传时需指定的请求头部。
