Welcome to Tencent Cloud MongoDB Service!

Cloud MongoDB Service is a high-performance NoSQL database  designed by Tencent Cloud, which is built on the globally accepted MongoDB. It is fully compatible with the MongoDB protocol and offers stable monitoring management. With elastic scalability and automatic disaster recovery capabilities, it applies to document-based database scenarios and eliminates your needs to build disaster recovery system and control management system.

You can use the APIs described in this document to perform operations on the MongoDB service, such as creating a MongoDB instance, querying the instance list, and setting the instance password. For more information, please see [API Overview](/document/product/240/7120).

Before using these APIs, please make sure that you have a thorough understanding of [MongoDB Product Overview](/document/product/240/3544) and [Service Limits](/document/product/240/622)


## 1. Glossary

| Term | Full Name | Description
|---------|---------|---------|
| Instance | Cloud MongoDB Service instance | Abbreviation for Tencent Cloud MongoDB Service |
| VPC | Virtual Private Cloud |	Virtual Private Cloud enables you to build an independent network space in Tencent Cloud to customize IP address ranges, IP addresses, routing policies, etc. You can also establish a VPN tunnel through public network/Direct Connect to achieve interconnection between VPC and your other cloud resources and deploy hybrid cloud flexibly. |

## 2. API Quick Start
To use Tencent Cloud MongoDB Service, you need to complete at least the following four steps:

1) Query supported instance specifications 
You can use API [Query Supported Instance Specifications](/document/product/240/8318) to query the configuration information for the availability zones where MongoDB instances are available.

2) Query the price of a replica set instance (Annual or Monthly Plan)
After confirming specification of the instance to be purchased, you can use API [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) to query the cost for purchasing the instance with specified specification.

3) Create a replica set instance (Annual or Monthly Plan)
You can use API [Create Instance (Annual or Monthly Plan)](/document/product/240/8308) to create an instance. For this purpose, you need to provide instance capacity, purchased usage period, availability zone, network, password and other information.

4) Query the creation progress of instance
After initiating an request for instance creation, you can use API [Query Order Details](/document/product/240/8313) to query the creation progress of the instance.

