Welcome to Tencent Cloud CRS!

CRS (Cloud Redis Store) is a caching and storage service that is compatible with Redis protocol. With high availability and high data reliability, it offers user-friendly and reliable Redis services, such as hot backup based on a master/slave architecture, automatic failover, restoration of data to any time point within the last three days, automatic backup, custom configuration of parameters, and viewing of monitoring data.

You can use the APIs described in this document to perform relevant operations on CRS service, such as creating a CRS instance, querying the instance list, and setting the instance password. For supported operations, please see [API Overview](https://cloud.tencent.com/doc/api/260/1749).

Before using these APIs, please make sure that you have a thorough understanding of CRS [Product Overview](https://cloud.tencent.com/doc/product/239/3205) and [Service Limits](https://cloud.tencent.com/doc/product/239/4073).

## 1. Glossary

| Term | Full Name | Full Name | Description
|---------|---------|---------|
| CRS | Cloud Redis Store | Cloud Redis Store | The abbreviation for Tencent Cloud's Cloud Redis Store service |
| VPC	| Virtual Private Cloud	| Virtual Private Cloud |	Virtual Private Cloud enables you to build an independent network space in Tencent Cloud to customize IP address ranges, IP addresses, routing policies, etc. You can also establish a VPN tunnel through public network/Direct Connect to achieve interconnection between VPC and your other cloud resources and deploy hybrid cloud flexibly. |

## 2. API Quick Start
To use CRS APIs, you need to complete at least the following four steps:

1) Query supported specifications
You can use the API [Query Supported Availability Zones](http://cloud.tencent.com/doc/api/260/4951) to query the availability zones where the Redis is available, and then use the API [Query Supported Specifications](http://cloud.tencent.com/doc/api/260/4974) to query the specifications of instances in the availability zones.

2) Query instance price
After confirming the specification of the instance to purchase, use the API [Query Instance Price](https://cloud.tencent.com/doc/api/260/5324) to query the fee to pay for the instance.

3) Create an instance
Use the API [Create Instance](https://cloud.tencent.com/doc/api/260/5325) to create an instance. For this reason, you need to provide information such as instance capacity, purchased usage period, availability zone, network to which the instance belongs and the password;

4) Query the creation progress of instance
After initiating the instance creation request, you can use the API [Query Order](https://cloud.tencent.com/doc/api/260/5329) to query the instance creation progress.
	
## 3. Service Limits
Currently, CRS service is available for all users in any case.


