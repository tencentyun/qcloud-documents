## Description

Get Object ACL allows the API to read the ACL list of an Object. Only the Object owner is allowed to perform the action.

## Request

### Request Syntax

```http
GET /ObjectName?acl Http/1.1
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

No particular response headers. Please refer to "Common Response Headers" for other headers.

### Response Content

| Parameter Name                | Description                                       | Type        |
| ------------------- | ---------------------------------------- | --------- |
| AccessControlPolicy | An independent ACL record                               | Container |
| Owner               | Owner of the identified resource                                  | Container |
| uin                 | User's QQ ID                                    | String    |
| Subacount           | QQ ID of the sub-account                                  | String    |
| AccessControlList   | Information of authorized account and permissions                              | Container |
| Grant               | A single authorization information entry. Each AccessControlList can contain 100 Grant entries | Container |
| Grantee             | Resource information of authorized account. Type can be RootAcount or SubAccount. For type of RootAcount, you may enter either a QQ ID or "anonymous"(which represents all user types) for UIN. For type of RootAcount, UIN represents root account, and SubAccount represents sub account | Container |
| Permission          | Permission information, enumerated values: READ, WRITE, FULL_CONTROL         | String    |

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
GET /ObjectName?acl HTTP/1.1
Host:zuhaotestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484641748;32557537748&q-key-time=1484641748;32557537748&q-header-list=host&q-url-param-list=acl&q-signature=79a3cb15cd1a2a2b6d567d78c7e8f9cd895bde21
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 266
Date: Tue Jan 17 16:30:03 2017
x-cos-request-id: NTg3ZGQ2MGJfNDQyMDRlXzE3YTdfMjk3

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


