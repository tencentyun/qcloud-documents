### How to Upgrade Cloud Database Instance Specification by Yourself
Once you have logged into cloud database console, you can upgrade the specification of specified instance through "Upgrade" operation.
![Upgrade][image-1]

### How to Calculate Fees
When the user is upgrading database instance, the system will calculate the price difference between instance specifications and this price difference will be deducted from the user's account. The user will need to top up first if there isn't enough balance in the account. After the upgrade, the fees will be calculated based on the price of the new instance specification.

### Restrictions when Upgrading Instance Specification by Yourself
1. High-performance instance specification self-upgrade feature is only available to pre-paid users.
2. You can only upgrade instances from smaller specifications into larger ones (such as upgrading a high-performance Type-C instance into high-performance Type-A instance). Degrading is not supported.
3. You can only upgrade an instance when it is in upgradeable status. For an instance that is currently being upgraded, you will need to wait for the upgrade process to complete before upgrading it again.
4. You cannot cancel upgrade process once it has started.

### Note
1. You can still use the original instance as usual during upgrade process (for example, import or export data).
2. The name, access IP and access port of the instance will not change after the instance is upgraded.
\*\* <font color="#FE4C40">3. When the upgrade process is completed, the MySQL database connections will be disconnected within seconds. It is recommended that applications are configured with auto reconnect feature.
4. During upgrade process, please try to avoid operations such as modifying the global parameters of MySQL, instance name, user password. </font> \*\*

[image-1]:	//mccdn.qcloud.com/static/img/d7b59861436817bcc9a0be795c49b1ec/image.png
