## 1. API Description
 
This API (DescribeBmBindInfo) is used to acquire the details of BM load balancers bound to CPM IDs and VM IPs.

Domain for API request:<font style="color:red">bmlb.api.qcloud.com</font>


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/product/386/6718).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| vpcId | Yes | Int | VPC ID. |
| instanceIds.n | Yes | Array | List of CPM IDs or VM IPs, used to acquire the list of load balancers bound to the CPMs. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. 0: Successful. Other values: Failed For more information, please see [Common Error Codes](/document/product/386/6725) in the Error Codes page. |
| message | String | Module error message description depending on API. |
| codeDesc | String | Error code message description. |
| loadBalancerSet | Array | List of returned load balancers | |

Each sub-item of "loadBalancerSet" is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| loadBalancerId | String | ID of  load balancer instance. |
| appId | Int | AppId of developer. |
| projectId | Int | Project ID of the load balancer  |
| vpcId | Int | VPC ID. |
| vip | String | IP of load balancer. |
| tgwSetType | String | TGW cluster type of load balancer. Value can be tunnel or fullnat. "tunnel" represents tunnel cluster and "fullnat" represents FULLNAT cluster. |
| exclusive | Int | Whether the TGW cluster is exclusive. |
| L4ListenerSet | Array | List of layer-4 listeners with the binding. |
| L7ListenerSet | Array | List of layer-7 listeners with the binding. |

Each sub-item of L4ListenerSet is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| listenerId | String | ID of the load balancer layer-7 listener. |
| listenerName | String | Name of the load balancer layer-7 listener. |
| protocol | String | Protocol type of load balancer layer-7 listener (HTTP, HTTPS). |
| loadBalancerPort | Int | Listening port of the load balancer layer-7 listener. |
| rsList | Array | List of CPMs bound to the forwarding path. |

Each sub-item of rsList is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | CPM ID or VM IP. |
| rsPort | Int | CPM port. |


Each sub-item of L7ListenerSet is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| listenerId | String | ID of the load balancer layer-7 listener. |
| listenerName | String | Name of the load balancer layer-7 listener. |
| protocol | String | Protocol type of load balancer layer-7 listener (HTTP, HTTPS). |
| loadBalancerPort | Int | Listening port of the load balancer layer-7 listener. |
| ruleSet | Array | List of returned forwarding rules. |

Each sub-item of ruleSet contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| domain | String | Layer-7 forwarding domain name of load balancer. |
| domainId | String | ID of layer-7 forwarding domain of load balancer. |
| locations | Array | List of forwarding paths under the forwarding domain. |

Each sub-item of locations contains the following fields

| Parameter Name | Type | Description |
|---------|---------|---------|
| url | String | Forwarding path of the layer-7 forwarding rules for the load balancer. |
| locationId | String | ID of layer-7 forwarding path of the load balancer. |
| rsList | Array | List of CPMs bound to the forwarding path. |

Each sub-item of rsList is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceId | String | CPM ID or VM IP. |
| rsPort | Int | CPM port. |


Module Error Codes

| Error Code | Error Message | Error Description |
|------|------|------|
| 9003 | InvalidParameter | Invalid parameter |
| 9006 | InternalError.CCDBAbnormal | CCDB service error |


## 4. Example
 
Input

<pre>
https://domain/v2/index.php?Action=DescribeBmBindInfo
&<<a href="https://www.qcloud.com/document/product/386/6718">Common request parameters</a>>
&vpcId=XXX
&instanceIds.1=1.1.1.1
&instanceIds.2=cpm-abcdefgh
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
        {
            "loadBalancerId": "lb-abcdefgh",
            "appId": XXX,
            "projectId": 0,
            "vpcId": XXX,
            "vip": "100.100.100.100",
            "tgwSetType": "fullnat",
            "exclusive": 0,
            "L4ListenerSet": [
                {
                    "listenerId": "lbl-abcdefgh",
                    "protocol": "tcp",
                    "loadBalancerPort": 1234,
                    "rsList": [
                        {
                            "instanceId": "1.1.1.1",
                            "rsPort": 1234
                        }
                    ]
                }
            ],
            "L7ListenerSet": [
                {
                    "listenerId": "lbl-abcdefge",
                    "protocol": "http",
                    "loadBalancerPort": 80,
                    "ruleSet": [
                        {
                            "domain": "a.com",
                            "domainId": "dm-abcdefgh",
                            "locations": [
                                {
                                    "url": "/",
                                    "locationId": "loc-abcdefgh",
                                    "rsList": [
                                        {
                                            "instanceId": "1.1.1.1",
                                            "rsPort": 80
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "loadBalancerId": "lb-abcdefge",
            "appId": XXX,
            "projectId": 0,
            "vpcId": XXX,
            "vip": "115.115.115.115",
            "tgwSetType": "fullnat",
            "exclusive": 0,
            "L4ListenerSet": [],
            "L7ListenerSet": [
                {
                    "listenerId": "lbl-abcdefgi",
                    "protocol": "http",
                    "loadBalancerPort": 80,
                    "ruleSet": [
                        {
                            "domain": "a.com",
                            "domainId": "dm-abcdefge",
                            "locations": [
                                {
                                    "url": "/",
                                    "locationId": "loc-abcdefgi",
                                    "rsList": [
                                        {
                                            "instanceId": "cpm-abcdefgh",
                                            "rsPort": 80
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "loadBalancerId": "lb-abcdefgi",
            "appId": XXX,
            "projectId": 0,
            "vpcId": XXX,
            "vip": "115.115.115.116",
            "tgwSetType": "tunnel",
            "exclusive": 0,
            "L4ListenerSet": [
                {
                    "listenerId": "lbl-abcdefgg",
                    "protocol": "tcp",
                    "loadBalancerPort": 1234,
                    "rsList": [
                        {
                            "instanceId": "cpm-abcdefgh",
                            "rsPort": 1234
                        }
                    ]
                }
            ],
            "L7ListenerSet": []
        }
    ],
    "totalCount": 3
}

```
