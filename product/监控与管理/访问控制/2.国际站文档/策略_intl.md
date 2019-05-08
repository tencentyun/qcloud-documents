## The Role of Policy
Policies describe permissions, when policies are associated with a user or user group, the user(s) can have access to the permissions described by the policies.
![](//mccdn.qcloud.com/static/img/10728645b9bf6e48b3c1f61e6d3caa28/image.png)
> Policy is an abstract representation of permission management capability in the organizational structure.

## Policy Types

### Preset Policy
Preset Tencent Cloud policies, such as system administrators, CDN administrators, etc. Generally, they describe general and all-inclusive permissions to help you quickly assign permissions. For example, if a team leader is associated with the "Super Administrator" policy, then this team leader can be associated with all cloud resources within the account.

### Custom Policy
You can create "Custom Policy" as needed, which allows you to assign permissions with a finer granularity. For example, you can associate a policy with a DBA to authorize him/her to only manage CDB instances, instead of CVM instances.

## Composition of Policy
A policy consists of multiple "Businesses", "Functions" and "Objects", and the three elements describe the permissions together.
For example: a policy describes the permission for deleting the CDN "Domain Name" www.123qc.com;
When the policy is associated with a user, the user can delete the CDN "Domain Name" www.123qc.com, as he/she has obtained the permission described by this policy.

### Business
This refers to the businesses opened to public by Tencent Cloud, such as CVM, CDN, CDB, User and Permission, Finance related businesses and so on. When a business is added to a policy, the policy can be used to describe permissions related to the business. Currently, you can add these businesses to policies:  "CDN", "Project Management", you can add multiple businesses to a policy.

### Function
This refers to the business capabilities provided by the Tencent Cloud businesses that are added into policies. For example: "CDN" provides capabilities for creating new domain name, modifying domain name configurations, etc. You can add multiple capabilities of multiple business to a policy.

### Object
Refers to the scope (cloud resources) affected by the functions, such as CDN domain name, CVM instance, CDB instance, etc.
For example: the CDN domain name www.123qc.com can be deleted;
The scope of "Delete Domain Name" function is "www.123qc.com", which is a CDN domain name that has been added to the account. 
Scope can be a combination of multiple cloud resources. There are three ways to specify a cloud resource. Here, we take CDN as an example:
![](//mccdn.qcloud.com/static/img/45e29235db7efbdbda1050bc3957d070/image.png)
> All objects: All cloud resources under the selected business, including those purchased or added in the future;

![](//mccdn.qcloud.com/static/img/66c22594038723204f05f1344e841112/image.png)
> By item: All domain names under the selected item;

![](//mccdn.qcloud.com/static/img/11573acc1e46b2663720a211979b18c0/image.png)
> By object: Specific domain names, such as the domain names under the project "element_tst", as shown above.

## Associate Policy
After a policy is created, it needs to be associated with users or user groups. When a policy is associated, the users can obtain the permissions described by the policy.
![](//mccdn.qcloud.com/static/img/93423975fb6ed0332690845ebeef2107/image.png)
> Open the detail page of a user or user group to associate policies.

### Associate Policies to User Groups
After a policy is associated with a user group, all users within the user group can obtain the permissions described by this policy.


## Best Practice
In this section, we use a scenario where the sub-user (QQ: 2732034714) is authorized to delete domain names in the CDN business, to describe how to authorize users through policies and explain the usage variance before and after a policy is associated.
After reading this section, you will know how to associate different policies for the sub-users under your account to manager their permissions.

### Before Associating a Policy
Assume a user can browse the CDN console, but isn't associated with the policy that describes the "Delete CDN Domain Name"permission, the user will receive a prompt when trying to delete domain name in the CDN console
![](//mccdn.qcloud.com/static/img/464d2676c8b514868f9e26f02c6531a3/image.png)

### Create Policy
In order for the authorized user to delete specified CDN domain names, you need to create a custom policy.

Step 1:   Go to the policy management console, click "Create Custom Policy".

Step 2:   Add CDN business to the policy and name it as "Best Practice", then click "Next".
![](//mccdn.qcloud.com/static/img/04b6f7953fd9e46fa13d8071a5c2f468/image.png)

Step 3:   "Enable" the permission for the "Delete Domain Name" function, then click "Next".
![](//mccdn.qcloud.com/static/img/7c0c0c72bd5e993f32813cecfd118cfb/image.png)

Step 4:   You need to specify the scope for the "Delete Domain name" function, that is, to specify the domain names that can be deleted. Here, all domain names are associated, including those added in the future. Click "Save".
![](//mccdn.qcloud.com/static/img/0748899793cab8d3c1b6d2c7dd5c5aff/image.png)

Step 5:   The "Best Practice" policy can be found in the policy list.
![](//mccdn.qcloud.com/static/img/001dfce47034e981306af7a95d7760b4/image.png)

### Associate Policy
Step 6:    In the "User Management" page, open the detail page of sub-user (QQ: 2732034714), and associate the "Best Practice" policy to it.
![](//mccdn.qcloud.com/static/img/86ce8761701df36bffe9e65f9b324a8b/image.png)

### After Associating a Policy
Step 7:   In the end, the sub-account (QQ: 2732034714) can log in to the CDN console and delete domain names.

