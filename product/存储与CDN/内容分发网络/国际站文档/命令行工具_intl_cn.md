## 调用准备
使用命令行脚本调用API，需要配置SecretId和SecretKey，登陆腾讯云进入[云API密钥](https://console.cloud.tencent.com/capi)，可以看到调用API时需要的SecretId和SecretKey，请妥善保管您的密钥。
![](https://mc.qcloudimg.com/static/img/6ca171d3f6662016a8f31cc5520ffaeb/1.png)

## 使用说明
命令行为python脚本，[前往下载](https://github.com/zz-mars/CDN_API_DEMO/tree/master/Qcloud_CDN_API/python)。

### 使用准备
在使用上述python脚本时，您需要安装 requests 库，可使用如下命令：
```
pip install requests
```
您可以直接执行脚本，会提示您目前已经支持的接口清单：
![](https://mc.qcloudimg.com/static/img/813c521d24602315a8ddd18c644f56a6/2.png)

接口功能说明，请参考[API概览](https://cloud.tencent.com/doc/api/231/1723)。

### 域名详情查询
#### 查询所有域名详情
使用如下命令，可以调用 [DescribeCdnHosts](https://cloud.tencent.com/doc/api/231/3937) 接口，查询APPID下所有域名详细信息：
```
python QcloudCdnTools_V2.py DescribeCdnHosts -u xxxxxx -p xxxxxxx
```

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey。

##### 结果示例
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


#### 根据域名查询域名详情
使用如下命令，可以调用 [GetHostInfoByHost](https://cloud.tencent.com/doc/api/231/3938) 接口，查询指定域名对应的详情：
```
python QcloudCdnTools_V2.py GetHostInfoByHost -u xxxxx -p xxxxxxx --hosts www.test.com --hosts www.test2.com
```
##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ --hosts 表示要查询的域名，可以一次查询多个，均使用 --hosts，注意，接口参数需要两条横线。

##### 结果示例
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


#### 根据域名ID查询域名详情
使用如下命令，可以调用 [GetHostInfoById](https://cloud.tencent.com/doc/api/231/3939) 接口，查询ID对应域名详情：
```
python QcloudCdnTools_V2.py GetHostInfoById -u xxxxx -p xxxxxxx --ids 1234
```

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ --ids 表示要查询的域名ID，可以一次查询多个，均使用 --ids，注意，接口参数需要两条横线。

##### 结果示例
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

### 刷新预热
#### 刷新URL
使用如下命令，可以调用[RefreshCdnUrl](https://cloud.tencent.com/doc/api/231/3946) 接口，刷新指定URL：
```
python QcloudCdnTools_V2.py RefreshCdnUrl -u xxxxx -p xxxxxxx --urls http://xxxxxxxtang.sp.oa.com/test.php --urls http://www.test.com/1.html
```

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ --urls 表示要刷新的URL，可以一次查询多个，均使用 --urls;
+ urls 参数前必须添加http:// 或者 https:// 前缀；
+ 每个用户每天仅允许刷新10000条URL，每次仅允许提交最多1000条进行刷新。

##### 结果示例
```json
[
    {
        u'log_id': 220332,
        u'count': 1
    }
]
```
其中 log_id 为提交的刷新任务ID，您可以根据此ID查询该刷新任务的执行状态，count 为本次提交的刷新URL数目。

#### 刷新目录
使用如下命令，可以调用[RefreshCdnDir](https://cloud.tencent.com/doc/api/231/3947) 接口，刷新指定目录：
```
python QcloudCdnTools_V2.py RefreshCdnDir -u xxxxx -p xxxxxxx --dirs http://www.test.com/abc/
```

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ --dirs 表示要刷新的URL，可以一次查询多个，均使用 --dirs;
+ dirs 参数前必须添加 http:// 或者 https:// 前缀；
+ 每个用户每天仅允许刷新100条目录，每次仅允许提交最多20条进行刷新。

##### 结果示例
```json
request is success.
```

#### 查询刷新记录

您可以使用如下命令查询刷新记录：

```
python QcloudCdnTools_V2.py GetCdnRefreshLog -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-16
```

##### 参数说明

- -u 表示SecretId；
- -p 表示SecretKey；
- startDate 为开始查询日期，endDate为结束查询日期，startDate需要小于endDate。

##### 结果示例

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

其中 status 为刷新状态，1表示刷新完成。URL刷新、目录刷新的记录均可以通过此接口查询到。



### 域名配置

#### 修改缓存配置

使用如下命令，您可以调用 [UpdateCache](https://cloud.tencent.com/doc/api/231/3934) 接口，修改缓存过期设置：
```
python QcloudCdnTools_V2.py UpdateCache -u xxxxx -p xxxxxxx --hostId 1234 --cache [[0,\"all\",1000],[1,\".jpg;.js\",2000],[2,\"/www/html\",3000]]
```

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ hostId 为您需要修改缓存过期配置的域名ID；
+ cache 为目标缓存配置，注意双引号需要转义。

**缓存过期设置**
一个域名的缓存过期配置由若干条缓存过期配置组成，每条缓存过期配置分为三个参数，第一个为缓存类型，第二个为匹配规则，第三个为设置的过期时间，单位为秒。CDN为您提供了三种类型：

+ 0：全部类型，表示匹配的所有文件，为默认缓存配置；
+ 1：文件类型，表示按文件后缀匹配，匹配内容示例： .jpg;.png；
+ 2：文件夹类型，表示按目录匹配，匹配内容示例：/abc;/def。

##### 结果示例
```json
request is success.
```



#### 修改域名所属项目

使用如下命令，您可以调用[UpdateCdnProject](https://cloud.tencent.com/doc/api/231/3935)接口，修改域名所属项目：
```
python QcloudCdnTools_V2.py UpdateCdnProject -u xxxxx -p xxxxxxx --hostId 1234 --projectId 0
```
修改域名所属项目时，您需要知道项目对应的ID，您可以前往[项目管理](https://console.cloud.tencent.com/project)进行查看，默认项目的ID为0。

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ hostId 表示要修改项目的域名对应的ID；
+ projectId 为目标项目的ID。

##### 结果示例
```json
request is success.
```



#### 修改域名配置

使用如下命令，您可以调用[UpdateCdnConfig](https://cloud.tencent.com/doc/api/231/1397) 接口修改域名配置，包括缓存过期设置、防盗链、回源HOST、全路径缓存等：
```
python QcloudCdnTools_V2.py UpdateCdnConfig -u xxxxx -p xxxxxxx --hostId 1234 --projectId 0 --cacheMode custom --cache [[0,\"all\",1023448]] --refer [1,[\"www.baidu.com\",\"www.qq.com\"]] --fwdHost www.test.org --fullUrl off
```

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ hostId 表示要修改配置的域名ID；
+ projectId 表示要修改的项目ID；
+ cacheMode 表示是否开启高级缓存设置；
+ cache 表示缓存过期设置，可参考 UpdateCache 处说明；
+ refer 表示防盗链设置；
+ fwdHost 表示回源Host设置；
+ fullUrl 表示是否开启全路径缓存，开启了全路径缓存，则表明过滤参数开关为关闭状态；若未开启全路径缓存，则表明过滤参数开关为开启状态；

**防盗链设置说明**
防盗链由两个字段组成，第一个字段标识了refer的类型：
+ 0：不设置防盗链；
+ 1：设置黑名单；
+ 2：设置白名单。

第二个字段为具体的名单列表。

##### 结果示例
```json
request is success.
```



### 域名管理

#### 添加域名

使用如下命令，您可以调用[AddCdnHost](https://cloud.tencent.com/doc/api/231/1406) 接口，新增CDN加速域名：

```
python QcloudCdnTools_V2.py AddCdnHost -u xxxxx -p xxxxxxx --host www.test.com --projectId 0 --hostType cname --origin 1.1.1.1
```

##### 参数说明

+ -u 表示SecretId；
+ -p 表示SecretKey；
+ host 表示要增加的加速域名，域名需要通过工信部备案，且尚未接入过腾讯云CDN；
+ projecctId 表示要将域名增加入的项目ID，可进入[项目管理](https://console.cloud.tencent.com/project) 查看项目对应ID；
+ hostType 为接入类型，若为'cname'则表示自有源接入；若为'ftp'则表示FTP源接入，此时源站参数会被忽略；
+ origin 表示源站配置。

##### 结果示例

```
request is success.
```



#### 下线域名

使用如下命令，您可以调用[OfflineHost](https://cloud.tencent.com/doc/api/231/1403)接口，关闭指定域名的CDN加速服务：
```
python QcloudCdnTools_V2.py OfflineHost -u xxxxx -p xxxxxxx --hostId 1234
```

##### 参数说明
+ -u 表示SecretId；
+ -p 表示SecretKey；
+ 处于“已开启”状态的域名调用下线命令才能成功；
+ hostId 表示要下线的域名ID，可通过 GetHostInfoByHost 获取域名对应ID。

##### 结果示例
```json
request is success.
```



#### 上线域名

使用如下命令，您可以调用[OnlineHost](https://cloud.tencent.com/doc/api/231/1402)接口，开启指定域名的CDN加速服务：

```
python QcloudCdnTools_V2.py OnlineHost -u xxxxx -p xxxxxxx --hostId 1234
```

##### 参数说明：

- -u 表示SecretId；
- -p 表示SecretKey；
- 只有处于”已关闭“状态的域名调用上线命令才能够成功；
- hostId 表示要下线的域名ID，可通过 GetHostInfoByHost 获取域名对应ID。

##### 结果示例

```json
request is success.
```



#### 删除域名

使用如下命令，您可以调用[DeleteCdnHost](https://cloud.tencent.com/doc/api/231/1396) 接口，删除指定域名：

```
python QcloudCdnTools_V2.py DeleteCdnHost -u xxxxx -p xxxxxx -hostId 1234
```

##### 参数说明：

- -u 表示SecretId；
- -p 表示SecretKey；
- 只有处于”已关闭“状态的域名调用删除命令才能够成功；
- hostId 表示要下线的域名ID，可通过 GetHostInfoByHost 获取域名对应ID。




### 日志相关

#### 获取日志下载链接

使用如下命令，您可以调用[GenerateLogList](https://cloud.tencent.com/doc/api/231/3950)接口，获取指定域名的CDN日志下载链接：

```
python QcloudCdnTools_V2.py GenerateLogList -u xxxxx -p xxxxxxx --hostId 1234
```

##### 参数说明

- -u 表示SecretId；
- -p 表示SecretKey；
- hostId 为要查询日志下载链接的域名ID；
- 获取30天内每天的日志下载链接。

##### 结果示例

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

若无link字段，则表示当天无日志数据产生。

 

### 消耗查询

#### 查询TOP100URL

使用如下命令，您可以调用[GetCdnStatTop](https://cloud.tencent.com/doc/api/231/3944)接口，查询域名或项目的TOP100流量/带宽消耗URL：

```
python QcloudCdnTools_V2.py GetCdnStatTop -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-15 --statType bandwidth --projects 0 --hosts test.com
```

##### 参数说明

- -u 表示SecretId；
- -p 表示SecretKey；
- startDate 表示查询起始时间，若设置为 2016-08-15，则实际查询开始时间为：2016-08-15 00:00:00；
- endDate 表示查询结束时间，若设置为 2016-08-15，则实际查询结束时间为：2016-08-15 23:55:00；
- projects 表示查询的项目ID，支持多个；
- hosts表示查询的域名，域名所属项目必须传参，否则会导致错误，支持多个；
- statType为排名依据，bandwidth表示带宽，flux表示流量。


##### 结果示例

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

value 为消耗值，flux的单位为Byte，bandwidth的单位为bps。



#### 查询状态码统计

使用如下命令，您可以调用[GetCdnStatusCode](https://cloud.tencent.com/doc/api/231/3943)接口，查询域名或项目的状态码统计：

```
python QcloudCdnTools_V2.py GetCdnStatusCode -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-15 --projects 0 --hosts test.com
```

##### 参数说明

- -u 表示SecretId；
- -p 表示SecretKey；
- startDate 表示查询起始时间，若设置为 2016-08-15，则实际查询开始时间为：2016-08-15 00:00:00；
- endDate 表示查询结束时间，若设置为 2016-08-15，则实际查询结束时间为：2016-08-15 23:55:00；
- projects 表示查询的项目ID，支持多个；
- hosts表示查询的域名，域名所属项目必须传参（projects），否则会导致错误，支持多个。

##### 结果示例

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



#### 查询消耗统计明细

使用如下命令，您可以调用[DescribeCdnHostDetailedInfo](https://cloud.tencent.com/doc/api/231/3942)接口，查询域名或项目的消耗明细：

```
python QcloudCdnTools_V2.py DescribeCdnHostDetailedInfo -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-05-08 --endDate 2016-08-15 --projects 0 --hosts www.test.com --statType bandwidth
```

##### 参数说明

- -u 表示SecretId；
- -p 表示SecretKey；
- startDate 表示查询起始时间，若设置为 2016-08-15，则实际查询开始时间为：2016-08-15 00:00:00；
- endDate 表示查询结束时间，若设置为 2016-08-15，则实际查询结束时间为：2016-08-15 23:55:00；
- projects 表示查询的项目ID，支持多个；
- hosts表示查询的域名，域名所属项目必须传参（projects），否则会导致错误，支持多个;
- statType为指定查询的消耗类型，flux为流量，单位为Byte；bandwidth为带宽，单位为bps。

##### 结果示例

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

period为时间粒度，根据所查询时间区间长短不同，返回的时间粒度也不同。1-3日，明细时间粒度均为5分钟，4-7日时间粒度为1小时，8天及以上时间粒度为1天。



#### 查询消耗量统计

使用如下命令，您可以调用[DescribeCdnHostInfo](https://cloud.tencent.com/doc/api/231/3941)接口，查询域名或项目的消耗统计：

```
python QcloudCdnTools_V2.py DescribeCdnHostInfo -u xxxxxxxxxxxx -p xxxxxxxxxxxx --startDate 2016-08-15 --endDate 2016-08-15 --projects 0 --hosts www.test.com --statType bandwidth
```

##### 参数说明

- -u 表示SecretId；
- -p 表示SecretKey；
- startDate 表示查询起始时间，若设置为 2016-08-15，则实际查询开始时间为：2016-08-15 00:00:00；
- endDate 表示查询结束时间，若设置为 2016-08-15，则实际查询结束时间为：2016-08-15 23:55:00；
- projects 表示查询的项目ID，支持多个；
- hosts表示查询的域名，域名所属项目必须传参（projects），否则会导致错误，支持多个;
- statType为指定查询的消耗类型，flux为流量，单位为Byte；bandwidth为带宽，单位为bps。

##### 结果示例

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

查询结果为指定时间区间的总量，host_type为域名接入时的类型，cname表示自有源接入，ftp表示FTP源接入，cos表示COS源接入。


