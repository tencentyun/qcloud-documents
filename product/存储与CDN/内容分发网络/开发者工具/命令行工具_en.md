## Preparation Before Calling
You need to configure SecretId and SecretKey to call API using command line script. Log in to Tencent Cloud and go to [Cloud API Key](https://console.cloud.tencent.com/capi) to view the SecretId and SecretKey needed to call API. Make sure to keep them safe.
![](https://mc.qcloudimg.com/static/img/3aae5dd60294ddbe70f4108ebbf04783/1.png)

## Instructions
The command line is python script. [Download](https://github.com/zz-mars/CDN_API_DEMO/tree/master/Qcloud_CDN_API/python).

### Preparation Before Using
You need to install requests library to use the python script mentioned above. Use the following command:
```
pip install requests
```
You may directly execute the script. A list of APIs that are currently supported will be presented to you:
![](https://mc.qcloudimg.com/static/img/813c521d24602315a8ddd18c644f56a6/2.png)

For the features of the APIs, please refer to [API Overview](https://cloud.tencent.com/doc/api/231/1723).

### Querying Domain Details
#### Querying Details of All Domains
Use the following command to call the [DescribeCdnHosts](https://cloud.tencent.com/doc/api/231/3937) API in order to query the details of all domains under the APPID:
```
python QcloudCdnTools_V2.py DescribeCdnHosts -u xxxxxx -p xxxxxxx
```

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey.

##### Example of Result
```josn
{
    u'total': 1,
    u'hosts': [
        {
            u'origin': u'8.8.8.8',
            u'enable_overseas': u'no',
            u'disabled': 0,
            u'create_time': u'2016-07-2610: 34: 09',
            u'seo': u'off',
            u'message': u'\u90e8\u7f72\u4e2d',
            u'id': 279950,
            u'cache': [
                {
                    u'type': 0,
                    u'unit': u'd',
                    u'rule': u'all',
                    u'time': 2592000
                },
                {
                    u'type': 1,
                    u'unit': u's',
                    u'rule': u'.php;.jsp;.asp;.aspx',
                    u'time': 0
                }
            ],
            u'middle_resource': -1,
            u'fwd_host_type': u'default',
            u'readonly': 0,
            u'fwd_host': u'www.test.com',
            u'service_type': u'media',
            u'project_id': 0,
            u'refer': {
                u'list': [                  
                ],
                u'type': 0,
                u'null_flag': 0
            },
            u'status': 4,
            u'update_time': u'2016-08-1220: 36: 58',
            u'ssl_expire_time': None,
            u'deleted': u'no',
            u'ssl_type': 0,
            u'ssl_deploy_time': None,
            u'app_id': 1251991073,
            u'host': u'www.test.com',
            u'bucket_name': u'',
            u'host_id': 279950,
            u'pid_config': None,
            u'cache_mode': u'simple',
            u'furl_cache': u'on',
            u'host_type': u'cname',
            u'owner_uin': 78976504,
            u'cname': u'www.test.com.cdn.dnsv1.com'
        }
        ...
    ]
}
```


#### Reviewing Domain Details Based on Domains
Use the following command to call the [GetHostInfoByHost](https://cloud.tencent.com/doc/api/231/3938) API in order to query the details of specified domain:
```
python QcloudCdnTools_V2.py GetHostInfoByHost -u xxxxx -p xxxxxxx --hosts www.test.com --hosts www.test2.com
```
##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ --hosts stands for the domain to be queried. You may query multiple domains at one time with each using a --host. Note that API parameter needs two dashes.

##### Example of Result
```json
{
    u'total': 2,
    u'hosts': [
        {
            u'origin': u'8.8.8.8',
            u'enable_overseas': u'no',
            u'disabled': 0,
            u'create_time': u'2016-07-2610: 34: 09',
            u'seo': u'off',
            u'message': u'\u5df2\u5f00\u542f',
            u'id': 1234,
            u'cache': [
                {
                    u'type': 0,
                    u'unit': u'd',
                    u'rule': u'all',
                    u'time': 2592000
                },
                {
                    u'type': 1,
                    u'unit': u's',
                    u'rule': u'.php;.jsp;.asp;.aspx',
                    u'time': 0
                }
            ],
            u'middle_resource': -1,
            u'fwd_host_type': u'default',
            u'readonly': 0,
            u'fwd_host': u'www.test.com',
            u'service_type': u'media',
            u'project_id': 0,
            u'refer': {
                u'list': [                 
                ],
                u'type': 0,
                u'null_flag': 0
            },
            u'status': 5,
            u'update_time': u'2016-08-1220: 36: 58',
            u'ssl_expire_time': None,
            u'deleted': u'no',
            u'ssl_type': 0,
            u'ssl_deploy_time': None,
            u'app_id': 1251991073,
            u'host': u'www.test.com',
            u'bucket_name': u'',
            u'host_id': 279950,
            u'pid_config': None,
            u'cache_mode': u'simple',
            u'furl_cache': u'on',
            u'host_type': u'cname',
            u'owner_uin': 78976504,
            u'cname': u'www.test.com.cdn.dnsv1.com'
        },
        ...
    ]
}
```


#### Querying Domain Details Based on Domain ID
Use the following command to call the [GetHostInfoById](https://cloud.tencent.com/doc/api/231/3939) API in order to query the details of a domain with specified ID:
```
python QcloudCdnTools_V2.py GetHostInfoById -u xxxxx -p xxxxxxx --ids 1234
```

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ --ids stands for the ID of the domain to be queried. You may query multiple domains at one time with each using a --ids. Note that API parameter needs two dashes.

##### Example of Result
```json
{
    u'total': 1,
    u'hosts': [
        {
            u'origin': u'8.8.8.8',
            u'enable_overseas': u'no',
            u'disabled': 0,
            u'create_time': u'2016-07-2610: 34: 09',
            u'seo': u'off',
            u'message': u'\u5df2\u5f00\u542f',
            u'id': 1234,
            u'cache': [
                {
                    u'type': 0,
                    u'unit': u'd',
                    u'rule': u'all',
                    u'time': 2592000
                },
                {
                    u'type': 1,
                    u'unit': u's',
                    u'rule': u'.php;.jsp;.asp;.aspx',
                    u'time': 0
                }
            ],
            u'middle_resource': -1,
            u'fwd_host_type': u'default',
            u'readonly': 0,
            u'fwd_host': u'www.test.com',
            u'service_type': u'media',
            u'project_id': 0,
            u'refer': {
                u'list': [                 
                ],
                u'type': 0,
                u'null_flag': 0
            },
            u'status': 5,
            u'update_time': u'2016-08-1220: 36: 58',
            u'ssl_expire_time': None,
            u'deleted': u'no',
            u'ssl_type': 0,
            u'ssl_deploy_time': None,
            u'app_id': 1251991073,
            u'host': u'www.test.com',
            u'bucket_name': u'',
            u'host_id': 279950,
            u'pid_config': None,
            u'cache_mode': u'simple',
            u'furl_cache': u'on',
            u'host_type': u'cname',
            u'owner_uin': 78976504,
            u'cname': u'www.test.com.cdn.dnsv1.com'
        }
    ]
}
```

### Refreshing and Prefetching
#### Refreshing URL
Use the following command to call the [RefreshCdnUrl](https://cloud.tencent.com/doc/api/231/3946) API to refresh the specified URL:
```
python QcloudCdnTools_V2.py RefreshCdnUrl -u xxxxx -p xxxxxxx --urls http://xxxxxxxtang.sp.oa.com/test.php --urls http://www.test.com/1.html
```

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ --urls stands for the URL to be refreshed. You may query multiple URLs at one time with each using a --urls;
+ You must add http:// or https:// prefix before the urls parameter;
+ Each user may only refresh 10,000 URLs each day, with a maximum of 1,000 URLs allowed to be submitted for each refresh.

##### Example of Result
```json
[
    {
        u'log_id': 220332,
        u'count': 1
    }
]
```
log_id stands for the ID of job that is submitted for refresh. You can query the execution status of the job using this ID. count stands for the number of URLs to be refreshed for this submission.

#### Refreshing Directory
Use the following command to call the [RefreshCdnDir](https://cloud.tencent.com/doc/api/231/3947) API to refresh the specified directory:
```
python QcloudCdnTools_V2.py RefreshCdnDir -u xxxxx -p xxxxxxx --dirs http://www.test.com/abc/
```

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ --dirs stands for the URL to be refreshed. You may query multiple URLs at one time with each using a --dirs;
+ You must add http:// or https:// prefix before the dirs parameter;
+ Each user may only refresh 100 directories each day, with a maximum of 20 directories allowed to be submitted for each refresh.

##### Example of Result
```json
request is success.
```

#### Querying Refresh Result

You can use the following command to query refresh result:

```
python QcloudCdnTools_V2.py GetCdnRefreshLog -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-16
```

##### Parameter Description

- -u stands for SecretId;
- -p stands for SecretKey;
- startDate is the starting date of the query, endDate is the ending date of the query. startDate must be earlier than endDate.

##### Example of Result

```json
{
    u'total': 2,
    u'logs': [
        {
            u'status': 1,
            u'complete_time': u'2016-08-1510: 39: 16',
            u'url_list': [
                u'http: //www.test.org/1.html'
            ],
            u'app_id': 1251991073,
            u'datetime': u'2016-08-1510: 39: 14',
            u'host': u'www.test.org',
            u'project_id': 0,
            u'type': 0,
            u'id': 1234
        },
		...
	]
}
```

status is the status of the refresh job. 1 means finished. The records for refreshing URLs and directories can be queried using this API.



### Domain Configuration

#### Modifying Cache Configuration

Use the following command to call the [UpdateCache](https://cloud.tencent.com/doc/api/231/3934) API to modify cache expiration time configuration:
```
python QcloudCdnTools_V2.py UpdateCache -u xxxxx -p xxxxxxx --hostId 1234 --cache [[0,\"all\",1000],[1,\".jpg;.js\",2000],[2,\"/www/html\",3000],[3,\"/index.html;/test/*.jpg\",3000]]
```

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ hostId is the ID of the domain whose cache expiration configuration is to be modified;
+ cache is the target cache configuration. Note that you need to escape the double quotation marks.

**Cache expiration configuration**
The cache expiration configuration of one domain is consisted of several entries of cache expiration configurations. Each entry is divided into three parameters: cache type,matching rule, and configured expiration time (in seconds). CDN provides three types:
+ 0: All types. This means all files are matched. This is the default cache configuration;
+ 1: File type. This means matching based on file extensions. Examples: .jpg; .png;
+ 2: Folder type. This means matching based on directories. Examples: /abc; /def;

##### Example of Result
```json
request is success.
```



#### Modifying a Domain's Project

Use the following command to call the [UpdateCdnProject](https://cloud.tencent.com/doc/api/231/3935) API to modify the project to which a domain belongs to:
```
python QcloudCdnTools_V2.py UpdateCdnProject -u xxxxx -p xxxxxxx --hostId 1234 --projectId 0
```
You need to know the project's ID when modifying a domain's project. Go to [Project Management](https://console.cloud.tencent.com/project) to check the project ID. The ID for the default project is 0.

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ hostId is the ID of a domain whose project is to be modified;
+ projectId is the target project ID.

##### Example of Result
```json
request is success.
```



#### Modifying Domain Configuration

Use the following command to call the [UpdateCdnConfig](https://cloud.tencent.com/doc/api/231/1397) API to modify such domain configurations as cache expiration configuration, hotlink protection, hosting source, full-path cache:
```
python QcloudCdnTools_V2.py UpdateCdnConfig -u xxxxx -p xxxxxxx --hostId 1234 --projectId 0 --cacheMode custom --cache [[0,\"all\",1023448]] --refer [1,[\"www.baidu.com\",\"www.qq.com\"]] --fwdHost www.test.org --fullUrl off
```

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ hostId is the ID of a domain whose configurations are to be modified;
+ projectId is the ID of a project to be modified;
+ cacheMode specifies whether to enable advanced cache configurations;
+ cache is the cache expiration configuration. Please refer to the instructions on UpdateCache;
+ refer is the hotlink protection configuration;
+ fwdHost is the hosting source configuration;
+ fullUrl specifies whether to enable full-path cache. Enabled full-path cache means parameter filtering is disabled; Disabled full-path cache means parameter filtering is enabled;

**Hotlink protection configuration instruction**
Hotlink protection consists of two fields. The first field specifies the type of refer:
+ 0: Do not configure hotlink protection;
+ 1: Configure blacklist;
+ 2: Configure whitelist.

The second field is the specific namelist.

##### Example of Result
```json
request is success.
```



##### Domain Management

#### Adding Domains

Use the following command to call the [AddCdnHost](https://cloud.tencent.com/doc/api/231/1406) API to add CDN accelerated domains:

```
python QcloudCdnTools_V2.py AddCdnHost -u xxxxx -p xxxxxxx --host www.test.com --projectId 0 --hostType cname --origin 1.1.1.1
```

##### Parameter Description

+ -u stands for SecretId;
+ -p stands for SecretKey;
+ host stands for the accelerated domain to be added. The domain is required to have been recorded by MIIT and have not been connected to Tencent Cloud CDN before;
+ projectId is the ID of a project to which a domain will be added. You can check project IDs in [Project Management](https://console.cloud.tencent.com/project);
+ hostType is the connection method. "cname" means own origin; "ftp" meas FTP origin (in which case the origin server parameter will be ignored);
+ origin is the configuration of origin server.

##### Example of Result

```
request is success.
```



#### Making Domain Offline

Use the following command to call the [OfflineHost](https://cloud.tencent.com/doc/api/231/1403) API to deactivate the CDN acceleration service for specified domain:
```
python QcloudCdnTools_V2.py OfflineHost -u xxxxx -p xxxxxxx --hostId 1234
```

##### Parameter Description
+ -u stands for SecretId;
+ -p stands for SecretKey;
+ The offline command can only be successfully called for domains whose statuses are "Activated";
+ hostId is the ID of the domain to be taken offline. You can acquire domain IDs with GetHostInfoByHost.

##### Example of Result
```json
request is success.
```



#### Making Domain Online

Use the following command to call the [OnlineHost](https://cloud.tencent.com/doc/api/231/1402) API to activate the CDN acceleration service for specified domain:

```
python QcloudCdnTools_V2.py OnlineHost -u xxxxx -p xxxxxxx --hostId 1234
```

##### Parameter Description:

- -u stands for SecretId;
- -p stands for SecretKey;
- The online command can only be successfully called for domains whose statuses are "Closed";
- hostId is the ID of the domain to be taken offline. You can acquire domain IDs with GetHostInfoByHost.

##### Example of Result

```json
request is success.
```



#### Deleting Domain

Use the following command to call the [DeleteCdnHost](https://cloud.tencent.com/doc/api/231/1396) API to delete specified domain:

```
python QcloudCdnTools_V2.py DeleteCdnHost -u xxxxx -p xxxxxx -hostId 1234
```

##### Parameter Description:

- -u stands for SecretId;
- -p stands for SecretKey;
- The deletion command can only be successfully called for domains whose statuses are "Closed";
- hostId is the ID of the domain to be taken offline. You can acquire domain IDs with GetHostInfoByHost.




### Logs

#### Obtaining Log Download Link

Use the following command to call the [GenerateLogList](https://cloud.tencent.com/doc/api/231/3950) API to acquire the CDN log download link of specified domain:

```
python QcloudCdnTools_V2.py GenerateLogList -u xxxxx -p xxxxxxx --hostId 1234
```

##### Parameter Description

- -u stands for SecretId;
- -p stands for SecretKey;
- hostId is the ID of a domain whose log download link is to be queried;
- The download links for the log of each day within 30 days will be acquired.

##### Example of Result

```json
{
    u'now': 1471267882,
    u'list': [
        {
            u'date': u'2016-07-16',
            u'type': 0,
            u'name': u'20160716-test.com'
        },
        {
            u'date': u'2016-07-17',
            u'link': u'http: //log-download.cdn.qcloud.com/20160717/20160717-test.com.gz?st=xYeU1vW6N9UJlSc3hxM0lg&e=1472131882',
            u'type': 1,
            u'name': u'20160717-test.com'
        },
		...
	]
}
```

If there is no link field, it means no log data has been generated on that day.

 

### Querying Consumption Data

#### Querying TOP100 URLs

Use the following command to call the [GetCdnStatTop](https://cloud.tencent.com/doc/api/231/3944) API to query TOP100 URLs with the highest traffic/bandwidth consumption for domains or projects:

```
python QcloudCdnTools_V2.py GetCdnStatTop -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-15 --statType bandwidth --projects 0 --hosts test.com
```

##### Parameter Description

- -u stands for SecretId;
- -p stands for SecretKey;
- startDate is the starting time of the query. For example, 8/15/2016 means the actual starting time of the query will be 8/15/2016 00:00:00;
- endDate is the ending time of the query. For example, 8/15/2016 means the actual ending time of the query will be 8/15/2016 23:55:00;
- projects is the ID of the project to be queried. You may enter multiple IDs;
- hosts is the domain to be queried. You must pass a parameter for the project to which the domain belongs, or it will cause an error. You may enter multiple domains;
- statType is ranking method, bandwidth is consumed bandwidth, and flux is traffic.


##### Example of Result

```json
{
    u'start_datetime': u'2016-08-15',
    u'url_data': [
        {
            u'name': u'test.com/uploads/20141218/1418891322.jpeg',
            u'value': 877
        },
        {
            u'name': u'test.com/uploads/20141218/1418891825.jpeg',
            u'value': 796
        },
        {
            u'name': u'test.com/uploads/20141218/1418896965.jpeg',
            u'value': 706
        },
		...
	]
}
```

value is consumption value. Measurement units for flux and bandwidth are Byte and bps, respectively.



#### Querying Status Code Statistics

Use the following command to call the [GetCdnStatusCode](https://cloud.tencent.com/doc/api/231/3943) API to query for status code statistics for domains or projects:

```
python QcloudCdnTools_V2.py GetCdnStatusCode -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-15 --projects 0 --hosts test.com
```

##### Parameter Description

- -u stands for SecretId;
- -p stands for SecretKey;
- startDate is the starting time of the query. For example, 8/15/2016 means the actual starting time of the query will be 8/15/2016 00:00:00;
- endDate is the ending time of the query. For example, 8/15/2016 means the actual ending time of the query will be 8/15/2016 23:55:00;
- projects is the ID of the project to be queried. You may enter multiple IDs;
- hosts is the domain to be queried. You must pass a parameter for the project to which the domain belongs (projects), or it will cause an error. You may enter multiple domains.

##### Example of Result

```json
[
    {
        u'200': [
            
        ],
        u'206': [
            
        ],
        u'304': [
            
        ],
        u'416': [
            
        ],
        u'404': [
            69,
			69,
            76,
            69,
            66,
            78,
            73,
            71,
            73,
            76,
      		...
     	],
      	u'500':[
          
      	]
    }
]
```



#### Querying Detailed Consumption Statistics

Use the following command to call the [DescribeCdnHostDetailedInfo](https://cloud.tencent.com/doc/api/231/3942) API to query the detailed consumption statistics for domains or projects:

```
python QcloudCdnTools_V2.py DescribeCdnHostDetailedInfo -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-05-08 --endDate 2016-08-15 --projects 0 --hosts www.test.com --statType bandwidth
```

##### Parameter Description

- -u stands for SecretId;
- -p stands for SecretKey;
- startDate is the starting time of the query. For example, 8/15/2016 means the actual starting time of the query will be 8/15/2016 00:00:00;
- endDate is the ending time of the query. For example, 8/15/2016 means the actual ending time of the query will be 8/15/2016 23:55:00;
- projects is the ID of the project to be queried. You may enter multiple IDs;
- hosts is the domain to be queried. You must pass a parameter for the project to which the domain belongs (projects), or it will cause an error. You may enter multiple domains;
- statType is the type of consumption to be queried. flux is traffic (in bytes). bandwidth is consumed bandwidth (in bps).

##### Example of Result

```json
{
    u'start_datetime': u'2016-08-1300: 00: 00',
    u'total_data': [
        35216,
        41875,
        42256,
        34333,
        40868,
        40906,
        38505,
        39487,
        39407,
  		...
  	],
    u'stat_type': u'flux',
    u'end_datetime': u'2016-08-1523: 55: 00',
    u'period': 5
}
```

period is the time granularity, which varies with different query time ranges. The time granularity is 5 minutes for a query time range of 1 to 3 days,  1 hour for a time range of 4 to 7 days, and 1 day for a time range of 8 days or above.



#### Querying Consumption statistics

Use the following command to call the [DescribeCdnHostInfo](https://cloud.tencent.com/doc/api/231/3941) API to query the consumption statistics for domains or projects:

```
python QcloudCdnTools_V2.py DescribeCdnHostInfo -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-15 --projects 0 --hosts www.test.com --statType bandwidth
```

##### Parameter Description

- -u stands for SecretId;
- -p stands for SecretKey;
- startDate is the starting time of the query. For example, 8/15/2016 means the actual starting time of the query will be 8/15/2016 00:00:00;
- endDate is the ending time of the query. For example, 8/15/2016 means the actual ending time of the query will be 8/15/2016 23:55:00;
- projects is the ID of the project to be queried. You may enter multiple IDs;
- hosts is the domain to be queried. You must pass a parameter for the project to which the domain belongs (projects), or it will cause an error. You may enter multiple domains;
- statType is the type of consumption to be queried. flux is traffic (in bytes). bandwidth is consumed bandwidth (in bps).

##### Example of Result

```json
{
    u'start_datetime': u'2016-08-1300: 00: 00',
    u'stat_type': u'bandwidth',
    u'end_datetime': u'2016-08-1523: 55: 00',
    u'detail_data': [
        {
            u'host_id': u'www.test.com',
            u'host_type': u'cname',
            u'host_name': u'www.test.com',
            u'host_value': 2214
        }
    ],
    u'period': 5
}
```

The result of the query will display the total consumption for the specified time range. host_type stands for the type of the connected domain, cname for self-owned origin, ftp for FTP origin and cos for COS origin.


