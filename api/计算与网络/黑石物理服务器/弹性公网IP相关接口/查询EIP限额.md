## 1. 接口描述
该接口用于查询当前已使用的EIP限额状况，默认同一个客户可以申请的EIP的总数量上限为100个。
 
域名: <font style="color:red">bmeip.api.qcloud.com</font>
接口名: DescribeEipBmQuota

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
|无|-|-|-|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回限额信息，具体结构描述如下 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.eipNumQuota | Int | 能申请EIP个数的总配额 | 
| data.currentEipNum | Int | 当前已使用的EIP个数，包括创建中、绑定中、已绑定、解绑中、未绑定集中状态的EIP总和| 
| data.dailyApplyQuota | Int | 日申请EIP的次数限制| 
| data.dailyApplyCount | Int | 当天申请EIP次数| 

## 4. 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9006|InternalErr|内部数据操作异常|

## 5. 示例
 
输入
<pre>

  https://bmeip.api.qcloud.com/v2/index.php?
  &Action=DescribeEipBmQuota
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```

{
    "code": 0,
    "message": "",
    "data": {
        "eipNumQuota": 20,
        "currentEipNum": 2,
        "dailyApplyQuota": 10,
        "dailyApplyCount": 7,
        "dailyAllocWanIpQuota": 10,
        "dailyAllocWanIpCount": 2    
    }
}

```

