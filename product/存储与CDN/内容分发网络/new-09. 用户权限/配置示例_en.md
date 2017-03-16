## Default Administrator Configuration Example

Super Administrator can only be set by **Creator** or other **Super Administrators**.

**Step 1**: Enter [Users and Permissions](https://console.qcloud.com/cam) page and click "Create User":
![](https://mccdn.qcloud.com/static/img/f59bb157507257a5e2a0a32f3ca8198d/image.jpg)

**Step 2**: Enter the administrator name, select "Yes" for **Allow Login to Tencent Cloud**, and enter QQ ID, mobile number, E-mail, and other information:
![](https://mccdn.qcloud.com/static/img/8a987fc8194761ba83410a6d7663486e/image.jpg)

**Step 3**: Select **Super Administrator** policy, which can be looked up in the search box above, and click "Finish":
![](https://mccdn.qcloud.com/static/img/8b2894a36804aee9406770014be7f135/image.jpg)

The setting of Super Administrator is completed now. You can log in to Tencent Cloud official website for management using the QQ ID and QQ password. The setting procedure for other default administrators is the same as this process.

## Project Administrator Configuration Example

Project administrator can manage all cloud resources under the specified projects.
### Creating project administrator policy
**Step 1**: Enter [Users and Permissions](https://console.qcloud.com/cam) page and click the "Policy Management" menu on the left:
![](https://mccdn.qcloud.com/static/img/f5601dc0b52c06eb43711b53517c6a49/image.jpg)

**Step 2**: Select "Custom Policy":
![](https://mccdn.qcloud.com/static/img/b52c032e4cbfa8a6534084e32ee6c3c3/image.jpg)

**Step 3**: Click "Create Custom Policy":
![](https://mccdn.qcloud.com/static/img/d0a26dbda5a8159dc05cee8ff2132b72/image.jpg)

**Step 4**: Enter the policy name and check "Project Management" as the service type:
![](https://mccdn.qcloud.com/static/img/7d2f8ffa81dea40dbba660dc97f2051f/image.jpg)

**Step 5**: Check "Manage Cloud Resources in CDN Business Projects" and "Manage Cloud Resources in Other Business Projects":
![](https://mccdn.qcloud.com/static/img/9812e00b4e54f090aefa13bcccef0f8c/image.jpg)

**Step 6**: Click "Associated with Objects"and set projects individually. Note: there is a mapping between features and projects. You can set Project A for "Manage Cloud Resources in CDN Business Projects" and Project B for "Manage Cloud Resources in Other Business Projects":
![](https://mccdn.qcloud.com/static/img/38808b353006f663041996825bc04197/image.jpg)
![](https://mccdn.qcloud.com/static/img/7df394da29f4e32b3ddba0c5fa7b2a78/image.jpg)

**Step 7**: The policy is created. You can see it in the List of Custom Policies:
![](https://mccdn.qcloud.com/static/img/06ccd5d20f7995f6873c5fa7c6cc08e8/image.jpg)

### Creating project administrator

**Step 1**: Click "User Management" on the left, select "Create User" and enter the user information:
![](https://mccdn.qcloud.com/static/img/9acc24b4ab50655d6e31eaf48f829060/image.jpg)

**Step 2**: Associate with the policy you have just created:
![](https://mccdn.qcloud.com/static/img/1fa9f41d334cc63f4a3c0f70972bccac/image.jpg)


## Sub-user Configuration Example

Assume that a sub-user is allowed to query the consumption statistics of "Test Project", manage the configuration information of a domain in "Test Project 2", and refresh a domain in "Test Project 3".

### Creating sub-user CDN policy
**Step 1**: Enter [Users and Permissions](https://console.qcloud.com/cam) page and click the "Policy Management" menu on the left:
![](https://mccdn.qcloud.com/static/img/f5601dc0b52c06eb43711b53517c6a49/image.jpg)

**Step 2**: Select "Custom Policy":
![](https://mccdn.qcloud.com/static/img/b52c032e4cbfa8a6534084e32ee6c3c3/image.jpg)

**Step 3**: Click "Create Custom Policy":
![](https://mccdn.qcloud.com/static/img/d0a26dbda5a8159dc05cee8ff2132b72/image.jpg)

**Step 4**: Check "CDN" as the service type:
![](https://mccdn.qcloud.com/static/img/90f3b49ce08b1df09df84cc0bbae22a7/image.jpg)

**Step 5**: Activate "Query Consumption Statistics", "Domain Configuration Management" and "Refresh and Prefetch":
![](https://mccdn.qcloud.com/static/img/81154e54d924269601b7f53e59477a07/image.jpg)

**Step 6**: Associate each feature with corresponding objects, and select the specified project and domain:
![](https://mccdn.qcloud.com/static/img/209e544d87729f5d3935b050538a722f/image.jpg)

**Step 7**: The policy is created. You can see it in the List of Custom Policies:
![](https://mccdn.qcloud.com/static/img/9e496d1623b0739dcae757710eecb4e6/image.jpg)


### Creating sub-user

**Step 1**: Click "User Management" on the left, select "Create User" and enter the user information:
![](https://mccdn.qcloud.com/static/img/684f42f3e99ca5107d979c8bd7a4a8be/image.jpg)

**Step 2**: Associate with the policy you have just created:
![](https://mccdn.qcloud.com/static/img/38eff20c6cf9f656a6171a2109c14275/image.jpg)


## Note

+ You can make division of permissions for the policies associated with existing sub-users;
+ The permission level of Default Administrator is higher than that of Project Administrator, which is higher than that of normal sub-user. If policy, project management policy and CDN policy are all associated with a sub-user, the sub-user has a combination of all of the permissions.











