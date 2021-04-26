## 简介

[访问管理](https://cloud.tencent.com/document/product/598)（Cloud Access Management，CAM）是腾讯云提供的 Web 服务，主要用于帮助用户安全管理腾讯云账户下资源的访问权限。用户可以通过 CAM 创建、管理和销毁用户（组），并使用身份管理和策略管理控制其他用户使用腾讯云资源的权限，CAM 策略的详细信息及使用请参见 [CAM 策略](https://cloud.tencent.com/document/product/598/10601)  文档。

主账号可以授权子账号或协作者访问管理权限，访问指定的日志服务资源，资源详情请参见 [操作列表](https://cloud.tencent.com/document/product/614/35567) 和 [资源列表](https://cloud.tencent.com/document/product/614/35566) 文档。

>!
> - 为保证使用安全，建议将授权的权限控制在需求范围内的最小权限。
> - list 类型的操作，表示可以查看所有资源，暂不支持仅查看一部分资源。例如，当具备 listTopic 权限时，可以查看当前日志集下所有日志主题列表，不支持列表里只显示部分日志主题。反之，当不具备 listTopic 权限时，无法查看任何日志主题。


## 操作示例
#### 控制台场景：日志服务所有权限

场景说明：主账号（UIN 为123456789）授权子账号或协作者可在 [日志服务控制台](https://console.cloud.tencent.com/cls) 访问和操作日志服务。

CAM 授权策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "cls:*"
            ],
            "resource": "*",
            "effect": "allow"
        }
    ]
}
```



#### 控制台场景：日志集和日志主题的只读权限

场景说明：主账号（UIN 为123456789）授权子账号或协作者可在 [日志服务控制台](https://console.cloud.tencent.com/cls) 进行以下操作：

- 子账号或协作者可以查看主账号的日志集列表。
- 子账号或协作者可以查看上海日志集（abcd0000-abcd-abcd-abcd-abcd11110000）的基本信息和所属日志主题列表。
- 子账号或协作者可以查看当前日志集下日志主题（123e4567-e89b-12d3-a456-426655440000）的基本信息，包括采集配置信息、索引配置信息、投递配置信息和投递任务列表。

CAM 授权策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:listLogset"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:logset/*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:list*",
                "cls:get*"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:logset/abcd0000-abcd-abcd-abcd-abcd11110000",
                "qcs::cls:ap-shanghai:uin/123456789:topic/123e4567-e89b-12d3-a456-426655440000"
            ]
        }
    ]
}
```



#### 控制台场景：机器组的只读权限

场景说明：主账号（UIN 为123456789）授权子账号或协作者可在 [日志服务控制台](https://console.cloud.tencent.com/cls) 进行以下操作：
- 子账号或协作者可以查看主账号的机器组列表。
- 子账号或协作者可以查看上海所有机器组的信息，包括机器列表和活跃状态。

CAM 授权策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:listMachineGroup",
                "cls:getMachineGroup",
                "cls:getMachineStatus"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:machinegroup/*"
            ]
        }
    ]
}
```



#### 控制台场景：日志主题检索权限

场景说明：主账号（UIN 为123456789）授权子账号或协作者可在 [日志服务控制台](https://console.cloud.tencent.com/cls) 对主账号上海地域的日志集（abcd0000-abcd-abcd-abcd-abcd11110000）下的日志主题（123e4567-e89b-12d3-a456-426655440000）进行检索。

CAM 授权策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:listLogset"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:logset/*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:listTopic"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:logset/abcd0000-abcd-abcd-abcd-abcd11110000"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:searchLog"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:logset/abcd0000-abcd-abcd-abcd-abcd11110000",
                "qcs::cls:ap-shanghai:uin/123456789:topic/123e4567-e89b-12d3-a456-426655440000"
            ]
        }
    ]
}
```



#### 控制台场景：日志主题投递任务执行详情查询权限

场景说明：主账号（UIN 为123456789）授权子账号或协作者可在 [日志服务控制台](https://console.cloud.tencent.com/cls) 对主账号日志集（abcd0000-abcd-abcd-abcd-abcd11110000）下日志主题（123e4567-e89b-12d3-a456-426655440000）的投递任务（1234abcd-0000-0000-0000-1234abcd0000）进行查看。

CAM 授权策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:listLogset"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:logset/*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:listTopic"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:logset/abcd0000-abcd-abcd-abcd-abcd11110000"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:listShipper"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:topic/123e4567-e89b-12d3-a456-426655440000"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "cls:listShipperTask"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:shipper/1234abcd-0000-0000-0000-1234abcd0000"
            ]
        }
    ]
}
```


#### API 场景：日志主题的写入和下载权限

场景说明：主账号（UIN 为123456789）授权子账号或协作者可使用 [API](https://cloud.tencent.com/document/product/614/16907) 接口进行以下操作：

- 子账号或协作者可以往主账号的日志主题（123e4567-e89b-12d3-a456-426655440000）里写数据。
- 子账号或协作者可以下载主账号的日志主题（123e4567-e89b-12d3-a456-426655440000）数据。

CAM 授权策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cls:getCursor",
                "cls:downloadLog",
                "cls:pushLog"
            ],
            "resource": [
                "qcs::cls:ap-shanghai:uin/123456789:topic/123e4567-e89b-12d3-a456-426655440000"
            ]
        }
    ]
}
```
