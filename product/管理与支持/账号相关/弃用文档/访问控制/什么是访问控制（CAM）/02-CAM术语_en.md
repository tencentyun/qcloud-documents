### 1. Root Account

Root account is also known as developer. When a Tencent Cloud account is created, a root account used for logging in to Tencent Cloud services is created. As the fundamental owner of Tencent Cloud resources, root account acts as the basis on which resource usage fee is calculated and billed. A root account has full access to its resources, including accessing the billing information of the account, modifying user password, creating users and user groups, and accessing other cloud service resources. By default, only the root account has access to the resources, and authorization from the root account is required for any access by any other user.

### 2. Sub-account (User) and User Group

Being an entity created by the root account, sub-account has an ID and identity credentials and can log in to Tencent Cloud console. A root account can create multiple sub-accounts (users). A sub-account does not own any resources by default, and must be authorized by its root account. A sub-account can belong to multiple root accounts to assist different root accounts in managing their own cloud resources. But a sub-account can only log in to a single root account at a time to manage the cloud resources under this root account. A sub-account can switch from a root account to another one by switching the developer on console. The sub-account can be automatically switched to the default root account when logging on the console, and owns the access permissions granted by the root account. After switching the developer, the sub-account owns the access permissions granted by the second root account, and the ones granted by the original root account become invalid immediately.
	
Users with the same functions can be added to the same user group, which is assigned the same permissions after being associated with certain policies. 

### 3. Identity Credentials

Identity credentials are used to prove the true identity of a user, and the security of the credentials must be ensured. It includes login credentials and access certificates.
    
Login credentials refer to user login name and password. By logging in to Tencent Cloud console using the login name and password, you can perform operations allowed by your permissions via the console.
    
Access certificates refer to the Cloud API keys (SecretID and SecretKey), including personal API and project keys. In most business scenarios, personal API keys are used to access Tencent Cloud APIs. In a small number of business scenarios, project keys are used to access the Tencent Cloud APIs, including Cloud Image, FaceIn, and COS, etc.
    
Multi-Factor Authentication (MFA) is a security protection built on the above identity credentials. When an MFA device is bound in the security information settings, you can choose to enable login and operation protections. When the MFA login protection is enabled, a user attempting to log in to Tencent Cloud website will be required to enter the dynamic security code from its MFA device for the step-two verification even the user name and password entered have been verified. When the MFA operation protection is enabled, a user must go through the step-two verification by entering the dynamic security code from the MFA device to perform some sensitive operations.

### 4. Resources

Resources are the objects that are operated in cloud services, such as COS bucket or object, VPCID, message queue, and so on. Root account, sub-account, and even policy are also a kind of resource.

### 5. Permission and Policy

Permission is an authorization to allow some users to perform certain operations and access certain resources. By default, a root account has the full access to all its resources, but a sub-account does not have access to any resources under its root account.
	
Policy is the syntax rule used to define and describe one or more permissions. A root account grants authorization by associating policies with users or user groups. A super administrator or any sub-account which is granted the policy management permission can also create, update and delete policies, or grant permissions for policies.
	
All policies can be operated on the user and permission pages of console. Some of the businesses support defining policies on the console-related pages, such as the COS console.
