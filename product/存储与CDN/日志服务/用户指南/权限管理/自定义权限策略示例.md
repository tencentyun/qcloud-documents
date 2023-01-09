## 数据采集相关

### 使用 Loglistener 采集数据

用户可以使用采集 Agent Loglistener 采集数据，且具备日志上传的能力（本示例展示机器安装 Loglistener 上传日志的最小权限）。

```
{
	"version": "2.0",
	"statement": [{
		"action": [
			"cls:pushLog",
			"cls:getConfig",
			"cls:agentHeartBeat"
		],
		"resource": "*",
		"effect": "allow"
	}]
}
```

>? 如果您使用的 Loglistener 为2.6.5以前的版本，则需要加上 "cls:listLogset" 权限。
>
### 使用自建 k8s 上传数据

用户可以使用 Logagent 采集自建 k8s 环境的日志数据，且具备上传的能力（本示例展示自建 k8s 上传日志的最小权限）。

```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
        "cls:pushLog",
		"cls:agentHeartBeat",
        "cls:getConfig",
        "cls:CreateConfig",
        "cls:DeleteConfig",
        "cls:ModifyConfig",
        "cls:DescribeConfigs",
        "cls:DescribeMachineGroupConfigs",
        "cls:DeleteConfigFromMachineGroup",
        "cls:ApplyConfigToMachineGroup",
        "cls:DescribeConfigMachineGroups",
        "cls:ModifyTopic",
        "cls:DeleteTopic",
        "cls:CreateTopic",
        "cls:DescribeTopics",
        "cls:CreateLogset",
        "cls:DeleteLogset",
        "cls:DescribeLogsets",
        "cls:CreateIndex",
        "cls:ModifyIndex",
        "cls:CreateMachineGroup",
        "cls:DeleteMachineGroup",
        "cls:DescribeMachineGroups",
        "cls:ModifyMachineGroup",
        "cls:CreateConfigExtra",
        "cls:DeleteConfigExtra",
        "cls:DescribeConfigExtras",       
        "cls:ModifyConfigExtra"
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```


### 使用 API 上传数据

用户可以通过 API 上传日志到 CLS（本示例展示使用 API 上传日志的最小权限）。

```
{
	"version": "2.0",
	"statement": [{
		"action": [
			"cls:UploadLog"
		],
		"resource": "*",
		"effect": "allow"
	}]
}
```

### 使用 Kafka 上传数据

用户可以通过 Kafka 协议上传日志到 CLS（本示例展示使用 Kafka 协议上传日志的最小权限）。

```
{
	"version": "2.0",
	"statement": [{
		"action": [
			"cls:RealtimeProducer"
		],
		"resource": "*",
		"effect": "allow"
	}]
}
```

### 管理采集配置及机器组

包括创建/修改/删除采集配置及创建/修改/删除机器组。
- Config 相关接口对应采集配置相关资源。
- MachineGroup 相关接口对应机器组相关资源。
- ConfigExtra 相关的三个接口权限用于管理自建 k8s 上传日志相关的集群配置信息，如不使用自建 k8s 上传日志相关功能可以忽略。

```
{
    "version": "2.0",
    "statement": [{
        "action": [
            "cls:DescribeLogsets",
            "cls:DescribeTopics",
            "cls:CreateConfig",
            "cls:CreateConfig",
            "cls:DeleteConfig",
            "cls:DescribeConfigs",
            "cls:ModifyConfig",
            "cls:CreateConfigExtra",
            "cls:DeleteConfigExtra",
            "cls:ModifyConfigExtra",
            "cls:CreateMachineGroup",
            "cls:DeleteMachineGroup",
            "cls:DescribeMachineGroups",
            "cls:DeleteConfigFromMachineGroup",
            "cls:ApplyConfigToMachineGroup",
            "cls:ModifyMachineGroup"
        ],
        "resource": "*",
        "effect": "allow"
    }
	]
}
```

## 检索分析相关

### 使用控制台检索日志

#### 管理权限：对所有日志主题具备管理权限

