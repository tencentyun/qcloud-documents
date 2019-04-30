## Description

 This API is used to modify the existing shipping task. When using this API, you need to manually grant CLS the permission to write to the specified bucket.

## Request

### Request example
 
 ```
 PUT /shipper HTTP/1.1
 Host: <Region>.cls.myqcloud.com
 Authorization: <AuthorizationString>
 Content-Type: application/json
 {
   "shipper_id": "xxxx-xx-xx-xx-xxxxxxxx",
   "bucket": "test-1250000001",
   "prefix": "test",
   "shipper_name": "myname",
   "interval": 300,
   "max_size": 256,
   "effective": true,
   "partition": "%Y%m%d",
     "compress": {
         "format": "none"
     },
     "content": {
         "format": "json",
     },
   "filter_rules": [{
     "key": "",
     "regex": "",
     "value": ""
   }]
 }
 ```
 
### Request line
 
 ```
 PUT /shipper
 ```
 
### Request header
 
 No special request header is used except for the common header.

### Request parameters

 | Field Name | Type | Location | Required | Description |
 | ------------ | ------ | ---- | ---- | ------------------------------------------------------------ |
 | shipper_id   | string | body | Yes | Modified shipping task ID |
 | bucket       | string | body | No | New bucket for the shipping task. Format: {bucketName}-{appid} |
 | prefix       | string | body | No | Prefix of the new directory of the shipping task |
 | shipper_name | string | body | No | Shipping rule name |
 | interval     | int    | body | No | Interval between shipping tasks (in sec). Default is 300. Value range: 60-3600 |
 | max_size     | int    | body | No | The maximum size of a file to be shipped (in MB). Default is 256 MB. Value range: 100-10240 |
 | effective    | bool   | body | No | Indicates whether to enable Shipper |
 | filter_rules | array  | body | No | Rules for filtering logs to be shipped. Logs that match the rules are shipped. The relation between rules is `and`. The number of rules is limited to 5. If the array is left empty, all logs are shipped without filtering. |
 | partition    | string | body | No | Rules for partitioning logs to be shipped. `Strftime` can be used to define the presentation of time format. |
 | compress     | object | body | Yes | Compression configuration of logs to be shipped |
 | content      | object | body | Yes | Format configuration of logs to be shipped |

 Rule is composed as follows:

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

 > **Note:**
 >
 > At least one of the followings should be provided: bucket, prefix, shipper_name, interval, max_size, effective, filter_rules, and compress.

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

