## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: EipBmDelete

释放弹性公网IP。

 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipIds.n|否|数组型|EIP实例ID列表，可以通过[DescribeEipBm](/doc/api/456/6671)接口查询，数组下标从0开始|

 > 绑定状态的EIP不可以释放，只可以释放未绑定状态的EIP。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回数组 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 绑定黑石物理机异步任务ID，可以通过[EipBmQueryTask](/doc/api/456/6670)查询任务状态|

## 4. 示例
 
输入
```

  https://eip.api.qcloud.com/v2/index.php?
  &Action=EipBmDelete
  &<公共请求参数>&eipIds.0=eip-iiiii
```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 2383049
    }
}

```

