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
![](https://mc.qcloudimg.com/static/img/8448453a645b659bac91b62298f4f5f0/2.png)

The mapping relationship is as follows:
+ Manage All Users >>>  AdministratorAccess
+ Manage All Cloud Resources >>>  QCloudResourceFullAccess
+ Manage Finance >>>  QCloudFinanceFullAccess


### Project Collaborator -> Custom Policy

Tencent Cloud's old project collaborator sub-user:

![](https://mccdn.qcloud.com/static/img/5019a4c7687fad90710fc52ca978d1f8/image.png)

After the upgrade to the new CAM system, the old project collaborators will make a smooth transition to a custom policy with the type of "Project Management" and be associated with old sub-users, as shown below:

![](https://mc.qcloudimg.com/static/img/f28443d4315a31919b173924b94c228e/3.png)

You can set the scope of business involved in project management as required.

#### Note
+ Projects owned by the project collaborators remain unchanged;
+ Project collaborators have the permission to perform **any operation** on all resources in specified project.


## Creating Policy

Log in to [Tencent Cloud Console](https://console.qcloud.com), and select [Users and Permissions](https://console.qcloud.com/cam) from the drop-down menu bar:
![](https://mc.qcloudimg.com/static/img/2ac03b249e5fa93e982726f6064e432d/5.png)

Select "Policy Management" in the menu bar on the left, and select "Custom Policy":
![](https://mc.qcloudimg.com/static/img/329d1548a0da4552fc7389ae25f84a4c/6.png)

### Selecting Service Type
Click "Create Custom Policy", name the policy, check "CDN" as the service type, and click "Next":
![](https://mc.qcloudimg.com/static/img/6ef81771a317d2bc0177c792fcea5ef5/7.png)

### Activating Features
CDN provides a number of features for query and management, which cover the permissions to present Console and call APIs. For more information, refer to [CDN Features](). Activate the features you need, and click "Next":

![](https://mc.qcloudimg.com/static/img/b4d6a07995598d6c7945edfea8145eec/8.png)


### Associating with Object

Select "Associating with Object" on the right of feature set to set the resources for which the operation is allowed:

![](https://mc.qcloudimg.com/static/img/97d3ced56e4993c1a236ce8cf300a5ae/9.png)

The features that are activated in the previous step need to be associated with objects. Creator can perform the association in three ways:
+ All Objects: Allow the sub-users to perform this feature on all the objects. Any newly added projects or domains are covered by the permission.
  ![](https://mc.qcloudimg.com/static/img/937590f181cd60dfe93057a63431bbe7/10.png)
+ Project Dimension: The users who don't set any project only have **Default Project**, so they can't associate with objects by project dimension and only can select all objects. The users who have multiple projects can directly divide the projects by project dimension. No resetting is required for newly added or deleted domains in project. (Note: The "All Projects" check box at the top left is only used for selecting all, and newly added projects still cannot be covered by the permission);
   ![](https://mc.qcloudimg.com/static/img/ab6145c54a22837cb286417c4b955deb/11.png)
+ Domain Dimension: Associate with objects individually by domains. If only this type is used, the policy configuration needs to be modified for any newly added domain (querying domain and filtering projects are supported);
   ![](https://mccdn.qcloud.com/static/img/8ef7af35224493aae588ef9c2dea9189/image.jpg)

## Editing Policy

Creator can **only** edit the custom policy. Click to enter "Custom Policy" list:

![](https://mc.qcloudimg.com/static/img/a40a8497d4641d495bcf6789d9f12178/13.png)

You can modify basic information of policy, associated objects and activation/deactivation of features:

![](https://mc.qcloudimg.com/static/img/7f5f6100f66748bf814ea14aa8be655c/14.png)

You can check the user groups or users that have been associated with the policy (only checking is allowed, no modification can be made):

![](https://mc.qcloudimg.com/static/img/55710fc8a6f960b876c17d34da9b25ce/15.png)


## Deleting Policy

Only custom policies can be deleted. You can delete custom policies just by clicking "Delete" on the right. **The policies that have been associated with users or user groups can only be deleted after disassociation**.
![](https://mc.qcloudimg.com/static/img/50e237e17165c9fab8a144f03d8c1354/16.png)
