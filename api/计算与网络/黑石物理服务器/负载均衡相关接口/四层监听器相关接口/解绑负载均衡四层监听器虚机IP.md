>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
 
UnbindBmL4ListenerVmIp 提供了解绑黑石负载均衡四层监听器虚机IP功能。

接口请求域名：bmlb.api.qcloud.com

## 请求
### 请求示例
```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=UnbindBmL4ListenerVmIp
	&<公共请求参数>
	&loadBalancerId=<负载均衡实例ID>
	&listenerId=<四层监听器ID>
	&vmList.0.port=<待解绑的虚机端口>
	&vmList.0.vmIp=<待解绑的虚机IP>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/product/386/6718)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| loadBalancerId | 是 | String |   负载均衡实例ID，可通过接口[DescribeBmLoadBalancers](/document/product/386/9306)查询。|
| listenerId | 是 | String | 负载均衡四层监听器ID，可通过接口[DescribeBmListeners](/document/product/386/9296)查询。|
| vmList | 是 | Array |   待解绑的虚机信息。|

vmList描述待解绑的虚机信息，n为下标，vmList包含字段如下

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|vmList.n.port|是|Int|待解绑的虚机端口，可选值1~65535。|
|vmList.n.vmIp|是|String|待解绑的虚机IP。|

## 响应

### 响应示例
```
{
 "code": 0,
 "message": "",
 "codeDesc": "Success",
 "requestId": "<异步任务ID>"
}
```

### 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/document/product/386/6725)。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 返回码信息描述。|
| requestId | Int | 任务ID。该接口为异步任务，可根据本参数调用[DescribeBmLoadBalancersTaskResult](/document/product/386/9308)接口来查询任务操作结果|


## 错误码

| 错误代码 | 英文提示 | 错误描述 |
|------|------|------|
| 9003 | InvalidParameter | 参数错误 |
| 9006 | InternalError.CCDBAbnormal | CCDB 服务异常 |
| 11041 | InvalidParameter.CCDBLBNotExist | CCDB中不存在该负载均衡记录信息 |
| 12003 | IncorrectStatus.LBWrongStatus | 该负载均衡状态不正确,无法执行当前操作 |
| -21001 | InvalidStatus.LBInvalidStatus | 当前负载均衡状态不允许此操作 |
| -12023 | InvalidL4Listener.NotExist | CCDB中不存在该四层监听器 |
| 11060 | InternalError.TGWAbnormal | TGW 服务异常 |



## 实际案例
### 输入
```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=UnbindBmL4ListenerVmIp
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=61431
	&Timestamp=1507728683
	&Region=bj
	&loadBalancerId=lb-abcdefgh
	&listenerId=lbl-abcdefgh
	&vmList.0.port=1234
	&vmList.0.vmIp=1.1.1.1
	&Signature=umZFAAWKzjXEQp4ySgrWAoWOHKI%3D
```

### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId" : 1234
}

```
