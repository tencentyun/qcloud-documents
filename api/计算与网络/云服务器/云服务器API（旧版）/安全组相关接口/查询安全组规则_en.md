## 1. API Description
 
This API (DescribeSecurityGroupPolicys) is used to query the rules for existing security groups.
Domain name for API request: dfw.api.qcloud.com
(1) The "ingress" and "egress" lists are returned.
(2) Each security group rule can contain a maximum of four valid fields: ipProtocol, cidrIp or sgId (the two are mutually exclusive and cannot be specified at the same time), portRange, and action. The action field is required. If any of the other fields is not specified, it means that the rule may ignore this field and match all when processing network messages.
 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Common request parameters are also needed when the API is called. For more information, please see Common Request Parameters page. The Action field for this API is DescribeSecurityGroupPolicys.
<table class="t"><tbody><tr>
<th><b>Parameter </b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Security group ID
</tbody></table>

 

## 3. Output Parameters
 
| Parameter  | Type | Description |
|---------|---------|---------|
| code | Int | Error code. 0: Successful; other values: Failed |
| message | String | Error message |
| data | Array | Returned data structure|

`data` is composed as follows:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.ingress <td> Array <td> Inbound rule list
<tr>
<td> data.egress <td> Array <td> Outbound rule list
</tbody></table>

`ingress`/`egress` structure
<table class="t"><tbody><tr>
<th><b>Parameter</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> index <td> Int <td> Rule position, starting from 0
<tr>
<td> addressModule <td> String <td> IP address ID or IP address group ID. It is mutually exclusive with cidrIp sgId.
<tr>
<td> ipProtocol <td> String <td> Network protocol, which supports UDP, TCP, ICMP, etc. If this is left empty, it supports all protocols.
<tr>
<td> cidrIp <td> String <td> IP or IP range. The absence of this field indicates full IP. It does not appear together with sgId at the same time.
<tr>
<td> sgId <td> String <td> Security group ID. It does not appear together with cidrIp at the same time.
<tr>
<td> portRange<td> String <td> Port or port range. The absence of this filed indicates full port.
<tr>
<td> serviceModule <td> String <td> Protocol port ID or protocol port group ID. It is mutually exclusive with ipProtocol+portRange.
<tr>
<td> desc <td> String <td> Rule description
<tr>
<td> action <td> String <td> Action (accept or drop)
<tr>
<td> version <td> Int <td> Version, which is automatically increased by one each time you update the security rules, so as to prevent your updated routing rules from being expired
</tbody></table>

## 4. Error Codes
 <table class="t"><tbody><tr>
<th><b>Error Code Value</b></th>
<th><b>Reason</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 7001 <td> Security group does not belong to the current user
</tbody></table>


## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeSecurityGroupPolicys
  &sgId=sg-33ocnj9n
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "ingress": [
            {
                "index": 0,
                "action": "ACCEPT",
                "serviceModule": "ppm-i083665x",
                "addressModule": "ipmg-poo8128q"
            },
            {
                "index": 1,
                "action": "ACCEPT",
                "portRange": "22",
                "sgId": "sg-ghm9l8ve",
                "ipProtocol": "tcp"
            },
            {
                "index": 2,
                "action": "ACCEPT",
                "cidrIp": "10.1.1.10",
                "ipProtocol": "tcp"
            }
        ]
    }
}

```


