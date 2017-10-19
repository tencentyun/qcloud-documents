## 功能描述

Add Tags To Vault请求实现为文件库添加标签。每个标签由一个键和一个值组成。每个文件库可最多有 50 个标签。如果请求过多标签导致超出文件库的标签限制，则返回 `LimitExceededException` 错误。

如果在文件库上的某个指定键的下面已存在一个标签，则将覆盖现有的键值。

请求成功则返回 204 No Content

## 请求

### 请求语法

```HTTP
POST /<UID>/vaults/<VaultName>/tags?operation=add HTTP 1.1
Host:cas.<Region>.myqcloud.com
Date:date
Authorization: Auth

{
   "Tags": 
      {
         "string": "string",
         "string": "string",
         ...
      }        
}
```

### 请求参数

| 名称            | 描述                                | 类型     | 必选   |
| ------------- | --------------------------------- | ------ | ---- |
| operation=add | 带有 add 值的operation参数，用于与删除标签进行区分。 | String | 是    |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

| 名称   | 描述                                       | 类型              | 必选   |
| ---- | ---------------------------------------- | --------------- | ---- |
| Tags | 要添加到文件库的标签。每个标签由一个键和一个值组成。该值可为空字符串。其中的String取值1-10个字符。 | String到String映射 | 是    |

```JSON
{
   "Tags": 
      {
         "string": "string",
         "string": "string",
        ...
      }        
}
```
## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容



