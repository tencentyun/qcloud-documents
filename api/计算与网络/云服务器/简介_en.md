Welcome to the Cloud Virtual Machine.

The Cloud Virtual Machine (CVM), which runs at the Tencent Data Center, provides auto scaling computing services and can be used to build and host software systems based on your business needs.

The CVM solution delivers a flexible set of computing, storage and network resources to users. You can use the APIs described in this document and refer to the examples to perform operations such as creation, termination, bandwidth adjustment and reboot on CVMs. For a full list of the supported operations, see the [API Overview Page](/doc/api/229/569).

Make sure you are familiar with the [Introduction to CVM Products](/ doc / product / 213/495) before using these APIs.


## 1. Glossary
This document frequently mentions the following terms:

| Term | Full Name | English | Description |
|---------|---------|---------|---------|
| Instance | Instance |[Instance](https://www.qcloud.com/doc/product/213/4939) |Indicates a cloud virtual machine.
| Image | Image | [Image](https://www.qcloud.com/doc/product/213/4940) | A copy of the software environment on a CVM instance, which generally includes operation system and installed software, and is used to create an instance. |
| SecurityGroup | Security Group | [Security Group](https://www.qcloud.com/doc/product/213/5221) | A type of virtual firewall with a state-based packet filtering feature, and a critical network security isolation means to control the network access of CVMs. |
| EIP | Elastic IP | [Elastic IP](https://www.qcloud.com/doc/product/213/5733) | A type of public IP. Unlike an ordinary public IP, an elastic IP belongs to a user account rather than an instance. The mapping relationship between an instance and a public IP address can be changed at any time. |
| Zone | Zone | [Availability Zone](https://www.qcloud.com/doc/product/213/6091) | Refers to Tencent Cloud's physical data centers whose power and network are independent from each other within the same [region](https://www.qcloud.com/doc/product/213/6091). They are designed to ensure that the failures within an availability zone can be isolated without spreading to and affecting other zones so that users' businesses can provide continuous online services. |
|Not available | Not available | Annual or monthly plan | A billing model, refer to [Billing Model Instruction](https://www.qcloud.com/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88). |
|Not available| Not available| Charge by quantity | A billing model, refer to [Billing Model Instruction](https://www.qcloud.com/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9). |

#### Definitions of input and return parameters
* limit and offset

	> These parameters are used to control pages; for results in a list format, if the number exceeds the "limit" value, then only the "limit" defined number of values will be returned. You can use the parameters "limit" and "offset" to control pages, where "limit" indicates the maximum number of items returned at a single time, and "offset" the offset value.
	> For example, the parameter offset = 0 & limit = 20 returns the zeroth to the twentieth items, offset=20&limit=20 the twentieth to the fortieth items, offset=40&limit=20 the fortieth to the sixtieth items, and so on.
	
* id.n

	> Formats for entering multiple parameters at the same time. When you encounter a format like this, you can enter multiple input parameters at the same time. For example:
	
	> id.0=10.12.243.21&id.1=10.11.243.21&id.2=10.12.243.21&id.3=10.13.243.21...
	
	> And so on (starting with the subscript 0).


## 2. API Quick Start

Below is a discussion on how to use CVM APIs in some typical scenarios:

1. You can simply create a charge-by-quantity instance by using the [Instance Creation](https://www.qcloud.com/doc/api/229/1350) API and providing information like Availability Zone ID, image ID, combination of CPU and memory and data disk size.
2. To change the configuration, you can use the [Configuration Adjustment](https://www.qcloud.com/doc/api/229/1344) API to upgrade the configuration. You can make adjustment to memory size and number of CPU cores, etc.
3. You can use [Instance Shutdown](https://www.qcloud.com/doc/api/229/1250) API to shutdown an instance. The instance will stop running once it is shut down.
4. If you don't want to use an instance any more, you can use the [Instance Return](https://www.qcloud.com/doc/api/229/1347) API to terminate it. No fee will apply once the instance is returned.

## 3. Usage Restriction 
* The quota limit on CVM API calling is 1,000 times per minute; and no more than 100 times per minute for a single API.
* The machines created by API are subject to the number limit described in the [Restrictions on CVM Instance Purchase](https://www.qcloud.com/doc/product/213/2664), and share the quota with machines created by the official website.
* For more details about the restrictions, please refer to the document for each API or the relevant product document.




