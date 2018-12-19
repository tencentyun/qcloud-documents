Policy is the syntax rule used to define and describe one or more permissions. CAM supports two types of policies: preset policy and custom policy.
	
### 1. Preset policy
	
The preset policy is a collection of some common permissions created and managed by Tencent Cloud, such as SuperAdmin, resource management permissions, which has a rough granularity. These policies are not editable.
	
In the interface of preset policy, we can perform a search using service type and keyword. Here, we choose "All" in the service type and enter "ad" as keyword for search.
![](https://mc.qcloudimg.com/static/img/7ae75fbd6c63eb215f6e2ebe80073179/Policy+Management9.png)


		
### 2. Custom policy

The policy created by users, which allows you to assign permissions with a finer granularity. For example, you can associate a policy with a DBA to authorize him/her to only manage CDB instances, instead of CVM instances.
	
Custom policies are created by using three methods: policy generator, business permission and syntax.

For the policies created using policy generator, the policy syntax is generated automatically after you select the service and operation from the policy guide and define resources. With convenience and flexibility in use, these policies are preferred. The policies created using business permission are configured by users, with permission granularity being controlled during business connection, to satisfy the needs of users for less-complex permission assignment. The policies created using syntax are configured by users, with flexible permission granularity being controlled by users, to satisfy the needs of users with high requirement on fine-grained permission assignment.
	
	
### 3. Create a custom policy

#### 3.1 Create a policy using policy generator

Step 1:  Go to [policy management console](https://console.cloud.tencent.com/cam/policy), click "Create Custom Policy", and select "Policy by policy generator".

![](https://mc.qcloudimg.com/static/img/ce500aaed5718fc1ffe62fe918f1bff9/Policy+Management10.png)

Step 2:  Select desired service and operation from the list, click "Add Statement", and then click Next. For the operation of a certain service that needs to be associated with an object, "Resource Description" is required. As shown below, the operation is required to be associated with an object. You can click "Note" on the left for detailed definition and example of "Resource Description".

![](https://mc.qcloudimg.com/static/img/2557e7830e4b5f51cabff317ae8f130f/Policy+Management11.png)

If the operation of a certain service does not need to be associated with an object, "Resource Description" is not required. As shown below, the operation is not required to be associated with an object. You will find that the field of "Resource Description" is unavailable.

![](https://mc.qcloudimg.com/static/img/facf21799e4848ece262b7c5871202ca/%7B8C2DBD2B-7892-4051-BA54-21D27DC53A7A%7D.png)


We can add multiple declarations in one policy. Here, we select AboutVaultLock of Archive Storage and SmsQcloudcom of SMS.

![](https://mc.qcloudimg.com/static/img/423bb3cbfa347b621f0838ff291a87e6/Policy+Management12.png)


Step 3: Click Create Policy. The policy name is generated automatically, in which, "policygen" is prefix, and the numbers are confirmed based on the creation time. The policy content generated automatically corresponds to the service and operation selected in the previous step, to which we can make a few adjustments. For any questions, click "Policy Syntax Description" and List of "Supported Businesses" at the bottom left.

![](https://mc.qcloudimg.com/static/img/ccae55ca18615019116275f1dc91a44e/Policy+Management13.png)


#### 3.2 Create a policy using business permission

Step 1:  Go to [policy management console](https://console.cloud.tencent.com/cam/policy), click "Create Custom Policy", and select "Create by Service Permission".

![](https://mc.qcloudimg.com/static/img/c707f8db590ee708cf7d1f0fbd1d6b70/Policy+Management14.png)

Step 2:  Add a business to the policy and name it, and then click "Next".

![](https://mc.qcloudimg.com/static/img/ec389f8253c9446ff59c233c613187fb/Policy+Management15.png)

Step 3:  "Enable" permissions of some of the features, and click "Next".


![](https://mc.qcloudimg.com/static/img/dff678fe590861b61afc0c4f1f1b10ba/Policy+Management16.png)

Step 4:  If an action scope should be specified for a feature, you need to add relevant resources, and click "Save".

![](https://mc.qcloudimg.com/static/img/80b94e1f49e618c9bbd024f0f4314d86/Policy+Management17.png)

Step 5:  Policies can be found in "Policy List".

![](https://mc.qcloudimg.com/static/img/e82fea7d78bca31e05cd5e5e279f383f/Policy+Management18.png)

#### 3.3 Create a policy using policy syntax:

Step 1:  Go to [policy management console](https://console.cloud.tencent.com/cam/policy), click "Create Custom Policy", and select "Create by Policy Syntax".

![](https://mc.qcloudimg.com/static/img/15ce622a4e1de64e6e68954ef5f04d01/Policy+Management19.png)

Step 2: You can choose a template type in this step. After selecting the type, you can perform a keyword search and select one of the searched templates, and then click "Next". Here, we choose "All" in the service type and enter "a" as keyword for search, and then select the template AdministratorAccess.

![](https://mc.qcloudimg.com/static/img/086e0f468f0dd6f35a78d58654428c5e/Policy+Management20.png)

Step 3: The policy content of corresponding template will show up here. We can make some modifications to the content and then click "Create Policy". The policy name is generated automatically, in which, "policygen" is prefix, and the numbers are confirmed based on the creation time. For any questions, click "Policy Syntax Description" and "List of Supported Businesses" at the bottom left.

![](https://mc.qcloudimg.com/static/img/9d761880b36e4818dc2e74652166a690/Policy+Management21.png)
