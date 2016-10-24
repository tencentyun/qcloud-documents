## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: EipBmBindRs

用于绑定黑石弹性公网IP到黑石物理服务器。

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipId | 否 | String | EIP实例ID |
| instanceId | 否 | String | 服务器实例ID，可通过[DescribeInstances]()接口返回字段中的unInstanceId获取|

 > 已绑定到NAT网关的物理机，目前暂不支持同时绑定EIP

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码]()。 |
| message |   String | 错误信息 |
| data |   Array | 返回数组 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 绑定黑石物理机异步任务ID，可以通过[EipBmQueryTask]()查询任务状态|

## 4. 示例
 
输入
```

  https://eip.api.qcloud.com/v2/index.php?
  &<公共请求参数>
  &instanceId=cpm-xxxxxx&eipId=eip-vvvvvvv

```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 100000
    }
}

```

