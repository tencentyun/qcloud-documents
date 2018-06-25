## 1. API Description
 
This API (ModifySecurityGroupPolicy) is used to modify the rules of existing security groups.
Domain name for API request: <font style="color:red">dfw.api.qcloud.com</font>

1) Input the inbound and outbound rules for a security group through the "ingress" and "egress" lists respectively. There is a [upper limit](https://cloud.tencent.com/doc/product/213/500#2.-.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84.E9.99.90.E5.88.B6) for each kind of rules. The last rule is a DROP rule by default. It does not need to be entered and is not subject to the rule number limit.
2) When there are multiple rules for the inbound or outbound direction, the rules take effect in the order shown in the entered list, overwriting the original rules of the security group.
3) Rules [Description](https://cloud.tencent.com/doc/product/213/500#3.-.E5.AE.89.E5.85.A8.E7.BB.84.E8.A7.84.E5.88.99)
4) Each security group rule can contain up to four valid fields: ipProtocol, cidrIp or sgId (the two are mutually exclusive and cannot be entered at the same time), portRange, and action. The action field is required. If any of the other fields does not appear, it means that the rule will ignore that field and match all when processing network messages.
5) The ipProtocol field allows you to enter tcp, udp and icmp in a case-insensitive manner.
6) The cidrIp field allows you to enter any string that conforms to the cidr format. (More details) In a basic network, if cidrIp contains private IPs on Tencent Cloud for devices within your account other than CVM, it does not mean this rule allows you to access these devices. The network isolation rules between tenants take priority over the private network rules in security groups.
7) The sgId field allows you to enter the IDs of security groups that are in the same project as the security group to modify, including the ID of the security group itself, to represent private IPs of all CVMs under the security group. When this field is used, this rule will change as the CVM associated with the ID entered here changes while it's being used to match network messages, and does not need to be modified.
8) The portRange field allows you to enter a single port number, or two port numbers separated by a minus sign, e.g., 80 or 8000-8010. The ipProtocol field must be filled with tcp or udp for the portRange field to be accepted.
9) The action field allows you to enter ACCEPT or DROP strings in a case-insensitive manner.
10) The desc field allows you to enter the description of a single rule, which must be no more than 50 UTF-8 characters in length.
11) If the rule fields are entered in violation of the above constraints, the entire calling will not be applied and an error will be returned, and your actual security group rules will remain unchanged.

## 2. Input Parameters
 
The following request parameter list only provides API request parameters. Public request parameters need to be added when the API is called. See the Public Request Parameters page for details. The Action field for this API is ModifySecurityGroupPolicy.
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> sgId <td> Yes <td> String <td> Security group ID
<tr>
<td> ingress <td> Yes <td> Array <td> Inbound rule list
<tr>
<td> egress <td> Yes <td> Array <td> Outbound rule list
</tbody></table>

ingress / egress rule member structure
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> ipProtocol <td> String <td> Network protocol, which supports udp, tcp, icmp, etc.; the absence of this field indicates full protocol
<tr>
<td> cidrIp <td> String <td> IP network segment address, which is not passed as full address, and mutually exclusive with sgId; existence of both of them in a rule will result in an error
<tr>
<td> sgId <td> String <td> Security group ID, which is mutually exclusive with cidrIp; existence of both of them in a rule will result in an error
<tr>
<td> portRange<td> String <td> Port, not passed as any port
<tr>
<td> desc <td> String <td> Rule description
<tr>
<td> action <td> String <td> Action, accept or drop
</tbody></table> 

## 3. Output Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code <td> Int <td> Error code, 0: succeeded, other values: failed
<tr>
<td> message <td> String <td> Error message
</tbody></table>

## 4. Error Codes
<table class="t"><tbody><tr>
<th><b>Error Code</b></th>
<th><b>Description</b></th>
<tr>

<td> 7000 <td> Security group backend exception
<tr>
<td> 7001 <td> Security group does not belong to the current user
<tr>
<td> 7002 <td> Reached the upper limit of rules
<tr>
<td> 7006 <td> This is a preset security group and cannot be deleted
<tr>
<td> 9003 <td> The rule data format is incorrect
</tbody></table>

## 5. Example
 
Input
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupPolicy
  &sgId=sg-33ocnj9n
  &ingress.0.ipProtocol=tcp
  &ingress.0.cidrIp=10.0.0.0/8
  &ingress.0.action=ACCEPT
  &ingress.0.portRange=22
  &ingress.0.desc=Access to tcp protocol port 22 for inbound traffic of private network is prohibited
  &egress.0.action=ACCEPT
  &egress.0.ipProtocol=tcp
  &egress.0.desc=Outbound tcp traffic of private network is allowed
  &egress.0.cidrIp=10.0.0.0/8
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>

</pre>

Output
```

{
    "code": 0,
    "message": ""
}

```

