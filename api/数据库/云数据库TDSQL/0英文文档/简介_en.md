Welcome to Tencent Cloud Database TDSQL. You can call the APIs discussed in this document to work with CDB for TDSQL. Before the use of these APIs, make sure you have a thorough understanding of the product as well as its usage and billing methods.

The product documentation of TDSQL can be found in [TDSQL Product Documentation](https://cloud.tencent.com/doc/product/237).
## 1. Glossary
| Term | Full Name | Description |
|---------|---------|---------|
| CDB | Cloud Database | High-performance distributed data storage service created based on the open source database MySQL. |
| TDSQL | CDB for TDSQL | Cloud database TDSQL is a relational database compatible with MySQL. Combining high security and availability of commercial databases with low cost of open-source databases, it is mainly applied in enterprise-level service scenarios. |
| VPC	 | Virtual Private Cloud	| Virtual Private Cloud enables you to build an independent network space on Tencent Cloud to customize IP address ranges, IP addresses, routing policies, etc. You can also establish a VPN tunnel through Internet/Direct Connect to interconnect VPC with your other cloud resources and deploy hybrid cloud flexibly. |

## 2. API Quick Start
To use the cloud database TDSQL service, follow steps below:

1. Create instances
You can create instances using API [Create Instance (/doc/api/309/5539), view available instance specifications using API [Query Supported Instance Specifications (/doc/api/309/5537), and query the prices of different instance specifications using API [Query Price](/doc/api/309/5538).

2. Manage instances 
After the instances are created, you can use API [View Instance List](/doc/api/309/5447) to view the list and details of created instances, and use the following APIs to manage the instances and view the statuses of the instances: [Create Account](/doc/api/309/5394), [Set Account Permissions](/doc/api/309/5397), [Renew Instance](/doc/api/309/5541),
[Acquire Log List](/doc/api/309/5402), [View Instance Resources Usage](/doc/api/309/5408), etc.

## 3. Service Limits
When creating an account, you cannot use related APIs to create, modify or delete SuperAdmin (root).