用户可以对所有的日志主题进行检索及管理，包括创建日志主题、删除日志主题和修改索引配置等，不包括采集配置、日志投递和日志加工等。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:CreateLogset",
                "cls:CreateTopic",
                "cls:CreateExport",
                "cls:CreateIndex",
                "cls:DeleteLogset",
                "cls:DeleteTopic",
                "cls:DeleteExport",
                "cls:DeleteIndex",
                "cls:ModifyLogset",
                "cls:ModifyTopic",
                "cls:ModifyIndex",
                "cls:MergePartition",
                "cls:SplitPartition",
                "cls:DescribeLogsets",
                "cls:DescribeTopics",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeIndexs",
                "cls:DescribePartitions",
                "cls:SearchLog",
                "cls:DescribeLogHistogram",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLatestJsonLog",
				"cls:DescribeRebuildIndexTasks",
				"cls:CreateRebuildIndexTask",
				"cls:EstimateRebuildIndexTask",
				"cls:CancelRebuildIndexTask"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

#### 管理权限：对指定日志主题具备管理权限

用户能够对指定的日志主题进行检索及管理，包括创建日志主题、删除日志主题和修改索引配置等，不包括采集配置、日志投递和日志加工等。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:CreateLogset",
                "cls:CreateTopic",
                "cls:CreateExport",
                "cls:CreateIndex",
                "cls:DeleteLogset",
                "cls:DeleteTopic",
                "cls:DeleteExport",
                "cls:DeleteIndex",
                "cls:ModifyLogset",
                "cls:ModifyTopic",
                "cls:ModifyIndex",
                "cls:MergePartition",
                "cls:SplitPartition",
                "cls:DescribeLogsets",
                "cls:DescribeTopics",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeIndexs",
                "cls:DescribePartitions",
                "cls:SearchLog",
                "cls:DescribeLogHistogram",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLatestJsonLog",
				"cls:DescribeRebuildIndexTasks",
				"cls:CreateRebuildIndexTask",
				"cls:EstimateRebuildIndexTask",
				"cls:CancelRebuildIndexTask"
            ],
            "resource": [
                "qcs::cls:ap-guangzhou:100007***827:logset/1c012db7-2cfd-4418-****-7342c7a42516",
                "qcs::cls:ap-guangzhou:100007***827:topic/380fe1f1-0c7b-4b0d-****-d514959db1bb"
            ]
        }
    ]
}
```

#### 管理权限：对指定标签的日志主题具备管理权限

用户可以对包含指定标签的日志主题进行检索及管理，包括创建日志主题、删除日志主题和修改索引配置等，不包括采集配置、日志投递和日志加工等。为日志主题绑定标签时，需同时为其所属的日志集绑定标签。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:CreateLogset",
                "cls:CreateTopic",
                "cls:CreateExport",
                "cls:CreateIndex",
                "cls:DeleteLogset",
                "cls:DeleteTopic",
                "cls:DeleteExport",
                "cls:DeleteIndex",
                "cls:ModifyLogset",
                "cls:ModifyTopic",
                "cls:ModifyIndex",
                "cls:MergePartition",
                "cls:SplitPartition",
                "cls:DescribeLogsets",
                "cls:DescribeTopics",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeIndexs",
                "cls:DescribePartitions",
                "cls:SearchLog",
                "cls:DescribeLogHistogram",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLatestJsonLog",
				"cls:DescribeRebuildIndexTasks",
				"cls:CreateRebuildIndexTask",
				"cls:EstimateRebuildIndexTask",
				"cls:CancelRebuildIndexTask"
            ],
            "resource": [
                "*"
            ],
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "testCAM&test1"
                    ]
                }
            }
        }
    ]
}
```

#### 只读权限：对所有日志主题具备只读权限

用户可以对所有的日志主题进行日志检索。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeIndexs",
                "cls:DescribePartitions",
                "cls:SearchLog",
                "cls:DescribeLogHistogram",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLatestJsonLog",
				"cls:DescribeRebuildIndexTasks"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

#### 只读权限：对指定日志主题具备只读权限

用户可以对指定的日志主题进行检索。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeIndexs",
                "cls:DescribePartitions",
                "cls:SearchLog",
                "cls:DescribeLogHistogram",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLatestJsonLog",
				"cls:DescribeRebuildIndexTasks"
            ],
            "resource": [
                "qcs::cls:ap-guangzhou:100007***827:logset/1c012db7-2cfd-4418-****-7342c7a42516",
                "qcs::cls:ap-guangzhou:100007***827:topic/380fe1f1-0c7b-4b0d-****-d514959db1bb"
            ]
        }
    ]
}
```

#### 只读权限：对指定标签的日志主题具备只读权限

用户可以对包含指定标签的日志主题进行检索。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeIndexs",
                "cls:DescribePartitions",
                "cls:SearchLog",
                "cls:DescribeLogHistogram",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLatestJsonLog",
				"cls:DescribeRebuildIndexTasks"
            ],
            "resource": [
                "*"
            ],
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "testCAM&test1"
                    ]
                }
            }
        }
    ]
}
```

