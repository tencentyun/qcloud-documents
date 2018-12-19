CDN has been connected to the new version of Cloud Resource Access Management system, which divides all the CDN operations based on different feature attributes. The permissions for each feature involve **Console Operation** and **Cloud API Operation**. The creator can configure a feature (or multiple features) and what are allowed to be operated for the feature (project/domain) for sub-users as required.

**Note**: The old collaborator cannot generate key pair to call the API operation. After this upgrade, any sub-user can use his or her own key pair to call the API he or she has the permission to use.

## Features for Administrators
### Creator

Creator is the owner of Tencent Cloud account and has the highest permission.

### Default Administrators
The creator can also set the following administrators by associating with **Default Policies** (For more details, refer to [Permission Policies](https://cloud.tencent.com/doc/product/228/6690)):

+ Finance Administrator
+ Super Administrator
+ Cloud Resource Administrator

Super administrator owns all the permissions of creator and can assign other sub-users, and cloud resource administrator has the permission to manage all cloud resources but cannot create other sub-users. Some features are provided only for default administrators, as shown below:

+ Use **Cloud API** [DescribeCdnHosts](https://cloud.tencent.com/doc/api/231/3937) to get details of all domains under the account;
+ Switch between projects of a domain using **Cloud API** [UpdateCdnProject](https://cloud.tencent.com/doc/api/231/3935) or in **CDN Console**;

For instructions on how to configure default administrators, refer to [Default Administrator Configuration Example](https://cloud.tencent.com/doc/product/228/6693).


### Project Administrator
In addition to default administrators, permission can be assigned to project administrator based on project dimension. Project administrator can manage all cloud resources in specified project.

Project administrator can be assigned by using the policy with a service type of **Project Management** in **Custom Policies**. The policy has two features:

+ Manage could resources in CDN projects
+ Manage could resources in other projects

The permission of project administrator is equivalent to that of the old **Project Collaborator**, which allows allocation of resources in the Console among the projects covered by the permission.

Since the division of projects is applicable to all cloud resources, you can select the business scope of project management as required. For instructions on how to make the configuration, refer to [Project Administrator Configuration Example](https://cloud.tencent.com/doc/product/ 228/6693) 


## Features for Sub-users

### Querying consumption and statistics

#### Note:
+ The permission to query consumption and statistics can only be assigned by **Project** currently;
+ It is impossible for a user who only has **default project** to make a division with a finer granularity when assigning the permission to query consumption and statistic to sub-users.

#### Console Permission Control
This feature enables sub-users to query the consumption and statistics data of one or more specified projects. The sub-users with this permission can perform the following operations in the Console:

![](https://mc.qcloudimg.com/static/img/2eaa53e3a644a26de5bc6b685c7ebd95/1.png)

+ CDN Console - Overview Page: Display the overview of one or more specified projects;
+ CDN Console - Statistics Analysis - Usage Statistics: Query and download consumption details of one or more specified projects;
+ CDN Console - Statistics Analysis - Access Statistics: Query and download access details of one or more specified projects;
+ CDN Console - Statistics Analysis - Status Code Statistics: Query and download status code statistics details of one or more specified projects;

#### Cloud API Permission Control
The sub-users with this permission can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://cloud.tencent.com/doc/api/231/1725#1.-.E7.94.B3.E8.AF.B7.E5.AE.89.E5.85.A8.E5.87.AD.E8.AF.81)) and use the key to call the following Cloud APIs to query the consumption and statistics data of one or more specified projects:
+ [DescribeCdnHostInfo](https://cloud.tencent.com/doc/api/231/3941): Query CDN consumption statistics
+ [DescribeCdnHostDetailedInfo](https://cloud.tencent.com/doc/api/231/3942): Query CDN consumption statistics in details 
+ [GetCdnStatusCode](https://cloud.tencent.com/doc/api/231/3943): Query CDN error code statistics
+ [GetCdnStatTop](https://cloud.tencent.com/doc/api/231/3944): Query TOP100 ranking in CDN consumption

#### Note
+ The deleted domains in projects can still be found in the query for consumption due to the presence of history.

### Viewing Domain Details
#### Note:
+ The permission to query domain details can only be assigned by **Project** currently;
+ It is impossible for a user who only has **default project** to make a division with a finer granularity when assigning the permission to view domain details to sub-users.

#### Console Permission Control

This feature enables sub-users to query the domain information of one or more specified projects (including their configuration details). The sub-users with this permission can perform the following operations in the Console:

![](https://mc.qcloudimg.com/static/img/4bd216b6f87d5841ace57eb8b0a8bd58/2.png)

+ CDN Console - Domain Management: View the domain information of one or more specified projects, and click "Management" to view more configuration details;


#### Cloud API Permission Control
The sub-users with this feature can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://intl.cloud.tencent.com/document/product/228/9261) and use the key to call the following Cloud APIs to query the domain details (the domain must belong to a project covered by the permission):

+ [GetHostInfoByHost](https://cloud.tencent.com/doc/api/231/3938): Query the domain and configuration details based on domain name
+ [GetHostInfoById](https://cloud.tencent.com/doc/api/231/3939): Query the domain and configuration details based on domain ID


### Querying Log Download Links

#### Note:
+ The permission to query domain details can only be assigned by **Project** currently;
+ It is impossible for a user who only has **default project** to make a division with a finer granularity when assigning the permission to query log download links to sub-users.

#### Console Permission Control
This feature enables sub-users to query the log download links on specified date of one or more specified projects. The sub-accounts with this permission can perform the following operations in the Console:

![](https://mc.qcloudimg.com/static/img/e1e3372ab5d24ca1a76cd5cfb744eae1/3.png)

+ CDN Console - Logs: Query the log download links of domains in one or more specified projects

#### Cloud API Permission Control
The sub-users with this feature can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://intl.cloud.tencent.com/document/product/228/9261) and use the key to call the following Cloud APIs to query the log download links (the domain must belong to a project covered by the permission):

### Adding Domain
#### Note:
+ The permission to add domain only be assigned by **Project** currently, that is, the project to which a domain is allowed to be added can be specified;
+ It is impossible for a user who only has **default project** to make a division with a finer granularity when assigning the permission to add domain to sub-users.

#### Console Permission Control

This feature enables sub-users to add domain to one or more specified projects. The following operations can be performed in the Console:

![](https://mc.qcloudimg.com/static/img/f140a611512ad738b053ff2757455acd/4.png)

![](https://mc.qcloudimg.com/static/img/71ed3a35de5e2cfb0aa3dc51cd1e054c/5.png)

+ CDN Console - Domain Management - Add Domain: In Step 1 page of Add Domain, the projects shown in "Project" drop-down box are the ones to which a domain is allowed to be added. If no project exists, it means the sub-user has no permission to add domain and thus cannot perform further operations.

#### Cloud API Permission Control
The sub-users with this feature can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://intl.cloud.tencent.com/document/product/228/9261) and use the key to call the following Cloud APIs to add domain (the project must be covered by the permission):

+ [AddCdnHost](https://cloud.tencent.com/doc/api/231/1406): Add domain


### Making Domain Online/Offline
#### Note:
+ The permission to make a domain online/offline can only be assigned by **Project** currently.

#### Console Permission Control

This feature enables sub-users to make one or more specified projects online/offline. The following operations can be performed in the Console:

![](https://mc.qcloudimg.com/static/img/73e47117cd61959c0dc06396a2f31c66/6.png)

+ CDN Console - Domain Management: Find a domain covered by the permission for going online/offline (activated/closed).

#### Cloud API Permission Control
The sub-users with this feature can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://intl.cloud.tencent.com/document/product/228/9261) and use the key to call the following Cloud APIs to make a domain online or offline (the domain must be covered by the permission):

+ [OnlineHost](https://cloud.tencent.com/doc/api/231/1402): Make a CDN domain online
+ [OfflineHost](https://cloud.tencent.com/doc/api/231/1403): Make a CDN domain offline

### Domain Configuration Management
#### Note:
+ The permission for domain configuration management can only be assigned by **Project** currently.

#### Console Permission Control
This feature enables sub-users to manage domain configurations for one or more specified projects. The following operations can be performed in the Console:

![](https://mc.qcloudimg.com/static/img/c4fe35f70c4a901dc52d4010c9e81829/7.png)

+ CDN Console - Domain Management: Click "Manage" to edit the basic and advanced configurations for the domains for which you have permission;

#### Cloud API Permission Control
The sub-users with this feature can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://intl.cloud.tencent.com/document/product/228/9261) and use the key to call the following Cloud APIs for domain configuration management (the specified domain must be covered by the permission):

+ [UpdateCdnConfig](https://cloud.tencent.com/doc/api/231/3933): Modify domain configuration
+ [UpdateCache](https://cloud.tencent.com/doc/api/231/3934): Modify the settings of domain caching rules
+ [UpdateCdnHost](https://cloud.tencent.com/doc/api/231/1397): Modify the settings of domain origin server

### Delete Domain
#### Note:
+ The permission to delete domain only be assigned by **Project** currently;
+ The domain to be deleted should have a status of "Closed". If not, it needs to be closed.

####  Console Permission Control
This feature enables sub-users to delete domains in one or more specified projects. The following operation can be performed in the Console:

![](https://mc.qcloudimg.com/static/img/8c4fc166efdb3ba932654eb01db663d3/8.png)

+ CDN Console - Domain management: Right click a closed domain for which you have permission to delete it;

#### Cloud API Permission Control
The sub-users with this feature can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://intl.cloud.tencent.com/document/product/228/9261) and use the key to call the following Cloud APIs for domain deletion (the specified domain must be covered by the permission and has a status of "Closed"):

+ [DeleteCdnHost](https://cloud.tencent.com/doc/api/231/1396): Delete CDN domain

### Refresh and Prefetch
#### Note:
+ The permission for refresh and prefetch only be assigned by **Project** currently;
+ The domains in submitted URL List or Directory List must be covered by the permission.

#### Console Permission Control
This feature enables sub-users to perform refresh and prefetch operations on URLs or directories of domains in one or more specified projects. The operation performed in the Console is shown below:

![](https://mc.qcloudimg.com/static/img/31438f0de7b10401a15f98b9e0c265ce/9.png)

+ CDN Console - Purge Cache: Paste URLs or directories under the domain for which you have permission in batch to the text box, and submit them for refresh.

#### Cloud API Permission Control
The sub-users with this feature can apply for a Cloud API Key (for more information, refer to [Applying for Security Credential](https://intl.cloud.tencent.com/document/product/228/9261) and use the key to call the following Cloud APIs to perform refresh and prefetch (only the URLs and directories under the domain covered by the permission can be submitted):

+ [RefreshCdnUrl](https://cloud.tencent.com/doc/api/231/3946): Refresh URL
+ [RefreshCdnDir](https://cloud.tencent.com/doc/api/231/3947): Refresh directory

### Default Features
Once the sub-user has configured permissions for CDN features, the following operations can be performed by default **without any configuration**:

+ Use the Console to query all refresh records:
  ![](https://mc.qcloudimg.com/static/img/88fef5c20d4e32b639136348e40c24c4/10.png)
+ Use Cloud API [GetCdnRefreshLog](https://cloud.tencent.com/doc/api/231/3948) to query refresh records.

For the example of sub-user feature configuration, please refer to [Sub-user Configuration Example](https://cloud.tencent.com/doc/product/228/6693).


