## 1. 接口描述
 
域名: vpc.api.qcloud.com
接口名: DescribeAcl

查询网络acl列表，接口已废弃，请使用接口<a href='https://www.qcloud.com/document/api/215/1441'>DescribeNetworkAcl</a>查询网络ACL信息
 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> vpcId <td> 否 <td> String <td> 私有网络ID
<tr>
<td> name <td> 否 <td> String <td> acl名称
<tr>
<td> offset <td> 否 <td> Int <td> 起始页
<tr>
<td> limit <td> 否 <td> Int <td> 每页条数
</tbody></table>

 

## 3. 输出参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message <td> String <td> 错误信息
<tr>
<td> data <td> Array <td> 返回信息
<tr>
<td> data.totalCount <td> Int <td> 网络acl总数量
<tr>
<td> data.aclSet <td> Array <td> 网络acl信息数组
<tr>
<td> data.aclSet.vpcId <td> Int <td> 私用网络ID
<tr>
<td> data.aclSet.unVpcId <td> String <td> 私用网络统一ID。建议使用统一ID
<tr>
<td> data.aclSet.networkAclName <td> String <td> 网络acl名称
<tr>
<td> data.aclSet.networkAclId <td> String <td> 网络acl ID
<tr>
<td> data.aclSet.vpcName <td> String <td> 私用网络名称
<tr>
<td> data.aclSet.vpcCidrBlock <td> String <td> 私用网络网段
<tr>
<td> data.aclSet.subnetNum <td> Int <td> 绑定子网数量
<tr>
<td> data.aclSet.createTime <td> String <td> 创建时间
<tr>
<td> data.aclSet.acl <td> Array <td> 网络acl规则信息,分egress和ingress
<tr>
<td> data.aclSet.acl.name <td> String <td> 备注
<tr>
<td> data.aclSet.acl.ipProtocol <td> String <td> 协议
<tr>
<td> data.aclSet.acl.cidrIp<td> String <td> 源ip或者源网段
<tr>
<td> data.aclSet.acl.portRange<td> String <td> 源端口
<tr>
<td> data.aclSet.acl.action <td> String <td>  策略,1:允许;0:拒绝
</tbody></table>

 

## 4. 示例
 
输入
<pre>

  https://vpc.api.qcloud.com/v2/index.php?ActionDescribeAcl
  &vpcIdvpc-7izaqk5h
  &<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>

</pre>

输出
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

