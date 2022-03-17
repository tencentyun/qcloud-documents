本文档为日志服务（Cloud Log Service，CLS）功能和其对应的管理权限和只读权限的授权策略。用户可根据需要授权的 CLS 功能，填写相对应的授权策略语句。

## 授权操作步骤

授权主要分为三个步骤：主账号创建自定义策略、主账号（CompanyExample）给子账号（Developer）授权日志主题（TopicA）的所有权限、子账号 Developer 访问 CLS 日志服务。其主账号创建自定义策略的步骤详情如下：

1. 使用主账号（CompanyExample）登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
3. 在左侧导航中，单击**策略**，进入策略管理页面。
4. 单击**新建自定义策略**。
5. 在弹出的窗口中，选择**按策略语法创建**。
6. 在按策略语法创建页面，选择**空白模版**，单击**下一步**。
7. 在编辑策略页面，设置策略名称和策略内容，单击**完成**。
例如，策略名称为 CLS-TopicA-Access。策略内容可参考如下内容进行设置：


## 数据采集相关

### 机器安装 Loglistener 上传日志最小权限

```
{
"version": "2.0",
"statement": [
  {
      "action": [
         "cls:pushlog",
         "cls:listLogset",
         "cls:getConfig",
         "cls:agentHeartBeat"
     ],
      "resource": "*",
      "effect": "allow"
  }
]
}
```

### Loglistener 采集规则配置

#### 管理权限

- 具备所有日志主题采集规则的管理权限。
```
{
"version": "2.0",
"statement": [
  {
  "action": [
         "cls:DescribeLogsets",
         "cls:DescribeConfigs",
         "cls:ModifyConfig",
         "cls:DescribeIndex",
         "cls:DescribeIndex",
         "cls:ModifyIndex"
                ],
   "resource": [
                "*"
            ],
   "effect": "allow"
  }
]
}
```
- 具备指定标签的日志主题采集规则管理权限。
```
{
    "version": "2.0",
    "statement": [
        {
        "action": [
                     "cls:DescribeLogsets",
                     "cls:DescribeConfigs",
                     "cls:ModifyConfig",
                     "cls:DescribeIndex",
                     "cls:DescribeIndex",
                     "cls:ModifyIndex"
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
            },
         "effect": "allow"
        }
    ]
}
```

#### 只读权限

- 具备所有日志主题采集规则的只读权限。
```
{
"version": "2.0",
"statement": [
  {
     "action": [
         "cls:DescribeLogsets",
         "cls:DescribeConfigs",
         "cls:DescribeIndex",
         "cls:DescribeIndex"
                ]
   "resource": [
                "*"
            ],
   "effect": "allow"
  }
]
}
```
- 具备指定标签的日志主题采集规则只读权限。
```
{
"version": "2.0",
"statement": [
  {
     "effect": "allow",
     "action": [
         "cls:DescribeLogsets",
         "cls:DescribeConfigs",
         "cls:DescribeIndex",
         "cls:DescribeIndex"
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

### API 上传日志最小权限

```
{
	"version": "2.0",
	"statement": [
  	{
      "action": [
                "cls:CreateTopic",
                "cls:CreateLogset",
                "cls:UploadLog",
            ],
      "resource": "*",
      "effect": "allow"
  	}
]
}
```

## 检索分析相关

### 使用控制台检索日志

#### 管理权限

- 全部日志主题具备控制台检索日志的管理权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeAsyncContextResult",
                "cls:DescribeAsyncSearchResult",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeLatestJsonLog",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLogHistogram",
                "cls:DescribePartitions",
                "cls:DescribeTopics",
                "cls:GetFastAnalysis",
                "cls:GetHistogram",
                "cls:GetLog",
                "cls:SearchLog",
                "cls:ShowContext",
                "cls:getIndex",
                "cls:getLogset",
                "cls:getTopic",
                "cls:searchLog",
                "cls:DescribeAsyncContextTasks",
                "cls:DescribeAsyncSearchTasks",
                "cls:DescribeLogsets",
                "cls:listLogset",
                "cls:listTopic",
                "cls:listPartitions",
                "cls:CreateAsyncContextTask",
                "cls:CreateAsyncSearchTask",
                "cls:CreateExport",
                "cls:CreateIndex",
                "cls:DeleteAsyncContextTask",
                "cls:DeleteAsyncSearchTask",
                "cls:DeleteExport",
                "cls:DeleteIndex",
                "cls:DeleteLogset",
                "cls:DeleteTopic",
                "cls:MergePartition",
                "cls:ModifyIndex",
                "cls:ModifyLogset",
                "cls:ModifyTopic",
                "cls:SplitPartition",
                "cls:deleteLogset",
                "cls:deleteTopic",
                "cls:downloadLog",
                "cls:modifyIndex",
                "cls:modifyLogset",
                "cls:modifyTopic",
                "cls:updatePartition",
                "cls:GetDeliverFunction",
                "cls:CreateLogset",
                "cls:CreateTopic",
                "cls:createLogset",
                "cls:createTopic"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```
