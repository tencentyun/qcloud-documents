## 1. API Description
This API (DescribeDealsByCond) is used to obtain order information. It's a new API for such operation.

Domain name: trade.api.qcloud.com

## 2. Input Parameters
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| startTime | Yes | datetime | Start time |
| endTime | Yes | datetime | End time |
| page | No | Int | Page number, starting from 0. Default is 0. |
| pageSize | No | Int | Number of data per page. Default is 20. |
| status | No | Int | Order Status. Default is 4 (successful order) <br>Order Status <br>1: Unpaid <br>2: Paid 3: Delivering <br>4: Delivered <br>5: Delivery failed <br>6: Refunded <br>7: Order closed <br>8: Order expired <br>9: Order invalidated <br>10: Product invalidated <br>11: Payment by agent rejected <br>12: Payment is in progress<br> |
| dealId | No | Int | Order ID|


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: Successful; other values: Failed. |
| message | String | Error message |
| data | Array | |
| data.deals | Array | | 
| data.deals.goodsCategoryId | Int | Product Category ID <br> 1 Purchase CVMs   <br> 19 Purchase bandwidth packages   <br> 26 Purchase VPN packages    <br> 27 Renew VPN packages    <br> 28 Update VPN packages    <br> 29 Purchase cloud video service packages    <br> 30 Renew cloud video service packages    <br> 31 Update cloud video service packages    <br> 32 Purchase CDN packages    <br> 34 New version of load balancer    <br> 35 Purchase Dayu service packages    <br> 36 Dayu traffic packages    <br> 40 Purchase LVB    <br> 41 Degrade CVM configuration    <br> 46 Purchase wenzhi monthly package    <br> 47 Renew wenzhi      <br> 48 Update wenzhi    <br> 51 Purchase SSLVPN monthly packages    <br> 52 Renew SSLVPN    <br> 53 Update SSLVPN    <br> 75 Purchase domain names   <br> 76 Renew domain names   <br> 79 Degrade CVM configuration   <br> 100001 Purchase Tencent Cloud Search   <br> 100002 Renew Tencent Cloud Search   <br> 100003 Change the configuration of Tencent Cloud Search   <br> 100004 Purchase MongoDB   <br> 100005 Renew MongoDB   <br> 100006 Change MongoDB configuration   <br> 100007 Purchase BGP high defense service packages   <br> 100008 Renew BGP high defense service packages   <br> 100009 Change the configuration of BGP high defense service packages   <br> 100013 Purchase Redis   <br> 100014 Renew Redis   <br> 100015 Change Redis configuration <br> 100016 Purchase MySQL <br> 100017 Renew MySQL <br> 100018 Change MySQL configuration <br> 100019 Purchase CVMs <br> 100020 Renew CVMs <br> 100021 Change CVM configuration <br> 100025 Purchase game compatibility testing <br> 100036 Purchase BGP super high defense service packages <br> 100037 Renew BGP super high defense service packages <br> 100039 Purchase SQLServer <br>     100040 Renew SQLServer <br> 100041 Change SQLServer configuration <br> 100042 Purchase TdSQL <br> 100043 Renew TdSQL <br> 100044 Change TdSQL configuration <br> 100045 Purchase standalone hosts <br> 100046 Renew standalone hosts <br> 100048 Purchase standalone host submachines <br> 100050 Change the configuration of standalone host submachines <br> 100051 Purchase CPMs <br> 100052 Renew CPMs <br> 100058 Purchase independent cloud disks <br> 100059 Renew independent cloud disks <br> 100060 Change the configuration of independent cloud disks     <br> 100062 Purchase BSPs <br> 100063 Renew BSPs <br> 100064 Change the configuration of BSPs <br> 100065 Purchase CPM MySQL <br> 100066 Renew CPM MySQL <br> 100067 Change CPM MySQL configuration <br> 100069 Purchase physical direct connect <br> 100070 Renew physical direct connect <br> 100072 Purchase BGP high defense IP <br> 100073 Renew BGP high defense IP <br> 100074 Change the configuration of BGP high defense IP <br> 100079 Purchase exclusive cage database clusters <br> 100080 Renew exclusive cage database clusters <br> 100089 Purchase cloud resolution service packages <br> 100090 Renew cloud resolution service packages <br> 100091 Change the configuration of cloud resolution service packages <br> 100092 Purchase HBase <br> 100093 Renew HBase <br> 100095 Purchase SSL certificates <br> 100096 Purchase distributed MongoDB <br> 100097 Renew distributed MongoDB <br> 100098 Change the configuration of distributed MongoDB <br> 100099 Purchase service market <br> 100101 Purchase postgresql <br> 100102 Renew postgresql <br> 100103          Change postgresql configuration <br> 100107 Purchase Yonghong BI <br> 100108 Renew Yonghong BI <br> 100109 Change Yonghong BI configuration <br> 100114 Purchase domain names <br> 100115 Renew domain names <br> 100123 Purchase cdn traffic packages <br> 100131 Purchase additional SMS quota of cloud monitor <br> 100133 Purchase HttpDNS traffic package (10 million times) <br> 100141 Purchase HttpDNS traffic package (30 million times) <br> 100143 Purchase distributed databases <br> 100144 Renew distributed databases <br> 100146 Purchase wetest remote testing <br>    100154 Purchase distributed databases <br> 100155 Purchase website building CVMs <br> 100156 Renew website building CVMs <br> 100166 Purchase SMS <br> 100203 Purchase cloud marketplace products <br> 100206 Purchase cdn traffic packages <br> 100215 Purchase website manager <br> 100218 Purchase Message Service CKafka <br>|
| data.deals.goodsDetail | Array | Product configuration information| 
| data.deals.taskDetail | Array | Parts of product information. Product ID is saved in this field when you purchase a product.| 
| data.deals.realTotalCost | Int | Total cost (in cents)| 
| data.deals.voucherDecline | Int | Coupon consumption (in cents)| 
| data.deals.projectId | Int | Project ID | 

