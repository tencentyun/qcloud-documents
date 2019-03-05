Policy consists of several elements and is used to describe specific information about authorization. Core elements include principal, action, resource, condition and effect. 

**Note:**
- The reserved words must be lowercase. The description doesn't have sequence requirement. 
- Condition element is optional if there is no particular condition restrictions for the policy. 
- It's not allowed to write principal element in the console, you can only use principal in policy syntax related parameters in policy management APIs.

### 1. Version

Describes policy syntax version. This element is required. Currently ,the only available value is "2.0".

### 2. Principal

Describes the entity to be authorized by the policy. This includes users (developers, sub accounts, anonymous users), user groups. More entities will be included in the future such as roles, users with federated identities. You can only use this element in policy syntax related parameters of policy management APIs.

### 3. Statement

Describes details of one or multiple policies. The element includes permission or permission set for other elements such as action, resource, condition, effect. One policy can only have one statement element.

### 4. Action

Describes allowed or disallowed actions. An action can be an API (described using the prefix "name") or a feature set (a set of specific APIs, described using the prefix "permid"). This element is mandatory.

### 5. Resource

Describes the detailed data of authorization. Resource is described using 6-piece format. Detailed resource definition for each product is different. For information on how to specify resource information, please see the corresponding product documentation of the resource declaration you wrote. This element is mandatory.

### 6. Condition

Describes the condition for the policy to become effective. Condition consists of operator, operational key and operate value. Condition value may include information such as time and IP address. Some services allow you to specify other values in the condition. This element is optional.

### 7. Effect
	
Describes whether the result produced by the declaration is "Allow" or "Explicitly Deny". This includes two situations: allow, deny. This element is mandatory.

### 8. Example Policy
	
The policy in this example allows the sub-account with ID 3232523 and group ID 18825 that belongs to the developer with ID 1238423 to have permission to use all COS read APIs and write objects, as well as to send message queues, for the COS bucket "bucketA" in Beijing region and the COS object "object2" in Guangzhou region, on condition that access IP falls within the range of 10.121.2.*.


```
{	 
        "version":"2.0", 
        "principal":{"qcs":["qcs::cam::uin/1238423:uin/3232523", 
                        "qcs::cam::uin/1238423:groupid/18825"]}, 
        "statement": 
        [ 
           { 
              "effect":"allow", 
              "action":["name/cos:PutObject","permid/280655"], 
              "resource":["qcs::cos:bj:uid/1238423:prefix/bucketA/*", 
                        "qcs::cos:gz:uid/1238423:prefix/bucketB/object2"], 
               "condition": {"ip_equal":{"qcs:ip":"10.121.2.10/24"}} 
           }, 
          { 
             "effect":"allow", 
             "action":"name/cmqqueue:Sendmessages", 
             "resource":"*" 
          } 
       ] 
} 
```
