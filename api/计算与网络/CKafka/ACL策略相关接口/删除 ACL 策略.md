

## 1. 接口描述

接口请求域名：`ckafka.api.qcloud.com`
本接口（DeleteAcl）用于为实例的用户删除 ACL 策略。

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/product/597/10084) 页面。

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| instanceId | 是 | String | 实例 ID |
| resourceType| 是 | Int|ACL 资源类型，（0：UNKNOWN，1：ANY，2：TOPIC，3：GROUP，4：CLUSTER，5：TRANSACTIONAL_ID） |
| resourceName| 是| String |资源名称，和 resourceType 相关，如当 resourceType 为 TOPIC 时，则该字段表示 topic 名称，当 resourceType 为 GROUP 时，该字段表示 group 名称 |
| operation| 是| Int|ACL 操作方式（0：UNKNOWN，1：ANY，2：ALL，3：READ，4：WRITE，5：CREATE，6：DELETE，7：ALTER，8：DESCRIBE，9：CLUSTER_ACTION，10：DESCRIBE_CONFIGS，11：ALTER_CONFIGS，12：IDEMPOTEN_WRITE） |
| permissionType| 是 | Int |权限类型（0：UNKNOWN，1：ANY，2：DENY，3：ALLOW） |
| host| 是 | String | ACL 策略作用的主机 IP，默认为  \*，表示任何 host 都可以访问 |
| principal| 是| String | ACL 策略关联的用户列表，默认为 User:\*，表示实例所有的用户|

## 3. 示例

输入：

```
  https://domain/v2/index.php?Action=AddAcl
  &instanceId=ckafka-tadfqa0
  &resourceType=2
  &resourceName=test-topic
  &operation=0
  &permissionType=3
  &host=*
  &principal=User:user1
  &<公共请求参数>
```

输出：

```
{
      "code" : 0,
      "codeDesc":"Success",
      "message" : "ok"
  }
```
