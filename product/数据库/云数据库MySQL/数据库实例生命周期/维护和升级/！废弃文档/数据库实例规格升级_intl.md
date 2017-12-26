### How to Upgrade Cloud Database Instance Specification by Yourself
Once you have logged into cloud database console, you can upgrade the specification of specified instance through "Upgrade" operation.
![](//mc.qcloudimg.com/static/img/76f13f9030f49071b3b94fac15dabe38/image.png)

### How to Calculate Fees
After the upgrade, the fees will be calculated based on the price of the new instance specification next billing period.

### Restrictions when Upgrading Instance Specification by Yourself
1. You can only upgrade instances from smaller specifications into larger ones (such as upgrading a high-performance Type-C instance into high-performance Type-A instance). **Degrading is not supported.**
2. You can only upgrade an instance when it is in upgradeable status. For an instance that is currently being upgraded, you will need to wait for the upgrade process to complete before upgrading it again.
3. You cannot cancel upgrade process once it has started.

### Note
1. You can still use the original instance as usual during upgrade process (for example, import or export data).
2. The name, access IP and access port of the instance will not change after the instance is upgraded.
3. **When the upgrade process is completed, the MySQL database connections will be disconnected within seconds. It is recommended that applications are configured with auto reconnect feature.**
4. **During upgrade process, please try to avoid operations such as modifying the global parameters of MySQL, instance name, user password.**


