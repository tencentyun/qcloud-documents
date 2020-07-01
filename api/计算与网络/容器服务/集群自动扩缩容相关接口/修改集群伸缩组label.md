>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>
## 接口描述

本接口（ModifyClusterAsgLabel）用于修改集群伸缩组 label，只修改传入 label 中对应的 key，label 中的原有 key 保持不变。

接口请求域名：
```
ccs.api.qcloud.com
```

## 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](https://cloud.tencent.com/document/api/457/9463) 页面。

| 参数名称 | 描述 | 必选  | 类型 |
|---------|---------|---------|---------|
| clusterId   |集群 ID，请填写 [查询集群列表](https://cloud.tencent.com/document/api/457/9448) 接口中返回的 clusterId 字段| 是    | String |  
| autoScalingGroupId   |伸缩组 ID| 是    | String |
| label   |label| 否    | Array |



## 输出参数
 
| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码。0 表示成功，其他值表示失败| Int |
| codeDesc |业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因| String |
| message | 模块错误信息描述，与接口相关| String |



## 示例

### 输入

```
  https://domain/v2/index.php?Action=ModifyClusterAsgLabel
  &clusterId=cls-xxxxxxxx
  &autoScalingGroupId=asg-xxxxxxxx
  &label.key=val
  &其它公共参数
```
### 输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}

```
