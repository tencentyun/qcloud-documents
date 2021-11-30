## 1. 接口描述

域名: vpc.api.qcloud.com
接口名: DescribeAcl

查询网络 ACL 列表

## 2. 输入参数

| **参数名称** | **必选** | **类型** | **描述**   |
| ------------ | -------- | -------- | ---------- |
| vpcId        | 否       | String   | 私有网络 ID |
| name         | 否       | String   | ACL 名称    |
| offset       | 否       | Int      | 起始页     |
| limit        | 否       | Int      | 每页条数   |

## 3. 输出参数

| **参数名称**               | **类型** | **描述**                          |
| -------------------------- | -------- | --------------------------------- |
| code                       | Int      | 错误码, 0: 成功, 其他值: 失败     |
| message                    | String   | 错误信息                          |
| data                       | Array    | 返回信息                          |
| data.totalCount            | Int      | 网络 ACL 总数量                     |
| data.aclSet                | Array    | 网络 ACL 信息数组                   |
| data.aclSet.vpcId          | Int      | 私用网络 ID                        |
| data.aclSet.unVpcId        | String   | 私用网络统一 ID。建议使用统一 ID    |
| data.aclSet.networkAclName | String   | 网络 ACL 名称                       |
| data.aclSet.networkAclId   | String   | 网络 ACL ID                        |
| data.aclSet.vpcName        | String   | 私用网络名称                      |
| data.aclSet.vpcCidrBlock   | String   | 私用网络网段                      |
| data.aclSet.subnetNum      | Int      | 绑定子网数量                      |
| data.aclSet.createTime     | String   | 创建时间                          |
| data.aclSet.acl            | Array    | 网络 ACL 规则信息，分 egress 和 ingress |
| data.aclSet.acl.name       | String   | 备注                              |
| data.aclSet.acl.ipProtocol | String   | 协议                              |
| data.aclSet.acl.cidrIp     | String   | 源 IP 或者源网段                    |
| data.aclSet.acl.portRange  | String   | 源端口                            |
| data.aclSet.acl.action     | String   | 策略，1:允许;0:拒绝                |

## 4. 示例

输入

```
  https://vpc.api.qcloud.com/v2/index.php?ActionDescribeAcl
  &vpcIdvpc-7izaqk5h
  &公共请求参数
```

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
