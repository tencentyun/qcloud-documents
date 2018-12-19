If you use multiple services such as CLB, CVM and Database, which are managed by different users who share your cloud account key, the following problems may exist:

- Your key is shared by multiple individuals, which leads to a high risk of leakage;
-  You cannot limit the access permission of other users, which is easy to pose a security risk due to misoperations.

[Cloud Access Management (CAM)](https://cloud.tencent.com/document/product/378/8969) is used to manage the permissions to access resources under Tencent Cloud accounts. By using CAM, you can determine which Tencent Cloud resources can be accessed by which sub-accounts through identity management and policy management.

For example, if you have multiple load balancer instances under your account that are deployed in different projects, to manage access permissions and authorize resources, you can bind the administrator of Project A with an authorization policy which states that only this administrator can use the load balancer resources under project A.

If you don't need to manage the permission of sub-accounts to access CLB resources, you can skip this chapter. This will not affect your understanding of other parts in this document.

The feature is in beta test for now and you can submit a [Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB) for application.

###  Basic Concepts of CAM
The root account authorizes sub-accounts by binding policies. The policy setting can be accurate to **"API, Resource, User/User Group, Allow/Deny, Condition"**.

**1. Account**
- **Root account**: As the fundamental owner of Tencent Cloud resources, root account acts as the basis for resource usage fee calculation and billing, and can be used to log in to Tencent Cloud services.
- **Sub-account**: An account created by the root account, which has an ID and identity credential and can be used to log in to Tencent Cloud console. A root account can create multiple sub-accounts (users). **A sub-account does not own any resources by default, and must be authorized by its root account.**
- **Identity credential**: It includes login credentials and access certificates. **Login credential** refers to user login name and password. **Access certificate** refers to the Cloud API keys (SecretId and SecretKey).

**2. Resources and Permissions**

- **Resources**: Resources are the objects to be operated in cloud services, such as CVM instance, COS bucket, VPC instance, and so on.
- **Permission**: Permission is an authorization to allow or reject some users to perform certain operations and access certain resources. By default, **a root account has the full access to all the resources under it**, while **a sub-account does not have access to any resources under its root account**.
- **Policy**: Policy is the syntax rule used to define and describe one or more permissions. **A root account** grants authorization by **associating policies** with users/user groups.
For more information, please see [CAM Overview](https://cloud.tencent.com/document/product/378/9028).

### Related Documents
| Document description | Link | 
|---------|---------|
| Relationship between policy and user | [Policy Management](https://cloud.tencent.com/document/product/378/8955) |
| Basic structure of policy | [Policy Syntax](https://cloud.tencent.com/document/product/378/8962) | 
| More products that support CAM | [List of Cloud Services that Support CAM](https://cloud.tencent.com/document/product/378/9029)|

