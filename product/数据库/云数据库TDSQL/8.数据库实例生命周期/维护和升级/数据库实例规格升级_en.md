### How to Upgrade Cloud Database Instance Specification by Yourself
Once you have logged into cloud database console, you can upgrade the specification of specified instance through "Upgrade" operation.
![](//mccdn.qcloud.com/static/img/8e5fb888a8c41e2b38c56a8f06163ce2/image.png)

### How to Calculate Fees
When the user is upgrading database instance, the system will calculate the price difference between instance specifications and this price difference will be deducted from the user's account. The user will need to top up first if there isn't enough balance in the account. After the upgrade, the fees will be calculated based on the price of the new instance specification.

### Customizing Upgrade Switching Time
The upgrade switching time can be customized for some instances. So, you can get ready in advance, and select a new master instance with larger configuration to which the instance is switched at the lows of business.

### Note
1. You can still use the original instance as usual during upgrade process (for example, import or export data).
2. The name, access IP and access port of the instance will not change after the instance is upgraded.
3. When the upgrade process is completed, the database connections will be disconnected within seconds. It is recommended that applications are configured with auto reconnect feature.
4. During upgrade process, please try to avoid operations such as modifying the global parameters of database, instance name, user password. 
