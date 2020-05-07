In order to help you get started with CDB for TDSQL APIs quickly, we provide an example on how to use these APIs.
To use the cloud database TDSQL service, you need to create a cloud database TDSQL instance by following the steps below:
First, check available instance specifications by calling API [Query Instance Specifications](/doc/api/309/5537). Each specification has a pid that serves as its product identification. After the specification is selected, you can used its pid to [Query Price](/doc/api/309/5538) and [Create Instance](/doc/api/309/5539).

## 1. Query Instance Specifications
Before creating a CDB instance, you need to check available instance specifications. Only common request parameters are required for this API, so you need not input additional parameters.

By inputting common request parameters, you can get the final request as follows:
```
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetSpecList
&SecretId=AKID6SYaSQcgHd5xxxxxxxlAWpGkaDa55q8
&Nonce=39586
&Timestamp=1470125343
&Region=gz
&Signature=DL6pfNGL1ZC5zM6ceOTVsF7qEKs%3D
```

As shown below, the returned results of the above request contain the configuration and dbType of each specification (returned pid field). 
Upon the expiration of an instance, you can call API [Renew Instance](/doc/api/309/5541) to renew the instance.

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "spec": [
            {
                "machine": "Z3",
                "specinfos": [
                    {
                        "machine": "Z3",
                        "specid": 1,
                        "mem": 48000,
                        "data_disk": 800000,
                        "log_disk": 200000,
                        "title": "Extra-large",
                        "typeName": "Standard",
                        "tdsqlVersion": "Compatible with MySQL 5.5/5.6",
                        "suitInfo": "Extra-large applications with daily independent users at 1,000k level",
                        "qps": 36300,
                        "pid": 10554
                    },
                    {
                        "machine": "Z3",
                        "specid": 2,
                        "mem": 24000,
                        "data_disk": 400000,
                        "log_disk": 100000,
                        "title": "Large",
                        "typeName": "Standard",
                        "tdsqlVersion": "Compatible with MySQL 5.5/5.6",
                        "suitInfo": "Large applications with daily independent users at 1,000k level",
                        "qps": 19300,
                        "pid": 10553
                    },
                    {
                        "machine": "Z3",
                        "specid": 4,
                        "mem": 12000,
                        "data_disk": 200000,
                        "log_disk": 50000,
                        "title": "Medium",
                        "typeName": "Standard",
                        "tdsqlVersion": "Compatible with MySQL 5.5/5.6",
                        "suitInfo": "Medium and large applications with daily independent users at 100k level",
                        "qps": 6800,
                        "pid": 10552
                    },
                    {
                        "machine": "Z3",
                        "specid": 8,
                        "mem": 6000,
                        "data_disk": 100000,
                        "log_disk": 25000,
                        "title": "Small",
                        "typeName": "Standard",
                        "tdsqlVersion": "Compatible with MySQL 5.5/5.6",
                        "suitInfo": "Medium applications with daily independent users at 10k level",
                        "qps": 4100,
                        "pid": 10551
                    }
                ]
            }
        ]
    }
}
```

## 2. Query Price
After selecting a specification, you can use dbType to query the price.
Here, we select the specification "dbType=10551" with memory of 6,000 MB and disk capacity of 100 GB.  Period is 1 month, and number of instances is 1. The relevant API request parameters are as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| costType | No | Int | Billing type: 0: Prepaid; 1: Pay per use. Only "Prepaid" is supported currently |
| dbType | Yes | Int | Product type. For more information, please see pid field in [Query Instance Specifications](/doc/api/309/5537) |
| goodsNum | No | Int | Number of goods |
| period | No | Int | Length of period (in month), which is applicable to "Prepaid" mode |

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlGetPrice
&SecretId=AKID6SYaSQcgHxxxxxxxm4ZlAWpGkaDa55q8
&Nonce=62962
&Timestamp=1470125880
&Region=gz
&dbType=10551
&period=1
&goodsNum=1
&Signature=WXyClJY9nt5cqURjxSBaiTsCs1M%3D
```
According to the returned results of the request as shown below, the price of the instance with the above specification is 1,600 CNY/month.
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "originalPrice": 160000,
    "price": 160000
}
```

## 3. Create an instance
Now, you can call the API "Create Instance" to create an instance.
Here, we select the specification "dbType=10551" with memory of 6,000 MB and disk capacity of 100 GB.  Period is 1 month, and number of instances is 1. The relevant API request parameters are as follows:

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| period | Yes | Int | Length of period (in month) |
| dbType | Yes | Int | Product type, which can be obtained via API [Query Instance Specifications](/doc/api/309/5537) |
| vpcId | No | Int | VPC ID. This field is not applicable now, so the instance can only be allocated to default network currently. |
| subnetId | No | Int | VPC subnet ID. This field is not applicable now, so the instance can only be allocated to default network currently. |
| projectId | No | Int | Project ID, which can be obtained via API [View Project List](/doc/api/309/5604) |
| goodsNum | Yes | Int | Number |

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://tdsql.api.qcloud.com/v2/index.php?Action=CdbTdsqlCreateInstance
&SecretId=AKID6SYaSQcgHxxxxxxJm4ZlAWpGkaDa55q8
&Nonce=695
&Timestamp=1470126034
&Region=gz
&dbType=10551
&period=1
&goodsNum=1
&Signature=YzvTqVYgBIdXbR%2FSvBzVYhPCjto%3D
```

As shown in the returned results of the above request, an order number is generated, which means our data center is delivering goods to you. Later, you can view the instance you just created via API [Query Instance List](/doc/api/309/5447),
or view the information such as instance ID created in the order directly via API [View Order Information](/doc/api/309/5690).
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "dealNames": [
            "20160802121453"
        ],
        "dealIds": [
            "1970063"
        ]
    }
}
```
