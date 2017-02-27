## 功能描述

使用API写入Bucket的ACL表，您可以通过Header：『x-cos-acl』『x-cos-grant-read』『x-cos-grant-write』『x-cos-grant-full-control』传入ACL信息，也可以通过body以XML格式传入ACL信息，但是只能**选择`Header`和`Body`其中一种**，否则返回冲突。

Put Bucket ACL是一个覆盖操作，传入新的ACL将覆盖原有ACL。只有所有者有权操作。

『x-cos-acl』：枚举值为public-read，private；public-read意味这个Bucket有公有读私有写的权限，private意味这个Bucket有私有读写的权限。

『x-cos-grant-read』：意味被赋予权限的用户拥有该Bucket的读权限

『x-cos-grant-write』：意味被赋予权限的用户拥有该Bucket的写权限

『x-cos-grant-full-control』：意味被赋予权限的用户拥有该Bucket的读写权限


## 请求

### 请求语法


```http
PUT /?acl Http/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Content-Type:application/xml
Content-MD5:MD5
x-cos-acl: [对应权限]
x-cos-grant-read: uin="",uin=""
x-cos-grant-write: uin="",uin=""
x-cos-grant-full-control: uin="",uin=""
Authorization: Auth String
```

### 请求参数

无特殊请求参数

### 请求头部

#### 权限相关头部

| 参数名称                     | 描述                                       | 类型     | 必选   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | 定义Bucket的ACL属性，有效值：private, public-read，默认值：private | String | 否    |
| x-cos-grant-read         | 赋予被授权者读的权限，格式x-cos-grant-read: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| x-cos-grant-write        | 赋予被授权者写的权限，格式x-cos-grant-write: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |
| x-cos-grant-full-control | 赋予被授权者读写权限，格式x-cos-grant-full-control: uin=" ",uin=" "<Br/> 当需要给子账户授权时，uin="RootAcountID/SubAccountID"，当需要给根账户授权时，uin="RootAcountID" | String | 否    |

### 请求内容

| 参数名称                | 描述                                       | 类型        |
| ------------------- | ---------------------------------------- | --------- |
| AccessControlPolicy | 一条独立的ACL记录                               | Container |
| Owner               | 标识资源的所有者                                 | Container |
| uin                 | 用户QQ号                                    | String    |
| Subacount           | 子账户QQ账号                                  | String    |
| AccessControlList   | 被授权者信息与权限信息                              | Container |
| Grant               | 单条授权信息，每个AccessControlList可以拥有100条Grant  | Container |
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

## 返回值

### 返回头部

无特殊返回头部，其他返回值请参见公共返回头部

### 返回内容

无返回内容

## 示例

### 请求

```HTTP
PUT /?acl HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484724784;32557620784&q-key-time=1484724784;32557620784&q-header-list=host&q-url-param-list=acl&q-signature=785d9075b8154119e6a075713c1b9e56ff0bddfc
Content-Length: 229
Content-Type: application/x-www-form-urlencoded

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

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed Jan 18 15:41:31 2017
Server: tencent-cos
x-cos-request-id: NTg3ZjFjMmJfOWIxZjRlXzZmNDhfMjIw
```

