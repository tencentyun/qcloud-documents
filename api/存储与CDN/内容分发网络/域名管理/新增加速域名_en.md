## API Description

**AddCdnHost** is used to add an accelerated domain name to Tencent Cloud CDN.

Domain name for API request: <font style="color:red">cdn.api.qcloud.com</font>

**Notes:**

+ The domain name to add must have never accessed to Tencent Cloud CDN.
+ The domain name to add must be licensed by MIIT. For more information, please see [Query ICP License](http://www.miitbeian.gov.cn/publish/query/indexFirst.action). 
+ Only one domain name can be added to Tencent Cloud CDN at a time.
+ To access a wildcard domain name, ownership verification is required, and the domain name cannot be accessed through this API.
+ The frequency of calling the API is limited to 100 times/min.

[View the example](https://cloud.tencent.com/document/product/228/1734)

## Input Parameters

The following request parameter list only provides the API request parameters. Common request parameters are required when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page. The Action field for this API is AddCdnHost.

| Parameter Name | Required | Type | Description |
| ----------- | ---- | ------ | ---------------------------------------- |
| host | Yes | String | The domain name to access CDN |
| projectId | Yes | String | Project ID, which is the ID of the project to which the domain name is to be added. [View Existing Projects and IDs](https://console.cloud.tencent.com/project) |
| hostType | Yes | String | The way to access a domain name. "cname" means the user uses his own origin server |
| origin | no | String | Origin server configuration. You can configure one domain name or multiple origin server IPs <br/>Available port range: 0-65535 <br/>Domain name mode: ```www.test.com:8080```<br/> IP mode: 1.1.1.1:8080, 2.2.2.2:8080 |
| serviceType | No | String | Acceleration type configuration<br/>"web": Static content acceleration<br/>"download": File downloading acceleration<br/>"media": Streaming media VOD acceleration<br/>If this field is left empty, it defaults to static content acceleration |
| fwdHost | No | String | Origin-pull domain name configuration. If this field is left empty, it defaults to be an accelerated domain name |
| cache | No | String | Cache expiration time configuration. For more information, please see the description below |

### Description of "cache"

#### cache

**Sample Parameters** 

```
[[0,"all",1000],[1,".jpg;.js",2000],[2,"/a;/www/b",3000],[3,"/a/1.html;/b/2.html",1000]]
```

Three parameters are provided for configuration of each cache expiration:

+  The first parameter indicates the cache type. Four types are optional:
  + 0: All types. This means all files are matched. This is the default cache configuration;
  + 1: File type. This means matching based on file extensions;
  + 2: Folder type. This means matching based on directories;
  + 3: Full-path match.
+  The second parameter specifies matching rules for cache types in the first parameter:
  + 0: "all" is entered in a fixed way. This means the matching rule is applicable to all files;
  + 1: Suffix, for example, .jps,.js, separated with ";";
  + 2: Directory, for example, /www/anc, /a/b, separated with ";";
  + 3: Full path, for example, /a/1.html, /b/2.html, separated with ";";
+  The third parameter represents the cache expiration time (in seconds)

Enter the rules from low to high priority.


## Output Parameters

| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: Successful; other values: Failed.<br/>For more information, please see [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |
| message  | String | Module error message description depending on API                           |
| codeDesc | String | Error message or error code at business side.<br/>For more information, please see [Business Error Codes](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Codes page. |

## Example

### Sample Parameters

```
host: www.test.com
projectId: 0
hostType: cname
origin: 8.8.8.8:8080
```


### GET Request


For a GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=AddCdnHost
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462440051
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
&projectId=0
&hostType=cname
&origin=8.8.8.8:8080
```

### POST Request
For a POST request, the parameters are input in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'AddCdnHost',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462868615,
  'Nonce' => 520585444,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'host' => 'www.test.com',
  'projectId' => '0',
  'hostType' => 'cname',
  'origin' => '8.8.8.8:8080'
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
    "message": "(20004) Not licensed cdn audit no icp [cdn audit no icp [The current domain has not been licensed by MIIT]]",
    "codeDesc": 20004
}

```








