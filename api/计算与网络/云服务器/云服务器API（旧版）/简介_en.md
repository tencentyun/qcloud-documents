Welcome to the Cloud Virtual Machine.

The Cloud Virtual Machine (CVM), which runs at the Tencent Data Center, provides auto scaling computing services and can be used to build and host software systems based on your business needs.

The CVM solution delivers a flexible set of computing, storage and network resources. You can conduct operations like creating/terminating/restarting CVM and changing bandwidth configuration via APIs described in this document. For a complete list of APIs, please refer to [API Overview](/doc/api/229/569).

It's recommended to read [Introduction to CVM Products](/doc/product/213/495) before using these APIs.


## 1. Glossary
This document frequently mentions the following terms:

| Term | Full Name | English | Description |
|---------|---------|---------|---------|
| Instance | Instance |[Instance](https://cloud.tencent.com/doc/product/213/4939) |Indicates a cloud virtual machine.
| Image | Image | [Image](https://cloud.tencent.com/doc/product/213/4940) | A copy of the software environment on a CVM instance, which generally includes operation system and installed software, and is used to create an instance. |
| SecurityGroup | Security Group | [Security Group](https://cloud.tencent.com/doc/product/213/5221) | A type of virtual firewall with a state-based packet filtering feature. It's an important network security isolation method used to control the network access of CVMs. |
| EIP | Elastic IP | [Elastic IP](https://cloud.tencent.com/doc/product/213/5733) | A type of public IP. Unlike an ordinary public IP, an elastic IP belongs to a user account rather than an instance. The mapping relationship between an instance and a public IP address can be changed at any time. |
| Zone | Zone | [Availability Zone](https://cloud.tencent.com/doc/product/213/6091) | Tencent Cloud physical data centers in the same [region](https://cloud.tencent.com/doc/product/213/6091) with indepenent power and network resources. They are designed to ensure that the failures within an availability zone can be isolated without spreading to and affecting other zones, so as to ensure users' businesses stability. |
| Prepaid | Prepaid packages | Prepaid annual or monthly plan | A billing model, refer to [Billing Model Instruction](https://cloud.tencent.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88). |
| Postpaid | Postpaid | Postpaid | A billing model, refer to [Billing Model Instruction](https://cloud.tencent.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9). |

#### Definitions of input and return parameters
* "limit" and "offset"

	> These two parameters are used to control number of entries in one page. When results in the list exceeds the "limit" value, only the "limit" defined number of values will be returned. You can use "limit" and "offset" to contorl entries per page. "limit" indicates the maximum number of items returned at a single time, and "offset" indicates the offset value.
	> For example, if you set "offset=0&limit=20", the  1st to 20th entries are returned; if you set "offset=40&limit=20", the 20th - 40th items are returned;  the fortieth to the sixtieth items, and so on.
	
* id.n

	> Formats for entering multiple parameters at the same time. When you encounter a format like this, you can enter multiple input parameters at the same time. For example:
	
	> id.0=10.12.243.21&id.1=10.11.243.21&id.2=10.12.243.21&id.3=10.13.243.21...
	
	> And so on (starting from 0).


## 2. API Quick Start

Let's start from APIs for postpaid CVMs:

1. [Create Postpaid Instances](https://cloud.tencent.com/doc/api/229/1350) API: Create postpaid instances with the specified information like Availability Zone ID, image ID, combination of CPU and memory and data disk size.
2. [Change Configurations of Postpaid Instances](https://cloud.tencent.com/doc/api/229/1344) API: Upgrade configurations of postpaid instances.
3. [Stop Instances](https://cloud.tencent.com/doc/api/229/1250) API: Stop running of unneccessary CVMs
4. [Return Postpaid Instances](https://cloud.tencent.com/doc/api/229/1347) API: Return Terminate postpaid instances and stop  

## 3. Usage Restriction 
* CVM API calling limit:1,000 times per minute (100 times/min for a single API).
* CVMs created by API are subject to the number limit described in the [Restrictions on CVM Instance Purchase](https://cloud.tencent.com/doc/product/213/2664), and share the quota with machines created on the Console.