goodsCategoryId product category ID <br>
    

## 4. Example
Input
<pre>
https://trade.api.qcloud.com/v2/index.php?Action=DescribeDealsByCond
&startTime=2016-01-01 00:00:00
&endTime=2016-02-01 00:00:00
&pageSize=2
&page=0
&<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "data":{
        "totalNum":"76",
        "deals":[
            {
                "dealName":"1",
                "dealId":"11",
                "goodsCategoryId":"100114",
                "goodsDetail":{
                    "domain":"dnspod.cn",
                    "years":"1",
                    "service":"DR_CN_NEW"
                },
                "creatTime":"2016-01-07 15:47:34",
                "billId":"20160107030000032133684280",
                "taskDetail":{
                    "flowId":"3333"
                },
                "realTotalCost":"1024",
                "voucherDecline":null,
                "projectId":"0"
            },
            {
                "dealName":"1",
                "dealId":"1",
                "goodsCategoryId":"100114",
                "goodsDetail":{
                    "type":"tdsql",
                    "action":"renewTDsql",
                    "appId":"1351000042",
                    "Memory":"6000",
                    "Storage":"100",
                    "Ids":"40590",
                    "instanceNames":"name40590",
                    "curDeadline":"2016-02-07",
                    "timeSpan":"4",
                    "timeUnit":"d",
                    "ProjectId":"0",
                    "userType":"1",
                    "operator":"909619400"
                },
                "creatTime":"2016-01-07 16:55:24",
                "billId":"2016010703000003213219435981",
                "taskDetail":{
                    "Ids":[
                        "40590"
                    ]
                },
                "realTotalCost":"10000",
                "voucherDecline":null,
                "projectId":"0"
            }
        ]
    }
}
```


