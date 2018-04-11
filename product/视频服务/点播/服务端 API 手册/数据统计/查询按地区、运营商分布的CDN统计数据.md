## 接口名称
DescribeCdnProvIspDetailStat

## 功能说明
用于查询指定域名指定日期、指定运营商、指定省份的国内 CDN 节点消耗明细。由于运营商/省份需要从日志中分析，数据延迟大概为20-30分钟，可以查询最近60天内的数据。

### 详细说明
1. 本接口只查询国内 CDN 节点的消耗明细。
2. 由于省份-运营商组合结果非常多，且本接口返回的为细粒度的数据，数据量较大，暂时不支持太多域名同时查询，一次最多可查询5个域名。
3. 若不填充省份仅指定运营商，则返回的全国每一个省份在该运营商的消耗明细，支持指定多个运营商查询。
4. 若不填充运营商，仅指定省份，则返回该省份每一个运营商的消耗明细，支持指定多个省份查询。
5. 若不填充运营商，也不指定省份，则返回每个省份每一个运营商的消耗明细。
6. 若该省份或运营商无数据，则不会返回。
7. 返回的流量数据的单位是 byte（字节），带宽的单位是bps （比特每秒）。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称      | 必填 | 类型   | 说明                                                                                                                                                                                                                  |
| ------------- | ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hosts         | 是   | Array  | 域名列表，一次最多查询5个域名。如果为空，将查询所有域名的统计数据（如果域名超过5个，返回错误）                                                                                                                        |
| date          | 是   | string | 查询日期，格式为 yyyy-MM-dd，如 2018-03-20                                                                                                                                                                            |
| statType      | 是   | string | CDN 统计数据类型 <ul><li> flux：表示流量明细，单位是字节（byte）;</li><li>bandwidth：表示峰值带宽明细，单位是比特每秒（bps）;</li><li>requests：表示请求数明细;</li><li>hitrate：表示平均请求命中率明细，单位为万分比 |
| provNames     | 否   | Array  | 省份英文名称列表，如果为空，表示查询所有省份的数据                                                                                                                                                                    |
| ispNames      | 否   | Array  | 运营商英文名称列表，如果为空，表示查询所有运营商的数据                                                                                                                                                                |
| COMMON_PARAMS | 是   |        | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)                                                                                                                                       |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeCdnProvIspDetailStat
&hosts.0=123.vod2.myqcloud.com
&date=2017-03-20
&statType=flux
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称      | 类型    | 说明                                                  |
| ------------- | ------- | ----------------------------------------------------- |
| code          | Integer | 错误码, 0：成功, 其他值：失败                         |
| message       | String  | 错误信息                                              |
| data          | Object  | 结果数据                                              |
| data.statType | String  | CDN 统计数据类型，和请求的 statType 参数一致          |
| data.list     | Array   | 省份、运营商统计数据列表，见 HostProvIspStatData 说明 |
|               |

#### HostProvIspData省份统计数据
| 参数名称                | 类型   | 说明                          |
| ----------------------- | ------ | ----------------------------- |
| host                    | String | 域名                          |
| provIspData             | Array  | 省份运营商统计数据明细        |  |
| provIspData.provEngName | String | 省份英文名称                  |
| provIspData.provZhName  | String | 省份中文名称                  |
| provIspData.ispEngName  | String | 运营商英文名称                |
| provIspData.ispZhName   | String | 运营商中文名称                |
| provIspData.statData    | Array  | 统计数据明细列表，见 StatData |

#### StatData
| 参数名称  | 类型    | 说明                       |
| --------- | ------- | -------------------------- |
| timeStamp | Integer | 统计项所属时间，Unix 时间戳 |
| value     | Integer | CDN 统计项数值             |


### 省份地区名称映射
| 英文名称              | 中文名称 |
| --------------------- | -------- |
| Anhui                 | 安徽     |
| Beijing               | 北京     |
| Chongqing             | 重庆     |
| Fujian                | 福建     |
| Gansu                 | 甘肃     |
| Guangdong             | 广东     |
| Guangxi               | 广西     |
| Guizhou               | 贵州     |
| Hainan                | 海南     |
| Hebei                 | 河北     |
| Heilongjian           | 黑龙江    |
| Henan                 | 河南     |
| Hubei                 | 湖北     |
| Hunan                 | 湖南     |
| Jiangsu               | 江苏     |
| Jiangxi               | 江西     |
| Jilin                 | 吉林     |
| Liaoning              | 辽宁     |
| Inner Mongoria        | 内蒙古   |
| Ningxia               | 宁夏     |
| Qinghai               | 青海     |
| Shandong              | 山东     |
| Shanxi                | 山西     |
| Shaanxi               | 陕西     |
| Shanghai              | 上海     |
| Sichuan               | 四川     |
| Taiwan                | 台湾     |
| Tianjin               | 天津     |
| Tibet                 | 西藏     |
| Xinjiang              | 新疆     |
| Yunnan                | 云南     |
| Zhejiang              | 浙江     |
| Hongkong Macao Taiwan | 港澳台   |
| Oevrsea               | 海外     |
| Other                 | 其它     |

 
### 运营商名称映射
| 英文名称                     | 中文名称   |
| ---------------------------- | ---------- |
| China Unicom                 | 中国联通   |
| China Railcom                | 中国铁通   |
| China Telecom                | 中国电信   |
| China Mobile                 | 中国移动   |
| Cernet                       | 教育网     |
| Great Wall Broadband Network | 长城宽带   |
| Oevrsea Isp                  | 海外运营商 |
| Other                        | 其它       |


### 错误码说明
| 错误码    | 含义说明                                     |
| --------- | -------------------------------------------- |
| 4000-7000 | 参见[公共错误码](/document/product/266/7783) |
| 1000      | 无效参数                                     |

### 应答示例
```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"statType": "flux",
		"list": [{
			"host": "123.vod2.myqcloud.com",
			"provIspData": [{
					"provZhName": "广东",
					"provEngName": "Guangdong",
					"ispZhName": "中国移动",
					"ispEngName": "China Mobile",
					"statData": [{
						"timeStamp": 1519833600,
						"value": 12333
					}, {
						"timeStamp": 1519833900,
						"value": 2333
					}]
				},

				{
					"provZhName": "广东",
					"provEngName": "Guangdong",
					"ispZhName": "中国联通",
					"ispEngName": "China Unicom",
					"statData": [{
						"timeStamp": 1519833600,
						"value": 12333
					}, {
						"timeStamp": 1519833900,
						"value": 2333
					}]
				}
			]
		}]
	}
}
```
