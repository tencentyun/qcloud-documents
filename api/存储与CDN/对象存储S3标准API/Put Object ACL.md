## 功能描述

使用API写入Object的ACL表，您可以通过Header：『x-cos-acl』『x-cos-grant-read』『x-cos-grant-write』『x-cos-grant-full-control』传入ACL信息，也可以通过body以XML格式传入ACL信息，但是只能选择Header和Body其中一种，不然返回冲突。

Put Object ACL是一个覆盖操作，传入新的ACL将覆盖原有ACL。

『x-cos-acl』：枚举值为public-read，private；public-read意味这个Object有公有读私有写的权限，private意味这个Object有私有读写的权限。

『x-cos-grant-read』：意味被赋予权限的用户拥有该Object的读权限

『x-cos-grant-write』：意味被赋予权限的用户拥有该Object的写权限

『x-cos-grant-full-control』：意味被赋予权限的用户拥有该Object的读写权限

| -          | Bucket维度                | Object维度                |
| ---------- | ----------------------- | ----------------------- |
| Read（读权限）  | GetBucket,HeadBucket    | GetObject, HeadObject   |
| Write（写权限） | PutBucket, DeleteBucket | PutObject, DeleteObject |

## 请求

### 请求语法

```http
PUT /ObjectName?acl Http/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
X-cos-acl: [对应权限]
X-cos-grant-read: uin="",uin=""
X-cos-grant-write: uin="",uin=""
X-cos-grant-full-control: uin="",uin=""
Authorization: Auth String
```

### 请求参数

无特殊请求参数

#### 必选头部

| 参数名称                | 是否必选 | 描述                                       |
| ------------------- | ---- | ---------------------------------------- |
| AccessControlPolicy | 是    | 一条独立的ACL记录                               |
| Owner               | 是    | 标识资源的所有者                                 |
| uin                 | 是    | 用户QQ号                                    |                                 |
| AccessControlList   | 是    | 被授权者信息与权限信息                              |
| Grant               | 是    | 单条授权信息，一个AccessControlList钟可以拥有100条Grant |
| Grantee             | 是    | 被授权者资源信息，type类型可以为RootAcount， SubAccount；当type类型为RootAcount时，可以在UIN中填写QQ，也可以填写anonymous（指代所有类型用户）。当type类型为RootAcount时，UIN代表根账户账号，SubAccount代表子账户账号 |
| Permission          | 是    | 权限信息，枚举值：READ，WRITE，FULL_CONTROL         |
|

#### 权限相关头部

| 参数名称                     | 是否必选 | 类型     | 描述                                       |
| ------------------------ | ---- | ------ | ---------------------------------------- |
| X-cos-acl                | 否    | String | 定义Object的ACL属性，有效值：private, public-read, public-read-write，默认值：private |
| X-cos-grant-read         | 否    | String | 赋予被授权者读的权限，格式X-cos-grant-read: uin=" ",uin=" " |
| X-cos-grant-write        | 否    | String | 赋予被授权者写的权限，格式X-cos-grant-write: uin=" ",uin=" " |
| X-cos-grant-full-control | 否    | String | 赋予被授权者读写权限，格式X-cos-grant-full-control: uin=" ",uin=" " |

### 请求内容

```xml
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

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容