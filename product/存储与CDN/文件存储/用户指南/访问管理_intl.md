CFS file storage has been connected to CAM authentication, allowing the master account to assign permissions to other users or user groups. CFS provides "full" permissions for authorized users: once authorized, the users can perform all operations related to the file system and permission groups.

To authorize other users to manage CFS file storage resources, follow the instructions below.

## Finding CFS Policy
Log in to the [CAM Console](https://console.cloud.tencent.com/cam), and find QcloudCFSFullAccess policy by searching for CFS on the Policy Management page.
![](https://main.qcloudimg.com/raw/3a6d3a7a506c96d89721c974051e963b.png)

## Viewing Authorization Information
Click on the policy named QcloudCFSFullAccess, and go to the details page. You can see **Policy Syntax** and **Bind User/Group** tags.
![](https://main.qcloudimg.com/raw/2610a3b00ba907d3afd77a1fc24c8c1b.png)

## Authorizing User/User Group
Click **Bind User/User Group**. In the pop-up window, select the user or user group that you want to authorize, and click **OK** to complete the authorization.
![](https://main.qcloudimg.com/raw/265ad68fe5dbd3a508f8f1c1ed4094ce.png)


## Canceling Authorization to User/User Group
Click **Remove User**, and the user/user group cannot perform any operation on CFS file storage resources after the authorization is canceled.
![](https://main.qcloudimg.com/raw/b01115e9d6921cc16a5bcaab2f615874.png)

