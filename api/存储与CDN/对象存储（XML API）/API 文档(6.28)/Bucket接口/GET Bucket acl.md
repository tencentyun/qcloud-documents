## 功能描述

GET Bucket acl 接口用来获取存储桶的访问控制列表（ACL）。该 API 的请求者需要对存储桶有读取 ACL 权限。

## 请求

#### 请求示例

```shell
GET /?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体
该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含存储桶所有者和完整的授权信息。

```shell
<AccessControlPolicy>
	<Owner>
		<ID>string</ID>
		<DisplayName>string</DisplayName>
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
				<DisplayName>string</DisplayName>
			</Grantee>
			<Permission>Enum</Permission>
		</Grant>
	</AccessControlList>
</AccessControlPolicy>
```

具体的节点描述如下：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
AccessControlPolicy|无|保存 GET Bucket acl 结果的所有信息|Container

**Container 节点 AccessControlPolicy 的内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Owner|AccessControlPolicy|存储桶持有者信息|Container
AccessControlList|AccessControlPolicy|被授权者信息与权限信息|Container

**Container 节点 Owner 的内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ID|AccessControlPolicy.Owner|存储桶持有者的完整 ID，格式为 `qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`，如 `qcs::cam::uin/100000000001:uin/100000000001`|string
DisplayName|AccessControlPolicy.Owner|存储桶持有者的名字|string

**Container 节点 AccessControlList 的内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Grant|AccessControlPolicy.AccessControlList|单个授权信息|Container

**Container 节点 AccessControlList.Grant 的内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Grantee|AccessControlPolicy.AccessControlList.Grant|被授权者信息，`xsi:type` 为 Group 或 CanonicalUser，当为 Group 时子节点包括且仅包括 URI，当指定为 CanonicalUser 时子节点包括且仅包括 ID 和 DisplayName|Container
Permission|AccessControlPolicy.AccessControlList.Grant|授予的权限信息，枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E6.93.8D.E4.BD.9C-permission) 文档中存储桶的操作部分，如 WRITE，FULL_CONTROL 等|Enum

**Container 节点 AccessControlList.Grant.Grantee 的内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
URI|AccessControlPolicy.AccessControlList.Grant.Grantee|预设用户组，请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E8.BA.AB.E4.BB.BD-grantee) 文档中预设用户组部分，如 `http://cam.qcloud.com/groups/global/AllUsers` 或 `http://cam.qcloud.com/groups/global/AuthenticatedUsers`|string
ID|AccessControlPolicy.AccessControlList.Grant.Grantee|被授权者的完整 ID，格式为 `qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`，如 `qcs::cam::uin/100000000001:uin/100000000001`|string
DisplayName|AccessControlPolicy.AccessControlList.Grant.Grantee|被授权者的名字|string

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
GET /?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 17 Jun 2019 08:37:35 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1560760655;1560767855&q-key-time=1560760655;1560767855&q-header-list=date;host&q-url-param-list=acl&q-signature=24b9d377eac860917a33c8c298042ce5b1a5****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1035
Connection: close
Date: Mon, 17 Jun 2019 08:37:36 GMT
Server: tencent-cos
x-cos-request-id: NWQwNzUxNTBfMzdiMDJhMDlfOWM0Nl85NDFk****

<AccessControlPolicy>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>qcs::cam::uin/100000000001:uin/100000000001</DisplayName>
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
				<DisplayName>qcs::cam::uin/100000000002:uin/100000000002</DisplayName>
			</Grantee>
			<Permission>WRITE</Permission>
		</Grant>
		<Grant>
			<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
				<ID>qcs::cam::uin/100000000002:uin/100000000002</ID>
				<DisplayName>qcs::cam::uin/100000000002:uin/100000000002</DisplayName>
			</Grantee>
			<Permission>READ_ACP</Permission>
		</Grant>
	</AccessControlList>
</AccessControlPolicy>
```
