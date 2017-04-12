## 1. API Description
This API (DescribeAcl) is used to query network ACLs.

Domain name:  vpc.api.qcloud.com


## 2. Input Parameters
 

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> vpcId <td> No <td> String <td> VPC ID
<tr>
<td> name <td> No <td> String <td> ACL name
<tr>
<td> offset <td> No <td> Int <td> Initial page
<tr>
<td> limit <td> No <td> Int <td> Number of entries per page
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
<tr>
<td> data <td> Array <td> Returned information
<tr>
<td> data.totalCount <td> Int <td> Total number of network ACLs
<tr>
<td> data.aclSet <td> Array <td> Network ACL information array
<tr>
<td> data.aclSet.vpcId <td> Int <td> VPC ID
<tr>
<td> data.aclSet.unVpcId <td> String <td> Unified VPC ID. It is recommended to use the unified ID
<tr>
<td> data.aclSet.networkAclName <td> String <td> Network ACL name
<tr>
<td> data.aclSet.networkAclId <td> String <td> Network ACL ID
<tr>
<td> data.aclSet.vpcName <td> String <td> VPC name
<tr>
<td> data.aclSet.vpcCidrBlock <td> String <td> VPC IP address range
<tr>
<td> data.aclSet.subnetNum <td> Int <td> Number of bound subnets
<tr>
<td> data.aclSet.createTime <td> String <td> Time of creation
<tr>
<td> data.aclSet.acl <td> Array <td> Network ACL rule information. This can be egress or ingress
<tr>
<td> data.aclSet.acl.name <td> String <td> Note
<tr>
<td> data.aclSet.acl.ipProtocol <td> String <td> Protocol
<tr>
<td> data.aclSet.acl.cidrIp<td> String <td> Source IP or source network segment
<tr>
<td> data.aclSet.acl.portRange<td> String <td> Source port
<tr>
<td> data.aclSet.acl.action <td> String <td>  Policy. 1: Allow; 0: Reject
</tbody></table>

 

## 4. Example
 
Input
<pre>

  https://vpc.api.qcloud.com/v2/index.php?ActionDescribeAcl
  &vpcIdvpc-7izaqk5h
  &<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>

</pre>

Output
```

{
    "code": 0,
    "message": "",
    "data": {
        "totalCount": 9,
        "aclSet": [
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "呃",
                "aclId": "acl-74iw0dqe",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-09-15 16:39:17"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "ACL-11",
                "aclId": "acl-k3z6g5ic",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-09-08 17:31:43"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "ACL-12",
                "aclId": "acl-dt8bmccm",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-09-08 17:29:58"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "shawn-acl",
                "aclId": "acl-56k6ljvm",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 2,
                "createTime": "2015-09-06 16:57:56"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "abc--99",
                "aclId": "acl-0jtfpfs2",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-09-01 15:46:02"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "abctest",
                "aclId": "acl-krmypnwq",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-08-31 20:40:30"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "test12",
                "aclId": "acl-qjtzcv50",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-08-31 10:48:24"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "acl_test9",
                "aclId": "acl-eejoh1fw",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-08-28 19:42:34"
            },
            {
                "vpcId": "vpc-7izaqk5h",
                "aclName": "12",
                "aclId": "acl-pzk2ly1u",
                "vpcName": "111341333",
                "vpcCidrBlock": "172.16.0.0\/12",
                "subnetNum": 0,
                "createTime": "2015-08-28 11:39:36"
            }
        ]
    }
}

```


