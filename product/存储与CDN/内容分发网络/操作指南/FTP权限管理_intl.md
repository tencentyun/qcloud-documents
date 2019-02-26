There may be multiple projects running in parallel in the same Tencent Cloud account. To prevent information leakage between projects, for users who adopt FTP hosting source, Tencent Cloud can assign appropriate hosting source account management solutions with different permission to specific project and directory.

<font style="color:red">Note: Currently, FTP hosting source is no longer available to new users. Existing users can continue to use it.</font>

Log in to [CDN Console](https://console.cloud.tencent.com/cdn), select **Hosted Sources** menu on the left, and then select **Hosting Source Access Management**. You will be directed to the function page for hosting source access management:
![](https://mc.qcloudimg.com/static/img/e426374f4f102dd8c976deafd940f4ac/1.png)

### Create a Sub-account
Click **+ Add a Sub-account** button to create a new FTP sub-account:
![](https://mc.qcloudimg.com/static/img/4d861967cfe52d633b01f6d37e321c23/2.png)

You can set the account info, password, authorized projects, and authorized directories of a sub-account.

**Note**:
+ The account name is defined by the user with the cloud service account as its prefix number;
+ You may not specify the authorized directories. In this case, you have granted all the permission to specified projects;
+ The authorized directory must be an FTP directory that already exists; otherwise the sub-account cannot be added.

### Change Sub-account Password
In the sub-account list, click **Reset Password** on the right side of the sub-account to change its login password:
![](https://mc.qcloudimg.com/static/img/c31757df490b02e46dea3012c9c176c0/3.png)

### Delete a Sub-account
In the sub-account list, click **Delete** on the right side of the sub-account to be deleted. You should enter the password of the sub-account when deleting it:
![](https://mc.qcloudimg.com/static/img/5046465f5c659d92eab2e0c3b9d2612a/4.png)


