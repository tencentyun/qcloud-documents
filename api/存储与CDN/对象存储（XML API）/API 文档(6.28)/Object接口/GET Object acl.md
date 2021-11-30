## 功能描述

GET Object acl 接口用来获取对象的访问控制列表（ACL）。该 API 的请求者需要对指定对象有读取 ACL 权限。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=GetObjectAcl&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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

```shell
GET /<ObjectKey>?acl HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含对象所有者和完整的授权信息。

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

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| AccessControlPolicy | 无 | 保存 GET Object acl 结果的所有信息 | Container |

**Container 节点 AccessControlPolicy 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Owner | AccessControlPolicy | 对象持有者信息 | Container |
| AccessControlList | AccessControlPolicy | 被授权者信息与权限信息 | Container |

**Container 节点 AccessControlPolicy.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ID | AccessControlPolicy.Owner | 对象持有者的完整 ID，格式为`qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`<br>例如`qcs::cam::uin/100000000001:uin/100000000001` | string |
| DisplayName | AccessControlPolicy.Owner | 对象持有者的名字 | string |

**Container 节点 AccessControlPolicy.AccessControlList 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Grant | AccessControlPolicy.AccessControlList | 单个授权信息 | Container |

**Container 节点 AccessControlPolicy.AccessControlList.Grant 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Grantee | AccessControlPolicy.AccessControlList.Grant | 被授权者信息，`xsi:type`为 Group 或 CanonicalUser，当为 Group 时子节点包括且仅包括 URI，当指定为 CanonicalUser 时子节点包括且仅包括 ID 和 DisplayName | Container |
| Permission | AccessControlPolicy.AccessControlList.Grant | 授予的权限信息，枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E6.93.8D.E4.BD.9C-permission) 文档中对象的操作部分，例如 READ，FULL_CONTROL 等 | Enum |

**Container 节点 AccessControlPolicy.AccessControlList.Grant.Grantee 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| URI | AccessControlPolicy.AccessControlList.Grant.Grantee | 预设用户组，请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E8.BA.AB.E4.BB.BD-grantee) 文档中预设用户组部分<br>例如`http://cam.qcloud.com/groups/global/AllUsers`或`http://cam.qcloud.com/groups/global/AuthenticatedUsers` | string |
| ID | AccessControlPolicy.AccessControlList.Grant.Grantee | 被授权者的完整 ID，格式为`qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`<br>例如`qcs::cam::uin/100000000001:uin/100000000001` | string |
| DisplayName | AccessControlPolicy.AccessControlList.Grant.Grantee | 被授权者的名字 | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
GET /exampleobject?acl HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 10 Sep 2019 08:29:26 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1568104166;1568111366&q-key-time=1568104166;1568111366&q-header-list=date;host&q-url-param-list=acl&q-signature=207b3066eaf73a81d80cf12bf9db594a1172****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 742
Connection: close
Date: Tue, 10 Sep 2019 08:29:26 GMT
Server: tencent-cos
x-cos-request-id: NWQ3NzVlZTZfYmIwMmEwOV83YTQ5XzEzNTcx****

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
			<Permission>READ_ACP</Permission>
		</Grant>
	</AccessControlList>
</AccessControlPolicy>
```
