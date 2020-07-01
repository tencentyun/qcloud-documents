## Prerequisite: Key of Sub-user

Log in to the console using the account and password of sub-account, and you can find the key of sub-user in the "Cloud Products" - "[Cloud API Key](https://console.cloud.tencent.com/capi)". The key is used to generate the signature, and you can have access to relevant Tencent Cloud resources after passing the verification.

Function of Signature:
- **Verify the identity of request user:** Identify it based on user key.
- **Prevent the content from being tampered with:** Sign for the request content using hash algorithm, and then analyze and determine whether the content is tampered with based on the consistency of signature.
- **Prevent replay attacks:** Signature content includes request time, signature time and validity period, which can avoid replay for expired requests. Also, Cloud Services can refuse expired requests based on request time.


## Simple Examples of API Calls

### 1. API Protocol

Encoding Type: utf8
Encoding Format: json
Transmission Mode: post
Request Protocol: http

Call specifications are as below:
```
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
```
Returned result: If there is an error in the returned result, returnCode is not 0, and returnMessage content is the error information.

```
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
```

> Note: interfaceName and para in input parameter and data in output parameter will be explained later.

### 2. API Description

For more information about APIs for user and permission CAM, [click here >>](https://mc.qcloudimg.com/static/pdf/0d1b37b99bb74fd6a796d6ca7fd0353c/docfile.pdf) 

### 3. Examples of Calls

#### Create a new policy: CreateCamStrategy

**Example of policy:**

Set a sub-user (with uin of 3232) to have permission for all queues under list account, and have the permissions of Consume Message and Delete Messages in Batch on horacetest1 from Beijing region.

**Field Explanation:**

| Parameter | Description | Example Value |
|---------|---------|---------|
| strategyName | Policy name. | strategy1 |
| strategyInfo | Content described by the policy. (Note that a json string is required here) | See Sample Codes |
| remark | Notes for the policy. | horace test |
| resource setting* | If the operation requires associating with resources, it represents all objects. If the operation does not require associating with resources (such as list operation), it represents empty object. |* |

**Sample Codes:**

```
{
"strategyName":"strategy1",
"strategyInfo":'{"version":"2.0","principal":{"qcs":["qcs::cam::uin/1238423:uin/3232","qcs::cam::uin/1238423:groupid/13"]},"statement":[{"effect":"allow","action":"name/cmqqueue:ListQueue","resource":"*"},{"effect":"allow","action":["name/cmqqueue:ReceiveMessage","name/cmqqueue:BatchDeleteMessage"],"resource":["qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1","qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1"]}]}',
"remark":"horace test"
}
```


#### Associate with/Remove policy by sub-accounts: OperateCamStrategy

This API is used for users or user groups to associate with/remove policies.

**Example of policy:** Associate the user with a UIN of 123456 to the policy with a policy ID of 666.

**Field Explanation:**

| Parameter | Description | Example Value |
|---------|---------|---------|
| groupId | If it is associated with users, -1 will be passed for groupId; <br>if it is associated with user groups, a specific group ID will be passed for groupId. | -1 |
| relateUin | If it is associated with users, a specific user uin will be passed for relateUin; if it is associated with user groups, -1 will be passed for relateUin. | 123456 |
| strategyId | ID of the policy to be associated with. | 666 |
| actionType | "1" indicates associating with policy; "2" indicates removing policy. | 1 |

**Sample Codes:**

```
{
	"groupId":-1,
	"relateUin":123456,
	"strategyId":666,
	"actionType":1
}
```
## Instructions
> Note: This section is applicable to user and permission management of various services. When setting CMQ service, please determine the relevant values of CMQ according to the following instructions.

1. principal can be left empty, and users can be associated with using API "Associating with Policy";
2. If there is only one element among principal, action and resource, it may not be enclosed with [].
3. Usually, 6-piece format is used for describing the resource, such as "qcs:project:serviceType:region:account:resource".
	- project can be replaced with id/0, "*" or "id/*", which represents all projects. If project is left blank for authorization, it represents id/0; if project is left blank for authentication, it means that it can appear in any project. It is left blank by default.
	- serviceType includes cos, cdn, vpc, etc., and "*" represents all services. This field cannot be left blank.
	- If region is left blank, it means all regions are included. Other available values include "gz", "st", "tj", "sh", "hk", "ca", "shjr" and "bj". It is left blank by default.
	- account is expressed as "uin/${uin}" or "uid/${uid}". If empty, it will be populated with "uin/${uin}" for resources of services such as CDN, VPC, and will be populated with "uid/${uid}" for COS service, with "${uin}" and "${uid}" representing uin and uid of visitor respectively. It is left blank by default. (A special value of "uin/-1" may occur for default policy, and -1 will be replaced by the developer uin when extension table is expanded. Also, the default policy only allows the authorization of sub-accounts or roles, so you can directly replace -1 with uin of root accounts to which the sub-accounts or roles belong.
	- resource consists of a name/value pair. name represents the resource of a service. For example, it is queueName and topicName for cmq. It is described with the prefix for cos, and is described with host for cdn. "*" represents all resources and is normalized to "*/*". This field cannot be left blank.
	- User or policy is also a type of resource. CAM root account is described as qcs::cam::uin/1238423: uin/1238423; CAM sub-account is qcs::cam::uin/1238423: uin/3236671; anonymous user is qcs::cam::anonymous: anonymous.
	- If resource is blank, it indicates that no object needs to be associated for the operation. It is normalized to * in the system.
 - Whether uin or uid is the owner of the resource shall be subject to service. It must be verified by the service after passing authentication. We also recommend you to verify it before authorization. 
