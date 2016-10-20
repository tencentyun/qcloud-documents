## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: EipBmApply

创建黑石弹性公网IP。

 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| goodsNum | 否 | Int | 创建的EIP数量，默认为1，最大20 |
| payMode | 否 | String | 创建的EIP计费模式，"flow"：流量计费；"bandwidth"：带宽计费（单位：MB）|
| bandwidth | 否 | Int | EIP为带宽计费时，选择的带宽上线（单位：MB，当前最大为1000MB）|
| vpcId | 否 | Int | 申请的EIP归属的VPC的ID |

 > 平台对用户每地域能申请的EIP最大配额有所限制。上述配额可通过[DescribeEipBmQuota]()接口获取。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码]()。 |
| message |   String | 错误信息 |
| data |   Array | 返回数组 |

data结构

|参数名称|类型|描述|
|---|---|---|
| data.eipIds | Array | 返回申请中的EIP实例ID列表|

## 4. 示例
 
输入
```

  https://eip.api.qcloud.com/v2/index.php?
  &<公共请求参数>
```

输出
```

{
    "code": 0,
    "message": "",
    "data": {
        "eipIds": [
            "eip-m44ku5d2"
        ]
    }
}

```

