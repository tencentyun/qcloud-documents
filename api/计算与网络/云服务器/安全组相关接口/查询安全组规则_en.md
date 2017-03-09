## 1. API Description
 
This API (DescribeSecurityGroupPolicy) is used to query the rules for existing security groups.
Domain name for API request:<font style="color:red">dfw.api.qcloud.com</font>
1) The "ingress" and "egress" lists will be returned.
2) Each security group rule can contain up to four valid fields: ipProtocol, cidrIp or sgId (the two are mutually exclusive and do not appear at the same time), portRange, and action. The action field will always be there. If any of the other fields does not appear, it means that the rule will ignore that field and match all when processing network messages.
 

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is DescribeSecurityGroupPolicy.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Security group ID
</tbody></table>

 

## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0: succeeded, other values: failed |
| message | String | Error message |
| data | Array | Returned data structure|

Data structure:
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> data.ingress <td> Array <td> Inbound rule list
<tr>
<td> data.egress <td> Array <td> Outbound rule list
</tbody></table>

Ingress/egress rule member structure
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> ipProtocol <td> String <td> Network protocol, which supports udp, tcp, icmp, etc.; the absence of this filed indicates full protocol.
<tr>
<td> cidrIp <td> String <td> IP or IP range; the absence of this field indicates full IP. Does not appear together with sgId.
<tr>
<td> sgId <td> String <td> Security group ID. Does not appear together with cidrIp.
<tr>
<td> portRange<td> String <td> Port or port range; the absence of this filed indicates full port.
<tr>
<td> desc <td> String <td> Rule description
<tr>
<td> action <td> String <td> Action, accept or drop
</tbody></table>

## 4. Error Codes
 <table class="t"><tbody><tr>
<th><b>Error Code</b></th>
<th><b>Description</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 7001 <td> Security group does not belong to the current user
</tbody></table>


## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeSecurityGroupPolicy
  &sgId=sg-33ocnj9n
  &<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": {
        "ingress": [
            {
                "ipProtocol": "tcp",
                "cidrIp": "10.0.0.0\/8",
                "portRange": "22",
                "desc": "Access to tcp protocol port 22 for inbound traffic of private network is prohibited",
                "action": "ACCEPT"
            }
        ],
        "egress": [
            {
                "ipProtocol": "tcp",
                "cidrIp": "10.0.0.0\/8",
                "desc": "Outbound tcp traffic of private network is allowed",
                "action": "ACCEPT"
            }
        ]
    }
}

```

