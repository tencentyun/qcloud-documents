>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
 
UnbindBmL7LocationVmIp 提供了解绑黑石负载均衡七层转发路径虚机IP功能。

接口请求域名：bmlb.api.qcloud.com


## 请求
### 请求示例

```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=UnbindBmL7LocationVmIp
	&<公共请求参数>
	&loadBalancerId=<负载均衡实例ID>
	&listenerId=<七层监听器实例ID>
	&domainId=<转发域名实例ID>
	&locationId=<转发路径实例ID>
	&vmList.0.port=<待解绑的虚机端口>
	&vmList.0.vmIp=<待解绑的虚机IP>
```

### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 UnbindBmL7LocationVmIp。

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| loadBalancerId | 是 | String |   负载均衡实例ID，可通过接口[DescribeBmLoadBalancers](/document/product/386/9306)查询。|
| listenerId | 是 | String | 七层监听器实例ID，可通过接口[DescribeBmForwardListeners](/document/product/386/9283)查询。|
| domainId | 是 | String |   转发域名实例ID，可通过接口[DescribeBmForwardRules](/document/product/386/9285)查询。|
| locationId | 是 | String |   转发路径实例ID，可通过接口[DescribeBmForwardRules](/document/product/386/9285)查询。|
| vmList | 是 | Array |   待解绑的主机信息。|

vmList描述待绑定的主机信息，n为下标，vmList包含字段如下

| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|vmList.n.port|是|Int|待解绑的虚机端口，可选值1~65535。|
|vmList.n.vmIp|是|String|待解绑的虚机IP。|


## 响应
### 响应示例

```
{
 "code": 0,
 "message": "",
 "codeDesc": "Success"
}
```

### 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/document/product/386/6725)。|
| message | String | 错误信息描述，与接口相关。|
| codeDesc | String | 返回码信息描述。|


## 错误码

| 错误代码 | 英文提示 | 错误描述 |
|------|------|------|
| 9003 | InvalidParameter | 参数错误 |
| 9006 | InternalError.CCDBAbnormal | CCDB 服务异常 |
| 11041 | InvalidParameter.CCDBLBNotExist | CCDB中不存在该负载均衡记录信息 |
| 12003 | IncorrectStatus.LBWrongStatus | 该负载均衡状态不正确,无法执行当前操作 |
| -21001 | InvalidStatus.LBInvalidStatus | 当前负载均衡状态不允许此操作 |
| 11060 | InternalError.TGWAbnormal | TGW 服务异常 |


## 实际案例
 
### 输入

```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=UnbindBmL7LocationVmIp
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=24763
	&Timestamp=1507714922
	&Region=bj
	&loadBalancerId=lb-abcdefgh
	&listenerId=lbl-abcdefgh
	&domainId=dm-abcdefgh
	&locationId=loc-abcdefgh
	&vmList.0.port=1234
	&vmList.0.vmIp=1.1.1.1
	&Signature=AySJsE6Zq3knXwPSzxlYUl%2FrM90%3D
```

### 输出

```
{
 "code": 0,
 "message": "",
 "codeDesc": "Success"
}

```
