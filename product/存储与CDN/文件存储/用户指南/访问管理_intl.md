CFS file storage has been connected to CAM authentication, allowing the master account to assign permissions to other users or user groups. CFS provides "full" permissions for authorized users: once authorized, the users can perform all operations related to the file system and permission groups.

To authorize other users to manage CFS file storage resources, follow the instructions below.

## Finding CFS Policy
Log in to the [CAM Console](https://console.cloud.tencent.com/cam), and find QcloudCFSFullAccess policy by searching for CFS on the Policy Management page.
![](https://main.qcloudimg.com/raw/5bec8712b800aa8fbc6842040c8f0a0d.png)

## Viewing Authorization Information
Click on the policy named QcloudCFSFullAccess, and go to the details page. You can see **Policy Syntax** and **Bind User/Group** tags.
![](https://main.qcloudimg.com/raw/3f6c1a3a455e505f3b35dd1ec6ee8ae5.png)

## Authorizing User/User Group
Click **Bind User/User Group**. In the pop-up window, select the user or user group that you want to authorize, and click **OK** to complete the authorization.
![](https://main.qcloudimg.com/raw/fec4e159bc7ecd8f9bc7b5d3a3769a06.png)


## Canceling Authorization to User/User Group
Click **Remove User**, and the user/user group cannot perform any operation on CFS file storage resources after the authorization is canceled.
![](https://main.qcloudimg.com/raw/4c4bd44b0592f3f2d51a5fab975dc2e6.png)

