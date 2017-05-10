Welcome to Tencent Cloud Physical Machine.

The Cloud Physical Machine (CPM), which runs at the Tencent Data Center, provides auto scaling computing services and can be used to build and host software systems based on your business needs.

The CPM solution delivers a flexible set of computing, storage and network resources to users. You can use the APIs described in this document and refer to the examples to perform operations such as creation, termination, bandwidth adjustment and reboot on CVMs. For a full list of the supported operations, please see the [API Overview Page](/doc/api/456/6632).

Before using these APIs, please make sure that you have a thorough understanding of [CVM Product Overview](/document/product/386/7031).


## 1. Glossary
The key terms involved in the document are as follows:

| Term | Full Name | Full Name | Description |
|---------|---------|---------|---------|
| Instance | Instance | CPM instance | Refers to a Cloud Physical Machine.
| EIP | Elastic IP | [Elastic IP](https://www.qcloud.com/doc/product/213/%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%EF%BC%88EIP%EF%BC%89#1.-eip.E7.AE.80.E4.BB.8B) | Elastic IP is a public IP. Unlike an ordinary public IP, an elastic IP belongs to a user account rather than an instance. The mapping relationship between an instance and a public IP address can be changed at any time.  |
| Zone | Zone | [Availability Zone](https://www.qcloud.com/doc/product/213/497#2.-.E5.8F.AF.E7.94.A8.E5.8C.BA) | Refers to Tencent Cloud's physical data centers whose power and network are independent from each other within the same [region](https://www.qcloud.com/doc/product/213/497#1.-.E5.9C.B0.E5.9F.9F). They are designed to ensure that the failures within an availability zone can be isolated without spreading to and affecting other zones so that users' businesses can provide continuous online services.  |
| Annual or Monthly Plan | Annual or Monthly Plan | Annual or Monthly Plan |	A billing model. For more information, please see [Billing Models](https://www.qcloud.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88). |
| Pay by Usage | Pay by Usage | Pay by Usage |	A billing model. For more information, please see [Billing Models](https://www.qcloud.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9). |

#### Definitions of Input and Response Parameters
* limit and offset

	> These parameters are used to control paging. For the results in a list format, if the number of entries exceeds the "limit" value, the number of returned values will be limited to the "limit" value. You can use the parameters "limit" and "offset" to control paging. "limit" indicates the maximum number of entries returned at a time, and "offset" is the offset value.
	For example, if offset = 0 & limit = 20, the 0th to the 20th entries will be returned; if offset=20&limit=20, the 20th to the 40th entries will be returned; if offset=40&limit=20, the 40th to the 60th entries will be returned, and so on.
	
* id.n

	> Format for inputting multiple parameters at a time. Multiple parameters in such a format can be input at the same time. For example:
	
	> id.0=10.12.243.21&id.1=10.11.243.21&id.2=10.12.243.21&id.3=10.13.243.21...
	
	> And so on (starting with the subscript 0).


## 2. API Quick Start

Below is a discussion on how to use CPM APIs in some typical scenarios:

1. You can create a CPM paid by usage by using API [Purchase CPM](/doc/api/456/6638) and providing information such as availability zone ID, OS type, and CPM model.
2. You can use API [Shut Down CPM](/doc/api/456/6639) to shut the CPM down. The CPM will stop running once it is shut down.


## 3. Service Limits 
* The quota limit on the count of calls to CPM APIs is 1,000/min; and the count of calls to a single API is limited to 100/min.

* For more information about the restrictions, please see the document for each API or the relevant product document.




