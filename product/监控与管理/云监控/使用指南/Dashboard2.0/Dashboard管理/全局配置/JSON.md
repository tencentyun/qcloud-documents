

本文将为您介绍 JSON 的操作步骤和相关说明。

## 查看、复制 JSON

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。
2. 在左侧导航栏中单击 **Dashboard 列表**，进入 Dashboard 列表页。
3. 单击 Dashboard 列表左上角的**新建**，进入新建 Dashboard 管理页。
4. 在面板区单击![](https://main.qcloudimg.com/raw/8e26fe2eacdd794457a53a745bd48f3c.png)或单击 Dashboard 列表页的**设置**，进入 Dashboard 全局配置页。
5. 单击 **JSON**，复制 JSON 模板，即可把 JSON 格式部署到您的自建系统，在您的系统可查看对应的 Dashboard。
   ![](https://main.qcloudimg.com/raw/50fffa2ed12cbf3d74fd6b0c95f5afe2.png)

JSON 模板包含 Dashboard 的属性、模板变量、面板查询等字段，具体字段说明请参考下文。

## JSON 字段说明

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

| 名称        | 说明                                                 |
| ----------- | ---------------------------------------------------- |
| Description | 当前 Dashboard 备注                                  |
| Refresh     | 自动刷新的时间间隔                                   |
| Title       | 当前 Dashboard 名称                                  |
| UUID        | Dashboard 唯一标识 ID                                |
| Version     | Dashboard 的版本，每次保存 Dashboard 都会增加        |
| Templating  | Dashboard 模板变量 ，详情请参考 [Templating](#step1) |
| Link        | Dashboard 链接，详情请参考 [Link](#step2)            |
| Panels      | 图表配置 ，请参考 [Panels](#step3)                   |
| Time        | Dashboard 的时间范围                                 |

### [](id:step1)Templating

```
"Templating": [ // 模板变量
		{
			"Label": "cvm实例名称", // 模板变量别名
			"Multi": true, // 是否多选
			"Name": "cvm", // 标签
			"Selected": [], // 模板变量的值
			"Type": "monitor", // 模板变量的类型
			"TemplatingType": "basics", // 标签的类型：基础监控、自定义监控
      "TemplatingType": '123', // 变量 id
		}
	]
```

### [](id:step2)Link

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

### [](id:step3)Panels

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
			"ID": 1595472129140, // 图表 ID
			"Panels": [], // Panel 为图表组的字段，里面存放子 Panel
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
				"id": "1595471392817",// 图表 panel 的 id
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
				"markline": {// mark 设置
					"marklineMax": {
						"max": [// 是否显示峰值.**‘1’**为true；**‘0’**为false
							"1"
						]
					}
				},
				"nullPointMode": "1",// 数据中空值展示方式：0-连接空数据；1-不填充；2-自动填充为0
				"options": {
					"dataLinks": []// datalinks 数组
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
						"decimals": 2,// 左侧 y 轴精度
						"format": "%",// 左侧 y 轴 label 单位
						"label": null,
						"logBase": 1,
						"max": 2,// 左侧 y 轴坐标最大值
						"min": 0,// 左侧 y 轴坐标最小值
						"show": [// 是否展示左侧 y 轴.**‘1’**为true；**‘0’**为false
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