- 某个标签的日志主题具备控制台检索日志的管理权限。
>! 配置时，需同时为日志主题和日志集绑定标签。
>
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeAsyncContextResult",
                "cls:DescribeAsyncSearchResult",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeLatestJsonLog",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLogHistogram",
                "cls:DescribePartitions",
                "cls:DescribeTopics",
                "cls:GetFastAnalysis",
                "cls:GetHistogram",
                "cls:GetLog",
                "cls:SearchLog",
                "cls:ShowContext",
                "cls:getIndex",
                "cls:getLogset",
                "cls:getTopic",
                "cls:searchLog",
                "cls:DescribeAsyncContextTasks",
                "cls:DescribeAsyncSearchTasks",
                "cls:DescribeLogsets",
                "cls:listLogset",
                "cls:listTopic",
                "cls:listPartitions",
                "cls:CreateAsyncContextTask",
                "cls:CreateAsyncSearchTask",
                "cls:CreateExport",
                "cls:CreateIndex",
                "cls:DeleteAsyncContextTask",
                "cls:DeleteAsyncSearchTask",
                "cls:DeleteExport",
                "cls:DeleteIndex",
                "cls:DeleteLogset",
                "cls:DeleteTopic",
                "cls:MergePartition",
                "cls:ModifyIndex",
                "cls:ModifyLogset",
                "cls:ModifyTopic",
                "cls:SplitPartition",
                "cls:deleteLogset",
                "cls:deleteTopic",
                "cls:downloadLog",
                "cls:modifyIndex",
                "cls:modifyLogset",
                "cls:modifyTopic",
                "cls:updatePartition",
                "cls:GetDeliverFunction"
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

#### 只读权限

- 对某个标签的日志主题控制台检索具有只读权限。
>! 配置时，需同时为日志主题和日志集绑定标签。
>
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeAsyncContextResult",
                "cls:DescribeAsyncSearchResult",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeLatestJsonLog",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLogHistogram",
                "cls:DescribePartitions",
                "cls:DescribeTopics",
                "cls:GetFastAnalysis",
                "cls:GetHistogram",
                "cls:GetLog",
                "cls:SearchLog",
                "cls:ShowContext",
                "cls:getIndex",
                "cls:getLogset",
                "cls:getTopic",
                "cls:searchLog",
                "cls:DescribeAsyncContextTasks",
                "cls:DescribeAsyncSearchTasks",
                "cls:DescribeLogsets",
                "cls:listLogset",
                "cls:listTopic",
                "cls:listPartitions"
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
- 对所有日志主题控制台的检索具备只读权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeAsyncContextResult",
                "cls:DescribeAsyncSearchResult",
                "cls:DescribeExports",
                "cls:DescribeIndex",
                "cls:DescribeLatestJsonLog",
                "cls:DescribeLogContext",
                "cls:DescribeLogFastAnalysis",
                "cls:DescribeLogHistogram",
                "cls:DescribePartitions",
                "cls:DescribeTopics",
                "cls:GetFastAnalysis",
                "cls:GetHistogram",
                "cls:GetLog",
                "cls:SearchLog",
                "cls:ShowContext",
                "cls:getIndex",
                "cls:getLogset",
                "cls:getTopic",
                "cls:searchLog",
                "cls:DescribeAsyncContextTasks",
                "cls:DescribeAsyncSearchTasks",
                "cls:DescribeLogsets",
                "cls:listLogset",
                "cls:listTopic",
                "cls:listPartitions"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

