## 1. Integration Platform 
BlueKing Integration Platform (or BlueKing PaaS) is an open platform that allows you to quickly and easily create, deploy and manage applications. It provides complete front- and back-end development frameworks, Enterprise Service Bus (ESB), scheduling engines, and public components, and helps you create supporting tools and operation systems quickly at low costs while eliminating the need for OPS.

BlueKing PaaS offers a complete set of self-help and automated services from application creation to deployment and subsequent OPS. These services include log query, monitoring and alarming, allowing you to concentrate on application development.

The following describes how to use BlueKing PaaS and the precautions for using it.

## 2. Developer Center 
Developer Center provides one-stop services from application creation to deployment and subsequent OPS. 
### 2.1	Application Creation 
#### 2.1.1	Create an Application
(1) Click **Create Application** on the left navigation bar.
(2) Enter basic registration information, such as application ID and name.
(3) Click **Create Application**. Then the system will automatically create a database for the application, initialize the codes in SVN repository and create the application.
![Developer Center](https://mc.qcloudimg.com/static/img/4faacd4a55952e6cf13860f52597d41d/1.png) 

#### 2.1.2	Check Out Code
(1) After the application is created, click **Check Out Code** to check out the application directory (the development framework is initialized to your code repository) to local for application development.
(2) You can also check out the code via the entry **Application List** -> **Click Application Name** -> **Code Management**.
(3) Your application code directory contains three subdirectories: trunk, tags, and branches. We recommend that you develop your application under trunk.
(4) Check out the code.
![Developer Center](https://mc.qcloudimg.com/static/img/704805d886e78fd88c2f146ee1d10273/2.png)  
![Developer Center](https://mc.qcloudimg.com/static/img/a7b062a28f861775cd2c050fc77bc9e6/3.png)  

### 2.2	Application Management
#### 2.2.1	Information Modification
On the information modification page, you can modify the profile, name, category, administrator, development leader, business type, and description of an application as well as page height and width.
![Developer Center](https://mc.qcloudimg.com/static/img/53884054eb444ca61ff7fae5c4c72946/4.png)  
Note: The modified page width and height take effect after you re-enable the application.

#### 2.2.2	Role Management
A BlueKing application has a creator, a developer and an administrator. Each of them has separate management permissions.

Role description:
- Creator: The person who creates an application has the highest role permissions on application management. 
- Developer: The person who develops an application can pull codes, deploy the application, and view application logs. 
- Administrator: An administrator can access any features and services except for pulling codes and deploying applications. An administrator can be a OPS or product manager.
![Developer Center](https://mc.qcloudimg.com/static/img/d2bb8a8c976d9701ddb846d5a7aab0fe/5.png) 
 
Enter the new roles' QQ accounts and use ";" to separate them.
The new application management roles and the application creator must be the collaborators of the same developer. You can view the information of the developer's collaborators in the **User Center** on BlueKing desktop.

#### 2.2.3	Variable Configuration
Sensitive variables such as external database IP and account password may be exposed if they are directly written into the code. Besides, the code needs to be pulled upon each modification and the modified variables need to be submitted for test and launched before use. To cope with such scenario, BlueKing's Developer Center provides variable configuration to help developers solve problems in variable hard-coding.

![Developer Center](https://mc.qcloudimg.com/static/img/9992458f62b5088ed29b32d07e578e8c/6.png)  
(1) Variable name must begin with `BKAPP_` and consist of uppercase/lowercase letters, numbers or underscores and should not exceed 50 characters. For example, the variable name can be set to BKAPP_TEST.
(2) Variable value must consist of uppercase/lowercase letters, numbers or underscores and should not exceed 100 characters.
(3) Environment variable obtained in the application is os.environ.get('BKAPP_TEST').
(4) After configuration is finished, the application takes effect in the environment only after the test deployment and production deployment are completed.

### 2.3	Application Deployment
#### 2.3.1	Release Deployment
BlueKing applications are automatically deployed on line by one-click. It adopts the distributed deployment mode: When a server crashes, user requests are forwarded to other servers, avoiding application exceptions while improving its stability. In addition, BlueKing applications use docker for isolation, which improves its security.

![Developer Center](https://mc.qcloudimg.com/static/img/14fe86ea5ce2fd5ec33f8ffe855e70fe/7.png)  
(1)	Test deployment
Deploy the application code in test environment, and then the application can be accessed in test environment.
For any feature updates, submit the code to SVN, and perform test deployment again.
If celery is used in the code to execute background tasks, select **Activate celery** when performing test deployment.
(2)	Production deployment
Deploy the application code in production environment, and then the application can be used on the BlueKing desktop (production environment).
(3)	Withdrawal
When the application code is withdrawn from the environment selected by the developer, users cannot access the application, but the database of this application is retained.
![Developer Center](https://mc.qcloudimg.com/static/img/c54b1232f76be54759adf794284382e0/8.png)  

#### 2.3.2	Release History
Each submission for test, launch and withdrawal are recorded. Users can view the details in **Release History** -> **Release Records**.
![Developer Center](https://mc.qcloudimg.com/static/img/79217a75cbe6f9434a61b2d924cc82b3/9.png)  

#### 2.3.3	Service Status
An application generally uses a number of services (such as MySQL and UWSGI) on the BlueKing platform. The statuses of the services are displayed in **Application Deployment** -> **Service Status**.
The production and test environments of BlueKing applications as well as the applied services are mutually independent. The status of these services in either environment can be viewed only when the test deployment and production deployment are performed.

![Developer Center](https://mc.qcloudimg.com/static/img/8c54b6efd37c7ce04f437be98e4a7d69/10.png)  
To view the status of celery and celery_beat, user must select **Activate celery** and **Activate Periodic Task** when performing test deployment and production deployment.
![Developer Center](https://mc.qcloudimg.com/static/img/5617dc4b9c523d913000f77a922c87a3/11.png)  
### 2.4	Code Management
#### 2.4.1 Code Checkout
After the developer creates an application, a code is initialized in the application directory according to the selected application development framework/sample. The developer conducts secondary development based on such code. The SVN address of the application code can be queried in **Code Checkout**. The code checkout address is `https://svn.o.qcloud.com/{Cloud service account}/{Application ID}`, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/d8a70575d2cabe4d27e506822e288f45/12.png)  
The account is your QQ account. If you forget the password, click on the Forgot Password link, and then a 6-digit random verification code will be sent to your mobile phone, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/3857fdfc9a2e31c507431767e54a2eb1/13.png)   
Enter the verification code, and then the generated password will be sent to your mobile phone, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/f8b2c656531e0a79a3d9d79d5b039dba/14.png)   
#### 2.4.2	Code Permission Management
Code permission management means managing the read/write permission of SVN codes. Developers can add or delete the permission information of some accounts on the permission management page. The minimum granularity managed by the code permission management is a permission under a single account. After you add a permission, you can view and submit codes under any directory of the current application (including the release directory) in the account.
![Developer Center](https://mc.qcloudimg.com/static/img/7cb99b49d9a83f8f50fa385879f1f0ad/15.png)  

![Developer Center](https://mc.qcloudimg.com/static/img/55cf19877485ef00a6313d38f1abeba4/16.png)   
 
Notes:
1. After a developer is added to **Application Management** -> **Role**, the system automatically adds the developer to the developer group, and activate application code permission for the developer at the same time.
2. The added developer must be a collaborator. The collaborator can be a collaborator of Tencent Cloud or a custom collaborator. You can query the custom collaborator in **User Center** on the BlueKing desktop.

#### 2.4.3	Record Submission
BlueKing PaaS records the details of each submission of SVN codes. You can view the submission time, modified files and submitter's information in **Submission Records**.
![Developer Center](https://mc.qcloudimg.com/static/img/a4d698ddc9abe835b64c714d4de3246b/17.png)   
#### 2.4.4	View Online
BlueKing PaaS supports viewing files, directories, and diff (comparing difference) for application codes on line. The file/folder name, the final version number, the final modification time and submitter are displayed on the right, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/b4f6e88952bbb654f4157d1c1608dc2e/18.png)   

Click a file to view the source code of the file, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/8e691280b520f34e3e9dee2a8a7fade3/19.png)  
 
Click **diff** to view the differences between the current file and the last file, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/70eed752a88cf2a886655d3914e6e818/20.png)   
### 2.5	Database
BlueKing equips every application with two independent databases (test database and public database) and highly available solutions to ensure data reliability. Besides, this platform supports almost all the features of MySQL.
#### 2.5.1	Django admin
BlueKing applications adopt the Django framework, a web-based database management tool. After the data model is registered to the admin.py file, you can add, delete, change and query the data on the page.
![Developer Center](https://mc.qcloudimg.com/static/img/eec88a4fd4c6b3c95bdd9313886d1025/21.png)  

![Developer Center](https://mc.qcloudimg.com/static/img/9665b69da181a07816b426f3c000e768/22.png)   
 
For more information about how to use Django admin, please see the [official website](https://docs.djangoproject.com/en/1.8/ref/contrib/admin/).
#### 2.5.2	Online Operation
BlueKing applications directly integrate the database backend management services of the Django framework. Developers can manage databases in the test and production environments on the page separately.
![Developer Center](https://mc.qcloudimg.com/static/img/2674ca0f7dc4b57f5dcebd4d4b01f3e4/23.png)   
### 2.6	Logs
BlueKing PaaS provides online log services. Developers can view an application's log information (including general log, component call, UWSGI, CELERY, NGINX, and Gunicorn) through **Service **-> **Log Query** or filtering by environment, log level or time.
![Developer Center](https://mc.qcloudimg.com/static/img/736ea496805f2ee541e866b65bc57642/24.png)   
- uWSGI/Nginx/Gunicorn are system logs. During deployment, logs are exported to a specific directory and developers cannot define its contents.
- General Log/Component Call/Celery are the logger-exported logs in the development framework, whose contents can be defined by developers.

After a log is generated, it is captured and resolved by the agent process, and then imported into the log query engine. This log can be found on BlueKing PaaS.
![Developer Center](https://mc.qcloudimg.com/static/img/1987440855f0fc439b1ba852cb6acd93/25.png)   
- Time: The default is last 1 hour. The available values include last 1 hour, 12 hours,1 day,7 days, and 14 days. Logs within 30 days can be viewed.
- Environment: The default is all environments. The available values include test environment and production environment.
- Type: The default is general Log. The available values include general log, component call, uWSGI, Celery, Nginx, and Gunicorn.
- Log level: General log, component call, and celery are marked with five levels, that is, DEBUG, INFO, WARNNING, ERROR, and CRITICAL. uWSGI, Nginx, and Guniorn are HTTP status codes.
- Information: You can enter keywords to search for desired information.

A log can be queried about 5s after it is generated.
### 2.7	Monitoring and Alarming
In addition to log viewing provided by BlueKing PaaS for developers to view the application log records, a real-time alarm pushing service is also needed to help developers find potential problems in the application at the first time and improve users' experience. That's how the log monitoring and alarming service come into being. With this service, developers configure alarm parameters, alarm recipients and other information by themselves and the platform monitors the log in real time. Once the required rules are met, the platform pushes alarm information to developers.
After the application is registered, the alarming service is activated by default, and it is strongly recommended not to deactivate this service manually for important applications.
![Developer Center](https://mc.qcloudimg.com/static/img/633173e0b0a57a057b2c981727e7c17f/26.png)   
![Developer Center](https://mc.qcloudimg.com/static/img/199ac0393cda65ff1aa29f92561d536f/27.png)   
This service can be deactivated after activation. It is recommended not to deactivate the service. Otherwise, recipients cannot receive any alarms.
#### 2.7.1	Alarm Configuration
After this service is activated, you can configure alarm recipients, alarm reception types and specific alarm parameter types.
![Developer Center](https://mc.qcloudimg.com/static/img/10311f52fd3ac8268c616e273ba7b581/28.png)   
- Alarm reception: Enter the recipient's QQ and select the desired type of alarm to receive. The system sends alarms to the recipient by email. The default recipient is the application developer.
- General alarm: Monitor developers' code debugging logs and send alarms. Log level and keyword-associated items can be configured. It is recommended for developers to adjust debugging logs to INFO level and exceptional logs to ERROR level to avoid unnecessary interference.
- HTTP alarm: Monitor the application's UWSGI logs and send alarms. Request error codes and slow request can be configured.
- Component alarm: Monitor the application's component call logs and send alarms. Log level can be configured.
- Celery alarm: Monitor the application' celery logs and send alarms. Logs level and keyword-associated items can be configured. This alarm is only applicable to applications with celery activated.

####	2.7.2 Alarm Statistics
The monitoring and alarming service also provides alarm statistics for developers to manage the stability of applications and optimize them accordingly. Alarm statistics displays the number of alarms on the current day and the trend of the number of alarms in a specified period by time and alarm type.
![Developer Center](https://mc.qcloudimg.com/static/img/f2a0f37b3276176e4ce10b42afa76ce2/29.png)   
### 2.8	Data Statistics
Application data is most concerned by application product managers and operators. BlueKing uses number of visits, online duration and activity level to display the usage of the application in an all-around way.
#### 2.8.1	Number of Visits
It refers to how many times an application is opened on the BlueKing desktop and in the application market. Number of visits can be queried by time or user.
![Developer Center](https://mc.qcloudimg.com/static/img/287efd1a9c58b35df311e990a7725377/30.png)  
#### 2.8.2 Online Duration
It refers to how much time users spend on the application page. Online duration can be queried by time or user.
![Developer Center](https://mc.qcloudimg.com/static/img/8fe943881b2e94a3d42a609bfa8df9ff/31.png)   
#### 2.8.3	Activity Level
It refers to the number of clicks (on links and buttons) made by users on the application page. Number of clicks can be queried by time or user.
![Developer Center](https://mc.qcloudimg.com/static/img/b931d852dda07fbc6febe0db2b776443/32.png)   
#### 2.8.4	Real-time Statistics of Container Resource
This service monitors and collects data on memory and CPU occupied by the application's docker container in real time to help users learn the application's CPU and memory usage.
![Developer Center](https://mc.qcloudimg.com/static/img/f8887ab70a7dd5d0f8057a86f74058a6/33.png)   
## 2.9.	Access Control
BlueKing applications are private applications by default and can only be accessed by the developers and their collaborators. After test deployment and production deployment are performed on an application, other people cannot access the application. The developer can grant users the access permission by adding them as collaborators.
![Developer Center](https://mc.qcloudimg.com/static/img/a506d0532b50afca7d5a45c801391549/34.png)  
 
If a user is not added to the whitelist, when the user tries to access the application, a prompt of no permission appears.
![Developer Center](https://mc.qcloudimg.com/static/img/5e1eeb3a4e6810a47c89dfc69d43adc8/35.png) 
  
In such case, developers need to add the user's QQ account as a collaborator by clicking **BlueKing Desktop** -> **User Center** -> **Add Collaborator**, refresh collaborators, and then the user can access the application.
![Developer Center](https://mc.qcloudimg.com/static/img/159d9379f5ab8322080e89287b8e502e/36.png)   

### 2.10	Permission Management
A common feature used by the BlueKing developers when developing applications is user permission management, including user permission configuration and application. However, as OpenID authentication is adopted during login, the QQ account of the user trying to log in is unknown to the application developer. Therefore, the platform provides the permission management service for applications. The features of BlueKing's uniform permission management service are as follows:
- Permission configuration, including configuration of permission features, reviewers, individual user permissions, and super users.
- Permission application
- Permission renewal
- Permission review

#### 2.10.1	Permission Configuration
Permission configuration includes feature registration, code development and other configurations.
(1) Permission feature registration
Enter the name (required), code (required), and description (optional) of the feature, and then save them to complete the feature registration.
![Developer Center](https://mc.qcloudimg.com/static/img/ee406ad62b91d49ff38456b3890eec95/37.png) 
(2) Use a decorator in an application to manage permissions
bk_check_auth is a uniform decorator in the permission system and is integrated into the development framework.
	a. Parameter (func_code): It receives the application's feature code registered with the Developer Center.
	b. ENABLE_BK_AUTH: It is used to enable/disable the uniform permission decorator. To enable it, set ENABLE_BK_AUTH to True in config/settings_custom.py.
The following is an example for how to use the decorator:
![Developer Center](https://mc.qcloudimg.com/static/img/5ab74dcc746e939b4d4e1b42ee861329/38.png) 
look_index is the feature code registered with Developer Center.
If a user is not authorized with such permission, a page indicating no permission appears. The user can click **Apply for Permissions** or **View My Permissions**, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/8aa10a16d18d1804caa8504de1fad457/39.png)  
(3). (Optional) Configuration of reviewers, individual user permissions, and super users
In addition to quick access, special roles and permission configurations are also provided to reduce developers' workload and meet special needs. Three special configurations are as follows:
a. Reviewer configuration
Reviewer is a special role. An application can be reviewed by its developers or reviewers. You can configure multiple reviewers in the Developer Center.
![Developer Center](https://mc.qcloudimg.com/static/img/6eca38eee610492a81a1e13e8530ab05/40.png)  
b. Configuration of individual user permissions
Developers or application administrators can grant users certain permissions in advance, without waiting for users to apply for such permissions after they are restricted.
![Developer Center](https://mc.qcloudimg.com/static/img/c37a15f156cd5869a1626e505a583cb7/41.png)  
![Developer Center](https://mc.qcloudimg.com/static/img/26bb42e766fd68c358f502fe1e7e6939/42.png)  
c. Super user configuration
Developers or application administrators can set some special users as super users, so that they can directly access or enable the application without any permission restrictions.
Super users have all the permissions under the uniform permission management and do not need to apply for any permissions.
![Developer Center](https://mc.qcloudimg.com/static/img/8a50844446fc3eee6a1e8168f7b3a01b/43.png)  

#### 2.10.2	Permission Application
[Entry Link](http://o.qcloud.com/console/?app=permission_center): http://o.qcloud.com/console/?app=permission_center
![Developer Center](https://mc.qcloudimg.com/static/img/ebb1a59b4d0de81fab05f2b5c5f8091c/45.png)  
To apply for a permission, select the application and desired feature, enter the application reason, and then submit it.
Note: Your application reason determines how fast your application is reviewed. Enter the real application reason to avoid rejection.
![Developer Center](https://mc.qcloudimg.com/static/img/bcbb4b501408d3eae588bb1aa48c90ee/46.png)  
#### 2.10.3	Permission Renewal
A permission is valid in 60 days upon application. After that, the permission cannot be used. User need to manually renew it or the developer renews it for users.
(1) Users manually apply for renewal
![Developer Center](https://mc.qcloudimg.com/static/img/d356545c9864e2ff790a6b909c4f9498/47.png)  
To apply for renewal, select a renewal period (60 days by default), enter the renewal reason, and then click **OK**.
Note: Your renewal reason determines how fast your renewal is reviewed. Enter the real renewal reason to avoid rejection.
![Developer Center](https://mc.qcloudimg.com/static/img/1c9cd81ba1a1d2cb9985bad3597d8083/48.png)  
(2). Developers renew permissions for users (in the Developer Center) as shown below
![Developer Center](https://mc.qcloudimg.com/static/img/1f708eab451286eb444f85880dc76c39/49.png) 
![Developer Center](https://mc.qcloudimg.com/static/img/3e1375361563d1c6c6dd12f478138fe2/50.png)  

#### 2.10.4	Permission Review
Permission review is the last step of the uniform permission management service. This task can be done by either application developers or reviewers. For how to configure reviewers, please see the aforesaid example. Both application developers and reviewers can review single or multiple applications. After the review is completed, the result is notified to the user by email. As it is to review user permission applications, developers or reviewers need to handle the application documents based on application reasons, application UIN, features, etc.
(1) Developers review applications (in the Developer Center)
Application developers can review permission application for all features. After the application documents are reviewed, developers can check the review records under "Reviewed".
![Developer Center](https://mc.qcloudimg.com/static/img/3d928844c8b91462ce69afc62c4d6091/51.png)  
(2) Reviewers review applications (on BlueKing desktop)
Reviewers are configured in the uniform permission management service, as described in step 3.
The task of a reviewer is to review the application for feature permissions.
The review entry is in the uniform permission management App on the BlueKing desktop. Entry link: http://o.qcloud.com/console/?app=permission_center.
![Developer Center](https://mc.qcloudimg.com/static/img/4c9f1579e05d173c6ac9c658eef0fd3d/52.png)  

### 2.11	Component Permission Application
BlueKing applications call APIs of other systems (such as CC and WEIXIN ) using BlueKing component APIs. The applications do not have the permissions of any component by default. You need to apply for component permissions on BlueKing PaaS.
![Developer Center](https://mc.qcloudimg.com/static/img/2c7f132398097c46d41d50bd372996b3/61.png) 
Click the API name to view the API description.
![Developer Center](https://mc.qcloudimg.com/static/img/45b7bb1f3e0fe294ed6ce0f840027c04/62.png)  
Component permissions include general permissions and sensitive permissions. General permissions are generally APIs for query, while sensitive permissions are APIs for creation and operation. These permissions need to be applied for separately, as shown below:
![Developer Center](https://mc.qcloudimg.com/static/img/43755b9d6b1cf9454042ae6f80a2a763/63.png)  
Applications are reviewed by the ESB team. Components can be used upon approval of applications.
![Developer Center](https://mc.qcloudimg.com/static/img/3bbea65549ec00ce15290957553b4bfb/64.png)  
[Component Documentation](http://o.qcloud.com/esb/docs/qcloud/): http://o.qcloud.com/esb/docs/qcloud/

### 2.12	Notifications and Announcements
BlueKing designs and implements a Node.js-based notification push service that allows easy connection with BlueKing subsystems and applications as well as third-party systems. The service is featured with real-time message pushing, custom display of notifications and message, and third-party system accessing.
![Developer Center](https://mc.qcloudimg.com/static/img/defde4a0a751bc1bc0297a91b1ed64ac/65.png)  

#### 2.12.1	Release Announcements
Entry: **Application List** (click on the application name) -> **Services** -> **Notifications and Announcements**. Click **Save** to save the announcement, and then the platform pushes this announcement to the application's web page from the start time to the end time of announcement display as specified by the user.
![Developer Center](https://mc.qcloudimg.com/static/img/fe4baf35f42f79bed0b3c81c6e75d701/66.png)  

#### 2.12.2	View Announcements
The BlueKing application development framework has access to APIs for all announcements and messages read by users. Users can directly view all the historical announcements in the application.
![Developer Center](https://mc.qcloudimg.com/static/img/6f1e6051f8723bd1912fea976fadd613/67.png)  
 
## 3	Backend Development Framework
Applications developed on BlueKing PaaS can be developed for the second time using the BlueKing backend development framework, which is created with Python, Django, Mako, Html, JavaScript, CSS and other technologies based on the Django framework.

### 3.1	Login Authentication Module
The BlueKing application development framework integrates the uniform BlueKing login authentication module and shares the same user information and authentication system with BlueKing PaaS.
![Developer Center](https://mc.qcloudimg.com/static/img/ea9d319ceb7801c4cc1730043428c3c1/71.png)  
BlueKing PaaS applications adopt the OpenID authentication mechanism.
OpenID is an open account designed for QQ accounts. It allows users to access third party businesses using QQ accounts while not disclosing them to the third party companies. OpenID provides a safe way to use QQ accounts in public.

	(1) The application uses independent domains such as APPID.qcloudapps.com and APPID.test.qcloudapps.com.
	(2) The application joins Tencent Connection as a third-party application. After a user logs in to the application, the openID and openkey are obtained.
	(3) The application verifies the user's identity by the openid and openkey.
Note: As OpenID authentication is adopted for login, the QQ account of the user trying to log in is unknown to the application developer. Therefore, the platform provides the permission management service.

### 3.2	Feature Enabling Module
This module allows developers to enable features as needed and perform Beta test during application development and iteration.
Developers need to add feature information to the table of app_control_function_controller and use decorators. The sample code is as follows:

![Developer Center](https://mc.qcloudimg.com/static/img/b8e10fb424617d59e560a2105d727be4/72.png)  
Feature example:

![Developer Center](https://mc.qcloudimg.com/static/img/dd3b88e67510cdcfbfd5a83507d85fe6/73.png)  

### 3.3	WEB Security Protection Module
The WEB security protection module is featured with anti-csrf attacks and anti-xss attacks.
- Anti-csrf attack: It uses the csrf module provided by django and is integrated into the development framework, so users do not need to make other settings.
Note: If csrf validation needs to be disabled for some requests, add csrf_exempt decorator in the view function.
- Anti-xss attack: The middleware of the anti-xss attack is integrated into the development framework, so all request parameters as special characters are escaped. Rich text contents and URLs are processed with special methods.

### 3.4	Component Module
The component module encapsulates all the APIs into an SDK and integrates the SDK into the development framework, so that users can directly call it in the application. Download URL: https://o.qcloud.com/esb/sdk_resource/esb/
#### 3.4.1	SDK Installation
When you develop in the local, use the following command to install the SDK locally.
pip install http://paas-10032816.cos.myqcloud.com/blueking.component.qcloud-0.1.1.tar.gz
Meanwhile, check whether the SDK package and version number in the requirements.txt file are correct.
If the SDK package is not entered in the requirement.txt file or the version number is wrong, the application cannot be accessed after the test/production deployment.

![Developer Center](https://mc.qcloudimg.com/static/img/9342f7ef898b054535a4d4ea194fe70e/74.png)  
#### 3.4.2	SDK Instructions
The SDK can be used by shortcuts or ComponentClient. For how to use it, please see:
https://o.qcloud.com/esb/sdk_resource/esb/
## 4 Frontend Services
BlueKing MagicBox is a frontend resource integration platform that provides developers with abundant frontend resources, including common UI components, JS plug-ins and basic templates. With BlueKing MagicBox, developers can quickly create pages. In addition, it also offers complete sample packages for selection. Developers can drag desired components to assemble pages and visualize the frontend layout.
### 4.1	Frontend Component Set
The frontend component set includes a variety of navigations and icons, functional tables and sheets, easy-to-use drop-down boxes and popups, etc. Developers can look up the desired component on line, copy codes and use the component. Developers can also preview components to learn their effects, and then select the appropriate one.
![Developer Center](https://mc.qcloudimg.com/static/img/6f65c059dcdff7666576c733a5464ce6/81.png)  
Developers can look up components on line, preview their effects, and even copy source codes of the components on line.
![Developer Center](https://mc.qcloudimg.com/static/img/48c90c30a4174ed28059c8e6929ae282/82.png)  
Each component is accompanied with a detailed user guide, including dependent files, usage, and parameter configuration instructions.
![Developer Center](https://mc.qcloudimg.com/static/img/ea9ceed33d76a631513b0e155acb42e9/83.png)  
### 4.2	Package Sample Set
The package sample set includes a number of samples, including the basic Bootstrap style, response-type style and mobile version. Developers can preview the sample effects on line, and download the desired one.
![Developer Center](https://mc.qcloudimg.com/static/img/190a310007e55fad7a91a5b4b2051e6a/84.png)  
### 4.3	Visualized Layout
Developers can drag components provided by BlueKing MagicBox on line to assemble pages. Besides, pages can be edited, saved, previewed and downloaded on line.
(1) Look up the desired component
![Developer Center](https://mc.qcloudimg.com/static/img/3280ed465712c6e9b08f520f6466a6b9/85.png) 
(2) Drag the component to the canvas
![Developer Center](https://mc.qcloudimg.com/static/img/72d09f6d70d58e561b538b701bbabd4e/86.png)  
(3) Preview, save or download
![Developer Center](https://mc.qcloudimg.com/static/img/fe3498ef6165b7a9fcaaa97a5f555ea1/87.png)  




