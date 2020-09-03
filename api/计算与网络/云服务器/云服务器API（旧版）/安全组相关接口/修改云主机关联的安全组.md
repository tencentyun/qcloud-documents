>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（ModifySecurityGroupsOfInstance）用于修改指定云服务器关联的安全组。(本接口将在合适时间下线，建议使用CVM::ModifyInstancesAttribute接口来替代本接口的功能)
接口请求域名：dfw.api.qcloud.com
1)此接口的操作以云服务器为索引，每个云服务器需要独立设置要关联到的安全组ID列表。
2)欠费的云服务器，或正在进行迁移、变更等流程中的云服务器不允许进行关联安全组操作，直到状态恢复正常。
3)对于绑定了多网卡云服务器，此接口修改云服务器的主网卡所关联的安全组,其他弹性网卡绑定的安全组保持不变。如果需要修改弹性网卡的安全组，请使用ModifySecurityGroupsOfNetworkInterface。
4)此接口调用后，新的安全组关联关系将覆盖云服务器之前的关联关联关系。假如您的云服务器现在关联了安全组A和B，希望再关联安全组C，但保留原来的A和B，则输入的sgIds参数需要包含A、B和C。移出某个安全组时，输入的sgIds参数需要包含剩余的安全组ID列表。
5)与安全组内规则类似，同一个云服务器关联的多个安全组有顺序，按照此接口中输入的sgIds顺序生效。当您的安全组规则内包含action = drop时，不同的顺序有可能带来不同的网络防护效果，需要谨慎修改。


## 2. 输入参数
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> instanceSet <td> 是 <td> Array <td> 云服务器关联安全组数据列表，不超过20个成员
</tbody></table> 
云服务器关联安全组数据字段
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> instanceId <td> 是 <td> String <td> 云服务器实例ID，将所传全部云服务器和所传安全组按顺序关联
<tr>
<td> sgIds <td> 是 <td> Array <td> 关联安全组唯一ID列表，关联顺序依sgIds成员顺序
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
</tbody></table>

## 4. 错误码表
 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>

<td> 7000 <td> 安全组后台异常
<tr>
<td> 7003 <td> 云服务器当前状态禁止关联
</tbody></table>
 

## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupsOfInstance
  &instanceSet.0.instanceId=ins-4q118hl2
  &instanceSet.0.sgIds.0=sg-1sdj39df
  &instanceSet.0.sgIds.1=sg-o8sk37is
  &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