### 可视化仪表盘

#### 管理权限

- 所有日志主题的仪表盘具备管理权限。
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
                "cls:ListDashboard"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
                "cls:DescribeTopics",
                "cls:DescribeLogsets"
            ],
            "resource": "*"
        }
    ]
}
```
- 指定标签的日志主题的仪表盘具备管理权限。
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
                "cls:DeleteChart",
                "cls:DeleteDashboard",
                "cls:ModifyChart",
                "cls:ModifyDashboard"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:ListDashboard"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
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
        }
    ]
}
```

#### 只读权限

- 所有日志主题的仪表盘具备只读权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:GetChart",
                "cls:GetDashboard",
                "cls:ListChart"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:ListDashboard"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
                "cls:DescribeTopics"
            ],
            "resource": "*"
        }
    ]
}
```
- 指定标签日志主题的仪表盘具备只读权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:GetChart",
                "cls:GetDashboard",
                "cls:ListChart"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:ListDashboard"
            ],
            "resource": "*"
        },
        {
            "effect": "allow",
            "action": [
                "cls:SearchLog",
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
        }
    ]
}
```

## 监控告警相关

#### 管理权限

- 具备所有日志主题监控告警的管理权限。
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
- 具备指定标签的日志主题监控告警管理权限（监控告警暂未完整支持按标签管理权限）。
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
                        "testCAM&test1"
                    ]
                }
            }
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

#### 只读权限

- 具备所有日志主题监控告警的只读权限。
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
- 具备指定标签的日志主题监控告警的只读权限（监控告警暂未完整支持按标签管理权限）。
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
                        "testCAM&test1"
                    ]
                }
            }
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

## 数据流出相关

### 投递 Ckafka

#### 管理权限

- 具备所有日志主题投递 Ckafka 的管理权限。
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
                "cls:modifyConsumer",
                "cls:getConsumer"
            ],
            "resource": "*"
        }
    ]
}
```
- 具备指定标签日志主题投递 Ckafka 的管理权限。
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
                "ckafka:DescribeInstances",
                "ckafka:DescribeTopic",
                "ckafka:DescribeInstanceAttributes",
                "cls:modifyConsumer",
                "cls:getConsumer"
            ],
            "resource": "*"
        }
    ]
}
```

#### 只读权限

- 具备所有日志主题投递 Ckafka 的只读权限。
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
                "cls:getConsumer"
            ],
            "resource": "*"
        }
    ]
}
```
- 具备指定标签日志主题投递 Ckafka 的只读权限。
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
                "cls:getConsumer"
            ],
            "resource": "*"
        }
    ]
}
```

### 投递 COS

#### 管理权限

- 具备所有日志主题投递 COS 的管理权限。
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
                "cam:ListAttachedRolePolicies",
                "cos:GetService",
            ],
            "resource": "*"
        }
    ]
}
```
- 具备指定标签日志主题投递 COS 的管理权限。
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
                "cam:ListAttachedRolePolicies",
                "cos:GetService",
            ],
            "resource": "*"
        }
    ]
}
```

#### 只读权限

- 具备所有日志主题投递 COS 的只读权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"            ],
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
                "cam:ListAttachedRolePolicies"
            ],
            "resource": "*"
        }
    ]
}
```
- 具备指定标签日志主题投递 COS 的只读权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:DescribeTopics",
                "cls:DescribeLogsets"            ],
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
                "cam:ListAttachedRolePolicies"
            ],
            "resource": "*"
        }
    ]
}
```

### 投递 SCF

#### 管理权限

- 具备所有日志主题投递 SCF 的管理权限。
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
- 具备指定标签日志主题投递 SCF 的管理权限。
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

#### 只读权限

- 具备所有日志主题投递 SCF 的只读权限。
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
- 具备指定标签日志主题投递 SCF 的只读权限。
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

## 开发者相关

### Grafana 配置

-  具备所有日志主题 grafana 展示权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:searchLog"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```
- 具备指定标签日志主题 grafana 展示权限。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:searchLog"
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

