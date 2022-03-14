>?云监控 Dashborad 全新改版，已于近期上线，欢迎大家使用新版 Dashboard 监控云上服务性能。旧版 Dashboard 即将下线，如需访问旧版文档，请参见 [旧版 Dashboard](https://cloud.tencent.com/document/product/248/13118)。



本文将为您介绍如何使用 Dashboard全局配置。

## Dashboard 全局配置
1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。
2. 在左侧导航栏中单击**Dashboard列表**，进入Dashboard列表页。
3. 单击 Dashboard 列表左上角的**新建**，进入新建 Dashboard 管理页。
4. 在面板区单击**![](https://main.qcloudimg.com/raw/8e26fe2eacdd794457a53a745bd48f3c.png)**或单击Dashboard 列表页的**设置**，进入 Dashboard 全局配置页。 Dashboard 全局配置支持基础设置、模板变量、链接管理、JSON，详细说明如下：
	- **基础设置**：支持自定义 Dashboard 名称和备注。
	- **模板变量**：支持自定义 Dashboard 数据筛选标签。
	- **链接管理**：支持自定义 Dashboard 快速跳转链接。您可以把业务相关的链接或面板关联到 Dashboard 中，方便您异障排查时进行快速跳转。
	- **JSON**：支持 JSON 格式查看、复制，您可以把 JSON 格式部署到您的自建系统，在您的系统查看 Dashboard。

### 基础设置

您可以对定义 Dashboard 名称和设置 Dashboard 备注。
![](https://main.qcloudimg.com/raw/e94ab9cafbf3bae9c5bc959511e772da.png)

### 模板变量
您可以自定义 Dashboard 筛选条件，在 Dashboard 管理页 [使用模板变量](#.E4.BD.BF.E7.94.A8.E6.A8.A1.E6.9D.BF.E5.8F.98.E9.87.8F) 。目前支持云服务器—基础监控、存储监控和云数据库MySQL主机、备机监控标签筛选。

1. 新建模板变量。
	单击**模板管理页** > **新增**，定义完模板变量信息后单击**确认**即可。
	![](https://main.qcloudimg.com/raw/84f4a6d0feb1aa68ce7fe184e02cb5c3.png)		 
2. 编辑、删除模板变量。
在模板变量列表中您可以进行模板变量的删除和编辑。
![](https://main.qcloudimg.com/raw/2ce8f088a373b4fa63da4ec7e0627b8f.png)
>?如需使用模板变量，请参考步骤 [使用模板变量](#.E4.BD.BF.E7.94.A8.E6.A8.A1.E6.9D.BF.E5.8F.98.E9.87.8F)。


### 链接管理
您可以自定义 Dashboard 快速跳转链接。链接管理包含链接名、类型、链接目标和参数，说明如下：
- 链接名：自定义链接名称
- 类型
  - 自定义链接：支持所有链接
  - 其它面板：链接到其它面板
- 链接目标：链接地址或链接面板
- 参数
 -  时间：跳转链接页是否同步面板时间
 - 模板变量：跳转链接页是否包含模板变量
- 打开方式
  - 新选项卡：新标签打开链接
- 当前页：当前标签打开链接
  

![](https://main.qcloudimg.com/raw/5f5d1cb38d63216df376e183a2836d93.png)

### JSON
JSON包含 Dashboard 的属性、模板变量、面板查询等字段，您可以把 JSON 格式部署到您的自建系统，在您的系统可查看对应的 Dashboard。

``` 
{
      "Description": "",
      "Refresh": "close",
      "Title": "JSONTEST",
      "UUID": "jdq4joy56is4w60q",
      "Version": 1,
      "Templating": [],
      "Links": [],
      "Panels": [],
      "Time": {
                "From": "now-12h",
                "To": "now"
        },
}
```

**JSON 字段说明：**

| 名称        | 说明                                              |
| ----------- | ------------------------------------------------- |
| Description | 当前 Dashboard 备注                                |
| Refresh     | 自动刷新的时间间隔                                |
| Title       | 当前 Dashboard 名称                               |
| UUID        | Dashboard 唯一标识 ID                              |
| Version     | Dashboard 的版本，每次保存 Dashboard 都会增加     |
| Templating  | Dashboard 模板变量 ，详情请参考 [模板变量](#step1) |
| Link        | Dashboard 链接，详情请参考 [链接](#step2)         |
| Panels      | 图表配置 ，请参考 [Panels](#step3)                        |
| Time        | Dashboard 的时间范围                              |

**[](id:step1)Templating</sapan>**

```
"Templating": [ // 模板变量
		{
			"Label": "cvm实例名称", // 模板变量别名
			"Multi": true, // 是否多选
			"Name": "cvm", // 标签
			"Selected": [], // 模板变量的值
			"Type": "monitor", // 模板变量的类型
			"TemplatingType": "basics", // 标签的类型：基础监控、自定义监控
      "TemplatingType": '123', // 变量id
		}
	]
```

**[](id:step2)Link**

```
"Links": [ // Dashboard链接
		{
			"IncludeVars": true, // 链接参数是否带上模板变量
			"KeepTime": true, // 链接参数是否带上时间变量
			"TargetBlank": true, // 是否新开选项卡
			"Title": "xxx", // 链接名称
			"Type": "other", // 链接类型：自定义链接和跳转其他Dashboard的链接
			"Url": "/monitor/dashboard2/dashboards/d/0hh64oj49rru3ctk/dashboard2-0yan-shi-an-li-xia-zuan-lian-jie",  // 链接地址
			"ID": 0 // ID
		}
	]
```

**[](id:step3)Panels**

```
"Panels": [ // panel配置
		{
			"Collapsed": false,  // 图表组是否折叠
			"Datasource": null, // 数据源
			"GridPos": { // 图表位置
				"H": 1,
				"W": 6,
				"X": 0,
				"Y": 0
			},
			"ID": 1595472129140, // 图表ID
			"Panels": [], // panel为图表组的字段，里面存放子Panel
			"Title": "默认图表组", // 标题
			"Type": "row" // 图表类型
		},
		{
			"DataLinks": [], // 图表配置的数据链接
			"Description": "", // 图表的备注
			"GridPos": {
				"H": 5,
				"W": 6,
				"X": 0,
				"Y": 1
			},
			"ID": 1595471392817,
			"Links": [], // 图表链接
			"Settings": { // 图表的可视化配置
				"aliasColors": {}, 
				"bars": false,
				"dashLength": 10, 
				"dashes": false,
				"datasource": null,
				"decimals": 2,// 图例精度
				"fieldConfig": {
					"defaults": {
						"custom": {}
					},
					"overrides": []
				},
				"fill": "0.8",// 图表填充透明度
				"fillGradient": 0,
				"gridPos": {
					"h": 8,
					"w": 12,
					"x": 0,
					"y": 0
				},
				"hiddenSeries": false,
				"id": "1595471392817",// 图表panel的id
				"legend": {// 图例设置
					"alignAsTable": [// 图例是否以表格形式展示
						"1"
					],
					"avg": [// 是否显示平均值.**‘1’**为true；**‘0’**为false
						"1"
					],
					"current": [// 是否显示最新值.**‘1’**为true；**‘0’**为false
						"1"
					],
					"max": [// 是否显示最大值.**‘1’**为true；**‘0’**为false
						"1"
					],
					"min": [// 是否显示最小值.**‘1’**为true；**‘0’**为false
						"1"
					],
					"rightSide": [// 是否放在右边.**‘1’**为true；**‘0’**为false
						"1"
					],
					"show": [// 是否显示图例.**‘1’**为true；**‘0’**为false
						"1"
					],
					"total": [// 是否展示累加值.**‘1’**为true；**‘0’**为false
						"1"
					],
					"values": false
				},
				"lines": [// 是否显示曲线.**‘1’**为true；**‘0’**为false
					"1"
				],
				"linesType": true,// 是否展示平滑曲线.**‘1’**为true；**‘0’**为false
				"linewidth": "2",// 曲线宽度
				"markline": {// mark设置
					"marklineMax": {
						"max": [// 是否显示峰值.**‘1’**为true；**‘0’**为false
							"1"
						]
					}
				},
				"nullPointMode": "1",// 数据中空值展示方式：0-连接空数据；1-不填充；2-自动填充为0
				"options": {
					"dataLinks": []// datalinks数组
				},
				"percentage": false,
				"pointradius": 2,
				"points": false,
				"renderer": "flot",
				"seriesOverrides": [],
				"spaceLength": 10,
				"stack": [// 是否堆积显示。**‘1’**为true；**‘0’**为false
					"1"
				],
				"steppedLine": false,
				"targets": [
					{
						"refId": "A",
						"scenarioId": "random_walk"
					}
				],
				"thresholds": [],
				"timeFrom": null,
				"timeRegions": [],
				"timeShift": null,
				"title": "新图表",
				"tooltip": {
					"shared": true,
					"sort": 0,
					"value_type": "individual"
				},
				"type": "graph",
				"xaxis": {
					"buckets": null,
					"mode": "time",
					"name": null,
					"show": true,
					"values": []
				},
				"yaxes": [
					{
						"decimals": 2,// 左侧y轴精度
						"format": "%",// 左侧y轴lebal单位
						"label": null,
						"logBase": 1,
						"max": 2,// 左侧y轴坐标最大值
						"min": 0,// 左侧y轴坐标最小值
						"show": [// 是否展示左侧y轴.**‘1’**为true；**‘0’**为false
							"1"
						]
					},
					{
						"decimals": 2,
						"format": "",
						"label": null,
						"logBase": 1,
						"max": null,
						"min": null,
						"show": [
							"1"
						]
					}
				],
				"yaxis": {
					"align": false,
					"alignLevel": null
				}
			},
			"Targets": [ // 指标配置
				{
					"Aggregate": "", // 统计方式
					"CompareLastWeek": false, // 环比
					"CompareYesterday": false, // 同比
					"Conditions": [ // 筛选条件
						{
							"Dimension": [
								"{\"InstanceId\":\"ins-19827u5b\"}",
								"{\"InstanceId\":\"ins-xxooxxoo\"}",
								"{\"InstanceId\":\"ins-19719mfp\"}"
							],
							"Region": "ap-guangzhou",
							"Type": "normal"
						}
					],
					"ConfigId": "cvm",
					"Datasource": "DS_QCEMetric", // 产品类型
					"DimensionKey": [
						"InstanceId"
					],
					"GroupBy": [ // groupby
						"InstanceId"
					],
					"MetricNames": [ // 指标名
						"BaseCpuUsage"
					],
					"Namespace": "QCE/CVM", // 命名空间
					"Period": 60 // 粒度
				},
			],
			"Title": "单指标 - 默认配置", // 图表名称
			"Type": "graph" // 图表类型
		},
	]
```


## 使用模板变量

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。
2. 在左侧导航栏中单击**Dashboard 列表**，进入 Dashboard 列表页。
3. 找到您需要查看模板变量的 Dashboard，单击对应的面板名称。
4. 创建模板变量后支持在 作为 Dashboard 和监控图表的快速选择器。
    - 在 Dashboard 使用：在 Dashboard 管理页中即可使用模板变量对 Dashboard 展示数据进行筛选。
       ![](https://main.qcloudimg.com/raw/ba7fb73ba166c1479e38c2ed84c385f1.png)
    - 在监控图表中使用：在图表编辑页，快速选择标签进行分组聚合展示实例数据。
       ![](https://main.qcloudimg.com/raw/9899cd8bf31fc6c8ad164aec1b76219a.png)
    > ?如需编辑图表，请参考 [编辑指标]( https://cloud.tencent.com/document/product/248/46761#.E7.BC.96.E8.BE.91.E6.8C.87.E6.A0.87 ) 。
