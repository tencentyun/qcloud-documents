### 1. Concepts and Application Scenarios
    
In many scenarios, we need to further define the conditions for the created policies.
    
Scenario 1: When a CAM user calls cloud APIs, the source of user access needs to be restricted by adding IP conditions to the current policy.
    
Scenario 2: When a CAM user calls VPC peering connection APIs, it is necessary to verify whether the CAM user has the access to peering connection APIs, peering connection resources and the VPC associated with the peering connection.
    
### 2. Syntax Structure	

![](https://mc.qcloudimg.com/static/img/4c47f9d1a72dfcdd76a7c3837711ae07/600.png)

The syntax structure of a condition is shown above.
    
A condition block consists of several sub blocks, each of which has a conditional operator and several conditional keys, with each conditional key having several conditional values. 
    
### 3.Evaluation Logic
    
The evaluation logic based on which a condition takes effect is described below.
    
1) A conditional key maps onto several conditional values. As long as the key value in the context matches any of the conditional values based on the associated conditional operator, the condition takes effect.
    
2) If a sub-block consists of multiple conditional keys, the sub-block takes effect only when the conditions for all the conditional keys take effect.
    
3) If a condition block consists of multiple sub-blocks, the condition takes effect only when all the sub blocks take effect.
    
4) For a conditional key containing if_exist, the condition still takes effect even if the key value does not exist in the context.
    
### 4. Examples
    
1) In the following example, the condition for allowing sending messages to the specified queue is that the cloud APIs must be called within IP address range 10.217.182.* or 111.21.33.*.


```
{
  "version": "2.0",
  "statement": {
    "effect": "allow",
    "action": "name/cmqqueue:Sendmessages",
    "resource": "qcs::cmq:sh::queueName/123877/test",
    "condition": {"ip_equal": {"qcs:ip": ["10.217.182.3/24", "111.21.33.72/24"]}}
  }
}
```

2) In the following example, the condition for allowing VPC to be bound to the specified NAT gateway is that the VPC is located in Shanghai with a VPCID value of 324238.

```
{
  "version": "2.0",
  "statement": {
    "effect": "allow",
    "action": "name/vpc:AcceptVpcPeeringConnection",
    "resource": "qcs::vpc:sh::pcx/2341",
    "condition": {"string_equal_if_exist": {"vpc:region": "sh"}}
  }
}
```

### 5. Conditional Operators
    
The following are currently supported conditional operators as well as common conditional keys and examples. For custom conditional keys of each product, please see the product documentation.


| Conditional Operator | Description | Condition Name | Example |
|---------|---------|---------|---------|
| string_equal | string is equal to | qcs:tag | {"string_equal":{"qcs:tag/tag_name1":"tag_value1"}} |
| string_not_equal | string is not equal to | qcs:tag | {"string_not_equal":{"qcs:tag/tag_name1":"tag_value1"}} |
| date_not_equal | date is not equal to | qcs:current_time | {"date_not_equal":{"qcs:current_time":"2016-06-01T00:01:00Z"}} |
| date_greater_than | date is later than | qcs:current_time | {" date_greater_than ":{"qcs:current_time":"2016-06-01T00:01:00Z"}} |
| date_greater_than_equal | date is later than or equal to | qcs:current_time | {" date_greater_than_equal ":{"qcs:current_time":"2016-06-01T00:01:00Z"}} |
| date_less_than | date is earlier than | qcs:current_time | {" date_less_than ":{"qcs:current_time":"2016-06-01T 00:01:00Z"}} |
| date_less_than_equal | date is earlier than or equal to | qcs:current_time | {" date_less_than ":{"qcs:current_time":"2016-06-01T 00:01:00Z"}} |
| date_less_than_equal | date is earlier than or equal to | qcs:current_time | {"date_less_than_equal ":{"qcs:current_time":"2016-06-01T00:01:00Z"}} |
| ip_equal | IP is equal to | qcs:ip | {"ip_equal":{"qcs:ip ":"10.121.2.10/24"}} |
| ip_not_equal | IP is not equal to | qcs:ip | {"ip_not_equal":{"qcs:ip ":["10.121.2.10/24", "10.121.2.20/24"]}} |
| numeric_not_equal | numeric value is not equal to | qcs:mfa | {" numeric_not_equal":{"mfa":1}} |
| numeric_greater_than | numeric value is greater than | | {"numeric_greater_than ":{"cvm_system_disk_size":10}} |
| numeric_greater_than_equal | numeric value is greater than or equal to | | {"numeric_greater_than_equal ":{"cvm_system_disk_size":10}} |
| numeric_less_than | numeric value is less than | | {"numeric_less_than ":{"cvm_system_disk_size":10}} |
| numeric_less_than_equal | numeric value is less than or equal to |  | {"numeric_less_than_equal ":{"cvm_system_disk_size":10}} |
| numeric_equal | numeric value is equal to | {" numeric_equal":{"mfa":1}} |
| numeric_greater_than | numeric value is greater than | | {"numeric_greater_than ":{"come_key":11}} |

Notes:

1) The date format is based on ISO8601 standard and UTC time is required.

2) IP format should conform to the CIDR notation.

3) For conditional key with a suffix of _if_exist, the condition takes effect even if the key value does not exist in the context.

4) Some of the businesses do not support conditions, or only support some of the conditions. For more information, please see business documentation.




