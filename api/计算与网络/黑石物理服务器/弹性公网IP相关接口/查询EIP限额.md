>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
DescribeEipBmQuota 接口用于查询当前已使用的EIP限额状况，默认同一个客户可以申请的EIP的总数量上限为100个，如需提高该上限值，请联系售后同学处理。
 
接口访问域名: bmeip.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipBmQuota
	&<公共请求参数>
```
### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 EipBmBindVpcIp。该接口没有需要显式传入的参数，仅使用公共请求参数即可。

|参数名称|必选|类型|描述|
|-------|----|---|----|
|无|-|-|-|


## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipNumQuota": 100,
        "currentEipNum": 0,
        "dailyApplyCount": 0,
        "dailyApplyQuota": 200
    }
}
```
### 响应参数

响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的接口内容。

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回限额信息，具体结构描述如下 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.eipNumQuota | Int | 能拥有的EIP个数的总配额，默认是100个 | 
| data.currentEipNum | Int | 当前已使用的EIP个数，包括创建中、绑定中、已绑定、解绑中、未绑定几种状态的EIP个数总和| 
| data.dailyApplyQuota | Int | 每日申请EIP的次数限制| 
| data.dailyApplyCount | Int | 当天申请EIP次数|

## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9006|InternalErr|内部数据操作异常|

## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=DescribeEipBmQuota
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=6791
	&Timestamp=1507777243
	&Region=bj
	&Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipNumQuota": 100,
        "currentEipNum": 0,
        "dailyApplyCount": 0,
        "dailyApplyQuota": 200
    }
}

```

