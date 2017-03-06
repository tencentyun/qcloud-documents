There may be multiple projects running in parallel in the same Tencent Cloud account. To prevent information leakage between projects, for users who adopt FTP hosting source, Tencent Cloud can assign appropriate hosting source account management solutions with different permission to specific project and directory.

<font style="color:red">Note: Currently, FTP hosting source is no longer available to new users. Existing users can continue to use it.</font>

Log in to [CDN Console](https://console.qcloud.com/cdn), select **Advanced** menu on the left, and then select **Hosting Source Permission Management**. You will be directed to the function page for hosting source permission management:
![](http://mccdn.qcloud.com/static/img/e61cd42218073b9efe883aebf103075b/image.png)

### Create a Sub-account
Click **+ Add a Sub-account** button to create a new FTP sub-account:
![](http://mccdn.qcloud.com/static/img/7704551caa3fdc2754adef8db0393d70/image.jpg)

You can set the account info, password, authorized projects, and authorized directories of a sub-account.

**Note**:
+ The account name is defined by the user with the cloud service account as its prefix number;
+ You may not specify the authorized directories. In this case, you have granted all the permission to specified projects;
+ The authorized directory must be an FTP directory that already exists; otherwise the sub-account cannot be added.

### Change Sub-account Password
In the sub-account list, click **Reset Password** on the right side of the sub-account to change its login password:
![](http://mccdn.qcloud.com/static/img/0db10570a7a3941b17ab554092bcaca1/image.jpg)

### Delete a Sub-account
In the sub-account list, click **Delete** on the right side of the sub-account to be deleted. You should enter the password of the sub-account when deleting it:
![](http://mccdn.qcloud.com/static/img/356e45b89a3330d74ba30647e062ad99/image.jpg)


