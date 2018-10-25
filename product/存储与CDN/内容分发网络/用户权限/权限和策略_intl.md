Permission System is designed to allow a developer to manage cloud products, cloud resources and other data information under its account and assign query permissions to achieve the control over operations and protection of sensitive information. Tencent Cloud's old collaborator system could assign permissions by setting global collaborators or project collaborators. For project collaborators, permission isolation by projects is applied. Global collaborators are divided into the following three types by permissions:

+ Manage all users: Add and delete other users
+ Manage finance: View finance-related information
+ Manage all cloud resources: Configure and view all global cloud resources

The old single-permission roles could not satisfy users' need for flexibility in permission division for features. To solve the problem, Tencent Cloud has launched **Cloud Resource Access Management** system, which enables creators to flexibly set the cloud products and data the sub-users are permitted to view as well as the objects they have the permission to perform operations to achieve a permission assignment with a finer granularity.

## Glossaries

#### Sub-user

Sub-users are the users added to the sub-user list by creator without the need to sign up for Tencent Cloud or activate CDN service. There are two types of sub-users:

+ Message-receiving 
+ Console-operating

##### Message-receiving sub-user

These users can receive text messages and e-mails pushed by Tencent Cloud by just undergoing the verification via mobile number or e-mail address, without the need to provide login account. They cannot log in to Tencent Cloud Console for operations. 

##### Console-operating sub-user

These users need to provide login account, mobile number and e-mail address. After being added as sub-users, they can log in to Tencent Cloud official website using login account to perform operations with specified permissions.

For more sub-user-related operations, refer to [Sub-user Management](https://cloud.tencent.com/doc/product/228/6691).

#### User Group

User group is a group of sub-users with same or similar permissions and is used for centralized batch permission assignment and management. For more user-group-related operations, refer to [User Group Management](https://cloud.tencent.com/doc/product/228/6692).

#### Policy

A policy involves three factors: service type, feature, and object:

+ Service Type: Select the permission type to set, such as CDN;
+ Feature: Select the allowed CDN operations, such as query for consumption, configuration management, etc. For more information, refer to [CDN Permissions](https://cloud.tencent.com/doc/product/228/6689).
+ Object: Specify for each feature the objects for which the feature is allowed. Take CDN as example, the object could be CDN project, CDN domain.

There are two types of policies:

+ Default policy: The collaborator types in old version;
+ Custom policy: The policy customized by the creator.

CAM achieves permission assignment by associating the configured policies with user/user group. For more policy-related operations, refer to [Policy Management](https://cloud.tencent.com/doc/product/228/6690).



## Note



+ **All collaborator sub-users** in old version will smoothly transition to the new CAM system with their permissions remaining unchanged. Creator **needs not to assign permissions** for them;

+ The permissions corresponding to the global collaborator types will make a smooth transition to the default policies. The creator can create a type of global collaborator in old version by directly associating with the default policy. For more details, refer to [Policy Management](https://cloud.tencent.com/doc/product/228/6690);

+ The project collaborator sub-users will make a smooth transition to the corresponding policies based on the projects for which they were assigned permissions. The users can add, modify or delete projects that are visible to them as described in the CAM Policy Management section. For more details, refer to [Policy Management](https://cloud.tencent.com/doc/product/228/6690).


