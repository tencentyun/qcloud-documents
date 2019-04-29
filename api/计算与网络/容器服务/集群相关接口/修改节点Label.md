## 1. 接口描述
本接口 ( ModifyClusterNodeLabel ) 用于修改节点Label。 可配合创建/更新服务的nodeAffinity 参数设置节点的亲和性调度。
接口请求域名：`ccs.api.qcloud.com`。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。

| 参数名称 | 描述 |类型 | 必选  | 
|---------|---------|---------|---------
| clusterId   | 集群 ID，请填写 [查询集群列表](/doc/api/457/9448) 接口中返回的 clusterId 字段 | String |是 |
| instanceId   | 节点 ID | String |是 |
| labels   | 需要为节点打上的Label | Object Array |是 |

labels 参数详细说明：

| 字段 | 描述 |类型 |必选 |  
|---------|---------|---------|---------|
|key | Label 的 key值 | String |是 | 
|value | Label 的 value值 | String | 否 |

## 3. 输出参数
 
| 参数名称 | 描述 |类型 | 
|---------|---------|---------|
| code | 公共错误码。0 表示成功，其他值表示失败|Int | 
| codeDesc | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message |  模块错误信息描述，与接口相关|String |

## 4. 示例
输入
```
  https://domain/v2/index.php?Action=ModifyClusterNodeLabel
  ------------基础参数----------
  &clusterId=cls-xxxxx
  &instanceId=ins-xxx
  ------------Labels------------
  &labels.0.key=foo
  &labels.0.value=bar
  &labels.1.key=foo2
  &labels.1.value=bar2
 
  &其它公共参数
```
输出
```
  {
    "code": 0,
    "message": "", 
    "codeDesc": "Success"
}

```
