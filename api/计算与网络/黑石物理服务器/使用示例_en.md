In order to help you get started with Cloud Physical Machine (CPM) API, we provide an example on how to use it. This article provides the guide on how to use the API to create a CPM.

##Purchasing a CPM

Before purchasing a CPM, we need to know which models configured for the CPM are available, because they determine the performance and corresponding price of the CPM. For more information, please see [Query Device Class](/document/product/386/6636). After selecting a model, we need to select the corresponding [RAID Type](/document/product/386/7370) and an [Operating System](/document/product/386/6727) supported for BM.

For example, to create a CPM (monthly plan) with a model of PS100 in Beijing Zone 1, and select Centos 7.2 operating system and the array of RAID 1+0, the request parameters should be:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| zoneId | Yes | Int | Availability zone ID. You can use [(DescribeRegions)](/doc/api/456/6634) API to acquire CPM availability zone information. |
| vpcId | Yes | Int | VPC ID. You can use API [DescribeBmVpcEx](/doc/api/456/6646) to acquire VPC information. |
| subnetId | Yes | Int | Subnet ID. You can use API [DescribeBmSubnetEx](/doc/api/456/6648) to acquire VPC information. |
| deviceClassCode | Yes | String | Device class code (the "code" displayed in the purchase page). You can use API [DescribeDeviceClass](/doc/api/456/6636) to acquire device class information, where the "deviceClassDisplay" field is the value required by deviceClassCode |
| osTypeId | Yes | Int | Operating system type ID. You can use API [DescribeOs](/doc/api/456/6727) to acquire operating system information. |
| raidId | Yes | Int | RAID type ID. You can use API [DescribeDeviceClassRaid](/doc/api/456/6640) to acquire RAID information. |
| timeUnit | Yes | String | Measurement unit for purchased usage period. Value: m: purchase by month.  |
| timeSpan | Yes | Int | Purchased usage period.  |
| goodsNum | Yes | Int | Number of CPMs to purchase.  |
| hasWanIp | No | Int | Whether to assign public IP. 0: Do not assign; 1: Assign. Default is 0. |
| needSecurityAgent | No | Int | Whether to install security Agent. 0: Do not install; 1: Install. Default is 0.  |
| needMonitorAgent | No | Int | Whether to install monitor Agent. 0: Do not install; 1: Install. Default is 0.  |
| alias | No | String | Device alias. The aliases will be automatically numbered if you purchase multiple machines.  |
| sysRootSpace | No | Int | System disk root partition size. Default is 10 G. For the size of system disk, Please see API [DescribeDeviceClassPartition](/document/product/386/7370) |
| sysSwaporuefiSpace | No | Int | The size of swap partition or /boot/efi partition of system disk. When the machine boots in UEFI mode, the partition is /boot/efi with a default size of 2 G. The partition is swap for normal machines, in which case you don't need to specify this partition. To determine whether the machine boots in UEFI mode, please see API [DescribeDeviceClass](/doc/api/456/6636) |
| sysUsrlocalSpace | No | Int | Size of /usr/local partition. This partition does not exist by default.  |
| sysDataSpace | No | Int | Size of /data partition. Any remaining space of the system disk will be allocated to the /data partition.  |


By combining common request parameters and API request parameters, you can get the final request as follows:

```
https://bm.api.qcloud.com/v2/index.php?
Action=RunInstancesHour
&Region=bj
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&zoneId=1000800001
&vpcId=1042
&subnetId=110
&deviceClassCode=PS100
&osTypeId=2
&raidId=3
&timeUnit=m
&timeSpan=1
&goodsNum=1
&hasWanIp=0
&needSecurityAgent=1
&needMonitorAgent=1
&alias=test
&sysRootSpace=50
&sysSwaporuefiSpace=2
&sysUsrlocalSpace=100
&sysDataSpace=300
```

The returned result for the request above is shown below. According to the result, the ID of the newly created CPM is dcpm-ntlsj9gh. The ID is the unique identifier of this instance. It is used to specify objects for the following operations on CPM.

```
{
  "code": 0,
  "message": "OK",
  "data": {
    "dealNames": [
      "20160721110015"
    ],
    "resourceIds": {
      "20160721110015": [
        "dcpm-ntlsj9gh"
      ]
    },
    "dealIds": [
      "454013"
    ]
  }
}
```

So now, we have purchased a CPM. Next, the CPM will be automatically deployed, and the billing process will be started after it has been delivered to the customer.