### 使用 API 检索分析日志

#### 只读权限：对所有日志主题具备检索分析只读权限

用户可以通过 API 对所有的日志主题进行日志检索分析。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

#### 只读权限：对指定日志主题具备检索分析只读权限

用户可以通过 API 对指定的日志主题进行日志检索分析。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog"
            ],
            "resource": [
                "qcs::cls:ap-guangzhou:100007***827:logset/1c012db7-2cfd-4418-****-7342c7a42516",
                "qcs::cls:ap-guangzhou:100007***827:topic/380fe1f1-0c7b-4b0d-****-d514959db1bb"
            ]
        }
    ]
}
```

#### 只读权限：对指定标签的日志主题具备检索分析只读权限

用户可以通过 API 对包含指定标签的的日志主题进行日志检索分析。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog"
            ],
            "resource": [
                "*"
            ],
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "testCAM&test1"
                    ]
                }
            }
        }
    ]
}
```


##  仪表盘相关

#### 管理权限：对所有仪表盘具备管理权限

用户可以管理**所有**的仪表盘，包括创建、删除、编辑、查看、订阅所有仪表盘。仪表盘可以使用**所有**日志主题的数据。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:GetChart",
                "cls:GetDashboard",
                "cls:ListChart",
                "cls:CreateChart",
                "cls:CreateDashboard",
                "cls:DeleteChart",
                "cls:DeleteDashboard",
                "cls:ModifyChart",
                "cls:ModifyDashboard",
                "cls:DescribeDashboards",
                "cls:SearchDashboardSubscribe",
                "cls:CreateDashboardSubscribe",
                "cls:ModifyDashboardSubscribe",
                "cls:DescribeDashboardSubscribes",
                "cls:DeleteDashboardSubscribe",
                "cls:ModifyDashboardSubscribeAck"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
                "cls:DescribeTopics",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeIndex",
                "cls:DescribeLogsets"
            ],
            "resource": "*"
        }
    ]
}
```



#### 管理权限：对指定标签的日志主题及仪表盘具备管理权限

用户可以管理**指定标签**的仪表盘，包括创建、删除、编辑、查看、订阅携带指定标签的仪表盘。仪表盘可以使用**指定标签**日志主题的数据。

```
    {
        "version": "2.0",
        "statement": [
             {
                "effect": "allow",
                "action": [
                    "cls:GetChart",
                    "cls:GetDashboard",
                    "cls:ListChart",
                    "cls:CreateChart",
                    "cls:CreateDashboard",
                    "cls:DeleteChart",
                    "cls:DeleteDashboard",
                    "cls:ModifyChart",
                    "cls:ModifyDashboard",
                    "cls:DescribeDashboards",
                    "cls:SearchDashboardSubscribe",
                    "cls:CreateDashboardSubscribe",
                    "cls:ModifyDashboardSubscribe",
                    "cls:DescribeDashboardSubscribes",
                    "cls:DeleteDashboardSubscribe",
                    "cls:ModifyDashboardSubscribeAck"
                ],
                "resource": "*",
                "condition": {
                    "for_any_value:string_equal": {
                        "qcs:resource_tag": [
                            "key&value"
                        ]
                    }
                }
            },
            {
                "effect": "allow",
                "action": [
                    "cls:SearchLog",
                    "cls:DescribeTopics",
                    "cls:DescribeLogFastAnalysis",
                    "cls:DescribeIndex",
                    "cls:DescribeLogsets"
                ],
                "resource": "*",
                "condition": {
                    "for_any_value:string_equal": {
                        "qcs:resource_tag": [
                            "key&value"
                        ]
                    }
                }
            }
        ]
    }
