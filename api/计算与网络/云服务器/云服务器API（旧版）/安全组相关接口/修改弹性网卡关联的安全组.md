>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
本接口（ModifySecurityGroupsOfNetworkInterface）用于修改指定弹性网卡关联的安全组。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>
1)此接口的操作以网卡为索引，每个网卡需要独立设置要关联到的安全组ID列表。
2)此接口调用后，新的安全组关联关系将覆盖网卡之前的关联关联关系。假如您的网卡现在关联了安全组A和B，希望再关联安全组C，但保留原来的A和B，则输入的sgIds参数需要包含A、B和C。移出某个安全组时，输入的sgIds参数需要包含剩余的安全组ID列表。
3)与安全组内规则类似，同一个网卡关联的多个安全组有顺序，按照此接口中输入的sgIds顺序生效。当您的安全组规则内包含action = DROP时，不同的顺序有可能带来不同的网络防护效果，需要谨慎修改。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为ModifySecurityGroupsOfNetworkInterface。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> networkInterfaceSet <td> 是 <td> Array <td> 网卡关联安全组数据列表
</tbody></table> 

弹性网卡关联安全组数据字段
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> networkInterfaceId <td> 是 <td> String <td> 弹性网卡ID，将所传全部网卡和所传安全组按顺序关联
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
</tbody></table>

## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=ModifySecurityGroupsOfInstance
  &networkInterfaceSet.0.networkInterfaceId=eni-3056glfn
  &networkInterfaceSet.0.sgIds.0=sg-1sdj39df
  &networkInterfaceSet.0.sgIds.1=sg-o8sk37is
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```