If you use Cloud Container Service (CCS) in Tencent Cloud which is managed by different users who share your cloud account key, the following problems may exist:
- Your key is shared by multiple users, which leads to a high risk of leakage.
- You cannot limit the access permission of other users, which is easy to pose a security risk due to misoperations.

To avoid the above problems, you can use sub-accounts to allow different users to manage different services. By default, sub-accounts have no permission to use CCS. So we need to create a policy to grant sub-accounts the permissions they need.

## Overview
Cloud Access Management (CAM) is a service package provided by Tencent Cloud, which is used to help customers manage the permissions to access resources under Tencent Cloud accounts in a secure way. By using CAM, you can create, manage and terminate users (or user groups), as well as determine which Tencent Cloud resources can be accessed and who can use them through identity management and policy management.

When using CAM, you can associate a policy to a user or a group of users. The policy can authorize or reject users to finish specified tasks using specified resources. For more basic information about CAM policy, please see [Policy Syntax](/doc/product/598/10603). For more information on how to use CAM policy, please see [Policy](/doc/product/598/10601).
If you don't need to manage the permission of sub-accounts to access CAM resources, you can skip this chapter. This will not affect your understanding and usage of other parts in this document.

## Getting Started
CAM policy must authorize or reject users to perform one or more CCS operations. Meanwhile, it must also specify the resources to work with (all resources, and part of operations can be used as some sources). Policy can also contain conditions to work with resource.

For CCS, some of API operations support resource-level permissions, which means, you cannot specify and use a certain resource when performing such API operations, you must specify all resources to use.

