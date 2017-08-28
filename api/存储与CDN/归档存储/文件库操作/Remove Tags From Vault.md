## 功能描述

Remove Tags From Vault请求实现从已附加到文件库的标签集中删除一个或多个标签

请求成功则返回 204 No Content

## 请求

### 请求语法

```HTTP
POST /<UID>/vaults/<VaultName>/tags?operation=remove HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth

{
   "TagKeys": 
      [
        "string": "string",
        "string": "string",
        ...
      ]
}
```

### 请求参数

| 名称               | 描述                                   | 类型     | 必选   |
| ---------------- | ------------------------------------ | ------ | ---- |
| operation=remove | 带有 remove 值的operation参数，用于与添加标签进行区分。 | String | 是    |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

| 名称      | 描述                                       | 类型       | 必选   |
| ------- | ---------------------------------------- | -------- | ---- |
| TagKeys | 要删除的文件库标签列表。每个标签由一个键和一个值组成。 列表中的键值对，可取值 1-10对 | String数组 | 是    |

```JSON
{
   "TagKeys": 
      [
        "string": "string",
        "string": "string",
        ...
      ]
}
```
## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容



