Permission is used to allow or reject some operations to access resources under certain conditions.
	
By default, the root account is the owner of resources, and has the permission to access all its resources. The sub-account has no permissions to access any resources. The resource creator does not automatically possess the permission to access its created resources, and should be authorized by the resource owner.
	
Policy is the syntax rule used to define and describe one or more permissions. CAM supports two types of policies: preset policy and custom policy. The preset policy (read-only) is a collection of some common permissions created and managed by Tencent Cloud, such as SuperAdmin, cloud resource Admin. The custom policy is a collection of permissions of resource management created by users in a more specific way. The preset policy cannot describe a certain resource in details, which has a rough granularity, while the custom policy can meet the different needs of users for permission management in a flexible manner.
	
You can grant permissions to users or user groups by binding them with one or more policies. The authorized policy can be either a preset policy or a custom policy.
