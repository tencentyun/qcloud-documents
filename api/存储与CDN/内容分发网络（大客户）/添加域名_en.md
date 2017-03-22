## 1. API Description

This API is used to add CDN accelerated domain.

Domain for API request:<font style="color:red">cdn.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to [Common Request Parameters](https://www.qcloud.com/doc/api/231/4473). The Action field for this API is EAddCdnHost.

| Parameter Name    | Required | Type     | Description                                       |
| ------- | ----------- | ------ | -------------------- |
| host    | Yes    | String | Accelerated domain |
| origin | Yes | String | Set origin server. You may set a domain or multiple origin IPs (the type of "ip:port" can be used, such as 8.8.8.8:8080). The port number should be between 0 and 65535 (exclusive of 0). |
| projectId | Yes | Int | Project ID. [Click to View](https://console.qcloud.com/project) |
| hostType | Yes | String | Domain type. "cname" refers to self-owned origin, "ftp" refers to FTP origin |
| cache | No | json | Set cache expiration rule. For details, refer to the description later. |
| cacheMode | No | String | Caching mode. There are two modes: "simple" means cache completely depends on the cache expiration rule set in the Console; "custom" means cache depends on the cache expiration rule set in the Console and the minimum value of max-age output by origin server.  |
|  refer | No | json | Set hotlink protection. For details, refer to the description later |
| fwdHost | No | String | Origin host header |
| fullUrl | No | String | Whether to enable full-path caching. "on" means enabling it, "off" means disabling it. |
| middleResource | No | String | Whether to enable intermediate node. "on" means enabling it, "off" means disabling it. |


##### Configuring Cache Expiration Rule

Example of cache configuration:
```
[[0,"all",1000],[1,".jpg;.js",2000],[2,"/www/html",3000],[3,"/index.html;/test/*.jpg",3000]]
```
The first parameter is caching type:

There are four types:

+ 0: All. This means all files are matched. This is the default cache configuration;
+ 1: File type. This means matching files based on filename extensions;
+ 2: Folder type. This means matching files based on directories;
+ 3: Full-path file. This means matching files according to home page or matching a specified file.

The second parameter specifies matching rule:

+ 0: Always populated with "all" ;
+ 1: Suffix - for example, .jps;.js, separated with ";"
+ 2: Directory - for example, /www/html; /www/anc/, separated with ";"
+ 3: Full-path file - full path of resource, for example, /index.html;/test/*.jpg, separated with ";". Only * matching is supported.

The third parameter specifies cache expiration time (in seconds).

##### Configuring Hotlink Protection

Example:
```
[1,["qq.baidu.com", "*.baidu.com"]]
```

The first field specifies the type of refer:

+ 0:  No hotlink protection is configured;
+ 1: Configure blacklist;
+ 2: Configure whitelist;

The second field is the specific list.



## 3. Output Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on the Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | Error message or error code at business side.                           |
| data     | Object | host_id, the ID of added domain |


## 4. Example

### 4.1 Input Example

> host: www.test.com
> origin: 1.1.1.1
> projectId: 0
> hostType: cname
> fwdHost: www.test1.com

### 4.2 GET Request

For GET request, all the parameters are required to be appended to the URL:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=EAddCdnHost
&SecretId=XXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462416887
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXX
&host=www.test.com
&orgin=1.1.1.1
&projectId=0
&hostType=cname
&fwdHost=www.test1.com
```

### 4.3 POST Request

For POST request, the parameters need to be filled in the HTTP Request-body. Request address:

```
https://cdn.api.qcloud.com/v2/index.php
```

Formats such as form-data and x-www-form-urlencoded are supported for the parameters. The array of parameters is as follows:

```
array (
  'Action' => 'EAddCdnHost',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'host' => 'www.test.com',
  'origin' => '1.1.1.1',
  'projectId' => '0',
  'hostType' => 'cname',
  'fwdHost' => 'www.test1.com'
)

```

### 4.4 Example of Returned Result

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "host_id": 394565
    }
}
```
























