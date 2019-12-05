## 1. Overview

### (1) Background

An enterprise may face the following security risks when using databases. This situation calls for a complete post-auditing and tracing mechanism, and this is when database auditing comes into play.

**Management Risk**
- Business system security risk caused by misoperations, unauthorized operations and operations against regulations performed by system admin; 
- Difficult to define responsibility because one account is shared by multiple people;
- Misoperations, malicious operations and tampering by development and maintenance staff from a third party; 
- Super admin possesses excessive permission, making it impossible to audit and monitor;


**Technical Risk**
- Backdoors or vulnerabilities left by application system developers; 
- Backdoors left by resigned employees.

**Policy Risk**
- Unable to satisfy the requirements defined by Classified Protection of Information Security (level 3, 7.1.3.3);
- Unable to satisfy the requirements defined by industry information security compliance documents, such as Implementation Guide for Classified Protection of Information System of Financial Industry, issued by the People's Bank of China;
### (2) Terminology Definition

**Audit policies:** These policies define which user actions will be audited and which actions will be taken. **Audit policy = Audit object + Audit rule + Response action**. That is, when configuring an audit policy, you need to specify the content to be audited. If the features of certain actions (either user actions or system actions) comply to an audit rule according to analysis when the policy is in effect, the audit engine will take responsive actions based on the responses defined by this policy, such as issuing an alarm.

**Audit rule:** In an audit policy, an audit rule defines a set of actions that need to be audited. This rule is composed of rule parameters. Each parameter defines a matching feature for a specific action.

### (3) Product Capability and Limits

Tencent Cloud provides database auditing feature. Audit logs are kept for 15 days by default (they can be kept longer in later versions), in order to help enterprises maintain risk control against potential database accesses and improve database security.

## 2. Audit Operation

### (1) Enable Database Auditing

Currently, users who use Cloud Database (TDSQL) can enable database auditing free of charge. You can enable this feature in **Tencent Cloud Console** -> **Cloud Database** -> **TDSQL** -> **Database Audit**.

Please note the following when enabling audit feature:

- .You must have at least one active CDB for TDSQL instance that is not isolated, or the system will cancel your auditing feature automatically.
- .TDSQL instances purchased prior to June 5th, 2016, need to be restarted and upgraded to support auditing feature. Since this process may cause interruption of your business for 1-5 seconds, you can contact Tencent Cloud personnel to make an appointment about the upgrade.
- .Database audit logs are presented in plaintext, thus it is recommended to enable [Two-Factor Authentication]( [https://cloud.tencent.com/help/page/erciyanzheng](https://cloud.tencent.com/help/page/erciyanzheng). This is optional.
![](//mccdn.qcloud.com/static/img/89e47d9466f5d5b2db1d9e6602eb94b7/image.png)
Page for activating auditing feature
![](//mccdn.qcloud.com/static/img/ac6fc0157833324ac398228c1a1415f0/image.png)
It takes several minutes to initialize auditing feature.

### (2) Create Audit Rule

Once auditing is activated, logs will be automatically forwarded to audit cluster through TDSQL gateway cluster. However, since no audit rules or audit policies are created yet, the logs will not be kept or displayed. Therefore, you can store the logs in the audit cluster by **Creating Audit Rule** -> **Associating Audit Policy**.

1. Go to the audit interface and choose **Audit Rule** button to create a rule.
![](//mccdn.qcloud.com/static/img/10ee0d0b0eb5a49887df8419daee306d/image.png)
2. Enter a name for the audit rule and choose **Next**.
![](//mccdn.qcloud.com/static/img/a5c1d8e4de3ca3c8e0b491372efc1644/image.png)
3. Go to parameter configuration page and enter the rule parameters (you need to enter at least one parameter).
Note the following when entering rule parameters:
- . **Condition relation between rule parameters:** The parameters are connected with a relation of "And", which means the rule is only considered a match when all parameters meet the conditions.
- . **Feature string:** The feature string defines details of a parameter, which means the detailed features of the operation object. To achieve exact match, users can simply define the key words of the parameters they need, so that the audit system only needs to record these user-defined rules to improve retrieval efficiency. Note: An empty feature string indicates that the user is not concerned with this parameter, which means "Match All".
- . **Match type:** Relation between parameter object and feature.
  - . **Include:** It means the match is successful if a characteristic string is displayed in network field;
  - . **Exclude:** It means the match is successful if a characteristic string is not displayed in network field;
  - . **Equal to:** This means the match is successful if the network field equals to the feature string;
  - . **Not equal to:** This means the match is successful if the network field does not equal to the feature string;
  - . **Regular expression:** This means the feature string supports standard [Regular Expression Syntax](https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F).
![](//mccdn.qcloud.com/static/img/241c4669c908d346b7a2cd16632d8cf1/image.png)
4. You can view all newly created rules in the rule list.
![](//mccdn.qcloud.com/static/img/4f6a7744d82875b836ed3d2e4283e0bc/image.png)
5. Once an audit rule is configured, you can "Modify" it any time. You can create similar rules through "Clone Rule" to improve efficiency.

### (3) Create Audit Policy

An audit policy is a complete auditing plan which consists of "audit rule", "audit object" and "response method". Users can create multiple audit policies for one instance at a time. During the resolution process, audit engine performs policy matching **according to the sequence configured by user in priority order (from top to bottom)**. Create an audit policy by following the steps below:
1. Go to policy creation window: Select **Audit Policy** and click the **New Policy** button.
![](//mccdn.qcloud.com/static/img/a5711897868ec47f9fcdcc1d8f95ed9c/image.png)
2. Enter policy requirement: Select the instances to be audited based on your needs and choose corresponding rules (alarm configuration is currently not supported).
![](//mccdn.qcloud.com/static/img/5ee47ce0b915dfabb76c4ec071cc2fdf/image.png)
3. Adjust priority: You can adjust priority for multiple policies under the same instance, a smaller number indicates a higher priority. Adjusted priority will take effect within an estimated one minute.
![](//mccdn.qcloud.com/static/img/9a0cf48a91f9cab02344a08ad9eb2333/image.png)
  4. You can modify audit policies in real time by using the modification feature. Modified policies will take effect within an estimated five minutes, and logs prior to modification will not be modified.

### (4) View logs

SQL statements that match with audit policies are presented in the Audit Log page. You can click to view them, or search for logs. Note:
- Due to design requirements, audit logs are presented in plaintext. Again, we recommend that you enable [Two-factor Authentication]( [https://cloud.tencent.com/help/page/erciyanzheng](https://cloud.tencent.com/help/page/erciyanzheng) to maintain control of the logs.
- Logs are recorded starting from when an audit policy is created. History data is not recorded.
- Transactions and storage processes may be recorded as single statements. For more information, please see [Syntax Currently Supported by Database Auditing](https://cloud.tencent.com/doc/product/237/4847).
- The maximum length supported for a single SQL statement is 1 KB. Excessive content will be truncated.
