## 1. 接口描述
 
本接口 (ResetClusterAsgLabel) 用于重置集群伸缩组label，传入的label会完全替换伸缩组的已有label。

接口请求域名：<font style="color:red">ccs.api.qcloud.com</font>



## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://www.qcloud.com/document/api/457/9463)页面。

| 参数名称 | 描述 | 必选  | 类型 |
|---------|---------|---------|---------|
| clusterId   |集群ID，请填写[查询集群列表](https://www.qcloud.com/document/api/457/9448)接口中返回的clusterId字段。| 是    | String |
| autoScalingGroupId   |伸缩组ID| 是    | String |
| label   |label| 否    | Array |



## 3. 输出参数
 
| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码。0表示成功，其他值表示失败| Int |
| codeDesc |业务侧错误码。成功时返回Success，错误时返回具体业务错误原因。| String |
| message | 模块错误信息描述，与接口相关| String |



## 4. 示例

输入

```
  https://domain/v2/index.php?Action=ResetClusterAsgLabel
  &clusterId=cls-xxxxxxxx
  &autoScalingGroupId=asg-xxxxxxxx
  &label.key=val
  &其它公共参数
```
输出

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": null
}

```