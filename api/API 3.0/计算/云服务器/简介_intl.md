Welcome to the Cloud Virtual Machine.

The Cloud Virtual Machine (CVM), which runs at the Tencent IDC, provides auto scaling computing services and can be used to build and host software systems based on your business needs.

The CVM solution delivers a flexible set of computing, storage and network resources. You can use the APIs described in this document and refer to the examples to create, terminate and restart CVMs, and adjust bandwidth for them. For a full list of the supported operations, please see the [API Overview](/document/api/213/15689).

Before using these APIs, please make sure that you have a thorough understanding of [CVM Overview](/doc/product/213/495).


> **Note:**
> - All CVM APIs under this module have been upgraded to API 3.0. All new CVM-related features are added to the APIs under this module. We **recommend that new users use the upgraded API 3.0.**
>- The features of old APIs remain available. For more information, please see [CVM API Overview (old)](/document/api/213/568).


## Glossary
The common terms involved in this document are as follows:

| Term | Full Name | Meaning | Description |
|---------|---------|---------|---------|
| Instance | Instance | [Instance](/doc/product/213/4939) | A cloud virtual machine. |
| Region | Region | [Region](/doc/product/213/6091) | A region where resources reside. Each region contains multiple availability zones. |
| Zone | Zone | [Availability zone](/doc/product/213/6091) | Refers to Tencent Cloud's physical IDCs whose power and network are independent from each other within the same [region](/doc/product/213/6091). They are designed to ensure that the failures within an availability zone can be isolated without spreading to and affecting other zones so that users' businesses can provide continuous online services. |
| Image | Image | [Image](/doc/product/213/4940) | A copy of the software environment on a CVM instance, generally including operation systems and installed software. It is used to create an instance. |
| SecurityGroup | Security Group | [Security Group](/doc/product/213/5221) | A virtual firewall that allows state-based packet filtering. As an important network security isolation tool, it is used to control the network access of CVM instances. |
| EIP | Elastic IP | [EIP](/doc/product/213/5733) | A type of public IP. Unlike an ordinary public IP, an EIP belongs to a user account rather than an instance. The mapping relationship between an instance and a public IP can be changed at any time. |
| None | None | Prepaid | A billing method. For more information, please see [Billing Methods](/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88). |
| None | None | Postpaid | A billing method. For more information, please see [Billing Methods](/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9). | |

#### Definitions of input and response parameters
* Limit and Offset
> These parameters are used to control paging. "Limit" indicates the maximum number of entries returned at a time, and "Offset" is the offset value. For the results in a list format, if the number of entries exceeds the "Limit" value, the number of returned values will be limited to the "Limit" value.
>
>For example, if Offset=0&Limit=20, the 0st to 20th entries are returned; if Offset=20&Limit=20, the 20th to 40th entries are returned; if Offset=40&Limit=20, the 40th to 60th entries are returned, and so on.

* Ids.N
> Format for inputting multiple parameters at a time. Multiple parameters in such a format can be input at the same time. For example:
>
> Ids.0=10.12.243.21&Ids.1=10.11.243.21&Ids.2=10.12.243.21&Ids.3=10.13.243.21...
>
> And so on (with subscripts starting with 0).


## Getting Started with API
The following introduces how to use CVM APIs in some typical scenarios:
1. Create an postpaid instance by using the API [Create Instances](/document/api/213/15730) and providing information like availability zone ID, image ID, model and other parameters.

2. Upgrade the configuration of an instance using the API [Adjust Instance Configuration](/document/api/213/15744). You can also change the CPU and memory by adjusting instance models.

3. Shut down an instance using the API [Shut Down Instances](/document/api/213/15743).

4. If you do not want to use an instance any more, you can terminate it using the API [Return Instances](/document/api/213/15723). No fee will apply once the instance is returned.

## Use Limits

* The CVMs created via the API are subject to the number limit described in the [Restrictions on CVM Instance Purchase](/doc/product/213/2664), and share the quota with those created on the official website.

* For more information on specific limits, please see the documents for appropriate APIs or products.

