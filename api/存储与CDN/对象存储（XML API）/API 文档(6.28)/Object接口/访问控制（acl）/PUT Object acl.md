## 功能描述

PUT Object acl 接口用来写入对象的访问控制列表（ACL），您可以通过请求头`x-cos-acl`和`x-cos-grant-*`传入 ACL 信息，或者通过请求体以 XML 格式传入 ACL 信息。
> !
> - 通过请求头设置 ACL 和通过请求体设置 ACL，两种方式只能选择其中一种。
> - PUT Object acl 是一个覆盖操作，传入新的 ACL 将覆盖原有 ACL。
> - 仅可对腾讯云 CAM 主账号或匿名用户授予权限，如需授予子用户或用户组权限请使用 [PUT Bucket policy](https://cloud.tencent.com/document/product/436/8282) 接口。有关 ACL 的详细说明，请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752)。
> - 该 API 的请求者需要对指定对象有写入 ACL 权限。
> 

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=PutObjectAcl&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 请求

#### 请求示例

**示例一**

```shell
PUT /<ObjectKey>?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: 0
Authorization: Auth String
```

**示例二**

```plaintext
PUT /<ObjectKey>?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Content-MD5: MD5
Authorization: Auth String



[Request Body]
```


>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

此接口无请求参数。

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| x-cos-acl | 定义对象的访问控制列表（ACL）属性。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中对象的预设 ACL 部分，例如 default，private，public-read 等，默认为 default<br>**注意：**如果您不需要进行对象 ACL 控制，请设置为 default 或者此项不进行设置，默认继承存储桶权限 | Enum | 否 |
| x-cos-grant-read | 赋予被授权者读取对象的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否 |
| x-cos-grant-read-acp | 赋予被授权者读取对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否 |
| x-cos-grant-write-acp | 赋予被授权者写入对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否 |
| x-cos-grant-full-control | 赋予被授权者操作对象的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否 |

#### 请求体

提交 **application/xml** 请求数据，包含对象所有者和完整的授权信息。

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

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| AccessControlPolicy | 无 | 包含 PUT Object acl 操作的所有请求信息 | Container | 是 |

**Container 节点 AccessControlPolicy 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| Owner | AccessControlPolicy | 对象持有者信息 | Container | 是 |
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 | Container | 是 |

**Container 节点 AccessControlPolicy.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| ID | AccessControlPolicy.Owner | 对象持有者的完整 ID，格式为`qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`<br>例如`qcs::cam::uin/100000000001:uin/100000000001` | string | 是 |

**Container 节点 AccessControlPolicy.AccessControlList 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| Grant | AccessControlPolicy.<br>AccessControlList | 单个授权信息，一个 AccessControlList 最多只能拥有100条 Grant | Container | 是 |

**Container 节点 AccessControlPolicy.AccessControlList.Grant 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| Grantee | AccessControlPolicy.<br>AccessControlList.Grant | 被授权者信息，`xsi:type`可指定为 Group 或 CanonicalUser，当指定为 Group 时子节点包括且仅允许包括 URI，当指定为 CanonicalUser 时子节点包括且仅允许包括 ID | Container | 是 |
| Permission | AccessControlPolicy.<br>AccessControlList.Grant | 授予的权限信息，枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E6.93.8D.E4.BD.9C-permission) 文档中对象的操作部分，例如 READ，FULL_CONTROL 等 | Enum | 是 |

**Container 节点 AccessControlPolicy.AccessControlList.Grant.Grantee 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| URI | AccessControlPolicy.<br>AccessControlList.Grant.Grantee | 预设用户组，请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E8.BA.AB.E4.BB.BD-grantee) 文档中预设用户组部分<br>例如`http://cam.qcloud.com/groups/global/AllUsers`或`http://cam.qcloud.com/groups/global/AuthenticatedUsers` | string | 当 Grantee 的`xsi:type`指定为 Group 时，必选 |
| ID | AccessControlPolicy.<br>AccessControlList.Grant.Grantee | 被授权者的完整 ID，格式为`qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`<br>例如`qcs::cam::uin/100000000001:uin/100000000001` | string | 当 Grantee 的`xsi:type`指定为 CanonicalUser 时，必选 |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：通过请求头设置 ACL

#### 请求

```shell
PUT /exampleobject?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 09 Sep 2019 13:11:09 GMT
x-cos-acl: public-read
x-cos-grant-read-acp: id="100000000002"
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1568034669;1568041869&q-key-time=1568034669;1568041869&q-header-list=content-length;date;host;x-cos-acl;x-cos-grant-read-acp&q-url-param-list=acl&q-signature=43faf0a3231435a922e16526709c281a537d****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Mon, 09 Sep 2019 13:11:10 GMT
Server: tencent-cos
x-cos-request-id: NWQ3NjRmNmRfZjZjMjBiMDlfMmE5MWJfMTI3OWZh****
```

#### 案例二：通过请求体设置 ACL

#### 请求

``` shell
PUT /exampleobject?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 10 Sep 2019 06:32:02 GMT
Content-Type: application/xml
Content-Length: 594
Content-MD5: zUPEBc1TeGrqTqEfPV7rxg==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1568097122;1568104322&q-key-time=1568097122;1568104322&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=acl&q-signature=edab1b68ce0f747604906354afbe5702b24c****
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
Date: Tue, 10 Sep 2019 06:32:02 GMT
Server: tencent-cos
x-cos-request-id: NWQ3NzQzNjJfZmVhODBiMDlfMjc5MGVfMTM4OTky****
```
