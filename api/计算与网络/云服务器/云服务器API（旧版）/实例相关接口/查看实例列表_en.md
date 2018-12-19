## 1. API Description

This API (DescribeInstances) is used to get the details of one or more instances.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* You can query instance list based on instance ID, instance name or instance status.
* If the parameter is empty, returns certain number (specified by limit, the default is 20) of instances under the current user account.
* The `status` field indicates the status of the instance, including the following status:

| Status ID | Status Name |
|---------|---------|
| 1 | Failure |
| 2 | Running 
| 3 | Creating 
| 4 | Shutdown completed 
| 5 | Returned
| 6 | Returning  
| 7 | Rebooting 
| 8 | Starting up
| 9 | Shutting-down
| 10 | Password resetting
| 11 | Formatting
| 12 | Image producing
| 13 | Bandwidth setting
| 14 | System reinstalling
| 15 | Domain name binding
| 16 | Domain name unbinding
| 17 | Cloud Load Balance binding
| 18 | Cloud Load Balance unbinding
| 19 | Upgrading
| 20 | Key issuing
| Others | In maintenance (The instance is running normally. But you cannot operate on this instance.)

## 2. Input Parameters

The following list only provides API request parameters. For common parameters, please see [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceIds.n | No | String | IDs of instances you want to query. It can be obtained from the unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API. (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)).
| lanIps.n | No | String | (Filter condition) Filter by the Private IP or Public IP (including IP and Elastic IP automatically assigned when the instance is created) of one or more instance(s)(This API allows passing multiple IPs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)).
| searchWord | No | String | (Filter condition) Filter by instance name, support fuzzy query. |
| status | No | Int | (Filter condition) The status of the instances, which are listed above.
| projectId | No | Int | (Filter condition) [Project ID](/document/api/378/4398). |
| zoneId | No | Int | (Filter condition) [Availability Zone ID](/document/api/213/15707). |
| offset | No | Int | Offset; default value is 0. For more information about `offset`, please see [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).
| limit | No | Int | Number of returned results. The default value is 20, and the maximum is 100. For more information about `limit`, please see [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, please refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| totalCount | Int | Number of instances that meet the condition. |
| instanceSet | Array | Instance information list. |

instanceSet contains a lot of instance information, and the data structure for each instance information is as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| instanceName | String | Instance name.
| unInstanceId | String | Instance ID in the format "ins-xxxxxxxx".
| lanIp | String | Private IP of instance primary ENI.
| wanIpSet | Array | Public IP list (including IP and Elastic IP automatically assigned when the instance is created).
| cpu | Int | The number of CPU cores.
| mem | Int | Memory size (GB).
| bandwidth | Int | Bandwidth size (Mbps).
| unImgId | String | Image ID in the format "img-xxxxxxxx".
| status | Int | Current status. For specific meaning, see above.
| Region | String | The region. Specific meaning can be queried through the [DescribeProductRegionList](/document/api/213/2849) API.
| createTime | String | Time of creation.
| deadlineTime | String | Expiry time. For postpaid instances, it will be"0000-00-00 00:00".
| autoRenew | Int | Whether the instance is set to [Auto Renewal](https://cloud.tencent.com/doc/api/229/1746). <br>0: Do not auto renew; <br>1: Auto renew; <br>2: Do not renew.
| projectId | Int | [Project ID](https://cloud.tencent.com/doc/api/229/1335).
| os | String | Operating system name.
| cvmPayMode | Int | Billing mode. <br>0: Monthly postpaid; <br>1: Prepaid package; <br>2: Postpaid
| networkPayMode | Int | Network billing mode. <br> 0: Monthly postpaid; <br>1: Prepaid package; <br> 2: Bill by traffic; <br> 3: Bill by bandwidth. <br>The difference between the network billing modes can be found in [Purchase Network Bandwidth](https://cloud.tencent.com/doc/product/213/509). |
| zoneId | Int | [Availability Zone](/doc/product/213/6091) ID.
| zoneName | String | Availability zone name.
| vpcId | Int | [Virtual Private Cloud](/help/什么是私有网络) ID.
| subnetId | Int | Subnet ID.
| isVpcGateway | Int | Whether a VPC [gateway](https://cloud.tencent.com/doc/product/215/1682). <br>0: No; <br>1: Yes
| diskInfo | Array | The object that contains the hard disk information.

diskInfo contains a lot of hard disk information, and the data structure for each single hard disk information is as follows:

| Parameter name | Type | Description |
|---------|---------|---------|
| storageId | String | Data disk ID.
| storageType | Int | Data disk type. <br>1. Local disk <br>2. Cloud HDD storage <br>3. SSD local disk <br>4. SSD cloud storage <br>5. Premium cloud storage
| storageSize | Int | Data disk size (GB).
| rootId | String | System disk ID.
| rootSize | Int | System disk size (GB). |
| rootType | Int | System disk type. <br>1. Local disk <br>2. Cloud HDD storage <br>3. SSD local disk <br>4. SSD cloud storage


## 4. Example

Input:

<pre>
 https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstances
 &instanceIds.0=ins-r8hr2upy
 &instanceIds.1=ins-5d8a23rs
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common Request Parameters</a>>
</pre>

Output:

```
{
    "codeDesc": "Success",
    "totalCount": 14,
    "message": "",
    "code": 0,
    "instanceSet": [
        {
            "lanIp": "10.104.37.58",
            "instanceId": "qcvmfd57f3113bc6fd6f0c8ce381f5433539",
            "unImgId": "img-0vbqvzfn",
            "imageId": 6,
            "autoRenew": 0,
            "bandwidth": 1,
            "vpcId": 0,
            "deviceClass": "VSELF",
            "diskInfo": {
                "rootType": 2,
                "rootId": "disk-4rnslbwq",
                "rootSize": 50
            },
            "subnetId": 0,
            "isVpcGateway": 0,
            "uuid": "9bd7331d-fb7d-4013-bcb1-65a0d4b46873",
            "wanIpSet": [
                "123.207.32.83"
            ],
            "projectId": 0,
            "deadlineTime": "2017-01-02 00:22:48",
            "cvmPayMode": 1,
            "zoneId": 100002,
            "instanceName": "3-day test image",
            "imageType": "Public image",
            "status": 4,
            "mem": 1,
            "Region": "gz",
            "networkPayMode": 2,
            "unInstanceId": "ins-gsbuwc26",
            "createTime": "2016-12-02 00:22:40",
            "zoneName": "Guangzhou Zone 2",
            "statusTime": "2016-12-02 12:28:09",
            "os": "Xserver V8.1_64",
            "cpu": 1
        },
        {
            "lanIp": "10.104.249.153",
            "instanceId": "qcvm0c7dca6b0244fde9b36d7cbc986274a5",
            "unImgId": "img-31tjrtph",
            "imageId": 53,
            "autoRenew": 0,
            "bandwidth": 1,
            "vpcId": 0,
            "deviceClass": "VSELF_2",
            "diskInfo": {
                "rootId": "disk-hq2agvi8",
                "storageSize": 100,
                "rootType": 2,
                "storageType": 2,
                "storageId": "disk-fegdogdg",
                "rootSize": 50
            },
            "subnetId": 0,
            "isVpcGateway": 0,
            "uuid": "a952c786-a1ee-4d0a-8c45-2640ea70e704",
            "wanIpSet": [
                "123.207.115.47"
            ],
            "projectId": 0,
            "deadlineTime": "2017-01-24 09:22:25",
            "cvmPayMode": 1,
            "zoneId": 100003,
            "instanceName": "jupyter",
            "imageType": "Public image",
            "status": 2,
            "mem": 16,
            "Region": "gz",
            "networkPayMode": 1,
            "unInstanceId": "ins-r8hr2upy",
            "createTime": "2016-11-24 09:22:18",
            "zoneName": "Guangzhou Zone 3",
            "statusTime": "2016-11-30 10:48:24",
            "os": "centos7.2x86_64",
            "cpu": 8
        }
    ]
}
```






