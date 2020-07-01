
Policy is the syntax rule used to define and describe one or more permissions. CAM supports two types of policies: preset policy and custom policy.
	
### 1. Preset policy
	
The preset policy is a collection of some common permissions created and managed by Tencent Cloud, such as SuperAdmin, resource management permissions, which has a rough granularity. These policies are not editable.
	
In the interface of preset policy, we can perform a search using service type and keyword. Here, we choose "All" in the service type and enter "ad" as keyword for search.
![](https://mc.qcloudimg.com/static/img/ce01bc4bdeaff2f2d701b9b1df66a2f6/image.jpg)


		
### 2. Custom policy

The policy created by users, which allows you to assign permissions with a finer granularity. For example, you can associate a policy with a DBA to authorize him/her to only manage CDB instances, instead of CVM instances.
	
Custom policies are created by using three methods: policy generator, business permission and syntax.

For the policies created using policy generator, the policy syntax is generated automatically after you select the service and operation from the policy guide and define resources. With convenience and flexibility in use, these policies are preferred. The policies created using business permission are configured by users, with permission granularity being controlled during business connection, to satisfy the needs of users for less-complex permission assignment. The policies created using syntax are configured by users, with flexible permission granularity being controlled by users, to satisfy the needs of users with high requirement on fine-grained permission assignment.
	
	
### 3. Create a custom policy

#### 3.1 Create a policy using policy generator

Step 1:  Go to policy management console, click "Create Custom Policy", and select "Policy Generator".

![](https://mc.qcloudimg.com/static/img/a28aa332634c323e6a038f455801a26b/1009.jpg)

Step 2:  Select desired service and operation from the list, click "Add Declaration", and then click Next. For the operation of a certain service that needs to be associated with an object, "Resource Description" is required. As shown below, the operation is required to be associated with an object. You can click "Note" on the left for detailed definition and example of "Resource Description".

![](https://mc.qcloudimg.com/static/img/fbce91eea2f7f14e432a42768f14f589/1011.jpg)

If the operation of a certain service does not need to be associated with an object, "Resource Description" is not required. As shown below, the operation is not required to be associated with an object. You will find that the field of "Resource Description" is unavailable.

![](https://mc.qcloudimg.com/static/img/f8b2fbfafe654ef5e93f2fb88ee8b01b/image.jpg)


We can add multiple declarations in one policy. Here, we select AboutVaultLock of Archive Storage and SmsQcloudcom of SMS.

![](https://mc.qcloudimg.com/static/img/a91d0db5117f6fcfcf2ea378c8fae5b0/image.jpg)


Step 3: Click Create Policy. The policy name is generated automatically, in which, "policygen" is prefix, and the numbers are confirmed based on the creation time. The policy content generated automatically corresponds to the service and operation selected in the previous step, to which we can make a few adjustments. For any questions, click "Policy Syntax Description" and List of "Supported Businesses" at the bottom left.

![](https://mc.qcloudimg.com/static/img/1dda08bff5595ff4809ce4bdd40e5dc0/1013.jpg)


#### 3.2 Create a policy using business permission

Step 1:  Go to policy management console, click "Create Custom Policy", and select "Business Permission".

![](https://mc.qcloudimg.com/static/img/39d208e0f038df3ea6bf4cf4e9c04c9a/s1.jpg)

Step 2:  Add a business to the policy and name it, and then click "Next".

![](https://mc.qcloudimg.com/static/img/2607689ca9fdc075493e53fcb870e43a/s2.jpg)

Step 3:  "Enable" permissions of some of the features, and click "Next".


![](https://mc.qcloudimg.com/static/img/04ab076bb4d78b5423c5210f91bfe796/s3.jpg)

Step 4:  If an action scope should be specified for a feature, you need to add relevant resources, and click "Save".

![](https://mc.qcloudimg.com/static/img/57653ba1c762fc2143466a93b6daaa6b/p4.jpg)

Step 5:  Policies can be found in "Policy List".

![](https://mc.qcloudimg.com/static/img/250d4a1790e2957ec9edaa3e00dcabae/p5.jpg)

#### 3.3 Create a policy using policy syntax:

Step 1:  Go to policy management console, click "Create Custom Policy", and select "Policy Syntax".

![](https://mc.qcloudimg.com/static/img/16b3c63209ba7237ea45221c63cd53fa/p1.jpg)

Step 2: You can choose a template type in this step. After selecting the type, you can perform a keyword search and select one of the searched templates, and then click "Next". Here, we choose "All" in the service type and enter "a" as keyword for search, and then select the template AdministratorAccess.

![](https://mc.qcloudimg.com/static/img/aeeefc2a76ba162dc0d3f9c60e085436/p2.jpg)

Step 3: The policy content of corresponding template will show up here. We can make some modifications to the content and then click "Create Policy". The policy name is generated automatically, in which, "policygen" is prefix, and the numbers are confirmed based on the creation time. For any questions, click "Policy Syntax Description" and "List of Supported Businesses" at the bottom left.

![](https://mc.qcloudimg.com/static/img/059282dcae3c1a16d0b324ff326685a4/p3.png)








