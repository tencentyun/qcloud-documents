### Fast Parameter Configuration
Before initial development, the applications, account and encoding/decoding parameters need to be configured. All configurations can be completed in Tencent Cloud console.
#### Step 1: Create an Application
1. Considering that a company may have multiple applications, a Tencent Video Cloud account can create multiple ILVB applications. However, the data of the applications are independent and isolated from each other. If multiple applications need to access each other, it's recommended to assign a same <b>`SDKAPPID`</b> for them.
2. Log in to Tencent Cloud console and find ILVB business. Click the **Create Application Access** button in the application list and enter a name for the application, then click **OK** to create an application.
3. After the application has been created, you can see <b>`SDKAPPID`</b> in the application list. The backend uses this parameter to identify applications.
4. If multiple applications need to access each other, it's recommended to assign a same<b>`SDKAPPID`</b>for them. In this case, developers are responsible to ensure that accounts assignment are unique across applications.

### Step 2: Choose Account Verification Method

1. To identify users in ILVB applications, you need to choose a verification method to verify accounts with Tencent Video Cloud.
2. The account verification methods are<b>`standalone mode`</b>and<b>`hosted mode`</b>.<br/>
In standalone mode, the developers are responsible for user registration and identity verification. Trust is built with signatures between the developers and Tencent. Most developers choose this mode.<br/>
Hosted mode means that Tencent Cloud provides developers with services of registration, storage and verification of the password for App account. This mode is suitable for quick development scenarios.<br/>
3. Select the application you created in the application list, and click the **App Configuration** link. Then, find **Account Integration System** in basic configurations. Enter your account name, select standalone mode or hosted mode, and confirm. Then you should see <b>`accountType`</b> on the page. This parameter value is also useful in development.

### Step 3. Configure Scenarios and Roles
Select the application you created in the application list, and click the **App Configuration** link. Select **SPEAR Engine Configuration** tab.    

1. Choose application scenario<br/>
The default scenario is instant messaging. For ILVB business, click **Change Scenario** link and choose ILVB scenario.
2. Function of Roles<br/>
Use a role to represent a set of audio/video encoding parameters. The SDK would fetch corresponding audio/video encoding parameters by the name of the role.
3. Add Roles and Encoding/Decoding Parameters Configuration<br/>

Select **Add User Roles and Configuration** under **Windows Web**, **iOS** and **Android** tabs to add the following three roles in each tab. The three roles correspond to the scenarios of starting LVB, joining a room and joining broadcasting, respectively.<br/>


* LiveMaster, choose type **VJ**<br/><br/>
![Add Roles](https://mc.qcloudimg.com/static/img/f3baf920bc8938dbf16dc5465f0a2253/jiaose.jpg)<br/><br/>
* Guest, choose type **Viewer**<br/><br/>
* LiveGuest, choose type **Broadcast Joining Viewer**<br/>



For detailed explanation of roles and parameters, please see [this document](https://github.com/zhaoyang21cn/suixinbo_doc/blob/master/SPEARConfig.md).
