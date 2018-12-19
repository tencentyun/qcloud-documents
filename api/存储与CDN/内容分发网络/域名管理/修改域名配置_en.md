## API Description
This API (**UpdateCdnConfig**) is used to modify the configuration information of accelerated domain names.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Notes:** 

+ You can only modify the configuration information of one domain name at a time.
+ You can modify multiple configuration information of a specified domain name at a time.
+ Calling the API can reach 100 times/min at most.

**Supported Configuration:**

+ Modify origin server configuration
+ Modify slave server information
+ Modify original-pull host
+ Enable/disable "Ignore query string"
+ Modify refer blacklist/whitelist configuration
+ Modify IP blacklist/whitelist configuration
+ Enable/disable video dragging
+ Modify cache expiration time configuration
+ Enable/disable advanced cache expiration configuration
+ Enable/disable intermediate server configuration
+ Configure capped bandwidth
+ Set response header
+ Set request header

[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters
The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is UpdateCdnConfig.

| Parameter Name | Required | Type | Description |
| -------------- | ---- | ------ | ---------------------------------------- |
| hostId | No | Int | The ID of domain name to be modified |
| host | No | String | The domain name to be modified |
| origin | no | String | Origin server configuration. You can configure one domain name or multiple origin server IPs<br/>Available port range: 0-65535 <br/>Domain name mode: ```www.test.com:8080```<br/>IP mode: 1.1.1.1:8080, 2.2.2.2:8080 |
| backupOrigin | no | String | Backup origin server configuration. You can configure one domain name or multiple origin server IPs<br/>Available port range: 0-65535<br/>Domain name mode: ```www.test.com:8080```<br/>IP mode: 1.1.1.1:8080, 2.2.2.2:8080 |
| fwdHost | No | String | Origin-pull Host, which is the parameter "host" in the HTTP header sent from CDN node to origin. |
| fullUrl | No | String | "Ignore Query String" configuration<br/>"on": Disable<br/>"off": Enable |
| refer | No | String | Hotlink protection configuration. For more information, please see the description below |
| accessIp | No | String | IP blacklist/whitelist configuration. For more information, please see the description below |
| videoSwitch | No | String | Video dragging configuration<br/>"on": Enable <br/>"off": Disable |
| cache | No | String | Cache expiration time configuration. For more information, please see the description below |
| cacheMode | No | String | Cache mode setting<br/>"simple": Cache completely depends on the console<br/>"custom": Cache depends on the cache expiration time set by the console and the minimum value in max-age set by origin server |
| middleResource | No | String | Intermediate server configuration<br/>"on": Enable<br/>"off": Disable |
| capping | No | String | Capped bandwidth setting. For more information, please see the description below |
| rspHeader | No | String | Response Header setting. For more information, please see the description below |
| reqHeader | No | String | Request Header settings. For more information, please see the description below |

### Descriptions of "refer", "accessIp", "cache", "capping", "rspHeader" and "reqHeader"

#### refer

**Sample Parameters** 

```
[1,["qq.baidu.com", "*.baidu.com"],1]
```

The first field specifies the type of refer:

- 0: Do not set hotlink protection
- 1: Set blacklist
- 2: Set whitelist

The second field is the specific list. The third field indicates whether to include blank "refer":

- 1: Include blank "refer"
- 0: Do not include blank "refer"

#### accessIp

**Sample Parameters** 

```
{"type":1,"list":["1.2.3.4","2.3.4.5"]}
```

The first parameter "type" indicates the blacklist/whitelist type:

- 1: Blacklist
- 2: Whitelist

The second parameter "list" indicates the corresponding blacklist IP list. IP address ranges can be configured in the following formats: /8, /16, /24.

A maximum of 100 and 50 IPs can be configured in a blacklist and a whitelist, respectively.

#### cache

**Sample Parameters** 

```
[[0,"all",1000],[1,".jpg;.js",2000],[2,"/www/html",3000],[3,"/www/1.html",1000]]
```

The first parameter indicates the cache type. Four types are available:

- 0: All types. This means all files are matched. This is the default cache configuration.
- 1: File type. This means matching files based on filename extensions.
- 2: Folder type. This means matching based on directories.

The second parameter specifies the matching rule:

- 0: Always entered with "all".
- 1: Suffix, such as .jps,.js, separated with ";".
- 2: Directory, such as /www/html, /www/anc/, separated with ";".
- 3: Full path, such as /www/1.html, /www/2.html, separated with ";".

The third parameter specifies the cache expiration time (in seconds).

"cache" is ranked according to the rule sequence in priority order (from top to bottom).

#### capping

**Sample Parameters**

```
{"bandwidth":1000000, "unit":"K", "overflow":"origin", "active":"yes"}
```

Description:

+ bandwidth: Capped bandwidth value (in Bps)
+ uint: The unit displayed on the console. Convert the above values (Bps) to other units. K means Kbps, M means Mbps, G means Gbps and T means Tbps.
+ overflow: A response is returned when the threshold is exceeded. "origin": Return to origin server in full volume. "404": 404 is returned for all requests.
+ active: "yes": "capping" is enabled. "no": "capping" is disabled.

#### rspHeader

**Sample Parameters** 

```
{"Content-Language":"zh_CN","Access-Control-Allow-Origin":"https://www.test.com"}
```

Response Header only supports the following header settings:

- Content-Disposition
- Content-Language
- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Max-Age
- Access-Control-Expose-Headers

According to HTTP protocol, Access-Control-Allow-Origin can only be set as "*" or a domain name (with a header of http:// or https://), and "value" cannot exceed 1,000 Bytes.

#### reqHeader

**Sample Parameters** 

```
{"cdn":"tencent"}
```

"value" cannot exceed 1,000 Bytes.

## Output Parameters

| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed.<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error message or error code at business side.<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |

## Example

### Sample Parameters

```
host: www.test.com
reqHeader: {"cdn":"tencent"}
```

### GET Request

For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=UpdateCdnConfig
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462872270
&Nonce=541116052
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
&reqHeader=%7B%22cdn%22%3A%22tencent%22%7D
```

### POST Request

For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'UpdateCdnConfig',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462872294,
  'Nonce' => 479724541,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'host' => 'www.test.com',
  'reqHeader' => '{"cdn":"tencent"}'
)
```


### Example of Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success"
}
```

```json
{
    "code": 4000,
    "message": "(9175) Deploying status cdn host in progress[host in progress]",
    "codeDesc": "UserRequestError"
}
```

