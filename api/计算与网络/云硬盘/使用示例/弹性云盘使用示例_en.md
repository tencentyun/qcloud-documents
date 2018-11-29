In order to help you get started with elastic cloud storage quickly, we provide an example on how to use it.

In this example, we first query the price of the elastic cloud storage to be purchased, and create an elastic cloud storage using the same configuration next, and then mount it onto the specified CVM.

## 1. Query the Price of Elastic Cloud Storage

Before creating an elastic cloud storage, you can inquire about the price of the cloud storage to be purchased using API [InquiryStoragePrice](/doc/api/364/2522). Here we inquire about the price for creating an elastic cloud storage of 50G in Shanghai Zone 1. The relevant API request parameters are as follows:

| Parameter Name | Description | Value |
| --- | --- | --- |
| inquiryType | Inquiry type. It is always "create" when you create an elastic cloud storage | create |
| goodsNum | Number of elastic cloud storages to be created | 1 |
| storageType | The type of the elastic cloud storage to be created. You can create a HDD or a SSD cloud storage  | cloudBasic |
| period | Availability period of the elastic cloud storage to be created (in months) | 1 |
| payMode | Payment mode. Currently, only Prepaid is supported | prePay |
| storageSize | Size of the elastic cloud storage to be created (GB) | 50 |

 By combining common request parameters and API request parameters, you can get the final request as follows:
```txt
https://cbs.api.qcloud.com/v2/index.php?
Action=InquiryStoragePrice
&goodsNum=1
&inquiryType=create
&payMode=prePay
&period=1
&storageSize=50
&storageType=cloudBasic
&Region=sh
&Nonce=323726294
&SecretId=AKIDxxxxugEY
&Signature=BbxBeaS8GZWiBegYmReA9PjfRbU
&Timestamp=1466043404
```

The returned result of the above request is as follows. It shows that RMB 15 will be charged for creating an elastic cloud storage of 50GB with a duration of one month.
```json
{
	"code": 0,
	"message": "",
	"price": 1500
}
```


## 2. Create an Elastic Cloud Storage

You can use the API [CreateCbsStorages (Create elastic cloud storage)](/doc/api/364/2524) to create an elastic cloud storage with specified configuration. The relevant API request parameters are as follows:

| Parameter Name | Description | Value |
| --- | --- | --- |
| zoneId | The availability zone where the elastic cloud storage to be created resides in. This can be queried through API [DescribeAvailabilityZones (Query availability zone)](/doc/api/229/1286) | 200001 (Shanghai Zone 1) |
| goodsNum | Number of elastic cloud storages to be created | 1 |
| storageType | The type of the elastic cloud storage to be created. You can create a HDD or a SSD cloud storage  | cloudBasic |
| period | Availability period of the elastic cloud storage to be created (in months) | 1 |
| payMode | Payment mode. Currently, only Prepaid is supported | prePay |
| storageSize | Size of the elastic cloud storage to be created (GB) | 50 |

 By combining common request parameters and API request parameters, you can get the final request as follows:

```txt
https://cbs.api.qcloud.com/v2/index.php?
Action=CreateCbsStorages
&goodsNum=1
&period=1
&storageSize=50
&storageType=cloudBasic
&zoneId=200001
&Region=sh
&Nonce=1040636527
&SecretId=AKIDxxxxugEY
&Signature=BbxBeaS8GZWiBegYmReA9PjfRbU%3D
&Timestamp=1466045426
```

The result of the above request is as follows. It shows that the instance ID of the elastic cloud storage created is `disk-czwe3ihx`.

```json
{
	"code": 0,
	"message": "",
	"storageIds": ["disk-czwe3ihx"]
}
```

## 3. Mount the Elastic Cloud Storage to the Specified CVM

When the elastic cloud storage has been created, you can use [AttachCbsStorages (Mount elastic cloud storage)](/doc/api/364/2520) to mount it to the specified CVM. In this case, it will be mounted to the CVM `ins-4fet7izv`. The relevant API request parameters are as follows:

| Parameter Name | Description | Value |
| --- | --- | --- |
| storageIds.0 | ID of elastic cloud storage to be mounted | disk-czwe3ihx |
| uInstanceId | ID of CVM to which the elastic cloud storage will be mounted | ins-4fet7izv |

 By combining common request parameters and API request parameters, you can get the final request as follows:

```txt
https://cbs.api.qcloud.com/v2/index.php?
Action=AttachCbsStorages
&storageIds.0=disk-czwe3ihx
&uInstanceId=ins-4fet7izv
&Region=sh
&Nonce=1274548126
&SecretId=AKIDxxxxugEY
&Signature=7EfrW5tX3vPy%2FsebB8A7FOkqwFs%3D
&Timestamp=1466047744
```

The result of the above request is as follows. You can check whether the cloud disk has been mounted to the specified CVM using the API [DescribeCbsStorages (Query Cloud Disk Information)](https://cloud.tencent.com/doc/api/364/2519).

```json
{
	"code": 0,
	"message": "",
	"detail": {
		"disk-czwe3ihx": {
			"code": 0,
			"message": "ok"
		},
	}
}
```

## 4. Initialize the Cloud Storage on CVM

The first time you use the new elastic cloud storage, you need to perform a series of operations on it, such as partitioning, formatting etc. For details, please refer to [Data Disk Partitioning and Formatting on Windows System](https://cloud.tencent.com/doc/product/213/2158) and [Data Disk Mounting, Partitioning and Formatting on Linux System](https://cloud.tencent.com/doc/product/362/3893). Note: For Linux system, partitioning is not necessary. You can skip the partitioning process and directly proceed to the formatting.


