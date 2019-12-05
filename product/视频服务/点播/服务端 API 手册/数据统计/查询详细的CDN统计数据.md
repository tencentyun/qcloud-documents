## 接口名称
DescribeCdnDetailStat

## 功能说明
查询指定域名在指定时间段的 CDN 统计数据明细（流量、带宽、请求数和请求命中率）。

- 只能查询最近90天的数据。
- 统计数据可以是每5分钟汇总的统计数据，也可以是每天汇总的统计数据，具体依据请求起始日期和结束日期的时间跨度以及请求的时间间隔参数来决定。

## 请求方式

#### 请求域名
`vod.api.qcloud.com`

#### 最高调用频率
100次/分钟      

#### 参数说明
| 参数名称      | 必填 | 类型    | 说明                                                                                                                                                                                                                                                                                                                                             |
| ------------- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| hosts         | 否   | Array   | 域名列表，如果为空，则查询所有云点播域名的统计数据；如果域名超过20个，则返回错误信息。                                                                                                                                                                                                                                                                       |
| startDate     | 是   | String  | 起始日期，格式为 yyyy-MM-dd，如2018-03-01。                                                                                                                                                                                                                                                                                                        |
| endDate       | 是   | String  | 结束日期，格式为 yyyy-MM-dd，如2018-03-02。                                                                                                                                                                                                                                                                                                        |
| statType      | 是   | String  | CDN 统计数据类型：<li> flux：流量，单位是字节（byte）。</li><li>bandwidth：带宽，单位是比特每秒（bps）。</li><li>requests：请求数。</li><li>hitrate：请求命中率，单位为万分比。</li><li>ip_visits：IP 访问次数（海外 CDN 节点不支持查询 IP 访问次数）。</li>                                                                                     |
| interval      | 否   | Integer | 统计数据的时间间隔，单位为分钟。该参数仅当 startDate 等于 endDate 时有效，即只能查询指定日期的详细数据。interval 可以取的值有：<li>5：每5分钟汇总一个统计数据。</li><li>30：每30分钟汇总一个统计数据。</li><li>60：每小时汇总一个统计数据。</li><li>120：每2小时汇总一个统计数据。</li> startDate 不等于 endDate 时返回的数据是每天汇总的统计数据。 |
| COMMON_PARAMS | 是   |    -     | 请参见 [公共参数](https://cloud.tencent.com/document/api/213/6976)。                                                                                                                                                                                                                                                                  |



#### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeCdnDetailStat
&hosts.0=123.vod2.myqcloud.com
&startDate=2018-03-01
&endDate=2018-03-01
&statType=flux
&interval=60
&COMMON_PARAMS
```
## 接口应答

#### 参数说明
| 参数名称      | 类型    | 说明                                                                       |
| ------------- | ------- | -------------------------------------------------------------------------- |
| code          | Integer | 错误码，0：成功；其他值：失败。                                             |
| message       | String  | 错误信息。                                                                   |
| data          | Object  | 结果数据。                                                                   |
| data.interval | Integer | 统计数据的时间间隔，单位为分钟。如 interval = 5，表示数据是每5分钟汇总的数据。 |
| data.statType | String  | CDN 统计数据类型， 和输入的 statType 一致。                                  |
| data.hostData | Array   | 每个域名的统计数据列表，请参见 [HostStatData](#p1)。                               |

#### <span id = "p1"></span>HostStatData
| 参数名称     | 类型   | 说明                                                                                                   |
| ------------ | ------ | ------------------------------------------------------------------------------------------------------ |
| host         | String | 域名。                                                                                                   |
| domesticData | Array  | 国内 CDN 节点的统计数据明细，请参见 [StatData](#p2)。                                                   |
| overseaData  | Array  | 海外 CDN 节点的统计数据明细，请参见 [StatData](#p2)。如果域名没有开通海外 CDN 加速，则不会返回这个数据。 |

#### <span id = "p2"></span>StatData
| 参数名称  | 类型    | 说明                      |
| --------- | ------- | ------------------------- |
| timeStamp | Integer | 数据所属时间，Unix 时间戳。 |
| value     | Integer | CDN 统计项数值。            |


#### 错误码说明
| 错误码    | 含义说明                                     |
| --------- | -------------------------------------------- |
| 4000 - 7000 | 请参见 [公共错误码](https://cloud.tencent.com/document/api/213/6982)。 |
| 1000      | 无效参数。                                     |
| 17010     | HOSTS 参数错误。                               |
| 17011     | 域名列表数据超过20个。                         |
| 17012     | statType 参数错误。                            |
| 17015     | date 参数错误。                                |



#### 应答示例
```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"interval": 60,
		"statType": "flux",
		"hostData": [{
			"host": "123.vod2.myqcloud.com",
			"domesticData": [{
					"timeStamp": 1519833600,
					"value": 35698
				},
				{
					"timeStamp": 1519837200,
					"value": 5698
				}
			]
		}]
	}
}
```

