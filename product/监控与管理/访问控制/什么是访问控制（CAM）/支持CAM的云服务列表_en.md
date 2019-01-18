The cloud services that support CAM are listed as follows:

| Service | Policy Syntax | Cloud API | Console | Authorization Granularity | Temporary Certificate |
|---------|---------|---------|---------|---------|---------|
| CDN | Yes | Yes | Yes | Operation level | No |
| CMQ | Yes | Yes | Yes | Resource level | No |
| KMS | Yes | Yes | Yes | Yes | Resource level | Yes |
| ILVB | Yes | No | Yes | Service level | No |
| VOD | Yes | No | Yes | Service level | No |
| LVB | Yes | No | Yes | Service level | No |
| SMS | Yes | No | Yes | Service level | No |
| COS | Yes | Yes | Yes | Resource level | Yes |
| CAS | Yes | Yes | Yes | Resource level | Yes |
| CM | Yes | Yes | Yes | Operation level | Yes |
| [VPC](https://cloud.tencent.com/document/product/215/9510) | Yes | Yes | Yes | Resource level | Yes |
| [CLB](https://cloud.tencent.com/document/product/214/9779) | Yes | Yes | Yes | Resource level | Yes |
| [CVM](https://cloud.tencent.com/document/product/213/10314) | Yes | Yes | Yes | Resource level | Yes |
| DFW | Yes | Yes | Yes | Resource level | Yes |
| CBS | Yes | Yes | Yes | Resource level | Yes |
| CCB | Yes | Yes | Yes | Resource level | Yes |
| CCR | Yes | Yes | Yes | Resource level | Yes |
| CCS | Yes | Yes | Yes | Resource level | Yes |
| Domain Name ICP Licensing | Yes | No | Yes | Service Level | No |
| HS | Yes | Yes | Yes | Operation level | Yes |
| Domain Name Service | Yes | No | Yes | Service level | No |
| Message Subscription | Yes | No | Yes | Service level | No |
| IM | Yes | No | Yes | Service level | No |
| httpdns | Yes | No | Yes | Service level | No | 
| AS | Yes | Yes | Yes | Service level | No |
| Dayu | Yes | Yes | Yes | Service level | No |
| Message Service | Yes | Yes | Yes | Service level | No | 
| Cloud Automated Testing | Yes | No | Yes | Service level | No |
| CLS | Yes | No | Yes | Service level | No | 
| Artificial Audio Intelligence | Yes | No | Yes | Service level | No | 
| Intelligent Customer Service | Yes | No | Yes | Service level | No |
| TDF | Yes | No | Yes | Service level | No |
| WeChat Cloud Pay | Yes | No | Yes | Service level | No | 
| Natural Language Processing | Yes | No | Yes | Service level | No | 
| Tencent Machine Learning | Yes | No | Yes | Service level | No |
| Tencent Machine Translation | Yes | No | Yes | Service level | No |
| Elastic MapReduce | Yes | No | Yes | Service level | No | 
| Tencent Cloud Search | Yes | No | Yes | Service level | No |

Notes:
1. "Cloud APIs" refers to whether cloud APIs are connected to the CAM, and "Console" refers to whether the console is connected to the CAM. 

2. Authorization Granularity is divided into three levels: service level, operation level and resource level. Service-level granularity defines the access to a service, operation-level granularity defines the access to an operation under a service, and resource-level granularity, the finest granularity, defines the access to a resource.

3. Some cloud services such as VPC are available only in gray release. For more information, please see the documentation for specific services.


