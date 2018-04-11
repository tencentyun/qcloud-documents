## 接口名称
DescribeCdnStat

## 功能说明
用于查询指定域名在某一时间区间的累计的 CDN 统计数据。如果查询流量、请求数，返回的是这段时间累计的总流量、总请求数，如果查询是的是带宽数据，返回的是这段时间的峰值带宽数据。

### 详细说明
1. 流量的单位是 byte （字节），带宽的单位是 bps （比特每秒）。
2. 可以查询最近90天的数据。

## 事件通知
无

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称      | 必填 | 类型   | 说明                                                                                                                                                                                                                |
| ------------- | ---- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hosts         | 否   | Array  | 域名列表，一次最多查询20个域名，如果为空。将查询用户所有点播域名的统计数据（如果域名数超过20个，则返回错误）                                                                                                      |
| startDate     | 是   | String | 起始日期，格式为 yyyy-MM-dd，如2018-03-01                                                                                                                                                                          |
| endDate       | 是   | String | 结束日期，格式为 yyyy-MM-dd，如2018-03-02                                                                                                                                                                          |
| statType      | 是   | String | CDN 统计数据类型，<ul><li> flux：表示流量，单位是字节（byte）；</li><li>bandwidth：表示峰值带宽，单位是比特每秒（bps）；</li><li>requests：表示请求数；</li><li>hitrate：表示平均请求命中率，单位为万分比</li></ul> |
| COMMON_PARAMS | 是   |        | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)                                                                                                                                     |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeCdnStat
&hosts.0=123.vod2.myqcloud.com
&startDate=2018-03-01
&endDate=2018-03-02
&statType=flux
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称           | 类型    | 说明                                          |
| ------------------ | ------- | --------------------------------------------- |
| code               | Integer | 错误码, 0: 成功；其他值: 失败                 |
| message            | String  | 错误信息                                      |
| statType           | string  | CDN 统计数据类型，和请求参数的 statType 一致  |
| data               | Array   | 结果数据                                      |
| data.host          | String  | 域名                                          |
| data.domesticValue | Integer | 国内 CDN 节点的统计数据，如流量或者峰值带宽 |
| data.overseaValue  | Integer | 海外 CDN 节点的统计数据，如流量或者峰值带宽 |

### 错误码说明
| 错误码    | 含义说明                                     |
| --------- | -------------------------------------------- |
| 4000-7000 | 参见[公共错误码](/document/product/266/7783) |
| 1000 | 输入参数错误 |

### 应答示例
```javascript
{
	"code": 0,
	"message": "",
	"statType": "flux",
	"data": [{
		"host": "123.vod2.myqcloud.com",
		"domesticValue": 13659874512,
		"oveaseaValue": 654859
	}]
}
```
