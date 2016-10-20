## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: DescribeEipBm

查询弹性公网IP。

 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipIds.n|否|数组型|EIP实例ID列表，可以通过[DescribeEipBm]()接口查询，数组下标从0开始|
| payMode|是|String|EIP计费方式：flow-流量计费；bandwidth-带宽计费|
| bandwidth|否|Int|带宽上限（该字段只在带宽计费模式下生效），单位MB，最小为0


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
  &<公共请求参数>&eipIds.0=eip-test&payMode=bandwidth&bandwidth=40
```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 2383050
    }
}
```

