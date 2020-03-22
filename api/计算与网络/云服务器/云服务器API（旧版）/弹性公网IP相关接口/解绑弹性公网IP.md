>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: EipUnBindInstance

弹性公网IP与服务器解绑。
>注：
平台对用户每地域每日解绑EIP重新分配普通公网IP次数有所限制（可参见<a href="/doc/product/213/1941" title="/doc/product/213/1941">EIP产品简介</a>）。上述配额可通过 <a href="https://cloud.tencent.com/document/api/213/1378" title="DescribeEipQuota">DescribeEipQuota</a> 接口获取。

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> eipId <td> 否 <td> String <td> EIP实例ID，可通过<a href="https://cloud.tencent.com/document/api/213/1379" title="DescribeEipQuota">DescribeEip</a>接口返回字段中的 eipId获取
<tr>
<td> allocWanIp <td> 否 <td> Int <td> 弹性公网IP与服务器解绑后，是否需要为服务器的主网卡主IP重新分配新的普通公网IP。该普通公网IP随着服务器的释放而释放，不具备弹性。<br>0：不分配； 1：分配（默认为0）。
<tr>
<td> networkInterfaceId <td> 否 <td> String <td> 弹性网卡唯一ID，可通过<a href="/doc/api/245/4814" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a>接口返回字段中的networkInterfaceId获取
<tr>
<td> privateIpAddress <td> 否 <td> String <td> 服务器内网IP，解绑时或者传入参数eipId，或者传入参数networkInterfaceId和privateIpAddress
<tr>
<td> unBindPrivateIpWithEip <td> 否 <td> Int <td> 弹性公网IP与服务器解绑后，是否需要解除networkInterfaceId和privateIpAddress与EIP的关系。此参数仅对支持弹性网卡的服务器在非主网卡主IP解绑时有意义，其他默认解除。<br>0：不解除； 1：解除（默认为1）。
</tbody></table>

 

## 3. 输出参数
 

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。|
| message | String | 模块错误信息描述，与接口相关。|


 

## 4. 示例
 
输入
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &eipId=eip-mksy14ay
  &allocWanIp=0

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

