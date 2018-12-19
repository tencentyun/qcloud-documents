To connect to a CDB for TDSQL instance, you should "create an account" and "obtain an instance address".

## 1. Creating an Account
### 1.1. Select Account Management on the Account Management Page
Before you start using the TDSQL service, you need to go to the management page of the TDSQL instance, create a database account for logging in to TDSQL, and set access permissions.
![](//mccdn.qcloud.com/img56835afdde2f1.png)

You can see **Account Management** on the management page, as shown below:
![](//mccdn.qcloud.com/img56835b1a37efe.png)
### 1.2. Create an Account
The account consists of a username, CVM IP, and password;
-  **Username**: It should be a combination of letters, numbers and underscores with a maximum length of 16 characters, and begin with a letter and end with a letter or number;
-  **CVM IP**: IP, IP segment, and % are supported. % means all of the IP addresses within a range, For example, if CVMs in the IP range of 10.10.10.1 - 10.10.10.254 are supported, enter 10.10.10.%;
-  **Password**: It should contain eight to 16 characters, including letter, numbers and symbols. According to national information security regulations, it is recommended that you change the password every three months.

![](//mccdn.qcloud.com/img56835b84c71c7.png)

Note: You need to set permissions for different CVM IPs under the same account separately. For a CVM IP to be given permissions similar to those of any one under the same account, select **Clone** in the **Account Management** to clone the account number and permissions.

### 1.3. Set Permissions
The permissions of TDSQL are defined at the object level, including 19 permissions of MySQL. You can also set permissions for objects such as tables, views, functions and triggers.
![](//mccdn.qcloud.com/img56835bf828954.png)
Note: You need to create a database before setting the object-level permissions.

## 2. Obtain the Private Network Access Address
You can obtain the private network access address of an instance on the Instance Details page. Please note that the private network access address refers to the VIP. The database instance is accessed by connecting to the gateway cluster rather than the database instance CPM. Therefore, the private IP does not change during CVM delivery failure or master/slave switch.
![](//mccdn.qcloud.com/img56835cbbbeb73.png)
From a CVM that **resides in the same network** as TDSQL, you can directly connect to the instance's **private network address** to access TDSQL services. Note: You may need to install MYSQL client first.
![](//mccdn.qcloud.com/img56835e0a9470d.png)