```



#### 管理权限：对指定资源的日志主题及仪表盘具备管理权限

用户可以管理**指定仪表盘**，包括创建、删除、编辑、查看、订阅指定的仪表盘资源。仪表盘可以使用**指定日志主题**的数据。

```
{
    "version": "2.0",
    "statement": [
         {
            "effect": "allow",
            "action": [
                "cls:GetChart",
                "cls:GetDashboard",
                "cls:ListChart",
                "cls:CreateChart",
                "cls:CreateDashboard",
                "cls:DeleteChart",
                "cls:DeleteDashboard",
                "cls:ModifyChart",
                "cls:ModifyDashboard",
                "cls:DescribeDashboards",
                "cls:SearchDashboardSubscribe",
                "cls:CreateDashboardSubscribe",
                "cls:ModifyDashboardSubscribe",
                "cls:DescribeDashboardSubscribes",
                "cls:DeleteDashboardSubscribe",
                "cls:ModifyDashboardSubscribeAck"
            ],
            "resource": [
                "qcs::cls::uin/100000***001:dashboard/dashboard-0769a3ba-2514-409d-****-f65b20b23736"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
                "cls:DescribeTopics",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeIndex",
                "cls:DescribeLogsets"
            ],
            "resource": [
                "qcs::cls::uin/100000***001:topic/174ca473-50d0-4fdf-****-2ef681a1e02a"
            ]
        }
    ]
}
```



#### 只读权限：对所有仪表盘具备只读权限

用户可以查看**所有**的仪表盘。仪表盘可以查看**所有**日志主题的数据。

```
{
    "version": "2.0",
    "statement": [
         {
            "effect": "allow",
            "action": [
                "cls:GetChart",
                "cls:GetDashboard",
                "cls:ListChart",
                "cls:DescribeDashboards",
                "cls:SearchDashboardSubscribe",
                "cls:DescribeDashboardSubscribes"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
                "cls:DescribeTopics",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeIndex",
                "cls:DescribeLogsets"
            ],
            "resource": "*"
        }
    ]
}
```



#### 只读权限：对指定标签的日志主题及仪表盘具备只读权限

用户可以查看携带**指定标签**的仪表盘资源。仪表盘可以查看携带**指定标签**的日志主题的数据。

```
{
    "version": "2.0",
    "statement": [
         {
            "effect": "allow",
            "action": [
                "cls:GetChart",
                "cls:GetDashboard",
                "cls:ListChart",
                "cls:DescribeDashboards",
                "cls:SearchDashboardSubscribe",
                "cls:DescribeDashboardSubscribes"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
                "cls:DescribeTopics",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeIndex",
                "cls:DescribeLogsets"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        }
    ]
}
```



#### 只读权限：对指定资源的日志主题及仪表盘具备只读权限

用户可以查看**指定仪表盘**。仪表盘可以查看**指定日志主题**的数据。

```
{
    "version": "2.0",
    "statement": [
         {
            "effect": "allow",
            "action": [
                "cls:GetChart",
                "cls:GetDashboard",
                "cls:ListChart",
                "cls:DescribeDashboards",
                "cls:SearchDashboardSubscribe",
                "cls:DescribeDashboardSubscribes"
            ],
            "resource": [
                "qcs::cls::uin/100000***001:dashboard/dashboard-0769a3ba-2514-409d-****-f65b20b23736"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
                "cls:DescribeTopics",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeIndex",
                "cls:DescribeLogsets"
            ],
            "resource": [
                "qcs::cls::uin/100000***001:topic/174ca473-50d0-4fdf-****-2ef681a1e02a"
            ]
        }
    ]
}
```


## 监控告警相关

#### 管理权限：对所有告警策略具备管理权限

用户可以对所有告警策略进行管理，包括创建告警策略、创建通知渠道组和查看告警策略等。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:DescribeAlarms",
                "cls:CreateAlarm",
                "cls:ModifyAlarm",
                "cls:DeleteAlarm",
                "cls:DescribeAlarmNotices",
                "cls:CreateAlarmNotice",
                "cls:ModifyAlarmNotice",
                "cls:DeleteAlarmNotice",
                "cam:ListGroups",
                "cam:DescribeSubAccountContacts",
                "cls:GetAlarmLog",
                "cls:DescribeAlertRecordHistory",
                "cls:CheckAlarmRule",
                "cls:CheckAlarmChannel"
            ],
            "resource": "*"
        }
    ]
}
```

#### 只读权限：对所有告警策略具备只读权限

用户可以查看所有告警策略。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:DescribeAlarms",
                "cls:DescribeAlarmNotices",
                "cls:GetAlarmLog",
                "cls:DescribeAlertRecordHistory",
                "cam:ListGroups",
                "cam:DescribeSubAccountContacts"
            ],
            "resource": "*"
        }
    ]
}
```

## 数据处理

### 数据加工相关

#### 管理权限：对所有数据加工任务具备管理权限

所有日志主题的“数据加工任务”的管理权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeDataTransformPreviewDataInfo",
                "cls:DescribeTopics",
                "cls:DescribeIndex",
                "cls:CreateDataTransform"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:DescribeFunctions",
                "cls:CheckFunction",
                "cls:DescribeDataTransformFailLogInfo",
                "cls:DescribeDataTransformInfo",
                "cls:DescribeDataTransformPreviewInfo",
                "cls:DescribeDataTransformProcessInfo",
                "cls:DeleteDataTransform",
                "cls:ModifyDataTransform"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

#### 只读权限：对所有数据加工任务具备只读权限

所有日志主题的“数据加工任务”的只读权限。由于仅是查看，所以不需要对 DSL 函数进行授权。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:DescribeDataTransformFailLogInfo",
                "cls:DescribeDataTransformInfo",
                "cls:DescribeDataTransformPreviewDataInfo",
                "cls:DescribeDataTransformPreviewInfo",
                "cls:DescribeDataTransformProcessInfo"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

### 定时 SQL 分析相关


#### 管理权限：对所有日志主题具备定时 SQL 分析的权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:SearchLog",
                "cls:DescribeScheduledSqlInfo",
                "cls:DescribeScheduledSqlProcessInfo",
                "cls:CreateScheduledSql",
                "cls:DeleteScheduledSql",
                "cls:ModifyScheduledSql",
                "cls:RetryScheduledSqlTask",
                "cam:ListAttachedRolePolicies"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

#### 管理权限：对指定标签日志主题具备 Kafka 协议消费权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics"
            ],
            "resource": [
                "*"
            ],
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:SearchLog",
                "cls:DescribeScheduledSqlInfo",
                "cls:DescribeScheduledSqlProcessInfo",
                "cls:CreateScheduledSql",
                "cls:DeleteScheduledSql",
                "cls:ModifyScheduledSql",
                "cls:RetryScheduledSqlTask",
                "cam:ListAttachedRolePolicies"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```


