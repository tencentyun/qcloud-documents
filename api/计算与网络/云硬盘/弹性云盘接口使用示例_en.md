In order to help you get started with elastic cloud storage quickly, we provide an example on how to use it.

In the example below, you first need to make an inquiry about the price of the elastic cloud storage to be purchased (this step can be ignored in practice), and then create an elastic cloud storage with the same configuration, and then mount it to the specified CVM.

## 1. Inquire About Price of Elastic Cloud Storage

Before creating an elastic cloud storage, you can inquire about the price of the cloud storage to be purchased using API [InquiryStoragePrice](/doc/api/364/2522). Here we inquire about the price for creating an elastic cloud storage of 50G in Shanghai Zone 1. The relevant API request parameters are as follows:

| Parameter Name | Description | Value |
| --- | --- | --- |
| inquiryType | Inquiry type. It is always "create" when you create an elastic cloud storage | create |
| goodsNum | Number of elastic cloud storages to be created | 1 |
| storageType | Type of elastic cloud storage to be created. You can create a HDD cloud storage or a SSD one | cloudBasic (HDD cloud storage) |
| period | Availability period of the elastic cloud storage to be created (in months) | 1 |
| payMode | Payment mode. Currently, only Prepaid is supported | prePay |
| storageSize | Size of the elastic cloud storage to be created (GB) | 50 |

By combining [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) and API request parameters, you can get the final request as follows:

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

The returned result of the above request is as follows. It shows that RMB 15 will be charged for creating a 50GB elastic cloud storage with an availability period of 1 month in Shanghai Zone 1 .

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
| storageType | Type of elastic cloud storage to be created. You can create a HDD cloud storage or a SSD one | cloudBasic (HDD cloud storage) |
| period | Availability period of the elastic cloud storage to be created (in months) | 1 |
| payMode | Payment mode. Currently, only Prepaid is supported | prePay |
| storageSize | Size of the elastic cloud storage to be created (GB) | 50 |

By combining [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) and API request parameters, you can get the final request as follows:

```txt
https://cbs.api.qcloud.com/v2/index.php?
Action=CreateCbsStorages
&goodsNum=1
&payMode=prePay
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

By combining [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976) and API request parameters, you can get the final request as follows:

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

The result of the above request is as follows. You can check whether the cloud storage has been mounted to the specified CVM using the API [DescribeCbsStorages (Query CBS Information)](https://cloud.tencent.com/doc/api/364/2519).

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

## 4. Initialize the Cloud Disk on CVM

The first time you use the new elastic cloud storage, you need to perform a series of operations on it, such as partitioning, formatting etc. For details, please refer to [Data Disk Partitioning and Formatting on Windows System ](https://cloud.tencent.com/doc/product/213/2158) and [Data Disk Mounting, Partitioning and Formatting on Linux System ](https://cloud.tencent.com/document/product/362/6735
). Note: For Linux system, partitioning is not necessary. You can skip the partitioning process and directly proceed to the formatting.


