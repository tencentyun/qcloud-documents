## 接口名称
DescribeCdnProvIspDetailStat

## 功能说明
查询指定域名指定日期按运营商、省份统计的国内 CDN 节点统计数据明细（流量、带宽、请求数、请求命中率）

1. 由于省份、运营商数据需要从日志中分析，数据延迟大概为20-30分钟。可以查询最近60天内的数据。
2. 不指定省份仅指定运营商，返回该运营商各个省份的统计数据，可以指定多个运营商进行查询。
3. 不指定运营商仅指定省份，返回该省份各个运营商的统计数据，可以指定多个省份进行查询。
4. 不指定运营商也不指定省份，返回每个省份每个运营商的统计数据。
5. 若某个省份或运营商无数据，不会返回。
6. 返回的明细数据粒度为5分钟。

## 请求方式

### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称      | 必填 | 类型   | 说明                                                                                                                                                                                |
| ------------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hosts         | 是   | Array  | 域名列表，如果为空，查询所有点播域名的统计数据，如果域名超过5个，返回错误                                                                                                           |
| date          | 是   | String | 查询日期，格式为 yyyy-MM-dd，如2018-03-01                                                                                                                                           |
| statType      | 是   | String | CDN 统计数据类型<ul><li> flux：流量，单位是字节（byte）</li><li>bandwidth：带宽，单位是比特每秒（bps）</li><li>requests：请求数</li><li>hitrate：请求命中率，单位为万分比</li></ul> |
| provNames     | 否   | Array  | 要查询的[省份英文名称列表](#provNameList) ，见，如 Beijin，如果为空，查询所有省份的数据                                                                                             |
| ispNames      | 否   | Array  | 要查询的[运营商英文名称列表](#ispNameList)，如 China Mobile，如如果为空，查询所有运营商的数据                                                                                       |
| COMMON_PARAMS | 是   |        | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0)                                                                                                     |

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeCdnProvIspDetailStat
&hosts.0=123.vod2.myqcloud.com
&date=2018-03-01
&provNames.0=Guangdong
&ispNames.0=China Mobile
&ipsNames.1=China Unicom
&statType=flux
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称      | 类型    | 说明                                            |
| ------------- | ------- | ----------------------------------------------- |
| code          | Integer | 错误码，0：成功， 其他值：失败                  |
| message       | String  | 错误信息                                        |
| data          | Object  | 结果数据                                        |
| data.statType | String  | CDN 统计数据类型，和请求的 statType 参数一致    |
| data.hostData | Array   | 每个域名的统计数据，见 HostProvIspStatData 说明 |

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
| 参数名称  | 类型    | 说明                          |
| --------- | ------- | ----------------------------- |
| timeStamp | Integer | 统计数据所属时间，Unix 时间戳 |
| value     | Integer | 统计项数值                    |


### <span id="provNameList">省份地区名称映射</span>
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
| Heilongjiang          | 黑龙江    |
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
| Tianjin               | 天津     |
| Tibet                 | 西藏     |
| Xinjiang              | 新疆     |
| Yunnan                | 云南     |
| Zhejiang              | 浙江     |
| Hongkong Macao Taiwan | 港澳台   |
| Oevrsea               | 海外     |
| Other                 | 其它     |

 
### <span id="ispNameList">运营商名称映射</span>
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
		"hostData": [{
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
