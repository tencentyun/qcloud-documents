## 1. API Description
 
This API (AssociateVip) is used to bind a pre-assigned private VIP to the specified CVM, so as to enable master and backup switchover.

<font style="color:red">The feature of this API can be implemented by using ENIs. It's recommended NOT to use this API.</font>

You can use a new API to establish a master/slave cluster in VPC using keepalived. For more information, see [here](https://cloud.tencent.com/document/product/215/5850).


Domain for API request: <font style="color:red">vpc.api.qcloud.com</font>


1) You need to contact Tencent Cloud customer service to apply for the VIP.
2) The CVM must be in the VPC.


## 2. Input Parameters
 The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, see <a href="/doc/api/372/4153" title="Common request parameters">Common Request Parameters</a>. The Action field for this API is AssociateVip.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | The Virtual Private Cloud ID assigned by the system. Both the vpcId before upgrading and the upgraded unVpcId are supported. For example: vpc-2ari9m7h.  |
| vipId | Yes | Int | VIP ID, for example: 12. You need to contact the online customer service to apply for a VIP ID |
| lanIp | Yes | String | CVM private IP, for example: 10.0.0.1. To query the CVM IP, please see <a href="https://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="Query Instance List">Query Instance List</a> |
 

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please see [ Common Error Codes](https://intl.cloud.tencent.com/document/product/215/4781) on the Error Code page. |
| message | String | Module error message description depending on API. |

## 4. Error Codes
 The following error code list only provides the error codes for this API. For common error codes, please see <a href="https://cloud.tencent.com/doc/api/245/4924" title="VPC Error Codes">VPC Error Codes</a>.

| Error Code | Description |
|---------|---------|
| InvalidVipId.NotFound | The vipId does not exist. Currently, VIP needs to be assigned manually. If you forgot your vipId or this is your first time binding, please contact the customer service to retrieve your vipID or apply for a vipID.  |
| InvalidLanIp.NotFound | The CVM does not exist. Please check the information you entered.To query the CVMs under the VPC, please see <a href="https://cloud.tencent.com/doc/api/229/831" title="Query CVM Instance List">Query CVM Instance List</a>.  |
| InvalidVpc.NotFound | The VPC does not exist. Please check the information you entered.|

## 5. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=AssociateVip
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
  &vpcId=vpc-2ari9m7h
	&vipId=1
	&lanIp=10.0.0.2
</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```


