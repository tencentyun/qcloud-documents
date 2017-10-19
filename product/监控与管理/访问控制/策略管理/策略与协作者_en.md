## Replacing the Collaborator Role
Policy will be completely replacing the collaborator role. When assigning permissions before, you need to configure a user as "Global Collaborator", "Project Collaborator"; in the future, you need to associate "Super Administrator" policy or "Project Administrator" policy to user. The following section will describe how policies replace the collaborator roles, to help you maintain your user habit.

## Preset Policy and Global Collaborator
"Policy" will replace the global collaborator role, and if you need to add collaborator role to a sub-user, associate the corresponding "Preset Policy" instead. The equivalence relations between collaborator roles and preset policies are shown below:

| Collaborator Role | Preset Policy Name | 
|---------|---------|
| Global collaborator (manage cloud resources, users, finance) | Super administrator | 
| Global collaborator (manage cloud resources) | Global cloud resource administrator | 
| Global collaborator (manage finance) | Global finance administrator | 
> You need to create "Custom Policy" to replace project collaborator. For more information, please see "Custom Policies and Project Collaborators".

### Transition from Global Collaborator to Policy

![](//mccdn.qcloud.com/static/img/b59edf2deab1d92d50d9fe6c6912f29a/image.png)
> Initially associate "Preset Policy" with equal effects to global collaborator.


## Custom Policy and Project Collaborator
If you need to add the project collaborator role for a sub-user, create a new "Custom Policy" and associate it to the sub-user. The steps are as follows:

Step 1:  Access the policy management console.
![](//mccdn.qcloud.com/static/img/c89067bbee25cabc34aa058bf7194502/image.png)
Step 2:  Create custom policy. Name the policy "Project A Administrator" and add "Project Management" to the policy. Click "Next".
![](//mccdn.qcloud.com/static/img/f6652cda7f9fc9b7f6ab2a24f9723a04/image.png)
Step 3: Enable the operation permission "Manage Cloud Resources within Project". Click "Next".
![](//mccdn.qcloud.com/static/img/380852b808833321120c5130998a036b/image.png)
Step 4:  Associate objects for "Manage Cloud Resources within Project".
![](//mccdn.qcloud.com/static/img/44fa94c64ccae019ad4a6aeefa840321/image.png)
Step 5:  Select the items to be managed as objects.
![](//mccdn.qcloud.com/static/img/18bb0e3231a835656048d609a38de4a9/image.png)
Step 6:  Click "Finish" to save the policy.
Step 7:  Associate the policy for users or user groups that need the permission.
![](//mccdn.qcloud.com/static/img/4b5d12cf46cfc19178138ebfa1796406/image.png)
Step 8:  Find "Project A Management" policy in the custom policies and associate it with users to complete the authorization process.
![](//mccdn.qcloud.com/static/img/2d35d4b79a7280922ed6160f0e83e01c/image.png)

### Transition from Project Collaborator to Policy
The role of project coordinator is replaced by "Custom Policy" that describes the business permission "Project Management". Tencent will pre-initialize a number of "Custom Policies" for the existing project collaborators and associate the policies to sub-users, in order to ensure that these sub-users can access the console normally.

#### Initialize Several "Custom Policies"
![](//mccdn.qcloud.com/static/img/fbc70b2ca9cb12769f97afcd645e85a3/image.png)
> The initialization logic is that one project initializes one policy.

#### Initial Association
![](//mccdn.qcloud.com/static/img/07bd7be98b84e6f43b37e890ef0fdfb3/image.png)
> A project collaborator will be initially associated with a series of "Custom Policies" with equal effect.

