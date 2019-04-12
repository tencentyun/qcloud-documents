## Default Administrator Configuration Example

Super Administrator can only be set by **Creator** or other **Super Administrators**.

**Step 1**: Enter [Users and Permissions](https://console.cloud.tencent.com/cam) page and click "Create User":
![](https://mc.qcloudimg.com/static/img/e868c7d73a299e9cc02aa274ca0f5ed5/1.png)

**Step 2**: Enter the administrator name, select "Yes" for **Allow Login to Tencent Cloud**, and enter QQ ID, mobile number, E-mail, and other information:
![](https://mc.qcloudimg.com/static/img/9ea77958b0f94d4c83f5d678e1905eb2/2.png)

**Step 3**: Select **AdministratorAccess** policy, which can be looked up in the search box above, and click "Finish":
![](https://mc.qcloudimg.com/static/img/e738bd0e91ec8471045c91b709d2949f/3.png)

The setting of Super Administrator is completed now. You can log in to Tencent Cloud official website for management using the QQ ID and QQ password. The setting procedure for other default administrators is the same as this process.

## Project Administrator Configuration Example

Project administrator can manage all cloud resources under the specified projects.
### Creating project administrator policy
**Step 1**: Enter [Users and Permissions](https://console.cloud.tencent.com/cam) page and click the "Policy Management" menu on the left:
![](https://mc.qcloudimg.com/static/img/bf0e1f00266712c8f0511f0869485fd8/4.png)

**Step 2**: Select "Custom Policy":
![](https://mc.qcloudimg.com/static/img/e8e21e27de47ed5d73c226bca82be161/5.png)

**Step 3**: Click "Create Custom Policy":
![](https://mc.qcloudimg.com/static/img/33bf48495b17c80683de2e5284f96e10/6.png)

**Step 4**: Enter the policy name and check "Project Management" as the service type:
![](https://mc.qcloudimg.com/static/img/ea809760b106ae77184a888df9443eaf/7.png)

**Step 5**: Check "Manage Cloud Resources in CDN Business Projects" and "Manage Cloud Resources in Other Business Projects":
![](https://mc.qcloudimg.com/static/img/a80a478ce2eabd8c3d6f392c03b912d4/9.png)

**Step 6**: Click "Associated with Objects"and set projects individually. Note: there is a mapping between features and projects. You can set Project A for "Manage Cloud Resources in CDN Business Projects" and Project B for "Manage Cloud Resources in Other Business Projects":
![](https://mc.qcloudimg.com/static/img/f79aa7aea974c3f4585701177ba44554/11.png)

**Step 7**: The policy is created. You can see it in the List of Custom Policies:
![](https://mc.qcloudimg.com/static/img/d7f3e7eb8dcc81584775f1c08f24e73c/13.png)

### Creating project administrator

**Step 1**: Click "User Management" on the left, select "Create User" and enter the user information:
![](https://mc.qcloudimg.com/static/img/e1fb7b3d6e6f5eafdfb83d19ed733238/14.png)

**Step 2**: Associate with the policy you have just created:
![](https://mc.qcloudimg.com/static/img/25b586a07bbdb1782ed74ad8bef926cd/15.png)


## Sub-user Configuration Example

Assume that a sub-user is allowed to query the consumption statistics of "Test Project", manage the configuration information of a domain in "Test Project 2", and refresh a domain in "Test Project 3".

### Creating sub-user CDN policy
**Step 1**: Enter [Users and Permissions](https://console.cloud.tencent.com/cam) page and click the "Policy Management" menu on the left:
![](https://mc.qcloudimg.com/static/img/05d4985be69ba747fa8df03a95c8eb28/16.png)

**Step 2**: Select "Custom Policy":
![](https://mc.qcloudimg.com/static/img/75750c4d936d9f5049a42e7c4aca70be/17.png)

**Step 3**: Click "Create Custom Policy":
![](https://mc.qcloudimg.com/static/img/ca24e6fcf603c3f6afb5a0b80123e6d6/18.png)

**Step 4**: Check "CDN" as the service type:
![](https://mc.qcloudimg.com/static/img/a3db67b4824e75f94ddf25433cea5dca/19.png)

**Step 5**: Activate "Query Consumption Statistics", "Domain Configuration Management" and "Refresh and Prefetch":
![](https://mc.qcloudimg.com/static/img/efa67584c3c026f0cbbeb20c6e94e384/20.png)

**Step 6**: Associate each feature with corresponding objects, and select the specified project and domain:
![](https://mc.qcloudimg.com/static/img/91b968c9ea07206bb42de5ecb3ca1946/21.png)

**Step 7**: The policy is created. You can see it in the List of Custom Policies:
![](https://mc.qcloudimg.com/static/img/8481a549ca9fba4831973476273596d4/22.png)


### Creating sub-user

**Step 1**: Click "User Management" on the left, select "Create User" and enter the user information:
![](https://mc.qcloudimg.com/static/img/9cee58d37cff9bb79e49cae34625a6c6/23.png)

**Step 2**: Associate with the policy you have just created:
![](https://mc.qcloudimg.com/static/img/5e7b23b731e01d2b5f5ffe2a2b72c87e/25.png)


## Note

+ You can make division of permissions for the policies associated with existing sub-users;

+ The permission level of Default Administrator is higher than that of Project Administrator, which is higher than that of normal sub-user. If policy, project management policy and CDN policy are all associated with a sub-user, the sub-user has a combination of all of the permissions.

  ​

