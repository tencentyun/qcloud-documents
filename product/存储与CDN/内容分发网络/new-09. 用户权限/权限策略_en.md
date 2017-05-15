A policy involves three factors: service type, feature, and object:

+ Service Type: Select the permission type to set, such as CDN;
+ Feature: Select the allowed CDN operations, such as query for consumption, configuration management, etc. For more information, refer to [CDN Permissions](https://www.qcloud.com/doc/product/228/6689).
+ Object: Specify for each feature the objects for which the feature is allowed. Take CDN as example, the object could be CDN project, CDN domain.

There are two types of policies:
+ Default policy: The collaborator types in old version;
+ Custom policy: The policy customized by the creator.

CAM assigns permissions by associating the configured policy with the user/user group, as described below.

## Transition of Collaborator Mechanism

The old collaborator sub-user system will make a smooth transition to the new CAM permission system. Developers **do not need to modify configurations**, and the use by collaborators **will not be affected**. Different collaborator types will be mapped to different policies and be automatically associated with corresponding sub-users.

### Global Collaborators -> Default Policies

Tencent Cloud's old users and permissions mechanism provides three types of global collaborators, as shown below:
![](https://mccdn.qcloud.com/static/img/e094573d3c490eef87952ef95d32bd2b/image.png)

After the upgrade to the new CAM system, the old collaborator types will make a smooth transition to the existing default policies, as shown below:
![](https://mccdn.qcloud.com/static/img/1cace17172be4a2a603de0c3e6edcfdb/image.jpg)

The mapping relationship is as follows:
+ Manage All Users >>> Super Administrator
+ Manage All Cloud Resources >>> Cloud Resource Administrator
+ Manage Finance >>> Finance Administrator


### Project Collaborator -> Custom Policy

Tencent Cloud's old project collaborator sub-user:

![](https://mccdn.qcloud.com/static/img/5019a4c7687fad90710fc52ca978d1f8/image.png)

After the upgrade to the new CAM system, the old project collaborators will make a smooth transition to a custom policy with the type of "Project Management" and be associated with old sub-users, as shown below:

![](https://mccdn.qcloud.com/static/img/641120f3b17c2d942a20965538b89503/image.png)

You can set the scope of business involved in project management as required.

#### Note
+ Projects owned by the project collaborators remain unchanged;
+ Project collaborators have the permission to perform **any operation** on all resources in specified project.


## Creating Policy

Log in to [Tencent Cloud Console](https://console.qcloud.com), and select [Users and Permissions](https://console.qcloud.com/cam) from the drop-down menu bar:
![](https://mccdn.qcloud.com/static/img/d222bf03bc784de99bd7b1f23063e13a/image.jpg)

Select "Policy Management" in the menu bar on the left, and select "Custom Policy":
![](https://mccdn.qcloud.com/static/img/f4ebdd17551f5fa2381d9cdb6c56f9f6/image.jpg)

### Selecting Service Type
Click "Create Custom Policy", name the policy, check "CDN" as the service type, and click "Next":
![](//mccdn.qcloud.com/static/img/e1ff2e94880181004d4b7f1c9c946eff/image.jpg)

### Activating Features
CDN provides a number of features for query and management, which cover the permissions to present Console and call APIs. For more information, refer to [CDN Features](). Activate the features you need, and click "Next":

![](https://mccdn.qcloud.com/static/img/b372b4c097643683a18d3bfbb5ce80de/image.jpg)


### Associating with Object

Select "Associating with Object" on the right of feature set to set the resources for which the operation is allowed:

![](https://mccdn.qcloud.com/static/img/379782fffb8c93d4b62bba5f1cd78260/image.jpg)

The features that are activated in the previous step need to be associated with objects. Creator can perform the association in three ways:
+ All Objects: Allow the sub-users to perform this feature on all the objects. Any newly added projects or domains are covered by the permission.
  ![](https://mccdn.qcloud.com/static/img/94ccf470b4289fefd327b766b32ca381/image.jpg)
+ Project Dimension: The users who don't set any project only have **Default Project**, so they can't associate with objects by project dimension and only can select all objects. The users who have multiple projects can directly divide the projects by project dimension. No resetting is required for newly added or deleted domains in project. (Note: The "All Projects" check box at the top left is only used for selecting all, and newly added projects still cannot be covered by the permission);
   ![](https://mccdn.qcloud.com/static/img/c5b68d2c37a26a3fa3cfe4b276ac7e1f/image.jpg)
+ Domain Dimension: Associate with objects individually by domains. If only this type is used, the policy configuration needs to be modified for any newly added domain (querying domain and filtering projects are supported);
   ![](https://mccdn.qcloud.com/static/img/8ef7af35224493aae588ef9c2dea9189/image.jpg)

## Editing Policy

Creator can **only** edit the custom policy. Click to enter "Custom Policy" list:

![](https://mccdn.qcloud.com/static/img/9e0f87167d5ee6ec928e3a0c3927653e/image.jpg)

You can modify basic information of policy, associated objects and activation/deactivation of features:

![](https://mccdn.qcloud.com/static/img/3eb77db6fd241b7a2aa41494f0491e18/image.jpg)

You can check the user groups or users that have been associated with the policy (only checking is allowed, no modification can be made):

![](https://mccdn.qcloud.com/static/img/fcb2359300d5b792dd826d07be12a951/image.jpg)


## Deleting Policy

Only custom policies can be deleted. You can delete custom policies just by clicking "Delete" on the right. **The policies that have been associated with users or user groups can only be deleted after disassociation**.
![](https://mccdn.qcloud.com/static/img/1ad3908439ec0ca93fe01324fd494346/image.jpg)
