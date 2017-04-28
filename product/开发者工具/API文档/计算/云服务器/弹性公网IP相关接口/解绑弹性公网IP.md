## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: EipUnBindInstance

弹性公网IP与服务器解绑。
>注：
平台对用户每地域每日解绑EIP重新分配普通公网IP次数有所限制（可参见<a href="/doc/product/213/1941" title="/doc/product/213/1941">EIP产品简介</a>）。上述配额可通过 <a href="http://www.qcloud.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D" title="DescribeEipQuota">DescribeEipQuota</a>接口获取。

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> eipId <td> 否 <td> String <td> EIP实例ID，可通过<a href="http://www.qcloud.com/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E5%88%97%E8%A1%A8" title="DescribeEipQuota">DescribeEip</a>接口返回字段中的 eipId获取
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
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td> 错误码, 0: 成功, 其他值: 失败，具体含义可以参考<a href="/document/product/213/6982" title="错误码">错误码</a>。
<tr>
<td> message <td> String <td> 错误信息
</tbody></table>

 

## 4. 示例
 
输入
```

  https://eip.api.qcloud.com/v2/index.php?
  &<公共请求参数>
  &eipId=eip-mksy14ay
  &allocWanIp=0

```

输出
```

{
    "code": 0,
    "message": ""
}

```

