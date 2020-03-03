## 功能描述

PUT Bucket acl 接口用来写入存储桶的访问控制列表（ACL），您可以通过请求头 `x-cos-acl` 和 `x-cos-grant-*` 传入 ACL 信息，或者通过请求体以 XML 格式传入 ACL 信息。
>!
>- 通过请求头设置 ACL 和通过请求体设置 ACL 两种方式只能选择其中一种。
>- PUT Bucket acl 是一个覆盖操作，传入新的 ACL 将覆盖原有 ACL。
>- 仅可对腾讯云 CAM 主账号或匿名用户授予权限，如需授予子用户或用户组权限请使用 [PUT Bucket policy](https://cloud.tencent.com/document/product/436/8282) 接口。有关 ACL 的详细说明，请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752)。
>- 该 API 的请求者需要对存储桶有写入 ACL 权限。

## 请求

#### 请求示例

**示例一**
```shell
PUT /?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: 0
Authorization: Auth String
```
**示例二**
```shell
PUT /?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Content-MD5: MD5
Authorization: Auth String

[Request Body]
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

名称|描述|类型|是否必选
---|---|---|---
x-cos-acl|定义存储桶的访问控制列表（ACL）属性。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中存储桶的预设 ACL 部分，如 private, public-read 等，默认为 private|Enum|否
x-cos-grant-read|赋予被授权者读取存储桶的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`|string|否
x-cos-grant-write|赋予被授权者写入存储桶的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`|string|否
x-cos-grant-read-acp|赋予被授权者读取存储桶的访问控制列表（ACL）和存储桶策略（Policy）的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`|string|否
x-cos-grant-write-acp|赋予被授权者写入存储桶的访问控制列表（ACL）和存储桶策略（Policy）的权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`|string|否
x-cos-grant-full-control|赋予被授权者操作存储桶的所有权限，格式为 id="[OwnerUin]"，如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，如 `id="100000000001",id="100000000002"`|string|否

#### 请求体

提交 **application/xml** 请求数据，包含存储桶所有者和完整的授权信息。

```shell
<AccessControlPolicy>
	<Owner>
		<ID>string</ID>
	</Owner>
	<AccessControlList>
		<Grant>
			<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
				<URI>string</URI>
			</Grantee>
			<Permission>Enum</Permission>
		</Grant>
		<Grant>
			<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
				<ID>string</ID>
			</Grantee>
			<Permission>Enum</Permission>
		</Grant>
	</AccessControlList>
</AccessControlPolicy>
```

具体的节点描述如下：

节点名称（关键字）|父节点|描述|类型|是否必选
---|---|---|---|---
AccessControlPolicy|无|包含 PUT Bucket acl 操作的所有请求信息|Container|是

**Container 节点 AccessControlPolicy 的内容：**

节点名称（关键字）|父节点|描述|类型|是否必选
---|---|---|---|---
Owner|AccessControlPolicy|存储桶持有者信息|Container|是
AccessControlList|AccessControlPolicy|被授权者信息与权限信息|Container|是

**Container 节点 Owner 的内容：**

节点名称（关键字）|父节点|描述|类型|是否必选
---|---|---|---|---
ID|AccessControlPolicy.Owner|存储桶持有者的完整 ID，格式为 `qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`，如 `qcs::cam::uin/100000000001:uin/100000000001`|string|是

**Container 节点 AccessControlList 的内容：**

节点名称（关键字）|父节点|描述|类型|是否必选
---|---|---|---|---
Grant|AccessControlPolicy.AccessControlList|单个授权信息，一个 AccessControlList 最多只能拥有100条 Grant|Container|是

**Container 节点 AccessControlList.Grant 的内容：**

节点名称（关键字）|父节点|描述|类型|是否必选
---|---|---|---|---
Grantee|AccessControlPolicy.AccessControlList.Grant|被授权者信息，`xsi:type` 可指定为 Group 或 CanonicalUser，当指定为 Group 时子节点包括且仅允许包括 URI，当指定为 CanonicalUser 时子节点包括且仅允许包括 ID|Container|是
Permission|AccessControlPolicy.AccessControlList.Grant|授予的权限信息。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E6.93.8D.E4.BD.9C-permission) 文档中存储桶的操作部分，如 WRITE，FULL_CONTROL 等|Enum|是

**Container 节点 AccessControlList.Grant.Grantee 的内容：**

节点名称（关键字）|父节点|描述|类型|是否必选
---|---|---|---|---
URI|AccessControlPolicy.AccessControlList.Grant.Grantee|预设用户组。请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E8.BA.AB.E4.BB.BD-grantee) 文档中预设用户组部分，如 `http://cam.qcloud.com/groups/global/AllUsers` 或 `http://cam.qcloud.com/groups/global/AuthenticatedUsers`|string|当 `Grantee` 的 `xsi:type` 指定为 `Group` 时必选
ID|AccessControlPolicy.AccessControlList.Grant.Grantee|被授权者的完整 ID，格式为 `qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`，如 `qcs::cam::uin/100000000001:uin/100000000001`|string|当 `Grantee` 的 `xsi:type` 指定为 `CanonicalUser` 时必选

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口的特殊错误信息如下所述，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

错误码|描述|HTTP 状态码
---|---|---
InvalidDigest|给定的 Content-MD5 值不合法|400 Bad Request
MalformedXML|请求体的 XML 格式不符合 XML 语法|400 Bad Request

## 实际案例

#### 案例一：通过请求头设置 ACL

#### 请求

```shell
PUT /?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 17 Jun 2019 08:30:12 GMT
x-cos-acl: public-read
x-cos-grant-write: id="100000000002"
x-cos-grant-read-acp: id="100000000002"
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1560760212;1560767412&q-key-time=1560760212;1560767412&q-header-list=content-length;date;host;x-cos-acl;x-cos-grant-read-acp;x-cos-grant-write&q-url-param-list=acl&q-signature=5b10c6ea4e6c9630c085e1f85476c76d8c4e****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Mon, 17 Jun 2019 08:30:13 GMT
Server: tencent-cos
x-cos-request-id: NWQwNzRmOTRfODhjMjJhMDlfMWRlYl81Mzc0****
```

#### 案例二：通过请求体设置 ACL

#### 请求

```shell
PUT /?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 17 Jun 2019 08:30:13 GMT
Content-Type: application/xml
Content-Length: 812
Content-MD5: 1qS+8SqnivarcO6Z11R0nw==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1560760213;1560767413&q-key-time=1560760213;1560767413&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=acl&q-signature=70f96b91823f3715905df125d96fe447554e****
Connection: close

<AccessControlPolicy>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
	</Owner>
	<AccessControlList>
		<Grant>
			<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
				<URI>http://cam.qcloud.com/groups/global/AllUsers</URI>
			</Grantee>
			<Permission>READ</Permission>
		</Grant>
		<Grant>
			<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
				<ID>qcs::cam::uin/100000000002:uin/100000000002</ID>
			</Grantee>
			<Permission>WRITE</Permission>
		</Grant>
		<Grant>
			<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
				<ID>qcs::cam::uin/100000000002:uin/100000000002</ID>
			</Grantee>
			<Permission>READ_ACP</Permission>
		</Grant>
	</AccessControlList>
</AccessControlPolicy>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Mon, 17 Jun 2019 08:30:13 GMT
Server: tencent-cos
x-cos-request-id: NWQwNzRmOTVfMzBjMDJhMDlfOTM3MF8yNzdj****
```
