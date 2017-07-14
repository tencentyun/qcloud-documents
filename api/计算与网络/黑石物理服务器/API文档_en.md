

Cloud Physical Machine (CPM) is an on-demand physical server rental service provided on a pay-by-usage basis, designed to offer high-performance, securely isolated physical clusters dedicated to cloud. With this service, all you need to do is specifying the model and quantity. The time taken in acquiring the server will be shortened to 4 hours. Tencent Cloud will take care of the server supply and operation& maintenance, allowing you to focus your attention on business innovation.

This document describes how to call the CPM APIs by giving examples. You can create, destroy and restart CPMs or perform other operations. For a complete list of all APIs, please see [API Overview Page](/doc/api/456/6632).

Before using these APIs, please make sure that you have a thorough understanding of [CPM Product](/doc/product/213/495).


## 1. Glossary


| Term | Full Name | Full Name | Description |
|---------|---------|---------|---------|
| Instance | Instance | Instance | A CPM
| Zone | Zone | Availability zone|Tencent Cloud's physical data centers whose electric power facilities and networks are independent from each other within the same region. They are designed to ensure that the failures within an availability zone can be isolated without spreading to and affecting other zones so that users' businesses can provide continuous online services.  |
| N/A | N/A | Annual or Monthly Plan |	A billing model. For more information, please see [Billing Models](https://www.qcloud.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88). |


#### Definitions of input and response parameters
* limit and offset

	>These parameters are used for paging control. If the number of results exceeds the "limit", the number of returned results will equal the value of "limit". You can use the parameters "limit" and "offset" to control paging. "limit" indicates the maximum number of entries returned at a time, and "offset" is the offset value.
	For example, if offset = 0 & limit = 20, the 0th to the 20th entries will be returned; if offset=20&limit=20, the 20th to the 40th entries will be returned; if offset=40&limit=20, the 40th to the 60th entries will be returned, and so on.
	
* id.n

	> Format for inputting multiple parameters at a time. Multiple parameters in such a format can be input at the same time. For example:
	
	> id.0=10.12.243.21&id.1=10.11.243.21&id.2=10.12.243.21&id.3=10.13.243.21...
	
	> And so on (starting with the subscript 0).


## 2. API Quick Start

Several typical scenarios are given here for illustrating how to use CPM APIs:

1. To purchase a CPM, call [BuyDevice](/doc/api/456/6638) and input parameters zoneId, deviceClassCode, etc.
2. To apply for EIPs with the number equaling the value of goodsNum, call [EipBmApply](/doc/api/456/6669) and input parameters goodsNum, payMode, etc.
3. To bind the specified EIP to the specified server, call [EipBmBindRs](/doc/api/456/6673) and input parameters eipId, instanceId, etc.

## 3. Service Limits 
* The quota limit on the count of calls to CPM APIs is 1,000/min; and the count of calls to a single API is limited to 100/min.
* For more information on the service limits, please see the documents for other APIs or products.




