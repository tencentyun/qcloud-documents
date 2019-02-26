## Description

This API is used to modify an existing index task.

## Request

### Request example

```
PUT /index HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>
Content-Type: application/json

{
  "topic_id": "xxxx-xx-xx-xx-xxxxxxxx",
  "effective": true,
  "rule": {
    "full_text": {
      "case_sensitive": false,
      "tokenizer": "{^&%"
    },
    "key_value": {
      "case_sensitive": false,
      "keys": ["age","name"],
      "types": ["long","text"],
      "tokenizers": ["","-"]
    }
  }
}

```

### Request line

```
PUT /index
```

### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|------|--------|-----------------------------------------------|
| topic_id     | string | body | Yes | ID of the topic to which the index to be modified belongs |
| effective    | bool   | body | Yes | Indicates whether to enable index |
| rule         | object | body | No | Index rule, which is required if effective is true. |


rule is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| full_text  | object | No | Configuration for full-text index |
| key_value  | object | No | Configuration for key-value index |
> **Note:**
>
> When setting rules, at least one of full_text or key_value should be specified.

full_text is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| case_sensitive | bool | Yes | Indicates whether it is case-sensitive |
| tokenizer | string | No | Delimiter for full-text index |

Key_value is composed as follows:

| Field Name | Type | Required | Description |
|------------|--------|---------|-------------------------------|
| case_sensitive | bool | Yes | Indicates whether it is case-sensitive |
| keys | array(string) | Yes | Keys for which an index needs to be created |
| types| array(string) | Yes | Types of keys for which an index needs to be created. A type corresponds to a key. Only ```long double text``` is supported |
| tokenizers| array(string) | No | Delimiters of the above keys. A word separator correspond to a key. This is only applicable to ```text``` type, and other types are empty strings. |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 0

```

### Response header

No special response header is used except for the common response header.

### Response parameters

None

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).

