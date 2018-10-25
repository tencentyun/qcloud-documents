## 接口描述
本接口 ( CheckClusterCIDR ) 用于校验指定CIDR创建集群是否冲突。

接口请求域名：
```
ccs.api.qcloud.com
```


## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。


| 参数名称   | 描述                               | 类型     | 必选 |
|-----------|-----------------------------------|----------|------|
|   vpcId   | vpc统一资源ID | String | 是    |
|clusterCIDR| 使用此CIDR创建集群是否合法 | String | 是 |



## 输出参数
 
| 参数名称 | 描述 |类型 | 
|----------|------|-----|
| code |公共错误码。0 表示成功，其他值表示失败| Int | 
| message | 模块错误信息描述，与接口相关|String | 
| codeDesc | 业务错误码。成功时返回 Success，错误时返回具体业务错误原因|String |



## 示例
### 输入
```
  https://domain/v2/index.php?Action=CheckClusterCIDR
  &vpcId=vpc-ap4xxxxx
  &clusterCIDR=172.16.0.0/16
  &其它公共参数
```

### 输出
```
{
    "code":4000,
    "message":"(-10013)与同VPC其它集群CIDR冲突",
    "codeDesc":"ConflictWithOtherClusterCIDR"
}
```
