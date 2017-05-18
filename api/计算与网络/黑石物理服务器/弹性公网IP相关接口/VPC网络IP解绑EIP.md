## 1. 接口描述
该接口用于绑定黑石弹性公网IP到黑石私有网络的IP（非黑石物理机IP）。解绑后EIP仍然会收取闲置费，请及时[释放清理](/document/product/386/6676)。
 
域名: <font style="color:red">eip.api.qcloud.com</font>
接口名: EipBmUnBindVpcIp

 

## 2. 输入参数
|参数名称|必选|类型|描述|
|-------|----|---|----|----|
| eipId | 是 | String | EIP实例ID |
| vpcId | 是 | Int | IP所属的VPC的ID|
| vpcIp | 是 | String | VPC内IP，可通过[申请内网IP接口](/document/product/386/7337)获得|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/doc/api/456/6725)。 |
| message |   String | 错误信息 |
| data |   Array | 返回异步任务信息，具体结构描述如下 |

Data结构

|参数名称|类型|描述|
|---|---|---|
| data.requestId | Int | 绑定黑石物理机异步任务ID，可以通过[查询EIP任务状态](/document/product/386/6670)查询任务状态|

## 4. 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|9032|InternalCgwErr|内部接口错误|
|30009|EipNotExist|操作的EIP记录不存在|
|30010|EipStateCannotOp|EIP当前状态不允许解绑|
|-50000|VpcIdInvalid|VpcId参数不正确|
|-49999|VpcIpBinded|操作的VpcIp已经绑定EIP|
|-49998|VpcIpNotExist|操作的VpcIp不存在|
|-49997|VpcIpInvalid|操作的VpcIp属于物理机IP|
|-49996|VpcIpSubnetInvalid|操作的VpcIp的子网信息异常|
|-49995|TunnelEipNotSuport|隧道模式的EIP暂不支持绑定VpcIP|
|-49994|VpcIpNotApplyed|操作的VpcIp未申请|

## 5. 示例
 
输入
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
  &Action=bmUnBindRs
  &vpcIp=10.10.x.x&eipId=eip-vvvvvvv&vpcId=1000

</pre>

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "requestId": 100000
    }
}

```

