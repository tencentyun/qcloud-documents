Welcome to Tencent Cloud Database MySQL. This document provides APIs for operating MySQL cloud database by calling on requests. Before using these APIs, be sure to fully understand the product, how to use it and its billing method.

In case of any conflict between the value range of any parameter provided in "API Description" of this document and that provided on the Tencent Cloud official website, **the latter shall prevail**.

Here are some commonly used terms in Cloud database MySQL:
## 1. Glossary
| Term | Full Name  | Chinese | Description |
|---------|---------|---------|---------|
| CDB | Cloud Database | Cloud Database | High-performance distributed data storage service professionally created based on open source database MySQL. |
| VPC	 | Virtual Private Cloud	| [Virtual Private Cloud](/doc/api/245/908)	| VPC (Virtual Private Cloud) helps you build an independent network space in Tencent Cloud. You can customize IP address range, IP addresses, routing policies, etc. You can also establish a VPN tunnel through public network/Direct Connect to achieve interconnection between VPC and your other cloud resources and deploy hybrid cloud flexibly. |


## 2. API Quick Start
In order to use the cloud database MySQL service, you need to complete the following steps in order:
1. Create an instance
You can create a new instance using [Create Instance (Annual or monthly plan)](/doc/api/253/1334) or [Create Instance (Pay-by-usage)](/doc/api/253/5175) API; view available instance specifications using [Query Supported Specifications (supporting custom availability zones and configurations)](/doc/api/253/6109) API; query the prices of different instance specifications using [Query Price (Annual or monthly plan)](/doc/api/253/1332) or [Query price (Pay-by-usage)](/doc/api/253/5176) API.
2. Initialize instance
You can use [Initialize Instance](/doc/api/253/5335) API to set the character set, port, root account/password, and table name case sensitivity of the instance.
3. Manage instance
After the instance is initialized, you can view the list of created instances using [Query List of Instances](/doc/api/253/1266) API and manage the instance by choosing to use [Modify Name](/doc/api/253/1270), [Reset Password](/doc/api/253/1271), [Renew Instance](/doc/api/253/1331), [Set Automatic Renewal](/doc/api/253/4112), [Modify Character Set](/doc/api/253/4113) and other APIs.


## 3. Service Limits
Currently, cloud database service is available to all users in any situations.
