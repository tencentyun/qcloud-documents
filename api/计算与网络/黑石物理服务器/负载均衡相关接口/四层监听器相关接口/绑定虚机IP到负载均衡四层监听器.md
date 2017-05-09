## 1. 接口描述
 
本接口 (BindBmL4ListenerVmIp) 提供了绑定虚机IP到黑石负载均衡四层监听器功能。

接口请求域名：<font style="color:red">bmlb.api.qcloud.com</font>


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/product/386/6718)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| loadBalancerId | 是 | String |   负载均衡实例ID，可通过接口[DescribeBmLoadBalancers](/document/product/456/9306)查询。|
| listenerId | 是 | String | 负载均衡四层监听器ID，可通过接口[DescribeBmListeners](/document/product/456/9296)查询。|
| vmList | 是 | Array |   待绑定的虚机信息。可以绑定多个主机端口。目前一个四层监听器下面最多允许绑定255个主机端口。|

vmList描述待绑定的虚机信息，n为下标，vmList包含字段如下

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|vmList.n.port|是|Int|待绑定的虚机端口，可选值1~65535。|
|vmList.n.vmIp|是|String|待绑定的虚机IP。|
|vmList.n.weight|是|Int|权重信息，可选值0~100。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](/document/product/386/6725)。|
| message | String | 模块错误信息描述，与接口相关。|
| codeDesc | String | 返回码信息描述。|


模块错误码

| 错误代码 | 英文提示 | 错误描述 |
|------|------|------|
| 9003 | InvalidParameter | 参数错误 |
| 9006 | InternalError.CCDBAbnormal | CCDB 服务异常 |
| 11041 | InvalidParameter.CCDBLBNotExist | CCDB中不存在该负载均衡记录信息 |
| 12003 | IncorrectStatus.LBWrongStatus | 该负载均衡状态不正确,无法执行当前操作 |
| -21001 | InvalidStatus.LBInvalidStatus | 当前负载均衡状态不允许此操作 |
| -12023 | InvalidL4Listener.NotExist | CCDB中不存在该四层监听器 |
| -12021 | IncorrectStatus.L4ListenerWrongStatus | 该负载均衡四层监听器状态不正确,无法执行当前操作 |
| 12013 | InvalidResource.BindCPMNumberOverLimit | 该负载均衡绑定的主机端口数量超过上限 |
| 11060 | InternalError.TGWAbnormal | TGW 服务异常 |
| 28000 | InternalError.VPCAbnormal | VPC 服务异常 |
| 14100 | InternalError.BmApiAbnormal | bmApi服务异常 |
| -12022 | InvalidParameter.InvalidMultiL4VportToRsport | 此主机端口已经绑定四层监听器 |
| -12024 | InvalidVmIp.NotExist | 不存在该虚拟IP |


## 4. 示例
 
输入

<pre>
https://domain/v2/index.php?Action=BindBmL4ListenerVmIp
&<<a href="https://www.qcloud.com/document/product/386/6718">公共请求参数</a>>
&loadBalancerId=lb-abcdefgh
&listenerId=lbl-abcdefgh
&vmList.1.port=1234
&vmList.1.vmIp=1.1.1.1
&vmList.1.weight=10
</pre>

输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
}

```