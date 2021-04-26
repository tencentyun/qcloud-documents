## Default Administrator Configuration Example

Super Administrator can only be set by **Creator** or other **Super Administrators**.

**Step 1**: Enter [Cloud Access Management](https://console.cloud.tencent.com/cam) page and click "Create User":
![](//mc.qcloudimg.com/static/img/d0fe6bee5904c659d7e0d701b69e4f65/image.png)

**Step 2**: Enter the administrator name, select "Yes" for **Allow Login to Tencent Cloud**, and enter Login Account
 ID, mobile number, E-mail, and other information:
![](//mc.qcloudimg.com/static/img/37da1c3b7480dafd45537e66bb2a12f7/image.png)

**Step 3**: Select **AdministratorAccess** policy, which can be looked up in the search box above, and click "Finish":
![](//mc.qcloudimg.com/static/img/3ef0ec79089af3f12beaf665fd3bd15f/image.png)

The setting of Super Administrator is completed now. You can log in to Tencent Cloud official website for management using the Login Account. The setting procedure for other default administrators is the same as this process.

## Sub-user Configuration Example

Assume that a sub-user is allowed to query the consumption statistics of "Test Project", manage the configuration information of a domain in "Test Project 2", and refresh a domain in "Test Project 3".

### Creating sub-user

**Step 1**: Click "User Management" on the left, select "Create User" and enter the user information:
![](//mc.qcloudimg.com/static/img/37da1c3b7480dafd45537e66bb2a12f7/image.png)

**Step 2**: Associate with the policy you have just created:
![](//mc.qcloudimg.com/static/img/a172ac9ab1bf6af27859febce74f5db4/image.png)


## Note

+ You can make division of permissions for the policies associated with existing sub-users;

+ The permission level of Default Administrator is higher than that of Project Administrator, which is higher than that of normal sub-user. If policy, project management policy and CDN policy are all associated with a sub-user, the sub-user has a combination of all of the permissions.

  ​

