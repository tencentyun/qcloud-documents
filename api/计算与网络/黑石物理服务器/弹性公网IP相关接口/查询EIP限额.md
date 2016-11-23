## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: DescribeEipBmQuota

查询EIP限额。

## 2. 输入参数
 
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
|无|-|-|-|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |
|  totalCount  |  Int |  返回符合过滤条件的EIP数量；假如指定limit，offset，该值有可能大于data数组中的数量 |
| data |   Array | 返回数组 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.eipNumQuota | Int | 能申请EIP个数的总配额 | 
| data.currentEipNum | Int | 当前EIP个数| 
| data.dailyApplyQuota | Int | 日申请EIP的次数限制| 
| data.dailyApplyCount | Int | 当天申请EIP次数| 
| data.dailyAllocWanIpQuota | Int | 日解绑EIP时重新分配普通公网IP的次数限制| 
| data.dailyAllocWanIpCount | Int | 当天解绑EIP并重新分配普通公网IP次数 |

## 4. 示例
 
输入
<pre>

  https://eip.api.qcloud.com/v2/index.php?
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

