List of Cloud Services that Support CAM is as follows:

| Service | Business Permissions | Policy Syntax | Cloud APIs | Console | Authorization Granularity | Conditions | Temporary Certificates |
|---------|---------|---------|---------|---------|
| CDN | Yes | No | Yes | Yes | Operation Level | No | No |
| CMQ | Yes | Yes | Yes | Yes | Resource Level | No | No |
| KMS | Yes | Yes | Yes | Yes | Resource Level | No | No |
| ILVB | Yes | Yes | No | Yes | Service Level | No | No |
| VOD | Yes | Yes | No | Yes | Service Level | No | No |
| LVB | Yes | Yes | No | Yes | Service Level | No | No |
| SMS | Yes | Yes | No | Yes | Service Level | No | No |
| COS | No | Yes | Yes | No | Resource Level | Partially Supported | Yes |
| CAS | No | Yes | Yes | Yes | Resource Level | Partially Supported | Yes |
| CM | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| [VPC (Gray)](https://cloud.tencent.com/document/product/215/9510) | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| CSG (Gray) | No | Yes | Yes | Yes | Resource Level | No | Yes |
| CDB (Gray) | No | Yes | Yes | No | Resource Level | No | No |
| DTS (Gray) | No | Yes | Yes | No | Resource Level | No | No |
| [CLB (Gray)](https://cloud.tencent.com/document/product/214/9779) | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| [CVM (Gray)](https://cloud.tencent.com/document/product/213/10314) | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| DFW (Gray) | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| CBS (Gray) | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| CCB | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| CCR | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| CCS | No | Yes | Yes | Yes | Resource Level | Partially Supported | No |
| CAS | No | Yes | Yes | Yes | Resource Level | Partially Supported | Yes |
| Domain Name ICP Licensing | No | Yes | No | Yes | Service Level | No | No |

Notes:
1) "Business Permission" refers to creating policies based on business permissions, and "Policy Syntax" refers to creating policies based on policy syntax.

2) "Cloud APIs" refers to whether cloud APIs are connected to CAM, and "Console" refers to whether the console is connected to CAM. 

3) Based on the granularity level, authorization granularity is divided into three levels: service level, operation level and resource level. Service-level granularity defines the access to a service, operation-level granularity defines the access to an operation under a service, and resource-level granularity, the finest granularity, defines the access to a resource.

4) Conditions are only supported by several businesses. For the list of services supporting conditions, please see the documentation for specific services.

5) Temporary certificates are only supported by COS and CAS currently.

6) COS only supports XML protocol-based APIs. Some cloud services such as VPC are available only in gray release. For more information, see the documentation for specific services.