## 数据投递/消费相关

### 投递 Ckafka

#### 管理权限：对所有日志主题具备投递 Ckafka 管理权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "cam:AttachRolePolicy",
                "cam:CreateRole",
                "cam:DescribeRoleList",
                "ckafka:DescribeInstances",
                "ckafka:DescribeTopic",
                "ckafka:DescribeInstanceAttributes",
                "cls:modifyConsumer",
                "cls:getConsumer",
                "cls:DescribeConsumer",
                "cls:DescribeConsumerPreview"
            ],
            "resource": "*"
        }
    ]
}
```

#### 管理权限：对指定标签日志主题具备投递 Ckafka 管理权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "age&13",
                        "name&vinson"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "cam:AttachRolePolicy",
                "cam:CreateRole",
                "cam:DescribeRoleList",
                "ckafka:DescribeInstances",
                "ckafka:DescribeTopic",
                "ckafka:DescribeInstanceAttributes",
                "cls:modifyConsumer",
                "cls:getConsumer",
                "cls:DescribeConsumer",
                "cls:DescribeConsumerPreview"
            ],
            "resource": "*"
        }
    ]
}
```

#### 只读权限：对所有日志主题具备投递ckafka只读权限

具备所有日志主题投递 Ckafka 的只读权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "ckafka:DescribeInstances",
                "ckafka:DescribeTopic",
                "ckafka:DescribeInstanceAttributes",
                "cls:getConsumer",
                "cls:DescribeConsumer",
                "cls:DescribeConsumerPreview"
            ],
            "resource": "*"
        }
    ]
}
```

#### 只读权限：对指定标签日志主题具备投递 Ckafka 只读权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "ckafka:DescribeInstances",
                "ckafka:DescribeTopic",
                "ckafka:DescribeInstanceAttributes",
                "cls:getConsumer",
                "cls:DescribeConsumer",
                "cls:DescribeConsumerPreview"
            ],
            "resource": "*"
        }
    ]
}
```

### 投递 COS

#### 管理权限：对所有日志主题具备投递 COS 管理权限

