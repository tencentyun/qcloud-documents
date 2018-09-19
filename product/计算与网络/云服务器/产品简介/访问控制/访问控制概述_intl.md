If you use such services as Cloud Virtual Machine (CVM), VPC, and database in Tencent Cloud and these services are managed by different users who share your cloud account key, the following problems may exist:

- Your key is shared by multiple users, which leads to a high risk of leakage.
- You cannot limit the access permission of other users, which is easy to pose a security risk due to misoperation.

To avoid the above problems, you can use sub-accounts to allow different users to manage different services. By default, sub-accounts have no permission to use CVM or related resources. So it is necessary to create a policy to grant sub-accounts the permissions to use the resources they need.

Cloud Access Management (CAM) is a service package provided by Tencent Cloud, which is used to help customers manage the permissions to access resources under Tencent Cloud accounts in a secure way. By using CAM, you can create, manage and terminate users (or user groups), as well as determine which Tencent Cloud resources can be accessed and who can use them through identity management and policy management.

When using CAM, you can associate a policy to a user or a group of users. The policy can authorize or reject users to finish specified tasks using specified resources. For more basic information about CAM policy, please see [Policy Syntax](https://cloud.tencent.com/document/product/378/8962). For more information on how to use CAM policy, please see [Policy](https://cloud.tencent.com/document/product/378/8955).

If you do not need to manage the access permission to CVM resources for sub-accounts, you can skip this chapter. This will not affect your understanding and usage of other parts in this document.

This feature is in Beta test for now. Submit a [Ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=7&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%20CVM) to apply for it.

**Getting Started**

CAM policy must authorize or reject users to perform one or more CVM operations. Meanwhile, it must specify the resources to work with (all resources, or part of resources for some operations). Policy can also contain conditions set for resource operations.

Some of CVM-based API operations support resource-level permissions, which means that you must specify all resources to use but cannot specify a specific resource for use when performing such API operations.




| Task | Link | 
|---------|---------|
| Learn about the basic structure of the policy | [Policy Syntax](https://cloud.tencent.com/document/product/213/10313#celueyufa) |
| Define operations in the policy | [CVM Operations](https://cloud.tencent.com/document/product/213/10313#caozuo) | 
| Define resources in the policy | [CVM Resource Path](https://cloud.tencent.com/document/product/213/10313#ziyuanlujing) |
| Limit the policy with conditions | [CVM Condition Keys](https://cloud.tencent.com/document/product/213/10313#tiaojianmiyue) |
| Resource-level permissions supported by CVM | [Resource-level Permissions Supported by CVM](https://cloud.tencent.com/document/product/213/10314) |
| CAM policy example | [CAM Policy Example](https://cloud.tencent.com/document/product/213/10312) |

