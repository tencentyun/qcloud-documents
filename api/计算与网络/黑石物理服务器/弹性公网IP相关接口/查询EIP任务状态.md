>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
EipBmQueryTask 接口用于查询弹性公网IP异步任务的状态，主要用于绑定，解绑等操作的进度状态查询。
 
接口访问域名: bmeip.api.qcloud.com



## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmQueryTask
	&<公共请求参数>
	&requestId=<EIP异步任务ID>
```
### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 EipBmQueryTask。

|参数名称|必选|类型|描述|
|-------|----|---|----|
| requestId|是|Int|EIP异步任务返回的requestId，可以参考[EipBmDelete](/document/product/386/6676)的响应参数|

## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "status": "<当前任务状态码>"
    }
}
```
### 响应参数
响应参数部分包含两层结构，外层展示接口的响应结果，内层展示具体的任务状态信息。

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息，具体的错误原因描述信息 |
| data |   Array | 返回数组 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.status | Int | 当前任务状态码：0-成功，1-失败，2-进行中|

## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|-8000|DesErr|流程系统异常|
|-8001|DesInBusy|系统繁忙|

## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=EipBmQueryTask
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=58353
	&Timestamp=1507773572
	&Region=bj
	&requestId=2383049
	&Signature=Yc7WOhUf5KWLDtyL296v%2FotywN0%3D
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "status": 0
    }
}

```

