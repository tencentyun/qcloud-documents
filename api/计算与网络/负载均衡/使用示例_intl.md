This example is provided to help you get started with load balancer APIs. Before using the APIs, deploy TCP service on two CVMs, and listen port 80. The service returns a string "hello world". By creating a load balancer instance, you can access the service on CVM through the load balancer VIP.
## Purchasing Public Network-based Load Balancer Instance
To use Load Balance service, you need to purchase a public network-based load balancer instance (with static IP). For more information on how to purchase a load balancer instance, please see [Purchase Load Balancer Instance](https://cloud.tencent.com/document/api/214/1254).

Here we create a public network-based load balancer instance (with static IP). The Action field of its common request parameters is CreateLoadBalancer. The request parameters of this API are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerType | Type of load balancer instance | **2**: Since the service is accessed via public network, we create a public network-based load balancer instance. |


By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://lb.api.qcloud.com/v2/index.php?Action=CreateLoadBalancer
&Region=ap-guangzhou
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerType=2
```
The returned results of the above request are as follows:

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "requestId": 3901941,
    "dealIds": [
        "3901941"
    ],
    "unLoadBalancerIds": {
        "3901941": [
            "lb-cjcymkw5",
        ]
    }
}
```
`lb-cjcymkw5` is the unique ID of the load balancer instance you just purchased. Query whether the load balancer instance has been successfully created via the API [Query the List of Load Balancer Instances](https://cloud.tencent.com/document/api/214/1261).

## Creating Load Balancer Listener
With the unique ID of load balancer instance, we can create a load balancer listener. For more information on how to create a load balancer listener, please see [Create Load Balancer Listener](https://cloud.tencent.com/document/api/214/1255).

In this example, the request parameters of the API used to create load balancer listeners are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerId | Unique ID of the load balancer instance | Use the unique ID of the load balancer instance you just created, i.e. `lb-cjcymkw5` |
| listeners.0.loadBalancerPort | Listening port of load balancer listener | 80 |
| listeners.0.instancePort | Listening port on backend CVM of load balancer listener | 80 |
| listeners.0.protocol | The protocol listened by load balancer listener. 1: HTTP, 2: TCP, 3: UDP, 4: HTTPS | In this example, select 2 to listen TCP protocol. |
| listeners.0.healthSwitch | Whether to enable the health check by load balancer listener. 1: Enable; 0: Disable. Default is "Enable". | In this example, select 1 to enable health check. |
| listeners.0.listenerName | Name of load balancer listener. This field is optional. Default value is used if you leave it empty. | In this example, the value is listenerTest |


By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://lb.api.qcloud.com/v2/index.php?Action=CreateLoadBalancerListeners
&Region=ap-guangzhou
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerId=lb-cjcymkw5
&listeners.0.loadBalancerPort=80
&listeners.0.instancePort=80
&listeners.0.protocol=2
&listeners.0.healthSwitch=1
&listeners.0.listenerName=listenerTest
  
```
The returned results of the above request are as follows:
```
{
  "code" : 0,
  "message" : "",
  "codeDesc": "Success",
  "requestId" : 12354
}
```
You can use the asynchronous API [Query Status of Load Balance Task](https://cloud.tencent.com/document/api/214/4007) to query whether the task with the request ID has been executed successfully.

## Binding Backend CVM to Load Balancer Instance
You need to bind CVM to load balancer instance after creating the listener. For more information on how to bind backend CVM to load balancer instance, please see [Bind backend CVM to Load Balancer Instance](https://cloud.tencent.com/document/api/214/1265).

Here we bind two CVMs to the load balancer instance created above. The unique IDs of these two CVMs are ins-5678test and ins-1234test. The Action field of common request parameters is RegisterInstancesWithLoadBalancer. The request parameters of this API are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerId | Unique ID of load balancer instance | Use the unique ID of the load balancer instance you just created, i.e. lb-abcdefgh |
| backends.0.instanceId | Unique ID of the CVM bound to the load balancer instance | In this example, it's the first CVM's unique ID, i.e. Ins-5678test |
| backends.0.weight | Weight of the CVM bound to the load balancer instance | In this example, use default value 10 |
| backends.1.instanceId | Unique ID of the CVM bound to the load balancer instance | In this example, it's the second CVM's unique ID, i.e. ins-1234test. |
| backends.1.weight | Weight of the CVM bound to the load balancer instance | In this example, use default value 10 |


By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://lb.api.qcloud.com/v2/index.php?Action=RegisterInstancesWithLoadBalancer
&Region=ap-guangzhou
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerId=lb-cjcymkw5
&backends.0.instanceId=ins-5678test
&backends.0.weight=10
&backends.0.instanceId=ins-1234test
&backends.0.weight=10
```
The returned results of the above request are as follows:
```
{
  "code" : 0,
  "message" : "",
  "codeDesc": "Success",
  "requestId" : 1234
}
```
You can use the asynchronous API [Query Status of Load Balance Task](https://cloud.tencent.com/document/api/214/4007) to query whether the task with the request ID has been executed successfully.

## Querying and Using Load Balancer Instance
Query the VIP or domain name of the load balancer instance. For more information on the API used to query the list of load balancer instances, please see the API [Query the List of Load Balancer Instances](https://cloud.tencent.com/document/api/214/1261).

The Action field of common request parameters is DescribeLoadBalancers. The request parameters of this API are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerIds.0 | Unique ID of load balancer instance | In this example, use the unique ID of the load balancer instance you just created, i.e. lb-cjcymkw5 |

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancers
&Region=ap-guangzhou
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerIds.0=lb-cjcymkw5

```

Response

```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "loadBalancerSet": [
        {
            "loadBalancerId": "lb-cjcymkw5",
            "unLoadBalancerId": "lb-cjcymkw5",
            "loadBalancerName": "59b25ffb-0",
            "loadBalancerType": 2,
            "domain": "20de02-0.gz.1251000011.clb.myqcloud.com",
            "loadBalancerVips": [
                "119.28.168.196"
            ],
            "status": 1,
            "createTime": "2017-09-08 17:16:42",
            "statusTime": "2017-09-20 13:37:55",
            "vpcId": 0,
            "uniqVpcId": "",
            "subnetId": 0,
            "projectId": 1005621,
            "forward": 0,
            "snat": false,
            "openBgp": 0,
            "isolation": 0,
            "log": ""
        },
    ],
    "totalCount": 1
}

```

Based on the query results, you can use the VIP `119.28.168.196` or domain name `20de02-0.gz.1251000011.clb.myqcloud.com` of the load balancer instance to forward the request to the backend CVMs bound to the instance according to the rule of load balancer listener to achieve the Load Balance service.

