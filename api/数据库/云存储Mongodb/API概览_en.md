## 1. Region APIs
| API | Action Name | Description |
|---------|---------|---------|
| [Query Supported Instance Specifications](/document/product/240/8318) | DescribeMongoDBProduct | Query supported instance specifications |

## 2. Instance APIs

| API | Action Name | Description |
|---------|---------|---------|
| [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) | InquiryMongoDB | Obtain the instance price (annual or monthly plan). Queries of the prices for purchase, renewal and upgrade of instances are supported |
| [Create Instance (Annual or Monthly Plan)](/document/product/240/8308) | CreateMongoDB | Create an instance (annual or monthly plan) and deduct the fee returned by API [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) |
| [Renew Instance (Annual or Monthly Plan)](/document/product/240/8314) | RenewMongoDB | Renew specified instance and deduct the fee returned by API [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) |
| [Upgrade Instance (Annual or Monthly Plan)](/document/product/240/8309) | UpgradeMongoDB | Upgrade specified instance and deduct the fee returned by API [Query Instance Price (Annual or Monthly Plan)](/document/product/240/8311) |
| [Query Order Details](/document/product/240/8313)| DescribeMongodbDealDetail | Query the details of orders for purchase, renewal and upgrade of instances |
| [Query Instance List](/document/product/240/8312) | DescribeMongoDBInstances | Query the list of replica set instance details based on specified conditions | 
| [Set Auto Renewal](/document/product/240/8315) | SetMongoDBAutoRenew | Set or cancel auto renewal. When auto renewal is set, the system will renew the instance automatically upon its expiration |
| [Reset Instance Password](/document/product/240/8316) | ResetMongoDBPassword | Reset the password for an instance |
| [Modify Instance Project](/document/product/240/8307) | ModifyMongoDBProject | Modify the project of an instance |
| [Modify Instance Name](/document/product/240/8306) | ModifyMongoDBName | Modify the name of an instance |
| [Query Task Result](/document/product/240/8310) | GetMongoDBJobInfo | Query the execution result of a task |

