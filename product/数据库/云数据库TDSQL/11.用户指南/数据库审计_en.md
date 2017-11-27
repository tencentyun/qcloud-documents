## 1. Overview

### 1.1 Background

Enterprises may be faced with the following security risks when using database. A complete post-audit and trace mechanism is required for these risks, that is why database audit capacity emerged.

**Administrative risks**
- Misoperations, rule-breaking operations, unauthorized operations performed by system admin prevent the business system from running securely; 
- There is no clear accountability because one account is used by multiple users;
- Misoperations, malicious operations and tampering by development and maintenance staff from a third party; 
- Super admin who has excessive permissions cannot perform audit control;


**Technical risks**
- Backdoor or bugs left by application system developers; 
- Backdoor left by a former employee.

**Policy risks**
- The requirements of national level protection (level 3) (7.1.3.3) cannot be met;
- The requirements of industrial information security compliance file cannot be met, for example, "Classified Protection of Information System of Financial Industry" of The People's Bank of China;
### 1.2 Terminology

**Audit policy:** It is used to define the user behaviors to be audited and the response method. **"Audit policy"="Audit object" + "Audit rule" + "Response action"** is the way to configure an audit policy. To this end, you need to specify audit content. After resolution, if the characteristics of some (user or system) behaviors are in conformity with an audit rule, and these behaviors occurs exactly when the policy becomes effective, the audit engine will send a response according to the response method defined by this policy, for example, an alarm, etc.

**Audit rule:** A collection of behaviors to be audited specified in an audit policy. A rule is comprised of rule parameters, and each parameter defines the matching characteristics of a specific behavior.

### 1.3 Product capability and limits

Tencent Cloud provides database audit capability, to help enterprises to carry out the risk control on a possible access to database, and provide a higher level of data security. The audit logs are retained for 15 days in default (the retention time can be prolonged in future versions).

## 2. Audit operation

### 2.1 Enable database audit feature

Currently, users who use Cloud Database MariaDB (TDSQL) can enable database audit free of charge. You can enable this feature in "Tencent Cloud Console -> Cloud Database -> MariaDB (TDSQL) -> Database Audit" page.

Please note the following points when enabling audit feature:

-  You must have at least one CDB for MariaDB (TDSQL) instance that is not offline or isolated, otherwise the system will disable your audit feature automatically.
-  The MariaDB (TDSQL) instance purchased before June 5, 2016 requires to be rebooted and upgraded to support this feature. Since reboot and upgrade may cause interruption of service for 1 to 5 seconds, you can contact Tencent Cloud staff to schedule time for upgrade.
-  Database audit logs are displayed in plaintext, so you are recommended to enable [Secondary Login Authentication](https://cloud.tencent.com/document/product/378/8392). However, this is not required.
![](//mccdn.qcloud.com/static/img/89e47d9466f5d5b2db1d9e6602eb94b7/image.png)
Audit enabling interface
![](//mccdn.qcloud.com/static/img/ac6fc0157833324ac398228c1a1415f0/image.png)
It may take a few minutes for initialization when enabling audit feature, please wait a moment.

### 2.2 Create audit rule

After the audit feature is enabled, logs are sent to the audit cluster automatically through MariaDB (TDSQL) gateway cluster. However, since no audit rules or policies are created, logs will not be recorded or displayed persistently. Therefore, you can store the logs in the audit cluster through "Create Audit Rule" -> "Associate Audit Policy".

1. Enter the audit interface, and select "Audit Rule" button to create a rule
![](//mccdn.qcloud.com/static/img/10ee0d0b0eb5a49887df8419daee306d/image.png)
2. Enter the name of audit rule and select "Next Step"
![](//mccdn.qcloud.com/static/img/a5c1d8e4de3ca3c8e0b491372efc1644/image.png)
3. Go to the parameter configuration page, and enter the rule parameters (you need to enter at least one of the listed rule parameters, and not all of them are required).
Please note the following capabilities when entering rule parameters:
- . **Conditional relationship between rule parameters:** The relationship between rule parameters is "and" relationship, that is, the match is successful if all the parameters are conform to the conditional rules.
- . **Characteristic string:** It is used to define the parameter, i.e., the characteristics of operation object. To achieve exact match, users only define the key words of the parameter they need, so that the audit system can only record user-defined rules to improve the retrieval efficiency of audit. Note: Empty characteristic string means users do not need this parameter, i.e., "match all".
- . **Match type:** The relationship between parameter object and characteristic.
  - . **Include:** It means the match is successful if a characteristic string is displayed in network field;
  - . **Exclude:** It means the match is successful if a characteristic string is not displayed in network field;
  - . **Equal to:** It means the match is successful if network field is equal to characteristic string;
  - . **Unequal to:** It means the match is successful if network field is unequal to characteristic string;
  - . **Regular expression:** It refers to a characteristic string, and supports standard [Regular Expression Syntax](https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F).
![](//mccdn.qcloud.com/static/img/241c4669c908d346b7a2cd16632d8cf1/image.png)
4. All the new rules can be viewed in the list of rules
![](//mccdn.qcloud.com/static/img/4f6a7744d82875b836ed3d2e4283e0bc/image.png)
5. After the audit rules are configured, you can "make modifications" at any time. You can use the "clone rule" to create similar rules to improve efficiency.

### 2.3 Create audit policy

The audit policy is a complete audit solution by combining "audit rule, audit object and response method". Users can create multiple audit policies for one instance at a time. During the resolution by audit engine, the matching is performed according to the configuration sequence of user's policies in priority order (from top to bottom). Create an audit policy by following the steps below:
1. Enter the policy generation window, select "Audit Policy", and click "Create Policy" button
![](//mccdn.qcloud.com/static/img/a5711897868ec47f9fcdcc1d8f95ed9c/image.png)
2. Enter policy requirements: Select the instance to be audited as required, and select corresponding rules (the configuration of alarm is not supported currently).
![](//mccdn.qcloud.com/static/img/5ee47ce0b915dfabb76c4ec071cc2fdf/image.png)
3. Adjust priority: You can adjust the priority for multiple policies under the same instance (a smaller priority number implies a higher priority). The priority is expected to take effect within one minute after adjustment.
![](//mccdn.qcloud.com/static/img/9a0cf48a91f9cab02344a08ad9eb2333/image.png)
4. You can modify audit policies in real time using modification feature. New policies are expected to take effect within 5 minutes after modification, and used for matching. The logs before modification of audit policies will not be modified.

### 2.4 View logs

The SQL statement matched to audit policy is displayed on the audit log page, so you can click to view or search. Note:

- According to design requirements, the audit logs are displayed in plaintext. You are recommended to enable [Secondary Login Authentication](https://cloud.tencent.com/document/product/378/8392) again, to keep logs under control.
- The logs are recorded starting at the time when the audit policy is created. Historical data are not recorded.
- The transaction or storage procedure may be recorded as a single statement. For more information, please see [syntax supported for database audit](https://cloud.tencent.com/doc/product/237/4847)
- The maximum size of single SQL statement supported currently is 1 KB, and the portion in excess will be truncated.
