## 1. API Description

The API (GetHostInfoByHost) is used to query domain details and configuration information based on domain names. You can query multiple domains at a time.

Domain name for API request:<font style="color:red">cdn.api.qcloud.com</font>

[Call Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. Refer to the [Common Request Parameters](https://cloud.tencent.com/doc/api/231/4473) page for details. The Action field for this API is GetHostInfoByHost.

| Parameter Name    | Required | Type     | Description                       |
| ------- | ---- | ------ | ------------------------ |
| hosts.n | Yes    | String | Host to be queried. You may query one or multiple hosts. |

#### Note

+ You may query one or multiple domains. When querying multiple domains, you can pass parameters like this:
```
hosts.0=www.test1.com&hosts.1=www.test2.com
```


## 3. Response Parameters

| Parameter Name     | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page.  |
| message  | String | Module error message description depending on API.                           |
| codeDesc | String | English error message or error code at business side.                           |
| data     | Array  | Result data, as described below                             |

#### data Field Description

| Parameter Name  | Type    | Description     |
| ----- | ----- | ------ |
| hosts | Array | Domain details array |
| total | Int   | Total number of domains   |

#### hosts Field Description

| Parameter Name            | Type     | Description                                       |
| --------------- | ------ | ---------------------------------------- |
| id              | Int    | ID after the domain is connected to CDN                         |
| app_id          | Int    | APPID of domain owner                             |
| owner_uin       | Int    | QQ ID of the user when logging in to Tencent Cloud                        |
| project_id      | Int    | Project ID of the domain                                |
| host            | String | Domain                                       |
| host_type       | String | Connection method. There are three modes: "cos" means the hosted origin when connecting the domain is COS origin; "cname" means self-owned origin is used when connecting the domain; "ftp" means FTP hosted origin provided by CDN is used when connecting the domain. |
| service_type    | String | Domain content type. There are three modes: "web" means it is static content; "download" means it is downloading content; "media" means it is media streaming content. |
| origin          | String | Origin server configuration corresponding to the domain                                 |
| cache           | Array  | Configuration of caching rules, as described below                           |
| status          | Int    | Domain state: "1" means the domain is in review; "2" means the domain is not approved ; "3" means the domain is approved and in deploying status; "4" means the domain is in deploying status; "5" means the domain is activated; "6" means the domain is closed. |
| disabled        | Int    | Indicate whether the domain is blocked; "0" indicates that the domain is not blocked.                 |
| message         | String | Domain status information, such as "Closed", "Activated" and "Deploying".             |
| enable_overseas | String | Indicate whether the overseas CDN is activated: "no" means the overseas CDN is not activated; "yes" means the overseas CDN is activated. |
| create_time     | String | Domain connection time                                   |
| update_time     | String | Last update time                                  |
| deleted         | String | Delete or not: "no" means the domain is not deleted; "yes" means the domain is deleted. |
| fwd_host_type   | String | Back-to-origin configuration type: "default" means the connected domain is the address for back-to-origin requests; "custom" means the domain uses customized address for back-to-origin requests.  |
| fwd_host        | String | Address for back-to-origin requests                                     |
| middle_resource | Int    | Configuration of intermediate node: "-1" means the domain has closed intermediate node services; "0" means the domain has activated intermediate node services. |
| refer           | Array  | Hotlink protection configuration, as described below                            |
| cname           | String | The accelerated domain with ".cdn.dnsv1.com" as suffix assigned by CDN            |
| cache_mode      | String | Type of caching rules: "simple" means cache completely depends on the Console; "custom" means cache depends on the cache expiration time set by the Console and the minimum value in max-age set by origin server. |
| furl_cache      | String | Filter parameter: "on" means to enable; "off" means to disable          |
| ssl_type        | Int    | Indicate whether to activate HTTPS: "0" means HTTPS configuration is not activated; others means HTTPS configuration is activated. |
| bucket_name     | String | bucket name corresponding to the COS origin                     |
| ssl_deploy_time | String | SSL deploying time                                  |
| ssl_expire_time | String | SSL expiration time                                  |
| seo             | String | Indicate whether to enable SEO optimization: "off" means to disable; "on" means to enable                |
| host_id         | Int    | Host ID, same as id                       |

#### cache Field Description

| Parameter Name | Type     | Description                                       |
| ---- | ------ | ---------------------------------------- |
| type | Int    | Type. There are four types: 0 refers to all files, 1 refers to file type, 2 refers to folder type, and 3 refers to full-path file |
| rule | String | Matching rule, corresponding to the types above                        |
| time | Int    | Cache expiration time (in seconds)                               |
| unit | String | The unit used to set cache expiration time. There are four types: "d" refers to day, "h" refers to hour, "m" refers to minute, and "s" refers to second |

#### refer Field Description

| Parameter Name      | Type    | Description                                       |
| --------- | ----- | ---------------------------------------- |
| type      | Int   | Hotlink protection type. There are three types: 0 means that hotlink protection is not configured; 1 means that the configured list is a blacklist; 2 means that the configured list is a whitelist |
| null_flag | Int | Indicate whether the hotlink protection is empty. 1 means the hotlink protection is empty                     |
| list      | Array | The configured hotlink protection list                                 |

**Note**:
+ The fields not described in the above are **invalid fields**, which can be ignored directly.


## 4. Example

### 4.1 Example of Input

> hosts.0:www.test.com



### 4.2 GET Request

All the parameters are required to be added after URL in GET request:

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetHostInfoByHost
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462434613
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXX
&hosts.0=www.test.com
```



### 4.3 POST Request

In POST request, the parameters will be filled in HTTP Request-body. The request address is:

```
https://cdn.api.qcloud.com/v2/index.php
```

Such formats of parameters as form-data, x-www-form-urlencoded are supported. The array of parameters is as follows:

```
array (
  'Action' => 'GetHostInfoByHost',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'hosts.0' => 'www.test.com'
)
```





### 4.4 Example of Returned Result

#### Query Successful

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "hosts": [
            {
                "id": 1234,
                "app_id": 1234567,
                "owner_uin": 7654321,
                "project_id": 0,
                "host": "www.test.com",
                "host_type": "cname",
                "service_type": "web",
                "origin": "8.8.8.8",
                "cache": [
                    {
                        "type": 0,
                        "rule": "all",
                        "time": 2592000,
                        "unit": "d"
                    },
                    {
                        "type": 1,
                        "rule": ".php;.jsp;.asp;.aspx",
                        "time": 0,
                        "unit": "s"
                    }
                ],
                "status": 5,
                "disabled": 0,
                "message": "Activated",
                "enable_overseas": "no",
                "create_time": "2016-08-25 21:22:40",
                "update_time": "2016-09-02 15:33:37",
                "deleted": "no",
                "fwd_host_type": "default",
                "fwd_host": "www.test.com",
                "middle_resource": -1,
                "refer": {
                    "type": 2,
                    "list": [
                        "1.1.1.1"
                    ],
                    "null_flag": 0
                },
                "readonly": 0,
                "cname": "www.test.com.cdn.dnsv1.com",
                "cache_mode": "simple",
                "furl_cache": "on",
                "ssl_type": 0,
                "pid_config": null,
                "bucket_name": "",
                "bucket_project_id": 0,
                "ssl_deploy_time": null,
                "ssl_expire_time": null,
                "seo": "off",
                "host_id": 308902
            }
        ],
        "total": 1
    }
}
```

#### Query Failed
```json
{
    "code": 4100,
    "message": "Authentication failed. Please refer to the Authentication section in the document.",
    "codeDesc": "AuthFailure"
}
```









