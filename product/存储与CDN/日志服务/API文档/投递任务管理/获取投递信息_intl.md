## Description
<<<<<<< HEAD

This API is used to obtain the details of a specified shipping policy.

## Request

### Request example

```
GET /shippers?topic_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
Host: <Region>.cls.myqcloud.com
Authorization: <AuthorizationString>

```

### Request line

```
GET /shippers
```
### Request header

No special request header is used except for the common header.

### Request parameters

| Field Name | Type | Location | Required | Description |
|--------------|--------|-------|---------|---------------------------|
| topic_id     | string | query | Yes | ID of the topic to which the shipping task to be queried belongs |
| offset         | int     | query | No | Starting point for query. Default is 0. |
| count          | int     | query | No | Number of shipping tasks to be queried. Default is 50, and maximum is 1,000. |

## Response

### Response example

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 123
{
  "shippers": [
  {
    "shipper_id": "xxxx-xx-xx-xx-xxxxxxxx",
    "topic_id": "yyyy-yy-yy-yy-yyyyyyyy",
    "bucket": "test-1250000001",
    "prefix": "test",
    "shipper_name": "myname",
    "interval": 300,
    "max_size": 256,
    "effective": true,
    "filter_rules": [{
      "key": "",
      "regex": "",
      "value": ""
    }],
    "partition": "%Y%m%d",
    "compress": {
        "format": "none"
    },
    "content": {
        "format": "json",
    },
    "create_time": "2017-12-12 12:12:12"
  }
  ]
}
```

### Response header

No special response header is used except for the common response header.

### Response parameters

| Field Name | Type | Required | Description |
|-------------|-----------|---------|-------------------------------|
| shippers    | JsonArray | Yes | Array of shipping information |

ShipperInfo is composed as follows:

| Field Name | Type | Required | Description |
| ------------ | ------ | ---- | ------------------------------------------------ |
| shipper_id   | string | Yes | Shipping rule ID |
| topic_id     | string | Yes | ID of the topic to which shipping rules belong |
| bucket       | string | Yes | Address of the bucket to which logs are shipped |
| prefix       | string | Yes | The prefix directory for shipping |
| shipper_name | string | Yes | Shipping rule name |
| interval     | int    | Yes | Interval between shipping tasks (in sec) |
| max_size     | int    | Yes | The maximum size of a file to be shipped (in MB) |
| effective    | bool   | Yes | Indicates whether to enable the task |
| filter_rules | object | Yes | Rules for filtering logs to be shipped |
| create_time  | string | Yes | Time when the log to be shipped is created |
| partition    | string | Yes | Rules for partitioning logs to be shipped. `Strftime` can be used to define the presentation of time format. |
| compress     | object | No | Compression configuration of logs to be shipped |
| content      | object | No | Format configuration of logs to be shipped |

filter_rules is composed as follows:

| Field Name | Type | Required | Description |
| ------ | ------ | ---- | ----------------------------------------------------- |
| key    | string | Yes | The key used for comparison. `__CONTENT__` means full text. |
| regex  | string | Yes | The regular expression used to extract the comparison content |
| value  | string | Yes | The value used to compare with the content extracted by using the above regex. The rule is hit if they are consistent. |

compress is composed as follows:

| Field Name | Type | Required | Description |
| ------ | ------ | ---- | ------------------------------------------ |
| format | string | Yes | Compression format, including `gzip`, `lzop` and `none` (do not compress) |

content is composed as follows:

| Field Name | Type | Required | Description |
| ------ | ------ | ---- | -------------------- |
| format | string | Yes | Content format, which supports `json` |

## Error Codes

See [Error Codes](https://cloud.tencent.com/document/product/614/12402).
=======
 
 This API is used to obtain the details of a specified shipping policy.
 
## Request
 
### Request example
 
 ```
 GET /shippers?topic_id=xxxx-xx-xx-xx-xxxxxxxx HTTP/1.1
 Host: <Region>.cls.myqcloud.com
 Authorization: <AuthorizationString>
 
 ```
 
### Request line
 
 ```
 GET /shippers
 ```
### Request header
 
 No special request header is used except for the common header.
 
### Request parameters
 
 | Field Name | Type | Location | Required | Description |
 |--------------|--------|-------|---------|---------------------------|
 | topic_id     | string | query | Yes | ID of the topic to which the shipping task to be queried belongs |
 | offset         | int     | query | No | Starting point for query. Default is 0. |
 | count          | int     | query | No | Number of shipping tasks to be queried. Default is 50, and maximum is 1,000. |
 
## Response
 
### Response example
 
 ```
 HTTP/1.1 200 OK
 Content-Type: application/json
 Content-Length: 123
 {
   "shippers": [
   {
 @@ -55,6 +54,13 @@ Content-Length: 123
       "regex": "",
       "value": ""
     }],
     "partition": "%Y%m%d",
     "compress": {
         "format": "none"
     },
     "content": {
         "format": "json",
     },
     "create_time": "2017-12-12 12:12:12"
   }
   ]
 }
 ```
 
### Response header
 
 No special response header is used except for the common response header.
 
### Response parameters

 | Field Name | Type | Required | Description |
 |-------------|-----------|---------|-------------------------------|
 | shippers    | JsonArray | Yes | Array of shipping information |

 ShipperInfo is composed as follows:  
 
 | Field Name | Type | Required | Description |
 | ------------ | ------ | ---- | ------------------------------------------------ |
 | shipper_id   | string | Yes | Shipping rule ID |
 | topic_id     | string | Yes | ID of the topic to which shipping rules belong |
 | bucket       | string | Yes | Address of the bucket to which logs are shipped |
 | prefix       | string | Yes | The prefix directory for shipping |
 | shipper_name | string | Yes | Shipping rule name |
 | interval     | int    | Yes | Interval between shipping tasks (in sec) |
 | max_size     | int    | Yes | The maximum size of a file to be shipped (in MB) |
 | effective    | bool   | Yes | Indicates whether to enable the task |
 | filter_rules | object | Yes | Rules for filtering logs to be shipped |
 | create_time  | string | Yes | Time when the log to be shipped is created |
 | partition    | string | Yes | Rules for partitioning logs to be shipped. `Strftime` can be used to define the presentation of time format. |
 | compress     | object | No | Compression configuration of logs to be shipped |
 | content      | object | No | Format configuration of logs to be shipped |

 filter_rules is composed as follows:

 | Field Name | Type | Required | Description |
 | ------ | ------ | ---- | ----------------------------------------------------- |
 | key    | string | Yes | The key used for comparison. `__CONTENT__` means full text. |
 | regex  | string | Yes | The regular expression used to extract the comparison content |
 | value  | string | Yes | The value used to compare with the content extracted by using the above regex. The rule is hit if they are consistent. |

 compress is composed as follows:

 | Field Name | Type | Required | Description |
 | ------ | ------ | ---- | ------------------------------------------ |
 | format | string | Yes | Compression format, including `gzip`, `lzop` and `none` (do not compress[AD1]) |

 content is composed as follows:

 | Field Name | Type | Required | Description |
 | ------ | ------ | ---- | -------------------- |
 | format | string | Yes | Content format, which supports `json` |

## Error Codes

 See [Error Codes](https://cloud.tencent.com/document/product/614/12402).
>>>>>>> 72cd0d02b3bd961f15f1a89abc26e00761d972e3

[AD1]1
