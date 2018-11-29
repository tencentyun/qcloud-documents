If you use multiple Tencent Cloud services, such as CDB (Cloud DataBase), CVM, VPC, and have these services managed by multiple individuals sharing the same cloud account key of yours, the following problems may occur:

- Your key is shared by multiple individuals, which leads to a high risk of leakage;
- You cannot limit the access permission of other users, which is easy to pose a security risk due to misoperations.

Now, Cloud Access Management comes to solve the issues above.
Cloud Access Management (CAM) is a service package provided by Tencent Cloud, and is used to help customers manage the permissions to access resources under Tencent Cloud accounts in a secure way. By using CAM, you can create, manage and terminate users (or user groups), as well as determine which Tencent Cloud resources can be accessed and who can use them through identity management and policy management. For more information on CAM, please see [CAM Overview](https://cloud.tencent.com/document/product/598/10583).

With CAM, you can use sub-accounts to allow different users to manage different services to avoid the problems above. Sub-accounts have no permissions to use CDB instances or CDB-related resources by default. Therefore, it is necessary to create policies to allow sub-accounts to use the needed resources or permissions.

A policy is a syntax rule used to define and describe one or more permissions. It allows or forbids one user or a group of users to use specific resources through authorization. For more information on CAM policy, please see [Policy Syntax](https://cloud.tencent.com/document/product/378/8962). For more information on how to use CAM policy, please see [Policy](https://cloud.tencent.com/document/product/378/8955).

If you do not need to manage the permission of sub-accounts to access CDB resources, you can skip this chapter. This will not affect your understanding and usage of other parts in this document.

**Getting Started**

CAM policy must allow or forbid users to perform one or multiple CDB operations through authorization. Meanwhile, it must specify the resources (all the resources or parts of resources) for operation. Conditions set for resource operation can also be included in a CAM policy.

>**Note**
> 
> - **The integration of CAM into CDB is only available in some regions where the CDB users can try the CAM. Such regions are Asia Pacific - Seoul, North America - Toronto, Western U.S - Silicon Valley, Europe - Frankfurt, Southeast Asia - Singapore, and Southwest - Chengdu.**
> - **It is highly recommended** that users use CAM policy to manage CDB resources and authorize CDB operations. The existing resources and operations managed by projects are not affected. However, for new resources and operations, it is recommended not to use projects for management and authorization any more.
> - Conditions cannot be set on CDB for now

| Task | Link | 
|:---------|:---------|
| Learn the basic policy syntax | [Policy Syntax](https://cloud.tencent.com/document/product/236/14466?lang=cn/#celueyufa) |
| Define operations in the policy | [CDB Operations](https://cloud.tencent.com/document/product/236/14466?lang=cn/#caozuo) | 
| Define resources in the policy | [CDB Resources](https://cloud.tencent.com/document/product/236/14466?lang=cn/#ziyuanlujing) |
| Resource-level permissions of CDB | [Resource-level Permissions of CDB](https://cloud.tencent.com/document/product/236/14467?lang=cn) |
| Policy Examples for Operations on Console | [Policy Examples for Operations on Console](https://cloud.tencent.com/document/product/236/14468?lang=cn) |
