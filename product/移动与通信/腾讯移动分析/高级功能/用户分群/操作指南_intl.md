To use the user grouping feature, you need to successfully register your App on MTA console, and then you can view the needed user grouping results through the following simple steps:
### Choosing Features on Console
Go to the MTA [Console](http://mta.qq.com/mta/custom/ctr_group/list_all?app_id=1), select an App and the applicable platform (Android or iOS). In the left menu bar, select **Set User Group** under **App Configuration Management**, and then click **New User Group** button in the upper right corner.
![](//mc.qcloudimg.com/static/img/f7deb4769ae60f7b65b3ee6b512065f8/image.png)
### Creating User Group
After clicking New User Group, fill in the group information page as shown in the figure below. You can create a user group according to the following filtering conditions:
1. **User Range**: filter active users/new users within a specified time period.
2. **Device Attributes**: filter the terminal device model and its version.
3. **Custom Event**: filter the user groups that trigger a specific event within a specified time period.
4. **Funnel Model**: filter the user groups that trigger a specific event in a specified sequence within a specified time period. After the relevant information is completed, click **Save User Group**.

>**Notes**:
>1. A maximum of 20 user groups can be created.
>2. A maximum of 5 user groups can be enabled synchronically: the data statistics is performed every day for the enabled user groups. The enabled user group is not editable, and you can only edit it after disabling it. After creating/editing a user group, you need to manually enable it before the data update.
>3. The user group expires and is automatically disabled 1 month later. You can re-enable this user group.

![](//mc.qcloudimg.com/static/img/5120c1438f4db9c306e03bc680ad5156/image.png)
### Viewing Retention Rate of User Group
After creating a user group, turn on the user group switch on the right side to enable it, and then the backend will gather statistics for it every day. You can click **User Retention Rate** under **User/Device Analysis**, and select the name of the user group to be viewed from the user groups in the upper right corner (as shown below). The lower the user retention rate, the lighter the color. You can also choose to view the retention rate in numbers. The data result can be exported in the .csv format. Also, you need to select the time period (7/14/30 days) and the terminal brand and model.
![](//mc.qcloudimg.com/static/img/7f12f4001f06740c27176a8597c4da11/image.png)
### Viewing Loss and Return of User Group
Click **User Loss and Return** under **User/Device Analysis**, and select the name of the user group to be viewed from the user groups in the upper right corner (as shown below). You can view the line chart of user loss and return trend and detailed account information in **User Loss and Return**. The data can be exported in the .csv format. Also, you need to choose the time period and the terminal brand and model.
![](//mc.qcloudimg.com/static/img/e60b02a6d2dc3d23ae448724ca7ac7fb/image.png)
### Viewing Activity Degree of User Group
Click **User Activity Degree** under **User/Device Analysis**, and select the name of the user group to be viewed from the user groups in the upper right corner (as shown below). You can view the total number of accounts in the user activity degree, line chart of activity degree trend and detailed active account information. Also, you need to choose the time period and the terminal brand and model.
![](//mc.qcloudimg.com/static/img/0b6af8fd13a4a33ff092f4da5ce5836e/image.png)
