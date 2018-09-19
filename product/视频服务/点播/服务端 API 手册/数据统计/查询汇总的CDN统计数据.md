## 接口名称
DescribeCdnStat

## 功能说明
查询指定域名在指定时间段累计的 CDN 统计数据（流量、带宽、请求数、请求命中率）。

1. 流量、请求数是所查询时间段累计的总流量、总请求数，带宽是所查询时间段的峰值带宽，请求命中率是所查询时间段的平均请求命中率。
2. 只能查询最近90天内的数据。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称      | 必填 | 类型   | 说明                                                                                                                                                                                                                                              |
| ------------- | ---- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hosts         | 否   | Array  | 域名列表，如果为空，查询所有点播域名的统计数据，如果域名数超过20个，返回错误                                                                                                                                                                      |
| startDate     | 是   | String | 起始日期，格式为 yyyy-MM-dd ，如2018-03-01                                                                                                                                                                                                        |
| endDate       | 是   | String | 结束日期，格式为 yyyy-MM-dd ，如2018-03-02                                                                                                                                                                                                        |
| statType      | 是   | String | 统计数据类型<ul><li> flux：流量，单位是字节（byte）</li><li>bandwidth：带宽，单位是比特每秒（bps）</li><li>requests：请求数</li><li>hitrate：请求命中率，单位为万分比</li><li>ip_visits：IP 访问次数（海外 CDN 节点不支持查询 IP 访问次数）</li></ul> |
| COMMON_PARAMS | 是   |        | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)                                                                                                                                                                   |

## 接口应答

### 参数说明
| 参数名称           | 类型    | 说明                                                              |
| ------------------ | ------- | ----------------------------------------------------------------- |
| code               | Integer | 错误码，0：成功；其他值：失败                                     |
| message            | String  | 错误信息                                                          |
| statType           | String  | 统计数据类型，和请求参数的 statType 一致                          |
| data               | Array   | 结果数据                                                          |
| data.host          | String  | 域名                                                              |
| data.domesticValue | Integer | 国内 CDN 节点的统计数据                                           |
| data.overseaValue  | Integer | 海外 CDN 节点的统计数据，如果域名没有开启海外加速，不会返回该数据 |

### 错误码说明
| 错误码    | 含义说明                                     |
| --------- | -------------------------------------------- |
| 4000-7000 | 参见[公共错误码](/document/product/266/7783) |
| 1000      | 输入参数错误                                 |
| 17010     | hosts 参数错误                               |
| 17011     | 域名列表数据超过20个                         |
| 17012     | statType 参数错误                            |
| 17013     | startDate 参数错误                           |


## 示例

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeCdnStat
&hosts.0=123.vod2.myqcloud.com
&startDate=2018-03-01
&endDate=2018-03-02
&statType=flux
&COMMON_PARAMS
```

### 应答示例
```javascript
{
	"code": 0,
	"message": "",
	"statType": "flux",
	"data": [{
		"host": "123.vod2.myqcloud.com",
		"domesticValue": 13659874512,
		"overseaValue": 654859
	}]
}
```
