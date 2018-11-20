In the [CAM console](https://console.cloud.tencent.com/cam), the overview page displays five modules: **CAM Resources, Login Links, Sensitive Operations, Last Login Information, and Security Guidelines**. Each module will be described in detail below.
- If an authorized user logs in to the console, the information of all modules will be displayed, as shown below:
![](https://main.qcloudimg.com/raw/d435c8e7cf7ed16659b33d73da41fa01.png) 
<a id="authority"></a>
- If a non-authorized user logs in to the console, only the **Login Links** and **Last Login Information** will be displayed, as shown below:
The primary account can grant authorization to appropriate sub-users (or collaborators) by the **QcloudCamSummaryAccess policy**, allowing them to view the information in the console overview page.
![](https://main.qcloudimg.com/raw/43041356d65e8f0076f5846d224847b7.png)

## CAM Resources
The CAM Resources module displays the number of users, user groups, and custom policies created under the primary account. Also, you can click the button below a specific number to enter its management page.
![](https://main.qcloudimg.com/raw/eb4a27aef033d26e1b5ac2314f6ddf25.png)

## Login Links
The Login Links module shows login links for sub-users and WeChat Work sub-users. Both the primary account and sub-users can copy the link through the Copy button on the right side of the link.
![](https://main.qcloudimg.com/raw/d68b8ed3cfe89966bc1e556a2240edae.png)
- Sub-users: Suitable for general sub-users.
- Sub-users from WeChat Work: Suitable for sub-users created or associated through WeChat Work.

## Sensitive Operations
The Sensitive Operations module displays the sensitive operation records (up to 50 records) of all accounts under the primary account in last 3 days, including account ID, operator ID, detailed sensitive operation and operation time.
![](https://main.qcloudimg.com/raw/82fdaeb9cb8135c6eef97e64d37db04f.png)
You can also click **View All Records** to enter the CloudAudit console to view sensitive operation records in detail.

## Last Login Information
The Last Login Information module shows the last login time, IP, and location of the current account.
![](https://main.qcloudimg.com/raw/e48475cba7fea457c552c30abba5af92.png)
<a id="more"></a>
## Security Guidelines
The Security Guidelines module provides necessary security operation guidelines about how to use CAM basic features, including enabling MFA, enabling account protection, and creating CAM users and user groups.
The **Enable MFA for Primary Account** and **Enable Protection for Primary Account** options are available only to the primary account. The other five options are available to all authorized users.
**To protect your account and cloud assets, we strongly recommend that you complete all the configurations in the security guidelines.**
Each option can be in the **Incomplete** or **Completed** status. If a primary account user log in to the console, the status of each option will be displayed. But authorized non-main-account users cannot view these statuses.
An authorized user can click the triangle symbol on the left side of each option to view the corresponding feature description and configuration entry. The figure below shows an example of the Security Guidelines module after a primary account user logs in to the console.
![](https://main.qcloudimg.com/raw/8b1276706131c07170af03fcefe54ad0.png)

### Enable MFA for Primary Account
Multi-factor Authentication (MFA) is a simple and efficient security certification method. An MFA device (dynamic password card or token card) can provides an extra layer of protection for your account, besides your username and password. Tencent Cloud offers two types of MFA devices: hardware MFA device and virtual MFA device. 
The primary account user can click **Enable MFA for Primary Account** below the detailed description to enter the specific settings page. For more information, please see:
- [Hardware MFA Device](https://cloud.tencent.com/document/product/378/14520)
- [Virtual MFA Device](https://cloud.tencent.com/document/product/378/14498)

### Enable Protection for Primary Account
A primary account user can enable login protection and operation protection.
- With the login protection enabled, a primary account user must first verify the identity by **MFA** to log in to Tencent Cloud. It helps to prevent the account from being illegally logged in by others who know its password, thus maximizing the security of the account and assets under the account.
- With the operation protection enabled, a primary account user must first verify the identity by **MFA** or **Mobile Verification** to perform sensitive operations, thus avoiding malicious use by others. 

The primary account user can click **Enable Protection for Primary Account** below the detailed description to enter the specific settings page. For more information, please see:
- [Login Protection](https://cloud.tencent.com/document/product/378/8392)
- [Operation Protection](https://cloud.tencent.com/document/product/378/10740)

### Create a CAM User
Create a CAM user and grant the required permissions. A primary account user of Tencent Cloud can manage different types of users with different roles using the user management feature. User types include collaborator, message recipient and sub-user. 
An authorized user can click **Create a User** below the detailed description to enter the specific settings page. For more information, please see:
- [Sub-user](https://cloud.tencent.com/document/product/598/13674)
- [Collaborator](https://cloud.tencent.com/document/product/598/13666)
- [Message Recipient](https://cloud.tencent.com/document/product/598/13667)

### Create a Group and Add Users
Create a user group and add CAM users. Associate appropriate policies for this user group to assign different permissions. This can help you manage and allocate account resources for greater productivity.
An authorized user can click **Create a Group** below the detailed description to enter the specific settings page. For more information, please see:
- [User Group Management](https://cloud.tencent.com/document/product/598/10599)

### Manage Authorization Policy
CAM supports two types of policies: preset policy and custom policy.
- The preset policy is a collection of some common permissions created and managed by Tencent Cloud, such as SuperAdmin, resource management permissions, which has a rough granular. These policies cannot be edited.
- The custom policy created by users allows you to assign permissions with a fine granular. These policies can be edited. 

Assigning permissions to user groups or users can simplify your permission management and audit of CAM users in your account.
An authorized user can click **Manage Custom Policy** below the detailed description to enter the specific settings page. For more information, please see:
- [Policy Management](https://cloud.tencent.com/document/product/598/10601)

### Enable MFA for Sub-users
Enabling MFA for sub-users (CAM users) can help enhance the security of cloud assets. With MFA enabled for CAM users, CAM users must perform secondary authentication to log in to Tencent Cloud or perform sensitive operations in Tencent Cloud, so as to guarantee the asset security. The related MFA settings are important for the cloud asset security. Sub-users or collaborators can only accept the settings of these security attributes for the primary account or users with CAM management permissions.
An authorized user can click **Enable MFA for Sub-users** below the detailed description to enter the specific settings page. For more information, please see:
- **Enable MFA for Sub-users** in [MFA Configuration Guide](https://cloud.tencent.com/document/product/598/14985)

### Enable Protection for Sub-users
An authorized user can enable login protection and operation protection for sub-users (CAM users).
- With the login protection enabled, a sub-user must first verify the identity by **MFA** to log in to Tencent Cloud. It helps to prevent the account from being illegally logged in by others who know its password, thus maximizing the security of the account and assets under the account.
- With the operation protection enabled, a sub-user must first verify the identity by **MFA** or **Mobile Verification** to perform sensitive operations, so as to guarantee the asset security.

Enabling login protection and operation protection for sub-users (CAM users) can help enhance the security of cloud assets.
An authorized user can click **Enable Protection for Sub-users** below the detailed description to enter the specific settings page:
1. Click the name of the sub-user for whom you want to enable protection to enter the user details page.
2. Click **Security Settings** in the user details page.
3. Click **Manage MFA** on the right side of **MFA Device** to enable login protection and operation protection for the selected sub-user.

