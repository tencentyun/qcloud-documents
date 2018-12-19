In Tencent Cloud CMQ, the permission management and control is implemented using CAM. The specific procedure is as follows:


# Ⅰ. Creating a User



### 1. Access Entry
Please visit the [Users and Permissions Console](https://console.cloud.tencent.com/cam)
![](//mccdn.qcloud.com/static/img/bc95b9e687ddb4c8eba5481f04af3e7a/image.png)

### 2. Function of User Management
You can add employees who need to manage the cloud resources in account (using QQ account for login credential) as sub-users of your account, and you can associate the appropriate policy for the sub-users to assign different permissions.

![](//mccdn.qcloud.com/static/img/10728645b9bf6e48b3c1f61e6d3caa28/image.png)
> Sub-users are like company employees.

![](//mccdn.qcloud.com/static/img/104e9ca6e0e22db0efe4795adbae9f5b/image.png)
> "User Management" is similar to the process that the C-level manages the employees in the organizational structure.

### 3. How to Create a Sub-user
Step1: Visit the [Users and Permissions Console](https://console.cloud.tencent.com/cam) and click "Create user"

Step2: If you need to log in to Tencent Cloud console or call Cloud APIs, select "Allow login to Tencent Cloud", and fill in "QQ Number" as login credential
![](//mccdn.qcloud.com/static/img/717db35eae2332917a152eb69e8b4339/image.png)

Step3: Associate policies for the user (policies specify the permissions, so the user can have the permissions which the policies specify when associating with the policies)
![](//mccdn.qcloud.com/static/img/6554d84d46a16ea7f708402600bfe08b/image.png)

Step4: In the "User Management" list, you can view the sub-users you just added.
![](//mccdn.qcloud.com/static/img/f25458bc47e905348883376d3d645244/image.png)


### 4. Key of Sub-account

Key: Using the login account and password of sub-account, you can find the key of sub-user in the "Cloud Products" - "Cloud API Key" in the console. The key is used to generate the signature, and you can have access to relevant Tencent Cloud resources after passing the verification.

Function of Signature:

- 1. Verify the identity of the request user. Identify it based on user key.
 
  2. Prevent the content from being tampered with. Sign for the request content using hash algorithm, and then analyze and determine whether the content is tampered with based on the consistency of signature.
 
  3. Prevent replay attacks. Signature content includes request time, signature time and validity period, which can avoid replay for expired requests. Also, Cloud Services can refuse expired requests based on request time.



-



# Ⅱ. Creating a Custom Policy (Console)



### 1. Specify Specific API (Enable Permissions)

We can create a custom policy to enable the permissions of specific API, for example, to specify the write permission (Consume Message, Consume Messages in Batch) of CMQ Queue.

![](//mc.qcloudimg.com/static/img/ebe81c0f3661863f9961db0c5716081d/image.png)

Specify specific API


![](//mc.qcloudimg.com/static/img/6237ef0c57ef39db790e19638f4e1bc5/image.png)




### 3. Specify Resource Objects

In the example, we specify the policy and use all of Queues under the sub-account (including those created by the sub-account) as the associated objects.


![](//mc.qcloudimg.com/static/img/ee8053f051805493d53d6f4f67f2d531/image.png)



### 4. Associate with a Sub-user

Associate the objects with a sub-user. When it is done, the sub-user will have the permission of Consume Message and Consume Messages in Batch for all the Queue resources under the sub-user.


![](//mc.qcloudimg.com/static/img/0bfdf9df7ad29dbae8e51c28904be972/image.png)


-



# Ⅲ. Examples of API Calls

### 1. API Protocol

```
Encoding Type: utf8
Encoding Format: json
Transmission Mode: post
Request Protocol: http
Call specifications are as below:
{
	"version"	: 1,
"componentName"	:"MC",
	"eventId"	:123456,
	"interface":{
"interfaceName" : "API Name"
"para" : {
                          API Parameters
                    }
}
}
Returned result: If there is an error in the returned result, returnCode is not 0, and returnMessage content is the error information
{
"version" : 1,
"eventId" : 123456,
"componentName" : "CONSOLE_LOGICAL_SERVER",
"returnValue" : 0,
"returnCode" : 0,
"returnMessage" : "OK",
"data" : {
"ownerUin":123,
"uin":124,
"ownerAppid":323
}
}
interfaceName and para in input parameter and data in output parameter will be explained later

```


### 2. API Description



https://mc.qcloudimg.com/static/pdf/0d1b37b99bb74fd6a796d6ca7fd0353c/docfile.pdf




### 3. Examples

```
1. Create a new policy: CreateCamStrategy
{
"strategyName":"strategy1",
"strategyInfo":'{"version":"2.0","principal":{"qcs":["qcs::cam::uin/1238423:uin/3232","qcs::cam::uin/1238423:groupid/13"]},"statement":[{"effect":"allow","action":"name/cmqqueue:ListQueue","resource":"*"},{"effect":"allow","action":["name/cmqqueue:ReceiveMessage","name/cmqqueue:BatchDeleteMessage"],"resource":["qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1","qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1"]}]}',
"remark":"horace test"
}
Sub-user Uin: 3232
strategyName: Policy name.
strategyInfo: Content described by the policy. (! Note that here it is necessary to pass a json string)
remark: Notes for the policy
resource setting*: if the operation requires associating with resources, it represents all objects. If the operation does not require associating with resources (such as list operation), it represents empty object
The meaning of policy: Sub-user 3232 is specified and granted the permissions of all queues under list account. It has the permissions of Consume Message and Delete Messages in Batch on horacetest1 from Beijing

```

```
2. Associate with/Remove policy API by sub-accounts: OperateCamStrategy
{
	"groupId":-1,
	"relateUin":123456,
	"strategyId":666,
	"actionType":1
}
Field Explanation:
groupId: if it is associated with users, groupId will deliver -1; if it is associated with user groups, groupId will deliver specific group ID.
relateUin: if it is associated with users, relateUin will deliver specific user uin; if it is associated with user groups, relateUin will deliver -1.
strategyId: ID of the policy to be associated with.
actionType: value "1" indicates associating with policy; value "2" indicates removing policy.
(This API is used for users or user groups to associate with/remove policies)
```



## 4. Instructions:

```
Notes:
	1) principal can be left empty, and users can be associated with using API "Associating with Policy"
	2) If there is only one element among principal, action and resource, it may not be enclosed with [].
	3) The format of resource is "qcs: project:serviceType:region:account:resource".
		a. project can be replaced with id/0, "*" or "id/*", which represents all projects. If project is left blank for authorization, it represents id/0; if project is left blank for authentication, it means that it can appear in any project. It is left blank by default.
		b. serviceType includes cos, cdn, vpc, etc., and "*" represents all services. This field cannot be left blank.
		c. If region is left blank, it means all regions are included. Other available values include "gz", "st", "tj", "sh", "hk", "ca", "shjr" and "bj". It is left blank by default.
		d. account is expressed as "uin/${uin}" or "uid/${uid}". If empty, it will be populated with "uin/${uin}" for resources of services such as CDN, VPC, and will be populated with "uid/${uid}" for COS service, with "${uin}" and "${uid}" representing uin and uid of visitor respectively. It is left blank by default. (A special value of "uin/-1" may occur for default policy, and -1 will be replaced by the developer uin when extension table is expanded. The uid/-1 for cos may be available in the future. Now it is unavailable because there is no corresponding relationship between uin and uid in DB. Also, the default policy only allows the authorization of sub-accounts or roles, so you can directly replace -1 with uin of root accounts to which the sub-accounts or roles belong)
		e. resource consists of a name/value pair. name represents the resource of a service. For example, prefix represents cos and host represents cdn. "*" represents all resources and is normalized to "*/*". This field cannot be left blank.
		f. User or policy is also a type of resource. CAM root account is qcs::cam::uin/1238423: uin/1238423; CAM sub-account is qcs::cam::uin/1238423: uin/3236671; anonymous user is qcs::cam::anonymous: anonymous.
	    g. If resource is blank, no object needs to be associated for the operation. It is normalized to * in the system.
        h. Whether uin or uid is the owner of the resource shall be subject to service. It must be verified by the service after passing authentication. We also recommend you to verify it before authorization. 
        
```
