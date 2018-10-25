## Description
This API (CreateBmLoadBalancer) is used to create BM load balancer instances. To use BM load balance service, you must create one or more BM load balancer instances. When the API is successfully called, the unique ID of the BM load balancer instance is returned. You can purchase two types of BM load balancer instances: public network-based and private network-based. Public network-based load balancer has a BGP VIP which is used to quickly access the CPM bound to the load balancer. Private network-based load balancer has a Tencent Cloud internal VIP which is used to quickly access the CPM bound to the load balancer, but cannot be accessed via Internet.

Domain for API request: bmlb.api.qcloud.com

## Request
### Request Example
```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=CreateBmLoadBalancer
	&<Common request parameters>
	&unVpcId=<ID of the VPC to which the load balancer instance belongs.>
	&loadBalancerType=<Load balancer type>
	&goodsNum=<Number of load balancer instances>
	&payMode=<Billing Method>
```

### Request Parameter
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see [Common Request Parameters](https://cloud.tencent.com/document/product/386/6718) page. The Action field for this API is CreateBmLoadBalancer.

| Parameter | Required | Type | Description |
| ---------------- | ---- | ------------- | ---------------------------------------- |
| unVpcId | Yes | String | ID of the VPC to which the BM load balancer instance belongs. |
| unSubnetId | No | String | When you purchase a private network-based cloud load balancer instance within the VPC, you need to specify the subnet ID. The VIP of the private network-based cloud load balancer instance is generated from this subnet. This field can be left empty in other cases. |
| projectId | No | Int | Project ID of the cloud load balancer. If it is left empty, the instance belongs to the default project. |
| loadBalancerType | Ye | String | Type of load balancer. Value can be open or internal. "open" represents public network (with daily rate), and "internal" represents private network. |
| goodsNum | No | Int | Number of BM load balancer instances to be purchased. Default is 1, and maximum is 20. |
| payMode | No | String | Billing method of BM load balancer. Value can be flow (Bill-by-traffic) or bandwidth (Bill-by-bandwidth). Default is flow. |
| tgwSetType | No | String | TGW cluster type of load balancer. Value can be tunnel or fullnat. "tunnel" represents tunnel cluster and "fullnat" represents FULLNAT cluster. Default is fullnat. Select tunnel if you want to acquire Client IP. |
| exclusive | No | int | The exclusive category of load balancer. 0: Non-exclusive; 1: Layer-4 exclusive; 2: Layer-7 exclusive; 3: Layer-4 and layer-7 exclusive; 4: Shared disaster recovery. |
| specifiedVips | No | Array(String) | The specified vip. If it is specified, the number must be consistent with goodsNum. Otherwise, a random vip is assigned by the backend. |

## Response

### Response Example
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerIds": <List of load balancer instance IDs>
}
```

## Response Parameters


| Parameter | Type | Description |
| --------------- | ------ | ---------------------------------------- |
| code | Int | Error code. 0: Successful; other values: Failed. For more information, please see [Error Codes](/document/product/386/6725). |
| message | String | Module error message description depending on API. |
| loadBalancerIds | Array | ID of the created BM load balancer instance. |

## Error Codes

| Error Code | Error Message | Error Description |
| ----- | -------------------------------------- | -------------------- |
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |
| 12010 | InvalidResource.LBNumberOverOrderLimit | The number of load balancer instances to be purchased in this order has exceeded the limit |
| 12011 | InvalidResource.LBNumberOverTotalLimit | The number of purchased load balancer instances has exceeded the limit |
| 20002 | InvalidParameter.VpcIdSubnetIdNotExist | The VPC and subnet information does not exist for this account in this region |

## Practical Case
### Input
```
GET https://bmlb.api.qcloud.com/v2/index.php?Action=CreateBmLoadBalancer
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=61431
	&Timestamp=1507728683
	&Region=bj
	&unVpcId=vpc-xxxx
	&loadBalancerType=open
	&goodsNum=2
	&payMode=flow
	&specifiedVips.0=10.1.143.210
	&specifiedVips.1=10.1.143.211
	&Signature=umZFAAWKzjXEQp4ySgrWAoWOHKI%3D
```


### Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerIds": [
        "lb-abcdefgh",
        "lb-abcdefge"
    ]
}
```
