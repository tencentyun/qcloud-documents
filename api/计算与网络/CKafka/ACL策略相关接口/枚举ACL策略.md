## 1. 接口描述

本接口 (ListAcl) 用于为实例的用户删除ACL策略

接口请求域名：<font style="color:red">ckafka.api.qcloud.com</font>

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/doc/api/431/5883)页面。

| 参数名称 | 必选 | 类型 | 描述 |
| --- | --- | --- | --- |
| instanceId | 是 | String | 实例id |
| resourceType| 是 | Int|ACL资源类型，（0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID） |
| resourceName| 是| String |资源名称，和resourceType相关如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称 |
| searchWord| 否 | String |（过滤条件）按照资源名称过滤，支持模糊查询。 |
| offset| 否| String |偏移量，不填默认为0 |
| limit| 否 | String |返回数量，不填则默认 10，最大值20 |

## 3. 示例

输入：

```
 https://domain/v2/index.php?Action=ListAcl
  &instanceId=ckafka-tadfqa0
  &resourceType=2
  &resourceName=test-topic
  &operation=0
  &permissionType=3
  &host=*
  &<公共请求参数>
```

输出：

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data":{
    "totalCount":1
    "users":[
    {
        "userId":123,
        "name":"test",
        "ctime":"2018-01-01 15:32:12",
        "mtime":"2018-01-01 16:32:!2"
    }]
}

```
> 备注：该功能目前处于灰度测试阶段，如需要在控制台试用，请通过 提交工单的方式开通白名单。