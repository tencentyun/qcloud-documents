## 1. API Description
Domain name: vpc.api.qcloud.com
API name: DescribeDirectConnectGatewayNatRule

This API is used to query the network address translation rule for Direct Connect gateway.

## 2. Input Parameters
| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | String | Virtual private cloud ID, which can be vpcId or unVpcId. unVpcId is recommended. Can be queried via the API <a href="http://www.qcloud.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%E5%88%97%E8%A1%A8" title="DescribeVpcEx">DescribeVpcEx</a> |
| directConnectGatewayId | Yes | String | Direct Connect gateway ID |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Succeeded; other values: Failed |
| message | String | Error message |
| data | Array | Network address translation rules, which are divided into local IP translation, peered IP translation, local source address translation, and local destination port translation |

Data structure

| Parameter Name | Type | Description |
|---------|---------|---------|
| data.localIPTranslation | Array | Local IP translation: the original IP within the VPC is mapped to a new IP, which is used to communicate with the Direct Connect peer. | 
| data.peerIPTranslation | Array | Peered IP translation: the original IP of the Direct Connect peer is mapped to a new IP, which is used to communicate with the connected VPC. | 
| data.localSourceIPPortTranslation | Array | Local source IP port translation: the source IP port within the VPC is mapped to specified IP pool, a random port of random IP is used to access the Direct Connect peer actively. Response packets are not affected. | 
| data.localDestinationIPPortTranslation | Array | Local destination IP port translation: the Direct Connect peer accesses the VPC actively and needs to access the mapped IP port in order to communicate with the original IP within the VPC. Response packets are not affected. | 


## 4. Example
Input
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=DescribeDirectConnectGatewayNatRule
&vpcId=vpc-1y7wcr29
&directConnectGatewayId=dcg-beyteaqt
&<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "localIPTranslation":[
            {
                "originalIP":"10.100.89.9",
                "translationIP":"172.16.3.2"
            }
        ],
        "peerIPTranslation":[
            {
                "originalIP":"10.100.89.20",
                "translationIP":"192.167.0.2"
            }
        ],
        "localSourceIPPortTranslation":[
            
        ],
        "localDestinationIPPortTranslation":[
            
        ]
    }
}
```


