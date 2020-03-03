## Description

This API is used to get the details of a specified index policy.

## Request

### Request example

```
GET /index?topic_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /index
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|---------------|--------|-------|---------|---------------------------|
| topic_id      | string | query | Yes | ID of the topic to which the index to be queried belongs |

### Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 153

{
  "topic_id": "yyyy-yy-yy-yy-yyyyyyyy",
  "effective": true,
  "rule": {
    "full_text": {
      "case_sensitive": false
    },
    "key_value": {
      "case_sensitive": false,
      "keys": ["age","name"],
      "types": ["long","text"]
    }
  }
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| topic_id   | string | Yes | ID of the topic to which index rules belong |
| effective  | bool   | Yes | Indicates whether to enable the task |
| rule       | object | No | Index rule, which is returned if effective is true. |

rule is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| full_text  | object | No | Configuration for full-text index |
| key_value  | object | No | Configuration for key-value index |

full_text is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| case_sensitive | bool | Yes | Indicates whether it is case-sensitive |

Key_value is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| case_sensitive | bool | Yes | Indicates whether it is case-sensitive |
| keys | array(string) | Yes | Keys for which an index needs to be created |
| types| array(string) | Yes | Types of the above keys. A type corresponds to a key. Only ```long double text``` is supported. |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

