## Description
Use API to read the ACL (Access Control List) of a Bucket. Only the Bucket owner is allowed to perform the action.

## Request

### Request Syntax

```http
GET /?acl Http/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

#### Required Headers

| Parameter Name          | Description   | Type     | Required   |
| ------------- | ---- | ------ | ---- |
| Authorization | Signature string  | String | Yes    |

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

| Parameter Name                | Description                                       | Type        |
| ------------------- | ---------------------------------------- | --------- |
| AccessControlPolicy | An independent ACL record                               | Container |
| Owner               | Owner of the identified resource                                  | Container |
| uin                 | User's QQ ID                                    | String    |
| Subacount           | QQ ID of the sub-account                                  | String    |
| AccessControlList   | Information of grantees and permissions                              | Container |
| Grant               | A single authorization information entry. Each AccessControlList can contain 100 Grant entries | Container |
| Grantee             | Resource information of authorized account. Type can be RootAcount or SubAccount. For type of RootAcount, you may enter either a QQ ID or "anonymous"(which represents users of all types) for UIN. For type of RootAcount, UIN represents root account, SubAccount represents sub account | Container |
| Permission          | Permission information, enumerated values include READ, WRITE, FULL_CONTROL         | String    |

```XML
<AccessControlPolicy>
  <Owner>
    <uin>ID</uin>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee type="SubAccount">
        <uin>ID</uin>
        <Subaccount> SUBID </Subaccount>
      </Grantee>
      <Permission>Permission</Permission>
    </Grant>
    <Grant>
      <Grantee type="RootAccount">
        <uin>ID</uin>
      </Grantee>
      <Permission>Permission</Permission>
    </Grant>
    <Grant>
      ...
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

## Example

### Request

```HTTP
GET /?acl HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b40652
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 266
Connection: keep-alive
Date: Thu Jan 12 17:23:49 2017
Server: tencent-cos
x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZmNw==

<AccessControlPolicy>
	<Owner>
		<uin>2779643970</uin>
	</Owner>
	<AccessControlList>
		<Grant>
			<Grantee type="RootAccount">
				<uin>2779643970</uin>
			</Grantee>
			<Permission>FULL_CONTROL</Permission>
		</Grant>
	</AccessControlList>
</AccessControlPolicy>
```
