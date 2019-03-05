## 功能描述

List Tags For Vault请求实现列出已添加到文件库的所有标签，如无，返回空串

请求成功则返回 200 OK

## 请求

### 请求语法

```HTTP
GET /<UID>/vaults/<VaultName>/tags HTTP 1.1
Host:cas.<Region>.myqcloud.com
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

| 名称   | 描述                                       | 类型              |
| ---- | ---------------------------------------- | --------------- |
| Tags | 已添加到文件库的标签。每个标签由一个键和一个值组成。该值可为空字符串。其中的String取值1-10个字符。 | String到String映射 |

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



