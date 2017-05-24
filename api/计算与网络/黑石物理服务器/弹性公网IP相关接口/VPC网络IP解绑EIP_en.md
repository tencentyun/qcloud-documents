## 1. API Description
This API (bmUnBindVpcIp) is used to unbind BM EIP from BM VPC IP (other than CPM IP). After the EIP is unbound, inactivity fee will still be charged for it, so please [release and clean up](/document/product/386/6676) it in a timely manner .
 
Domain: eip.api.qcloud.com

 

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|-------|----|---|----|----|
| eipId | Yes | String | EIP instance ID |
| vpcId | Yes | Int | ID of the VPC to which the IP belongs |
| vpcIp | Yes | String | Private IP of VPC, which can be obtained using API [Apply for Private IP](/document/product/386/7337) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded, other values: Failed. For more information, please see [Error Codes](/doc/api/456/6725).  |
| message | String | Error message |
| data | Array | Return asynchronous task information. For more information on its composition, please see below |

Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---|---|---|
| data.requestId | Int | ID of asynchronous task for binding to CPM. The task status can be queried via API [Query EIP Task Status](/document/product/386/6670) |

## 4. Error Codes
| Error Code | Error Message | Error Description |
|---|---|---|
| 9003 | ParamInvalid | Incorrect request parameter |
| 9006 | InternalErr | An error occurred with internal data operation |
| 9032 | InternalCgwErr | Internal API error |
| 30009 | EipNotExist | The EIP does not exist |
| 30010 | EipStateCannotOp | The EIP is not allowed to be unbound under current status |
| -50000 | VpcIdInvalid | Incorrect VpcId parameter |
| -49999 | VpcIpBinded | The VpcIp has been bound to EIP |
| -49998 | VpcIpNotExist | The VpcIp does not exist |
| -49997 | VpcIpInvalid | The VpcIp is a CPM IP |
| -49996 | VpcIpSubnetInvalid | The subnet information of the VpcIp is invalid |
| -49995 | TunnelEipNotSuport | EIP in a tunnel mode does not support binding to VpcIP currently |
| -49994 | VpcIpNotApplyed | The VpcIp has not been applied for yet |

## 5. Example
 
Input
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
  &Action=bmUnBindRs
  &vpcIp=10.10.x.x&eipId=eip-vvvvvvv&vpcId=1000

</pre>

Output
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


