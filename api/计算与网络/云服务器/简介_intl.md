

Cloud Virtual Machine (CVM), which runs at the Tencent Data Center, provides auto scaling computing services and can be used to build and host software systems based on your business needs.

The CVM solution delivers a flexible set of computing, storage and network resources. You can conduct operations like creating/terminating/restarting CVM and changing bandwidth configuration via APIs described in this document. For more information, please see [API Overview](/document/api/213/10015).

It's recommended to read [CVM Overview](/doc/product/213/495) before using these APIs.


> **Note:**
>- All CVM APIs under this module have been updated. All new features related to the CVM are added to the APIs under this module. **For new users, it's recommended to use new APIs.**
>- The old APIs remain available. For more information, please see [API Overview (old)](https://cloud.tencent.com/document/product/213/568).


## Glossary
The key terms involved in the document are as follows:

| Term | Description |
|---------|---------|
| [Instance](/doc/product/213/4939) | A cloud virtual machine. |
| [Region](/document/product/213/497#1.-.E5.9C.B0.E5.9F.9F) | A region where resources reside. Each region contains multiple availability zones. |
| [Availability Zone](/doc/product/213/6091) | Tencent Cloud physical data centers in the same [region](/doc/product/213/6091) with independent power and network resources. They are designed to ensure that the failures within an availability zone can be isolated without spreading to and affecting other zones, so as to ensure customers' business stability. |
| [Image](/doc/product/213/4940) | A copy of the software environment on a CVM instance, which generally includes operation system and installed software, and is used to create an instance. |
| [Security Group](/doc/product/213/5221) | A type of virtual firewall with a state-based packet filtering feature. It's an important network security isolation method used to control the network access of CVM instances. |
| [Elastic IP](/doc/product/213/5733) | A type of public IP. Unlike an ordinary public IP, an elastic IP belongs to a user account rather than an instance. The mapping relationship between an instance and a public IP address can be changed at any time. |
| Prepaid | A billing model. For more information, please see [Billing Model Instruction](/doc/product/213/2180#1.-.E5.8C.85.E5.B9.B4.E5.8C.85.E6.9C.88). |
| Postpaid | A billing model. For more information, please see [Billing Model Instruction](/doc/product/213/2180#2.-.E6.8C.89.E9.87.8F.E8.AE.A1.E8.B4.B9). |

#### Definitions of Input and Response Parameters
* Limit and Offset
>These two parameters are used to control number of entries in one page. When results in the list exceeds the Limit value, only the Limit defined number of values is returned. You can use Limit and Offset to control entries per page. Limit indicates the maximum number of entries returned at a time, and Offset indicates the offset value.
>
> For example, if you set `Offset=0&Limit=20`, the 1st to 20th entries are returned; if you set Offset=20&Limit=20, the 20th to 40th entries are returned; if you set Offset=40&Limit=20, the 40th to 60th entries are returned, and so on.
	
* Ids.N
>Formats for entering multiple parameters at the same time. When you encounter a format like this, you can enter multiple input parameters at the same time. For example:
>
>	Ids.0=10.12.243.21&Ids.1=10.11.243.21&Ids.2=10.12.243.21&Ids.3=10.13.243.21...
>	
>  And so on (starting from 0).


## API Quick Start

Let's start from APIs for postpaid CVMs:

1. [Create Postpaid Instances](/document/api/213/9384) API: Create postpaid instances with the specified information like availability zone ID, image ID, model, and parameters.
2. [Change Configurations of Postpaid Instances](/document/api/213/9394) API: Upgrade configurations of postpaid instances by changing CPU and memory through adjustment of instance model.
3. [Stop Instances](/document/api/213/9383) API: Stop running of unnecessary CVMs.
4. [Return Postpaid Instances](/document/api/213/9395) API: Return and terminate postpaid instances and stop charging.

## Usage Restriction 
* CVM API calling limit: Total 1,000 times per minute (100 times/min for a single API).
* CVMs created via API are subject to the number limit described in the [Restrictions on CVM Instance Purchase](/doc/product/213/2664), and share the quota with machines created on the Console.
* For more information about the restrictions, please see the document for each API or the relevant product document.