具备所有日志主题投递 COS 的管理权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets",
                "cls:DescribeIndex"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:CreateShipper",
                "cls:ModifyShipper",
                "cls:DescribeShippers",
                "cls:DeleteShipper",
                "cls:DescribeShipperTasks",
                "cls:RetryShipperTask",
                "cls:DescribeShipperPreview",
                "cos:GetService",
                "cam:ListAttachedRolePolicies",
                "cam:AttachRolePolicy",
                "cam:CreateRole",
                "cam:DescribeRoleList"
            ],
            "resource": "*"
        }
    ]
}
```

#### 管理权限：对指定标签日志主题具备投递 COS 管理权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets",
                "cls:DescribeIndex"
            ],
            "resource": "*", 
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:CreateShipper",
                "cls:ModifyShipper",
                "cls:DescribeShippers",
                "cls:DeleteShipper",
                "cls:DescribeShipperTasks",
                "cls:RetryShipperTask",
                "cls:DescribeShipperPreview",
                "cos:GetService",
                "cam:ListAttachedRolePolicies",
                "cam:AttachRolePolicy",
                "cam:CreateRole",
                "cam:DescribeRoleList"
            ],
            "resource": "*"
        }
    ]
}
```

####  只读权限：对所有日志主题具备投递 COS 只读权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets" ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:DescribeShippers",
                "cls:DescribeShipperTasks",
                "cls:RetryShipperTask",
                "cls:DescribeShipperPreview",
                "cam:ListAttachedRolePolicies"
            ],
            "resource": "*"
        }
    ]
}
```

####  只读权限：对指定标签日志主题具备投递 COS 只读权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:DescribeShippers",
                "cls:DescribeShipperTasks",
                "cls:RetryShipperTask",
                "cls:DescribeShipperPreview",
                "cam:ListAttachedRolePolicies"
            ],
            "resource": "*"
        }
    ]
}
```

### 投递 SCF

#### 管理权限：对所有日志主题具备投递 SCF 管理权限

具备所有日志主题投递 SCF 的管理权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "cls:CreateDeliverFunction",
                "cls:DeleteDeliverFunction",
                "cls:ModifyDeliverFunction",
                "cls:GetDeliverFunction",
                "scf:ListFunctions",
                "scf:ListAliases",
                "scf:ListVersionByFunction"
            ],
            "resource": "*"
        }
    ]
}
```

#### 管理权限：对指定标签日志主题具备投递 SCF 管理权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "cls:CreateDeliverFunction",
                "cls:DeleteDeliverFunction",
                "cls:ModifyDeliverFunction",
                "cls:GetDeliverFunction",
                "scf:ListFunctions",
                "scf:ListAliases",
                "scf:ListVersionByFunction"
            ],
            "resource": "*"
        }
    ]
}
```

#### 只读权限：对所有日志主题具备投递 SCF 只读权限

具备所有日志主题投递 SCF 的只读权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "cls:GetDeliverFunction",
                "scf:ListFunctions",
                "scf:ListAliases",
                "scf:ListVersionByFunction"
            ],
            "resource": "*"
        }
    ]
}
```

#### 只读权限：对指定标签日志主题具备投递 SCF 只读权限

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cam:ListAttachedRolePolicies",
                "cls:GetDeliverFunction",
                "scf:ListFunctions",
                "scf:ListAliases",
                "scf:ListVersionByFunction"
            ],
            "resource": "*"
        }
    ]
}
```

### Kafka 协议消费

#### 管理权限：对所有日志主题具备 Kafka 协议消费权限

具备所有日志主题 Kafka 协议消费权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics"
            ],
            "resource": [
                "*"]
     },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:DescribeKafkaConsumer",
                "cls:CloseKafkaConsumer",
                "cls:ModifyKafkaConsumer",
                "cls:OpenKafkaConsumer",
                "cam:ListAttachedRolePolicies"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

#### 管理权限：对指定标签日志主题具备 Kafka 协议消费权限

具备指定标签日志主题 Kafka 协议消费的管理权限。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeLogsets",
                "cls:DescribeTopics"
            ],
            "resource": [
                "*"
            ],
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "tag:DescribeResourceTagsByResourceIds",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues",
                "cls:DescribeKafkaConsumer",
                "cls:CloseKafkaConsumer",
                "cls:ModifyKafkaConsumer",
                "cls:OpenKafkaConsumer",
                "cam:ListAttachedRolePolicies"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

## 开发者相关 

### CLS 对接 Grafana

#### 通过 Grafana 展示所有日志主题的数据

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

#### 通过 Grafana 展示具备指定标签的日志主题的数据

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog"
            ],
            "resource": [
                "*"
            ],
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "key&value"
                    ]
                }
            }
        }
    ]
}
```
