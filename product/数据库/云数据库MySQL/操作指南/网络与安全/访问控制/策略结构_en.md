
<span id = "celueyufa"></span>
### Policy Syntax

CAM policy:

```
{	 
        "version":"2.0", 
        "statement": 
        [ 
           { 
              "effect":"effect", 
              "action":["action"], 
              "resource":["resource"], 
               "condition": {"key":{"value"}} 
           } 
       ] 
} 

```
- **Version** is required, and must be "2.0" for now.
- **Statement** describes details of one or multiple policies. The element includes permission or permission set for other elements such as effect, action, resource, condition. One policy can only have one statement element.
 1. **Action** describes allowed or rejected operations. The operation can be API (with the prefix of cdb:). The element is required.
 2. **Resourcce** describes detailed data of authorization. Resource is described in 6-piece format. Detailed resource definition for each product is different. For more information on how to specify resource information, please see the corresponding product documentation of the resource declaration you wrote. The element is required.
 3. **Condition** describes the condition for the policy to take effect. Condition consists of operator, operational key and operate value. Condition value may include information such as time and IP address. Some services allow you to specify other values in the condition. This element is optional.
 4. **Effect** describes whether the result produced by the declaration is "Allow" or "Explicitly Deny". This includes two situations: allow, deny. The element is required.

<span id = "caozuo"></span>
### CDB Operations

In the CDB policy statement, you can specify any API operation from any service supported by CDB. For CDB, use the API with prefix of cdb:, such as cdb:CreateDBInstance or cdb:CreateAccounts.

1. If you want to specify multiple operations in one statement, separate them with comma as shown below:
```
"action":["cdb:action1","cdb:action2"]
```
2. You can also use wildcard to specify multiple operations, for example, you can specify all the operations starting with " Describe " as shown below:
```
"action":["cdb:Describe*"]
```
3. If you want to specify all the operations in CDB, use the wildcard * as shown below:
```
"action":["cdb:*"]
```

<span id = "ziyuanlujing"></span> 
### CDB Resources

Each CAM policy statement has its own resources.
General resource syntax is as follows:
```
qcs:project_id:service_type:region:account:resource
```

- **project_id**: The project information, which is only used to be compatible with the earlier CAM logics. It can be left empty.
- **service_type**: Abbreviation of the product, such as cdb.
- **region**: Region information, such as ap-guangzhou.
- **account**: The root account information of the resource owner, such as uin/653339763.
- **resource**: The detailed resource information of each product, such as instanceId/instance_id1 or instanceId/*.

For example:

1. You can set it to be a specific instance (cdb-k05xdcta) in the statement as shown below:
```
"resource":[ "qcs::cdb:ap-guangzhou:uin/653339763:instanceId/cdb-k05xdcta"]
```
2. You can also specify all instances under a specific account using the wildcard * as shown below:
```
"resource":[ "qcs::cdb:ap-guangzhou:uin/653339763:instanceId/*"]
```
3. If you want to specify all resources or a specific API operation does not support resource-level permissions, use the wildcard * in the Resource element as shown below:
```
"resource": ["*"]
```
4. If you want to specify multiple resources in one instruction, separate them with comma. In the example below, two resources are specified:
```
"resource":["resource1","resource2"]
```

The table below describes the resources that can be used in CDB and the corresponding syntax.
The words with prefix of $ are all appellations.

- project refers to the project ID.
- region refers to the region.
- account refers to the account ID.

| Resource | Resource description method in authorization policy |
|:-------|:-------|
| Instance |  ```qcs::cdb:$region:$account:instanceId/$instanceId```|
| VPC |  ```qcs::vpc:$region:$account:vpc/$vpcId```|
| Security Group |  ```qcs::cvm:$region:$account:sg/$sgId```|

