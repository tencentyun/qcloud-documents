## 1. 接口描述
该接口用于申请创建黑石弹性公网IP。
 
域名: <font style="color:red">bmeip.api.qcloud.com</font>
接口名: EipBmApply

 

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| goodsNum | 否 | Int | 创建的EIP数量，默认为1，最大20 |
| payMode | 否 | String | 创建的EIP计费模式，"flow"：流量计费；"bandwidth"：带宽计费（单位：MB）|
| bandwidth | 否 | Int | EIP为带宽计费时，选择的带宽上线（单位：MB，当前最大为1000MB）|
| vpcId | 是 | Int | 申请的EIP归属的VPC的ID，可通过[查询私有网络列表](/document/product/386/6646)返回的字段vpcId获得 |

 > 平台对用户每地域能申请的EIP最大配额有所限制。上述配额可通过[DescribeEipBmQuota](/doc/api/456/6668)接口获取。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回申请的eip实例对应的异步任务信息，具体结构描述如下 |

data结构

|参数名称|类型|描述|
|---|---|---|
| data.eipIds | Array | 返回申请中的EIP实例ID列表|
| data.requestId | Int | 绑定黑石物理机异步任务ID，可以通过[EipBmQueryTask](/doc/api/456/6670)查询任务状态|

## 4. 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30001|ExceedTheLimit|申请总数超过限额|
|30003|ExceedDailyLimit|当日申请数超限额|
|30016|ISPInvalid|ISP非法|


## 5. 示例
 
输入
```

  https://bmeip.api.qcloud.com/v2/index.php?
  &Action=EipBmApply
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>&goodsNum=2&payMode=flow&vpcId=1
```

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipIds": [
            "eip-qcloudv5"
        ],
        "requestId": 2382031
    }
}

```

