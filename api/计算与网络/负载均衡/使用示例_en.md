In order to help you get started with Cloud Load Balancer APIs quickly, we provide an example on how to use the APIs. Before using the APIs, please deploy TCP service on two CVMs, and listen for port 80. The service will return a string that says "hello world". By creating a cloud load balancer instance, you can access the service on CVM through the VIP of cloud load balancer.
## 1. Purchase Cloud Load Balancer Instance of Public Network Type (with Daily Rate)
Before using Cloud Load Balancer, we need to purchase a cloud load balancer instance of public network type (with daily rate). For more information on how to purchase a cloud load balancer instance, please refer to [Purchase Cloud Load Balancer Instance](/doc/api/244/1254).

Here we create a cloud load balance instance of public network type (with daily rate). The Action field of its common request parameters is CreateLoadBalancer. The request parameters of this API are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerType | Type of cloud load balancer instance | 2; since the service is accessed via public network, we create a Cloud Load Balancer instance of public network type (with daily rate).   |
| loadBalancerName | Name of cloud load balancer instance | The name can be defined by users. In this example, we name it "test".  |


By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://lb.api.qcloud.com/v2/index.php?Action=CreateLoadBalancer
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerType=2
&loadBalancerName=test
```
The returned result of the above request is as follows:

```
{
    "code" : 0,
    "message" : "",
    "unLoadBalancerIds":[
        "lb-abcdefgh"
    ],
    "dealIds":[
        121
    ]
}
```
lb-abcdefgh is the unique ID of the cloud load balancer instance you just purchased. Use API [Query the List of cloud load balancer Instances](/doc/api/244/1261) to query whether the cloud load balancer instance has been successfully created. If so, then go to Step 2.

## 2. Create Cloud Load Balancer Listener
With unique ID of cloud load balancer instance, we can create cloud load balancer listener. For more information on how to create cloud load balancer listener, please refer to [Create Cloud Load Balancer Listener](/doc/api/244/1255).

In this example, the request parameters of the API used to create cloud load balancer listener are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerId | Unique ID of cloud load balancer instance | You can use the unique ID of the cloud load balancer instance you just created, i.e. lb-abcdefgh |
| listeners.1.loadBalancerPort | Listening port of cloud load balancer listener | 80 |
| listeners.1.instancePort | Listening port on backend CVM of cloud load balancer listener | 80 |
| listeners.1.protocol | The protocol listened for by cloud load balancer listener. 1:HTTP, 2:TCP, 3:UDP, 4:HTTPS | In this example, select 2 to listen for TCP protocol |
| listeners.1.healthSwitch | Whether to enable the health check by cloud load balancer listener. 1: Enable; 0: Disable. Default is "Enable" | In this example, select 1 to enable health check |
| listeners.1.listenerName | Name of cloud load balancer listener. This field is optional. If left blank, it will be filled with default value | In this example, the value is listenerTest |


By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://lb.api.qcloud.com/v2/index.php?Action=CreateLoadBalancerListeners
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerId=lb-abcdefgh
&listeners.1.loadBalancerPort=80
&listeners.1.instancePort=80
&listeners.1.protocol=2
&listeners.1.healthSwitch=1
&listeners.1.listenerName=listenerTest

```
The returned result of the above request is as follows:
```
{
  "code" : 0,
  "message" : "",
  "requestId" : 123
}
```
You can use asynchronous API [Query Status of Cloud Load Balance Task](/doc/api/244/4007) to query whether the task with requestId has been executed successfully.

## 3. Bind Backend CVM to Cloud Load Balancer instance
You need to bind CVM to cloud load balancer instance after creating the listener. For more information on how to bind backend CVM to cloud load balancer instance, please refer to [Bind Backend CVM to Cloud Load Balancer Instance](/doc/api/244/1265).

Here we bind two CVMs to the cloud load balancer instance created above. The unique IDs of these two CVMs are ins-5678test and ins-1234test respectively. The Action field of common request parameters is RegisterInstancesWithLoadBalancer. The request parameters of this API are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerId | Unique ID of cloud load balance instance | You can use the unique ID of the cloud load balancer instance you just created, i.e. lb-abcdefgh |
| backends.1.instanceId | Unique ID of the CVM bound to the cloud load balancer instance | In this example, it's the first CVM's unique ID, i.e. ins-5678test |
| backends.1.weight | Weight of the CVM bound to the cloud load balancer instance | In this example, use default value 10 |
| backends.2.instanceId | Unique ID of the CVM bound to the cloud load balancer instance | In this example, it's the second CVM's unique ID, i.e. ins-1234test |
| backends.2.weight | Weight of the CVM bound to the cloud load balancer instance | In this example, use default value 10 |


By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://lb.api.qcloud.com/v2/index.php?Action=CreateLoadBalancerListeners
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerId=lb-abcdefgh
&backends.1.instanceId=ins-5678test
&backends.1.weight=10
&backends.2.instanceId=ins-1234test
&backends.2.weight=10
```
The returned result of the above request is as follows:
```
{
  "code" : 0,
  "message" : "",
  "requestId" : 1234
}
```
You can use asynchronous API [Query Status of Cloud Load Balance Task](/doc/api/244/4007) to query whether the task with requestId has been executed successfully.

## 4. Query and Use Cloud Load Balancer Instance
At last, you need to query the VIP or domain of the cloud load balancer instance. For the API used to query the list of cloud load balancer instances, please refer to API [Query the List of Cloud Load Balancer Instances](/doc/api/244/1261).

The Action field of common request parameters is DescribeLoadBalancers. The request parameters of this API are shown in the following table:

| Parameter Name | Description | Value |
|---------|---------|---------|
| loadBalancerIds.1 | Unique ID of cloud load balancer instance | In this example, use the unique ID of cloud load balancer instance you just created, i.e. lb-abcdefgh |

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://lb.api.qcloud.com/v2/index.php?Action=DescribeLoadBalancers
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&loadBalancerIds.1=lb-abcdefgh
```

Output
```
{
  "code" : 0,
  "message" : "",
  "totalCount" : 1,
  "loadBalancerSet":[
 	{
            "loadBalancerId": "qlb5feb7941833ca285c65ff7528393173e",
            "unLoadBalancerId": "lb-abcdefgh",
            "loadBalancerName": "test",
            "loadBalancerType": 2,
            "domain": "20de02-0.gz.1251000011.clb.myqcloud.com",
            "loadBalancerVips": [
                "203.195.128.180"
            ],
            "status": 1,
            "createTime": "2016-09-01 16:08:24",
            "statusTime": "2016-09-02 16:04:59",
            "sessionExpire": 0,
            "vpcId": 0,
            "subnetId": 0,
            "projectId": 0,
            "openBgp": false
        }
   ]
}
```

Based on the query results, you can use the cloud load balancer instance's VIP (203.195.128.180) or domain (20de02-0.gz.1251000011.clb.myqcloud.com) to forward the request to the backend CVMs bound to the instance according to the rule of cloud load balancer listener to achieve the Cloud Load Balance service.
