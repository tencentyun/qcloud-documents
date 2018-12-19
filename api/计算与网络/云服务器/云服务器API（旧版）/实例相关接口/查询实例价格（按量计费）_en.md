## 1. API Description
 
This API (InquiryInstancePriceHour) is used to query the price of postpaid instance.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* This API applies only to <font color="red">postpaid instance</font>. To query the price of a prepaid instance, please use [InquiryInstancePrice](https://cloud.tencent.com/doc/api/229/1349) API.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

* There are range limits on the parameters. For more information on the parameters, please see [here](https://cloud.tencent.com/doc/api/229/1248)

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| cpu | Yes | Int | Number of instance cores. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177).
| mem | Yes | Int | Memory size (GB) of the instance. For limitations on the ratio of CPU to memory, refer to [CVM Instance Configuration](/document/product/213/2177).
| imageId | Yes | String | Image ID. It can be obtained from unImgId in the returned filed of [Query Image](https://cloud.tencent.com/doc/api/229/查询可用的镜像列表) API (the link contains a list of public image names and IDs). |
| imageType | Yes | Int | Image type.  1: Private Image; 2: Public Image; 3: Image form Service Marketplace; 4: Shared Image. The imageType must match the actual type of the imageid. |
| bandwidthType | No | String | Bandwidth type. PayByHour: Charge by bandwidth usage time <br>PayByTraffic: Charge by traffic. <br> The default is to charge by usage time. The difference between the network billing models can be found in [Purchase Network Bandwidth](https://cloud.tencent.com/doc/product/213/509). |
| bandwidth | No | Int | Public network bandwidth (Mbps), or the peak public network bandwidth when bandwidth type is "Pay by Traffic". The default is 0.|
| storageSize | Yes | Int | Data disk size (GB). Increase in increments of 10. 0 means that no data disk is needed. For the maximum size of different data disks, refer to [Overview of Hard Disk Products](https://cloud.tencent.com/doc/product/213/498). |
| storageType | No | Int | Data disk type. 1: Local disk, 2: Cloud Block Storage; local disk by default. For the selection of different data disk types, refer to [Overview of Hard Disk Products](https://cloud.tencent.com/doc/product/213/498). |
| goodsNum | No | Int | Number of purchased instances. The default is 1 and the maximum is 100





## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| data | Array | Return a list |

**Data List Structure**

| Parameter Name | Type | Description |
|---------|---------|---------|
| bandwidth | Array | Bandwidth details. |
| cvm | Array | Instance details. |

**CVM, bandwidth list structure**

| Parameter Name | Type | Description |
|---------|---------|---------|
| price | String | Price. |
| price_unit | String | Price unit. |


## 4. Example
 
Input

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=InquiryInstancePriceHour
  &cpu=1
  &mem=1
  &bandwidthType=PayByTraffic
  &bandwidth=2
  &storageSize=10
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output

```
{
    "code": 0,
    "message": "",
    "data": {
        "cvm": {
            "price": "0.28",
            "price_unit": "HOUR"
        },
        "bandwidth": {
            "price": "1.60",
            "price_unit": "GB"
        }
    }
}
```





