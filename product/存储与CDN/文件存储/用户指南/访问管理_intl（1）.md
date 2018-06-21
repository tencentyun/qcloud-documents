CFS has been connected to CAM authentication, which allows the main account to assign permissions to other users or user groups easily. CFS provides "full control" permissions for authorized users: once authorized, the users can perform all the operations related to the file system and the permission group.

To authorize other users to manage CFS file storage resources, follow the instructions below.

## Finding the CFS Policy
Log in to the [CAM console](https://console.cloud.tencent.com/cam), and find the QcloudCFSFullAccess policy by searching for CFS on the Policy Management page.
![](https://main.qcloudimg.com/raw/3a6d3a7a506c96d89721c974051e963b.png)

## Viewing Authorization Information
Click on the QcloudCFSFullAccess policy to enter the details page, and you can see **Policy Syntax** and **Associate with Users/User Groups** tabs.
![](https://main.qcloudimg.com/raw/2610a3b00ba907d3afd77a1fc24c8c1b.png)

## Authorizing Users/User Groups
Click **Associate with Users/User Groups**. In the pop-up window, select the user or user group that you want to authorize, and click **OK** to complete the authorization.
![](https://main.qcloudimg.com/raw/265ad68fe5dbd3a508f8f1c1ed4094ce.png)


## Cancelling Authorization to Users/User Groups
Click **Disassociate from Users**. The user/user group will not be able to perform any operations on CFS resources after the disassociation is completed.
![](https://main.qcloudimg.com/raw/b01115e9d6921cc16a5bcaab2f615874.png)

