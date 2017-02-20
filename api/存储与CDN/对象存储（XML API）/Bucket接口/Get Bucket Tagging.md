## 功能描述
Get Bucket Tagging接口实现获取指定Bucket的标签。

## 请求

### 请求语法

```HTTP
GET /?tagging HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称      | 描述                           | 类型        |
| ------- | ---------------------------- | --------- |
| Tagging | 说明所有TagSet和Tag的信息            | Contianer |
| TagSet  | 说明一系列的Tag信息<br/>父节点：Tagging  | Contianer |
| Tag     | 说明单个的Tag信息<br/>父节点：TagSetTag | Contianer |
| Key     | Tag的类别名称<br/>父节点：Tag         | String    |
| Value   | Tag的值<br/>父节点：Tag            | String    |

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
