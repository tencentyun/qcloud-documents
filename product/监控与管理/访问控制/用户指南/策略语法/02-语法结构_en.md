![](https://mc.qcloudimg.com/static/img/06d3b1a6be4d9798286256ce2ecebbed/poly.png)

The syntax structure of the entire policy is shown in the figure above.

	
Policy consists of version and statement, it can also include principal information. You can only use principal in policy syntax related parameters in policy management APIs. Statement consists of several sub statements. Each sub statement includes four elements: action, resource, condition (optional) and effect.
	
### 1. JSON Format
	
Policy syntax is based on JSON format. You cannot submit created or updated policies that do not meet the requirement of JSON format. Users must ensure that policies use the correct JSON format. The standard of JSON format is defined in RFC 7159. You can also use the online JSON verification program to check policy format.
    
### 2. Conventions of Syntax
    
Here are the conventions for syntax descriptions:
    
1) These characters are JSON characters included in policy syntax:

 { } [ ] " , :
    
2) These characters are special characters used to describe policy syntax and are not included in policies: 

 = < > ( ) |
   
3) When an element allows multiple values, the values are described using comma separators and ellipsis. For example:

  ```        
 [<resource_string>, < resource_string>, ...]
     
 <principal_map> = { <principal_map_entry>, > <principal_map_entry>, ... }
   ```      
	 
The element can also include one value even if multiple values are allowed. When an element includes only one value, you must remove the comma in the end and use brackets to indicate optional value. For example:

 ```    
 "resource": [<resource_string>]
     
 "resource": <resource_string>
     
```


4) The question mark (?) behind the element indicates that the element is optional. For example:
 

 ```   
 <condition_block?>
```
     
5) When the element is enumerated value, use vertical line "|" to separate the values and use parenthesis "()" to define the range of the values. For example:

 ```      
("allow" | "deny")
```
 
6) Use double quotes to enclose string elements. For example:
 
      
```
<version_block> = "version" : "2.0"
```



### 3. Syntax Description

```

policy  = {
     <version_block>
     <principal_block?>,
     <statement_block>
}

<version_block> = "version" : "2.0"

<statement_block> = "statement" : [ <statement>, <statement>, ... ]

<statement> = {     
    <effect_block>,
    <action_block>,
    <resource_block>,
    <condition_block?>
}

<effect_block> = "effect" : ("allow" | "deny")  

<principal_block> = "principal": ("*" | <principal_map>)

<principal_map> = { <principal_map_entry>, <principal_map_entry>, ... }

<principal_map_entry> = "qcs":   
    [<principal_id_string>, <principal_id_string>, ...]

<action_block> = "action": 
    ("*" | [<action_string>, <action_string>, ...])

<resource_block> = "resource": 
    ("*" | [<resource_string>, <resource_string>, ...])

<condition_block> = "condition" : { <condition_map> }
<condition_map> { 
  <condition_type_string> : { <condition_key_string> : <condition_value_list> },
  <condition_type_string> : { <condition_key_string> : <condition_value_list> }, ...
}  
<condition_value_list> = [<condition_value>, <condition_value>, ...]
<condition_value> = ("string" | "number")
```
Syntax instruction:

1) A policy may contain multiple statements.
     
The maximum length for a policy is 4,096 characters (spaces not included). See restrictions for details.

There is no restriction for the order in which each block is displayed. For example, in a policy, version_block can be located right behind effect_block.

2) Current supported syntax version is 2.0.

3) It's not allowed to write principal_block element in the console, you can only use principal in policy syntax related parameters in policy management APIs.

4) Lists are supported by both actions and resources. Actions also support action sets (permid) defined in each product.
    
5) Condition can be a single condition or a logic combination that contains multiple sub condition blocks. Each condition consists of operator (condition_type), condition key (condition_key) and condition value (condition_value).
    
6) The effect of each statement can be "deny" or "allow". If there are both "allow" and "deny" in the statements of a policy, we prioritize "deny".

### 4. String Instruction

    
Instructions regarding element strings in syntax descriptions.
    
action_string:
    
Consists of description action scope, service type and action name. 


```
//All actions for all products
"action":"*"
"action":"name/*:*"
//All actions for COS products
"action":"name/cos:*"
//GetBucketPolicy action for COS products
"action":"name/cos:GetBucketPolicy"
//Actions that match with "Bucket" for COS products
"action":"name/cos:*Bucket*"
//Action list with the action set ID of 280649
"action":"permid/280649"
//Action list with the name "GetBucketPolicy\PutBucketPolicy\DeleteBucketPolicy" for COS products
"action":["name/cos:GetBucketPolicy","name/cos:PutBucketPolicy","name/cos: DeleteBucketPolicy"]
```

 "permid" is the action set ID defined for each product. For more information, please see the help documents for each product.
    
resource_string:
    
Resource is described using 6-piece format." qcs:  project :serviceType:region:account:resource". Example:

```
//Object resource of COS product. Region: Shanghai. UID of the resource owner: 1238423. Resource name: bucket1/object2. Resource prefix: prefix
qcs::cos:sh:uid/1238423:prefix/bucket1/object2
//Queue of CMQ product. Region: Shanghai. UID of the resource owner: 6887234. Resource name: 6887234/queueName1. Resource prefix: queueName
qcs::cmqqueue:sh:uin/6887234:queueName/6887234/queueName1
```
 condition_type_string:
    
Conditional operator used to describe type of the test condition. For example: string_equal, string_not_equal, date_ equal, date_not_equal, ip_equal, ip_not_equal, numeric_equal, numeric_not_equal and so on. Example:

```
"condition":{
         "string_equal":{"qcs:tag":["dev1","dev3"],
                      "mfa":"1"]},
         "ip_equal":{"qcs:ip":"10.131.12.12/24"}
}
```
condition_key_string:
    
Condition key which indicates that operation will be performed by using conditional operator on its value, in order to determine if the conditions are met. CAM defines a set of condition keys that can be used in any product, such as qcs:current_time, qcs:ip, qcs:uin and qcs:owner_uin. For more information, please see Conditions.
    
principal_id_string:
    
For CAM products, users are resources. Thus, principals are also described using 6-piece format. An example is given below. For more information, please see Resource Description Method.

```
"principal":   {"qcs":["qcs::cam::uin/1238423:uin/3232",
             "qcs::cam::uin/1238423:groupid/13"]}
```

