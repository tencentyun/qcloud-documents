## 接口名称
DescribeCdnRegionIspDetailStat

## 功能说明
查询指定域名或日期按地区、运营商统计的国内 CDN 节点统计数据（流量、带宽和请求数）。
>?
- 返回的数据为每5分钟一个统计数据。
2. 由于地区、运营商数据需要从日志中分析，数据延迟大概为20分钟 - 30分钟。
3. 只能查询最近60天内的数据。
4. 仅指定运营商，返回该运营商所有地区的统计数据。
5. 仅指定地区，返回该地区所有运营商的统计数据。
6. 不指定运营商也不指定地区，返回所有地区所有运营商的统计数据。
7. 如果某个地区或运营商无数据，则不会返回。


## 请求方式

#### 请求域名
`vod.api.qcloud.com`

#### 最高调用频率
100次/分钟

#### 参数说明
| 参数名称      | 必填 | 类型   | 说明                                                                                                                                                                                |
| ------------- | ---- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hosts         | 否   | Array  | 域名列表，如果为空，则查询所有云点播域名的统计数据；如果域名超过20个，返回错误信息。                                                                                                           |
| date          | 是   | String | 查询日期，格式为 yyyy-MM-dd，如2018-03-01。                                                                                                                                          |
| statType      | 是   | String | CDN 统计数据类型：<li> flux：流量，单位是字节（byte）。</li><li>bandwidth：带宽，单位是比特每秒（bps）。</li><li>requests：请求数。</li>                                       |
| regionNames   | 否   | Array  | 要查询的 [地区英文名称列表](#regionNameList)，如 Beijing。如果为空，则查询所有地区的数据。                                                                                              |
| ispNames      | 否   | Array  | 要查询的 [运营商英文名称列表](#ispNameList)，如 China Mobile。如果为空，则查询所有运营商的数据。                                                                                        |
| COMMON_PARAMS | 是   |   -     | 请参见 [公共参数](https://cloud.tencent.com/document/api/213/6976)。                                                                                                     |

#### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=DescribeCdnRegionIspDetailStat
&hosts.0=123.vod2.myqcloud.com
&date=2018-03-01
&regionNames.0=Guangdong
&ispNames.0=China Mobile
&ispNames.1=China Unicom
&statType=flux
&COMMON_PARAMS
```

## 接口应答

#### 参数说明
| 参数名称      | 类型    | 说明                                              |
| ------------- | ------- | ------------------------------------------------- |
| code          | Integer | 错误码，0：成功；其他值：失败。                    |
| message       | String  | 错误信息。                                          |
| data          | Object  | 结果数据。                                          |
| data.statType | String  | CDN 统计数据类型，和请求的 statType 参数一致。      |
| data.hostData | Array   | 每个域名的统计数据，请参见 [HostRegionIspStatData](#p1)。 |

#### [](id:p1)HostRegionIspData 数据说明
| 参数名称                    | 类型   | 说明                                               |
| --------------------------- | ------ | -------------------------------------------------- |
| host                        | String | 域名。                                               |
| regionIspData               | Array  | 地区及运营商统计数据。                               |
| regionIspData.regionEngName | String | 地区英文名称。                                       |
| regionIspData.regionZhName  | String | 地区中文名称。                                       |
| regionIspData.ispEngName    | String | 运营商英文名称。                                     |
| regionIspData.ispZhName     | String | 运营商中文名称。                                     |
| regionIspData.statData      | Array  | 统计数据列表，每5分钟汇总一个统计数据，请参见 [StatData](#p2)。 |

#### [](id:p2)StatData 数据说明
| 参数名称  | 类型    | 说明                          |
| --------- | ------- | ----------------------------- |
| timeStamp | Integer | 统计数据所属时间，Unix 时间戳。 |
| value     | Integer | 统计项数值。                    |


#### [](id:regionNameList)地区名称映射
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
| Heilongjiang          | 黑龙江   |
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
| Oversea               | 海外     |
| Other                 | 其它     |


#### 运营商名称映射[](id:ispNameList)
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


#### 错误码说明
| 错误码    | 含义说明                                     |
| --------- | -------------------------------------------- |
| 4000 - 7000 | 请参见 [公共错误码](https://cloud.tencent.com/document/api/213/6982)。 |
| 1000      | 无效参数。                                     |
| 17010     | HOSTS 参数错误。                               |
| 17011     | 域名列表数据超过20个。                          |
| 17012     | statType 参数错误。                            |
| 17015     | date 参数错误。                                |

#### 应答示例

```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"statType": "flux",
		"hostData": [{
			"host": "123.vod2.myqcloud.com",
			"regionIspData": [{
					"regionZhName": "广东",
					"regionEngName": "Guangdong",
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
					"regionZhName": "广东",
					"regionEngName": "Guangdong",
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




