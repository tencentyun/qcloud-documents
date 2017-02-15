## 功能描述
Put Bucket Tagging接口实现给用指定Bucket打标签。用来组织和管理相关Bucket。当该请求设置相同Key名称，不同Value时，会返回400。请求成功，则返回204。

## 请求

### 请求语法

```HTTP
PUT /?tagging HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Content-Type:application/xml
Authorization: Auth

[XML]
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

| 名称      | 描述                          | 类型        | 必选   |
| ------- | --------------------------- | --------- | ---- |
| Tagging | 说明所有TagSet和Tag的信息           | Contianer | 是    |
| TagSet  | 说明一系列的Tag信息<br/>父节点：Tagging | Contianer | 是    |
| Tag     | 说明单个的Tag信息<br/>父节点：TagSet   | Contianer | 是    |
| Key     | Tag的类别名称<br/>父节点：Tag        | String    | 是    |
| Value   | Tag的值<br/>父节点：Tag           | String    | 是    |

```xml
<Tagging>
  <TagSet>
    <Tag>
      <Key></Key>
      <Value></Value>
    </Tag>
    <Tag>
      ...
    </Tag>
  </TagSet>
</Tagging>
```

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容

## 示例
### 请求
```xml
PUT /?tagging HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817032;32557713032&q-key-time=1484817032;32557713032&q-header-list=host&q-url-param-list=tagging&q-signature=0a99e59b753c26b807e4b372560b0d026d26af26
Content-Type:application/xml
Content-Length: 75

<Tagging>
  <TagSet>
    <Tag>
      <Key>1</Key>
      <Value>2</Value>
    </Tag>
  </TagSet>
</Tagging>
```
### 返回
```xml
HTTP/1.1 204
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 17:12:29 2017
Server: tencent-cos
x-cos-request-id: NTg4MDgyZmRfOTkxZjRlXzEwNjRfZWI2

```

