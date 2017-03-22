## 功能描述

Get Object ACL接口实现使用API读取Object的ACL表，只有所有者有权操作。

## 请求

### 请求语法

```http
GET /ObjectName?acl Http/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

#### 必选头部

| 参数名称          | 描述   | 类型     | 必选   |
| ------------- | ---- | ------ | ---- |
| Authorization | 签名串  | String | 是    |


### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 参数名称                | 描述                                       | 类型        |
| ------------------- | ---------------------------------------- | --------- |
| AccessControlPolicy | 一条独立的ACL记录                               | Container |
| Owner               | 标识资源的所有者                                 | Container |
| uin                 | 用户QQ号                                    | String    |
| Subacount           | 子账户QQ账号                                  | String    |
| AccessControlList   | 被授权者信息与权限信息                              | Container |
| Grant               | 单条授权信息，一个AccessControlList钟可以拥有100条Grant | Container |
| Grantee             | 被授权者资源信息，type类型可以为RootAcount， SubAccount；当type类型为RootAcount时，可以在UIN中填写QQ，也可以填写anonymous（指代所有类型用户）。当type类型为RootAcount时，UIN代表根账户账号，SubAccount代表子账户账号 | Container |
| Permission          | 权限信息，枚举值：READ，WRITE，FULL_CONTROL         | String    |

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

## 示例

### 请求

```HTTP
GET /ObjectName?acl HTTP/1.1
Host:zuhaotestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484641748;32557537748&q-key-time=1484641748;32557537748&q-header-list=host&q-url-param-list=acl&q-signature=79a3cb15cd1a2a2b6d567d78c7e8f9cd895bde21
```

### 返回

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

