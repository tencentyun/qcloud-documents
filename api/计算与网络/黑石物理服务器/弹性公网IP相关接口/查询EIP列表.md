## 1. 接口描述
该接口用于查询当前使用中的弹性公网IP列表。

域名: <font style="color:red">bmeip.api.qcloud.com</font>
接口名: DescribeEipBm

## 2. 输入参数
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipIds.n|否|String|EIP实例ID列表，数组下标从0开始|
| eips.n|否|String|EIP列表，数组下标从0开始|
| unInstanceIds.n|否|String|服务器实例ID列表，数组下标从0开始，可通过[DescribeDevice](/doc/api/456/6728)接口返回字段中的instanceId获取|
| searchKey|否|String|EIP实例名称，模糊匹配|
| status.n|否|Int|状态列表，数组下标从0开始<br>0：创建中； 1：绑定中；2：已绑定；3：解绑中； 4：未绑定； 6：下线中； 9：创建失败|
| offset | 否 | Int | 偏移量，默认为0|
| limit | 否 | Int | 返回EIP数量，默认 20, 最大值 100|
| orderBy | 否 | String | 排序字段，支持这些字段名：eipId, eip, status, unInstanceId, arrears, createdAt。[查看说明](#datastruct)|
| orderType | 否 | Int | 1倒序，0顺序，默认倒序|
|vpcId|否|Int|EIP所属vpcId，会筛选出指定vpc的EIP，可通过[查询私有网络列表](/document/product/386/6646)返回的字段vpcId获得|
|payMode|否|字符串型|计费模式，流量计费：flow，带宽计费：bandwidth|

 > 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset进行分页查询；比如我想查询第110~149 这40条记录，则可以设置 offset=110，limit=40。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message | String | 错误信息 |
| codeDesc | String | 错误码描述 |  
|  totalCount  |  Int |  返回符合过滤条件的EIP数量；假如指定limit，offset，该值有可能大于data数组中的数量 |
| data |   Array | 返回EIP实例列表，具体结构描述如下 |

<span id="datastruct">data结构</span>

|参数名称|类型|描述|
|---|---|---|
| data.eipSet | Array | 返回EIP信息数组|
| data.eipSet.eipId | String | EIP实例ID|
| data.eipSet.eipName | String | EIP名称|
| data.eipSet.eip | String | EIP地址|
| data.eipSet.ispId | Int | 运营商ID 0：电信； 1：联通； 2：移动； 3：教育网； 4：盈科； 5：BGP； 6：香港|
| data.eipSet.status | Int | 状态 0：创建中； 1：绑定中； 2：已绑定； 3：解绑中； 4：未绑定； 6：下线中； 9：创建失败|
| data.eipSet.arrears | Int | 是否欠费隔离 1： 欠费隔离； 0： 正常。处在欠费隔离情况下的EIP不能进行任何管理操作。|
| data.eipSet.unInstanceId | String | EIP所绑定的服务器实例ID，未绑定则为空|
| data.eipSet.freeAt | String | EIP解绑时间|
| data.eipSet.createdAt | String | EIP创建时间|
| data.eipSet.updatedAt | String | EIP更新时间|
| data.eipSet.freeSecond | Int | EIP未绑定服务器时长（单位：秒）|
| data.eipSet.payMode | String | EIP计费模式，"flow"：流量计费； "bandwidth"：带宽计费|
| data.eipSet.bandwidth | Int | EIP带宽计费模式下的带宽上限（单位：MB）|
| data.eipSet.latestPayMode | String | 最近一次操作变更的EIP计费模式，"flow"：流量计费； "bandwidth"：带宽计费 |
| data.eipSet.latestBandwidth | Int | 最近一次操作变更的EIP计费模式对应的带宽上限值，仅在带宽计费模式下有效（单位：MB）|

## 4. 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|


## 5. 示例
 
输入
<pre>

  https://bmeip.api.qcloud.com/v2/index.php?
  &Action=DescribeEipBm
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>&startNum=0&endNum=20
</pre>

输出
```

{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": {
		"eipSet": [{
			"eipId": "eip-qcloudbm",
			"eipName": "",
			"eip": "111.111.111.111",
			"ispId": 5,
			"status": 4,
			"arrears": 0,
			"unInstanceId": "",
			"freeAt": "2016-10-13 11:23:19",
			"createdAt": "2016-10-13 11:23:18",
			"updatedAt": "2016-10-13 11:23:19",
			"freeSecond": 3600,
			"type": null,
			"payMode": "bandwidth",
			"bandwidth": 10,
			"latestPayMode": "flow",
			"latestBandwidth": 0
		}]
    },
    "totalCount": 1
}

```

