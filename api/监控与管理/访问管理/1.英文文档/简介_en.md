## Cloud Access Management
Thank you for choosing Cloud Access Management (CAM). You can work with and manage the access to the resources under your Tencent Cloud account by calling the APIs described in this document. Please make sure you have a thorough understanding of CAM before using these APIs.

### 1. Glossary
The common glossaries involved in this document are as follows:

| Glossary | Full Name | Description |
| ------------ | ------------ | ------------ | ------------ |
| Role | Role |A virtual account with a set of permissions. It is used to grant access to Tencent Cloud resources under your account. |
| STS | Tencent Cloud Security Token Service | Provide credentials with custom validity period and access permissions. |

### 2. API Quick Start

You can use CAM APIs to manage the access to resources under your Tencent Cloud account. The following describes the application scenarios of APIs in this document.
- Role-related APIs allow you to create a virtual sub-account (role), specify the accounts allowed to assume the role, and grant the role a set of permissions to access resources under your account.
- The API " Apply for Temporary Credentials for Role" is used to get temporary credentials for the role that the user can assume. 
- The API "Get Temporary Credentials for User with Federated Identity" is used to issue credentials with custom validity period and access permissions to a user with federated identity (the user managed by your local account system).

## Role-related APIs
A role in CAM is a virtual sub-account, for which you can grant a set of permissions and specify the users allowed to assume the role. A role can be associated with more than one account, and any user allowed to assume the role can be assigned the role. In addition, a role does not have long-term credentials (passwords or API keys) a standard account has, and CAM dynamically creates temporary credentials for a user who applies for a role. You can work with and manage the roles by calling the APIs described in this document.

### 1. Glossary
The common glossaries involved in this document are as follows:

| Glossary | Full Name | Description |
| ------------ | ------------ | ------------ | ------------ |
| policyDocument | Trust policy of role | Used to grant the specified user the permission to apply for this role. |
| description | Description | Description of the role. |

### 2. API Quick Start

You can manage roles by calling role-related APIs. The following describes the application scenarios of APIs in this document.
- The API "Create Role" is used to create a virtual sub-account (role), and specify the accounts allowed to assume the role.
- The API "Bind Policy to Role" is used to grant the specified role a set of permissions to access resources under your account.
- The API "Unbind Policy from Role" is used to unbind a policy from a role.
- The API "Get Role Information" is used to obtain the details of a role.
- The API "Get Role List" is used to get a list of the roles under your account.
- The API "Modify Trust Policy of Role" is used to modify the trust policy of the specified role.
- The API "Modify Role Description" is used to modify the description of a role.
- The API "Delete Role" is used to delete a role.

## STS-related APIs
Tencent Cloud Security Token Service (STS) is a cloud service that allows Tencent Cloud accounts (or CAM users) to manage short-term access permissions. With STS, you can issue credentials with custom validity period and access permissions to other users so that they can directly call Tencent cloud service APIs with STS temporary credentials.

### 1. Glossary
The common glossaries involved in this document are as follows:

| Glossary | Full Name | Description |
| ------------ | ------------ | ------------ | ------------ |
| policy | Policy | The policy granted when you apply for temporary credentials for a user with federated identity. |
| durationSeconds | Validity | The validity period set for the temporary credentials you apply for. |
| credentials | Credentials| The credentials obtained via STS. |

### 2. API Quick Start

The STS APIs allow you to apply for temporary credentials with custom period of validity and access permissions.
- The API "Get Temporary Credentials for User with Federated Identity" is used to issue credentials with custom period of validity and access permissions to a user with federated identity (a user managed by your local account system).
- The API "Apply for Temporary Credentials for Role" is used to get temporary credentials for the role that can be assumed by the user.

